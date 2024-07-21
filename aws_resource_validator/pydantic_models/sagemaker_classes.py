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
from aws_resource_validator.pydantic_models.sagemaker_constants import *

class ActionSourceTypeDef(BaseModel):
    SourceUri: str
    SourceType: Optional[str] = None
    SourceId: Optional[str] = None

class AddAssociationRequestRequestTypeDef(BaseModel):
    SourceArn: str
    DestinationArn: str
    AssociationType: Optional[AssociationEdgeTypeType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AdditionalS3DataSourceTypeDef(BaseModel):
    S3DataType: AdditionalS3DataSourceDataTypeType
    S3Uri: str
    CompressionType: Optional[CompressionTypeType] = None

class AgentVersionTypeDef(BaseModel):
    Version: str
    AgentCount: int

class AlarmTypeDef(BaseModel):
    AlarmName: Optional[str] = None

class MetricDefinitionTypeDef(BaseModel):
    Name: str
    Regex: str

class AlgorithmStatusItemTypeDef(BaseModel):
    Name: str
    Status: DetailedAlgorithmStatusType
    FailureReason: Optional[str] = None

class AlgorithmSummaryTypeDef(BaseModel):
    AlgorithmName: str
    AlgorithmArn: str
    CreationTime: datetime
    AlgorithmStatus: AlgorithmStatusType
    AlgorithmDescription: Optional[str] = None

class AmazonQSettingsTypeDef(BaseModel):
    Status: Optional[FeatureStatusType] = None
    QProfileArn: Optional[str] = None

class AnnotationConsolidationConfigTypeDef(BaseModel):
    AnnotationConsolidationLambdaArn: str

class ResourceSpecTypeDef(BaseModel):
    SageMakerImageArn: Optional[str] = None
    SageMakerImageVersionArn: Optional[str] = None
    SageMakerImageVersionAlias: Optional[str] = None
    InstanceType: Optional[AppInstanceTypeType] = None
    LifecycleConfigArn: Optional[str] = None

class AppSpecificationExtraOutputTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None

class AppSpecificationOutputTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None

class AppSpecificationTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None

class ArtifactSourceTypeTypeDef(BaseModel):
    SourceIdType: ArtifactSourceIdTypeType
    Value: str

class AssociateTrialComponentRequestRequestTypeDef(BaseModel):
    TrialComponentName: str
    TrialName: str

class AsyncInferenceClientConfigTypeDef(BaseModel):
    MaxConcurrentInvocationsPerInstance: Optional[int] = None

class AsyncInferenceNotificationConfigOutputTypeDef(BaseModel):
    SuccessTopic: Optional[str] = None
    ErrorTopic: Optional[str] = None
    IncludeInferenceResponseIn: Optional[List[AsyncNotificationTopicTypesType]] = None

class AsyncInferenceNotificationConfigTypeDef(BaseModel):
    SuccessTopic: Optional[str] = None
    ErrorTopic: Optional[str] = None
    IncludeInferenceResponseIn: Optional[Sequence[AsyncNotificationTopicTypesType]] = None

class AthenaDatasetDefinitionTypeDef(BaseModel):
    Catalog: str
    Database: str
    QueryString: str
    OutputS3Uri: str
    OutputFormat: AthenaResultFormatType
    WorkGroup: Optional[str] = None
    KmsKeyId: Optional[str] = None
    OutputCompression: Optional[AthenaResultCompressionTypeType] = None

class AutoMLAlgorithmConfigOutputTypeDef(BaseModel):
    AutoMLAlgorithms: List[AutoMLAlgorithmType]

class AutoMLAlgorithmConfigTypeDef(BaseModel):
    AutoMLAlgorithms: Sequence[AutoMLAlgorithmType]

class AutoMLCandidateStepTypeDef(BaseModel):
    CandidateStepType: CandidateStepTypeType
    CandidateStepArn: str
    CandidateStepName: str

class AutoMLContainerDefinitionTypeDef(BaseModel):
    Image: str
    ModelDataUrl: str
    Environment: Optional[Dict[str, str]] = None

class FinalAutoMLJobObjectiveMetricTypeDef(BaseModel):
    MetricName: AutoMLMetricEnumType
    Value: float
    Type: Optional[AutoMLJobObjectiveTypeType] = None
    StandardMetricName: Optional[AutoMLMetricEnumType] = None

class AutoMLS3DataSourceTypeDef(BaseModel):
    S3DataType: AutoMLS3DataTypeType
    S3Uri: str

class AutoMLDataSplitConfigTypeDef(BaseModel):
    ValidationFraction: Optional[float] = None

class AutoMLJobArtifactsTypeDef(BaseModel):
    CandidateDefinitionNotebookLocation: Optional[str] = None
    DataExplorationNotebookLocation: Optional[str] = None

class AutoMLJobCompletionCriteriaTypeDef(BaseModel):
    MaxCandidates: Optional[int] = None
    MaxRuntimePerTrainingJobInSeconds: Optional[int] = None
    MaxAutoMLJobRuntimeInSeconds: Optional[int] = None

class AutoMLJobObjectiveTypeDef(BaseModel):
    MetricName: AutoMLMetricEnumType

class AutoMLJobStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None

class AutoMLPartialFailureReasonTypeDef(BaseModel):
    PartialFailureMessage: Optional[str] = None

class AutoMLOutputDataConfigTypeDef(BaseModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None

class TabularResolvedAttributesTypeDef(BaseModel):
    ProblemType: Optional[ProblemTypeType] = None

class TextGenerationResolvedAttributesTypeDef(BaseModel):
    BaseModelName: Optional[str] = None

class VpcConfigOutputTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class VpcConfigTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class AutoParameterTypeDef(BaseModel):
    Name: str
    ValueHint: str

class AutotuneTypeDef(BaseModel):
    Mode: Literal["Enabled"]

class BatchDataCaptureConfigTypeDef(BaseModel):
    DestinationS3Uri: str
    KmsKeyId: Optional[str] = None
    GenerateInferenceId: Optional[bool] = None

class BatchDescribeModelPackageErrorTypeDef(BaseModel):
    ErrorCode: str
    ErrorResponse: str

class BatchDescribeModelPackageInputRequestTypeDef(BaseModel):
    ModelPackageArnList: Sequence[str]

class BestObjectiveNotImprovingTypeDef(BaseModel):
    MaxNumberOfTrainingJobsNotImproving: Optional[int] = None

class MetricsSourceTypeDef(BaseModel):
    ContentType: str
    S3Uri: str
    ContentDigest: Optional[str] = None

class CacheHitResultTypeDef(BaseModel):
    SourcePipelineExecutionArn: Optional[str] = None

class OutputParameterTypeDef(BaseModel):
    Name: str
    Value: str

class CandidateArtifactLocationsTypeDef(BaseModel):
    Explainability: str
    ModelInsights: Optional[str] = None
    BacktestResults: Optional[str] = None

class MetricDatumTypeDef(BaseModel):
    MetricName: Optional[AutoMLMetricEnumType] = None
    Value: Optional[float] = None
    Set: Optional[MetricSetSourceType] = None
    StandardMetricName: Optional[AutoMLMetricExtendedEnumType] = None

class DirectDeploySettingsTypeDef(BaseModel):
    Status: Optional[FeatureStatusType] = None

class GenerativeAiSettingsTypeDef(BaseModel):
    AmazonBedrockRoleArn: Optional[str] = None

class IdentityProviderOAuthSettingTypeDef(BaseModel):
    DataSourceName: Optional[DataSourceNameType] = None
    Status: Optional[FeatureStatusType] = None
    SecretArn: Optional[str] = None

class KendraSettingsTypeDef(BaseModel):
    Status: Optional[FeatureStatusType] = None

class ModelRegisterSettingsTypeDef(BaseModel):
    Status: Optional[FeatureStatusType] = None
    CrossAccountModelRegisterRoleArn: Optional[str] = None

class TimeSeriesForecastingSettingsTypeDef(BaseModel):
    Status: Optional[FeatureStatusType] = None
    AmazonForecastRoleArn: Optional[str] = None

class WorkspaceSettingsTypeDef(BaseModel):
    S3ArtifactPath: Optional[str] = None
    S3KmsKeyId: Optional[str] = None

class CapacitySizeTypeDef(BaseModel):
    Type: CapacitySizeTypeType
    Value: int

class CaptureContentTypeHeaderOutputTypeDef(BaseModel):
    CsvContentTypes: Optional[List[str]] = None
    JsonContentTypes: Optional[List[str]] = None

class CaptureContentTypeHeaderTypeDef(BaseModel):
    CsvContentTypes: Optional[Sequence[str]] = None
    JsonContentTypes: Optional[Sequence[str]] = None

class CaptureOptionTypeDef(BaseModel):
    CaptureMode: CaptureModeType

class CategoricalParameterOutputTypeDef(BaseModel):
    Name: str
    Value: List[str]

class CategoricalParameterRangeExtraOutputTypeDef(BaseModel):
    Name: str
    Values: List[str]

class CategoricalParameterRangeOutputTypeDef(BaseModel):
    Name: str
    Values: List[str]

class CategoricalParameterRangeSpecificationOutputTypeDef(BaseModel):
    Values: List[str]

class CategoricalParameterRangeSpecificationTypeDef(BaseModel):
    Values: Sequence[str]

class CategoricalParameterRangeTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class CategoricalParameterTypeDef(BaseModel):
    Name: str
    Value: Sequence[str]

class ShuffleConfigTypeDef(BaseModel):
    Seed: int

class ChannelSpecificationOutputTypeDef(BaseModel):
    Name: str
    SupportedContentTypes: List[str]
    SupportedInputModes: List[TrainingInputModeType]
    Description: Optional[str] = None
    IsRequired: Optional[bool] = None
    SupportedCompressionTypes: Optional[List[CompressionTypeType]] = None

class ChannelSpecificationTypeDef(BaseModel):
    Name: str
    SupportedContentTypes: Sequence[str]
    SupportedInputModes: Sequence[TrainingInputModeType]
    Description: Optional[str] = None
    IsRequired: Optional[bool] = None
    SupportedCompressionTypes: Optional[Sequence[CompressionTypeType]] = None

class CheckpointConfigTypeDef(BaseModel):
    S3Uri: str
    LocalPath: Optional[str] = None

class ClarifyCheckStepMetadataTypeDef(BaseModel):
    CheckType: Optional[str] = None
    BaselineUsedForDriftCheckConstraints: Optional[str] = None
    CalculatedBaselineConstraints: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ViolationReport: Optional[str] = None
    CheckJobArn: Optional[str] = None
    SkipCheck: Optional[bool] = None
    RegisterNewBaseline: Optional[bool] = None

class ClarifyInferenceConfigOutputTypeDef(BaseModel):
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

class ClarifyInferenceConfigTypeDef(BaseModel):
    FeaturesAttribute: Optional[str] = None
    ContentTemplate: Optional[str] = None
    MaxRecordCount: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    ProbabilityIndex: Optional[int] = None
    LabelIndex: Optional[int] = None
    ProbabilityAttribute: Optional[str] = None
    LabelAttribute: Optional[str] = None
    LabelHeaders: Optional[Sequence[str]] = None
    FeatureHeaders: Optional[Sequence[str]] = None
    FeatureTypes: Optional[Sequence[ClarifyFeatureTypeType]] = None

class ClarifyShapBaselineConfigTypeDef(BaseModel):
    MimeType: Optional[str] = None
    ShapBaseline: Optional[str] = None
    ShapBaselineUri: Optional[str] = None

class ClarifyTextConfigTypeDef(BaseModel):
    Language: ClarifyTextLanguageType
    Granularity: ClarifyTextGranularityType

class ClusterEbsVolumeConfigTypeDef(BaseModel):
    VolumeSizeInGB: int

class ClusterLifeCycleConfigTypeDef(BaseModel):
    SourceS3Uri: str
    OnCreate: str

class ClusterInstancePlacementTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None

class ClusterInstanceStatusDetailsTypeDef(BaseModel):
    Status: ClusterInstanceStatusType
    Message: Optional[str] = None

class ClusterSummaryTypeDef(BaseModel):
    ClusterArn: str
    ClusterName: str
    CreationTime: datetime
    ClusterStatus: ClusterStatusType

class ContainerConfigExtraOutputTypeDef(BaseModel):
    ContainerArguments: Optional[List[str]] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerEnvironmentVariables: Optional[Dict[str, str]] = None

class FileSystemConfigTypeDef(BaseModel):
    MountPath: Optional[str] = None
    DefaultUid: Optional[int] = None
    DefaultGid: Optional[int] = None

class ContainerConfigOutputTypeDef(BaseModel):
    ContainerArguments: Optional[List[str]] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerEnvironmentVariables: Optional[Dict[str, str]] = None

class ContainerConfigTypeDef(BaseModel):
    ContainerArguments: Optional[Sequence[str]] = None
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerEnvironmentVariables: Optional[Mapping[str, str]] = None

class CustomImageTypeDef(BaseModel):
    ImageName: str
    AppImageConfigName: str
    ImageVersionNumber: Optional[int] = None

class GitConfigTypeDef(BaseModel):
    RepositoryUrl: str
    Branch: Optional[str] = None
    SecretArn: Optional[str] = None

class CodeRepositoryTypeDef(BaseModel):
    RepositoryUrl: str

class CognitoConfigTypeDef(BaseModel):
    UserPool: str
    ClientId: str

class CognitoMemberDefinitionTypeDef(BaseModel):
    UserPool: str
    UserGroup: str
    ClientId: str

class VectorConfigTypeDef(BaseModel):
    Dimension: int

class CollectionConfigurationExtraOutputTypeDef(BaseModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Dict[str, str]] = None

class CollectionConfigurationOutputTypeDef(BaseModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Dict[str, str]] = None

class CollectionConfigurationTypeDef(BaseModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Mapping[str, str]] = None

class CompilationJobSummaryTypeDef(BaseModel):
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

class ConditionStepMetadataTypeDef(BaseModel):
    Outcome: Optional[ConditionOutcomeType] = None

class MultiModelConfigTypeDef(BaseModel):
    ModelCacheSetting: Optional[ModelCacheSettingType] = None

class ContextSourceTypeDef(BaseModel):
    SourceUri: str
    SourceType: Optional[str] = None
    SourceId: Optional[str] = None

class ContinuousParameterRangeSpecificationTypeDef(BaseModel):
    MinValue: str
    MaxValue: str

class ContinuousParameterRangeTypeDef(BaseModel):
    Name: str
    MinValue: str
    MaxValue: str
    ScalingType: Optional[HyperParameterScalingTypeType] = None

class ConvergenceDetectedTypeDef(BaseModel):
    CompleteOnConvergence: Optional[CompleteOnConvergenceType] = None

class MetadataPropertiesTypeDef(BaseModel):
    CommitId: Optional[str] = None
    Repository: Optional[str] = None
    GeneratedBy: Optional[str] = None
    ProjectId: Optional[str] = None

class ModelDeployConfigTypeDef(BaseModel):
    AutoGenerateEndpointName: Optional[bool] = None
    EndpointName: Optional[str] = None

class InputConfigTypeDef(BaseModel):
    S3Uri: str
    Framework: FrameworkType
    DataInputConfig: Optional[str] = None
    FrameworkVersion: Optional[str] = None

class NeoVpcConfigTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class StoppingConditionTypeDef(BaseModel):
    MaxRuntimeInSeconds: Optional[int] = None
    MaxWaitTimeInSeconds: Optional[int] = None
    MaxPendingTimeInSeconds: Optional[int] = None

class DataQualityAppSpecificationTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    Environment: Optional[Mapping[str, str]] = None

class MonitoringStoppingConditionTypeDef(BaseModel):
    MaxRuntimeInSeconds: int

class EdgeOutputConfigTypeDef(BaseModel):
    S3OutputLocation: str
    KmsKeyId: Optional[str] = None
    PresetDeploymentType: Optional[Literal["GreengrassV2Component"]] = None
    PresetDeploymentConfig: Optional[str] = None

class EdgeDeploymentModelConfigTypeDef(BaseModel):
    ModelHandle: str
    EdgePackagingJobName: str

class ThroughputConfigTypeDef(BaseModel):
    ThroughputMode: ThroughputModeType
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None

class FlowDefinitionOutputConfigTypeDef(BaseModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None

class HumanLoopRequestSourceTypeDef(BaseModel):
    AwsManagedHumanLoopRequestSource: AwsManagedHumanLoopRequestSourceType

class HubS3StorageConfigTypeDef(BaseModel):
    S3OutputPath: Optional[str] = None

class UiTemplateTypeDef(BaseModel):
    Content: str

class CreateImageVersionRequestRequestTypeDef(BaseModel):
    BaseImage: str
    ClientToken: str
    ImageName: str
    Aliases: Optional[Sequence[str]] = None
    VendorGuidance: Optional[VendorGuidanceType] = None
    JobType: Optional[JobTypeType] = None
    MLFramework: Optional[str] = None
    ProgrammingLang: Optional[str] = None
    Processor: Optional[ProcessorType] = None
    Horovod: Optional[bool] = None
    ReleaseNotes: Optional[str] = None

class InferenceComponentRuntimeConfigTypeDef(BaseModel):
    CopyCount: int

class LabelingJobOutputConfigTypeDef(BaseModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None
    SnsTopicArn: Optional[str] = None

class LabelingJobStoppingConditionsTypeDef(BaseModel):
    MaxHumanLabeledObjectCount: Optional[int] = None
    MaxPercentageOfInputDatasetLabeled: Optional[int] = None

class ModelBiasAppSpecificationTypeDef(BaseModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Mapping[str, str]] = None

class ModelCardExportOutputConfigTypeDef(BaseModel):
    S3OutputPath: str

class ModelCardSecurityConfigTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None

class ModelExplainabilityAppSpecificationTypeDef(BaseModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Mapping[str, str]] = None

class InferenceExecutionConfigTypeDef(BaseModel):
    Mode: InferenceExecutionModeType

class ModelPackageModelCardTypeDef(BaseModel):
    ModelCardContent: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None

class ModelPackageSecurityConfigTypeDef(BaseModel):
    KmsKeyId: str

class ModelQualityAppSpecificationTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    ProblemType: Optional[MonitoringProblemTypeType] = None
    Environment: Optional[Mapping[str, str]] = None

class InstanceMetadataServiceConfigurationTypeDef(BaseModel):
    MinimumInstanceMetadataServiceVersion: str

class NotebookInstanceLifecycleHookTypeDef(BaseModel):
    Content: Optional[str] = None

class OptimizationJobOutputConfigTypeDef(BaseModel):
    S3OutputLocation: str
    KmsKeyId: Optional[str] = None

class OptimizationVpcConfigTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class ParallelismConfigurationTypeDef(BaseModel):
    MaxParallelExecutionSteps: int

class PipelineDefinitionS3LocationTypeDef(BaseModel):
    Bucket: str
    ObjectKey: str
    VersionId: Optional[str] = None

class CreatePresignedDomainUrlRequestRequestTypeDef(BaseModel):
    DomainId: str
    UserProfileName: str
    SessionExpirationDurationInSeconds: Optional[int] = None
    ExpiresInSeconds: Optional[int] = None
    SpaceName: Optional[str] = None
    LandingUri: Optional[str] = None

class CreatePresignedMlflowTrackingServerUrlRequestRequestTypeDef(BaseModel):
    TrackingServerName: str
    ExpiresInSeconds: Optional[int] = None
    SessionExpirationDurationInSeconds: Optional[int] = None

class CreatePresignedNotebookInstanceUrlInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str
    SessionExpirationDurationInSeconds: Optional[int] = None

class ExperimentConfigTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    TrialComponentDisplayName: Optional[str] = None
    RunName: Optional[str] = None

class ProcessingStoppingConditionTypeDef(BaseModel):
    MaxRuntimeInSeconds: int

class OwnershipSettingsTypeDef(BaseModel):
    OwnerUserProfileName: str

class SpaceSharingSettingsTypeDef(BaseModel):
    SharingType: SharingTypeType

class InfraCheckConfigTypeDef(BaseModel):
    EnableInfraCheck: Optional[bool] = None

class OutputDataConfigTypeDef(BaseModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None
    CompressionType: Optional[OutputCompressionTypeType] = None

class ProfilerConfigTypeDef(BaseModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Mapping[str, str]] = None
    DisableProfiler: Optional[bool] = None

class RemoteDebugConfigTypeDef(BaseModel):
    EnableRemoteDebug: Optional[bool] = None

class RetryStrategyTypeDef(BaseModel):
    MaximumRetryAttempts: int

class SessionChainingConfigTypeDef(BaseModel):
    EnableSessionTagChaining: Optional[bool] = None

class TensorBoardOutputConfigTypeDef(BaseModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None

class DataProcessingTypeDef(BaseModel):
    InputFilter: Optional[str] = None
    OutputFilter: Optional[str] = None
    JoinSource: Optional[JoinSourceType] = None

class ModelClientConfigTypeDef(BaseModel):
    InvocationsTimeoutInSeconds: Optional[int] = None
    InvocationsMaxRetries: Optional[int] = None

class TransformOutputTypeDef(BaseModel):
    S3OutputPath: str
    Accept: Optional[str] = None
    AssembleWith: Optional[AssemblyTypeType] = None
    KmsKeyId: Optional[str] = None

class TransformResourcesTypeDef(BaseModel):
    InstanceType: TransformInstanceTypeType
    InstanceCount: int
    VolumeKmsKeyId: Optional[str] = None

class TrialComponentArtifactTypeDef(BaseModel):
    Value: str
    MediaType: Optional[str] = None

class TrialComponentParameterValueTypeDef(BaseModel):
    StringValue: Optional[str] = None
    NumberValue: Optional[float] = None

class TrialComponentStatusTypeDef(BaseModel):
    PrimaryStatus: Optional[TrialComponentPrimaryStatusType] = None
    Message: Optional[str] = None

class OidcConfigTypeDef(BaseModel):
    ClientId: str
    ClientSecret: str
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    LogoutEndpoint: str
    JwksUri: str
    Scope: Optional[str] = None
    AuthenticationRequestExtraParams: Optional[Mapping[str, str]] = None

class SourceIpConfigTypeDef(BaseModel):
    Cidrs: Sequence[str]

class WorkforceVpcConfigRequestTypeDef(BaseModel):
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None

class NotificationConfigurationTypeDef(BaseModel):
    NotificationTopicArn: Optional[str] = None

class EFSFileSystemConfigTypeDef(BaseModel):
    FileSystemId: str
    FileSystemPath: Optional[str] = None

class EFSFileSystemTypeDef(BaseModel):
    FileSystemId: str

class CustomPosixUserConfigTypeDef(BaseModel):
    Uid: int
    Gid: int

class CustomizedMetricSpecificationTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None

class DataCaptureConfigSummaryTypeDef(BaseModel):
    EnableCapture: bool
    CaptureStatus: CaptureStatusType
    CurrentSamplingPercentage: int
    DestinationS3Uri: str
    KmsKeyId: str

class DataCatalogConfigTypeDef(BaseModel):
    TableName: str
    Catalog: str
    Database: str

class DataQualityAppSpecificationOutputTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None

class MonitoringConstraintsResourceTypeDef(BaseModel):
    S3Uri: Optional[str] = None

class MonitoringStatisticsResourceTypeDef(BaseModel):
    S3Uri: Optional[str] = None

class EndpointInputTypeDef(BaseModel):
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

class FileSystemDataSourceTypeDef(BaseModel):
    FileSystemId: str
    FileSystemAccessMode: FileSystemAccessModeType
    FileSystemType: FileSystemTypeType
    DirectoryPath: str

class S3DataSourceExtraOutputTypeDef(BaseModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[List[str]] = None
    InstanceGroupNames: Optional[List[str]] = None

class S3DataSourceOutputTypeDef(BaseModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[List[str]] = None
    InstanceGroupNames: Optional[List[str]] = None

class S3DataSourceTypeDef(BaseModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[Sequence[str]] = None
    InstanceGroupNames: Optional[Sequence[str]] = None

class RedshiftDatasetDefinitionTypeDef(BaseModel):
    ClusterId: str
    Database: str
    DbUser: str
    QueryString: str
    ClusterRoleArn: str
    OutputS3Uri: str
    OutputFormat: RedshiftResultFormatType
    KmsKeyId: Optional[str] = None
    OutputCompression: Optional[RedshiftResultCompressionTypeType] = None

class DebugRuleConfigurationExtraOutputTypeDef(BaseModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None

class DebugRuleConfigurationOutputTypeDef(BaseModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None

class DebugRuleConfigurationTypeDef(BaseModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Mapping[str, str]] = None

class DebugRuleEvaluationStatusTypeDef(BaseModel):
    RuleConfigurationName: Optional[str] = None
    RuleEvaluationJobArn: Optional[str] = None
    RuleEvaluationStatus: Optional[RuleEvaluationStatusType] = None
    StatusDetails: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class DefaultEbsStorageSettingsTypeDef(BaseModel):
    DefaultEbsVolumeSizeInGb: int
    MaximumEbsVolumeSizeInGb: int

class DeleteActionRequestRequestTypeDef(BaseModel):
    ActionName: str

class DeleteAlgorithmInputRequestTypeDef(BaseModel):
    AlgorithmName: str

class DeleteAppImageConfigRequestRequestTypeDef(BaseModel):
    AppImageConfigName: str

class DeleteAppRequestRequestTypeDef(BaseModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None

class DeleteAssociationRequestRequestTypeDef(BaseModel):
    SourceArn: str
    DestinationArn: str

class DeleteClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str

class DeleteCodeRepositoryInputRequestTypeDef(BaseModel):
    CodeRepositoryName: str

class DeleteCompilationJobRequestRequestTypeDef(BaseModel):
    CompilationJobName: str

class DeleteContextRequestRequestTypeDef(BaseModel):
    ContextName: str

class DeleteDataQualityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class DeleteDeviceFleetRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str

class RetentionPolicyTypeDef(BaseModel):
    HomeEfsFileSystem: Optional[RetentionTypeType] = None

class DeleteEdgeDeploymentPlanRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str

class DeleteEdgeDeploymentStageRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    StageName: str

class DeleteEndpointConfigInputRequestTypeDef(BaseModel):
    EndpointConfigName: str

class DeleteEndpointInputRequestTypeDef(BaseModel):
    EndpointName: str

class DeleteExperimentRequestRequestTypeDef(BaseModel):
    ExperimentName: str

class DeleteFeatureGroupRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str

class DeleteFlowDefinitionRequestRequestTypeDef(BaseModel):
    FlowDefinitionName: str

class DeleteHubContentReferenceRequestRequestTypeDef(BaseModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str

class DeleteHubContentRequestRequestTypeDef(BaseModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: str

class DeleteHubRequestRequestTypeDef(BaseModel):
    HubName: str

class DeleteHumanTaskUiRequestRequestTypeDef(BaseModel):
    HumanTaskUiName: str

class DeleteHyperParameterTuningJobRequestRequestTypeDef(BaseModel):
    HyperParameterTuningJobName: str

class DeleteImageRequestRequestTypeDef(BaseModel):
    ImageName: str

class DeleteImageVersionRequestRequestTypeDef(BaseModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None

class DeleteInferenceComponentInputRequestTypeDef(BaseModel):
    InferenceComponentName: str

class DeleteInferenceExperimentRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteMlflowTrackingServerRequestRequestTypeDef(BaseModel):
    TrackingServerName: str

class DeleteModelBiasJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class DeleteModelCardRequestRequestTypeDef(BaseModel):
    ModelCardName: str

class DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class DeleteModelInputRequestTypeDef(BaseModel):
    ModelName: str

class DeleteModelPackageGroupInputRequestTypeDef(BaseModel):
    ModelPackageGroupName: str

class DeleteModelPackageGroupPolicyInputRequestTypeDef(BaseModel):
    ModelPackageGroupName: str

class DeleteModelPackageInputRequestTypeDef(BaseModel):
    ModelPackageName: str

class DeleteModelQualityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class DeleteMonitoringScheduleRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str

class DeleteNotebookInstanceInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str

class DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigName: str

class DeleteOptimizationJobRequestRequestTypeDef(BaseModel):
    OptimizationJobName: str

class DeletePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str
    ClientRequestToken: str

class DeleteProjectInputRequestTypeDef(BaseModel):
    ProjectName: str

class DeleteSpaceRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpaceName: str

class DeleteStudioLifecycleConfigRequestRequestTypeDef(BaseModel):
    StudioLifecycleConfigName: str

class DeleteTagsInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class DeleteTrialComponentRequestRequestTypeDef(BaseModel):
    TrialComponentName: str

class DeleteTrialRequestRequestTypeDef(BaseModel):
    TrialName: str

class DeleteUserProfileRequestRequestTypeDef(BaseModel):
    DomainId: str
    UserProfileName: str

class DeleteWorkforceRequestRequestTypeDef(BaseModel):
    WorkforceName: str

class DeleteWorkteamRequestRequestTypeDef(BaseModel):
    WorkteamName: str

class DeployedImageTypeDef(BaseModel):
    SpecifiedImage: Optional[str] = None
    ResolvedImage: Optional[str] = None
    ResolutionTime: Optional[datetime] = None

class RealTimeInferenceRecommendationTypeDef(BaseModel):
    RecommendationId: str
    InstanceType: ProductionVariantInstanceTypeType
    Environment: Optional[Dict[str, str]] = None

class DeviceSelectionConfigOutputTypeDef(BaseModel):
    DeviceSubsetType: DeviceSubsetTypeType
    Percentage: Optional[int] = None
    DeviceNames: Optional[List[str]] = None
    DeviceNameContains: Optional[str] = None

class EdgeDeploymentConfigTypeDef(BaseModel):
    FailureHandlingPolicy: FailureHandlingPolicyType

class EdgeDeploymentStatusTypeDef(BaseModel):
    StageStatus: StageStatusType
    EdgeDeploymentSuccessInStage: int
    EdgeDeploymentPendingInStage: int
    EdgeDeploymentFailedInStage: int
    EdgeDeploymentStatusMessage: Optional[str] = None
    EdgeDeploymentStageStartTime: Optional[datetime] = None

class DeviceSelectionConfigTypeDef(BaseModel):
    DeviceSubsetType: DeviceSubsetTypeType
    Percentage: Optional[int] = None
    DeviceNames: Optional[Sequence[str]] = None
    DeviceNameContains: Optional[str] = None

class DeregisterDevicesRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str
    DeviceNames: Sequence[str]

class DerivedInformationTypeDef(BaseModel):
    DerivedDataInputConfig: Optional[str] = None

class DescribeActionRequestRequestTypeDef(BaseModel):
    ActionName: str

class DescribeAlgorithmInputRequestTypeDef(BaseModel):
    AlgorithmName: str

class DescribeAppImageConfigRequestRequestTypeDef(BaseModel):
    AppImageConfigName: str

class DescribeAppRequestRequestTypeDef(BaseModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None

class DescribeArtifactRequestRequestTypeDef(BaseModel):
    ArtifactArn: str

class DescribeAutoMLJobRequestRequestTypeDef(BaseModel):
    AutoMLJobName: str

class ModelDeployResultTypeDef(BaseModel):
    EndpointName: Optional[str] = None

class DescribeAutoMLJobV2RequestRequestTypeDef(BaseModel):
    AutoMLJobName: str

class DescribeClusterNodeRequestRequestTypeDef(BaseModel):
    ClusterName: str
    NodeId: str

class DescribeClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str

class DescribeCodeRepositoryInputRequestTypeDef(BaseModel):
    CodeRepositoryName: str

class DescribeCompilationJobRequestRequestTypeDef(BaseModel):
    CompilationJobName: str

class ModelArtifactsTypeDef(BaseModel):
    S3ModelArtifacts: str

class ModelDigestsTypeDef(BaseModel):
    ArtifactDigest: Optional[str] = None

class NeoVpcConfigOutputTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class DescribeContextRequestRequestTypeDef(BaseModel):
    ContextName: str

class DescribeDataQualityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class DescribeDeviceFleetRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str

class DescribeDeviceRequestRequestTypeDef(BaseModel):
    DeviceName: str
    DeviceFleetName: str
    NextToken: Optional[str] = None

class EdgeModelTypeDef(BaseModel):
    ModelName: str
    ModelVersion: str
    LatestSampleTime: Optional[datetime] = None
    LatestInference: Optional[datetime] = None

class DescribeDomainRequestRequestTypeDef(BaseModel):
    DomainId: str

class DescribeEdgeDeploymentPlanRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEdgePackagingJobRequestRequestTypeDef(BaseModel):
    EdgePackagingJobName: str

class EdgePresetDeploymentOutputTypeDef(BaseModel):
    Type: Literal["GreengrassV2Component"]
    Artifact: Optional[str] = None
    Status: Optional[EdgePresetDeploymentStatusType] = None
    StatusMessage: Optional[str] = None

class DescribeEndpointConfigInputRequestTypeDef(BaseModel):
    EndpointConfigName: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeEndpointInputRequestTypeDef(BaseModel):
    EndpointName: str

class DescribeExperimentRequestRequestTypeDef(BaseModel):
    ExperimentName: str

class ExperimentSourceTypeDef(BaseModel):
    SourceArn: str
    SourceType: Optional[str] = None

class DescribeFeatureGroupRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    NextToken: Optional[str] = None

class LastUpdateStatusTypeDef(BaseModel):
    Status: LastUpdateStatusValueType
    FailureReason: Optional[str] = None

class OfflineStoreStatusTypeDef(BaseModel):
    Status: OfflineStoreStatusValueType
    BlockedReason: Optional[str] = None

class ThroughputConfigDescriptionTypeDef(BaseModel):
    ThroughputMode: ThroughputModeType
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None

class DescribeFeatureMetadataRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    FeatureName: str

class FeatureParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DescribeFlowDefinitionRequestRequestTypeDef(BaseModel):
    FlowDefinitionName: str

class DescribeHubContentRequestRequestTypeDef(BaseModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: Optional[str] = None

class HubContentDependencyTypeDef(BaseModel):
    DependencyOriginPath: Optional[str] = None
    DependencyCopyPath: Optional[str] = None

class DescribeHubRequestRequestTypeDef(BaseModel):
    HubName: str

class DescribeHumanTaskUiRequestRequestTypeDef(BaseModel):
    HumanTaskUiName: str

class UiTemplateInfoTypeDef(BaseModel):
    Url: Optional[str] = None
    ContentSha256: Optional[str] = None

class DescribeHyperParameterTuningJobRequestRequestTypeDef(BaseModel):
    HyperParameterTuningJobName: str

class HyperParameterTuningJobCompletionDetailsTypeDef(BaseModel):
    NumberOfTrainingJobsObjectiveNotImproving: Optional[int] = None
    ConvergenceDetectedTime: Optional[datetime] = None

class HyperParameterTuningJobConsumedResourcesTypeDef(BaseModel):
    RuntimeInSeconds: Optional[int] = None

class ObjectiveStatusCountersTypeDef(BaseModel):
    Succeeded: Optional[int] = None
    Pending: Optional[int] = None
    Failed: Optional[int] = None

class TrainingJobStatusCountersTypeDef(BaseModel):
    Completed: Optional[int] = None
    InProgress: Optional[int] = None
    RetryableError: Optional[int] = None
    NonRetryableError: Optional[int] = None
    Stopped: Optional[int] = None

class DescribeImageRequestRequestTypeDef(BaseModel):
    ImageName: str

class DescribeImageVersionRequestRequestTypeDef(BaseModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None

class DescribeInferenceComponentInputRequestTypeDef(BaseModel):
    InferenceComponentName: str

class InferenceComponentRuntimeConfigSummaryTypeDef(BaseModel):
    DesiredCopyCount: Optional[int] = None
    CurrentCopyCount: Optional[int] = None

class DescribeInferenceExperimentRequestRequestTypeDef(BaseModel):
    Name: str

class EndpointMetadataTypeDef(BaseModel):
    EndpointName: str
    EndpointConfigName: Optional[str] = None
    EndpointStatus: Optional[EndpointStatusType] = None
    FailureReason: Optional[str] = None

class InferenceExperimentScheduleOutputTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class DescribeInferenceRecommendationsJobRequestRequestTypeDef(BaseModel):
    JobName: str

class DescribeLabelingJobRequestRequestTypeDef(BaseModel):
    LabelingJobName: str

class LabelCountersTypeDef(BaseModel):
    TotalLabeled: Optional[int] = None
    HumanLabeled: Optional[int] = None
    MachineLabeled: Optional[int] = None
    FailedNonRetryableError: Optional[int] = None
    Unlabeled: Optional[int] = None

class LabelingJobOutputTypeDef(BaseModel):
    OutputDatasetS3Uri: str
    FinalActiveLearningModelArn: Optional[str] = None

class DescribeLineageGroupRequestRequestTypeDef(BaseModel):
    LineageGroupName: str

class DescribeMlflowTrackingServerRequestRequestTypeDef(BaseModel):
    TrackingServerName: str

class DescribeModelBiasJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class ModelBiasAppSpecificationOutputTypeDef(BaseModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None

class DescribeModelCardExportJobRequestRequestTypeDef(BaseModel):
    ModelCardExportJobArn: str

class ModelCardExportArtifactsTypeDef(BaseModel):
    S3ExportArtifacts: str

class DescribeModelCardRequestRequestTypeDef(BaseModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None

class DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class ModelExplainabilityAppSpecificationOutputTypeDef(BaseModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None

class DescribeModelInputRequestTypeDef(BaseModel):
    ModelName: str

class DescribeModelPackageGroupInputRequestTypeDef(BaseModel):
    ModelPackageGroupName: str

class DescribeModelPackageInputRequestTypeDef(BaseModel):
    ModelPackageName: str

class DescribeModelQualityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str

class ModelQualityAppSpecificationOutputTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    ProblemType: Optional[MonitoringProblemTypeType] = None
    Environment: Optional[Dict[str, str]] = None

class DescribeMonitoringScheduleRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str

class MonitoringExecutionSummaryTypeDef(BaseModel):
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

class DescribeNotebookInstanceInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str

class DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigName: str

class DescribeOptimizationJobRequestRequestTypeDef(BaseModel):
    OptimizationJobName: str

class OptimizationOutputTypeDef(BaseModel):
    RecommendedInferenceImage: Optional[str] = None

class OptimizationVpcConfigOutputTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class DescribePipelineDefinitionForExecutionRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: str

class DescribePipelineExecutionRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: str

class PipelineExperimentConfigTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None

class DescribePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str

class DescribeProcessingJobRequestRequestTypeDef(BaseModel):
    ProcessingJobName: str

class DescribeProjectInputRequestTypeDef(BaseModel):
    ProjectName: str

class ServiceCatalogProvisionedProductDetailsTypeDef(BaseModel):
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductStatusMessage: Optional[str] = None

class DescribeSpaceRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpaceName: str

class DescribeStudioLifecycleConfigRequestRequestTypeDef(BaseModel):
    StudioLifecycleConfigName: str

class DescribeSubscribedWorkteamRequestRequestTypeDef(BaseModel):
    WorkteamArn: str

class SubscribedWorkteamTypeDef(BaseModel):
    WorkteamArn: str
    MarketplaceTitle: Optional[str] = None
    SellerName: Optional[str] = None
    MarketplaceDescription: Optional[str] = None
    ListingId: Optional[str] = None

class DescribeTrainingJobRequestRequestTypeDef(BaseModel):
    TrainingJobName: str

class MetricDataTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Value: Optional[float] = None
    Timestamp: Optional[datetime] = None

class ProfilerConfigOutputTypeDef(BaseModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None

class ProfilerRuleConfigurationOutputTypeDef(BaseModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None

class ProfilerRuleEvaluationStatusTypeDef(BaseModel):
    RuleConfigurationName: Optional[str] = None
    RuleEvaluationJobArn: Optional[str] = None
    RuleEvaluationStatus: Optional[RuleEvaluationStatusType] = None
    StatusDetails: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class SecondaryStatusTransitionTypeDef(BaseModel):
    Status: SecondaryStatusType
    StartTime: datetime
    EndTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class WarmPoolStatusTypeDef(BaseModel):
    Status: WarmPoolResourceStatusType
    ResourceRetainedBillableTimeInSeconds: Optional[int] = None
    ReusedByJob: Optional[str] = None

class DescribeTransformJobRequestRequestTypeDef(BaseModel):
    TransformJobName: str

class DescribeTrialComponentRequestRequestTypeDef(BaseModel):
    TrialComponentName: str

class TrialComponentMetricSummaryTypeDef(BaseModel):
    MetricName: Optional[str] = None
    SourceArn: Optional[str] = None
    TimeStamp: Optional[datetime] = None
    Max: Optional[float] = None
    Min: Optional[float] = None
    Last: Optional[float] = None
    Count: Optional[int] = None
    Avg: Optional[float] = None
    StdDev: Optional[float] = None

class TrialComponentSourceTypeDef(BaseModel):
    SourceArn: str
    SourceType: Optional[str] = None

class DescribeTrialRequestRequestTypeDef(BaseModel):
    TrialName: str

class TrialSourceTypeDef(BaseModel):
    SourceArn: str
    SourceType: Optional[str] = None

class DescribeUserProfileRequestRequestTypeDef(BaseModel):
    DomainId: str
    UserProfileName: str

class DescribeWorkforceRequestRequestTypeDef(BaseModel):
    WorkforceName: str

class DescribeWorkteamRequestRequestTypeDef(BaseModel):
    WorkteamName: str

class ProductionVariantServerlessUpdateConfigTypeDef(BaseModel):
    MaxConcurrency: Optional[int] = None
    ProvisionedConcurrency: Optional[int] = None

class DeviceDeploymentSummaryTypeDef(BaseModel):
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

class DeviceFleetSummaryTypeDef(BaseModel):
    DeviceFleetArn: str
    DeviceFleetName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class DeviceStatsTypeDef(BaseModel):
    ConnectedDeviceCount: int
    RegisteredDeviceCount: int

class EdgeModelSummaryTypeDef(BaseModel):
    ModelName: str
    ModelVersion: str

class DeviceTypeDef(BaseModel):
    DeviceName: str
    Description: Optional[str] = None
    IotThingName: Optional[str] = None

class DisassociateTrialComponentRequestRequestTypeDef(BaseModel):
    TrialComponentName: str
    TrialName: str

class DockerSettingsOutputTypeDef(BaseModel):
    EnableDockerAccess: Optional[FeatureStatusType] = None
    VpcOnlyTrustedAccounts: Optional[List[str]] = None

class DockerSettingsTypeDef(BaseModel):
    EnableDockerAccess: Optional[FeatureStatusType] = None
    VpcOnlyTrustedAccounts: Optional[Sequence[str]] = None

class DomainDetailsTypeDef(BaseModel):
    DomainArn: Optional[str] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Status: Optional[DomainStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Url: Optional[str] = None

class FileSourceTypeDef(BaseModel):
    S3Uri: str
    ContentType: Optional[str] = None
    ContentDigest: Optional[str] = None

class EMRStepMetadataTypeDef(BaseModel):
    ClusterId: Optional[str] = None
    StepId: Optional[str] = None
    StepName: Optional[str] = None
    LogFilePath: Optional[str] = None

class EbsStorageSettingsTypeDef(BaseModel):
    EbsVolumeSizeInGb: int

class EdgeDeploymentPlanSummaryTypeDef(BaseModel):
    EdgeDeploymentPlanArn: str
    EdgeDeploymentPlanName: str
    DeviceFleetName: str
    EdgeDeploymentSuccess: int
    EdgeDeploymentPending: int
    EdgeDeploymentFailed: int
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class EdgeModelStatTypeDef(BaseModel):
    ModelName: str
    ModelVersion: str
    OfflineDeviceCount: int
    ConnectedDeviceCount: int
    ActiveDeviceCount: int
    SamplingDeviceCount: int

class EdgePackagingJobSummaryTypeDef(BaseModel):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    EdgePackagingJobStatus: EdgePackagingJobStatusType
    CompilationJobName: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class EdgeTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None

class EndpointConfigSummaryTypeDef(BaseModel):
    EndpointConfigName: str
    EndpointConfigArn: str
    CreationTime: datetime

class EndpointInfoTypeDef(BaseModel):
    EndpointName: Optional[str] = None

class ProductionVariantServerlessConfigTypeDef(BaseModel):
    MemorySizeInMB: int
    MaxConcurrency: int
    ProvisionedConcurrency: Optional[int] = None

class InferenceMetricsTypeDef(BaseModel):
    MaxInvocations: int
    ModelLatency: int

class EndpointSummaryTypeDef(BaseModel):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatusType

class EnvironmentParameterTypeDef(BaseModel):
    Key: str
    ValueType: str
    Value: str

class FailStepMetadataTypeDef(BaseModel):
    ErrorMessage: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: str
    Operator: Optional[OperatorType] = None
    Value: Optional[str] = None

class FinalHyperParameterTuningJobObjectiveMetricTypeDef(BaseModel):
    MetricName: str
    Value: float
    Type: Optional[HyperParameterTuningJobObjectiveTypeType] = None

class FlowDefinitionSummaryTypeDef(BaseModel):
    FlowDefinitionName: str
    FlowDefinitionArn: str
    FlowDefinitionStatus: FlowDefinitionStatusType
    CreationTime: datetime
    FailureReason: Optional[str] = None

class GetDeviceFleetReportRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str

class GetLineageGroupPolicyRequestRequestTypeDef(BaseModel):
    LineageGroupName: str

class GetModelPackageGroupPolicyInputRequestTypeDef(BaseModel):
    ModelPackageGroupName: str

class ScalingPolicyObjectiveTypeDef(BaseModel):
    MinInvocationsPerMinute: Optional[int] = None
    MaxInvocationsPerMinute: Optional[int] = None

class ScalingPolicyMetricTypeDef(BaseModel):
    InvocationsPerInstance: Optional[int] = None
    ModelLatency: Optional[int] = None

class PropertyNameSuggestionTypeDef(BaseModel):
    PropertyName: Optional[str] = None

class GitConfigForUpdateTypeDef(BaseModel):
    SecretArn: Optional[str] = None

class HolidayConfigAttributesTypeDef(BaseModel):
    CountryCode: Optional[str] = None

class HubContentInfoTypeDef(BaseModel):
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

class HubInfoTypeDef(BaseModel):
    HubName: str
    HubArn: str
    HubStatus: HubStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    HubDisplayName: Optional[str] = None
    HubDescription: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None

class HumanLoopActivationConditionsConfigTypeDef(BaseModel):
    HumanLoopActivationConditions: str

class UiConfigTypeDef(BaseModel):
    UiTemplateS3Uri: Optional[str] = None
    HumanTaskUiArn: Optional[str] = None

class HumanTaskUiSummaryTypeDef(BaseModel):
    HumanTaskUiName: str
    HumanTaskUiArn: str
    CreationTime: datetime

class HyperParameterTuningJobObjectiveTypeDef(BaseModel):
    Type: HyperParameterTuningJobObjectiveTypeType
    MetricName: str

class VpcConfigExtraOutputTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class HyperParameterTuningInstanceConfigTypeDef(BaseModel):
    InstanceType: TrainingInstanceTypeType
    InstanceCount: int
    VolumeSizeInGB: int

class ResourceLimitsTypeDef(BaseModel):
    MaxParallelTrainingJobs: int
    MaxNumberOfTrainingJobs: Optional[int] = None
    MaxRuntimeInSeconds: Optional[int] = None

class HyperbandStrategyConfigTypeDef(BaseModel):
    MinResource: Optional[int] = None
    MaxResource: Optional[int] = None

class ParentHyperParameterTuningJobTypeDef(BaseModel):
    HyperParameterTuningJobName: Optional[str] = None

class IamIdentityTypeDef(BaseModel):
    Arn: Optional[str] = None
    PrincipalId: Optional[str] = None
    SourceIdentity: Optional[str] = None

class IamPolicyConstraintsTypeDef(BaseModel):
    SourceIp: Optional[EnabledOrDisabledType] = None
    VpcSourceIp: Optional[EnabledOrDisabledType] = None

class RepositoryAuthConfigTypeDef(BaseModel):
    RepositoryCredentialsProviderArn: str

class ImageTypeDef(BaseModel):
    CreationTime: datetime
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatusType
    LastModifiedTime: datetime
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    FailureReason: Optional[str] = None

class ImageVersionTypeDef(BaseModel):
    CreationTime: datetime
    ImageArn: str
    ImageVersionArn: str
    ImageVersionStatus: ImageVersionStatusType
    LastModifiedTime: datetime
    Version: int
    FailureReason: Optional[str] = None

class InferenceComponentComputeResourceRequirementsTypeDef(BaseModel):
    MinMemoryRequiredInMb: int
    NumberOfCpuCoresRequired: Optional[float] = None
    NumberOfAcceleratorDevicesRequired: Optional[float] = None
    MaxMemoryRequiredInMb: Optional[int] = None

class InferenceComponentContainerSpecificationTypeDef(BaseModel):
    Image: Optional[str] = None
    ArtifactUrl: Optional[str] = None
    Environment: Optional[Mapping[str, str]] = None

class InferenceComponentStartupParametersTypeDef(BaseModel):
    ModelDataDownloadTimeoutInSeconds: Optional[int] = None
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int] = None

class InferenceComponentSummaryTypeDef(BaseModel):
    CreationTime: datetime
    InferenceComponentArn: str
    InferenceComponentName: str
    EndpointArn: str
    EndpointName: str
    VariantName: str
    LastModifiedTime: datetime
    InferenceComponentStatus: Optional[InferenceComponentStatusType] = None

class InferenceExperimentScheduleExtraOutputTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class InferenceHubAccessConfigTypeDef(BaseModel):
    HubContentArn: str

class RecommendationMetricsTypeDef(BaseModel):
    CostPerHour: Optional[float] = None
    CostPerInference: Optional[float] = None
    MaxInvocations: Optional[int] = None
    ModelLatency: Optional[int] = None
    CpuUtilization: Optional[float] = None
    MemoryUtilization: Optional[float] = None
    ModelSetupTime: Optional[int] = None

class InferenceRecommendationsJobTypeDef(BaseModel):
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

class InstanceGroupTypeDef(BaseModel):
    InstanceType: TrainingInstanceTypeType
    InstanceCount: int
    InstanceGroupName: str

class IntegerParameterRangeSpecificationTypeDef(BaseModel):
    MinValue: str
    MaxValue: str

class IntegerParameterRangeTypeDef(BaseModel):
    Name: str
    MinValue: str
    MaxValue: str
    ScalingType: Optional[HyperParameterScalingTypeType] = None

class KernelSpecTypeDef(BaseModel):
    Name: str
    DisplayName: Optional[str] = None

class LabelCountersForWorkteamTypeDef(BaseModel):
    HumanLabeled: Optional[int] = None
    PendingHuman: Optional[int] = None
    Total: Optional[int] = None

class LabelingJobDataAttributesExtraOutputTypeDef(BaseModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None

class LabelingJobDataAttributesOutputTypeDef(BaseModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None

class LabelingJobDataAttributesTypeDef(BaseModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None

class LabelingJobS3DataSourceTypeDef(BaseModel):
    ManifestS3Uri: str

class LabelingJobSnsDataSourceTypeDef(BaseModel):
    SnsTopicArn: str

class LineageGroupSummaryTypeDef(BaseModel):
    LineageGroupArn: Optional[str] = None
    LineageGroupName: Optional[str] = None
    DisplayName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None

class ListCandidatesForAutoMLJobRequestRequestTypeDef(BaseModel):
    AutoMLJobName: str
    StatusEquals: Optional[CandidateStatusType] = None
    CandidateNameEquals: Optional[str] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[CandidateSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MonitoringJobDefinitionSummaryTypeDef(BaseModel):
    MonitoringJobDefinitionName: str
    MonitoringJobDefinitionArn: str
    CreationTime: datetime
    EndpointName: str

class ListDomainsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInferenceRecommendationsJobStepsRequestRequestTypeDef(BaseModel):
    JobName: str
    Status: Optional[RecommendationJobStatusType] = None
    StepType: Optional[Literal["BENCHMARK"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TrackingServerSummaryTypeDef(BaseModel):
    TrackingServerArn: Optional[str] = None
    TrackingServerName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    IsActive: Optional[IsTrackingServerActiveType] = None
    MlflowVersion: Optional[str] = None

class ModelCardExportJobSummaryTypeDef(BaseModel):
    ModelCardExportJobName: str
    ModelCardExportJobArn: str
    Status: ModelCardExportJobStatusType
    ModelCardName: str
    ModelCardVersion: int
    CreatedAt: datetime
    LastModifiedAt: datetime

class ModelCardVersionSummaryTypeDef(BaseModel):
    ModelCardName: str
    ModelCardArn: str
    ModelCardStatus: ModelCardStatusType
    ModelCardVersion: int
    CreationTime: datetime
    LastModifiedTime: Optional[datetime] = None

class ModelCardSummaryTypeDef(BaseModel):
    ModelCardName: str
    ModelCardArn: str
    ModelCardStatus: ModelCardStatusType
    CreationTime: datetime
    LastModifiedTime: Optional[datetime] = None

class ModelMetadataSummaryTypeDef(BaseModel):
    Domain: str
    Framework: str
    Task: str
    Model: str
    FrameworkVersion: str

class ModelPackageGroupSummaryTypeDef(BaseModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    CreationTime: datetime
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ModelPackageGroupDescription: Optional[str] = None

class ModelPackageSummaryTypeDef(BaseModel):
    ModelPackageArn: str
    CreationTime: datetime
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageVersion: Optional[int] = None
    ModelPackageDescription: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None

class ModelSummaryTypeDef(BaseModel):
    ModelName: str
    ModelArn: str
    CreationTime: datetime

class MonitoringAlertHistorySummaryTypeDef(BaseModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    CreationTime: datetime
    AlertStatus: MonitoringAlertStatusType

class ListMonitoringAlertsRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MonitoringScheduleSummaryTypeDef(BaseModel):
    MonitoringScheduleName: str
    MonitoringScheduleArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleStatus: ScheduleStatusType
    EndpointName: Optional[str] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class NotebookInstanceLifecycleConfigSummaryTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigName: str
    NotebookInstanceLifecycleConfigArn: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class NotebookInstanceSummaryTypeDef(BaseModel):
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

class OptimizationJobSummaryTypeDef(BaseModel):
    OptimizationJobName: str
    OptimizationJobArn: str
    CreationTime: datetime
    OptimizationJobStatus: OptimizationJobStatusType
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationTypes: List[str]
    OptimizationStartTime: Optional[datetime] = None
    OptimizationEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class ListPipelineExecutionStepsRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None

class PipelineExecutionSummaryTypeDef(BaseModel):
    PipelineExecutionArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    PipelineExecutionStatus: Optional[PipelineExecutionStatusType] = None
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineExecutionFailureReason: Optional[str] = None

class ListPipelineParametersForExecutionRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ParameterTypeDef(BaseModel):
    Name: str
    Value: str

class PipelineSummaryTypeDef(BaseModel):
    PipelineArn: Optional[str] = None
    PipelineName: Optional[str] = None
    PipelineDisplayName: Optional[str] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastExecutionTime: Optional[datetime] = None

class ProcessingJobSummaryTypeDef(BaseModel):
    ProcessingJobName: str
    ProcessingJobArn: str
    CreationTime: datetime
    ProcessingJobStatus: ProcessingJobStatusType
    ProcessingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    ExitMessage: Optional[str] = None

class ProjectSummaryTypeDef(BaseModel):
    ProjectName: str
    ProjectArn: str
    ProjectId: str
    CreationTime: datetime
    ProjectStatus: ProjectStatusType
    ProjectDescription: Optional[str] = None

class ResourceCatalogTypeDef(BaseModel):
    ResourceCatalogArn: str
    ResourceCatalogName: str
    Description: str
    CreationTime: datetime

class ListSpacesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None

class ListStageDevicesRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    StageName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ExcludeDevicesDeployedInOtherStage: Optional[bool] = None

class StudioLifecycleConfigDetailsTypeDef(BaseModel):
    StudioLifecycleConfigArn: Optional[str] = None
    StudioLifecycleConfigName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    StudioLifecycleConfigAppType: Optional[StudioLifecycleConfigAppTypeType] = None

class ListSubscribedWorkteamsRequestRequestTypeDef(BaseModel):
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsInputRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef(BaseModel):
    HyperParameterTuningJobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[TrainingJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None

class TransformJobSummaryTypeDef(BaseModel):
    TransformJobName: str
    TransformJobArn: str
    CreationTime: datetime
    TransformJobStatus: TransformJobStatusType
    TransformEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    FailureReason: Optional[str] = None

class ListUserProfilesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[UserProfileSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameContains: Optional[str] = None

class UserProfileDetailsTypeDef(BaseModel):
    DomainId: Optional[str] = None
    UserProfileName: Optional[str] = None
    Status: Optional[UserProfileStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class ListWorkforcesRequestRequestTypeDef(BaseModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListWorkteamsRequestRequestTypeDef(BaseModel):
    SortBy: Optional[ListWorkteamsSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OidcMemberDefinitionExtraOutputTypeDef(BaseModel):
    Groups: Optional[List[str]] = None

class OidcMemberDefinitionOutputTypeDef(BaseModel):
    Groups: Optional[List[str]] = None

class OidcMemberDefinitionTypeDef(BaseModel):
    Groups: Optional[Sequence[str]] = None

class PredefinedMetricSpecificationTypeDef(BaseModel):
    PredefinedMetricType: Optional[str] = None

class ModelAccessConfigTypeDef(BaseModel):
    AcceptEula: bool

class MonitoringGroundTruthS3InputTypeDef(BaseModel):
    S3Uri: Optional[str] = None

class ModelCompilationConfigOutputTypeDef(BaseModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None

class ModelCompilationConfigTypeDef(BaseModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Mapping[str, str]] = None

class ModelDashboardEndpointTypeDef(BaseModel):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatusType

class ModelDashboardIndicatorActionTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class RealTimeInferenceConfigTypeDef(BaseModel):
    InstanceType: InstanceTypeType
    InstanceCount: int

class ModelInputTypeDef(BaseModel):
    DataInputConfig: str

class ModelLatencyThresholdTypeDef(BaseModel):
    Percentile: Optional[str] = None
    ValueInMilliseconds: Optional[int] = None

class ModelMetadataFilterTypeDef(BaseModel):
    Name: ModelMetadataFilterTypeType
    Value: str

class ModelPackageStatusItemTypeDef(BaseModel):
    Name: str
    Status: DetailedModelPackageStatusType
    FailureReason: Optional[str] = None

class ModelQuantizationConfigOutputTypeDef(BaseModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None

class ModelQuantizationConfigTypeDef(BaseModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Mapping[str, str]] = None

class ModelStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None

class MonitoringAppSpecificationExtraOutputTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None

class MonitoringAppSpecificationOutputTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None

class MonitoringAppSpecificationTypeDef(BaseModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None

class MonitoringClusterConfigTypeDef(BaseModel):
    InstanceCount: int
    InstanceType: ProcessingInstanceTypeType
    VolumeSizeInGB: int
    VolumeKmsKeyId: Optional[str] = None

class MonitoringCsvDatasetFormatTypeDef(BaseModel):
    Header: Optional[bool] = None

class MonitoringJsonDatasetFormatTypeDef(BaseModel):
    Line: Optional[bool] = None

class MonitoringS3OutputTypeDef(BaseModel):
    S3Uri: str
    LocalPath: str
    S3UploadMode: Optional[ProcessingS3UploadModeType] = None

class ScheduleConfigTypeDef(BaseModel):
    ScheduleExpression: str
    DataAnalysisStartTime: Optional[str] = None
    DataAnalysisEndTime: Optional[str] = None

class S3StorageConfigTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None
    ResolvedOutputS3Uri: Optional[str] = None

class OidcConfigForResponseTypeDef(BaseModel):
    ClientId: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    LogoutEndpoint: Optional[str] = None
    JwksUri: Optional[str] = None
    Scope: Optional[str] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None

class OnlineStoreSecurityConfigTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None

class TtlDurationTypeDef(BaseModel):
    Unit: Optional[TtlDurationUnitType] = None
    Value: Optional[int] = None

class OptimizationModelAccessConfigTypeDef(BaseModel):
    AcceptEula: bool

class TargetPlatformTypeDef(BaseModel):
    Os: TargetPlatformOsType
    Arch: TargetPlatformArchType
    Accelerator: Optional[TargetPlatformAcceleratorType] = None

class OwnershipSettingsSummaryTypeDef(BaseModel):
    OwnerUserProfileName: Optional[str] = None

class ParentTypeDef(BaseModel):
    TrialName: Optional[str] = None
    ExperimentName: Optional[str] = None

class ProductionVariantManagedInstanceScalingTypeDef(BaseModel):
    Status: Optional[ManagedInstanceScalingStatusType] = None
    MinInstanceCount: Optional[int] = None
    MaxInstanceCount: Optional[int] = None

class ProductionVariantRoutingConfigTypeDef(BaseModel):
    RoutingStrategy: RoutingStrategyType

class ProductionVariantStatusTypeDef(BaseModel):
    Status: VariantStatusType
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None

class PhaseTypeDef(BaseModel):
    InitialNumberOfUsers: Optional[int] = None
    SpawnRate: Optional[int] = None
    DurationInSeconds: Optional[int] = None

class ProcessingJobStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None

class QualityCheckStepMetadataTypeDef(BaseModel):
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

class RegisterModelStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None

class TrainingJobStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None

class TransformJobStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None

class TuningJobStepMetaDataTypeDef(BaseModel):
    Arn: Optional[str] = None

class SelectiveExecutionResultTypeDef(BaseModel):
    SourcePipelineExecutionArn: Optional[str] = None

class ProcessingClusterConfigTypeDef(BaseModel):
    InstanceCount: int
    InstanceType: ProcessingInstanceTypeType
    VolumeSizeInGB: int
    VolumeKmsKeyId: Optional[str] = None

class ProcessingFeatureStoreOutputTypeDef(BaseModel):
    FeatureGroupName: str

class ProcessingS3InputTypeDef(BaseModel):
    S3Uri: str
    S3DataType: ProcessingS3DataTypeType
    LocalPath: Optional[str] = None
    S3InputMode: Optional[ProcessingS3InputModeType] = None
    S3DataDistributionType: Optional[ProcessingS3DataDistributionTypeType] = None
    S3CompressionType: Optional[ProcessingS3CompressionTypeType] = None

class ProcessingS3OutputTypeDef(BaseModel):
    S3Uri: str
    LocalPath: str
    S3UploadMode: ProcessingS3UploadModeType

class ProductionVariantCoreDumpConfigTypeDef(BaseModel):
    DestinationS3Uri: str
    KmsKeyId: Optional[str] = None

class ProfilerConfigExtraOutputTypeDef(BaseModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None

class ProfilerConfigForUpdateTypeDef(BaseModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Mapping[str, str]] = None
    DisableProfiler: Optional[bool] = None

class ProfilerRuleConfigurationTypeDef(BaseModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Mapping[str, str]] = None

class PropertyNameQueryTypeDef(BaseModel):
    PropertyNameHint: str

class ProvisioningParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class USDTypeDef(BaseModel):
    Dollars: Optional[int] = None
    Cents: Optional[int] = None
    TenthFractionsOfACent: Optional[int] = None

class PutModelPackageGroupPolicyInputRequestTypeDef(BaseModel):
    ModelPackageGroupName: str
    ResourcePolicy: str

class VertexTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    LineageType: Optional[LineageTypeType] = None

class RStudioServerProAppSettingsTypeDef(BaseModel):
    AccessStatus: Optional[RStudioServerProAccessStatusType] = None
    UserGroup: Optional[RStudioServerProUserGroupType] = None

class RecommendationJobCompiledOutputConfigTypeDef(BaseModel):
    S3OutputUri: Optional[str] = None

class RecommendationJobPayloadConfigOutputTypeDef(BaseModel):
    SamplePayloadUrl: Optional[str] = None
    SupportedContentTypes: Optional[List[str]] = None

class RecommendationJobPayloadConfigTypeDef(BaseModel):
    SamplePayloadUrl: Optional[str] = None
    SupportedContentTypes: Optional[Sequence[str]] = None

class RecommendationJobResourceLimitTypeDef(BaseModel):
    MaxNumberOfTests: Optional[int] = None
    MaxParallelOfTests: Optional[int] = None

class RecommendationJobVpcConfigOutputTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class RecommendationJobVpcConfigTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class RemoteDebugConfigForUpdateTypeDef(BaseModel):
    EnableRemoteDebug: Optional[bool] = None

class RenderableTaskTypeDef(BaseModel):
    Input: str

class RenderingErrorTypeDef(BaseModel):
    Code: str
    Message: str

class ResourceConfigForUpdateTypeDef(BaseModel):
    KeepAlivePeriodInSeconds: int

class VisibilityConditionsTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class SelectedStepTypeDef(BaseModel):
    StepName: str

class SendPipelineExecutionStepFailureRequestRequestTypeDef(BaseModel):
    CallbackToken: str
    FailureReason: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class ShadowModelVariantConfigTypeDef(BaseModel):
    ShadowModelVariantName: str
    SamplingPercentage: int

class SharingSettingsTypeDef(BaseModel):
    NotebookOutputOption: Optional[NotebookOutputOptionType] = None
    S3OutputPath: Optional[str] = None
    S3KmsKeyId: Optional[str] = None

class SourceIpConfigExtraOutputTypeDef(BaseModel):
    Cidrs: List[str]

class SourceIpConfigOutputTypeDef(BaseModel):
    Cidrs: List[str]

class SpaceSharingSettingsSummaryTypeDef(BaseModel):
    SharingType: Optional[SharingTypeType] = None

class StairsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None
    NumberOfSteps: Optional[int] = None
    UsersPerStep: Optional[int] = None

class StartEdgeDeploymentStageRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    StageName: str

class StartInferenceExperimentRequestRequestTypeDef(BaseModel):
    Name: str

class StartMlflowTrackingServerRequestRequestTypeDef(BaseModel):
    TrackingServerName: str

class StartMonitoringScheduleRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str

class StartNotebookInstanceInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str

class StopAutoMLJobRequestRequestTypeDef(BaseModel):
    AutoMLJobName: str

class StopCompilationJobRequestRequestTypeDef(BaseModel):
    CompilationJobName: str

class StopEdgeDeploymentStageRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    StageName: str

class StopEdgePackagingJobRequestRequestTypeDef(BaseModel):
    EdgePackagingJobName: str

class StopHyperParameterTuningJobRequestRequestTypeDef(BaseModel):
    HyperParameterTuningJobName: str

class StopInferenceRecommendationsJobRequestRequestTypeDef(BaseModel):
    JobName: str

class StopLabelingJobRequestRequestTypeDef(BaseModel):
    LabelingJobName: str

class StopMlflowTrackingServerRequestRequestTypeDef(BaseModel):
    TrackingServerName: str

class StopMonitoringScheduleRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str

class StopNotebookInstanceInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str

class StopOptimizationJobRequestRequestTypeDef(BaseModel):
    OptimizationJobName: str

class StopPipelineExecutionRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: str
    ClientRequestToken: str

class StopProcessingJobRequestRequestTypeDef(BaseModel):
    ProcessingJobName: str

class StopTrainingJobRequestRequestTypeDef(BaseModel):
    TrainingJobName: str

class StopTransformJobRequestRequestTypeDef(BaseModel):
    TransformJobName: str

class StudioWebPortalSettingsOutputTypeDef(BaseModel):
    HiddenMlTools: Optional[List[MlToolsType]] = None
    HiddenAppTypes: Optional[List[AppTypeType]] = None

class StudioWebPortalSettingsTypeDef(BaseModel):
    HiddenMlTools: Optional[Sequence[MlToolsType]] = None
    HiddenAppTypes: Optional[Sequence[AppTypeType]] = None

class ThroughputConfigUpdateTypeDef(BaseModel):
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None

class TimeSeriesConfigOutputTypeDef(BaseModel):
    TargetAttributeName: str
    TimestampAttributeName: str
    ItemIdentifierAttributeName: str
    GroupingAttributeNames: Optional[List[str]] = None

class TimeSeriesConfigTypeDef(BaseModel):
    TargetAttributeName: str
    TimestampAttributeName: str
    ItemIdentifierAttributeName: str
    GroupingAttributeNames: Optional[Sequence[str]] = None

class TimeSeriesTransformationsOutputTypeDef(BaseModel):
    Filling: Optional[Dict[str, Dict[FillingTypeType, str]]] = None
    Aggregation: Optional[Dict[str, AggregationTransformationValueType]] = None

class TimeSeriesTransformationsTypeDef(BaseModel):
    Filling: Optional[Mapping[str, Mapping[FillingTypeType, str]]] = None
    Aggregation: Optional[Mapping[str, AggregationTransformationValueType]] = None

class TrainingRepositoryAuthConfigTypeDef(BaseModel):
    TrainingRepositoryCredentialsProviderArn: str

class TransformS3DataSourceTypeDef(BaseModel):
    S3DataType: S3DataTypeType
    S3Uri: str

class UpdateActionRequestRequestTypeDef(BaseModel):
    ActionName: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Mapping[str, str]] = None
    PropertiesToRemove: Optional[Sequence[str]] = None

class UpdateArtifactRequestRequestTypeDef(BaseModel):
    ArtifactArn: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    PropertiesToRemove: Optional[Sequence[str]] = None

class UpdateClusterSoftwareRequestRequestTypeDef(BaseModel):
    ClusterName: str

class UpdateContextRequestRequestTypeDef(BaseModel):
    ContextName: str
    Description: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    PropertiesToRemove: Optional[Sequence[str]] = None

class VariantPropertyTypeDef(BaseModel):
    VariantPropertyType: VariantPropertyTypeType

class UpdateExperimentRequestRequestTypeDef(BaseModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None

class UpdateHubRequestRequestTypeDef(BaseModel):
    HubName: str
    HubDescription: Optional[str] = None
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[Sequence[str]] = None

class UpdateImageRequestRequestTypeDef(BaseModel):
    ImageName: str
    DeleteProperties: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    RoleArn: Optional[str] = None

class UpdateImageVersionRequestRequestTypeDef(BaseModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    AliasesToAdd: Optional[Sequence[str]] = None
    AliasesToDelete: Optional[Sequence[str]] = None
    VendorGuidance: Optional[VendorGuidanceType] = None
    JobType: Optional[JobTypeType] = None
    MLFramework: Optional[str] = None
    ProgrammingLang: Optional[str] = None
    Processor: Optional[ProcessorType] = None
    Horovod: Optional[bool] = None
    ReleaseNotes: Optional[str] = None

class UpdateMlflowTrackingServerRequestRequestTypeDef(BaseModel):
    TrackingServerName: str
    ArtifactStoreUri: Optional[str] = None
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None

class UpdateModelCardRequestRequestTypeDef(BaseModel):
    ModelCardName: str
    Content: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None

class UpdateMonitoringAlertRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    DatapointsToAlert: int
    EvaluationPeriod: int

class UpdateTrialRequestRequestTypeDef(BaseModel):
    TrialName: str
    DisplayName: Optional[str] = None

class WorkforceVpcConfigResponseTypeDef(BaseModel):
    VpcId: str
    SecurityGroupIds: List[str]
    Subnets: List[str]
    VpcEndpointId: Optional[str] = None

class ActionSummaryTypeDef(BaseModel):
    ActionArn: Optional[str] = None
    ActionName: Optional[str] = None
    Source: Optional[ActionSourceTypeDef] = None
    ActionType: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class AddAssociationResponseTypeDef(BaseModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTrialComponentResponseTypeDef(BaseModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateActionResponseTypeDef(BaseModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAlgorithmOutputTypeDef(BaseModel):
    AlgorithmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppImageConfigResponseTypeDef(BaseModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppResponseTypeDef(BaseModel):
    AppArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateArtifactResponseTypeDef(BaseModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoMLJobResponseTypeDef(BaseModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoMLJobV2ResponseTypeDef(BaseModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeRepositoryOutputTypeDef(BaseModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCompilationJobResponseTypeDef(BaseModel):
    CompilationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContextResponseTypeDef(BaseModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataQualityJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseModel):
    DomainArn: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEdgeDeploymentPlanResponseTypeDef(BaseModel):
    EdgeDeploymentPlanArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointConfigOutputTypeDef(BaseModel):
    EndpointConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointOutputTypeDef(BaseModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentResponseTypeDef(BaseModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFeatureGroupResponseTypeDef(BaseModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowDefinitionResponseTypeDef(BaseModel):
    FlowDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHubContentReferenceResponseTypeDef(BaseModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHubResponseTypeDef(BaseModel):
    HubArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHumanTaskUiResponseTypeDef(BaseModel):
    HumanTaskUiArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHyperParameterTuningJobResponseTypeDef(BaseModel):
    HyperParameterTuningJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageResponseTypeDef(BaseModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageVersionResponseTypeDef(BaseModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceComponentOutputTypeDef(BaseModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceExperimentResponseTypeDef(BaseModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceRecommendationsJobResponseTypeDef(BaseModel):
    JobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelingJobResponseTypeDef(BaseModel):
    LabelingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMlflowTrackingServerResponseTypeDef(BaseModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelBiasJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelCardExportJobResponseTypeDef(BaseModel):
    ModelCardExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelCardResponseTypeDef(BaseModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelExplainabilityJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelOutputTypeDef(BaseModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelPackageGroupOutputTypeDef(BaseModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelPackageOutputTypeDef(BaseModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelQualityJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitoringScheduleResponseTypeDef(BaseModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookInstanceLifecycleConfigOutputTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookInstanceOutputTypeDef(BaseModel):
    NotebookInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOptimizationJobResponseTypeDef(BaseModel):
    OptimizationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineResponseTypeDef(BaseModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedDomainUrlResponseTypeDef(BaseModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedMlflowTrackingServerUrlResponseTypeDef(BaseModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedNotebookInstanceUrlOutputTypeDef(BaseModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProcessingJobResponseTypeDef(BaseModel):
    ProcessingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectOutputTypeDef(BaseModel):
    ProjectArn: str
    ProjectId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSpaceResponseTypeDef(BaseModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioLifecycleConfigResponseTypeDef(BaseModel):
    StudioLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingJobResponseTypeDef(BaseModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransformJobResponseTypeDef(BaseModel):
    TransformJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrialComponentResponseTypeDef(BaseModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrialResponseTypeDef(BaseModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserProfileResponseTypeDef(BaseModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkforceResponseTypeDef(BaseModel):
    WorkforceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkteamResponseTypeDef(BaseModel):
    WorkteamArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteActionResponseTypeDef(BaseModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteArtifactResponseTypeDef(BaseModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAssociationResponseTypeDef(BaseModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteContextResponseTypeDef(BaseModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExperimentResponseTypeDef(BaseModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInferenceExperimentResponseTypeDef(BaseModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMlflowTrackingServerResponseTypeDef(BaseModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePipelineResponseTypeDef(BaseModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrialComponentResponseTypeDef(BaseModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrialResponseTypeDef(BaseModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkteamResponseTypeDef(BaseModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageResponseTypeDef(BaseModel):
    CreationTime: datetime
    Description: str
    DisplayName: str
    FailureReason: str
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatusType
    LastModifiedTime: datetime
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageVersionResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePipelineDefinitionForExecutionResponseTypeDef(BaseModel):
    PipelineDefinition: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStudioLifecycleConfigResponseTypeDef(BaseModel):
    StudioLifecycleConfigArn: str
    StudioLifecycleConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTrialComponentResponseTypeDef(BaseModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetLineageGroupPolicyResponseTypeDef(BaseModel):
    LineageGroupArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelPackageGroupPolicyOutputTypeDef(BaseModel):
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSagemakerServicecatalogPortfolioStatusOutputTypeDef(BaseModel):
    Status: SagemakerServicecatalogStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ImportHubContentResponseTypeDef(BaseModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseModel):
    SageMakerImageVersionAliases: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutModelPackageGroupPolicyOutputTypeDef(BaseModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RetryPipelineExecutionResponseTypeDef(BaseModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendPipelineExecutionStepFailureResponseTypeDef(BaseModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendPipelineExecutionStepSuccessResponseTypeDef(BaseModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartInferenceExperimentResponseTypeDef(BaseModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMlflowTrackingServerResponseTypeDef(BaseModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineExecutionResponseTypeDef(BaseModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopInferenceExperimentResponseTypeDef(BaseModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopMlflowTrackingServerResponseTypeDef(BaseModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipelineExecutionResponseTypeDef(BaseModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionResponseTypeDef(BaseModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppImageConfigResponseTypeDef(BaseModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateArtifactResponseTypeDef(BaseModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterSoftwareResponseTypeDef(BaseModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeRepositoryOutputTypeDef(BaseModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContextResponseTypeDef(BaseModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainResponseTypeDef(BaseModel):
    DomainArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointOutputTypeDef(BaseModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointWeightsAndCapacitiesOutputTypeDef(BaseModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperimentResponseTypeDef(BaseModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFeatureGroupResponseTypeDef(BaseModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHubResponseTypeDef(BaseModel):
    HubArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageResponseTypeDef(BaseModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageVersionResponseTypeDef(BaseModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInferenceComponentOutputTypeDef(BaseModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInferenceComponentRuntimeConfigOutputTypeDef(BaseModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInferenceExperimentResponseTypeDef(BaseModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMlflowTrackingServerResponseTypeDef(BaseModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelCardResponseTypeDef(BaseModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelPackageOutputTypeDef(BaseModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitoringAlertResponseTypeDef(BaseModel):
    MonitoringScheduleArn: str
    MonitoringAlertName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitoringScheduleResponseTypeDef(BaseModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineExecutionResponseTypeDef(BaseModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineResponseTypeDef(BaseModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectOutputTypeDef(BaseModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSpaceResponseTypeDef(BaseModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrainingJobResponseTypeDef(BaseModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrialComponentResponseTypeDef(BaseModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrialResponseTypeDef(BaseModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserProfileResponseTypeDef(BaseModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AddTagsOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentRequestRequestTypeDef(BaseModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateHubContentReferenceRequestRequestTypeDef(BaseModel):
    HubName: str
    SageMakerPublicHubContentArn: str
    HubContentName: Optional[str] = None
    MinVersion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateImageRequestRequestTypeDef(BaseModel):
    ImageName: str
    RoleArn: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMlflowTrackingServerRequestRequestTypeDef(BaseModel):
    TrackingServerName: str
    ArtifactStoreUri: str
    RoleArn: str
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    MlflowVersion: Optional[str] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelPackageGroupInputRequestTypeDef(BaseModel):
    ModelPackageGroupName: str
    ModelPackageGroupDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateStudioLifecycleConfigRequestRequestTypeDef(BaseModel):
    StudioLifecycleConfigName: str
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportHubContentRequestRequestTypeDef(BaseModel):
    HubContentName: str
    HubContentType: HubContentTypeType
    DocumentSchemaVersion: str
    HubName: str
    HubContentDocument: str
    HubContentVersion: Optional[str] = None
    HubContentDisplayName: Optional[str] = None
    HubContentDescription: Optional[str] = None
    HubContentMarkdown: Optional[str] = None
    HubContentSearchKeywords: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoRollbackConfigOutputTypeDef(BaseModel):
    Alarms: Optional[List[AlarmTypeDef]] = None

class AutoRollbackConfigTypeDef(BaseModel):
    Alarms: Optional[Sequence[AlarmTypeDef]] = None

class HyperParameterAlgorithmSpecificationExtraOutputTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None

class HyperParameterAlgorithmSpecificationOutputTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None

class HyperParameterAlgorithmSpecificationTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None

class AlgorithmStatusDetailsTypeDef(BaseModel):
    ValidationStatuses: Optional[List[AlgorithmStatusItemTypeDef]] = None
    ImageScanStatuses: Optional[List[AlgorithmStatusItemTypeDef]] = None

class ListAlgorithmsOutputTypeDef(BaseModel):
    AlgorithmSummaryList: List[AlgorithmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AppDetailsTypeDef(BaseModel):
    DomainId: Optional[str] = None
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    AppType: Optional[AppTypeType] = None
    AppName: Optional[str] = None
    Status: Optional[AppStatusType] = None
    CreationTime: Optional[datetime] = None
    ResourceSpec: Optional[ResourceSpecTypeDef] = None

class CreateAppRequestRequestTypeDef(BaseModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ResourceSpec: Optional[ResourceSpecTypeDef] = None

class DescribeAppResponseTypeDef(BaseModel):
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
    ResourceSpec: ResourceSpecTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RStudioServerProDomainSettingsForUpdateTypeDef(BaseModel):
    DomainExecutionRoleArn: str
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    RStudioConnectUrl: Optional[str] = None
    RStudioPackageManagerUrl: Optional[str] = None

class RStudioServerProDomainSettingsTypeDef(BaseModel):
    DomainExecutionRoleArn: str
    RStudioConnectUrl: Optional[str] = None
    RStudioPackageManagerUrl: Optional[str] = None
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None

class SpaceCodeEditorAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None

class TensorBoardAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None

class ArtifactSourceExtraOutputTypeDef(BaseModel):
    SourceUri: str
    SourceTypes: Optional[List[ArtifactSourceTypeTypeDef]] = None

class ArtifactSourceOutputTypeDef(BaseModel):
    SourceUri: str
    SourceTypes: Optional[List[ArtifactSourceTypeTypeDef]] = None

class ArtifactSourceTypeDef(BaseModel):
    SourceUri: str
    SourceTypes: Optional[Sequence[ArtifactSourceTypeTypeDef]] = None

class AsyncInferenceOutputConfigOutputTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None
    S3OutputPath: Optional[str] = None
    NotificationConfig: Optional[AsyncInferenceNotificationConfigOutputTypeDef] = None
    S3FailurePath: Optional[str] = None

class AsyncInferenceOutputConfigTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None
    S3OutputPath: Optional[str] = None
    NotificationConfig: Optional[AsyncInferenceNotificationConfigTypeDef] = None
    S3FailurePath: Optional[str] = None

class AutoMLCandidateGenerationConfigOutputTypeDef(BaseModel):
    FeatureSpecificationS3Uri: Optional[str] = None
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfigOutputTypeDef]] = None

class CandidateGenerationConfigOutputTypeDef(BaseModel):
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfigOutputTypeDef]] = None

class AutoMLCandidateGenerationConfigTypeDef(BaseModel):
    FeatureSpecificationS3Uri: Optional[str] = None
    AlgorithmsConfig: Optional[Sequence[AutoMLAlgorithmConfigTypeDef]] = None

class CandidateGenerationConfigTypeDef(BaseModel):
    AlgorithmsConfig: Optional[Sequence[AutoMLAlgorithmConfigTypeDef]] = None

class AutoMLDataSourceTypeDef(BaseModel):
    S3DataSource: AutoMLS3DataSourceTypeDef

class ImageClassificationJobConfigTypeDef(BaseModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None

class TextClassificationJobConfigTypeDef(BaseModel):
    ContentColumn: str
    TargetLabelColumn: str
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None

class ResolvedAttributesTypeDef(BaseModel):
    AutoMLJobObjective: Optional[AutoMLJobObjectiveTypeDef] = None
    ProblemType: Optional[ProblemTypeType] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None

class AutoMLJobSummaryTypeDef(BaseModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    EndTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PartialFailureReasons: Optional[List[AutoMLPartialFailureReasonTypeDef]] = None

class AutoMLProblemTypeResolvedAttributesTypeDef(BaseModel):
    TabularResolvedAttributes: Optional[TabularResolvedAttributesTypeDef] = None
    TextGenerationResolvedAttributes: Optional[TextGenerationResolvedAttributesTypeDef] = None

class AutoMLSecurityConfigOutputTypeDef(BaseModel):
    VolumeKmsKeyId: Optional[str] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class LabelingJobResourceConfigOutputTypeDef(BaseModel):
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class MonitoringNetworkConfigOutputTypeDef(BaseModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class NetworkConfigOutputTypeDef(BaseModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class AutoMLSecurityConfigTypeDef(BaseModel):
    VolumeKmsKeyId: Optional[str] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class LabelingJobResourceConfigTypeDef(BaseModel):
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class MonitoringNetworkConfigTypeDef(BaseModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class NetworkConfigTypeDef(BaseModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class BiasTypeDef(BaseModel):
    Report: Optional[MetricsSourceTypeDef] = None
    PreTrainingReport: Optional[MetricsSourceTypeDef] = None
    PostTrainingReport: Optional[MetricsSourceTypeDef] = None

class DriftCheckModelDataQualityTypeDef(BaseModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class DriftCheckModelQualityTypeDef(BaseModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class ExplainabilityTypeDef(BaseModel):
    Report: Optional[MetricsSourceTypeDef] = None

class ModelDataQualityTypeDef(BaseModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class ModelQualityTypeDef(BaseModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class CallbackStepMetadataTypeDef(BaseModel):
    CallbackToken: Optional[str] = None
    SqsQueueUrl: Optional[str] = None
    OutputParameters: Optional[List[OutputParameterTypeDef]] = None

class LambdaStepMetadataTypeDef(BaseModel):
    Arn: Optional[str] = None
    OutputParameters: Optional[List[OutputParameterTypeDef]] = None

class SendPipelineExecutionStepSuccessRequestRequestTypeDef(BaseModel):
    CallbackToken: str
    OutputParameters: Optional[Sequence[OutputParameterTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class CandidatePropertiesTypeDef(BaseModel):
    CandidateArtifactLocations: Optional[CandidateArtifactLocationsTypeDef] = None
    CandidateMetrics: Optional[List[MetricDatumTypeDef]] = None

class CanvasAppSettingsOutputTypeDef(BaseModel):
    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettingsTypeDef] = None
    ModelRegisterSettings: Optional[ModelRegisterSettingsTypeDef] = None
    WorkspaceSettings: Optional[WorkspaceSettingsTypeDef] = None
    IdentityProviderOAuthSettings: Optional[List[IdentityProviderOAuthSettingTypeDef]] = None
    DirectDeploySettings: Optional[DirectDeploySettingsTypeDef] = None
    KendraSettings: Optional[KendraSettingsTypeDef] = None
    GenerativeAiSettings: Optional[GenerativeAiSettingsTypeDef] = None

class CanvasAppSettingsTypeDef(BaseModel):
    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettingsTypeDef] = None
    ModelRegisterSettings: Optional[ModelRegisterSettingsTypeDef] = None
    WorkspaceSettings: Optional[WorkspaceSettingsTypeDef] = None
    IdentityProviderOAuthSettings: Optional[Sequence[IdentityProviderOAuthSettingTypeDef]] = None
    DirectDeploySettings: Optional[DirectDeploySettingsTypeDef] = None
    KendraSettings: Optional[KendraSettingsTypeDef] = None
    GenerativeAiSettings: Optional[GenerativeAiSettingsTypeDef] = None

class RollingUpdatePolicyTypeDef(BaseModel):
    MaximumBatchSize: CapacitySizeTypeDef
    WaitIntervalInSeconds: int
    MaximumExecutionTimeoutInSeconds: Optional[int] = None
    RollbackMaximumBatchSize: Optional[CapacitySizeTypeDef] = None

class TrafficRoutingConfigTypeDef(BaseModel):
    Type: TrafficRoutingConfigTypeType
    WaitIntervalInSeconds: int
    CanarySize: Optional[CapacitySizeTypeDef] = None
    LinearStepSize: Optional[CapacitySizeTypeDef] = None

class InferenceExperimentDataStorageConfigOutputTypeDef(BaseModel):
    Destination: str
    KmsKey: Optional[str] = None
    ContentType: Optional[CaptureContentTypeHeaderOutputTypeDef] = None

class InferenceExperimentDataStorageConfigTypeDef(BaseModel):
    Destination: str
    KmsKey: Optional[str] = None
    ContentType: Optional[CaptureContentTypeHeaderTypeDef] = None

class DataCaptureConfigOutputTypeDef(BaseModel):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: List[CaptureOptionTypeDef]
    EnableCapture: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeaderOutputTypeDef] = None

class DataCaptureConfigTypeDef(BaseModel):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: Sequence[CaptureOptionTypeDef]
    EnableCapture: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeaderTypeDef] = None

class EnvironmentParameterRangesOutputTypeDef(BaseModel):
    CategoricalParameterRanges: Optional[List[CategoricalParameterOutputTypeDef]] = None

class EnvironmentParameterRangesTypeDef(BaseModel):
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterTypeDef]] = None

class ClarifyShapConfigTypeDef(BaseModel):
    ShapBaselineConfig: ClarifyShapBaselineConfigTypeDef
    NumberOfSamples: Optional[int] = None
    UseLogit: Optional[bool] = None
    Seed: Optional[int] = None
    TextConfig: Optional[ClarifyTextConfigTypeDef] = None

class ClusterInstanceStorageConfigTypeDef(BaseModel):
    EbsVolumeConfig: Optional[ClusterEbsVolumeConfigTypeDef] = None

class ClusterNodeSummaryTypeDef(BaseModel):
    InstanceGroupName: str
    InstanceId: str
    InstanceType: ClusterInstanceTypeType
    LaunchTime: datetime
    InstanceStatus: ClusterInstanceStatusDetailsTypeDef

class ListClustersResponseTypeDef(BaseModel):
    NextToken: str
    ClusterSummaries: List[ClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CodeEditorAppImageConfigExtraOutputTypeDef(BaseModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigExtraOutputTypeDef] = None

class JupyterLabAppImageConfigExtraOutputTypeDef(BaseModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigExtraOutputTypeDef] = None

class CodeEditorAppImageConfigOutputTypeDef(BaseModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigOutputTypeDef] = None

class JupyterLabAppImageConfigOutputTypeDef(BaseModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigOutputTypeDef] = None

class CodeEditorAppImageConfigTypeDef(BaseModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigTypeDef] = None

class JupyterLabAppImageConfigTypeDef(BaseModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigTypeDef] = None

class CodeEditorAppSettingsOutputTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[List[str]] = None

class CodeEditorAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None

class KernelGatewayAppSettingsOutputTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[List[str]] = None

class KernelGatewayAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None

class RSessionAppSettingsOutputTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None

class RSessionAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None

class CodeRepositorySummaryTypeDef(BaseModel):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: Optional[GitConfigTypeDef] = None

class CreateCodeRepositoryInputRequestTypeDef(BaseModel):
    CodeRepositoryName: str
    GitConfig: GitConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeCodeRepositoryOutputTypeDef(BaseModel):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: GitConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JupyterLabAppSettingsOutputTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepositoryTypeDef]] = None

class JupyterLabAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None
    CodeRepositories: Optional[Sequence[CodeRepositoryTypeDef]] = None

class JupyterServerAppSettingsOutputTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepositoryTypeDef]] = None

class JupyterServerAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None
    CodeRepositories: Optional[Sequence[CodeRepositoryTypeDef]] = None

class SpaceJupyterLabAppSettingsOutputTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CodeRepositories: Optional[List[CodeRepositoryTypeDef]] = None

class SpaceJupyterLabAppSettingsTypeDef(BaseModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CodeRepositories: Optional[Sequence[CodeRepositoryTypeDef]] = None

class CollectionConfigTypeDef(BaseModel):
    VectorConfig: Optional[VectorConfigTypeDef] = None

class DebugHookConfigExtraOutputTypeDef(BaseModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Dict[str, str]] = None
    CollectionConfigurations: Optional[List[CollectionConfigurationExtraOutputTypeDef]] = None

class DebugHookConfigOutputTypeDef(BaseModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Dict[str, str]] = None
    CollectionConfigurations: Optional[List[CollectionConfigurationOutputTypeDef]] = None

class DebugHookConfigTypeDef(BaseModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Mapping[str, str]] = None
    CollectionConfigurations: Optional[Sequence[CollectionConfigurationTypeDef]] = None

class ListCompilationJobsResponseTypeDef(BaseModel):
    CompilationJobSummaries: List[CompilationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContextSummaryTypeDef(BaseModel):
    ContextArn: Optional[str] = None
    ContextName: Optional[str] = None
    Source: Optional[ContextSourceTypeDef] = None
    ContextType: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class CreateContextRequestRequestTypeDef(BaseModel):
    ContextName: str
    Source: ContextSourceTypeDef
    ContextType: str
    Description: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TuningJobCompletionCriteriaTypeDef(BaseModel):
    TargetObjectiveMetricValue: Optional[float] = None
    BestObjectiveNotImproving: Optional[BestObjectiveNotImprovingTypeDef] = None
    ConvergenceDetected: Optional[ConvergenceDetectedTypeDef] = None

class CreateActionRequestRequestTypeDef(BaseModel):
    ActionName: str
    Source: ActionSourceTypeDef
    ActionType: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Mapping[str, str]] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTrialRequestRequestTypeDef(BaseModel):
    TrialName: str
    ExperimentName: str
    DisplayName: Optional[str] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDeviceFleetRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfigTypeDef
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EnableIotRoleAlias: Optional[bool] = None

class CreateEdgePackagingJobRequestRequestTypeDef(BaseModel):
    EdgePackagingJobName: str
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: EdgeOutputConfigTypeDef
    ResourceKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeDeviceFleetResponseTypeDef(BaseModel):
    DeviceFleetName: str
    DeviceFleetArn: str
    OutputConfig: EdgeOutputConfigTypeDef
    Description: str
    CreationTime: datetime
    LastModifiedTime: datetime
    RoleArn: str
    IotRoleAlias: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceFleetRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfigTypeDef
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    EnableIotRoleAlias: Optional[bool] = None

class CreateHubRequestRequestTypeDef(BaseModel):
    HubName: str
    HubDescription: str
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[Sequence[str]] = None
    S3StorageConfig: Optional[HubS3StorageConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeHubResponseTypeDef(BaseModel):
    HubName: str
    HubArn: str
    HubDisplayName: str
    HubDescription: str
    HubSearchKeywords: List[str]
    S3StorageConfig: HubS3StorageConfigTypeDef
    HubStatus: HubStatusType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHumanTaskUiRequestRequestTypeDef(BaseModel):
    HumanTaskUiName: str
    UiTemplate: UiTemplateTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateInferenceComponentRuntimeConfigInputRequestTypeDef(BaseModel):
    InferenceComponentName: str
    DesiredRuntimeConfig: InferenceComponentRuntimeConfigTypeDef

class CreateModelCardExportJobRequestRequestTypeDef(BaseModel):
    ModelCardName: str
    ModelCardExportJobName: str
    OutputConfig: ModelCardExportOutputConfigTypeDef
    ModelCardVersion: Optional[int] = None

class CreateModelCardRequestRequestTypeDef(BaseModel):
    ModelCardName: str
    Content: str
    ModelCardStatus: ModelCardStatusType
    SecurityConfig: Optional[ModelCardSecurityConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateNotebookInstanceInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str
    InstanceType: InstanceTypeType
    RoleArn: str
    SubnetId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    LifecycleConfigName: Optional[str] = None
    DirectInternetAccess: Optional[DirectInternetAccessType] = None
    VolumeSizeInGB: Optional[int] = None
    AcceleratorTypes: Optional[Sequence[NotebookInstanceAcceleratorTypeType]] = None
    DefaultCodeRepository: Optional[str] = None
    AdditionalCodeRepositories: Optional[Sequence[str]] = None
    RootAccess: Optional[RootAccessType] = None
    PlatformIdentifier: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       InstanceMetadataServiceConfigurationTypeDef     ] = None

class DescribeNotebookInstanceOutputTypeDef(BaseModel):
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
    InstanceMetadataServiceConfiguration: InstanceMetadataServiceConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNotebookInstanceInputRequestTypeDef(BaseModel):
    NotebookInstanceName: str
    InstanceType: Optional[InstanceTypeType] = None
    RoleArn: Optional[str] = None
    LifecycleConfigName: Optional[str] = None
    DisassociateLifecycleConfig: Optional[bool] = None
    VolumeSizeInGB: Optional[int] = None
    DefaultCodeRepository: Optional[str] = None
    AdditionalCodeRepositories: Optional[Sequence[str]] = None
    AcceleratorTypes: Optional[Sequence[NotebookInstanceAcceleratorTypeType]] = None
    DisassociateAcceleratorTypes: Optional[bool] = None
    DisassociateDefaultCodeRepository: Optional[bool] = None
    DisassociateAdditionalCodeRepositories: Optional[bool] = None
    RootAccess: Optional[RootAccessType] = None
    InstanceMetadataServiceConfiguration: Optional[       InstanceMetadataServiceConfigurationTypeDef     ] = None

class CreateNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None
    OnStart: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None

class DescribeNotebookInstanceLifecycleConfigOutputTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigArn: str
    NotebookInstanceLifecycleConfigName: str
    OnCreate: List[NotebookInstanceLifecycleHookTypeDef]
    OnStart: List[NotebookInstanceLifecycleHookTypeDef]
    LastModifiedTime: datetime
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None
    OnStart: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None

class RetryPipelineExecutionRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: str
    ClientRequestToken: str
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class UpdatePipelineExecutionRequestRequestTypeDef(BaseModel):
    PipelineExecutionArn: str
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class CreatePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str
    ClientRequestToken: str
    RoleArn: str
    PipelineDisplayName: Optional[str] = None
    PipelineDefinition: Optional[str] = None
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3LocationTypeDef] = None
    PipelineDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class UpdatePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str
    PipelineDisplayName: Optional[str] = None
    PipelineDefinition: Optional[str] = None
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3LocationTypeDef] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class InferenceExperimentScheduleTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class ListActionsRequestRequestTypeDef(BaseModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAlgorithmsInputRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListAppImageConfigsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[AppImageConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None

class ListArtifactsRequestRequestTypeDef(BaseModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAssociationsRequestRequestTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortAssociationsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAutoMLJobsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[AutoMLJobStatusType] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[AutoMLSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClusterNodesRequestRequestTypeDef(BaseModel):
    ClusterName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    InstanceGroupNameContains: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListClustersRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListCodeRepositoriesInputRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[CodeRepositorySortByType] = None
    SortOrder: Optional[CodeRepositorySortOrderType] = None

class ListCompilationJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[CompilationJobStatusType] = None
    SortBy: Optional[ListCompilationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListContextsRequestRequestTypeDef(BaseModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataQualityJobDefinitionsRequestRequestTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListDeviceFleetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ListDeviceFleetsSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListDevicesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LatestHeartbeatAfter: Optional[TimestampTypeDef] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None

class ListEdgeDeploymentPlansRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    DeviceFleetNameContains: Optional[str] = None
    SortBy: Optional[ListEdgeDeploymentPlansSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListEdgePackagingJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    ModelNameContains: Optional[str] = None
    StatusEquals: Optional[EdgePackagingJobStatusType] = None
    SortBy: Optional[ListEdgePackagingJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListEndpointConfigsInputRequestTypeDef(BaseModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListEndpointsInputRequestTypeDef(BaseModel):
    SortBy: Optional[EndpointSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[EndpointStatusType] = None

class ListExperimentsRequestRequestTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFeatureGroupsRequestRequestTypeDef(BaseModel):
    NameContains: Optional[str] = None
    FeatureGroupStatusEquals: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValueType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[FeatureGroupSortOrderType] = None
    SortBy: Optional[FeatureGroupSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFlowDefinitionsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHubContentVersionsRequestRequestTypeDef(BaseModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    MinVersion: Optional[str] = None
    MaxSchemaVersion: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[HubContentSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHubContentsRequestRequestTypeDef(BaseModel):
    HubName: str
    HubContentType: HubContentTypeType
    NameContains: Optional[str] = None
    MaxSchemaVersion: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[HubContentSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHubsRequestRequestTypeDef(BaseModel):
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[HubSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHumanTaskUisRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHyperParameterTuningJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[HyperParameterTuningJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[HyperParameterTuningJobStatusType] = None

class ListImageVersionsRequestRequestTypeDef(BaseModel):
    ImageName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ImageVersionSortByType] = None
    SortOrder: Optional[ImageVersionSortOrderType] = None

class ListImagesRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ImageSortByType] = None
    SortOrder: Optional[ImageSortOrderType] = None

class ListInferenceComponentsInputRequestTypeDef(BaseModel):
    SortBy: Optional[InferenceComponentSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[InferenceComponentStatusType] = None
    EndpointNameEquals: Optional[str] = None
    VariantNameEquals: Optional[str] = None

class ListInferenceExperimentsRequestRequestTypeDef(BaseModel):
    NameContains: Optional[str] = None
    Type: Optional[Literal["ShadowMode"]] = None
    StatusEquals: Optional[InferenceExperimentStatusType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortInferenceExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInferenceRecommendationsJobsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[RecommendationJobStatusType] = None
    SortBy: Optional[ListInferenceRecommendationsJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ModelNameEquals: Optional[str] = None
    ModelPackageVersionArnEquals: Optional[str] = None

class ListLabelingJobsForWorkteamRequestRequestTypeDef(BaseModel):
    WorkteamArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None

class ListLabelingJobsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[LabelingJobStatusType] = None

class ListLineageGroupsRequestRequestTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMlflowTrackingServersRequestRequestTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListModelBiasJobDefinitionsRequestRequestTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListModelCardExportJobsRequestRequestTypeDef(BaseModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    ModelCardExportJobNameContains: Optional[str] = None
    StatusEquals: Optional[ModelCardExportJobStatusType] = None
    SortBy: Optional[ModelCardExportJobSortByType] = None
    SortOrder: Optional[ModelCardExportJobSortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListModelCardVersionsRequestRequestTypeDef(BaseModel):
    ModelCardName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[Literal["Version"]] = None
    SortOrder: Optional[ModelCardSortOrderType] = None

class ListModelCardsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None

class ListModelExplainabilityJobDefinitionsRequestRequestTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListModelPackageGroupsInputRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None

class ListModelPackagesInputRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageType: Optional[ModelPackageTypeType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelPackageSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListModelQualityJobDefinitionsRequestRequestTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListModelsInputRequestTypeDef(BaseModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListMonitoringAlertHistoryRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: Optional[str] = None
    MonitoringAlertName: Optional[str] = None
    SortBy: Optional[MonitoringAlertHistorySortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[MonitoringAlertStatusType] = None

class ListMonitoringExecutionsRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: Optional[str] = None
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringExecutionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ScheduledTimeBefore: Optional[TimestampTypeDef] = None
    ScheduledTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[ExecutionStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None

class ListMonitoringSchedulesRequestRequestTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringScheduleSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[ScheduleStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None

class ListNotebookInstanceLifecycleConfigsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKeyType] = None
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None

class ListNotebookInstancesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[NotebookInstanceSortKeyType] = None
    SortOrder: Optional[NotebookInstanceSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[NotebookInstanceStatusType] = None
    NotebookInstanceLifecycleConfigNameContains: Optional[str] = None
    DefaultCodeRepositoryContains: Optional[str] = None
    AdditionalCodeRepositoryEquals: Optional[str] = None

class ListOptimizationJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    OptimizationContains: Optional[str] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[OptimizationJobStatusType] = None
    SortBy: Optional[ListOptimizationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListPipelineExecutionsRequestRequestTypeDef(BaseModel):
    PipelineName: str
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPipelinesRequestRequestTypeDef(BaseModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProcessingJobsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[ProcessingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProjectsInputRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ProjectSortByType] = None
    SortOrder: Optional[ProjectSortOrderType] = None

class ListResourceCatalogsRequestRequestTypeDef(BaseModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListStudioLifecycleConfigsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    AppTypeEquals: Optional[StudioLifecycleConfigAppTypeType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[StudioLifecycleConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None

class ListTrainingJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    WarmPoolStatusEquals: Optional[WarmPoolResourceStatusType] = None

class ListTransformJobsRequestRequestTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TransformJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTrialComponentsRequestRequestTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    SourceArn: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialComponentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTrialsRequestRequestTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    TrialComponentName: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialsByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class QueryFiltersTypeDef(BaseModel):
    Types: Optional[Sequence[str]] = None
    LineageTypes: Optional[Sequence[LineageTypeType]] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    ModifiedBefore: Optional[TimestampTypeDef] = None
    ModifiedAfter: Optional[TimestampTypeDef] = None
    Properties: Optional[Mapping[str, str]] = None

class CreateTrialComponentRequestRequestTypeDef(BaseModel):
    TrialComponentName: str
    DisplayName: Optional[str] = None
    Status: Optional[TrialComponentStatusTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Parameters: Optional[Mapping[str, TrialComponentParameterValueTypeDef]] = None
    InputArtifacts: Optional[Mapping[str, TrialComponentArtifactTypeDef]] = None
    OutputArtifacts: Optional[Mapping[str, TrialComponentArtifactTypeDef]] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateTrialComponentRequestRequestTypeDef(BaseModel):
    TrialComponentName: str
    DisplayName: Optional[str] = None
    Status: Optional[TrialComponentStatusTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Parameters: Optional[Mapping[str, TrialComponentParameterValueTypeDef]] = None
    ParametersToRemove: Optional[Sequence[str]] = None
    InputArtifacts: Optional[Mapping[str, TrialComponentArtifactTypeDef]] = None
    InputArtifactsToRemove: Optional[Sequence[str]] = None
    OutputArtifacts: Optional[Mapping[str, TrialComponentArtifactTypeDef]] = None
    OutputArtifactsToRemove: Optional[Sequence[str]] = None

class CreateWorkforceRequestRequestTypeDef(BaseModel):
    WorkforceName: str
    CognitoConfig: Optional[CognitoConfigTypeDef] = None
    OidcConfig: Optional[OidcConfigTypeDef] = None
    SourceIpConfig: Optional[SourceIpConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequestTypeDef] = None

class UpdateWorkforceRequestRequestTypeDef(BaseModel):
    WorkforceName: str
    SourceIpConfig: Optional[SourceIpConfigTypeDef] = None
    OidcConfig: Optional[OidcConfigTypeDef] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequestTypeDef] = None

class CustomFileSystemConfigTypeDef(BaseModel):
    EFSFileSystemConfig: Optional[EFSFileSystemConfigTypeDef] = None

class CustomFileSystemTypeDef(BaseModel):
    EFSFileSystem: Optional[EFSFileSystemTypeDef] = None

class ModelBiasBaselineConfigTypeDef(BaseModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None

class ModelExplainabilityBaselineConfigTypeDef(BaseModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None

class ModelQualityBaselineConfigTypeDef(BaseModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None

class DataQualityBaselineConfigTypeDef(BaseModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None
    StatisticsResource: Optional[MonitoringStatisticsResourceTypeDef] = None

class MonitoringBaselineConfigTypeDef(BaseModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None
    StatisticsResource: Optional[MonitoringStatisticsResourceTypeDef] = None

class DataSourceExtraOutputTypeDef(BaseModel):
    S3DataSource: Optional[S3DataSourceExtraOutputTypeDef] = None
    FileSystemDataSource: Optional[FileSystemDataSourceTypeDef] = None

class DataSourceOutputTypeDef(BaseModel):
    S3DataSource: Optional[S3DataSourceOutputTypeDef] = None
    FileSystemDataSource: Optional[FileSystemDataSourceTypeDef] = None

class DataSourceTypeDef(BaseModel):
    S3DataSource: Optional[S3DataSourceTypeDef] = None
    FileSystemDataSource: Optional[FileSystemDataSourceTypeDef] = None

class DatasetDefinitionTypeDef(BaseModel):
    AthenaDatasetDefinition: Optional[AthenaDatasetDefinitionTypeDef] = None
    RedshiftDatasetDefinition: Optional[RedshiftDatasetDefinitionTypeDef] = None
    LocalPath: Optional[str] = None
    DataDistributionType: Optional[DataDistributionTypeType] = None
    InputMode: Optional[InputModeType] = None

class DefaultSpaceStorageSettingsTypeDef(BaseModel):
    DefaultEbsStorageSettings: Optional[DefaultEbsStorageSettingsTypeDef] = None

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainId: str
    RetentionPolicy: Optional[RetentionPolicyTypeDef] = None

class InferenceComponentContainerSpecificationSummaryTypeDef(BaseModel):
    DeployedImage: Optional[DeployedImageTypeDef] = None
    ArtifactUrl: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None

class DeploymentRecommendationTypeDef(BaseModel):
    RecommendationStatus: RecommendationStatusType
    RealTimeInferenceRecommendations: Optional[       List[RealTimeInferenceRecommendationTypeDef]     ] = None

class DeploymentStageStatusSummaryTypeDef(BaseModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigOutputTypeDef
    DeploymentConfig: EdgeDeploymentConfigTypeDef
    DeploymentStatus: EdgeDeploymentStatusTypeDef

class DeploymentStageTypeDef(BaseModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigTypeDef
    DeploymentConfig: Optional[EdgeDeploymentConfigTypeDef] = None

class DescribeDeviceResponseTypeDef(BaseModel):
    DeviceArn: str
    DeviceName: str
    Description: str
    DeviceFleetName: str
    IotThingName: str
    RegistrationTime: datetime
    LatestHeartbeat: datetime
    Models: List[EdgeModelTypeDef]
    MaxModels: int
    AgentVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEdgePackagingJobResponseTypeDef(BaseModel):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: EdgeOutputConfigTypeDef
    ResourceKey: str
    EdgePackagingJobStatus: EdgePackagingJobStatusType
    EdgePackagingJobStatusMessage: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ModelArtifact: str
    ModelSignature: str
    PresetDeploymentOutput: EdgePresetDeploymentOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointInputEndpointDeletedWaitTypeDef(BaseModel):
    EndpointName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndpointInputEndpointInServiceWaitTypeDef(BaseModel):
    EndpointName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageRequestImageCreatedWaitTypeDef(BaseModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageRequestImageDeletedWaitTypeDef(BaseModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageRequestImageUpdatedWaitTypeDef(BaseModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageVersionRequestImageVersionCreatedWaitTypeDef(BaseModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageVersionRequestImageVersionDeletedWaitTypeDef(BaseModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef(BaseModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef(BaseModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef(BaseModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef(BaseModel):
    ProcessingJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef(BaseModel):
    TrainingJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef(BaseModel):
    TransformJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ExperimentSummaryTypeDef(BaseModel):
    ExperimentArn: Optional[str] = None
    ExperimentName: Optional[str] = None
    DisplayName: Optional[str] = None
    ExperimentSource: Optional[ExperimentSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class FeatureGroupSummaryTypeDef(BaseModel):
    FeatureGroupName: str
    FeatureGroupArn: str
    CreationTime: datetime
    FeatureGroupStatus: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatus: Optional[OfflineStoreStatusTypeDef] = None

class DescribeFeatureMetadataResponseTypeDef(BaseModel):
    FeatureGroupArn: str
    FeatureGroupName: str
    FeatureName: str
    FeatureType: FeatureTypeType
    CreationTime: datetime
    LastModifiedTime: datetime
    Description: str
    Parameters: List[FeatureParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FeatureMetadataTypeDef(BaseModel):
    FeatureGroupArn: Optional[str] = None
    FeatureGroupName: Optional[str] = None
    FeatureName: Optional[str] = None
    FeatureType: Optional[FeatureTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Description: Optional[str] = None
    Parameters: Optional[List[FeatureParameterTypeDef]] = None

class UpdateFeatureMetadataRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    FeatureName: str
    Description: Optional[str] = None
    ParameterAdditions: Optional[Sequence[FeatureParameterTypeDef]] = None
    ParameterRemovals: Optional[Sequence[str]] = None

class DescribeHubContentResponseTypeDef(BaseModel):
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
    HubContentDependencies: List[HubContentDependencyTypeDef]
    HubContentStatus: HubContentStatusType
    FailureReason: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHumanTaskUiResponseTypeDef(BaseModel):
    HumanTaskUiArn: str
    HumanTaskUiName: str
    HumanTaskUiStatus: HumanTaskUiStatusType
    CreationTime: datetime
    UiTemplate: UiTemplateInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InferenceExperimentSummaryTypeDef(BaseModel):
    Name: str
    Type: Literal["ShadowMode"]
    Status: InferenceExperimentStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    Schedule: Optional[InferenceExperimentScheduleOutputTypeDef] = None
    StatusReason: Optional[str] = None
    Description: Optional[str] = None
    CompletionTime: Optional[datetime] = None
    RoleArn: Optional[str] = None

class DescribeModelCardExportJobResponseTypeDef(BaseModel):
    ModelCardExportJobName: str
    ModelCardExportJobArn: str
    Status: ModelCardExportJobStatusType
    ModelCardName: str
    ModelCardVersion: int
    OutputConfig: ModelCardExportOutputConfigTypeDef
    CreatedAt: datetime
    LastModifiedAt: datetime
    FailureReason: str
    ExportArtifacts: ModelCardExportArtifactsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMonitoringExecutionsResponseTypeDef(BaseModel):
    MonitoringExecutionSummaries: List[MonitoringExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSubscribedWorkteamResponseTypeDef(BaseModel):
    SubscribedWorkteam: SubscribedWorkteamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribedWorkteamsResponseTypeDef(BaseModel):
    SubscribedWorkteams: List[SubscribedWorkteamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TrainingJobSummaryTypeDef(BaseModel):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime
    TrainingJobStatus: TrainingJobStatusType
    TrainingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    WarmPoolStatus: Optional[WarmPoolStatusTypeDef] = None

class TrialSummaryTypeDef(BaseModel):
    TrialArn: Optional[str] = None
    TrialName: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialSource: Optional[TrialSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class DesiredWeightAndCapacityTypeDef(BaseModel):
    VariantName: str
    DesiredWeight: Optional[float] = None
    DesiredInstanceCount: Optional[int] = None
    ServerlessUpdateConfig: Optional[ProductionVariantServerlessUpdateConfigTypeDef] = None

class ListStageDevicesResponseTypeDef(BaseModel):
    DeviceDeploymentSummaries: List[DeviceDeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDeviceFleetsResponseTypeDef(BaseModel):
    DeviceFleetSummaries: List[DeviceFleetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeviceSummaryTypeDef(BaseModel):
    DeviceName: str
    DeviceArn: str
    Description: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    IotThingName: Optional[str] = None
    RegistrationTime: Optional[datetime] = None
    LatestHeartbeat: Optional[datetime] = None
    Models: Optional[List[EdgeModelSummaryTypeDef]] = None
    AgentVersion: Optional[str] = None

class RegisterDevicesRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str
    Devices: Sequence[DeviceTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDevicesRequestRequestTypeDef(BaseModel):
    DeviceFleetName: str
    Devices: Sequence[DeviceTypeDef]

class ListDomainsResponseTypeDef(BaseModel):
    Domains: List[DomainDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DriftCheckBiasTypeDef(BaseModel):
    ConfigFile: Optional[FileSourceTypeDef] = None
    PreTrainingConstraints: Optional[MetricsSourceTypeDef] = None
    PostTrainingConstraints: Optional[MetricsSourceTypeDef] = None

class DriftCheckExplainabilityTypeDef(BaseModel):
    Constraints: Optional[MetricsSourceTypeDef] = None
    ConfigFile: Optional[FileSourceTypeDef] = None

class SpaceStorageSettingsTypeDef(BaseModel):
    EbsStorageSettings: Optional[EbsStorageSettingsTypeDef] = None

class ListEdgeDeploymentPlansResponseTypeDef(BaseModel):
    EdgeDeploymentPlanSummaries: List[EdgeDeploymentPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDeviceFleetReportResponseTypeDef(BaseModel):
    DeviceFleetArn: str
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfigTypeDef
    Description: str
    ReportGenerated: datetime
    DeviceStats: DeviceStatsTypeDef
    AgentVersions: List[AgentVersionTypeDef]
    ModelStats: List[EdgeModelStatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEdgePackagingJobsResponseTypeDef(BaseModel):
    EdgePackagingJobSummaries: List[EdgePackagingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEndpointConfigsOutputTypeDef(BaseModel):
    EndpointConfigs: List[EndpointConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EndpointOutputConfigurationTypeDef(BaseModel):
    EndpointName: str
    VariantName: str
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    InitialInstanceCount: Optional[int] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None

class EndpointPerformanceTypeDef(BaseModel):
    Metrics: InferenceMetricsTypeDef
    EndpointInfo: EndpointInfoTypeDef

class ListEndpointsOutputTypeDef(BaseModel):
    Endpoints: List[EndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModelConfigurationTypeDef(BaseModel):
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameters: Optional[List[EnvironmentParameterTypeDef]] = None
    CompilationJobName: Optional[str] = None

class NestedFiltersTypeDef(BaseModel):
    NestedPropertyName: str
    Filters: Sequence[FilterTypeDef]

class HyperParameterTrainingJobSummaryTypeDef(BaseModel):
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
    FinalHyperParameterTuningJobObjectiveMetric: Optional[       FinalHyperParameterTuningJobObjectiveMetricTypeDef     ] = None
    ObjectiveStatus: Optional[ObjectiveStatusType] = None

class ListFlowDefinitionsResponseTypeDef(BaseModel):
    FlowDefinitionSummaries: List[FlowDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetScalingConfigurationRecommendationRequestRequestTypeDef(BaseModel):
    InferenceRecommendationsJobName: str
    RecommendationId: Optional[str] = None
    EndpointName: Optional[str] = None
    TargetCpuUtilizationPerCore: Optional[int] = None
    ScalingPolicyObjective: Optional[ScalingPolicyObjectiveTypeDef] = None

class GetSearchSuggestionsResponseTypeDef(BaseModel):
    PropertyNameSuggestions: List[PropertyNameSuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeRepositoryInputRequestTypeDef(BaseModel):
    CodeRepositoryName: str
    GitConfig: Optional[GitConfigForUpdateTypeDef] = None

class ListHubContentVersionsResponseTypeDef(BaseModel):
    HubContentSummaries: List[HubContentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHubContentsResponseTypeDef(BaseModel):
    HubContentSummaries: List[HubContentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHubsResponseTypeDef(BaseModel):
    HubSummaries: List[HubInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class HumanLoopActivationConfigTypeDef(BaseModel):
    HumanLoopActivationConditionsConfig: HumanLoopActivationConditionsConfigTypeDef

class ListHumanTaskUisResponseTypeDef(BaseModel):
    HumanTaskUiSummaries: List[HumanTaskUiSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetworkConfigExtraOutputTypeDef(BaseModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigExtraOutputTypeDef] = None

class HyperParameterTuningResourceConfigExtraOutputTypeDef(BaseModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal["Prioritized"]] = None
    InstanceConfigs: Optional[List[HyperParameterTuningInstanceConfigTypeDef]] = None

class HyperParameterTuningResourceConfigOutputTypeDef(BaseModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal["Prioritized"]] = None
    InstanceConfigs: Optional[List[HyperParameterTuningInstanceConfigTypeDef]] = None

class HyperParameterTuningResourceConfigTypeDef(BaseModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal["Prioritized"]] = None
    InstanceConfigs: Optional[Sequence[HyperParameterTuningInstanceConfigTypeDef]] = None

class HyperParameterTuningJobSummaryTypeDef(BaseModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobArn: str
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatusType
    Strategy: HyperParameterTuningJobStrategyTypeType
    CreationTime: datetime
    TrainingJobStatusCounters: TrainingJobStatusCountersTypeDef
    ObjectiveStatusCounters: ObjectiveStatusCountersTypeDef
    HyperParameterTuningEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    ResourceLimits: Optional[ResourceLimitsTypeDef] = None

class HyperParameterTuningJobStrategyConfigTypeDef(BaseModel):
    HyperbandStrategyConfig: Optional[HyperbandStrategyConfigTypeDef] = None

class HyperParameterTuningJobWarmStartConfigExtraOutputTypeDef(BaseModel):
    ParentHyperParameterTuningJobs: List[ParentHyperParameterTuningJobTypeDef]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType

class HyperParameterTuningJobWarmStartConfigOutputTypeDef(BaseModel):
    ParentHyperParameterTuningJobs: List[ParentHyperParameterTuningJobTypeDef]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType

class HyperParameterTuningJobWarmStartConfigTypeDef(BaseModel):
    ParentHyperParameterTuningJobs: Sequence[ParentHyperParameterTuningJobTypeDef]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType

class UserContextTypeDef(BaseModel):
    UserProfileArn: Optional[str] = None
    UserProfileName: Optional[str] = None
    DomainId: Optional[str] = None
    IamIdentity: Optional[IamIdentityTypeDef] = None

class S3PresignTypeDef(BaseModel):
    IamPolicyConstraints: Optional[IamPolicyConstraintsTypeDef] = None

class ImageConfigTypeDef(BaseModel):
    RepositoryAccessMode: RepositoryAccessModeType
    RepositoryAuthConfig: Optional[RepositoryAuthConfigTypeDef] = None

class ListImagesResponseTypeDef(BaseModel):
    Images: List[ImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListImageVersionsResponseTypeDef(BaseModel):
    ImageVersions: List[ImageVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InferenceComponentSpecificationTypeDef(BaseModel):
    ComputeResourceRequirements: InferenceComponentComputeResourceRequirementsTypeDef
    ModelName: Optional[str] = None
    Container: Optional[InferenceComponentContainerSpecificationTypeDef] = None
    StartupParameters: Optional[InferenceComponentStartupParametersTypeDef] = None

class ListInferenceComponentsOutputTypeDef(BaseModel):
    InferenceComponents: List[InferenceComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListInferenceRecommendationsJobsResponseTypeDef(BaseModel):
    InferenceRecommendationsJobs: List[InferenceRecommendationsJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResourceConfigExtraOutputTypeDef(BaseModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroupTypeDef]] = None

class ResourceConfigOutputTypeDef(BaseModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroupTypeDef]] = None

class ResourceConfigTypeDef(BaseModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[Sequence[InstanceGroupTypeDef]] = None

class ParameterRangeOutputTypeDef(BaseModel):
    IntegerParameterRangeSpecification: Optional[       IntegerParameterRangeSpecificationTypeDef     ] = None
    ContinuousParameterRangeSpecification: Optional[       ContinuousParameterRangeSpecificationTypeDef     ] = None
    CategoricalParameterRangeSpecification: Optional[       CategoricalParameterRangeSpecificationOutputTypeDef     ] = None

class ParameterRangeTypeDef(BaseModel):
    IntegerParameterRangeSpecification: Optional[       IntegerParameterRangeSpecificationTypeDef     ] = None
    ContinuousParameterRangeSpecification: Optional[       ContinuousParameterRangeSpecificationTypeDef     ] = None
    CategoricalParameterRangeSpecification: Optional[       CategoricalParameterRangeSpecificationTypeDef     ] = None

class ParameterRangesExtraOutputTypeDef(BaseModel):
    IntegerParameterRanges: Optional[List[IntegerParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRangeTypeDef]] = None
    CategoricalParameterRanges: Optional[       List[CategoricalParameterRangeExtraOutputTypeDef]     ] = None
    AutoParameters: Optional[List[AutoParameterTypeDef]] = None

class ParameterRangesOutputTypeDef(BaseModel):
    IntegerParameterRanges: Optional[List[IntegerParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRangeTypeDef]] = None
    CategoricalParameterRanges: Optional[List[CategoricalParameterRangeOutputTypeDef]] = None
    AutoParameters: Optional[List[AutoParameterTypeDef]] = None

class ParameterRangesTypeDef(BaseModel):
    IntegerParameterRanges: Optional[Sequence[IntegerParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[Sequence[ContinuousParameterRangeTypeDef]] = None
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterRangeTypeDef]] = None
    AutoParameters: Optional[Sequence[AutoParameterTypeDef]] = None

class KernelGatewayImageConfigExtraOutputTypeDef(BaseModel):
    KernelSpecs: List[KernelSpecTypeDef]
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None

class KernelGatewayImageConfigOutputTypeDef(BaseModel):
    KernelSpecs: List[KernelSpecTypeDef]
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None

class KernelGatewayImageConfigTypeDef(BaseModel):
    KernelSpecs: Sequence[KernelSpecTypeDef]
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None

class LabelingJobForWorkteamSummaryTypeDef(BaseModel):
    JobReferenceCode: str
    WorkRequesterAccountId: str
    CreationTime: datetime
    LabelingJobName: Optional[str] = None
    LabelCounters: Optional[LabelCountersForWorkteamTypeDef] = None
    NumberOfHumanWorkersPerDataObject: Optional[int] = None

class LabelingJobDataSourceTypeDef(BaseModel):
    S3DataSource: Optional[LabelingJobS3DataSourceTypeDef] = None
    SnsDataSource: Optional[LabelingJobSnsDataSourceTypeDef] = None

class ListLineageGroupsResponseTypeDef(BaseModel):
    LineageGroupSummaries: List[LineageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListActionsRequestListActionsPaginateTypeDef(BaseModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAlgorithmsInputListAlgorithmsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAliasesRequestListAliasesPaginateTypeDef(BaseModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppImageConfigsRequestListAppImageConfigsPaginateTypeDef(BaseModel):
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[AppImageConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppsRequestListAppsPaginateTypeDef(BaseModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArtifactsRequestListArtifactsPaginateTypeDef(BaseModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociationsRequestListAssociationsPaginateTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortAssociationsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAutoMLJobsRequestListAutoMLJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[AutoMLJobStatusType] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[AutoMLSortByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef(BaseModel):
    AutoMLJobName: str
    StatusEquals: Optional[CandidateStatusType] = None
    CandidateNameEquals: Optional[str] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[CandidateSortByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterNodesRequestListClusterNodesPaginateTypeDef(BaseModel):
    ClusterName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    InstanceGroupNameContains: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCodeRepositoriesInputListCodeRepositoriesPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[CodeRepositorySortByType] = None
    SortOrder: Optional[CodeRepositorySortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCompilationJobsRequestListCompilationJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[CompilationJobStatusType] = None
    SortBy: Optional[ListCompilationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContextsRequestListContextsPaginateTypeDef(BaseModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataQualityJobDefinitionsRequestListDataQualityJobDefinitionsPaginateTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceFleetsRequestListDeviceFleetsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ListDeviceFleetsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicesRequestListDevicesPaginateTypeDef(BaseModel):
    LatestHeartbeatAfter: Optional[TimestampTypeDef] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEdgeDeploymentPlansRequestListEdgeDeploymentPlansPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    DeviceFleetNameContains: Optional[str] = None
    SortBy: Optional[ListEdgeDeploymentPlansSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEdgePackagingJobsRequestListEdgePackagingJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    ModelNameContains: Optional[str] = None
    StatusEquals: Optional[EdgePackagingJobStatusType] = None
    SortBy: Optional[ListEdgePackagingJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointConfigsInputListEndpointConfigsPaginateTypeDef(BaseModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointsInputListEndpointsPaginateTypeDef(BaseModel):
    SortBy: Optional[EndpointSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[EndpointStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExperimentsRequestListExperimentsPaginateTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFeatureGroupsRequestListFeatureGroupsPaginateTypeDef(BaseModel):
    NameContains: Optional[str] = None
    FeatureGroupStatusEquals: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValueType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[FeatureGroupSortOrderType] = None
    SortBy: Optional[FeatureGroupSortByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowDefinitionsRequestListFlowDefinitionsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHumanTaskUisRequestListHumanTaskUisPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHyperParameterTuningJobsRequestListHyperParameterTuningJobsPaginateTypeDef(BaseModel):
    SortBy: Optional[HyperParameterTuningJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[HyperParameterTuningJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImageVersionsRequestListImageVersionsPaginateTypeDef(BaseModel):
    ImageName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[ImageVersionSortByType] = None
    SortOrder: Optional[ImageVersionSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImagesRequestListImagesPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ImageSortByType] = None
    SortOrder: Optional[ImageSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInferenceComponentsInputListInferenceComponentsPaginateTypeDef(BaseModel):
    SortBy: Optional[InferenceComponentSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[InferenceComponentStatusType] = None
    EndpointNameEquals: Optional[str] = None
    VariantNameEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInferenceExperimentsRequestListInferenceExperimentsPaginateTypeDef(BaseModel):
    NameContains: Optional[str] = None
    Type: Optional[Literal["ShadowMode"]] = None
    StatusEquals: Optional[InferenceExperimentStatusType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortInferenceExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef(BaseModel):
    JobName: str
    Status: Optional[RecommendationJobStatusType] = None
    StepType: Optional[Literal["BENCHMARK"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInferenceRecommendationsJobsRequestListInferenceRecommendationsJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[RecommendationJobStatusType] = None
    SortBy: Optional[ListInferenceRecommendationsJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    ModelNameEquals: Optional[str] = None
    ModelPackageVersionArnEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef(BaseModel):
    WorkteamArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLabelingJobsRequestListLabelingJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[LabelingJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLineageGroupsRequestListLineageGroupsPaginateTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMlflowTrackingServersRequestListMlflowTrackingServersPaginateTypeDef(BaseModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelBiasJobDefinitionsRequestListModelBiasJobDefinitionsPaginateTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef(BaseModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    ModelCardExportJobNameContains: Optional[str] = None
    StatusEquals: Optional[ModelCardExportJobStatusType] = None
    SortBy: Optional[ModelCardExportJobSortByType] = None
    SortOrder: Optional[ModelCardExportJobSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef(BaseModel):
    ModelCardName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SortBy: Optional[Literal["Version"]] = None
    SortOrder: Optional[ModelCardSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCardsRequestListModelCardsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelExplainabilityJobDefinitionsRequestListModelExplainabilityJobDefinitionsPaginateTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelPackageGroupsInputListModelPackageGroupsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelPackagesInputListModelPackagesPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageType: Optional[ModelPackageTypeType] = None
    SortBy: Optional[ModelPackageSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelQualityJobDefinitionsRequestListModelQualityJobDefinitionsPaginateTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelsInputListModelsPaginateTypeDef(BaseModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringAlertHistoryRequestListMonitoringAlertHistoryPaginateTypeDef(BaseModel):
    MonitoringScheduleName: Optional[str] = None
    MonitoringAlertName: Optional[str] = None
    SortBy: Optional[MonitoringAlertHistorySortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[MonitoringAlertStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef(BaseModel):
    MonitoringScheduleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringExecutionsRequestListMonitoringExecutionsPaginateTypeDef(BaseModel):
    MonitoringScheduleName: Optional[str] = None
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringExecutionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    ScheduledTimeBefore: Optional[TimestampTypeDef] = None
    ScheduledTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[ExecutionStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringSchedulesRequestListMonitoringSchedulesPaginateTypeDef(BaseModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringScheduleSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[ScheduleStatusType] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringTypeEquals: Optional[MonitoringTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotebookInstanceLifecycleConfigsInputListNotebookInstanceLifecycleConfigsPaginateTypeDef(BaseModel):
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKeyType] = None
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotebookInstancesInputListNotebookInstancesPaginateTypeDef(BaseModel):
    SortBy: Optional[NotebookInstanceSortKeyType] = None
    SortOrder: Optional[NotebookInstanceSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[NotebookInstanceStatusType] = None
    NotebookInstanceLifecycleConfigNameContains: Optional[str] = None
    DefaultCodeRepositoryContains: Optional[str] = None
    AdditionalCodeRepositoryEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOptimizationJobsRequestListOptimizationJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    OptimizationContains: Optional[str] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[OptimizationJobStatusType] = None
    SortBy: Optional[ListOptimizationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineExecutionStepsRequestListPipelineExecutionStepsPaginateTypeDef(BaseModel):
    PipelineExecutionArn: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef(BaseModel):
    PipelineName: str
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef(BaseModel):
    PipelineExecutionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesRequestListPipelinesPaginateTypeDef(BaseModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProcessingJobsRequestListProcessingJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[ProcessingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceCatalogsRequestListResourceCatalogsPaginateTypeDef(BaseModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpacesRequestListSpacesPaginateTypeDef(BaseModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStageDevicesRequestListStageDevicesPaginateTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    StageName: str
    ExcludeDevicesDeployedInOtherStage: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioLifecycleConfigsRequestListStudioLifecycleConfigsPaginateTypeDef(BaseModel):
    NameContains: Optional[str] = None
    AppTypeEquals: Optional[StudioLifecycleConfigAppTypeType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[StudioLifecycleConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscribedWorkteamsRequestListSubscribedWorkteamsPaginateTypeDef(BaseModel):
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsInputListTagsPaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef(BaseModel):
    HyperParameterTuningJobName: str
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[TrainingJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingJobsRequestListTrainingJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    WarmPoolStatusEquals: Optional[WarmPoolResourceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransformJobsRequestListTransformJobsPaginateTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TransformJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrialComponentsRequestListTrialComponentsPaginateTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    SourceArn: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialComponentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrialsRequestListTrialsPaginateTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    TrialComponentName: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserProfilesRequestListUserProfilesPaginateTypeDef(BaseModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[UserProfileSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkforcesRequestListWorkforcesPaginateTypeDef(BaseModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkteamsRequestListWorkteamsPaginateTypeDef(BaseModel):
    SortBy: Optional[ListWorkteamsSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataQualityJobDefinitionsResponseTypeDef(BaseModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelBiasJobDefinitionsResponseTypeDef(BaseModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelExplainabilityJobDefinitionsResponseTypeDef(BaseModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelQualityJobDefinitionsResponseTypeDef(BaseModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMlflowTrackingServersResponseTypeDef(BaseModel):
    TrackingServerSummaries: List[TrackingServerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelCardExportJobsResponseTypeDef(BaseModel):
    ModelCardExportJobSummaries: List[ModelCardExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelCardVersionsResponseTypeDef(BaseModel):
    ModelCardVersionSummaryList: List[ModelCardVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelCardsResponseTypeDef(BaseModel):
    ModelCardSummaries: List[ModelCardSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelMetadataResponseTypeDef(BaseModel):
    ModelMetadataSummaries: List[ModelMetadataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelPackageGroupsOutputTypeDef(BaseModel):
    ModelPackageGroupSummaryList: List[ModelPackageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelPackagesOutputTypeDef(BaseModel):
    ModelPackageSummaryList: List[ModelPackageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelsOutputTypeDef(BaseModel):
    Models: List[ModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMonitoringAlertHistoryResponseTypeDef(BaseModel):
    MonitoringAlertHistory: List[MonitoringAlertHistorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMonitoringSchedulesResponseTypeDef(BaseModel):
    MonitoringScheduleSummaries: List[MonitoringScheduleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNotebookInstanceLifecycleConfigsOutputTypeDef(BaseModel):
    NotebookInstanceLifecycleConfigs: List[NotebookInstanceLifecycleConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNotebookInstancesOutputTypeDef(BaseModel):
    NotebookInstances: List[NotebookInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOptimizationJobsResponseTypeDef(BaseModel):
    OptimizationJobSummaries: List[OptimizationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPipelineExecutionsResponseTypeDef(BaseModel):
    PipelineExecutionSummaries: List[PipelineExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPipelineParametersForExecutionResponseTypeDef(BaseModel):
    PipelineParameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPipelinesResponseTypeDef(BaseModel):
    PipelineSummaries: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProcessingJobsResponseTypeDef(BaseModel):
    ProcessingJobSummaries: List[ProcessingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProjectsOutputTypeDef(BaseModel):
    ProjectSummaryList: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceCatalogsResponseTypeDef(BaseModel):
    ResourceCatalogs: List[ResourceCatalogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStudioLifecycleConfigsResponseTypeDef(BaseModel):
    StudioLifecycleConfigs: List[StudioLifecycleConfigDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTransformJobsResponseTypeDef(BaseModel):
    TransformJobSummaries: List[TransformJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUserProfilesResponseTypeDef(BaseModel):
    UserProfiles: List[UserProfileDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MemberDefinitionExtraOutputTypeDef(BaseModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinitionTypeDef] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionExtraOutputTypeDef] = None

class MemberDefinitionOutputTypeDef(BaseModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinitionTypeDef] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionOutputTypeDef] = None

class MemberDefinitionTypeDef(BaseModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinitionTypeDef] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionTypeDef] = None

class MetricSpecificationTypeDef(BaseModel):
    Predefined: Optional[PredefinedMetricSpecificationTypeDef] = None
    Customized: Optional[CustomizedMetricSpecificationTypeDef] = None

class S3ModelDataSourceTypeDef(BaseModel):
    S3Uri: str
    S3DataType: S3ModelDataTypeType
    CompressionType: ModelCompressionTypeType
    ModelAccessConfig: Optional[ModelAccessConfigTypeDef] = None
    HubAccessConfig: Optional[InferenceHubAccessConfigTypeDef] = None

class TextGenerationJobConfigOutputTypeDef(BaseModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    BaseModelName: Optional[str] = None
    TextGenerationHyperParameters: Optional[Dict[str, str]] = None
    ModelAccessConfig: Optional[ModelAccessConfigTypeDef] = None

class TextGenerationJobConfigTypeDef(BaseModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    BaseModelName: Optional[str] = None
    TextGenerationHyperParameters: Optional[Mapping[str, str]] = None
    ModelAccessConfig: Optional[ModelAccessConfigTypeDef] = None

class MonitoringAlertActionsTypeDef(BaseModel):
    ModelDashboardIndicator: Optional[ModelDashboardIndicatorActionTypeDef] = None

class ModelInfrastructureConfigTypeDef(BaseModel):
    InfrastructureType: Literal["RealTimeInference"]
    RealTimeInferenceConfig: RealTimeInferenceConfigTypeDef

class RecommendationJobStoppingConditionsOutputTypeDef(BaseModel):
    MaxInvocations: Optional[int] = None
    ModelLatencyThresholds: Optional[List[ModelLatencyThresholdTypeDef]] = None
    FlatInvocations: Optional[FlatInvocationsType] = None

class RecommendationJobStoppingConditionsTypeDef(BaseModel):
    MaxInvocations: Optional[int] = None
    ModelLatencyThresholds: Optional[Sequence[ModelLatencyThresholdTypeDef]] = None
    FlatInvocations: Optional[FlatInvocationsType] = None

class ModelMetadataSearchExpressionTypeDef(BaseModel):
    Filters: Optional[Sequence[ModelMetadataFilterTypeDef]] = None

class ModelPackageStatusDetailsTypeDef(BaseModel):
    ValidationStatuses: List[ModelPackageStatusItemTypeDef]
    ImageScanStatuses: Optional[List[ModelPackageStatusItemTypeDef]] = None

class OptimizationConfigOutputTypeDef(BaseModel):
    ModelQuantizationConfig: Optional[ModelQuantizationConfigOutputTypeDef] = None
    ModelCompilationConfig: Optional[ModelCompilationConfigOutputTypeDef] = None

class OptimizationConfigTypeDef(BaseModel):
    ModelQuantizationConfig: Optional[ModelQuantizationConfigTypeDef] = None
    ModelCompilationConfig: Optional[ModelCompilationConfigTypeDef] = None

class MonitoringResourcesTypeDef(BaseModel):
    ClusterConfig: MonitoringClusterConfigTypeDef

class MonitoringDatasetFormatExtraOutputTypeDef(BaseModel):
    Csv: Optional[MonitoringCsvDatasetFormatTypeDef] = None
    Json: Optional[MonitoringJsonDatasetFormatTypeDef] = None
    Parquet: Optional[Dict[str, Any]] = None

class MonitoringDatasetFormatOutputTypeDef(BaseModel):
    Csv: Optional[MonitoringCsvDatasetFormatTypeDef] = None
    Json: Optional[MonitoringJsonDatasetFormatTypeDef] = None
    Parquet: Optional[Dict[str, Any]] = None

class MonitoringDatasetFormatTypeDef(BaseModel):
    Csv: Optional[MonitoringCsvDatasetFormatTypeDef] = None
    Json: Optional[MonitoringJsonDatasetFormatTypeDef] = None
    Parquet: Optional[Mapping[str, Any]] = None

class MonitoringOutputTypeDef(BaseModel):
    S3Output: MonitoringS3OutputTypeDef

class OfflineStoreConfigTypeDef(BaseModel):
    S3StorageConfig: S3StorageConfigTypeDef
    DisableGlueTableCreation: Optional[bool] = None
    DataCatalogConfig: Optional[DataCatalogConfigTypeDef] = None
    TableFormat: Optional[TableFormatType] = None

class OnlineStoreConfigTypeDef(BaseModel):
    SecurityConfig: Optional[OnlineStoreSecurityConfigTypeDef] = None
    EnableOnlineStore: Optional[bool] = None
    TtlDuration: Optional[TtlDurationTypeDef] = None
    StorageType: Optional[StorageTypeType] = None

class OnlineStoreConfigUpdateTypeDef(BaseModel):
    TtlDuration: Optional[TtlDurationTypeDef] = None

class OptimizationJobModelSourceS3TypeDef(BaseModel):
    S3Uri: Optional[str] = None
    ModelAccessConfig: Optional[OptimizationModelAccessConfigTypeDef] = None

class OutputConfigTypeDef(BaseModel):
    S3OutputLocation: str
    TargetDevice: Optional[TargetDeviceType] = None
    TargetPlatform: Optional[TargetPlatformTypeDef] = None
    CompilerOptions: Optional[str] = None
    KmsKeyId: Optional[str] = None

class PendingProductionVariantSummaryTypeDef(BaseModel):
    VariantName: str
    DeployedImages: Optional[List[DeployedImageTypeDef]] = None
    CurrentWeight: Optional[float] = None
    DesiredWeight: Optional[float] = None
    CurrentInstanceCount: Optional[int] = None
    DesiredInstanceCount: Optional[int] = None
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    AcceleratorType: Optional[ProductionVariantAcceleratorTypeType] = None
    VariantStatus: Optional[List[ProductionVariantStatusTypeDef]] = None
    CurrentServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    DesiredServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScalingTypeDef] = None
    RoutingConfig: Optional[ProductionVariantRoutingConfigTypeDef] = None

class ProductionVariantSummaryTypeDef(BaseModel):
    VariantName: str
    DeployedImages: Optional[List[DeployedImageTypeDef]] = None
    CurrentWeight: Optional[float] = None
    DesiredWeight: Optional[float] = None
    CurrentInstanceCount: Optional[int] = None
    DesiredInstanceCount: Optional[int] = None
    VariantStatus: Optional[List[ProductionVariantStatusTypeDef]] = None
    CurrentServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    DesiredServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScalingTypeDef] = None
    RoutingConfig: Optional[ProductionVariantRoutingConfigTypeDef] = None

class ProcessingResourcesTypeDef(BaseModel):
    ClusterConfig: ProcessingClusterConfigTypeDef

class ProcessingOutputTypeDef(BaseModel):
    OutputName: str
    S3Output: Optional[ProcessingS3OutputTypeDef] = None
    FeatureStoreOutput: Optional[ProcessingFeatureStoreOutputTypeDef] = None
    AppManaged: Optional[bool] = None

class ProductionVariantTypeDef(BaseModel):
    VariantName: str
    ModelName: Optional[str] = None
    InitialInstanceCount: Optional[int] = None
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    InitialVariantWeight: Optional[float] = None
    AcceleratorType: Optional[ProductionVariantAcceleratorTypeType] = None
    CoreDumpConfig: Optional[ProductionVariantCoreDumpConfigTypeDef] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    VolumeSizeInGB: Optional[int] = None
    ModelDataDownloadTimeoutInSeconds: Optional[int] = None
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int] = None
    EnableSSMAccess: Optional[bool] = None
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScalingTypeDef] = None
    RoutingConfig: Optional[ProductionVariantRoutingConfigTypeDef] = None
    InferenceAmiVersion: Optional[Literal["al2-ami-sagemaker-inference-gpu-2"]] = None

class SuggestionQueryTypeDef(BaseModel):
    PropertyNameQuery: Optional[PropertyNameQueryTypeDef] = None

class ServiceCatalogProvisioningDetailsExtraOutputTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameterTypeDef]] = None

class ServiceCatalogProvisioningDetailsOutputTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameterTypeDef]] = None

class ServiceCatalogProvisioningDetailsTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[Sequence[ProvisioningParameterTypeDef]] = None

class ServiceCatalogProvisioningUpdateDetailsTypeDef(BaseModel):
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningParameters: Optional[Sequence[ProvisioningParameterTypeDef]] = None

class PublicWorkforceTaskPriceTypeDef(BaseModel):
    AmountInUsd: Optional[USDTypeDef] = None

class QueryLineageResponseTypeDef(BaseModel):
    Vertices: List[VertexTypeDef]
    Edges: List[EdgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RecommendationJobOutputConfigTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None
    CompiledOutputConfig: Optional[RecommendationJobCompiledOutputConfigTypeDef] = None

class RecommendationJobContainerConfigOutputTypeDef(BaseModel):
    Domain: Optional[str] = None
    Task: Optional[str] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    PayloadConfig: Optional[RecommendationJobPayloadConfigOutputTypeDef] = None
    NearestModelName: Optional[str] = None
    SupportedInstanceTypes: Optional[List[str]] = None
    SupportedEndpointType: Optional[RecommendationJobSupportedEndpointTypeType] = None
    DataInputConfig: Optional[str] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class RecommendationJobContainerConfigTypeDef(BaseModel):
    Domain: Optional[str] = None
    Task: Optional[str] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    PayloadConfig: Optional[RecommendationJobPayloadConfigTypeDef] = None
    NearestModelName: Optional[str] = None
    SupportedInstanceTypes: Optional[Sequence[str]] = None
    SupportedEndpointType: Optional[RecommendationJobSupportedEndpointTypeType] = None
    DataInputConfig: Optional[str] = None
    SupportedResponseMIMETypes: Optional[Sequence[str]] = None

class RenderUiTemplateRequestRequestTypeDef(BaseModel):
    Task: RenderableTaskTypeDef
    RoleArn: str
    UiTemplate: Optional[UiTemplateTypeDef] = None
    HumanTaskUiArn: Optional[str] = None

class RenderUiTemplateResponseTypeDef(BaseModel):
    RenderedContent: str
    Errors: List[RenderingErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRequestRequestTypeDef(BaseModel):
    Resource: ResourceTypeType
    SearchExpression: Optional["SearchExpressionTypeDef"] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[Sequence[VisibilityConditionsTypeDef]] = None

class SelectiveExecutionConfigExtraOutputTypeDef(BaseModel):
    SelectedSteps: List[SelectedStepTypeDef]
    SourcePipelineExecutionArn: Optional[str] = None

class SelectiveExecutionConfigOutputTypeDef(BaseModel):
    SelectedSteps: List[SelectedStepTypeDef]
    SourcePipelineExecutionArn: Optional[str] = None

class SelectiveExecutionConfigTypeDef(BaseModel):
    SelectedSteps: Sequence[SelectedStepTypeDef]
    SourcePipelineExecutionArn: Optional[str] = None

class ShadowModeConfigOutputTypeDef(BaseModel):
    SourceModelVariantName: str
    ShadowModelVariants: List[ShadowModelVariantConfigTypeDef]

class ShadowModeConfigTypeDef(BaseModel):
    SourceModelVariantName: str
    ShadowModelVariants: Sequence[ShadowModelVariantConfigTypeDef]

class TrafficPatternOutputTypeDef(BaseModel):
    TrafficType: Optional[TrafficTypeType] = None
    Phases: Optional[List[PhaseTypeDef]] = None
    Stairs: Optional[StairsTypeDef] = None

class TrafficPatternTypeDef(BaseModel):
    TrafficType: Optional[TrafficTypeType] = None
    Phases: Optional[Sequence[PhaseTypeDef]] = None
    Stairs: Optional[StairsTypeDef] = None

class TrainingImageConfigTypeDef(BaseModel):
    TrainingRepositoryAccessMode: TrainingRepositoryAccessModeType
    TrainingRepositoryAuthConfig: Optional[TrainingRepositoryAuthConfigTypeDef] = None

class TransformDataSourceTypeDef(BaseModel):
    S3DataSource: TransformS3DataSourceTypeDef

class WorkforceTypeDef(BaseModel):
    WorkforceName: str
    WorkforceArn: str
    LastUpdatedDate: Optional[datetime] = None
    SourceIpConfig: Optional[SourceIpConfigOutputTypeDef] = None
    SubDomain: Optional[str] = None
    CognitoConfig: Optional[CognitoConfigTypeDef] = None
    OidcConfig: Optional[OidcConfigForResponseTypeDef] = None
    CreateDate: Optional[datetime] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigResponseTypeDef] = None
    Status: Optional[WorkforceStatusType] = None
    FailureReason: Optional[str] = None

class ListActionsResponseTypeDef(BaseModel):
    ActionSummaries: List[ActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAppsResponseTypeDef(BaseModel):
    Apps: List[AppDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DomainSettingsForUpdateTypeDef(BaseModel):
    RStudioServerProDomainSettingsForUpdate: Optional[       RStudioServerProDomainSettingsForUpdateTypeDef     ] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    DockerSettings: Optional[DockerSettingsTypeDef] = None
    AmazonQSettings: Optional[AmazonQSettingsTypeDef] = None

class DomainSettingsOutputTypeDef(BaseModel):
    SecurityGroupIds: Optional[List[str]] = None
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettingsTypeDef] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    DockerSettings: Optional[DockerSettingsOutputTypeDef] = None
    AmazonQSettings: Optional[AmazonQSettingsTypeDef] = None

class DomainSettingsTypeDef(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettingsTypeDef] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    DockerSettings: Optional[DockerSettingsTypeDef] = None
    AmazonQSettings: Optional[AmazonQSettingsTypeDef] = None

class ArtifactSummaryTypeDef(BaseModel):
    ArtifactArn: Optional[str] = None
    ArtifactName: Optional[str] = None
    Source: Optional[ArtifactSourceOutputTypeDef] = None
    ArtifactType: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class CreateArtifactRequestRequestTypeDef(BaseModel):
    Source: ArtifactSourceTypeDef
    ArtifactType: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DeleteArtifactRequestRequestTypeDef(BaseModel):
    ArtifactArn: Optional[str] = None
    Source: Optional[ArtifactSourceTypeDef] = None

class AsyncInferenceConfigOutputTypeDef(BaseModel):
    OutputConfig: AsyncInferenceOutputConfigOutputTypeDef
    ClientConfig: Optional[AsyncInferenceClientConfigTypeDef] = None

class AsyncInferenceConfigTypeDef(BaseModel):
    OutputConfig: AsyncInferenceOutputConfigTypeDef
    ClientConfig: Optional[AsyncInferenceClientConfigTypeDef] = None

class TabularJobConfigOutputTypeDef(BaseModel):
    TargetAttributeName: str
    CandidateGenerationConfig: Optional[CandidateGenerationConfigOutputTypeDef] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    FeatureSpecificationS3Uri: Optional[str] = None
    Mode: Optional[AutoMLModeType] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    ProblemType: Optional[ProblemTypeType] = None
    SampleWeightAttributeName: Optional[str] = None

class TimeSeriesForecastingJobConfigOutputTypeDef(BaseModel):
    ForecastFrequency: str
    ForecastHorizon: int
    TimeSeriesConfig: TimeSeriesConfigOutputTypeDef
    FeatureSpecificationS3Uri: Optional[str] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    ForecastQuantiles: Optional[List[str]] = None
    Transformations: Optional[TimeSeriesTransformationsOutputTypeDef] = None
    HolidayConfig: Optional[List[HolidayConfigAttributesTypeDef]] = None
    CandidateGenerationConfig: Optional[CandidateGenerationConfigOutputTypeDef] = None

class TabularJobConfigTypeDef(BaseModel):
    TargetAttributeName: str
    CandidateGenerationConfig: Optional[CandidateGenerationConfigTypeDef] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    FeatureSpecificationS3Uri: Optional[str] = None
    Mode: Optional[AutoMLModeType] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    ProblemType: Optional[ProblemTypeType] = None
    SampleWeightAttributeName: Optional[str] = None

class TimeSeriesForecastingJobConfigTypeDef(BaseModel):
    ForecastFrequency: str
    ForecastHorizon: int
    TimeSeriesConfig: TimeSeriesConfigTypeDef
    FeatureSpecificationS3Uri: Optional[str] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    ForecastQuantiles: Optional[Sequence[str]] = None
    Transformations: Optional[TimeSeriesTransformationsTypeDef] = None
    HolidayConfig: Optional[Sequence[HolidayConfigAttributesTypeDef]] = None
    CandidateGenerationConfig: Optional[CandidateGenerationConfigTypeDef] = None

class AutoMLChannelTypeDef(BaseModel):
    TargetAttributeName: str
    DataSource: Optional[AutoMLDataSourceTypeDef] = None
    CompressionType: Optional[CompressionTypeType] = None
    ContentType: Optional[str] = None
    ChannelType: Optional[AutoMLChannelTypeType] = None
    SampleWeightAttributeName: Optional[str] = None

class AutoMLJobChannelTypeDef(BaseModel):
    ChannelType: Optional[AutoMLChannelTypeType] = None
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    DataSource: Optional[AutoMLDataSourceTypeDef] = None

class ListAutoMLJobsResponseTypeDef(BaseModel):
    AutoMLJobSummaries: List[AutoMLJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoMLResolvedAttributesTypeDef(BaseModel):
    AutoMLJobObjective: Optional[AutoMLJobObjectiveTypeDef] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    AutoMLProblemTypeResolvedAttributes: Optional[       AutoMLProblemTypeResolvedAttributesTypeDef     ] = None

class AutoMLJobConfigOutputTypeDef(BaseModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    SecurityConfig: Optional[AutoMLSecurityConfigOutputTypeDef] = None
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfigOutputTypeDef] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfigTypeDef] = None
    Mode: Optional[AutoMLModeType] = None

class LabelingJobAlgorithmsConfigOutputTypeDef(BaseModel):
    LabelingJobAlgorithmSpecificationArn: str
    InitialActiveLearningModelArn: Optional[str] = None
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfigOutputTypeDef] = None

class AutoMLJobConfigTypeDef(BaseModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    SecurityConfig: Optional[AutoMLSecurityConfigTypeDef] = None
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfigTypeDef] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfigTypeDef] = None
    Mode: Optional[AutoMLModeType] = None

class LabelingJobAlgorithmsConfigTypeDef(BaseModel):
    LabelingJobAlgorithmSpecificationArn: str
    InitialActiveLearningModelArn: Optional[str] = None
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfigTypeDef] = None

class ModelMetricsTypeDef(BaseModel):
    ModelQuality: Optional[ModelQualityTypeDef] = None
    ModelDataQuality: Optional[ModelDataQualityTypeDef] = None
    Bias: Optional[BiasTypeDef] = None
    Explainability: Optional[ExplainabilityTypeDef] = None

class PipelineExecutionStepMetadataTypeDef(BaseModel):
    TrainingJob: Optional[TrainingJobStepMetadataTypeDef] = None
    ProcessingJob: Optional[ProcessingJobStepMetadataTypeDef] = None
    TransformJob: Optional[TransformJobStepMetadataTypeDef] = None
    TuningJob: Optional[TuningJobStepMetaDataTypeDef] = None
    Model: Optional[ModelStepMetadataTypeDef] = None
    RegisterModel: Optional[RegisterModelStepMetadataTypeDef] = None
    Condition: Optional[ConditionStepMetadataTypeDef] = None
    Callback: Optional[CallbackStepMetadataTypeDef] = None
    Lambda: Optional[LambdaStepMetadataTypeDef] = None
    EMR: Optional[EMRStepMetadataTypeDef] = None
    QualityCheck: Optional[QualityCheckStepMetadataTypeDef] = None
    ClarifyCheck: Optional[ClarifyCheckStepMetadataTypeDef] = None
    Fail: Optional[FailStepMetadataTypeDef] = None
    AutoMLJob: Optional[AutoMLJobStepMetadataTypeDef] = None

class AutoMLCandidateTypeDef(BaseModel):
    CandidateName: str
    ObjectiveStatus: ObjectiveStatusType
    CandidateSteps: List[AutoMLCandidateStepTypeDef]
    CandidateStatus: CandidateStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    FinalAutoMLJobObjectiveMetric: Optional[FinalAutoMLJobObjectiveMetricTypeDef] = None
    InferenceContainers: Optional[List[AutoMLContainerDefinitionTypeDef]] = None
    EndTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    CandidateProperties: Optional[CandidatePropertiesTypeDef] = None
    InferenceContainerDefinitions: Optional[       Dict[AutoMLProcessingUnitType, List[AutoMLContainerDefinitionTypeDef]] = None

class BlueGreenUpdatePolicyTypeDef(BaseModel):
    TrafficRoutingConfiguration: TrafficRoutingConfigTypeDef
    TerminationWaitInSeconds: Optional[int] = None
    MaximumExecutionTimeoutInSeconds: Optional[int] = None

class EndpointInputConfigurationOutputTypeDef(BaseModel):
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameterRanges: Optional[EnvironmentParameterRangesOutputTypeDef] = None

class EndpointInputConfigurationTypeDef(BaseModel):
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameterRanges: Optional[EnvironmentParameterRangesTypeDef] = None

class ClarifyExplainerConfigOutputTypeDef(BaseModel):
    ShapConfig: ClarifyShapConfigTypeDef
    EnableExplanations: Optional[str] = None
    InferenceConfig: Optional[ClarifyInferenceConfigOutputTypeDef] = None

class ClarifyExplainerConfigTypeDef(BaseModel):
    ShapConfig: ClarifyShapConfigTypeDef
    EnableExplanations: Optional[str] = None
    InferenceConfig: Optional[ClarifyInferenceConfigTypeDef] = None

class ClusterInstanceGroupDetailsTypeDef(BaseModel):
    CurrentCount: Optional[int] = None
    TargetCount: Optional[int] = None
    InstanceGroupName: Optional[str] = None
    InstanceType: Optional[ClusterInstanceTypeType] = None
    LifeCycleConfig: Optional[ClusterLifeCycleConfigTypeDef] = None
    ExecutionRole: Optional[str] = None
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[List[ClusterInstanceStorageConfigTypeDef]] = None

class ClusterInstanceGroupSpecificationTypeDef(BaseModel):
    InstanceCount: int
    InstanceGroupName: str
    InstanceType: ClusterInstanceTypeType
    LifeCycleConfig: ClusterLifeCycleConfigTypeDef
    ExecutionRole: str
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[Sequence[ClusterInstanceStorageConfigTypeDef]] = None

class ClusterNodeDetailsTypeDef(BaseModel):
    InstanceGroupName: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceStatus: Optional[ClusterInstanceStatusDetailsTypeDef] = None
    InstanceType: Optional[ClusterInstanceTypeType] = None
    LaunchTime: Optional[datetime] = None
    LifeCycleConfig: Optional[ClusterLifeCycleConfigTypeDef] = None
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[List[ClusterInstanceStorageConfigTypeDef]] = None
    PrivatePrimaryIp: Optional[str] = None
    PrivateDnsHostname: Optional[str] = None
    Placement: Optional[ClusterInstancePlacementTypeDef] = None

class ListClusterNodesResponseTypeDef(BaseModel):
    NextToken: str
    ClusterNodeSummaries: List[ClusterNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCodeRepositoriesOutputTypeDef(BaseModel):
    CodeRepositorySummaryList: List[CodeRepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FeatureDefinitionTypeDef(BaseModel):
    FeatureName: str
    FeatureType: FeatureTypeType
    CollectionType: Optional[CollectionTypeType] = None
    CollectionConfig: Optional[CollectionConfigTypeDef] = None

class ListContextsResponseTypeDef(BaseModel):
    ContextSummaries: List[ContextSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class QueryLineageRequestRequestTypeDef(BaseModel):
    StartArns: Optional[Sequence[str]] = None
    Direction: Optional[DirectionType] = None
    IncludeEdges: Optional[bool] = None
    Filters: Optional[QueryFiltersTypeDef] = None
    MaxDepth: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ChannelExtraOutputTypeDef(BaseModel):
    ChannelName: str
    DataSource: DataSourceExtraOutputTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfigTypeDef] = None

class ChannelOutputTypeDef(BaseModel):
    ChannelName: str
    DataSource: DataSourceOutputTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfigTypeDef] = None

class ChannelTypeDef(BaseModel):
    ChannelName: str
    DataSource: DataSourceTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfigTypeDef] = None

class ProcessingInputTypeDef(BaseModel):
    InputName: str
    AppManaged: Optional[bool] = None
    S3Input: Optional[ProcessingS3InputTypeDef] = None
    DatasetDefinition: Optional[DatasetDefinitionTypeDef] = None

class DefaultSpaceSettingsOutputTypeDef(BaseModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutputTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutputTypeDef] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsOutputTypeDef] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettingsTypeDef] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfigTypeDef] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfigTypeDef]] = None

class DefaultSpaceSettingsTypeDef(BaseModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsTypeDef] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettingsTypeDef] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfigTypeDef] = None
    CustomFileSystemConfigs: Optional[Sequence[CustomFileSystemConfigTypeDef]] = None

class UserSettingsOutputTypeDef(BaseModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SharingSettings: Optional[SharingSettingsTypeDef] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutputTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutputTypeDef] = None
    TensorBoardAppSettings: Optional[TensorBoardAppSettingsTypeDef] = None
    RStudioServerProAppSettings: Optional[RStudioServerProAppSettingsTypeDef] = None
    RSessionAppSettings: Optional[RSessionAppSettingsOutputTypeDef] = None
    CanvasAppSettings: Optional[CanvasAppSettingsOutputTypeDef] = None
    CodeEditorAppSettings: Optional[CodeEditorAppSettingsOutputTypeDef] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsOutputTypeDef] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettingsTypeDef] = None
    DefaultLandingUri: Optional[str] = None
    StudioWebPortal: Optional[StudioWebPortalType] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfigTypeDef] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfigTypeDef]] = None
    StudioWebPortalSettings: Optional[StudioWebPortalSettingsOutputTypeDef] = None

class UserSettingsTypeDef(BaseModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SharingSettings: Optional[SharingSettingsTypeDef] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsTypeDef] = None
    TensorBoardAppSettings: Optional[TensorBoardAppSettingsTypeDef] = None
    RStudioServerProAppSettings: Optional[RStudioServerProAppSettingsTypeDef] = None
    RSessionAppSettings: Optional[RSessionAppSettingsTypeDef] = None
    CanvasAppSettings: Optional[CanvasAppSettingsTypeDef] = None
    CodeEditorAppSettings: Optional[CodeEditorAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsTypeDef] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettingsTypeDef] = None
    DefaultLandingUri: Optional[str] = None
    StudioWebPortal: Optional[StudioWebPortalType] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfigTypeDef] = None
    CustomFileSystemConfigs: Optional[Sequence[CustomFileSystemConfigTypeDef]] = None
    StudioWebPortalSettings: Optional[StudioWebPortalSettingsTypeDef] = None

class InferenceComponentSpecificationSummaryTypeDef(BaseModel):
    ModelName: Optional[str] = None
    Container: Optional[InferenceComponentContainerSpecificationSummaryTypeDef] = None
    StartupParameters: Optional[InferenceComponentStartupParametersTypeDef] = None
    ComputeResourceRequirements: Optional[       InferenceComponentComputeResourceRequirementsTypeDef     ] = None

class DescribeEdgeDeploymentPlanResponseTypeDef(BaseModel):
    EdgeDeploymentPlanArn: str
    EdgeDeploymentPlanName: str
    ModelConfigs: List[EdgeDeploymentModelConfigTypeDef]
    DeviceFleetName: str
    EdgeDeploymentSuccess: int
    EdgeDeploymentPending: int
    EdgeDeploymentFailed: int
    Stages: List[DeploymentStageStatusSummaryTypeDef]
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEdgeDeploymentPlanRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    ModelConfigs: Sequence[EdgeDeploymentModelConfigTypeDef]
    DeviceFleetName: str
    Stages: Optional[Sequence[DeploymentStageTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEdgeDeploymentStageRequestRequestTypeDef(BaseModel):
    EdgeDeploymentPlanName: str
    Stages: Sequence[DeploymentStageTypeDef]

class ListExperimentsResponseTypeDef(BaseModel):
    ExperimentSummaries: List[ExperimentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFeatureGroupsResponseTypeDef(BaseModel):
    FeatureGroupSummaries: List[FeatureGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListInferenceExperimentsResponseTypeDef(BaseModel):
    InferenceExperiments: List[InferenceExperimentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrainingJobsResponseTypeDef(BaseModel):
    TrainingJobSummaries: List[TrainingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrialsResponseTypeDef(BaseModel):
    TrialSummaries: List[TrialSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef(BaseModel):
    EndpointName: str
    DesiredWeightsAndCapacities: Sequence[DesiredWeightAndCapacityTypeDef]

class ListDevicesResponseTypeDef(BaseModel):
    DeviceSummaries: List[DeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DriftCheckBaselinesTypeDef(BaseModel):
    Bias: Optional[DriftCheckBiasTypeDef] = None
    Explainability: Optional[DriftCheckExplainabilityTypeDef] = None
    ModelQuality: Optional[DriftCheckModelQualityTypeDef] = None
    ModelDataQuality: Optional[DriftCheckModelDataQualityTypeDef] = None

class SpaceSettingsOutputTypeDef(BaseModel):
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutputTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutputTypeDef] = None
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettingsOutputTypeDef] = None
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettingsTypeDef] = None
    CustomFileSystems: Optional[List[CustomFileSystemTypeDef]] = None

class SpaceSettingsSummaryTypeDef(BaseModel):
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettingsTypeDef] = None

class SpaceSettingsTypeDef(BaseModel):
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsTypeDef] = None
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettingsTypeDef] = None
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettingsTypeDef] = None
    CustomFileSystems: Optional[Sequence[CustomFileSystemTypeDef]] = None

class InferenceRecommendationTypeDef(BaseModel):
    EndpointConfiguration: EndpointOutputConfigurationTypeDef
    ModelConfiguration: ModelConfigurationTypeDef
    RecommendationId: Optional[str] = None
    Metrics: Optional[RecommendationMetricsTypeDef] = None
    InvocationEndTime: Optional[datetime] = None
    InvocationStartTime: Optional[datetime] = None

class RecommendationJobInferenceBenchmarkTypeDef(BaseModel):
    ModelConfiguration: ModelConfigurationTypeDef
    Metrics: Optional[RecommendationMetricsTypeDef] = None
    EndpointMetrics: Optional[InferenceMetricsTypeDef] = None
    EndpointConfiguration: Optional[EndpointOutputConfigurationTypeDef] = None
    FailureReason: Optional[str] = None
    InvocationEndTime: Optional[datetime] = None
    InvocationStartTime: Optional[datetime] = None

class SearchExpressionTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NestedFilters: Optional[Sequence[NestedFiltersTypeDef]] = None
    SubExpressions: Optional[Sequence[Dict[str, Any]]] = None
    Operator: Optional[BooleanOperatorType] = None

class ListTrainingJobsForHyperParameterTuningJobResponseTypeDef(BaseModel):
    TrainingJobSummaries: List[HyperParameterTrainingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHyperParameterTuningJobsResponseTypeDef(BaseModel):
    HyperParameterTuningJobSummaries: List[HyperParameterTuningJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociationSummaryTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    SourceName: Optional[str] = None
    DestinationName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None

class DescribeActionResponseTypeDef(BaseModel):
    ActionName: str
    ActionArn: str
    Source: ActionSourceTypeDef
    ActionType: str
    Description: str
    Status: ActionStatusType
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    MetadataProperties: MetadataPropertiesTypeDef
    LineageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeArtifactResponseTypeDef(BaseModel):
    ArtifactName: str
    ArtifactArn: str
    Source: ArtifactSourceOutputTypeDef
    ArtifactType: str
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    MetadataProperties: MetadataPropertiesTypeDef
    LineageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContextResponseTypeDef(BaseModel):
    ContextName: str
    ContextArn: str
    Source: ContextSourceTypeDef
    ContextType: str
    Description: str
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    LineageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExperimentResponseTypeDef(BaseModel):
    ExperimentName: str
    ExperimentArn: str
    DisplayName: str
    Source: ExperimentSourceTypeDef
    Description: str
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLineageGroupResponseTypeDef(BaseModel):
    LineageGroupName: str
    LineageGroupArn: str
    DisplayName: str
    Description: str
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMlflowTrackingServerResponseTypeDef(BaseModel):
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
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelCardResponseTypeDef(BaseModel):
    ModelCardArn: str
    ModelCardName: str
    ModelCardVersion: int
    Content: str
    ModelCardStatus: ModelCardStatusType
    SecurityConfig: ModelCardSecurityConfigTypeDef
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ModelCardProcessingStatus: ModelCardProcessingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelPackageGroupOutputTypeDef(BaseModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    ModelPackageGroupDescription: str
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePipelineResponseTypeDef(BaseModel):
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
    CreatedBy: UserContextTypeDef
    LastModifiedBy: UserContextTypeDef
    ParallelismConfiguration: ParallelismConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrialComponentResponseTypeDef(BaseModel):
    TrialComponentName: str
    TrialComponentArn: str
    DisplayName: str
    Source: TrialComponentSourceTypeDef
    Status: TrialComponentStatusTypeDef
    StartTime: datetime
    EndTime: datetime
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    Parameters: Dict[str, TrialComponentParameterValueTypeDef]
    InputArtifacts: Dict[str, TrialComponentArtifactTypeDef]
    OutputArtifacts: Dict[str, TrialComponentArtifactTypeDef]
    MetadataProperties: MetadataPropertiesTypeDef
    Metrics: List[TrialComponentMetricSummaryTypeDef]
    LineageGroupArn: str
    Sources: List[TrialComponentSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrialResponseTypeDef(BaseModel):
    TrialName: str
    TrialArn: str
    DisplayName: str
    ExperimentName: str
    Source: TrialSourceTypeDef
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    MetadataProperties: MetadataPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTypeDef(BaseModel):
    ExperimentName: Optional[str] = None
    ExperimentArn: Optional[str] = None
    DisplayName: Optional[str] = None
    Source: Optional[ExperimentSourceTypeDef] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class ModelCardTypeDef(BaseModel):
    ModelCardArn: Optional[str] = None
    ModelCardName: Optional[str] = None
    ModelCardVersion: Optional[int] = None
    Content: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SecurityConfig: Optional[ModelCardSecurityConfigTypeDef] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    ModelId: Optional[str] = None
    RiskRating: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None

class ModelDashboardModelCardTypeDef(BaseModel):
    ModelCardArn: Optional[str] = None
    ModelCardName: Optional[str] = None
    ModelCardVersion: Optional[int] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SecurityConfig: Optional[ModelCardSecurityConfigTypeDef] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    ModelId: Optional[str] = None
    RiskRating: Optional[str] = None

class ModelPackageGroupTypeDef(BaseModel):
    ModelPackageGroupName: Optional[str] = None
    ModelPackageGroupArn: Optional[str] = None
    ModelPackageGroupDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    ModelPackageGroupStatus: Optional[ModelPackageGroupStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None

class PipelineTypeDef(BaseModel):
    PipelineArn: Optional[str] = None
    PipelineName: Optional[str] = None
    PipelineDisplayName: Optional[str] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    PipelineStatus: Optional[PipelineStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastRunTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class TrialComponentSimpleSummaryTypeDef(BaseModel):
    TrialComponentName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    TrialComponentSource: Optional[TrialComponentSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None

class TrialComponentSummaryTypeDef(BaseModel):
    TrialComponentName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialComponentSource: Optional[TrialComponentSourceTypeDef] = None
    Status: Optional[TrialComponentStatusTypeDef] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None

class WorkerAccessConfigurationTypeDef(BaseModel):
    S3Presign: Optional[S3PresignTypeDef] = None

class CreateInferenceComponentInputRequestTypeDef(BaseModel):
    InferenceComponentName: str
    EndpointName: str
    VariantName: str
    Specification: InferenceComponentSpecificationTypeDef
    RuntimeConfig: InferenceComponentRuntimeConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateInferenceComponentInputRequestTypeDef(BaseModel):
    InferenceComponentName: str
    Specification: Optional[InferenceComponentSpecificationTypeDef] = None
    RuntimeConfig: Optional[InferenceComponentRuntimeConfigTypeDef] = None

class HyperParameterSpecificationOutputTypeDef(BaseModel):
    Name: str
    Type: ParameterTypeType
    Description: Optional[str] = None
    Range: Optional[ParameterRangeOutputTypeDef] = None
    IsTunable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    DefaultValue: Optional[str] = None

class HyperParameterSpecificationTypeDef(BaseModel):
    Name: str
    Type: ParameterTypeType
    Description: Optional[str] = None
    Range: Optional[ParameterRangeTypeDef] = None
    IsTunable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    DefaultValue: Optional[str] = None

class HyperParameterTuningJobConfigExtraOutputTypeDef(BaseModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimitsTypeDef
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfigTypeDef] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    ParameterRanges: Optional[ParameterRangesExtraOutputTypeDef] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteriaTypeDef] = None
    RandomSeed: Optional[int] = None

class HyperParameterTuningJobConfigOutputTypeDef(BaseModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimitsTypeDef
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfigTypeDef] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    ParameterRanges: Optional[ParameterRangesOutputTypeDef] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteriaTypeDef] = None
    RandomSeed: Optional[int] = None

class HyperParameterTuningJobConfigTypeDef(BaseModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimitsTypeDef
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfigTypeDef] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    ParameterRanges: Optional[ParameterRangesTypeDef] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteriaTypeDef] = None
    RandomSeed: Optional[int] = None

class AppImageConfigDetailsTypeDef(BaseModel):
    AppImageConfigArn: Optional[str] = None
    AppImageConfigName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigOutputTypeDef] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigOutputTypeDef] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigOutputTypeDef] = None

class DescribeAppImageConfigResponseTypeDef(BaseModel):
    AppImageConfigArn: str
    AppImageConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    KernelGatewayImageConfig: KernelGatewayImageConfigOutputTypeDef
    JupyterLabAppImageConfig: JupyterLabAppImageConfigOutputTypeDef
    CodeEditorAppImageConfig: CodeEditorAppImageConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppImageConfigRequestRequestTypeDef(BaseModel):
    AppImageConfigName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigTypeDef] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigTypeDef] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigTypeDef] = None

class UpdateAppImageConfigRequestRequestTypeDef(BaseModel):
    AppImageConfigName: str
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigTypeDef] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigTypeDef] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigTypeDef] = None

class ListLabelingJobsForWorkteamResponseTypeDef(BaseModel):
    LabelingJobSummaryList: List[LabelingJobForWorkteamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LabelingJobInputConfigExtraOutputTypeDef(BaseModel):
    DataSource: LabelingJobDataSourceTypeDef
    DataAttributes: Optional[LabelingJobDataAttributesExtraOutputTypeDef] = None

class LabelingJobInputConfigOutputTypeDef(BaseModel):
    DataSource: LabelingJobDataSourceTypeDef
    DataAttributes: Optional[LabelingJobDataAttributesOutputTypeDef] = None

class LabelingJobInputConfigTypeDef(BaseModel):
    DataSource: LabelingJobDataSourceTypeDef
    DataAttributes: Optional[LabelingJobDataAttributesTypeDef] = None

class TargetTrackingScalingPolicyConfigurationTypeDef(BaseModel):
    MetricSpecification: Optional[MetricSpecificationTypeDef] = None
    TargetValue: Optional[float] = None

class AdditionalModelDataSourceTypeDef(BaseModel):
    ChannelName: str
    S3DataSource: S3ModelDataSourceTypeDef

class ModelDataSourceTypeDef(BaseModel):
    S3DataSource: Optional[S3ModelDataSourceTypeDef] = None

class MonitoringAlertSummaryTypeDef(BaseModel):
    MonitoringAlertName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    AlertStatus: MonitoringAlertStatusType
    DatapointsToAlert: int
    EvaluationPeriod: int
    Actions: MonitoringAlertActionsTypeDef

class ModelVariantConfigSummaryTypeDef(BaseModel):
    ModelName: str
    VariantName: str
    InfrastructureConfig: ModelInfrastructureConfigTypeDef
    Status: ModelVariantStatusType

class ModelVariantConfigTypeDef(BaseModel):
    ModelName: str
    VariantName: str
    InfrastructureConfig: ModelInfrastructureConfigTypeDef

class ListModelMetadataRequestListModelMetadataPaginateTypeDef(BaseModel):
    SearchExpression: Optional[ModelMetadataSearchExpressionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelMetadataRequestRequestTypeDef(BaseModel):
    SearchExpression: Optional[ModelMetadataSearchExpressionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchTransformInputExtraOutputTypeDef(BaseModel):
    DataCapturedDestinationS3Uri: str
    DatasetFormat: MonitoringDatasetFormatExtraOutputTypeDef
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

class BatchTransformInputOutputTypeDef(BaseModel):
    DataCapturedDestinationS3Uri: str
    DatasetFormat: MonitoringDatasetFormatOutputTypeDef
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

class BatchTransformInputTypeDef(BaseModel):
    DataCapturedDestinationS3Uri: str
    DatasetFormat: MonitoringDatasetFormatTypeDef
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

class MonitoringOutputConfigExtraOutputTypeDef(BaseModel):
    MonitoringOutputs: List[MonitoringOutputTypeDef]
    KmsKeyId: Optional[str] = None

class MonitoringOutputConfigOutputTypeDef(BaseModel):
    MonitoringOutputs: List[MonitoringOutputTypeDef]
    KmsKeyId: Optional[str] = None

class MonitoringOutputConfigTypeDef(BaseModel):
    MonitoringOutputs: Sequence[MonitoringOutputTypeDef]
    KmsKeyId: Optional[str] = None

class OptimizationJobModelSourceTypeDef(BaseModel):
    S3: Optional[OptimizationJobModelSourceS3TypeDef] = None

class CreateCompilationJobRequestRequestTypeDef(BaseModel):
    CompilationJobName: str
    RoleArn: str
    OutputConfig: OutputConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    ModelPackageVersionArn: Optional[str] = None
    InputConfig: Optional[InputConfigTypeDef] = None
    VpcConfig: Optional[NeoVpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeCompilationJobResponseTypeDef(BaseModel):
    CompilationJobName: str
    CompilationJobArn: str
    CompilationJobStatus: CompilationJobStatusType
    CompilationStartTime: datetime
    CompilationEndTime: datetime
    StoppingCondition: StoppingConditionTypeDef
    InferenceImage: str
    ModelPackageVersionArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    ModelArtifacts: ModelArtifactsTypeDef
    ModelDigests: ModelDigestsTypeDef
    RoleArn: str
    InputConfig: InputConfigTypeDef
    OutputConfig: OutputConfigTypeDef
    VpcConfig: NeoVpcConfigOutputTypeDef
    DerivedInformation: DerivedInformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingDeploymentSummaryTypeDef(BaseModel):
    EndpointConfigName: str
    ProductionVariants: Optional[List[PendingProductionVariantSummaryTypeDef]] = None
    StartTime: Optional[datetime] = None
    ShadowProductionVariants: Optional[List[PendingProductionVariantSummaryTypeDef]] = None

class ProcessingOutputConfigExtraOutputTypeDef(BaseModel):
    Outputs: List[ProcessingOutputTypeDef]
    KmsKeyId: Optional[str] = None

class ProcessingOutputConfigOutputTypeDef(BaseModel):
    Outputs: List[ProcessingOutputTypeDef]
    KmsKeyId: Optional[str] = None

class ProcessingOutputConfigTypeDef(BaseModel):
    Outputs: Sequence[ProcessingOutputTypeDef]
    KmsKeyId: Optional[str] = None

class UpdateTrainingJobRequestRequestTypeDef(BaseModel):
    TrainingJobName: str
    ProfilerConfig: Optional[ProfilerConfigForUpdateTypeDef] = None
    ProfilerRuleConfigurations: Optional[Sequence[ProfilerRuleConfigurationUnionTypeDef]] = None
    ResourceConfig: Optional[ResourceConfigForUpdateTypeDef] = None
    RemoteDebugConfig: Optional[RemoteDebugConfigForUpdateTypeDef] = None

class GetSearchSuggestionsRequestRequestTypeDef(BaseModel):
    Resource: ResourceTypeType
    SuggestionQuery: Optional[SuggestionQueryTypeDef] = None

class DescribeProjectOutputTypeDef(BaseModel):
    ProjectArn: str
    ProjectName: str
    ProjectId: str
    ProjectDescription: str
    ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsOutputTypeDef
    ServiceCatalogProvisionedProductDetails: ServiceCatalogProvisionedProductDetailsTypeDef
    ProjectStatus: ProjectStatusType
    CreatedBy: UserContextTypeDef
    CreationTime: datetime
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectTypeDef(BaseModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    ProjectId: Optional[str] = None
    ProjectDescription: Optional[str] = None
    ServiceCatalogProvisioningDetails: Optional[       ServiceCatalogProvisioningDetailsOutputTypeDef     ] = None
    ServiceCatalogProvisionedProductDetails: Optional[       ServiceCatalogProvisionedProductDetailsTypeDef     ] = None
    ProjectStatus: Optional[ProjectStatusType] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None

class CreateProjectInputRequestTypeDef(BaseModel):
    ProjectName: str
    ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsTypeDef
    ProjectDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateProjectInputRequestTypeDef(BaseModel):
    ProjectName: str
    ProjectDescription: Optional[str] = None
    ServiceCatalogProvisioningUpdateDetails: Optional[       ServiceCatalogProvisioningUpdateDetailsTypeDef     ] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class HumanLoopConfigOutputTypeDef(BaseModel):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    TaskTimeLimitInSeconds: Optional[int] = None
    TaskKeywords: Optional[List[str]] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPriceTypeDef] = None

class HumanLoopConfigTypeDef(BaseModel):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    TaskTimeLimitInSeconds: Optional[int] = None
    TaskKeywords: Optional[Sequence[str]] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPriceTypeDef] = None

class HumanTaskConfigOutputTypeDef(BaseModel):
    WorkteamArn: str
    UiConfig: UiConfigTypeDef
    PreHumanTaskLambdaArn: str
    TaskTitle: str
    TaskDescription: str
    NumberOfHumanWorkersPerDataObject: int
    TaskTimeLimitInSeconds: int
    AnnotationConsolidationConfig: AnnotationConsolidationConfigTypeDef
    TaskKeywords: Optional[List[str]] = None
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    MaxConcurrentTaskCount: Optional[int] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPriceTypeDef] = None

class HumanTaskConfigTypeDef(BaseModel):
    WorkteamArn: str
    UiConfig: UiConfigTypeDef
    PreHumanTaskLambdaArn: str
    TaskTitle: str
    TaskDescription: str
    NumberOfHumanWorkersPerDataObject: int
    TaskTimeLimitInSeconds: int
    AnnotationConsolidationConfig: AnnotationConsolidationConfigTypeDef
    TaskKeywords: Optional[Sequence[str]] = None
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    MaxConcurrentTaskCount: Optional[int] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPriceTypeDef] = None

class DescribePipelineExecutionResponseTypeDef(BaseModel):
    PipelineArn: str
    PipelineExecutionArn: str
    PipelineExecutionDisplayName: str
    PipelineExecutionStatus: PipelineExecutionStatusType
    PipelineExecutionDescription: str
    PipelineExperimentConfig: PipelineExperimentConfigTypeDef
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedBy: UserContextTypeDef
    ParallelismConfiguration: ParallelismConfigurationTypeDef
    SelectiveExecutionConfig: SelectiveExecutionConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PipelineExecutionTypeDef(BaseModel):
    PipelineArn: Optional[str] = None
    PipelineExecutionArn: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineExecutionStatus: Optional[PipelineExecutionStatusType] = None
    PipelineExecutionDescription: Optional[str] = None
    PipelineExperimentConfig: Optional[PipelineExperimentConfigTypeDef] = None
    FailureReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfigOutputTypeDef] = None
    PipelineParameters: Optional[List[ParameterTypeDef]] = None

class StartPipelineExecutionRequestRequestTypeDef(BaseModel):
    PipelineName: str
    ClientRequestToken: str
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineParameters: Optional[Sequence[ParameterTypeDef]] = None
    PipelineExecutionDescription: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfigTypeDef] = None

class AlgorithmSpecificationExtraOutputTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfigTypeDef] = None

class AlgorithmSpecificationOutputTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfigTypeDef] = None

class AlgorithmSpecificationTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfigTypeDef] = None

class TransformInputTypeDef(BaseModel):
    DataSource: TransformDataSourceTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    SplitType: Optional[SplitTypeType] = None

class DescribeWorkforceResponseTypeDef(BaseModel):
    Workforce: WorkforceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkforcesResponseTypeDef(BaseModel):
    Workforces: List[WorkforceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateWorkforceResponseTypeDef(BaseModel):
    Workforce: WorkforceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArtifactsResponseTypeDef(BaseModel):
    ArtifactSummaries: List[ArtifactSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoMLProblemTypeConfigOutputTypeDef(BaseModel):
    ImageClassificationJobConfig: Optional[ImageClassificationJobConfigTypeDef] = None
    TextClassificationJobConfig: Optional[TextClassificationJobConfigTypeDef] = None
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfigOutputTypeDef] = None
    TabularJobConfig: Optional[TabularJobConfigOutputTypeDef] = None
    TextGenerationJobConfig: Optional[TextGenerationJobConfigOutputTypeDef] = None

class AutoMLProblemTypeConfigTypeDef(BaseModel):
    ImageClassificationJobConfig: Optional[ImageClassificationJobConfigTypeDef] = None
    TextClassificationJobConfig: Optional[TextClassificationJobConfigTypeDef] = None
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfigTypeDef] = None
    TabularJobConfig: Optional[TabularJobConfigTypeDef] = None
    TextGenerationJobConfig: Optional[TextGenerationJobConfigTypeDef] = None

class CreateAutoMLJobRequestRequestTypeDef(BaseModel):
    AutoMLJobName: str
    InputDataConfig: Sequence[AutoMLChannelTypeDef]
    OutputDataConfig: AutoMLOutputDataConfigTypeDef
    RoleArn: str
    ProblemType: Optional[ProblemTypeType] = None
    AutoMLJobObjective: Optional[AutoMLJobObjectiveTypeDef] = None
    AutoMLJobConfig: Optional[AutoMLJobConfigTypeDef] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ModelDeployConfig: Optional[ModelDeployConfigTypeDef] = None

class PipelineExecutionStepTypeDef(BaseModel):
    StepName: Optional[str] = None
    StepDisplayName: Optional[str] = None
    StepDescription: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    StepStatus: Optional[StepStatusType] = None
    CacheHitResult: Optional[CacheHitResultTypeDef] = None
    FailureReason: Optional[str] = None
    Metadata: Optional[PipelineExecutionStepMetadataTypeDef] = None
    AttemptCount: Optional[int] = None
    SelectiveExecutionResult: Optional[SelectiveExecutionResultTypeDef] = None

class DescribeAutoMLJobResponseTypeDef(BaseModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    InputDataConfig: List[AutoMLChannelTypeDef]
    OutputDataConfig: AutoMLOutputDataConfigTypeDef
    RoleArn: str
    AutoMLJobObjective: AutoMLJobObjectiveTypeDef
    ProblemType: ProblemTypeType
    AutoMLJobConfig: AutoMLJobConfigOutputTypeDef
    CreationTime: datetime
    EndTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    PartialFailureReasons: List[AutoMLPartialFailureReasonTypeDef]
    BestCandidate: AutoMLCandidateTypeDef
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    GenerateCandidateDefinitionsOnly: bool
    AutoMLJobArtifacts: AutoMLJobArtifactsTypeDef
    ResolvedAttributes: ResolvedAttributesTypeDef
    ModelDeployConfig: ModelDeployConfigTypeDef
    ModelDeployResult: ModelDeployResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCandidatesForAutoMLJobResponseTypeDef(BaseModel):
    Candidates: List[AutoMLCandidateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeploymentConfigOutputTypeDef(BaseModel):
    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicyTypeDef] = None
    RollingUpdatePolicy: Optional[RollingUpdatePolicyTypeDef] = None
    AutoRollbackConfiguration: Optional[AutoRollbackConfigOutputTypeDef] = None

class DeploymentConfigTypeDef(BaseModel):
    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicyTypeDef] = None
    RollingUpdatePolicy: Optional[RollingUpdatePolicyTypeDef] = None
    AutoRollbackConfiguration: Optional[AutoRollbackConfigTypeDef] = None

class RecommendationJobInputConfigOutputTypeDef(BaseModel):
    ModelPackageVersionArn: Optional[str] = None
    ModelName: Optional[str] = None
    JobDurationInSeconds: Optional[int] = None
    TrafficPattern: Optional[TrafficPatternOutputTypeDef] = None
    ResourceLimit: Optional[RecommendationJobResourceLimitTypeDef] = None
    EndpointConfigurations: Optional[List[EndpointInputConfigurationOutputTypeDef]] = None
    VolumeKmsKeyId: Optional[str] = None
    ContainerConfig: Optional[RecommendationJobContainerConfigOutputTypeDef] = None
    Endpoints: Optional[List[EndpointInfoTypeDef]] = None
    VpcConfig: Optional[RecommendationJobVpcConfigOutputTypeDef] = None

class RecommendationJobInputConfigTypeDef(BaseModel):
    ModelPackageVersionArn: Optional[str] = None
    ModelName: Optional[str] = None
    JobDurationInSeconds: Optional[int] = None
    TrafficPattern: Optional[TrafficPatternTypeDef] = None
    ResourceLimit: Optional[RecommendationJobResourceLimitTypeDef] = None
    EndpointConfigurations: Optional[Sequence[EndpointInputConfigurationTypeDef]] = None
    VolumeKmsKeyId: Optional[str] = None
    ContainerConfig: Optional[RecommendationJobContainerConfigTypeDef] = None
    Endpoints: Optional[Sequence[EndpointInfoTypeDef]] = None
    VpcConfig: Optional[RecommendationJobVpcConfigTypeDef] = None

class ExplainerConfigOutputTypeDef(BaseModel):
    ClarifyExplainerConfig: Optional[ClarifyExplainerConfigOutputTypeDef] = None

class ExplainerConfigTypeDef(BaseModel):
    ClarifyExplainerConfig: Optional[ClarifyExplainerConfigTypeDef] = None

class DescribeClusterResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterName: str
    ClusterStatus: ClusterStatusType
    CreationTime: datetime
    FailureMessage: str
    InstanceGroups: List[ClusterInstanceGroupDetailsTypeDef]
    VpcConfig: VpcConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str
    InstanceGroups: Sequence[ClusterInstanceGroupSpecificationTypeDef]
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str
    InstanceGroups: Sequence[ClusterInstanceGroupSpecificationTypeDef]

class DescribeClusterNodeResponseTypeDef(BaseModel):
    NodeDetails: ClusterNodeDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFeatureGroupRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    RecordIdentifierFeatureName: str
    EventTimeFeatureName: str
    FeatureDefinitions: Sequence[FeatureDefinitionTypeDef]
    OnlineStoreConfig: Optional[OnlineStoreConfigTypeDef] = None
    OfflineStoreConfig: Optional[OfflineStoreConfigTypeDef] = None
    ThroughputConfig: Optional[ThroughputConfigTypeDef] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeFeatureGroupResponseTypeDef(BaseModel):
    FeatureGroupArn: str
    FeatureGroupName: str
    RecordIdentifierFeatureName: str
    EventTimeFeatureName: str
    FeatureDefinitions: List[FeatureDefinitionTypeDef]
    CreationTime: datetime
    LastModifiedTime: datetime
    OnlineStoreConfig: OnlineStoreConfigTypeDef
    OfflineStoreConfig: OfflineStoreConfigTypeDef
    ThroughputConfig: ThroughputConfigDescriptionTypeDef
    RoleArn: str
    FeatureGroupStatus: FeatureGroupStatusType
    OfflineStoreStatus: OfflineStoreStatusTypeDef
    LastUpdateStatus: LastUpdateStatusTypeDef
    FailureReason: str
    Description: str
    NextToken: str
    OnlineStoreTotalSizeBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class FeatureGroupTypeDef(BaseModel):
    FeatureGroupArn: Optional[str] = None
    FeatureGroupName: Optional[str] = None
    RecordIdentifierFeatureName: Optional[str] = None
    EventTimeFeatureName: Optional[str] = None
    FeatureDefinitions: Optional[List[FeatureDefinitionTypeDef]] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    OnlineStoreConfig: Optional[OnlineStoreConfigTypeDef] = None
    OfflineStoreConfig: Optional[OfflineStoreConfigTypeDef] = None
    RoleArn: Optional[str] = None
    FeatureGroupStatus: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatus: Optional[OfflineStoreStatusTypeDef] = None
    LastUpdateStatus: Optional[LastUpdateStatusTypeDef] = None
    FailureReason: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class UpdateFeatureGroupRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    FeatureAdditions: Optional[Sequence[FeatureDefinitionTypeDef]] = None
    OnlineStoreConfig: Optional[OnlineStoreConfigUpdateTypeDef] = None
    ThroughputConfig: Optional[ThroughputConfigUpdateTypeDef] = None

class HyperParameterTrainingJobDefinitionExtraOutputTypeDef(BaseModel):
    AlgorithmSpecification: HyperParameterAlgorithmSpecificationExtraOutputTypeDef
    RoleArn: str
    OutputDataConfig: OutputDataConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    DefinitionName: Optional[str] = None
    TuningObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    HyperParameterRanges: Optional[ParameterRangesExtraOutputTypeDef] = None
    StaticHyperParameters: Optional[Dict[str, str]] = None
    InputDataConfig: Optional[List[ChannelExtraOutputTypeDef]] = None
    VpcConfig: Optional[VpcConfigExtraOutputTypeDef] = None
    ResourceConfig: Optional[ResourceConfigExtraOutputTypeDef] = None
    HyperParameterTuningResourceConfig: Optional[       HyperParameterTuningResourceConfigExtraOutputTypeDef     ] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfigTypeDef] = None
    RetryStrategy: Optional[RetryStrategyTypeDef] = None
    Environment: Optional[Dict[str, str]] = None

class HyperParameterTrainingJobDefinitionOutputTypeDef(BaseModel):
    AlgorithmSpecification: HyperParameterAlgorithmSpecificationOutputTypeDef
    RoleArn: str
    OutputDataConfig: OutputDataConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    DefinitionName: Optional[str] = None
    TuningObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    HyperParameterRanges: Optional[ParameterRangesOutputTypeDef] = None
    StaticHyperParameters: Optional[Dict[str, str]] = None
    InputDataConfig: Optional[List[ChannelOutputTypeDef]] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    ResourceConfig: Optional[ResourceConfigOutputTypeDef] = None
    HyperParameterTuningResourceConfig: Optional[       HyperParameterTuningResourceConfigOutputTypeDef     ] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfigTypeDef] = None
    RetryStrategy: Optional[RetryStrategyTypeDef] = None
    Environment: Optional[Dict[str, str]] = None

class TrainingJobDefinitionOutputTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    InputDataConfig: List[ChannelOutputTypeDef]
    OutputDataConfig: OutputDataConfigTypeDef
    ResourceConfig: ResourceConfigOutputTypeDef
    StoppingCondition: StoppingConditionTypeDef
    HyperParameters: Optional[Dict[str, str]] = None

class HyperParameterTrainingJobDefinitionTypeDef(BaseModel):
    AlgorithmSpecification: HyperParameterAlgorithmSpecificationTypeDef
    RoleArn: str
    OutputDataConfig: OutputDataConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    DefinitionName: Optional[str] = None
    TuningObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    HyperParameterRanges: Optional[ParameterRangesTypeDef] = None
    StaticHyperParameters: Optional[Mapping[str, str]] = None
    InputDataConfig: Optional[Sequence[ChannelTypeDef]] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    ResourceConfig: Optional[ResourceConfigTypeDef] = None
    HyperParameterTuningResourceConfig: Optional[       HyperParameterTuningResourceConfigTypeDef     ] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfigTypeDef] = None
    RetryStrategy: Optional[RetryStrategyTypeDef] = None
    Environment: Optional[Mapping[str, str]] = None

class TrainingJobDefinitionTypeDef(BaseModel):
    TrainingInputMode: TrainingInputModeType
    InputDataConfig: Sequence[ChannelTypeDef]
    OutputDataConfig: OutputDataConfigTypeDef
    ResourceConfig: ResourceConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    HyperParameters: Optional[Mapping[str, str]] = None

class DescribeDomainResponseTypeDef(BaseModel):
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
    DefaultUserSettings: UserSettingsOutputTypeDef
    DomainSettings: DomainSettingsOutputTypeDef
    AppNetworkAccessType: AppNetworkAccessTypeType
    HomeEfsFileSystemKmsKeyId: str
    SubnetIds: List[str]
    Url: str
    VpcId: str
    KmsKeyId: str
    AppSecurityGroupManagement: AppSecurityGroupManagementType
    DefaultSpaceSettings: DefaultSpaceSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserProfileResponseTypeDef(BaseModel):
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
    UserSettings: UserSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    AuthMode: AuthModeType
    DefaultUserSettings: UserSettingsTypeDef
    SubnetIds: Sequence[str]
    VpcId: str
    DomainSettings: Optional[DomainSettingsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AppNetworkAccessType: Optional[AppNetworkAccessTypeType] = None
    HomeEfsFileSystemKmsKeyId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagementType] = None
    DefaultSpaceSettings: Optional[DefaultSpaceSettingsTypeDef] = None

class CreateUserProfileRequestRequestTypeDef(BaseModel):
    DomainId: str
    UserProfileName: str
    SingleSignOnUserIdentifier: Optional[str] = None
    SingleSignOnUserValue: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UserSettings: Optional[UserSettingsTypeDef] = None

class UpdateDomainRequestRequestTypeDef(BaseModel):
    DomainId: str
    DefaultUserSettings: Optional[UserSettingsTypeDef] = None
    DomainSettingsForUpdate: Optional[DomainSettingsForUpdateTypeDef] = None
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagementType] = None
    DefaultSpaceSettings: Optional[DefaultSpaceSettingsTypeDef] = None
    SubnetIds: Optional[Sequence[str]] = None
    AppNetworkAccessType: Optional[AppNetworkAccessTypeType] = None

class UpdateUserProfileRequestRequestTypeDef(BaseModel):
    DomainId: str
    UserProfileName: str
    UserSettings: Optional[UserSettingsTypeDef] = None

class DescribeInferenceComponentOutputTypeDef(BaseModel):
    InferenceComponentName: str
    InferenceComponentArn: str
    EndpointName: str
    EndpointArn: str
    VariantName: str
    FailureReason: str
    Specification: InferenceComponentSpecificationSummaryTypeDef
    RuntimeConfig: InferenceComponentRuntimeConfigSummaryTypeDef
    CreationTime: datetime
    LastModifiedTime: datetime
    InferenceComponentStatus: InferenceComponentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpaceResponseTypeDef(BaseModel):
    DomainId: str
    SpaceArn: str
    SpaceName: str
    HomeEfsFileSystemUid: str
    Status: SpaceStatusType
    LastModifiedTime: datetime
    CreationTime: datetime
    FailureReason: str
    SpaceSettings: SpaceSettingsOutputTypeDef
    OwnershipSettings: OwnershipSettingsTypeDef
    SpaceSharingSettings: SpaceSharingSettingsTypeDef
    SpaceDisplayName: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class SpaceDetailsTypeDef(BaseModel):
    DomainId: Optional[str] = None
    SpaceName: Optional[str] = None
    Status: Optional[SpaceStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    SpaceSettingsSummary: Optional[SpaceSettingsSummaryTypeDef] = None
    SpaceSharingSettingsSummary: Optional[SpaceSharingSettingsSummaryTypeDef] = None
    OwnershipSettingsSummary: Optional[OwnershipSettingsSummaryTypeDef] = None
    SpaceDisplayName: Optional[str] = None

class CreateSpaceRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpaceName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    SpaceSettings: Optional[SpaceSettingsTypeDef] = None
    OwnershipSettings: Optional[OwnershipSettingsTypeDef] = None
    SpaceSharingSettings: Optional[SpaceSharingSettingsTypeDef] = None
    SpaceDisplayName: Optional[str] = None

class UpdateSpaceRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpaceName: str
    SpaceSettings: Optional[SpaceSettingsTypeDef] = None
    SpaceDisplayName: Optional[str] = None

class InferenceRecommendationsJobStepTypeDef(BaseModel):
    StepType: Literal["BENCHMARK"]
    JobName: str
    Status: RecommendationJobStatusType
    InferenceBenchmark: Optional[RecommendationJobInferenceBenchmarkTypeDef] = None

class SearchRequestSearchPaginateTypeDef(BaseModel):
    Resource: ResourceTypeType
    SearchExpression: Optional[SearchExpressionTypeDef] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[Sequence[VisibilityConditionsTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociationsResponseTypeDef(BaseModel):
    AssociationSummaries: List[AssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TrialTypeDef(BaseModel):
    TrialName: Optional[str] = None
    TrialArn: Optional[str] = None
    DisplayName: Optional[str] = None
    ExperimentName: Optional[str] = None
    Source: Optional[TrialSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    TrialComponentSummaries: Optional[List[TrialComponentSimpleSummaryTypeDef]] = None

class ListTrialComponentsResponseTypeDef(BaseModel):
    TrialComponentSummaries: List[TrialComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class WorkteamTypeDef(BaseModel):
    WorkteamName: str
    MemberDefinitions: List[MemberDefinitionOutputTypeDef]
    WorkteamArn: str
    Description: str
    WorkforceArn: Optional[str] = None
    ProductListingIds: Optional[List[str]] = None
    SubDomain: Optional[str] = None
    CreateDate: Optional[datetime] = None
    LastUpdatedDate: Optional[datetime] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfigurationTypeDef] = None

class TrainingSpecificationOutputTypeDef(BaseModel):
    TrainingImage: str
    SupportedTrainingInstanceTypes: List[TrainingInstanceTypeType]
    TrainingChannels: List[ChannelSpecificationOutputTypeDef]
    TrainingImageDigest: Optional[str] = None
    SupportedHyperParameters: Optional[List[HyperParameterSpecificationOutputTypeDef]] = None
    SupportsDistributedTraining: Optional[bool] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None
    SupportedTuningJobObjectiveMetrics: Optional[       List[HyperParameterTuningJobObjectiveTypeDef]     ] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class TrainingSpecificationTypeDef(BaseModel):
    TrainingImage: str
    SupportedTrainingInstanceTypes: Sequence[TrainingInstanceTypeType]
    TrainingChannels: Sequence[ChannelSpecificationTypeDef]
    TrainingImageDigest: Optional[str] = None
    SupportedHyperParameters: Optional[Sequence[HyperParameterSpecificationTypeDef]] = None
    SupportsDistributedTraining: Optional[bool] = None
    MetricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None
    SupportedTuningJobObjectiveMetrics: Optional[       Sequence[HyperParameterTuningJobObjectiveTypeDef]     ] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class ListAppImageConfigsResponseTypeDef(BaseModel):
    AppImageConfigs: List[AppImageConfigDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LabelingJobSummaryTypeDef(BaseModel):
    LabelingJobName: str
    LabelingJobArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LabelingJobStatus: LabelingJobStatusType
    LabelCounters: LabelCountersTypeDef
    WorkteamArn: str
    PreHumanTaskLambdaArn: str
    AnnotationConsolidationLambdaArn: Optional[str] = None
    FailureReason: Optional[str] = None
    LabelingJobOutput: Optional[LabelingJobOutputTypeDef] = None
    InputConfig: Optional[LabelingJobInputConfigOutputTypeDef] = None

class CreateWorkteamRequestRequestTypeDef(BaseModel):
    WorkteamName: str
    MemberDefinitions: Sequence[MemberDefinitionUnionTypeDef]
    Description: str
    WorkforceName: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateWorkteamRequestRequestTypeDef(BaseModel):
    WorkteamName: str
    MemberDefinitions: Optional[Sequence[MemberDefinitionUnionTypeDef]] = None
    Description: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfigurationTypeDef] = None

class ScalingPolicyTypeDef(BaseModel):
    TargetTracking: Optional[TargetTrackingScalingPolicyConfigurationTypeDef] = None

class ContainerDefinitionExtraOutputTypeDef(BaseModel):
    ContainerHostname: Optional[str] = None
    Image: Optional[str] = None
    ImageConfig: Optional[ImageConfigTypeDef] = None
    Mode: Optional[ContainerModeType] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None
    AdditionalModelDataSources: Optional[List[AdditionalModelDataSourceTypeDef]] = None
    Environment: Optional[Dict[str, str]] = None
    ModelPackageName: Optional[str] = None
    InferenceSpecificationName: Optional[str] = None
    MultiModelConfig: Optional[MultiModelConfigTypeDef] = None

class ContainerDefinitionOutputTypeDef(BaseModel):
    ContainerHostname: Optional[str] = None
    Image: Optional[str] = None
    ImageConfig: Optional[ImageConfigTypeDef] = None
    Mode: Optional[ContainerModeType] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None
    AdditionalModelDataSources: Optional[List[AdditionalModelDataSourceTypeDef]] = None
    Environment: Optional[Dict[str, str]] = None
    ModelPackageName: Optional[str] = None
    InferenceSpecificationName: Optional[str] = None
    MultiModelConfig: Optional[MultiModelConfigTypeDef] = None

class ContainerDefinitionTypeDef(BaseModel):
    ContainerHostname: Optional[str] = None
    Image: Optional[str] = None
    ImageConfig: Optional[ImageConfigTypeDef] = None
    Mode: Optional[ContainerModeType] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None
    AdditionalModelDataSources: Optional[Sequence[AdditionalModelDataSourceTypeDef]] = None
    Environment: Optional[Mapping[str, str]] = None
    ModelPackageName: Optional[str] = None
    InferenceSpecificationName: Optional[str] = None
    MultiModelConfig: Optional[MultiModelConfigTypeDef] = None

class ModelPackageContainerDefinitionExtraOutputTypeDef(BaseModel):
    Image: str
    ContainerHostname: Optional[str] = None
    ImageDigest: Optional[str] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None
    ProductId: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None
    ModelInput: Optional[ModelInputTypeDef] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    NearestModelName: Optional[str] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class ModelPackageContainerDefinitionOutputTypeDef(BaseModel):
    Image: str
    ContainerHostname: Optional[str] = None
    ImageDigest: Optional[str] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None
    ProductId: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None
    ModelInput: Optional[ModelInputTypeDef] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    NearestModelName: Optional[str] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class ModelPackageContainerDefinitionTypeDef(BaseModel):
    Image: str
    ContainerHostname: Optional[str] = None
    ImageDigest: Optional[str] = None
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None
    ProductId: Optional[str] = None
    Environment: Optional[Mapping[str, str]] = None
    ModelInput: Optional[ModelInputTypeDef] = None
    Framework: Optional[str] = None
    FrameworkVersion: Optional[str] = None
    NearestModelName: Optional[str] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class SourceAlgorithmTypeDef(BaseModel):
    AlgorithmName: str
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None

class ListMonitoringAlertsResponseTypeDef(BaseModel):
    MonitoringAlertSummaries: List[MonitoringAlertSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInferenceExperimentResponseTypeDef(BaseModel):
    Arn: str
    Name: str
    Type: Literal["ShadowMode"]
    Schedule: InferenceExperimentScheduleOutputTypeDef
    Status: InferenceExperimentStatusType
    StatusReason: str
    Description: str
    CreationTime: datetime
    CompletionTime: datetime
    LastModifiedTime: datetime
    RoleArn: str
    EndpointMetadata: EndpointMetadataTypeDef
    ModelVariants: List[ModelVariantConfigSummaryTypeDef]
    DataStorageConfig: InferenceExperimentDataStorageConfigOutputTypeDef
    ShadowModeConfig: ShadowModeConfigOutputTypeDef
    KmsKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceExperimentRequestRequestTypeDef(BaseModel):
    Name: str
    Type: Literal["ShadowMode"]
    RoleArn: str
    EndpointName: str
    ModelVariants: Sequence[ModelVariantConfigTypeDef]
    ShadowModeConfig: ShadowModeConfigTypeDef
    Schedule: Optional[InferenceExperimentScheduleTypeDef] = None
    Description: Optional[str] = None
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfigTypeDef] = None
    KmsKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StopInferenceExperimentRequestRequestTypeDef(BaseModel):
    Name: str
    ModelVariantActions: Mapping[str, ModelVariantActionType]
    DesiredModelVariants: Optional[Sequence[ModelVariantConfigTypeDef]] = None
    DesiredState: Optional[InferenceExperimentStopDesiredStateType] = None
    Reason: Optional[str] = None

class UpdateInferenceExperimentRequestRequestTypeDef(BaseModel):
    Name: str
    Schedule: Optional[InferenceExperimentScheduleTypeDef] = None
    Description: Optional[str] = None
    ModelVariants: Optional[Sequence[ModelVariantConfigTypeDef]] = None
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfigTypeDef] = None
    ShadowModeConfig: Optional[ShadowModeConfigTypeDef] = None

class MonitoringInputExtraOutputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputExtraOutputTypeDef] = None

class DataQualityJobInputOutputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class ModelBiasJobInputOutputTypeDef(BaseModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class ModelExplainabilityJobInputOutputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class ModelQualityJobInputOutputTypeDef(BaseModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class MonitoringInputOutputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class DataQualityJobInputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class ModelBiasJobInputTypeDef(BaseModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class ModelExplainabilityJobInputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class ModelQualityJobInputTypeDef(BaseModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class MonitoringInputTypeDef(BaseModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class CreateOptimizationJobRequestRequestTypeDef(BaseModel):
    OptimizationJobName: str
    RoleArn: str
    ModelSource: OptimizationJobModelSourceTypeDef
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationConfigs: Sequence[OptimizationConfigUnionTypeDef]
    OutputConfig: OptimizationJobOutputConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    OptimizationEnvironment: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VpcConfig: Optional[OptimizationVpcConfigTypeDef] = None

class DescribeOptimizationJobResponseTypeDef(BaseModel):
    OptimizationJobArn: str
    OptimizationJobStatus: OptimizationJobStatusType
    OptimizationStartTime: datetime
    OptimizationEndTime: datetime
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    OptimizationJobName: str
    ModelSource: OptimizationJobModelSourceTypeDef
    OptimizationEnvironment: Dict[str, str]
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationConfigs: List[OptimizationConfigOutputTypeDef]
    OutputConfig: OptimizationJobOutputConfigTypeDef
    OptimizationOutput: OptimizationOutputTypeDef
    RoleArn: str
    StoppingCondition: StoppingConditionTypeDef
    VpcConfig: OptimizationVpcConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProcessingJobResponseTypeDef(BaseModel):
    ProcessingInputs: List[ProcessingInputTypeDef]
    ProcessingOutputConfig: ProcessingOutputConfigOutputTypeDef
    ProcessingJobName: str
    ProcessingResources: ProcessingResourcesTypeDef
    StoppingCondition: ProcessingStoppingConditionTypeDef
    AppSpecification: AppSpecificationOutputTypeDef
    Environment: Dict[str, str]
    NetworkConfig: NetworkConfigOutputTypeDef
    RoleArn: str
    ExperimentConfig: ExperimentConfigTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessingJobTypeDef(BaseModel):
    ProcessingInputs: Optional[List[ProcessingInputTypeDef]] = None
    ProcessingOutputConfig: Optional[ProcessingOutputConfigOutputTypeDef] = None
    ProcessingJobName: Optional[str] = None
    ProcessingResources: Optional[ProcessingResourcesTypeDef] = None
    StoppingCondition: Optional[ProcessingStoppingConditionTypeDef] = None
    AppSpecification: Optional[AppSpecificationOutputTypeDef] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigOutputTypeDef] = None
    RoleArn: Optional[str] = None
    ExperimentConfig: Optional[ExperimentConfigTypeDef] = None
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
    Tags: Optional[List[TagTypeDef]] = None

class CreateProcessingJobRequestRequestTypeDef(BaseModel):
    ProcessingJobName: str
    ProcessingResources: ProcessingResourcesTypeDef
    AppSpecification: AppSpecificationTypeDef
    RoleArn: str
    ProcessingInputs: Optional[Sequence[ProcessingInputTypeDef]] = None
    ProcessingOutputConfig: Optional[ProcessingOutputConfigTypeDef] = None
    StoppingCondition: Optional[ProcessingStoppingConditionTypeDef] = None
    Environment: Optional[Mapping[str, str]] = None
    NetworkConfig: Optional[NetworkConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ExperimentConfig: Optional[ExperimentConfigTypeDef] = None

class DescribeFlowDefinitionResponseTypeDef(BaseModel):
    FlowDefinitionArn: str
    FlowDefinitionName: str
    FlowDefinitionStatus: FlowDefinitionStatusType
    CreationTime: datetime
    HumanLoopRequestSource: HumanLoopRequestSourceTypeDef
    HumanLoopActivationConfig: HumanLoopActivationConfigTypeDef
    HumanLoopConfig: HumanLoopConfigOutputTypeDef
    OutputConfig: FlowDefinitionOutputConfigTypeDef
    RoleArn: str
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowDefinitionRequestRequestTypeDef(BaseModel):
    FlowDefinitionName: str
    OutputConfig: FlowDefinitionOutputConfigTypeDef
    RoleArn: str
    HumanLoopRequestSource: Optional[HumanLoopRequestSourceTypeDef] = None
    HumanLoopActivationConfig: Optional[HumanLoopActivationConfigTypeDef] = None
    HumanLoopConfig: Optional[HumanLoopConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeLabelingJobResponseTypeDef(BaseModel):
    LabelingJobStatus: LabelingJobStatusType
    LabelCounters: LabelCountersTypeDef
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    JobReferenceCode: str
    LabelingJobName: str
    LabelingJobArn: str
    LabelAttributeName: str
    InputConfig: LabelingJobInputConfigOutputTypeDef
    OutputConfig: LabelingJobOutputConfigTypeDef
    RoleArn: str
    LabelCategoryConfigS3Uri: str
    StoppingConditions: LabelingJobStoppingConditionsTypeDef
    LabelingJobAlgorithmsConfig: LabelingJobAlgorithmsConfigOutputTypeDef
    HumanTaskConfig: HumanTaskConfigOutputTypeDef
    Tags: List[TagTypeDef]
    LabelingJobOutput: LabelingJobOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelingJobRequestRequestTypeDef(BaseModel):
    LabelingJobName: str
    LabelAttributeName: str
    InputConfig: LabelingJobInputConfigTypeDef
    OutputConfig: LabelingJobOutputConfigTypeDef
    RoleArn: str
    HumanTaskConfig: HumanTaskConfigTypeDef
    LabelCategoryConfigS3Uri: Optional[str] = None
    StoppingConditions: Optional[LabelingJobStoppingConditionsTypeDef] = None
    LabelingJobAlgorithmsConfig: Optional[LabelingJobAlgorithmsConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeTrainingJobResponseTypeDef(BaseModel):
    TrainingJobName: str
    TrainingJobArn: str
    TuningJobArn: str
    LabelingJobArn: str
    AutoMLJobArn: str
    ModelArtifacts: ModelArtifactsTypeDef
    TrainingJobStatus: TrainingJobStatusType
    SecondaryStatus: SecondaryStatusType
    FailureReason: str
    HyperParameters: Dict[str, str]
    AlgorithmSpecification: AlgorithmSpecificationOutputTypeDef
    RoleArn: str
    InputDataConfig: List[ChannelOutputTypeDef]
    OutputDataConfig: OutputDataConfigTypeDef
    ResourceConfig: ResourceConfigOutputTypeDef
    WarmPoolStatus: WarmPoolStatusTypeDef
    VpcConfig: VpcConfigOutputTypeDef
    StoppingCondition: StoppingConditionTypeDef
    CreationTime: datetime
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    LastModifiedTime: datetime
    SecondaryStatusTransitions: List[SecondaryStatusTransitionTypeDef]
    FinalMetricDataList: List[MetricDataTypeDef]
    EnableNetworkIsolation: bool
    EnableInterContainerTrafficEncryption: bool
    EnableManagedSpotTraining: bool
    CheckpointConfig: CheckpointConfigTypeDef
    TrainingTimeInSeconds: int
    BillableTimeInSeconds: int
    DebugHookConfig: DebugHookConfigOutputTypeDef
    ExperimentConfig: ExperimentConfigTypeDef
    DebugRuleConfigurations: List[DebugRuleConfigurationOutputTypeDef]
    TensorBoardOutputConfig: TensorBoardOutputConfigTypeDef
    DebugRuleEvaluationStatuses: List[DebugRuleEvaluationStatusTypeDef]
    ProfilerConfig: ProfilerConfigOutputTypeDef
    ProfilerRuleConfigurations: List[ProfilerRuleConfigurationOutputTypeDef]
    ProfilerRuleEvaluationStatuses: List[ProfilerRuleEvaluationStatusTypeDef]
    ProfilingStatus: ProfilingStatusType
    Environment: Dict[str, str]
    RetryStrategy: RetryStrategyTypeDef
    RemoteDebugConfig: RemoteDebugConfigTypeDef
    InfraCheckConfig: InfraCheckConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TrainingJobTypeDef(BaseModel):
    TrainingJobName: Optional[str] = None
    TrainingJobArn: Optional[str] = None
    TuningJobArn: Optional[str] = None
    LabelingJobArn: Optional[str] = None
    AutoMLJobArn: Optional[str] = None
    ModelArtifacts: Optional[ModelArtifactsTypeDef] = None
    TrainingJobStatus: Optional[TrainingJobStatusType] = None
    SecondaryStatus: Optional[SecondaryStatusType] = None
    FailureReason: Optional[str] = None
    HyperParameters: Optional[Dict[str, str]] = None
    AlgorithmSpecification: Optional[AlgorithmSpecificationOutputTypeDef] = None
    RoleArn: Optional[str] = None
    InputDataConfig: Optional[List[ChannelOutputTypeDef]] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    ResourceConfig: Optional[ResourceConfigOutputTypeDef] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    StoppingCondition: Optional[StoppingConditionTypeDef] = None
    CreationTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    SecondaryStatusTransitions: Optional[List[SecondaryStatusTransitionTypeDef]] = None
    FinalMetricDataList: Optional[List[MetricDataTypeDef]] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfigTypeDef] = None
    TrainingTimeInSeconds: Optional[int] = None
    BillableTimeInSeconds: Optional[int] = None
    DebugHookConfig: Optional[DebugHookConfigOutputTypeDef] = None
    ExperimentConfig: Optional[ExperimentConfigTypeDef] = None
    DebugRuleConfigurations: Optional[List[DebugRuleConfigurationOutputTypeDef]] = None
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfigTypeDef] = None
    DebugRuleEvaluationStatuses: Optional[List[DebugRuleEvaluationStatusTypeDef]] = None
    ProfilerConfig: Optional[ProfilerConfigOutputTypeDef] = None
    Environment: Optional[Dict[str, str]] = None
    RetryStrategy: Optional[RetryStrategyTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateTransformJobRequestRequestTypeDef(BaseModel):
    TransformJobName: str
    ModelName: str
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    ModelClientConfig: Optional[ModelClientConfigTypeDef] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Mapping[str, str]] = None
    DataCaptureConfig: Optional[BatchDataCaptureConfigTypeDef] = None
    DataProcessing: Optional[DataProcessingTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ExperimentConfig: Optional[ExperimentConfigTypeDef] = None

class DescribeTransformJobResponseTypeDef(BaseModel):
    TransformJobName: str
    TransformJobArn: str
    TransformJobStatus: TransformJobStatusType
    FailureReason: str
    ModelName: str
    MaxConcurrentTransforms: int
    ModelClientConfig: ModelClientConfigTypeDef
    MaxPayloadInMB: int
    BatchStrategy: BatchStrategyType
    Environment: Dict[str, str]
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    DataCaptureConfig: BatchDataCaptureConfigTypeDef
    TransformResources: TransformResourcesTypeDef
    CreationTime: datetime
    TransformStartTime: datetime
    TransformEndTime: datetime
    LabelingJobArn: str
    AutoMLJobArn: str
    DataProcessing: DataProcessingTypeDef
    ExperimentConfig: ExperimentConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransformJobDefinitionExtraOutputTypeDef(BaseModel):
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None

class TransformJobDefinitionOutputTypeDef(BaseModel):
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None

class TransformJobDefinitionTypeDef(BaseModel):
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Mapping[str, str]] = None

class TransformJobTypeDef(BaseModel):
    TransformJobName: Optional[str] = None
    TransformJobArn: Optional[str] = None
    TransformJobStatus: Optional[TransformJobStatusType] = None
    FailureReason: Optional[str] = None
    ModelName: Optional[str] = None
    MaxConcurrentTransforms: Optional[int] = None
    ModelClientConfig: Optional[ModelClientConfigTypeDef] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None
    TransformInput: Optional[TransformInputTypeDef] = None
    TransformOutput: Optional[TransformOutputTypeDef] = None
    DataCaptureConfig: Optional[BatchDataCaptureConfigTypeDef] = None
    TransformResources: Optional[TransformResourcesTypeDef] = None
    CreationTime: Optional[datetime] = None
    TransformStartTime: Optional[datetime] = None
    TransformEndTime: Optional[datetime] = None
    LabelingJobArn: Optional[str] = None
    AutoMLJobArn: Optional[str] = None
    DataProcessing: Optional[DataProcessingTypeDef] = None
    ExperimentConfig: Optional[ExperimentConfigTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeAutoMLJobV2ResponseTypeDef(BaseModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    AutoMLJobInputDataConfig: List[AutoMLJobChannelTypeDef]
    OutputDataConfig: AutoMLOutputDataConfigTypeDef
    RoleArn: str
    AutoMLJobObjective: AutoMLJobObjectiveTypeDef
    AutoMLProblemTypeConfig: AutoMLProblemTypeConfigOutputTypeDef
    AutoMLProblemTypeConfigName: AutoMLProblemTypeConfigNameType
    CreationTime: datetime
    EndTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    PartialFailureReasons: List[AutoMLPartialFailureReasonTypeDef]
    BestCandidate: AutoMLCandidateTypeDef
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    AutoMLJobArtifacts: AutoMLJobArtifactsTypeDef
    ResolvedAttributes: AutoMLResolvedAttributesTypeDef
    ModelDeployConfig: ModelDeployConfigTypeDef
    ModelDeployResult: ModelDeployResultTypeDef
    DataSplitConfig: AutoMLDataSplitConfigTypeDef
    SecurityConfig: AutoMLSecurityConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoMLJobV2RequestRequestTypeDef(BaseModel):
    AutoMLJobName: str
    AutoMLJobInputDataConfig: Sequence[AutoMLJobChannelTypeDef]
    OutputDataConfig: AutoMLOutputDataConfigTypeDef
    AutoMLProblemTypeConfig: AutoMLProblemTypeConfigTypeDef
    RoleArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    SecurityConfig: Optional[AutoMLSecurityConfigTypeDef] = None
    AutoMLJobObjective: Optional[AutoMLJobObjectiveTypeDef] = None
    ModelDeployConfig: Optional[ModelDeployConfigTypeDef] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfigTypeDef] = None

class ListPipelineExecutionStepsResponseTypeDef(BaseModel):
    PipelineExecutionSteps: List[PipelineExecutionStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEndpointInputRequestTypeDef(BaseModel):
    EndpointName: str
    EndpointConfigName: str
    DeploymentConfig: Optional[DeploymentConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateEndpointInputRequestTypeDef(BaseModel):
    EndpointName: str
    EndpointConfigName: str
    RetainAllVariantProperties: Optional[bool] = None
    ExcludeRetainedVariantProperties: Optional[Sequence[VariantPropertyTypeDef]] = None
    DeploymentConfig: Optional[DeploymentConfigTypeDef] = None
    RetainDeploymentConfig: Optional[bool] = None

class DescribeInferenceRecommendationsJobResponseTypeDef(BaseModel):
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
    InputConfig: RecommendationJobInputConfigOutputTypeDef
    StoppingConditions: RecommendationJobStoppingConditionsOutputTypeDef
    InferenceRecommendations: List[InferenceRecommendationTypeDef]
    EndpointPerformances: List[EndpointPerformanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceRecommendationsJobRequestRequestTypeDef(BaseModel):
    JobName: str
    JobType: RecommendationJobTypeType
    RoleArn: str
    InputConfig: RecommendationJobInputConfigTypeDef
    JobDescription: Optional[str] = None
    StoppingConditions: Optional[RecommendationJobStoppingConditionsTypeDef] = None
    OutputConfig: Optional[RecommendationJobOutputConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeEndpointConfigOutputTypeDef(BaseModel):
    EndpointConfigName: str
    EndpointConfigArn: str
    ProductionVariants: List[ProductionVariantTypeDef]
    DataCaptureConfig: DataCaptureConfigOutputTypeDef
    KmsKeyId: str
    CreationTime: datetime
    AsyncInferenceConfig: AsyncInferenceConfigOutputTypeDef
    ExplainerConfig: ExplainerConfigOutputTypeDef
    ShadowProductionVariants: List[ProductionVariantTypeDef]
    ExecutionRoleArn: str
    VpcConfig: VpcConfigOutputTypeDef
    EnableNetworkIsolation: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointOutputTypeDef(BaseModel):
    EndpointName: str
    EndpointArn: str
    EndpointConfigName: str
    ProductionVariants: List[ProductionVariantSummaryTypeDef]
    DataCaptureConfig: DataCaptureConfigSummaryTypeDef
    EndpointStatus: EndpointStatusType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LastDeploymentConfig: DeploymentConfigOutputTypeDef
    AsyncInferenceConfig: AsyncInferenceConfigOutputTypeDef
    PendingDeploymentSummary: PendingDeploymentSummaryTypeDef
    ExplainerConfig: ExplainerConfigOutputTypeDef
    ShadowProductionVariants: List[ProductionVariantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointConfigInputRequestTypeDef(BaseModel):
    EndpointConfigName: str
    ProductionVariants: Sequence[ProductionVariantTypeDef]
    DataCaptureConfig: Optional[DataCaptureConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    AsyncInferenceConfig: Optional[AsyncInferenceConfigTypeDef] = None
    ExplainerConfig: Optional[ExplainerConfigTypeDef] = None
    ShadowProductionVariants: Optional[Sequence[ProductionVariantTypeDef]] = None
    ExecutionRoleArn: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    EnableNetworkIsolation: Optional[bool] = None

class DescribeHyperParameterTuningJobResponseTypeDef(BaseModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobArn: str
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfigOutputTypeDef
    TrainingJobDefinition: HyperParameterTrainingJobDefinitionOutputTypeDef
    TrainingJobDefinitions: List[HyperParameterTrainingJobDefinitionOutputTypeDef]
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatusType
    CreationTime: datetime
    HyperParameterTuningEndTime: datetime
    LastModifiedTime: datetime
    TrainingJobStatusCounters: TrainingJobStatusCountersTypeDef
    ObjectiveStatusCounters: ObjectiveStatusCountersTypeDef
    BestTrainingJob: HyperParameterTrainingJobSummaryTypeDef
    OverallBestTrainingJob: HyperParameterTrainingJobSummaryTypeDef
    WarmStartConfig: HyperParameterTuningJobWarmStartConfigOutputTypeDef
    Autotune: AutotuneTypeDef
    FailureReason: str
    TuningJobCompletionDetails: HyperParameterTuningJobCompletionDetailsTypeDef
    ConsumedResources: HyperParameterTuningJobConsumedResourcesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HyperParameterTuningJobSearchEntityTypeDef(BaseModel):
    HyperParameterTuningJobName: Optional[str] = None
    HyperParameterTuningJobArn: Optional[str] = None
    HyperParameterTuningJobConfig: Optional[HyperParameterTuningJobConfigOutputTypeDef] = None
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinitionOutputTypeDef] = None
    TrainingJobDefinitions: Optional[       List[HyperParameterTrainingJobDefinitionOutputTypeDef]     ] = None
    HyperParameterTuningJobStatus: Optional[HyperParameterTuningJobStatusType] = None
    CreationTime: Optional[datetime] = None
    HyperParameterTuningEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    TrainingJobStatusCounters: Optional[TrainingJobStatusCountersTypeDef] = None
    ObjectiveStatusCounters: Optional[ObjectiveStatusCountersTypeDef] = None
    BestTrainingJob: Optional[HyperParameterTrainingJobSummaryTypeDef] = None
    OverallBestTrainingJob: Optional[HyperParameterTrainingJobSummaryTypeDef] = None
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfigOutputTypeDef] = None
    FailureReason: Optional[str] = None
    TuningJobCompletionDetails: Optional[HyperParameterTuningJobCompletionDetailsTypeDef] = None
    ConsumedResources: Optional[HyperParameterTuningJobConsumedResourcesTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateTrainingJobRequestRequestTypeDef(BaseModel):
    TrainingJobName: str
    AlgorithmSpecification: AlgorithmSpecificationTypeDef
    RoleArn: str
    OutputDataConfig: OutputDataConfigTypeDef
    ResourceConfig: ResourceConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    HyperParameters: Optional[Mapping[str, str]] = None
    InputDataConfig: Optional[Sequence[ChannelUnionTypeDef]] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EnableNetworkIsolation: Optional[bool] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableManagedSpotTraining: Optional[bool] = None
    CheckpointConfig: Optional[CheckpointConfigTypeDef] = None
    DebugHookConfig: Optional[DebugHookConfigTypeDef] = None
    DebugRuleConfigurations: Optional[Sequence[DebugRuleConfigurationUnionTypeDef]] = None
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfigTypeDef] = None
    ExperimentConfig: Optional[ExperimentConfigTypeDef] = None
    ProfilerConfig: Optional[ProfilerConfigTypeDef] = None
    ProfilerRuleConfigurations: Optional[Sequence[ProfilerRuleConfigurationUnionTypeDef]] = None
    Environment: Optional[Mapping[str, str]] = None
    RetryStrategy: Optional[RetryStrategyTypeDef] = None
    RemoteDebugConfig: Optional[RemoteDebugConfigTypeDef] = None
    InfraCheckConfig: Optional[InfraCheckConfigTypeDef] = None
    SessionChainingConfig: Optional[SessionChainingConfigTypeDef] = None

class ListSpacesResponseTypeDef(BaseModel):
    Spaces: List[SpaceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListInferenceRecommendationsJobStepsResponseTypeDef(BaseModel):
    Steps: List[InferenceRecommendationsJobStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeWorkteamResponseTypeDef(BaseModel):
    Workteam: WorkteamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkteamsResponseTypeDef(BaseModel):
    Workteams: List[WorkteamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateWorkteamResponseTypeDef(BaseModel):
    Workteam: WorkteamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLabelingJobsResponseTypeDef(BaseModel):
    LabelingJobSummaryList: List[LabelingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DynamicScalingConfigurationTypeDef(BaseModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None
    ScalingPolicies: Optional[List[ScalingPolicyTypeDef]] = None

class DescribeModelOutputTypeDef(BaseModel):
    ModelName: str
    PrimaryContainer: ContainerDefinitionOutputTypeDef
    Containers: List[ContainerDefinitionOutputTypeDef]
    InferenceExecutionConfig: InferenceExecutionConfigTypeDef
    ExecutionRoleArn: str
    VpcConfig: VpcConfigOutputTypeDef
    CreationTime: datetime
    ModelArn: str
    EnableNetworkIsolation: bool
    DeploymentRecommendation: DeploymentRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModelTypeDef(BaseModel):
    ModelName: Optional[str] = None
    PrimaryContainer: Optional[ContainerDefinitionOutputTypeDef] = None
    Containers: Optional[List[ContainerDefinitionOutputTypeDef]] = None
    InferenceExecutionConfig: Optional[InferenceExecutionConfigTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    CreationTime: Optional[datetime] = None
    ModelArn: Optional[str] = None
    EnableNetworkIsolation: Optional[bool] = None
    Tags: Optional[List[TagTypeDef]] = None
    DeploymentRecommendation: Optional[DeploymentRecommendationTypeDef] = None

class AdditionalInferenceSpecificationDefinitionExtraOutputTypeDef(BaseModel):
    Name: str
    Containers: List[ModelPackageContainerDefinitionExtraOutputTypeDef]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class InferenceSpecificationExtraOutputTypeDef(BaseModel):
    Containers: List[ModelPackageContainerDefinitionExtraOutputTypeDef]
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class AdditionalInferenceSpecificationDefinitionOutputTypeDef(BaseModel):
    Name: str
    Containers: List[ModelPackageContainerDefinitionOutputTypeDef]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class InferenceSpecificationOutputTypeDef(BaseModel):
    Containers: List[ModelPackageContainerDefinitionOutputTypeDef]
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class AdditionalInferenceSpecificationDefinitionTypeDef(BaseModel):
    Name: str
    Containers: Sequence[ModelPackageContainerDefinitionTypeDef]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[Sequence[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       Sequence[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[Sequence[str]] = None
    SupportedResponseMIMETypes: Optional[Sequence[str]] = None

class InferenceSpecificationTypeDef(BaseModel):
    Containers: Sequence[ModelPackageContainerDefinitionTypeDef]
    SupportedTransformInstanceTypes: Optional[Sequence[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       Sequence[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[Sequence[str]] = None
    SupportedResponseMIMETypes: Optional[Sequence[str]] = None

class SourceAlgorithmSpecificationExtraOutputTypeDef(BaseModel):
    SourceAlgorithms: List[SourceAlgorithmTypeDef]

class SourceAlgorithmSpecificationOutputTypeDef(BaseModel):
    SourceAlgorithms: List[SourceAlgorithmTypeDef]

class SourceAlgorithmSpecificationTypeDef(BaseModel):
    SourceAlgorithms: Sequence[SourceAlgorithmTypeDef]

class MonitoringJobDefinitionExtraOutputTypeDef(BaseModel):
    MonitoringInputs: List[MonitoringInputExtraOutputTypeDef]
    MonitoringOutputConfig: MonitoringOutputConfigExtraOutputTypeDef
    MonitoringResources: MonitoringResourcesTypeDef
    MonitoringAppSpecification: MonitoringAppSpecificationExtraOutputTypeDef
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigExtraOutputTypeDef] = None

class DescribeDataQualityJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    DataQualityBaselineConfig: DataQualityBaselineConfigTypeDef
    DataQualityAppSpecification: DataQualityAppSpecificationOutputTypeDef
    DataQualityJobInput: DataQualityJobInputOutputTypeDef
    DataQualityJobOutputConfig: MonitoringOutputConfigOutputTypeDef
    JobResources: MonitoringResourcesTypeDef
    NetworkConfig: MonitoringNetworkConfigOutputTypeDef
    RoleArn: str
    StoppingCondition: MonitoringStoppingConditionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelBiasJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelBiasBaselineConfig: ModelBiasBaselineConfigTypeDef
    ModelBiasAppSpecification: ModelBiasAppSpecificationOutputTypeDef
    ModelBiasJobInput: ModelBiasJobInputOutputTypeDef
    ModelBiasJobOutputConfig: MonitoringOutputConfigOutputTypeDef
    JobResources: MonitoringResourcesTypeDef
    NetworkConfig: MonitoringNetworkConfigOutputTypeDef
    RoleArn: str
    StoppingCondition: MonitoringStoppingConditionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelExplainabilityJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelExplainabilityBaselineConfig: ModelExplainabilityBaselineConfigTypeDef
    ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecificationOutputTypeDef
    ModelExplainabilityJobInput: ModelExplainabilityJobInputOutputTypeDef
    ModelExplainabilityJobOutputConfig: MonitoringOutputConfigOutputTypeDef
    JobResources: MonitoringResourcesTypeDef
    NetworkConfig: MonitoringNetworkConfigOutputTypeDef
    RoleArn: str
    StoppingCondition: MonitoringStoppingConditionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelQualityJobDefinitionResponseTypeDef(BaseModel):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelQualityBaselineConfig: ModelQualityBaselineConfigTypeDef
    ModelQualityAppSpecification: ModelQualityAppSpecificationOutputTypeDef
    ModelQualityJobInput: ModelQualityJobInputOutputTypeDef
    ModelQualityJobOutputConfig: MonitoringOutputConfigOutputTypeDef
    JobResources: MonitoringResourcesTypeDef
    NetworkConfig: MonitoringNetworkConfigOutputTypeDef
    RoleArn: str
    StoppingCondition: MonitoringStoppingConditionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MonitoringJobDefinitionOutputTypeDef(BaseModel):
    MonitoringInputs: List[MonitoringInputOutputTypeDef]
    MonitoringOutputConfig: MonitoringOutputConfigOutputTypeDef
    MonitoringResources: MonitoringResourcesTypeDef
    MonitoringAppSpecification: MonitoringAppSpecificationOutputTypeDef
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigOutputTypeDef] = None

class CreateDataQualityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str
    DataQualityAppSpecification: DataQualityAppSpecificationTypeDef
    DataQualityJobInput: DataQualityJobInputTypeDef
    DataQualityJobOutputConfig: MonitoringOutputConfigTypeDef
    JobResources: MonitoringResourcesTypeDef
    RoleArn: str
    DataQualityBaselineConfig: Optional[DataQualityBaselineConfigTypeDef] = None
    NetworkConfig: Optional[MonitoringNetworkConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelBiasJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str
    ModelBiasAppSpecification: ModelBiasAppSpecificationTypeDef
    ModelBiasJobInput: ModelBiasJobInputTypeDef
    ModelBiasJobOutputConfig: MonitoringOutputConfigTypeDef
    JobResources: MonitoringResourcesTypeDef
    RoleArn: str
    ModelBiasBaselineConfig: Optional[ModelBiasBaselineConfigTypeDef] = None
    NetworkConfig: Optional[MonitoringNetworkConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelExplainabilityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str
    ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecificationTypeDef
    ModelExplainabilityJobInput: ModelExplainabilityJobInputTypeDef
    ModelExplainabilityJobOutputConfig: MonitoringOutputConfigTypeDef
    JobResources: MonitoringResourcesTypeDef
    RoleArn: str
    ModelExplainabilityBaselineConfig: Optional[ModelExplainabilityBaselineConfigTypeDef] = None
    NetworkConfig: Optional[MonitoringNetworkConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelQualityJobDefinitionRequestRequestTypeDef(BaseModel):
    JobDefinitionName: str
    ModelQualityAppSpecification: ModelQualityAppSpecificationTypeDef
    ModelQualityJobInput: ModelQualityJobInputTypeDef
    ModelQualityJobOutputConfig: MonitoringOutputConfigTypeDef
    JobResources: MonitoringResourcesTypeDef
    RoleArn: str
    ModelQualityBaselineConfig: Optional[ModelQualityBaselineConfigTypeDef] = None
    NetworkConfig: Optional[MonitoringNetworkConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MonitoringJobDefinitionTypeDef(BaseModel):
    MonitoringInputs: Sequence[MonitoringInputTypeDef]
    MonitoringOutputConfig: MonitoringOutputConfigTypeDef
    MonitoringResources: MonitoringResourcesTypeDef
    MonitoringAppSpecification: MonitoringAppSpecificationTypeDef
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Environment: Optional[Mapping[str, str]] = None
    NetworkConfig: Optional[NetworkConfigTypeDef] = None

class ModelPackageValidationProfileExtraOutputTypeDef(BaseModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionExtraOutputTypeDef

class AlgorithmValidationProfileOutputTypeDef(BaseModel):
    ProfileName: str
    TrainingJobDefinition: TrainingJobDefinitionOutputTypeDef
    TransformJobDefinition: Optional[TransformJobDefinitionOutputTypeDef] = None

class ModelPackageValidationProfileOutputTypeDef(BaseModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionOutputTypeDef

class AlgorithmValidationProfileTypeDef(BaseModel):
    ProfileName: str
    TrainingJobDefinition: TrainingJobDefinitionTypeDef
    TransformJobDefinition: Optional[TransformJobDefinitionTypeDef] = None

class ModelPackageValidationProfileTypeDef(BaseModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionTypeDef

class TrialComponentSourceDetailTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    TrainingJob: Optional[TrainingJobTypeDef] = None
    ProcessingJob: Optional[ProcessingJobTypeDef] = None
    TransformJob: Optional[TransformJobTypeDef] = None

class CreateHyperParameterTuningJobRequestRequestTypeDef(BaseModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfigTypeDef
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinitionTypeDef] = None
    TrainingJobDefinitions: Optional[       Sequence[HyperParameterTrainingJobDefinitionUnionTypeDef]     ] = None
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Autotune: Optional[AutotuneTypeDef] = None

class GetScalingConfigurationRecommendationResponseTypeDef(BaseModel):
    InferenceRecommendationsJobName: str
    RecommendationId: str
    EndpointName: str
    TargetCpuUtilizationPerCore: int
    ScalingPolicyObjective: ScalingPolicyObjectiveTypeDef
    Metric: ScalingPolicyMetricTypeDef
    DynamicScalingConfiguration: DynamicScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelInputRequestTypeDef(BaseModel):
    ModelName: str
    PrimaryContainer: Optional[ContainerDefinitionTypeDef] = None
    Containers: Optional[Sequence[ContainerDefinitionUnionTypeDef]] = None
    InferenceExecutionConfig: Optional[InferenceExecutionConfigTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    EnableNetworkIsolation: Optional[bool] = None

class BatchDescribeModelPackageSummaryTypeDef(BaseModel):
    ModelPackageGroupName: str
    ModelPackageArn: str
    CreationTime: datetime
    InferenceSpecification: InferenceSpecificationOutputTypeDef
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageVersion: Optional[int] = None
    ModelPackageDescription: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None

class MonitoringScheduleConfigExtraOutputTypeDef(BaseModel):
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionExtraOutputTypeDef] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class MonitoringScheduleConfigOutputTypeDef(BaseModel):
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionOutputTypeDef] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class MonitoringScheduleConfigTypeDef(BaseModel):
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionTypeDef] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class ModelPackageValidationSpecificationExtraOutputTypeDef(BaseModel):
    ValidationRole: str
    ValidationProfiles: List[ModelPackageValidationProfileExtraOutputTypeDef]

class AlgorithmValidationSpecificationOutputTypeDef(BaseModel):
    ValidationRole: str
    ValidationProfiles: List[AlgorithmValidationProfileOutputTypeDef]

class ModelPackageValidationSpecificationOutputTypeDef(BaseModel):
    ValidationRole: str
    ValidationProfiles: List[ModelPackageValidationProfileOutputTypeDef]

class AlgorithmValidationSpecificationTypeDef(BaseModel):
    ValidationRole: str
    ValidationProfiles: Sequence[AlgorithmValidationProfileTypeDef]

class ModelPackageValidationSpecificationTypeDef(BaseModel):
    ValidationRole: str
    ValidationProfiles: Sequence[ModelPackageValidationProfileTypeDef]

class TrialComponentTypeDef(BaseModel):
    TrialComponentName: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    Source: Optional[TrialComponentSourceTypeDef] = None
    Status: Optional[TrialComponentStatusTypeDef] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    Parameters: Optional[Dict[str, TrialComponentParameterValueTypeDef]] = None
    InputArtifacts: Optional[Dict[str, TrialComponentArtifactTypeDef]] = None
    OutputArtifacts: Optional[Dict[str, TrialComponentArtifactTypeDef]] = None
    Metrics: Optional[List[TrialComponentMetricSummaryTypeDef]] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    SourceDetail: Optional[TrialComponentSourceDetailTypeDef] = None
    LineageGroupArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    Parents: Optional[List[ParentTypeDef]] = None
    RunName: Optional[str] = None

class BatchDescribeModelPackageOutputTypeDef(BaseModel):
    ModelPackageSummaries: Dict[str, BatchDescribeModelPackageSummaryTypeDef]
    BatchDescribeModelPackageErrorMap: Dict[str, BatchDescribeModelPackageErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelPackageInputRequestTypeDef(BaseModel):
    ModelPackageArn: str
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ApprovalDescription: Optional[str] = None
    CustomerMetadataProperties: Optional[Mapping[str, str]] = None
    CustomerMetadataPropertiesToRemove: Optional[Sequence[str]] = None
    AdditionalInferenceSpecificationsToAdd: Optional[       Sequence[AdditionalInferenceSpecificationDefinitionUnionTypeDef]     ] = None
    InferenceSpecification: Optional[InferenceSpecificationTypeDef] = None
    SourceUri: Optional[str] = None
    ModelCard: Optional[ModelPackageModelCardTypeDef] = None

class DescribeMonitoringScheduleResponseTypeDef(BaseModel):
    MonitoringScheduleArn: str
    MonitoringScheduleName: str
    MonitoringScheduleStatus: ScheduleStatusType
    MonitoringType: MonitoringTypeType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleConfig: MonitoringScheduleConfigOutputTypeDef
    EndpointName: str
    LastMonitoringExecutionSummary: MonitoringExecutionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModelDashboardMonitoringScheduleTypeDef(BaseModel):
    MonitoringScheduleArn: Optional[str] = None
    MonitoringScheduleName: Optional[str] = None
    MonitoringScheduleStatus: Optional[ScheduleStatusType] = None
    MonitoringType: Optional[MonitoringTypeType] = None
    FailureReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    MonitoringScheduleConfig: Optional[MonitoringScheduleConfigOutputTypeDef] = None
    EndpointName: Optional[str] = None
    MonitoringAlertSummaries: Optional[List[MonitoringAlertSummaryTypeDef]] = None
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummaryTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class MonitoringScheduleTypeDef(BaseModel):
    MonitoringScheduleArn: Optional[str] = None
    MonitoringScheduleName: Optional[str] = None
    MonitoringScheduleStatus: Optional[ScheduleStatusType] = None
    MonitoringType: Optional[MonitoringTypeType] = None
    FailureReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    MonitoringScheduleConfig: Optional[MonitoringScheduleConfigOutputTypeDef] = None
    EndpointName: Optional[str] = None
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummaryTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateMonitoringScheduleRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateMonitoringScheduleRequestRequestTypeDef(BaseModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef

class DescribeAlgorithmOutputTypeDef(BaseModel):
    AlgorithmName: str
    AlgorithmArn: str
    AlgorithmDescription: str
    CreationTime: datetime
    TrainingSpecification: TrainingSpecificationOutputTypeDef
    InferenceSpecification: InferenceSpecificationOutputTypeDef
    ValidationSpecification: AlgorithmValidationSpecificationOutputTypeDef
    AlgorithmStatus: AlgorithmStatusType
    AlgorithmStatusDetails: AlgorithmStatusDetailsTypeDef
    ProductId: str
    CertifyForMarketplace: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelPackageOutputTypeDef(BaseModel):
    ModelPackageName: str
    ModelPackageGroupName: str
    ModelPackageVersion: int
    ModelPackageArn: str
    ModelPackageDescription: str
    CreationTime: datetime
    InferenceSpecification: InferenceSpecificationOutputTypeDef
    SourceAlgorithmSpecification: SourceAlgorithmSpecificationOutputTypeDef
    ValidationSpecification: ModelPackageValidationSpecificationOutputTypeDef
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageStatusDetails: ModelPackageStatusDetailsTypeDef
    CertifyForMarketplace: bool
    ModelApprovalStatus: ModelApprovalStatusType
    CreatedBy: UserContextTypeDef
    MetadataProperties: MetadataPropertiesTypeDef
    ModelMetrics: ModelMetricsTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ApprovalDescription: str
    Domain: str
    Task: str
    SamplePayloadUrl: str
    CustomerMetadataProperties: Dict[str, str]
    DriftCheckBaselines: DriftCheckBaselinesTypeDef
    AdditionalInferenceSpecifications: List[       AdditionalInferenceSpecificationDefinitionOutputTypeDef     ]
    SkipModelValidation: SkipModelValidationType
    SourceUri: str
    SecurityConfig: ModelPackageSecurityConfigTypeDef
    ModelCard: ModelPackageModelCardTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModelPackageTypeDef(BaseModel):
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageVersion: Optional[int] = None
    ModelPackageArn: Optional[str] = None
    ModelPackageDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    InferenceSpecification: Optional[InferenceSpecificationOutputTypeDef] = None
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecificationOutputTypeDef] = None
    ValidationSpecification: Optional[ModelPackageValidationSpecificationOutputTypeDef] = None
    ModelPackageStatus: Optional[ModelPackageStatusType] = None
    ModelPackageStatusDetails: Optional[ModelPackageStatusDetailsTypeDef] = None
    CertifyForMarketplace: Optional[bool] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    ModelMetrics: Optional[ModelMetricsTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedBy: Optional[UserContextTypeDef] = None
    ApprovalDescription: Optional[str] = None
    Domain: Optional[str] = None
    Task: Optional[str] = None
    SamplePayloadUrl: Optional[str] = None
    AdditionalInferenceSpecifications: Optional[       List[AdditionalInferenceSpecificationDefinitionOutputTypeDef]     ] = None
    SourceUri: Optional[str] = None
    SecurityConfig: Optional[ModelPackageSecurityConfigTypeDef] = None
    ModelCard: Optional[ModelPackageModelCardTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    CustomerMetadataProperties: Optional[Dict[str, str]] = None
    DriftCheckBaselines: Optional[DriftCheckBaselinesTypeDef] = None
    SkipModelValidation: Optional[SkipModelValidationType] = None

class CreateAlgorithmInputRequestTypeDef(BaseModel):
    AlgorithmName: str
    TrainingSpecification: TrainingSpecificationTypeDef
    AlgorithmDescription: Optional[str] = None
    InferenceSpecification: Optional[InferenceSpecificationTypeDef] = None
    ValidationSpecification: Optional[AlgorithmValidationSpecificationTypeDef] = None
    CertifyForMarketplace: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelPackageInputRequestTypeDef(BaseModel):
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageDescription: Optional[str] = None
    InferenceSpecification: Optional[InferenceSpecificationTypeDef] = None
    ValidationSpecification: Optional[ModelPackageValidationSpecificationTypeDef] = None
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecificationTypeDef] = None
    CertifyForMarketplace: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    ModelMetrics: Optional[ModelMetricsTypeDef] = None
    ClientToken: Optional[str] = None
    Domain: Optional[str] = None
    Task: Optional[str] = None
    SamplePayloadUrl: Optional[str] = None
    CustomerMetadataProperties: Optional[Mapping[str, str]] = None
    DriftCheckBaselines: Optional[DriftCheckBaselinesTypeDef] = None
    AdditionalInferenceSpecifications: Optional[       Sequence[AdditionalInferenceSpecificationDefinitionUnionTypeDef]     ] = None
    SkipModelValidation: Optional[SkipModelValidationType] = None
    SourceUri: Optional[str] = None
    SecurityConfig: Optional[ModelPackageSecurityConfigTypeDef] = None
    ModelCard: Optional[ModelPackageModelCardTypeDef] = None

class ModelDashboardModelTypeDef(BaseModel):
    Model: Optional[ModelTypeDef] = None
    Endpoints: Optional[List[ModelDashboardEndpointTypeDef]] = None
    LastBatchTransformJob: Optional[TransformJobTypeDef] = None
    MonitoringSchedules: Optional[List[ModelDashboardMonitoringScheduleTypeDef]] = None
    ModelCard: Optional[ModelDashboardModelCardTypeDef] = None

class EndpointTypeDef(BaseModel):
    EndpointName: str
    EndpointArn: str
    EndpointConfigName: str
    EndpointStatus: EndpointStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    ProductionVariants: Optional[List[ProductionVariantSummaryTypeDef]] = None
    DataCaptureConfig: Optional[DataCaptureConfigSummaryTypeDef] = None
    FailureReason: Optional[str] = None
    MonitoringSchedules: Optional[List[MonitoringScheduleTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    ShadowProductionVariants: Optional[List[ProductionVariantSummaryTypeDef]] = None

class SearchRecordTypeDef(BaseModel):
    TrainingJob: Optional[TrainingJobTypeDef] = None
    Experiment: Optional[ExperimentTypeDef] = None
    Trial: Optional[TrialTypeDef] = None
    TrialComponent: Optional[TrialComponentTypeDef] = None
    Endpoint: Optional[EndpointTypeDef] = None
    ModelPackage: Optional[ModelPackageTypeDef] = None
    ModelPackageGroup: Optional[ModelPackageGroupTypeDef] = None
    Pipeline: Optional[PipelineTypeDef] = None
    PipelineExecution: Optional[PipelineExecutionTypeDef] = None
    FeatureGroup: Optional[FeatureGroupTypeDef] = None
    FeatureMetadata: Optional[FeatureMetadataTypeDef] = None
    Project: Optional[ProjectTypeDef] = None
    HyperParameterTuningJob: Optional[HyperParameterTuningJobSearchEntityTypeDef] = None
    ModelCard: Optional[ModelCardTypeDef] = None
    Model: Optional[ModelDashboardModelTypeDef] = None

class SearchResponseTypeDef(BaseModel):
    Results: List[SearchRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

