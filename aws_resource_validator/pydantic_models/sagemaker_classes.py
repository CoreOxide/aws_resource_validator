from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ActionSourceTypeDef(BaseValidatorModel):
    SourceUri: str
    SourceType: Optional[str] = None
    SourceId: Optional[str] = None

class AddAssociationRequestRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    AssociationType: Optional[AssociationEdgeTypeType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class AdditionalS3DataSourceTypeDef(BaseValidatorModel):
    S3DataType: AdditionalS3DataSourceDataTypeType
    S3Uri: str
    CompressionType: Optional[CompressionTypeType] = None

class AgentVersionTypeDef(BaseValidatorModel):
    Version: str
    AgentCount: int

class AlarmTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None

class MetricDefinitionTypeDef(BaseValidatorModel):
    Name: str
    Regex: str

class AlgorithmStatusItemTypeDef(BaseValidatorModel):
    Name: str
    Status: DetailedAlgorithmStatusType
    FailureReason: Optional[str] = None

class AlgorithmSummaryTypeDef(BaseValidatorModel):
    AlgorithmName: str
    AlgorithmArn: str
    CreationTime: datetime
    AlgorithmStatus: AlgorithmStatusType
    AlgorithmDescription: Optional[str] = None

class AmazonQSettingsTypeDef(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None
    QProfileArn: Optional[str] = None

class AnnotationConsolidationConfigTypeDef(BaseValidatorModel):
    AnnotationConsolidationLambdaArn: str

class ResourceSpecTypeDef(BaseValidatorModel):
    SageMakerImageArn: Optional[str] = None
    SageMakerImageVersionArn: Optional[str] = None
    SageMakerImageVersionAlias: Optional[str] = None
    InstanceType: Optional[AppInstanceTypeType] = None
    LifecycleConfigArn: Optional[str] = None

class AppSpecificationExtraOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None

class AppSpecificationOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None

class AppSpecificationTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None

class ArtifactSourceTypeTypeDef(BaseValidatorModel):
    SourceIdType: ArtifactSourceIdTypeType
    Value: str

class AssociateTrialComponentRequestRequestTypeDef(BaseValidatorModel):
    TrialComponentName: str
    TrialName: str

class AsyncInferenceClientConfigTypeDef(BaseValidatorModel):
    MaxConcurrentInvocationsPerInstance: Optional[int] = None

class AsyncInferenceNotificationConfigOutputTypeDef(BaseValidatorModel):
    SuccessTopic: Optional[str] = None
    ErrorTopic: Optional[str] = None
    IncludeInferenceResponseIn: Optional[List[AsyncNotificationTopicTypesType]] = None

class AsyncInferenceNotificationConfigTypeDef(BaseValidatorModel):
    SuccessTopic: Optional[str] = None
    ErrorTopic: Optional[str] = None
    IncludeInferenceResponseIn: Optional[Sequence[AsyncNotificationTopicTypesType]] = None

class AthenaDatasetDefinitionTypeDef(BaseValidatorModel):
    Catalog: str
    Database: str
    QueryString: str
    OutputS3Uri: str
    OutputFormat: AthenaResultFormatType
    WorkGroup: Optional[str] = None
    KmsKeyId: Optional[str] = None
    OutputCompression: Optional[AthenaResultCompressionTypeType] = None

class AutoMLAlgorithmConfigOutputTypeDef(BaseValidatorModel):
    AutoMLAlgorithms: List[AutoMLAlgorithmType]

class AutoMLAlgorithmConfigTypeDef(BaseValidatorModel):
    AutoMLAlgorithms: Sequence[AutoMLAlgorithmType]

class AutoMLCandidateStepTypeDef(BaseValidatorModel):
    CandidateStepType: CandidateStepTypeType
    CandidateStepArn: str
    CandidateStepName: str

class AutoMLContainerDefinitionTypeDef(BaseValidatorModel):
    Image: str
    ModelDataUrl: str
    Environment: Optional[Dict[str, str]] = None

class FinalAutoMLJobObjectiveMetricTypeDef(BaseValidatorModel):
    MetricName: AutoMLMetricEnumType
    Value: float
    Type: Optional[AutoMLJobObjectiveTypeType] = None
    StandardMetricName: Optional[AutoMLMetricEnumType] = None

class AutoMLS3DataSourceTypeDef(BaseValidatorModel):
    S3DataType: AutoMLS3DataTypeType
    S3Uri: str

class AutoMLDataSplitConfigTypeDef(BaseValidatorModel):
    ValidationFraction: Optional[float] = None

class AutoMLJobArtifactsTypeDef(BaseValidatorModel):
    CandidateDefinitionNotebookLocation: Optional[str] = None
    DataExplorationNotebookLocation: Optional[str] = None

class AutoMLJobCompletionCriteriaTypeDef(BaseValidatorModel):
    MaxCandidates: Optional[int] = None
    MaxRuntimePerTrainingJobInSeconds: Optional[int] = None
    MaxAutoMLJobRuntimeInSeconds: Optional[int] = None

class AutoMLJobObjectiveTypeDef(BaseValidatorModel):
    MetricName: AutoMLMetricEnumType

class AutoMLJobStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class AutoMLPartialFailureReasonTypeDef(BaseValidatorModel):
    PartialFailureMessage: Optional[str] = None

class AutoMLOutputDataConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None

class TabularResolvedAttributesTypeDef(BaseValidatorModel):
    ProblemType: Optional[ProblemTypeType] = None

class TextGenerationResolvedAttributesTypeDef(BaseValidatorModel):
    BaseValidatorModelName: Optional[str] = None

class VpcConfigOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class VpcConfigTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class AutoParameterTypeDef(BaseValidatorModel):
    Name: str
    ValueHint: str

class AutotuneTypeDef(BaseValidatorModel):
    Mode: Literal["Enabled"]

class BatchDataCaptureConfigTypeDef(BaseValidatorModel):
    DestinationS3Uri: str
    KmsKeyId: Optional[str] = None
    GenerateInferenceId: Optional[bool] = None

class BatchDescribeModelPackageErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorResponse: str

class BatchDescribeModelPackageInputRequestTypeDef(BaseValidatorModel):
    ModelPackageArnList: Sequence[str]

class BestObjectiveNotImprovingTypeDef(BaseValidatorModel):
    MaxNumberOfTrainingJobsNotImproving: Optional[int] = None

class MetricsSourceTypeDef(BaseValidatorModel):
    ContentType: str
    S3Uri: str
    ContentDigest: Optional[str] = None

class CacheHitResultTypeDef(BaseValidatorModel):
    SourcePipelineExecutionArn: Optional[str] = None

class OutputParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class CandidateArtifactLocationsTypeDef(BaseValidatorModel):
    Explainability: str
    ModelInsights: Optional[str] = None
    BacktestResults: Optional[str] = None

class MetricDatumTypeDef(BaseValidatorModel):
    MetricName: Optional[AutoMLMetricEnumType] = None
    Value: Optional[float] = None
    Set: Optional[MetricSetSourceType] = None
    StandardMetricName: Optional[AutoMLMetricExtendedEnumType] = None

class DirectDeploySettingsTypeDef(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None

class GenerativeAiSettingsTypeDef(BaseValidatorModel):
    AmazonBedrockRoleArn: Optional[str] = None

class IdentityProviderOAuthSettingTypeDef(BaseValidatorModel):
    DataSourceName: Optional[DataSourceNameType] = None
    Status: Optional[FeatureStatusType] = None
    SecretArn: Optional[str] = None

class KendraSettingsTypeDef(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None

class ModelRegisterSettingsTypeDef(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None
    CrossAccountModelRegisterRoleArn: Optional[str] = None

class TimeSeriesForecastingSettingsTypeDef(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None
    AmazonForecastRoleArn: Optional[str] = None

class WorkspaceSettingsTypeDef(BaseValidatorModel):
    S3ArtifactPath: Optional[str] = None
    S3KmsKeyId: Optional[str] = None

class CapacitySizeTypeDef(BaseValidatorModel):
    Type: CapacitySizeTypeType
    Value: int

class CaptureContentTypeHeaderOutputTypeDef(BaseValidatorModel):
    CsvContentTypes: Optional[List[str]] = None
    JsonContentTypes: Optional[List[str]] = None

class CaptureContentTypeHeaderTypeDef(BaseValidatorModel):
    CsvContentTypes: Optional[Sequence[str]] = None
    JsonContentTypes: Optional[Sequence[str]] = None

class CaptureOptionTypeDef(BaseValidatorModel):
    CaptureMode: CaptureModeType

class CategoricalParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Value: List[str]

class CategoricalParameterRangeExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[str]

class CategoricalParameterRangeOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[str]

class CategoricalParameterRangeSpecificationOutputTypeDef(BaseValidatorModel):
    Values: List[str]

class CategoricalParameterRangeSpecificationTypeDef(BaseValidatorModel):
    Values: Sequence[str]

class CategoricalParameterRangeTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]

class CategoricalParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: Sequence[str]

class ShuffleConfigTypeDef(BaseValidatorModel):
    Seed: int

class ChannelSpecificationOutputTypeDef(BaseValidatorModel):
    Name: str
    SupportedContentTypes: List[str]
    SupportedInputModes: List[TrainingInputModeType]
    Description: Optional[str] = None
    IsRequired: Optional[bool] = None
    SupportedCompressionTypes: Optional[List[CompressionTypeType]] = None

class ChannelSpecificationTypeDef(BaseValidatorModel):
    Name: str
    SupportedContentTypes: Sequence[str]
    SupportedInputModes: Sequence[TrainingInputModeType]
    Description: Optional[str] = None
    IsRequired: Optional[bool] = None
    SupportedCompressionTypes: Optional[Sequence[CompressionTypeType]] = None

class CheckpointConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    LocalPath: Optional[str] = None

class ClarifyCheckStepMetadataTypeDef(BaseValidatorModel):
    CheckType: Optional[str] = None
    BaselineUsedForDriftCheckConstraints: Optional[str] = None
    CalculatedBaselineConstraints: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ViolationReport: Optional[str] = None
    CheckJobArn: Optional[str] = None
    SkipCheck: Optional[bool] = None
    RegisterNewBaseline: Optional[bool] = None

class ClarifyInferenceConfigOutputTypeDef(BaseValidatorModel):
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

class ClarifyInferenceConfigTypeDef(BaseValidatorModel):
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

class ClarifyShapBaselineConfigTypeDef(BaseValidatorModel):
    MimeType: Optional[str] = None
    ShapBaseline: Optional[str] = None
    ShapBaselineUri: Optional[str] = None

class ClarifyTextConfigTypeDef(BaseValidatorModel):
    Language: ClarifyTextLanguageType
    Granularity: ClarifyTextGranularityType

class ClusterEbsVolumeConfigTypeDef(BaseValidatorModel):
    VolumeSizeInGB: int

class ClusterLifeCycleConfigTypeDef(BaseValidatorModel):
    SourceS3Uri: str
    OnCreate: str

class ClusterInstancePlacementTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None

class ClusterInstanceStatusDetailsTypeDef(BaseValidatorModel):
    Status: ClusterInstanceStatusType
    Message: Optional[str] = None

class ClusterSummaryTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    CreationTime: datetime
    ClusterStatus: ClusterStatusType

class ContainerConfigExtraOutputTypeDef(BaseValidatorModel):
    ContainerArguments: Optional[List[str]] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerEnvironmentVariables: Optional[Dict[str, str]] = None

class FileSystemConfigTypeDef(BaseValidatorModel):
    MountPath: Optional[str] = None
    DefaultUid: Optional[int] = None
    DefaultGid: Optional[int] = None

class ContainerConfigOutputTypeDef(BaseValidatorModel):
    ContainerArguments: Optional[List[str]] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerEnvironmentVariables: Optional[Dict[str, str]] = None

class ContainerConfigTypeDef(BaseValidatorModel):
    ContainerArguments: Optional[Sequence[str]] = None
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerEnvironmentVariables: Optional[Mapping[str, str]] = None

class CustomImageTypeDef(BaseValidatorModel):
    ImageName: str
    AppImageConfigName: str
    ImageVersionNumber: Optional[int] = None

class GitConfigTypeDef(BaseValidatorModel):
    RepositoryUrl: str
    Branch: Optional[str] = None
    SecretArn: Optional[str] = None

class CodeRepositoryTypeDef(BaseValidatorModel):
    RepositoryUrl: str

class CognitoConfigTypeDef(BaseValidatorModel):
    UserPool: str
    ClientId: str

class CognitoMemberDefinitionTypeDef(BaseValidatorModel):
    UserPool: str
    UserGroup: str
    ClientId: str

class VectorConfigTypeDef(BaseValidatorModel):
    Dimension: int

class CollectionConfigurationExtraOutputTypeDef(BaseValidatorModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Dict[str, str]] = None

class CollectionConfigurationOutputTypeDef(BaseValidatorModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Dict[str, str]] = None

class CollectionConfigurationTypeDef(BaseValidatorModel):
    CollectionName: Optional[str] = None
    CollectionParameters: Optional[Mapping[str, str]] = None

class CompilationJobSummaryTypeDef(BaseValidatorModel):
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

class ConditionStepMetadataTypeDef(BaseValidatorModel):
    Outcome: Optional[ConditionOutcomeType] = None

class MultiModelConfigTypeDef(BaseValidatorModel):
    ModelCacheSetting: Optional[ModelCacheSettingType] = None

class ContextSourceTypeDef(BaseValidatorModel):
    SourceUri: str
    SourceType: Optional[str] = None
    SourceId: Optional[str] = None

class ContinuousParameterRangeSpecificationTypeDef(BaseValidatorModel):
    MinValue: str
    MaxValue: str

class ContinuousParameterRangeTypeDef(BaseValidatorModel):
    Name: str
    MinValue: str
    MaxValue: str
    ScalingType: Optional[HyperParameterScalingTypeType] = None

class ConvergenceDetectedTypeDef(BaseValidatorModel):
    CompleteOnConvergence: Optional[CompleteOnConvergenceType] = None

class MetadataPropertiesTypeDef(BaseValidatorModel):
    CommitId: Optional[str] = None
    Repository: Optional[str] = None
    GeneratedBy: Optional[str] = None
    ProjectId: Optional[str] = None

class ModelDeployConfigTypeDef(BaseValidatorModel):
    AutoGenerateEndpointName: Optional[bool] = None
    EndpointName: Optional[str] = None

class InputConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    Framework: FrameworkType
    DataInputConfig: Optional[str] = None
    FrameworkVersion: Optional[str] = None

class NeoVpcConfigTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class StoppingConditionTypeDef(BaseValidatorModel):
    MaxRuntimeInSeconds: Optional[int] = None
    MaxWaitTimeInSeconds: Optional[int] = None
    MaxPendingTimeInSeconds: Optional[int] = None

class DataQualityAppSpecificationTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    Environment: Optional[Mapping[str, str]] = None

class MonitoringStoppingConditionTypeDef(BaseValidatorModel):
    MaxRuntimeInSeconds: int

class EdgeOutputConfigTypeDef(BaseValidatorModel):
    S3OutputLocation: str
    KmsKeyId: Optional[str] = None
    PresetDeploymentType: Optional[Literal["GreengrassV2Component"]] = None
    PresetDeploymentConfig: Optional[str] = None

class EdgeDeploymentModelConfigTypeDef(BaseValidatorModel):
    ModelHandle: str
    EdgePackagingJobName: str

class ThroughputConfigTypeDef(BaseValidatorModel):
    ThroughputMode: ThroughputModeType
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None

class FlowDefinitionOutputConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None

class HumanLoopRequestSourceTypeDef(BaseValidatorModel):
    AwsManagedHumanLoopRequestSource: AwsManagedHumanLoopRequestSourceType

class HubS3StorageConfigTypeDef(BaseValidatorModel):
    S3OutputPath: Optional[str] = None

class UiTemplateTypeDef(BaseValidatorModel):
    Content: str

class CreateImageVersionRequestRequestTypeDef(BaseValidatorModel):
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

class InferenceComponentRuntimeConfigTypeDef(BaseValidatorModel):
    CopyCount: int

class LabelingJobOutputConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None
    SnsTopicArn: Optional[str] = None

class LabelingJobStoppingConditionsTypeDef(BaseValidatorModel):
    MaxHumanLabeledObjectCount: Optional[int] = None
    MaxPercentageOfInputDatasetLabeled: Optional[int] = None

class ModelBiasAppSpecificationTypeDef(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Mapping[str, str]] = None

class ModelCardExportOutputConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str

class ModelCardSecurityConfigTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None

class ModelExplainabilityAppSpecificationTypeDef(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Mapping[str, str]] = None

class InferenceExecutionConfigTypeDef(BaseValidatorModel):
    Mode: InferenceExecutionModeType

class ModelPackageModelCardTypeDef(BaseValidatorModel):
    ModelCardContent: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None

class ModelPackageSecurityConfigTypeDef(BaseValidatorModel):
    KmsKeyId: str

class ModelQualityAppSpecificationTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    ProblemType: Optional[MonitoringProblemTypeType] = None
    Environment: Optional[Mapping[str, str]] = None

class InstanceMetadataServiceConfigurationTypeDef(BaseValidatorModel):
    MinimumInstanceMetadataServiceVersion: str

class NotebookInstanceLifecycleHookTypeDef(BaseValidatorModel):
    Content: Optional[str] = None

class OptimizationJobOutputConfigTypeDef(BaseValidatorModel):
    S3OutputLocation: str
    KmsKeyId: Optional[str] = None

class OptimizationVpcConfigTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class ParallelismConfigurationTypeDef(BaseValidatorModel):
    MaxParallelExecutionSteps: int

class PipelineDefinitionS3LocationTypeDef(BaseValidatorModel):
    Bucket: str
    ObjectKey: str
    VersionId: Optional[str] = None

class CreatePresignedDomainUrlRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    SessionExpirationDurationInSeconds: Optional[int] = None
    ExpiresInSeconds: Optional[int] = None
    SpaceName: Optional[str] = None
    LandingUri: Optional[str] = None

class CreatePresignedMlflowTrackingServerUrlRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str
    ExpiresInSeconds: Optional[int] = None
    SessionExpirationDurationInSeconds: Optional[int] = None

class CreatePresignedNotebookInstanceUrlInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceName: str
    SessionExpirationDurationInSeconds: Optional[int] = None

class ExperimentConfigTypeDef(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    TrialComponentDisplayName: Optional[str] = None
    RunName: Optional[str] = None

class ProcessingStoppingConditionTypeDef(BaseValidatorModel):
    MaxRuntimeInSeconds: int

class OwnershipSettingsTypeDef(BaseValidatorModel):
    OwnerUserProfileName: str

class SpaceSharingSettingsTypeDef(BaseValidatorModel):
    SharingType: SharingTypeType

class InfraCheckConfigTypeDef(BaseValidatorModel):
    EnableInfraCheck: Optional[bool] = None

class OutputDataConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str
    KmsKeyId: Optional[str] = None
    CompressionType: Optional[OutputCompressionTypeType] = None

class ProfilerConfigTypeDef(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Mapping[str, str]] = None
    DisableProfiler: Optional[bool] = None

class RemoteDebugConfigTypeDef(BaseValidatorModel):
    EnableRemoteDebug: Optional[bool] = None

class RetryStrategyTypeDef(BaseValidatorModel):
    MaximumRetryAttempts: int

class SessionChainingConfigTypeDef(BaseValidatorModel):
    EnableSessionTagChaining: Optional[bool] = None

class TensorBoardOutputConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None

class DataProcessingTypeDef(BaseValidatorModel):
    InputFilter: Optional[str] = None
    OutputFilter: Optional[str] = None
    JoinSource: Optional[JoinSourceType] = None

class ModelClientConfigTypeDef(BaseValidatorModel):
    InvocationsTimeoutInSeconds: Optional[int] = None
    InvocationsMaxRetries: Optional[int] = None

class TransformOutputTypeDef(BaseValidatorModel):
    S3OutputPath: str
    Accept: Optional[str] = None
    AssembleWith: Optional[AssemblyTypeType] = None
    KmsKeyId: Optional[str] = None

class TransformResourcesTypeDef(BaseValidatorModel):
    InstanceType: TransformInstanceTypeType
    InstanceCount: int
    VolumeKmsKeyId: Optional[str] = None

class TrialComponentArtifactTypeDef(BaseValidatorModel):
    Value: str
    MediaType: Optional[str] = None

class TrialComponentParameterValueTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    NumberValue: Optional[float] = None

class TrialComponentStatusTypeDef(BaseValidatorModel):
    PrimaryStatus: Optional[TrialComponentPrimaryStatusType] = None
    Message: Optional[str] = None

class OidcConfigTypeDef(BaseValidatorModel):
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

class SourceIpConfigTypeDef(BaseValidatorModel):
    Cidrs: Sequence[str]

class WorkforceVpcConfigRequestTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None

class NotificationConfigurationTypeDef(BaseValidatorModel):
    NotificationTopicArn: Optional[str] = None

class EFSFileSystemConfigTypeDef(BaseValidatorModel):
    FileSystemId: str
    FileSystemPath: Optional[str] = None

class EFSFileSystemTypeDef(BaseValidatorModel):
    FileSystemId: str

class CustomPosixUserConfigTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int

class CustomizedMetricSpecificationTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None

class DataCaptureConfigSummaryTypeDef(BaseValidatorModel):
    EnableCapture: bool
    CaptureStatus: CaptureStatusType
    CurrentSamplingPercentage: int
    DestinationS3Uri: str
    KmsKeyId: str

class DataCatalogConfigTypeDef(BaseValidatorModel):
    TableName: str
    Catalog: str
    Database: str

class DataQualityAppSpecificationOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None

class MonitoringConstraintsResourceTypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None

class MonitoringStatisticsResourceTypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None

class EndpointInputTypeDef(BaseValidatorModel):
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

class FileSystemDataSourceTypeDef(BaseValidatorModel):
    FileSystemId: str
    FileSystemAccessMode: FileSystemAccessModeType
    FileSystemType: FileSystemTypeType
    DirectoryPath: str

class S3DataSourceExtraOutputTypeDef(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[List[str]] = None
    InstanceGroupNames: Optional[List[str]] = None

class S3DataSourceOutputTypeDef(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[List[str]] = None
    InstanceGroupNames: Optional[List[str]] = None

class S3DataSourceTypeDef(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str
    S3DataDistributionType: Optional[S3DataDistributionType] = None
    AttributeNames: Optional[Sequence[str]] = None
    InstanceGroupNames: Optional[Sequence[str]] = None

class RedshiftDatasetDefinitionTypeDef(BaseValidatorModel):
    ClusterId: str
    Database: str
    DbUser: str
    QueryString: str
    ClusterRoleArn: str
    OutputS3Uri: str
    OutputFormat: RedshiftResultFormatType
    KmsKeyId: Optional[str] = None
    OutputCompression: Optional[RedshiftResultCompressionTypeType] = None

class DebugRuleConfigurationExtraOutputTypeDef(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None

class DebugRuleConfigurationOutputTypeDef(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None

class DebugRuleConfigurationTypeDef(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Mapping[str, str]] = None

class DebugRuleEvaluationStatusTypeDef(BaseValidatorModel):
    RuleConfigurationName: Optional[str] = None
    RuleEvaluationJobArn: Optional[str] = None
    RuleEvaluationStatus: Optional[RuleEvaluationStatusType] = None
    StatusDetails: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class DefaultEbsStorageSettingsTypeDef(BaseValidatorModel):
    DefaultEbsVolumeSizeInGb: int
    MaximumEbsVolumeSizeInGb: int

class DeleteActionRequestRequestTypeDef(BaseValidatorModel):
    ActionName: str

class DeleteAlgorithmInputRequestTypeDef(BaseValidatorModel):
    AlgorithmName: str

class DeleteAppImageConfigRequestRequestTypeDef(BaseValidatorModel):
    AppImageConfigName: str

class DeleteAppRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None

class DeleteAssociationRequestRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str

class DeleteCodeRepositoryInputRequestTypeDef(BaseValidatorModel):
    CodeRepositoryName: str

class DeleteCompilationJobRequestRequestTypeDef(BaseValidatorModel):
    CompilationJobName: str

class DeleteContextRequestRequestTypeDef(BaseValidatorModel):
    ContextName: str

class DeleteDataQualityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class DeleteDeviceFleetRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str

class RetentionPolicyTypeDef(BaseValidatorModel):
    HomeEfsFileSystem: Optional[RetentionTypeType] = None

class DeleteEdgeDeploymentPlanRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str

class DeleteEdgeDeploymentStageRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str

class DeleteEndpointConfigInputRequestTypeDef(BaseValidatorModel):
    EndpointConfigName: str

class DeleteEndpointInputRequestTypeDef(BaseValidatorModel):
    EndpointName: str

class DeleteExperimentRequestRequestTypeDef(BaseValidatorModel):
    ExperimentName: str

class DeleteFeatureGroupRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str

class DeleteFlowDefinitionRequestRequestTypeDef(BaseValidatorModel):
    FlowDefinitionName: str

class DeleteHubContentReferenceRequestRequestTypeDef(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str

class DeleteHubContentRequestRequestTypeDef(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: str

class DeleteHubRequestRequestTypeDef(BaseValidatorModel):
    HubName: str

class DeleteHumanTaskUiRequestRequestTypeDef(BaseValidatorModel):
    HumanTaskUiName: str

class DeleteHyperParameterTuningJobRequestRequestTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: str

class DeleteImageRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str

class DeleteImageVersionRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None

class DeleteInferenceComponentInputRequestTypeDef(BaseValidatorModel):
    InferenceComponentName: str

class DeleteInferenceExperimentRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteMlflowTrackingServerRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str

class DeleteModelBiasJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class DeleteModelCardRequestRequestTypeDef(BaseValidatorModel):
    ModelCardName: str

class DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class DeleteModelInputRequestTypeDef(BaseValidatorModel):
    ModelName: str

class DeleteModelPackageGroupInputRequestTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str

class DeleteModelPackageGroupPolicyInputRequestTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str

class DeleteModelPackageInputRequestTypeDef(BaseValidatorModel):
    ModelPackageName: str

class DeleteModelQualityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class DeleteMonitoringScheduleRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str

class DeleteNotebookInstanceInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceName: str

class DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str

class DeleteOptimizationJobRequestRequestTypeDef(BaseValidatorModel):
    OptimizationJobName: str

class DeletePipelineRequestRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str

class DeleteProjectInputRequestTypeDef(BaseValidatorModel):
    ProjectName: str

class DeleteSpaceRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpaceName: str

class DeleteStudioLifecycleConfigRequestRequestTypeDef(BaseValidatorModel):
    StudioLifecycleConfigName: str

class DeleteTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class DeleteTrialComponentRequestRequestTypeDef(BaseValidatorModel):
    TrialComponentName: str

class DeleteTrialRequestRequestTypeDef(BaseValidatorModel):
    TrialName: str

class DeleteUserProfileRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    UserProfileName: str

class DeleteWorkforceRequestRequestTypeDef(BaseValidatorModel):
    WorkforceName: str

class DeleteWorkteamRequestRequestTypeDef(BaseValidatorModel):
    WorkteamName: str

class DeployedImageTypeDef(BaseValidatorModel):
    SpecifiedImage: Optional[str] = None
    ResolvedImage: Optional[str] = None
    ResolutionTime: Optional[datetime] = None

class RealTimeInferenceRecommendationTypeDef(BaseValidatorModel):
    RecommendationId: str
    InstanceType: ProductionVariantInstanceTypeType
    Environment: Optional[Dict[str, str]] = None

class DeviceSelectionConfigOutputTypeDef(BaseValidatorModel):
    DeviceSubsetType: DeviceSubsetTypeType
    Percentage: Optional[int] = None
    DeviceNames: Optional[List[str]] = None
    DeviceNameContains: Optional[str] = None

class EdgeDeploymentConfigTypeDef(BaseValidatorModel):
    FailureHandlingPolicy: FailureHandlingPolicyType

class EdgeDeploymentStatusTypeDef(BaseValidatorModel):
    StageStatus: StageStatusType
    EdgeDeploymentSuccessInStage: int
    EdgeDeploymentPendingInStage: int
    EdgeDeploymentFailedInStage: int
    EdgeDeploymentStatusMessage: Optional[str] = None
    EdgeDeploymentStageStartTime: Optional[datetime] = None

class DeviceSelectionConfigTypeDef(BaseValidatorModel):
    DeviceSubsetType: DeviceSubsetTypeType
    Percentage: Optional[int] = None
    DeviceNames: Optional[Sequence[str]] = None
    DeviceNameContains: Optional[str] = None

class DeregisterDevicesRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str
    DeviceNames: Sequence[str]

class DerivedInformationTypeDef(BaseValidatorModel):
    DerivedDataInputConfig: Optional[str] = None

class DescribeActionRequestRequestTypeDef(BaseValidatorModel):
    ActionName: str

class DescribeAlgorithmInputRequestTypeDef(BaseValidatorModel):
    AlgorithmName: str

class DescribeAppImageConfigRequestRequestTypeDef(BaseValidatorModel):
    AppImageConfigName: str

class DescribeAppRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None

class DescribeArtifactRequestRequestTypeDef(BaseValidatorModel):
    ArtifactArn: str

class DescribeAutoMLJobRequestRequestTypeDef(BaseValidatorModel):
    AutoMLJobName: str

class ModelDeployResultTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None

class DescribeAutoMLJobV2RequestRequestTypeDef(BaseValidatorModel):
    AutoMLJobName: str

class DescribeClusterNodeRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NodeId: str

class DescribeClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str

class DescribeCodeRepositoryInputRequestTypeDef(BaseValidatorModel):
    CodeRepositoryName: str

class DescribeCompilationJobRequestRequestTypeDef(BaseValidatorModel):
    CompilationJobName: str

class ModelArtifactsTypeDef(BaseValidatorModel):
    S3ModelArtifacts: str

class ModelDigestsTypeDef(BaseValidatorModel):
    ArtifactDigest: Optional[str] = None

class NeoVpcConfigOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class DescribeContextRequestRequestTypeDef(BaseValidatorModel):
    ContextName: str

class DescribeDataQualityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class DescribeDeviceFleetRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str

class DescribeDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceName: str
    DeviceFleetName: str
    NextToken: Optional[str] = None

class EdgeModelTypeDef(BaseValidatorModel):
    ModelName: str
    ModelVersion: str
    LatestSampleTime: Optional[datetime] = None
    LatestInference: Optional[datetime] = None

class DescribeDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str

class DescribeEdgeDeploymentPlanRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEdgePackagingJobRequestRequestTypeDef(BaseValidatorModel):
    EdgePackagingJobName: str

class EdgePresetDeploymentOutputTypeDef(BaseValidatorModel):
    Type: Literal["GreengrassV2Component"]
    Artifact: Optional[str] = None
    Status: Optional[EdgePresetDeploymentStatusType] = None
    StatusMessage: Optional[str] = None

class DescribeEndpointConfigInputRequestTypeDef(BaseValidatorModel):
    EndpointConfigName: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeEndpointInputRequestTypeDef(BaseValidatorModel):
    EndpointName: str

class DescribeExperimentRequestRequestTypeDef(BaseValidatorModel):
    ExperimentName: str

class ExperimentSourceTypeDef(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None

class DescribeFeatureGroupRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    NextToken: Optional[str] = None

class LastUpdateStatusTypeDef(BaseValidatorModel):
    Status: LastUpdateStatusValueType
    FailureReason: Optional[str] = None

class OfflineStoreStatusTypeDef(BaseValidatorModel):
    Status: OfflineStoreStatusValueType
    BlockedReason: Optional[str] = None

class ThroughputConfigDescriptionTypeDef(BaseValidatorModel):
    ThroughputMode: ThroughputModeType
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None

class DescribeFeatureMetadataRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    FeatureName: str

class FeatureParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DescribeFlowDefinitionRequestRequestTypeDef(BaseValidatorModel):
    FlowDefinitionName: str

class DescribeHubContentRequestRequestTypeDef(BaseValidatorModel):
    HubName: str
    HubContentType: HubContentTypeType
    HubContentName: str
    HubContentVersion: Optional[str] = None

class HubContentDependencyTypeDef(BaseValidatorModel):
    DependencyOriginPath: Optional[str] = None
    DependencyCopyPath: Optional[str] = None

class DescribeHubRequestRequestTypeDef(BaseValidatorModel):
    HubName: str

class DescribeHumanTaskUiRequestRequestTypeDef(BaseValidatorModel):
    HumanTaskUiName: str

class UiTemplateInfoTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    ContentSha256: Optional[str] = None

class DescribeHyperParameterTuningJobRequestRequestTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: str

class HyperParameterTuningJobCompletionDetailsTypeDef(BaseValidatorModel):
    NumberOfTrainingJobsObjectiveNotImproving: Optional[int] = None
    ConvergenceDetectedTime: Optional[datetime] = None

class HyperParameterTuningJobConsumedResourcesTypeDef(BaseValidatorModel):
    RuntimeInSeconds: Optional[int] = None

class ObjectiveStatusCountersTypeDef(BaseValidatorModel):
    Succeeded: Optional[int] = None
    Pending: Optional[int] = None
    Failed: Optional[int] = None

class TrainingJobStatusCountersTypeDef(BaseValidatorModel):
    Completed: Optional[int] = None
    InProgress: Optional[int] = None
    RetryableError: Optional[int] = None
    NonRetryableError: Optional[int] = None
    Stopped: Optional[int] = None

class DescribeImageRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str

class DescribeImageVersionRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None

class DescribeInferenceComponentInputRequestTypeDef(BaseValidatorModel):
    InferenceComponentName: str

class InferenceComponentRuntimeConfigSummaryTypeDef(BaseValidatorModel):
    DesiredCopyCount: Optional[int] = None
    CurrentCopyCount: Optional[int] = None

class DescribeInferenceExperimentRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class EndpointMetadataTypeDef(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: Optional[str] = None
    EndpointStatus: Optional[EndpointStatusType] = None
    FailureReason: Optional[str] = None

class InferenceExperimentScheduleOutputTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class DescribeInferenceRecommendationsJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: str

class DescribeLabelingJobRequestRequestTypeDef(BaseValidatorModel):
    LabelingJobName: str

class LabelCountersTypeDef(BaseValidatorModel):
    TotalLabeled: Optional[int] = None
    HumanLabeled: Optional[int] = None
    MachineLabeled: Optional[int] = None
    FailedNonRetryableError: Optional[int] = None
    Unlabeled: Optional[int] = None

class LabelingJobOutputTypeDef(BaseValidatorModel):
    OutputDatasetS3Uri: str
    FinalActiveLearningModelArn: Optional[str] = None

class DescribeLineageGroupRequestRequestTypeDef(BaseValidatorModel):
    LineageGroupName: str

class DescribeMlflowTrackingServerRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str

class DescribeModelBiasJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class ModelBiasAppSpecificationOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None

class DescribeModelCardExportJobRequestRequestTypeDef(BaseValidatorModel):
    ModelCardExportJobArn: str

class ModelCardExportArtifactsTypeDef(BaseValidatorModel):
    S3ExportArtifacts: str

class DescribeModelCardRequestRequestTypeDef(BaseValidatorModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None

class DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class ModelExplainabilityAppSpecificationOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ConfigUri: str
    Environment: Optional[Dict[str, str]] = None

class DescribeModelInputRequestTypeDef(BaseValidatorModel):
    ModelName: str

class DescribeModelPackageGroupInputRequestTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str

class DescribeModelPackageInputRequestTypeDef(BaseValidatorModel):
    ModelPackageName: str

class DescribeModelQualityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
    JobDefinitionName: str

class ModelQualityAppSpecificationOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None
    ProblemType: Optional[MonitoringProblemTypeType] = None
    Environment: Optional[Dict[str, str]] = None

class DescribeMonitoringScheduleRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str

class MonitoringExecutionSummaryTypeDef(BaseValidatorModel):
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

class DescribeNotebookInstanceInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceName: str

class DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str

class DescribeOptimizationJobRequestRequestTypeDef(BaseValidatorModel):
    OptimizationJobName: str

class OptimizationOutputTypeDef(BaseValidatorModel):
    RecommendedInferenceImage: Optional[str] = None

class OptimizationVpcConfigOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class DescribePipelineDefinitionForExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str

class DescribePipelineExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str

class PipelineExperimentConfigTypeDef(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None

class DescribePipelineRequestRequestTypeDef(BaseValidatorModel):
    PipelineName: str

class DescribeProcessingJobRequestRequestTypeDef(BaseValidatorModel):
    ProcessingJobName: str

class DescribeProjectInputRequestTypeDef(BaseValidatorModel):
    ProjectName: str

class ServiceCatalogProvisionedProductDetailsTypeDef(BaseValidatorModel):
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductStatusMessage: Optional[str] = None

class DescribeSpaceRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpaceName: str

class DescribeStudioLifecycleConfigRequestRequestTypeDef(BaseValidatorModel):
    StudioLifecycleConfigName: str

class DescribeSubscribedWorkteamRequestRequestTypeDef(BaseValidatorModel):
    WorkteamArn: str

class SubscribedWorkteamTypeDef(BaseValidatorModel):
    WorkteamArn: str
    MarketplaceTitle: Optional[str] = None
    SellerName: Optional[str] = None
    MarketplaceDescription: Optional[str] = None
    ListingId: Optional[str] = None

class DescribeTrainingJobRequestRequestTypeDef(BaseValidatorModel):
    TrainingJobName: str

class MetricDataTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Value: Optional[float] = None
    Timestamp: Optional[datetime] = None

class ProfilerConfigOutputTypeDef(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None

class ProfilerRuleConfigurationOutputTypeDef(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Dict[str, str]] = None

class ProfilerRuleEvaluationStatusTypeDef(BaseValidatorModel):
    RuleConfigurationName: Optional[str] = None
    RuleEvaluationJobArn: Optional[str] = None
    RuleEvaluationStatus: Optional[RuleEvaluationStatusType] = None
    StatusDetails: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class SecondaryStatusTransitionTypeDef(BaseValidatorModel):
    Status: SecondaryStatusType
    StartTime: datetime
    EndTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class WarmPoolStatusTypeDef(BaseValidatorModel):
    Status: WarmPoolResourceStatusType
    ResourceRetainedBillableTimeInSeconds: Optional[int] = None
    ReusedByJob: Optional[str] = None

class DescribeTransformJobRequestRequestTypeDef(BaseValidatorModel):
    TransformJobName: str

class DescribeTrialComponentRequestRequestTypeDef(BaseValidatorModel):
    TrialComponentName: str

class TrialComponentMetricSummaryTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    SourceArn: Optional[str] = None
    TimeStamp: Optional[datetime] = None
    Max: Optional[float] = None
    Min: Optional[float] = None
    Last: Optional[float] = None
    Count: Optional[int] = None
    Avg: Optional[float] = None
    StdDev: Optional[float] = None

class TrialComponentSourceTypeDef(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None

class DescribeTrialRequestRequestTypeDef(BaseValidatorModel):
    TrialName: str

class TrialSourceTypeDef(BaseValidatorModel):
    SourceArn: str
    SourceType: Optional[str] = None

class DescribeUserProfileRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    UserProfileName: str

class DescribeWorkforceRequestRequestTypeDef(BaseValidatorModel):
    WorkforceName: str

class DescribeWorkteamRequestRequestTypeDef(BaseValidatorModel):
    WorkteamName: str

class ProductionVariantServerlessUpdateConfigTypeDef(BaseValidatorModel):
    MaxConcurrency: Optional[int] = None
    ProvisionedConcurrency: Optional[int] = None

class DeviceDeploymentSummaryTypeDef(BaseValidatorModel):
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

class DeviceFleetSummaryTypeDef(BaseValidatorModel):
    DeviceFleetArn: str
    DeviceFleetName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class DeviceStatsTypeDef(BaseValidatorModel):
    ConnectedDeviceCount: int
    RegisteredDeviceCount: int

class EdgeModelSummaryTypeDef(BaseValidatorModel):
    ModelName: str
    ModelVersion: str

class DeviceTypeDef(BaseValidatorModel):
    DeviceName: str
    Description: Optional[str] = None
    IotThingName: Optional[str] = None

class DisassociateTrialComponentRequestRequestTypeDef(BaseValidatorModel):
    TrialComponentName: str
    TrialName: str

class DockerSettingsOutputTypeDef(BaseValidatorModel):
    EnableDockerAccess: Optional[FeatureStatusType] = None
    VpcOnlyTrustedAccounts: Optional[List[str]] = None

class DockerSettingsTypeDef(BaseValidatorModel):
    EnableDockerAccess: Optional[FeatureStatusType] = None
    VpcOnlyTrustedAccounts: Optional[Sequence[str]] = None

class DomainDetailsTypeDef(BaseValidatorModel):
    DomainArn: Optional[str] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Status: Optional[DomainStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Url: Optional[str] = None

class FileSourceTypeDef(BaseValidatorModel):
    S3Uri: str
    ContentType: Optional[str] = None
    ContentDigest: Optional[str] = None

class EMRStepMetadataTypeDef(BaseValidatorModel):
    ClusterId: Optional[str] = None
    StepId: Optional[str] = None
    StepName: Optional[str] = None
    LogFilePath: Optional[str] = None

class EbsStorageSettingsTypeDef(BaseValidatorModel):
    EbsVolumeSizeInGb: int

class EdgeDeploymentPlanSummaryTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    EdgeDeploymentPlanName: str
    DeviceFleetName: str
    EdgeDeploymentSuccess: int
    EdgeDeploymentPending: int
    EdgeDeploymentFailed: int
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class EdgeModelStatTypeDef(BaseValidatorModel):
    ModelName: str
    ModelVersion: str
    OfflineDeviceCount: int
    ConnectedDeviceCount: int
    ActiveDeviceCount: int
    SamplingDeviceCount: int

class EdgePackagingJobSummaryTypeDef(BaseValidatorModel):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    EdgePackagingJobStatus: EdgePackagingJobStatusType
    CompilationJobName: Optional[str] = None
    ModelName: Optional[str] = None
    ModelVersion: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class EdgeTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None

class EndpointConfigSummaryTypeDef(BaseValidatorModel):
    EndpointConfigName: str
    EndpointConfigArn: str
    CreationTime: datetime

class EndpointInfoTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None

class ProductionVariantServerlessConfigTypeDef(BaseValidatorModel):
    MemorySizeInMB: int
    MaxConcurrency: int
    ProvisionedConcurrency: Optional[int] = None

class InferenceMetricsTypeDef(BaseValidatorModel):
    MaxInvocations: int
    ModelLatency: int

class EndpointSummaryTypeDef(BaseValidatorModel):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatusType

class EnvironmentParameterTypeDef(BaseValidatorModel):
    Key: str
    ValueType: str
    Value: str

class FailStepMetadataTypeDef(BaseValidatorModel):
    ErrorMessage: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Operator: Optional[OperatorType] = None
    Value: Optional[str] = None

class FinalHyperParameterTuningJobObjectiveMetricTypeDef(BaseValidatorModel):
    MetricName: str
    Value: float
    Type: Optional[HyperParameterTuningJobObjectiveTypeType] = None

class FlowDefinitionSummaryTypeDef(BaseValidatorModel):
    FlowDefinitionName: str
    FlowDefinitionArn: str
    FlowDefinitionStatus: FlowDefinitionStatusType
    CreationTime: datetime
    FailureReason: Optional[str] = None

class GetDeviceFleetReportRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str

class GetLineageGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    LineageGroupName: str

class GetModelPackageGroupPolicyInputRequestTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str

class ScalingPolicyObjectiveTypeDef(BaseValidatorModel):
    MinInvocationsPerMinute: Optional[int] = None
    MaxInvocationsPerMinute: Optional[int] = None

class ScalingPolicyMetricTypeDef(BaseValidatorModel):
    InvocationsPerInstance: Optional[int] = None
    ModelLatency: Optional[int] = None

class PropertyNameSuggestionTypeDef(BaseValidatorModel):
    PropertyName: Optional[str] = None

class GitConfigForUpdateTypeDef(BaseValidatorModel):
    SecretArn: Optional[str] = None

class HolidayConfigAttributesTypeDef(BaseValidatorModel):
    CountryCode: Optional[str] = None

class HubContentInfoTypeDef(BaseValidatorModel):
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

class HubInfoTypeDef(BaseValidatorModel):
    HubName: str
    HubArn: str
    HubStatus: HubStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    HubDisplayName: Optional[str] = None
    HubDescription: Optional[str] = None
    HubSearchKeywords: Optional[List[str]] = None

class HumanLoopActivationConditionsConfigTypeDef(BaseValidatorModel):
    HumanLoopActivationConditions: str

class UiConfigTypeDef(BaseValidatorModel):
    UiTemplateS3Uri: Optional[str] = None
    HumanTaskUiArn: Optional[str] = None

class HumanTaskUiSummaryTypeDef(BaseValidatorModel):
    HumanTaskUiName: str
    HumanTaskUiArn: str
    CreationTime: datetime

class HyperParameterTuningJobObjectiveTypeDef(BaseValidatorModel):
    Type: HyperParameterTuningJobObjectiveTypeType
    MetricName: str

class VpcConfigExtraOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class HyperParameterTuningInstanceConfigTypeDef(BaseValidatorModel):
    InstanceType: TrainingInstanceTypeType
    InstanceCount: int
    VolumeSizeInGB: int

class ResourceLimitsTypeDef(BaseValidatorModel):
    MaxParallelTrainingJobs: int
    MaxNumberOfTrainingJobs: Optional[int] = None
    MaxRuntimeInSeconds: Optional[int] = None

class HyperbandStrategyConfigTypeDef(BaseValidatorModel):
    MinResource: Optional[int] = None
    MaxResource: Optional[int] = None

class ParentHyperParameterTuningJobTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: Optional[str] = None

class IamIdentityTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    PrincipalId: Optional[str] = None
    SourceIdentity: Optional[str] = None

class IamPolicyConstraintsTypeDef(BaseValidatorModel):
    SourceIp: Optional[EnabledOrDisabledType] = None
    VpcSourceIp: Optional[EnabledOrDisabledType] = None

class RepositoryAuthConfigTypeDef(BaseValidatorModel):
    RepositoryCredentialsProviderArn: str

class ImageTypeDef(BaseValidatorModel):
    CreationTime: datetime
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatusType
    LastModifiedTime: datetime
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    FailureReason: Optional[str] = None

class ImageVersionTypeDef(BaseValidatorModel):
    CreationTime: datetime
    ImageArn: str
    ImageVersionArn: str
    ImageVersionStatus: ImageVersionStatusType
    LastModifiedTime: datetime
    Version: int
    FailureReason: Optional[str] = None

class InferenceComponentComputeResourceRequirementsTypeDef(BaseValidatorModel):
    MinMemoryRequiredInMb: int
    NumberOfCpuCoresRequired: Optional[float] = None
    NumberOfAcceleratorDevicesRequired: Optional[float] = None
    MaxMemoryRequiredInMb: Optional[int] = None

class InferenceComponentContainerSpecificationTypeDef(BaseValidatorModel):
    Image: Optional[str] = None
    ArtifactUrl: Optional[str] = None
    Environment: Optional[Mapping[str, str]] = None

class InferenceComponentStartupParametersTypeDef(BaseValidatorModel):
    ModelDataDownloadTimeoutInSeconds: Optional[int] = None
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int] = None

class InferenceComponentSummaryTypeDef(BaseValidatorModel):
    CreationTime: datetime
    InferenceComponentArn: str
    InferenceComponentName: str
    EndpointArn: str
    EndpointName: str
    VariantName: str
    LastModifiedTime: datetime
    InferenceComponentStatus: Optional[InferenceComponentStatusType] = None

class InferenceExperimentScheduleExtraOutputTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class InferenceHubAccessConfigTypeDef(BaseValidatorModel):
    HubContentArn: str

class RecommendationMetricsTypeDef(BaseValidatorModel):
    CostPerHour: Optional[float] = None
    CostPerInference: Optional[float] = None
    MaxInvocations: Optional[int] = None
    ModelLatency: Optional[int] = None
    CpuUtilization: Optional[float] = None
    MemoryUtilization: Optional[float] = None
    ModelSetupTime: Optional[int] = None

class InferenceRecommendationsJobTypeDef(BaseValidatorModel):
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

class InstanceGroupTypeDef(BaseValidatorModel):
    InstanceType: TrainingInstanceTypeType
    InstanceCount: int
    InstanceGroupName: str

class IntegerParameterRangeSpecificationTypeDef(BaseValidatorModel):
    MinValue: str
    MaxValue: str

class IntegerParameterRangeTypeDef(BaseValidatorModel):
    Name: str
    MinValue: str
    MaxValue: str
    ScalingType: Optional[HyperParameterScalingTypeType] = None

class KernelSpecTypeDef(BaseValidatorModel):
    Name: str
    DisplayName: Optional[str] = None

class LabelCountersForWorkteamTypeDef(BaseValidatorModel):
    HumanLabeled: Optional[int] = None
    PendingHuman: Optional[int] = None
    Total: Optional[int] = None

class LabelingJobDataAttributesExtraOutputTypeDef(BaseValidatorModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None

class LabelingJobDataAttributesOutputTypeDef(BaseValidatorModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None

class LabelingJobDataAttributesTypeDef(BaseValidatorModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None

class LabelingJobS3DataSourceTypeDef(BaseValidatorModel):
    ManifestS3Uri: str

class LabelingJobSnsDataSourceTypeDef(BaseValidatorModel):
    SnsTopicArn: str

class LineageGroupSummaryTypeDef(BaseValidatorModel):
    LineageGroupArn: Optional[str] = None
    LineageGroupName: Optional[str] = None
    DisplayName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None

class ListCandidatesForAutoMLJobRequestRequestTypeDef(BaseValidatorModel):
    AutoMLJobName: str
    StatusEquals: Optional[CandidateStatusType] = None
    CandidateNameEquals: Optional[str] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[CandidateSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MonitoringJobDefinitionSummaryTypeDef(BaseValidatorModel):
    MonitoringJobDefinitionName: str
    MonitoringJobDefinitionArn: str
    CreationTime: datetime
    EndpointName: str

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInferenceRecommendationsJobStepsRequestRequestTypeDef(BaseValidatorModel):
    JobName: str
    Status: Optional[RecommendationJobStatusType] = None
    StepType: Optional[Literal["BENCHMARK"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TrackingServerSummaryTypeDef(BaseValidatorModel):
    TrackingServerArn: Optional[str] = None
    TrackingServerName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    IsActive: Optional[IsTrackingServerActiveType] = None
    MlflowVersion: Optional[str] = None

class ModelCardExportJobSummaryTypeDef(BaseValidatorModel):
    ModelCardExportJobName: str
    ModelCardExportJobArn: str
    Status: ModelCardExportJobStatusType
    ModelCardName: str
    ModelCardVersion: int
    CreatedAt: datetime
    LastModifiedAt: datetime

class ModelCardVersionSummaryTypeDef(BaseValidatorModel):
    ModelCardName: str
    ModelCardArn: str
    ModelCardStatus: ModelCardStatusType
    ModelCardVersion: int
    CreationTime: datetime
    LastModifiedTime: Optional[datetime] = None

class ModelCardSummaryTypeDef(BaseValidatorModel):
    ModelCardName: str
    ModelCardArn: str
    ModelCardStatus: ModelCardStatusType
    CreationTime: datetime
    LastModifiedTime: Optional[datetime] = None

class ModelMetadataSummaryTypeDef(BaseValidatorModel):
    Domain: str
    Framework: str
    Task: str
    Model: str
    FrameworkVersion: str

class ModelPackageGroupSummaryTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    CreationTime: datetime
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ModelPackageGroupDescription: Optional[str] = None

class ModelPackageSummaryTypeDef(BaseValidatorModel):
    ModelPackageArn: str
    CreationTime: datetime
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageName: Optional[str] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageVersion: Optional[int] = None
    ModelPackageDescription: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None

class ModelSummaryTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    CreationTime: datetime

class MonitoringAlertHistorySummaryTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    CreationTime: datetime
    AlertStatus: MonitoringAlertStatusType

class ListMonitoringAlertsRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MonitoringScheduleSummaryTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleStatus: ScheduleStatusType
    EndpointName: Optional[str] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class NotebookInstanceLifecycleConfigSummaryTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    NotebookInstanceLifecycleConfigArn: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class NotebookInstanceSummaryTypeDef(BaseValidatorModel):
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

class OptimizationJobSummaryTypeDef(BaseValidatorModel):
    OptimizationJobName: str
    OptimizationJobArn: str
    CreationTime: datetime
    OptimizationJobStatus: OptimizationJobStatusType
    DeploymentInstanceType: OptimizationJobDeploymentInstanceTypeType
    OptimizationTypes: List[str]
    OptimizationStartTime: Optional[datetime] = None
    OptimizationEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class ListPipelineExecutionStepsRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None

class PipelineExecutionSummaryTypeDef(BaseValidatorModel):
    PipelineExecutionArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    PipelineExecutionStatus: Optional[PipelineExecutionStatusType] = None
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineExecutionFailureReason: Optional[str] = None

class ListPipelineParametersForExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class PipelineSummaryTypeDef(BaseValidatorModel):
    PipelineArn: Optional[str] = None
    PipelineName: Optional[str] = None
    PipelineDisplayName: Optional[str] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastExecutionTime: Optional[datetime] = None

class ProcessingJobSummaryTypeDef(BaseValidatorModel):
    ProcessingJobName: str
    ProcessingJobArn: str
    CreationTime: datetime
    ProcessingJobStatus: ProcessingJobStatusType
    ProcessingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    ExitMessage: Optional[str] = None

class ProjectSummaryTypeDef(BaseValidatorModel):
    ProjectName: str
    ProjectArn: str
    ProjectId: str
    CreationTime: datetime
    ProjectStatus: ProjectStatusType
    ProjectDescription: Optional[str] = None

class ResourceCatalogTypeDef(BaseValidatorModel):
    ResourceCatalogArn: str
    ResourceCatalogName: str
    Description: str
    CreationTime: datetime

class ListSpacesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None

class ListStageDevicesRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ExcludeDevicesDeployedInOtherStage: Optional[bool] = None

class StudioLifecycleConfigDetailsTypeDef(BaseValidatorModel):
    StudioLifecycleConfigArn: Optional[str] = None
    StudioLifecycleConfigName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    StudioLifecycleConfigAppType: Optional[StudioLifecycleConfigAppTypeType] = None

class ListSubscribedWorkteamsRequestRequestTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[TrainingJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None

class TransformJobSummaryTypeDef(BaseValidatorModel):
    TransformJobName: str
    TransformJobArn: str
    CreationTime: datetime
    TransformJobStatus: TransformJobStatusType
    TransformEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    FailureReason: Optional[str] = None

class ListUserProfilesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[UserProfileSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameContains: Optional[str] = None

class UserProfileDetailsTypeDef(BaseValidatorModel):
    DomainId: Optional[str] = None
    UserProfileName: Optional[str] = None
    Status: Optional[UserProfileStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class ListWorkforcesRequestRequestTypeDef(BaseValidatorModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListWorkteamsRequestRequestTypeDef(BaseValidatorModel):
    SortBy: Optional[ListWorkteamsSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OidcMemberDefinitionExtraOutputTypeDef(BaseValidatorModel):
    Groups: Optional[List[str]] = None

class OidcMemberDefinitionOutputTypeDef(BaseValidatorModel):
    Groups: Optional[List[str]] = None

class OidcMemberDefinitionTypeDef(BaseValidatorModel):
    Groups: Optional[Sequence[str]] = None

class PredefinedMetricSpecificationTypeDef(BaseValidatorModel):
    PredefinedMetricType: Optional[str] = None

class ModelAccessConfigTypeDef(BaseValidatorModel):
    AcceptEula: bool

class MonitoringGroundTruthS3InputTypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None

class ModelCompilationConfigOutputTypeDef(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None

class ModelCompilationConfigTypeDef(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Mapping[str, str]] = None

class ModelDashboardEndpointTypeDef(BaseValidatorModel):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatusType

class ModelDashboardIndicatorActionTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class RealTimeInferenceConfigTypeDef(BaseValidatorModel):
    InstanceType: InstanceTypeType
    InstanceCount: int

class ModelInputTypeDef(BaseValidatorModel):
    DataInputConfig: str

class ModelLatencyThresholdTypeDef(BaseValidatorModel):
    Percentile: Optional[str] = None
    ValueInMilliseconds: Optional[int] = None

class ModelMetadataFilterTypeDef(BaseValidatorModel):
    Name: ModelMetadataFilterTypeType
    Value: str

class ModelPackageStatusItemTypeDef(BaseValidatorModel):
    Name: str
    Status: DetailedModelPackageStatusType
    FailureReason: Optional[str] = None

class ModelQuantizationConfigOutputTypeDef(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Dict[str, str]] = None

class ModelQuantizationConfigTypeDef(BaseValidatorModel):
    Image: Optional[str] = None
    OverrideEnvironment: Optional[Mapping[str, str]] = None

class ModelStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class MonitoringAppSpecificationExtraOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None

class MonitoringAppSpecificationOutputTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None

class MonitoringAppSpecificationTypeDef(BaseValidatorModel):
    ImageUri: str
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    RecordPreprocessorSourceUri: Optional[str] = None
    PostAnalyticsProcessorSourceUri: Optional[str] = None

class MonitoringClusterConfigTypeDef(BaseValidatorModel):
    InstanceCount: int
    InstanceType: ProcessingInstanceTypeType
    VolumeSizeInGB: int
    VolumeKmsKeyId: Optional[str] = None

class MonitoringCsvDatasetFormatTypeDef(BaseValidatorModel):
    Header: Optional[bool] = None

class MonitoringJsonDatasetFormatTypeDef(BaseValidatorModel):
    Line: Optional[bool] = None

class MonitoringS3OutputTypeDef(BaseValidatorModel):
    S3Uri: str
    LocalPath: str
    S3UploadMode: Optional[ProcessingS3UploadModeType] = None

class ScheduleConfigTypeDef(BaseValidatorModel):
    ScheduleExpression: str
    DataAnalysisStartTime: Optional[str] = None
    DataAnalysisEndTime: Optional[str] = None

class S3StorageConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None
    ResolvedOutputS3Uri: Optional[str] = None

class OidcConfigForResponseTypeDef(BaseValidatorModel):
    ClientId: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    LogoutEndpoint: Optional[str] = None
    JwksUri: Optional[str] = None
    Scope: Optional[str] = None
    AuthenticationRequestExtraParams: Optional[Dict[str, str]] = None

class OnlineStoreSecurityConfigTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None

class TtlDurationTypeDef(BaseValidatorModel):
    Unit: Optional[TtlDurationUnitType] = None
    Value: Optional[int] = None

class OptimizationModelAccessConfigTypeDef(BaseValidatorModel):
    AcceptEula: bool

class TargetPlatformTypeDef(BaseValidatorModel):
    Os: TargetPlatformOsType
    Arch: TargetPlatformArchType
    Accelerator: Optional[TargetPlatformAcceleratorType] = None

class OwnershipSettingsSummaryTypeDef(BaseValidatorModel):
    OwnerUserProfileName: Optional[str] = None

class ParentTypeDef(BaseValidatorModel):
    TrialName: Optional[str] = None
    ExperimentName: Optional[str] = None

class ProductionVariantManagedInstanceScalingTypeDef(BaseValidatorModel):
    Status: Optional[ManagedInstanceScalingStatusType] = None
    MinInstanceCount: Optional[int] = None
    MaxInstanceCount: Optional[int] = None

class ProductionVariantRoutingConfigTypeDef(BaseValidatorModel):
    RoutingStrategy: RoutingStrategyType

class ProductionVariantStatusTypeDef(BaseValidatorModel):
    Status: VariantStatusType
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None

class PhaseTypeDef(BaseValidatorModel):
    InitialNumberOfUsers: Optional[int] = None
    SpawnRate: Optional[int] = None
    DurationInSeconds: Optional[int] = None

class ProcessingJobStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class QualityCheckStepMetadataTypeDef(BaseValidatorModel):
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

class RegisterModelStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class TrainingJobStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class TransformJobStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class TuningJobStepMetaDataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class SelectiveExecutionResultTypeDef(BaseValidatorModel):
    SourcePipelineExecutionArn: Optional[str] = None

class ProcessingClusterConfigTypeDef(BaseValidatorModel):
    InstanceCount: int
    InstanceType: ProcessingInstanceTypeType
    VolumeSizeInGB: int
    VolumeKmsKeyId: Optional[str] = None

class ProcessingFeatureStoreOutputTypeDef(BaseValidatorModel):
    FeatureGroupName: str

class ProcessingS3InputTypeDef(BaseValidatorModel):
    S3Uri: str
    S3DataType: ProcessingS3DataTypeType
    LocalPath: Optional[str] = None
    S3InputMode: Optional[ProcessingS3InputModeType] = None
    S3DataDistributionType: Optional[ProcessingS3DataDistributionTypeType] = None
    S3CompressionType: Optional[ProcessingS3CompressionTypeType] = None

class ProcessingS3OutputTypeDef(BaseValidatorModel):
    S3Uri: str
    LocalPath: str
    S3UploadMode: ProcessingS3UploadModeType

class ProductionVariantCoreDumpConfigTypeDef(BaseValidatorModel):
    DestinationS3Uri: str
    KmsKeyId: Optional[str] = None

class ProfilerConfigExtraOutputTypeDef(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Dict[str, str]] = None
    DisableProfiler: Optional[bool] = None

class ProfilerConfigForUpdateTypeDef(BaseValidatorModel):
    S3OutputPath: Optional[str] = None
    ProfilingIntervalInMilliseconds: Optional[int] = None
    ProfilingParameters: Optional[Mapping[str, str]] = None
    DisableProfiler: Optional[bool] = None

class ProfilerRuleConfigurationTypeDef(BaseValidatorModel):
    RuleConfigurationName: str
    RuleEvaluatorImage: str
    LocalPath: Optional[str] = None
    S3OutputPath: Optional[str] = None
    InstanceType: Optional[ProcessingInstanceTypeType] = None
    VolumeSizeInGB: Optional[int] = None
    RuleParameters: Optional[Mapping[str, str]] = None

class PropertyNameQueryTypeDef(BaseValidatorModel):
    PropertyNameHint: str

class ProvisioningParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class USDTypeDef(BaseValidatorModel):
    Dollars: Optional[int] = None
    Cents: Optional[int] = None
    TenthFractionsOfACent: Optional[int] = None

class PutModelPackageGroupPolicyInputRequestTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str
    ResourcePolicy: str

class VertexTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    LineageType: Optional[LineageTypeType] = None

class RStudioServerProAppSettingsTypeDef(BaseValidatorModel):
    AccessStatus: Optional[RStudioServerProAccessStatusType] = None
    UserGroup: Optional[RStudioServerProUserGroupType] = None

class RecommendationJobCompiledOutputConfigTypeDef(BaseValidatorModel):
    S3OutputUri: Optional[str] = None

class RecommendationJobPayloadConfigOutputTypeDef(BaseValidatorModel):
    SamplePayloadUrl: Optional[str] = None
    SupportedContentTypes: Optional[List[str]] = None

class RecommendationJobPayloadConfigTypeDef(BaseValidatorModel):
    SamplePayloadUrl: Optional[str] = None
    SupportedContentTypes: Optional[Sequence[str]] = None

class RecommendationJobResourceLimitTypeDef(BaseValidatorModel):
    MaxNumberOfTests: Optional[int] = None
    MaxParallelOfTests: Optional[int] = None

class RecommendationJobVpcConfigOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class RecommendationJobVpcConfigTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class RemoteDebugConfigForUpdateTypeDef(BaseValidatorModel):
    EnableRemoteDebug: Optional[bool] = None

class RenderableTaskTypeDef(BaseValidatorModel):
    Input: str

class RenderingErrorTypeDef(BaseValidatorModel):
    Code: str
    Message: str

class ResourceConfigForUpdateTypeDef(BaseValidatorModel):
    KeepAlivePeriodInSeconds: int

class VisibilityConditionsTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class SelectedStepTypeDef(BaseValidatorModel):
    StepName: str

class SendPipelineExecutionStepFailureRequestRequestTypeDef(BaseValidatorModel):
    CallbackToken: str
    FailureReason: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class ShadowModelVariantConfigTypeDef(BaseValidatorModel):
    ShadowModelVariantName: str
    SamplingPercentage: int

class SharingSettingsTypeDef(BaseValidatorModel):
    NotebookOutputOption: Optional[NotebookOutputOptionType] = None
    S3OutputPath: Optional[str] = None
    S3KmsKeyId: Optional[str] = None

class SourceIpConfigExtraOutputTypeDef(BaseValidatorModel):
    Cidrs: List[str]

class SourceIpConfigOutputTypeDef(BaseValidatorModel):
    Cidrs: List[str]

class SpaceSharingSettingsSummaryTypeDef(BaseValidatorModel):
    SharingType: Optional[SharingTypeType] = None

class StairsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None
    NumberOfSteps: Optional[int] = None
    UsersPerStep: Optional[int] = None

class StartEdgeDeploymentStageRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str

class StartInferenceExperimentRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartMlflowTrackingServerRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str

class StartMonitoringScheduleRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str

class StartNotebookInstanceInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceName: str

class StopAutoMLJobRequestRequestTypeDef(BaseValidatorModel):
    AutoMLJobName: str

class StopCompilationJobRequestRequestTypeDef(BaseValidatorModel):
    CompilationJobName: str

class StopEdgeDeploymentStageRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str

class StopEdgePackagingJobRequestRequestTypeDef(BaseValidatorModel):
    EdgePackagingJobName: str

class StopHyperParameterTuningJobRequestRequestTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: str

class StopInferenceRecommendationsJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: str

class StopLabelingJobRequestRequestTypeDef(BaseValidatorModel):
    LabelingJobName: str

class StopMlflowTrackingServerRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str

class StopMonitoringScheduleRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str

class StopNotebookInstanceInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceName: str

class StopOptimizationJobRequestRequestTypeDef(BaseValidatorModel):
    OptimizationJobName: str

class StopPipelineExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ClientRequestToken: str

class StopProcessingJobRequestRequestTypeDef(BaseValidatorModel):
    ProcessingJobName: str

class StopTrainingJobRequestRequestTypeDef(BaseValidatorModel):
    TrainingJobName: str

class StopTransformJobRequestRequestTypeDef(BaseValidatorModel):
    TransformJobName: str

class StudioWebPortalSettingsOutputTypeDef(BaseValidatorModel):
    HiddenMlTools: Optional[List[MlToolsType]] = None
    HiddenAppTypes: Optional[List[AppTypeType]] = None

class StudioWebPortalSettingsTypeDef(BaseValidatorModel):
    HiddenMlTools: Optional[Sequence[MlToolsType]] = None
    HiddenAppTypes: Optional[Sequence[AppTypeType]] = None

class ThroughputConfigUpdateTypeDef(BaseValidatorModel):
    ThroughputMode: Optional[ThroughputModeType] = None
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None

class TimeSeriesConfigOutputTypeDef(BaseValidatorModel):
    TargetAttributeName: str
    TimestampAttributeName: str
    ItemIdentifierAttributeName: str
    GroupingAttributeNames: Optional[List[str]] = None

class TimeSeriesConfigTypeDef(BaseValidatorModel):
    TargetAttributeName: str
    TimestampAttributeName: str
    ItemIdentifierAttributeName: str
    GroupingAttributeNames: Optional[Sequence[str]] = None

class TimeSeriesTransformationsOutputTypeDef(BaseValidatorModel):
    Filling: Optional[Dict[str, Dict[FillingTypeType, str]]] = None
    Aggregation: Optional[Dict[str, AggregationTransformationValueType]] = None

class TimeSeriesTransformationsTypeDef(BaseValidatorModel):
    Filling: Optional[Mapping[str, Mapping[FillingTypeType, str]]] = None
    Aggregation: Optional[Mapping[str, AggregationTransformationValueType]] = None

class TrainingRepositoryAuthConfigTypeDef(BaseValidatorModel):
    TrainingRepositoryCredentialsProviderArn: str

class TransformS3DataSourceTypeDef(BaseValidatorModel):
    S3DataType: S3DataTypeType
    S3Uri: str

class UpdateActionRequestRequestTypeDef(BaseValidatorModel):
    ActionName: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Mapping[str, str]] = None
    PropertiesToRemove: Optional[Sequence[str]] = None

class UpdateArtifactRequestRequestTypeDef(BaseValidatorModel):
    ArtifactArn: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    PropertiesToRemove: Optional[Sequence[str]] = None

class UpdateClusterSoftwareRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str

class UpdateContextRequestRequestTypeDef(BaseValidatorModel):
    ContextName: str
    Description: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    PropertiesToRemove: Optional[Sequence[str]] = None

class VariantPropertyTypeDef(BaseValidatorModel):
    VariantPropertyType: VariantPropertyTypeType

class UpdateExperimentRequestRequestTypeDef(BaseValidatorModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None

class UpdateHubRequestRequestTypeDef(BaseValidatorModel):
    HubName: str
    HubDescription: Optional[str] = None
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[Sequence[str]] = None

class UpdateImageRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str
    DeleteProperties: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    RoleArn: Optional[str] = None

class UpdateImageVersionRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateMlflowTrackingServerRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str
    ArtifactStoreUri: Optional[str] = None
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None

class UpdateModelCardRequestRequestTypeDef(BaseValidatorModel):
    ModelCardName: str
    Content: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None

class UpdateMonitoringAlertRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringAlertName: str
    DatapointsToAlert: int
    EvaluationPeriod: int

class UpdateTrialRequestRequestTypeDef(BaseValidatorModel):
    TrialName: str
    DisplayName: Optional[str] = None

class WorkforceVpcConfigResponseTypeDef(BaseValidatorModel):
    VpcId: str
    SecurityGroupIds: List[str]
    Subnets: List[str]
    VpcEndpointId: Optional[str] = None

class ActionSummaryTypeDef(BaseValidatorModel):
    ActionArn: Optional[str] = None
    ActionName: Optional[str] = None
    Source: Optional[ActionSourceTypeDef] = None
    ActionType: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class AddAssociationResponseTypeDef(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTrialComponentResponseTypeDef(BaseValidatorModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateActionResponseTypeDef(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAlgorithmOutputTypeDef(BaseValidatorModel):
    AlgorithmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppImageConfigResponseTypeDef(BaseValidatorModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppResponseTypeDef(BaseValidatorModel):
    AppArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateArtifactResponseTypeDef(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoMLJobResponseTypeDef(BaseValidatorModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoMLJobV2ResponseTypeDef(BaseValidatorModel):
    AutoMLJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeRepositoryOutputTypeDef(BaseValidatorModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCompilationJobResponseTypeDef(BaseValidatorModel):
    CompilationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContextResponseTypeDef(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataQualityJobDefinitionResponseTypeDef(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseValidatorModel):
    DomainArn: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEdgeDeploymentPlanResponseTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointConfigOutputTypeDef(BaseValidatorModel):
    EndpointConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointOutputTypeDef(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentResponseTypeDef(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFeatureGroupResponseTypeDef(BaseValidatorModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowDefinitionResponseTypeDef(BaseValidatorModel):
    FlowDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHubContentReferenceResponseTypeDef(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHubResponseTypeDef(BaseValidatorModel):
    HubArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHumanTaskUiResponseTypeDef(BaseValidatorModel):
    HumanTaskUiArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHyperParameterTuningJobResponseTypeDef(BaseValidatorModel):
    HyperParameterTuningJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageResponseTypeDef(BaseValidatorModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageVersionResponseTypeDef(BaseValidatorModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceComponentOutputTypeDef(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceExperimentResponseTypeDef(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceRecommendationsJobResponseTypeDef(BaseValidatorModel):
    JobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelingJobResponseTypeDef(BaseValidatorModel):
    LabelingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMlflowTrackingServerResponseTypeDef(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelBiasJobDefinitionResponseTypeDef(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelCardExportJobResponseTypeDef(BaseValidatorModel):
    ModelCardExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelCardResponseTypeDef(BaseValidatorModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelExplainabilityJobDefinitionResponseTypeDef(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelOutputTypeDef(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelPackageGroupOutputTypeDef(BaseValidatorModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelPackageOutputTypeDef(BaseValidatorModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelQualityJobDefinitionResponseTypeDef(BaseValidatorModel):
    JobDefinitionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitoringScheduleResponseTypeDef(BaseValidatorModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookInstanceLifecycleConfigOutputTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookInstanceOutputTypeDef(BaseValidatorModel):
    NotebookInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOptimizationJobResponseTypeDef(BaseValidatorModel):
    OptimizationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineResponseTypeDef(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedDomainUrlResponseTypeDef(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedMlflowTrackingServerUrlResponseTypeDef(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedNotebookInstanceUrlOutputTypeDef(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProcessingJobResponseTypeDef(BaseValidatorModel):
    ProcessingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectOutputTypeDef(BaseValidatorModel):
    ProjectArn: str
    ProjectId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSpaceResponseTypeDef(BaseValidatorModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioLifecycleConfigResponseTypeDef(BaseValidatorModel):
    StudioLifecycleConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingJobResponseTypeDef(BaseValidatorModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransformJobResponseTypeDef(BaseValidatorModel):
    TransformJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrialComponentResponseTypeDef(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrialResponseTypeDef(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserProfileResponseTypeDef(BaseValidatorModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkforceResponseTypeDef(BaseValidatorModel):
    WorkforceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkteamResponseTypeDef(BaseValidatorModel):
    WorkteamArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteActionResponseTypeDef(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteArtifactResponseTypeDef(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAssociationResponseTypeDef(BaseValidatorModel):
    SourceArn: str
    DestinationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteContextResponseTypeDef(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExperimentResponseTypeDef(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInferenceExperimentResponseTypeDef(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMlflowTrackingServerResponseTypeDef(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePipelineResponseTypeDef(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrialComponentResponseTypeDef(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrialResponseTypeDef(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkteamResponseTypeDef(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageResponseTypeDef(BaseValidatorModel):
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

class DescribeImageVersionResponseTypeDef(BaseValidatorModel):
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

class DescribePipelineDefinitionForExecutionResponseTypeDef(BaseValidatorModel):
    PipelineDefinition: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStudioLifecycleConfigResponseTypeDef(BaseValidatorModel):
    StudioLifecycleConfigArn: str
    StudioLifecycleConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTrialComponentResponseTypeDef(BaseValidatorModel):
    TrialComponentArn: str
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetLineageGroupPolicyResponseTypeDef(BaseValidatorModel):
    LineageGroupArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelPackageGroupPolicyOutputTypeDef(BaseValidatorModel):
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSagemakerServicecatalogPortfolioStatusOutputTypeDef(BaseValidatorModel):
    Status: SagemakerServicecatalogStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ImportHubContentResponseTypeDef(BaseValidatorModel):
    HubArn: str
    HubContentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseValidatorModel):
    SageMakerImageVersionAliases: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutModelPackageGroupPolicyOutputTypeDef(BaseValidatorModel):
    ModelPackageGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RetryPipelineExecutionResponseTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendPipelineExecutionStepFailureResponseTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendPipelineExecutionStepSuccessResponseTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartInferenceExperimentResponseTypeDef(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMlflowTrackingServerResponseTypeDef(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineExecutionResponseTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopInferenceExperimentResponseTypeDef(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopMlflowTrackingServerResponseTypeDef(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipelineExecutionResponseTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionResponseTypeDef(BaseValidatorModel):
    ActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppImageConfigResponseTypeDef(BaseValidatorModel):
    AppImageConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateArtifactResponseTypeDef(BaseValidatorModel):
    ArtifactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterSoftwareResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeRepositoryOutputTypeDef(BaseValidatorModel):
    CodeRepositoryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContextResponseTypeDef(BaseValidatorModel):
    ContextArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainResponseTypeDef(BaseValidatorModel):
    DomainArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointOutputTypeDef(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointWeightsAndCapacitiesOutputTypeDef(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperimentResponseTypeDef(BaseValidatorModel):
    ExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFeatureGroupResponseTypeDef(BaseValidatorModel):
    FeatureGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHubResponseTypeDef(BaseValidatorModel):
    HubArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageResponseTypeDef(BaseValidatorModel):
    ImageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageVersionResponseTypeDef(BaseValidatorModel):
    ImageVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInferenceComponentOutputTypeDef(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInferenceComponentRuntimeConfigOutputTypeDef(BaseValidatorModel):
    InferenceComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInferenceExperimentResponseTypeDef(BaseValidatorModel):
    InferenceExperimentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMlflowTrackingServerResponseTypeDef(BaseValidatorModel):
    TrackingServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelCardResponseTypeDef(BaseValidatorModel):
    ModelCardArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelPackageOutputTypeDef(BaseValidatorModel):
    ModelPackageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitoringAlertResponseTypeDef(BaseValidatorModel):
    MonitoringScheduleArn: str
    MonitoringAlertName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitoringScheduleResponseTypeDef(BaseValidatorModel):
    MonitoringScheduleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineExecutionResponseTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineResponseTypeDef(BaseValidatorModel):
    PipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectOutputTypeDef(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSpaceResponseTypeDef(BaseValidatorModel):
    SpaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrainingJobResponseTypeDef(BaseValidatorModel):
    TrainingJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrialComponentResponseTypeDef(BaseValidatorModel):
    TrialComponentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrialResponseTypeDef(BaseValidatorModel):
    TrialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserProfileResponseTypeDef(BaseValidatorModel):
    UserProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AddTagsOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentRequestRequestTypeDef(BaseValidatorModel):
    ExperimentName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateHubContentReferenceRequestRequestTypeDef(BaseValidatorModel):
    HubName: str
    SageMakerPublicHubContentArn: str
    HubContentName: Optional[str] = None
    MinVersion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateImageRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str
    RoleArn: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMlflowTrackingServerRequestRequestTypeDef(BaseValidatorModel):
    TrackingServerName: str
    ArtifactStoreUri: str
    RoleArn: str
    TrackingServerSize: Optional[TrackingServerSizeType] = None
    MlflowVersion: Optional[str] = None
    AutomaticModelRegistration: Optional[bool] = None
    WeeklyMaintenanceWindowStart: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelPackageGroupInputRequestTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateStudioLifecycleConfigRequestRequestTypeDef(BaseValidatorModel):
    StudioLifecycleConfigName: str
    StudioLifecycleConfigContent: str
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportHubContentRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoRollbackConfigOutputTypeDef(BaseValidatorModel):
    Alarms: Optional[List[AlarmTypeDef]] = None

class AutoRollbackConfigTypeDef(BaseValidatorModel):
    Alarms: Optional[Sequence[AlarmTypeDef]] = None

class HyperParameterAlgorithmSpecificationExtraOutputTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None

class HyperParameterAlgorithmSpecificationOutputTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None

class HyperParameterAlgorithmSpecificationTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None

class AlgorithmStatusDetailsTypeDef(BaseValidatorModel):
    ValidationStatuses: Optional[List[AlgorithmStatusItemTypeDef]] = None
    ImageScanStatuses: Optional[List[AlgorithmStatusItemTypeDef]] = None

class ListAlgorithmsOutputTypeDef(BaseValidatorModel):
    AlgorithmSummaryList: List[AlgorithmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AppDetailsTypeDef(BaseValidatorModel):
    DomainId: Optional[str] = None
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    AppType: Optional[AppTypeType] = None
    AppName: Optional[str] = None
    Status: Optional[AppStatusType] = None
    CreationTime: Optional[datetime] = None
    ResourceSpec: Optional[ResourceSpecTypeDef] = None

class CreateAppRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    AppType: AppTypeType
    AppName: str
    UserProfileName: Optional[str] = None
    SpaceName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ResourceSpec: Optional[ResourceSpecTypeDef] = None

class DescribeAppResponseTypeDef(BaseValidatorModel):
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

class RStudioServerProDomainSettingsForUpdateTypeDef(BaseValidatorModel):
    DomainExecutionRoleArn: str
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    RStudioConnectUrl: Optional[str] = None
    RStudioPackageManagerUrl: Optional[str] = None

class RStudioServerProDomainSettingsTypeDef(BaseValidatorModel):
    DomainExecutionRoleArn: str
    RStudioConnectUrl: Optional[str] = None
    RStudioPackageManagerUrl: Optional[str] = None
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None

class SpaceCodeEditorAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None

class TensorBoardAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None

class ArtifactSourceExtraOutputTypeDef(BaseValidatorModel):
    SourceUri: str
    SourceTypes: Optional[List[ArtifactSourceTypeTypeDef]] = None

class ArtifactSourceOutputTypeDef(BaseValidatorModel):
    SourceUri: str
    SourceTypes: Optional[List[ArtifactSourceTypeTypeDef]] = None

class ArtifactSourceTypeDef(BaseValidatorModel):
    SourceUri: str
    SourceTypes: Optional[Sequence[ArtifactSourceTypeTypeDef]] = None

class AsyncInferenceOutputConfigOutputTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    S3OutputPath: Optional[str] = None
    NotificationConfig: Optional[AsyncInferenceNotificationConfigOutputTypeDef] = None
    S3FailurePath: Optional[str] = None

class AsyncInferenceOutputConfigTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    S3OutputPath: Optional[str] = None
    NotificationConfig: Optional[AsyncInferenceNotificationConfigTypeDef] = None
    S3FailurePath: Optional[str] = None

class AutoMLCandidateGenerationConfigOutputTypeDef(BaseValidatorModel):
    FeatureSpecificationS3Uri: Optional[str] = None
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfigOutputTypeDef]] = None

class CandidateGenerationConfigOutputTypeDef(BaseValidatorModel):
    AlgorithmsConfig: Optional[List[AutoMLAlgorithmConfigOutputTypeDef]] = None

class AutoMLCandidateGenerationConfigTypeDef(BaseValidatorModel):
    FeatureSpecificationS3Uri: Optional[str] = None
    AlgorithmsConfig: Optional[Sequence[AutoMLAlgorithmConfigTypeDef]] = None

class CandidateGenerationConfigTypeDef(BaseValidatorModel):
    AlgorithmsConfig: Optional[Sequence[AutoMLAlgorithmConfigTypeDef]] = None

class AutoMLDataSourceTypeDef(BaseValidatorModel):
    S3DataSource: AutoMLS3DataSourceTypeDef

class ImageClassificationJobConfigTypeDef(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None

class TextClassificationJobConfigTypeDef(BaseValidatorModel):
    ContentColumn: str
    TargetLabelColumn: str
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None

class ResolvedAttributesTypeDef(BaseValidatorModel):
    AutoMLJobObjective: Optional[AutoMLJobObjectiveTypeDef] = None
    ProblemType: Optional[ProblemTypeType] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None

class AutoMLJobSummaryTypeDef(BaseValidatorModel):
    AutoMLJobName: str
    AutoMLJobArn: str
    AutoMLJobStatus: AutoMLJobStatusType
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatusType
    CreationTime: datetime
    LastModifiedTime: datetime
    EndTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PartialFailureReasons: Optional[List[AutoMLPartialFailureReasonTypeDef]] = None

class AutoMLProblemTypeResolvedAttributesTypeDef(BaseValidatorModel):
    TabularResolvedAttributes: Optional[TabularResolvedAttributesTypeDef] = None
    TextGenerationResolvedAttributes: Optional[TextGenerationResolvedAttributesTypeDef] = None

class AutoMLSecurityConfigOutputTypeDef(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class LabelingJobResourceConfigOutputTypeDef(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class MonitoringNetworkConfigOutputTypeDef(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class NetworkConfigOutputTypeDef(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None

class AutoMLSecurityConfigTypeDef(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class LabelingJobResourceConfigTypeDef(BaseValidatorModel):
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class MonitoringNetworkConfigTypeDef(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class NetworkConfigTypeDef(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class BiasTypeDef(BaseValidatorModel):
    Report: Optional[MetricsSourceTypeDef] = None
    PreTrainingReport: Optional[MetricsSourceTypeDef] = None
    PostTrainingReport: Optional[MetricsSourceTypeDef] = None

class DriftCheckModelDataQualityTypeDef(BaseValidatorModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class DriftCheckModelQualityTypeDef(BaseValidatorModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class ExplainabilityTypeDef(BaseValidatorModel):
    Report: Optional[MetricsSourceTypeDef] = None

class ModelDataQualityTypeDef(BaseValidatorModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class ModelQualityTypeDef(BaseValidatorModel):
    Statistics: Optional[MetricsSourceTypeDef] = None
    Constraints: Optional[MetricsSourceTypeDef] = None

class CallbackStepMetadataTypeDef(BaseValidatorModel):
    CallbackToken: Optional[str] = None
    SqsQueueUrl: Optional[str] = None
    OutputParameters: Optional[List[OutputParameterTypeDef]] = None

class LambdaStepMetadataTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    OutputParameters: Optional[List[OutputParameterTypeDef]] = None

class SendPipelineExecutionStepSuccessRequestRequestTypeDef(BaseValidatorModel):
    CallbackToken: str
    OutputParameters: Optional[Sequence[OutputParameterTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class CandidatePropertiesTypeDef(BaseValidatorModel):
    CandidateArtifactLocations: Optional[CandidateArtifactLocationsTypeDef] = None
    CandidateMetrics: Optional[List[MetricDatumTypeDef]] = None

class CanvasAppSettingsOutputTypeDef(BaseValidatorModel):
    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettingsTypeDef] = None
    ModelRegisterSettings: Optional[ModelRegisterSettingsTypeDef] = None
    WorkspaceSettings: Optional[WorkspaceSettingsTypeDef] = None
    IdentityProviderOAuthSettings: Optional[List[IdentityProviderOAuthSettingTypeDef]] = None
    DirectDeploySettings: Optional[DirectDeploySettingsTypeDef] = None
    KendraSettings: Optional[KendraSettingsTypeDef] = None
    GenerativeAiSettings: Optional[GenerativeAiSettingsTypeDef] = None

class CanvasAppSettingsTypeDef(BaseValidatorModel):
    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettingsTypeDef] = None
    ModelRegisterSettings: Optional[ModelRegisterSettingsTypeDef] = None
    WorkspaceSettings: Optional[WorkspaceSettingsTypeDef] = None
    IdentityProviderOAuthSettings: Optional[Sequence[IdentityProviderOAuthSettingTypeDef]] = None
    DirectDeploySettings: Optional[DirectDeploySettingsTypeDef] = None
    KendraSettings: Optional[KendraSettingsTypeDef] = None
    GenerativeAiSettings: Optional[GenerativeAiSettingsTypeDef] = None

class RollingUpdatePolicyTypeDef(BaseValidatorModel):
    MaximumBatchSize: CapacitySizeTypeDef
    WaitIntervalInSeconds: int
    MaximumExecutionTimeoutInSeconds: Optional[int] = None
    RollbackMaximumBatchSize: Optional[CapacitySizeTypeDef] = None

class TrafficRoutingConfigTypeDef(BaseValidatorModel):
    Type: TrafficRoutingConfigTypeType
    WaitIntervalInSeconds: int
    CanarySize: Optional[CapacitySizeTypeDef] = None
    LinearStepSize: Optional[CapacitySizeTypeDef] = None

class InferenceExperimentDataStorageConfigOutputTypeDef(BaseValidatorModel):
    Destination: str
    KmsKey: Optional[str] = None
    ContentType: Optional[CaptureContentTypeHeaderOutputTypeDef] = None

class InferenceExperimentDataStorageConfigTypeDef(BaseValidatorModel):
    Destination: str
    KmsKey: Optional[str] = None
    ContentType: Optional[CaptureContentTypeHeaderTypeDef] = None

class DataCaptureConfigOutputTypeDef(BaseValidatorModel):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: List[CaptureOptionTypeDef]
    EnableCapture: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeaderOutputTypeDef] = None

class DataCaptureConfigTypeDef(BaseValidatorModel):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: Sequence[CaptureOptionTypeDef]
    EnableCapture: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeaderTypeDef] = None

class EnvironmentParameterRangesOutputTypeDef(BaseValidatorModel):
    CategoricalParameterRanges: Optional[List[CategoricalParameterOutputTypeDef]] = None

class EnvironmentParameterRangesTypeDef(BaseValidatorModel):
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterTypeDef]] = None

class ClarifyShapConfigTypeDef(BaseValidatorModel):
    ShapBaselineConfig: ClarifyShapBaselineConfigTypeDef
    NumberOfSamples: Optional[int] = None
    UseLogit: Optional[bool] = None
    Seed: Optional[int] = None
    TextConfig: Optional[ClarifyTextConfigTypeDef] = None

class ClusterInstanceStorageConfigTypeDef(BaseValidatorModel):
    EbsVolumeConfig: Optional[ClusterEbsVolumeConfigTypeDef] = None

class ClusterNodeSummaryTypeDef(BaseValidatorModel):
    InstanceGroupName: str
    InstanceId: str
    InstanceType: ClusterInstanceTypeType
    LaunchTime: datetime
    InstanceStatus: ClusterInstanceStatusDetailsTypeDef

class ListClustersResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ClusterSummaries: List[ClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CodeEditorAppImageConfigExtraOutputTypeDef(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigExtraOutputTypeDef] = None

class JupyterLabAppImageConfigExtraOutputTypeDef(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigExtraOutputTypeDef] = None

class CodeEditorAppImageConfigOutputTypeDef(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigOutputTypeDef] = None

class JupyterLabAppImageConfigOutputTypeDef(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigOutputTypeDef] = None

class CodeEditorAppImageConfigTypeDef(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigTypeDef] = None

class JupyterLabAppImageConfigTypeDef(BaseValidatorModel):
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None
    ContainerConfig: Optional[ContainerConfigTypeDef] = None

class CodeEditorAppSettingsOutputTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[List[str]] = None

class CodeEditorAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None

class KernelGatewayAppSettingsOutputTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[List[str]] = None

class KernelGatewayAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None

class RSessionAppSettingsOutputTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None

class RSessionAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None

class CodeRepositorySummaryTypeDef(BaseValidatorModel):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: Optional[GitConfigTypeDef] = None

class CreateCodeRepositoryInputRequestTypeDef(BaseValidatorModel):
    CodeRepositoryName: str
    GitConfig: GitConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeCodeRepositoryOutputTypeDef(BaseValidatorModel):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: GitConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JupyterLabAppSettingsOutputTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[List[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepositoryTypeDef]] = None

class JupyterLabAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CustomImages: Optional[Sequence[CustomImageTypeDef]] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None
    CodeRepositories: Optional[Sequence[CodeRepositoryTypeDef]] = None

class JupyterServerAppSettingsOutputTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    LifecycleConfigArns: Optional[List[str]] = None
    CodeRepositories: Optional[List[CodeRepositoryTypeDef]] = None

class JupyterServerAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    LifecycleConfigArns: Optional[Sequence[str]] = None
    CodeRepositories: Optional[Sequence[CodeRepositoryTypeDef]] = None

class SpaceJupyterLabAppSettingsOutputTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CodeRepositories: Optional[List[CodeRepositoryTypeDef]] = None

class SpaceJupyterLabAppSettingsTypeDef(BaseValidatorModel):
    DefaultResourceSpec: Optional[ResourceSpecTypeDef] = None
    CodeRepositories: Optional[Sequence[CodeRepositoryTypeDef]] = None

class CollectionConfigTypeDef(BaseValidatorModel):
    VectorConfig: Optional[VectorConfigTypeDef] = None

class DebugHookConfigExtraOutputTypeDef(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Dict[str, str]] = None
    CollectionConfigurations: Optional[List[CollectionConfigurationExtraOutputTypeDef]] = None

class DebugHookConfigOutputTypeDef(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Dict[str, str]] = None
    CollectionConfigurations: Optional[List[CollectionConfigurationOutputTypeDef]] = None

class DebugHookConfigTypeDef(BaseValidatorModel):
    S3OutputPath: str
    LocalPath: Optional[str] = None
    HookParameters: Optional[Mapping[str, str]] = None
    CollectionConfigurations: Optional[Sequence[CollectionConfigurationTypeDef]] = None

class ListCompilationJobsResponseTypeDef(BaseValidatorModel):
    CompilationJobSummaries: List[CompilationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContextSummaryTypeDef(BaseValidatorModel):
    ContextArn: Optional[str] = None
    ContextName: Optional[str] = None
    Source: Optional[ContextSourceTypeDef] = None
    ContextType: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class CreateContextRequestRequestTypeDef(BaseValidatorModel):
    ContextName: str
    Source: ContextSourceTypeDef
    ContextType: str
    Description: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TuningJobCompletionCriteriaTypeDef(BaseValidatorModel):
    TargetObjectiveMetricValue: Optional[float] = None
    BestObjectiveNotImproving: Optional[BestObjectiveNotImprovingTypeDef] = None
    ConvergenceDetected: Optional[ConvergenceDetectedTypeDef] = None

class CreateActionRequestRequestTypeDef(BaseValidatorModel):
    ActionName: str
    Source: ActionSourceTypeDef
    ActionType: str
    Description: Optional[str] = None
    Status: Optional[ActionStatusType] = None
    Properties: Optional[Mapping[str, str]] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTrialRequestRequestTypeDef(BaseValidatorModel):
    TrialName: str
    ExperimentName: str
    DisplayName: Optional[str] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDeviceFleetRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfigTypeDef
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EnableIotRoleAlias: Optional[bool] = None

class CreateEdgePackagingJobRequestRequestTypeDef(BaseValidatorModel):
    EdgePackagingJobName: str
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: EdgeOutputConfigTypeDef
    ResourceKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeDeviceFleetResponseTypeDef(BaseValidatorModel):
    DeviceFleetName: str
    DeviceFleetArn: str
    OutputConfig: EdgeOutputConfigTypeDef
    Description: str
    CreationTime: datetime
    LastModifiedTime: datetime
    RoleArn: str
    IotRoleAlias: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceFleetRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfigTypeDef
    RoleArn: Optional[str] = None
    Description: Optional[str] = None
    EnableIotRoleAlias: Optional[bool] = None

class CreateHubRequestRequestTypeDef(BaseValidatorModel):
    HubName: str
    HubDescription: str
    HubDisplayName: Optional[str] = None
    HubSearchKeywords: Optional[Sequence[str]] = None
    S3StorageConfig: Optional[HubS3StorageConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeHubResponseTypeDef(BaseValidatorModel):
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

class CreateHumanTaskUiRequestRequestTypeDef(BaseValidatorModel):
    HumanTaskUiName: str
    UiTemplate: UiTemplateTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateInferenceComponentRuntimeConfigInputRequestTypeDef(BaseValidatorModel):
    InferenceComponentName: str
    DesiredRuntimeConfig: InferenceComponentRuntimeConfigTypeDef

class CreateModelCardExportJobRequestRequestTypeDef(BaseValidatorModel):
    ModelCardName: str
    ModelCardExportJobName: str
    OutputConfig: ModelCardExportOutputConfigTypeDef
    ModelCardVersion: Optional[int] = None

class CreateModelCardRequestRequestTypeDef(BaseValidatorModel):
    ModelCardName: str
    Content: str
    ModelCardStatus: ModelCardStatusType
    SecurityConfig: Optional[ModelCardSecurityConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateNotebookInstanceInputRequestTypeDef(BaseValidatorModel):
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

class DescribeNotebookInstanceOutputTypeDef(BaseValidatorModel):
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

class UpdateNotebookInstanceInputRequestTypeDef(BaseValidatorModel):
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

class CreateNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None
    OnStart: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None

class DescribeNotebookInstanceLifecycleConfigOutputTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigArn: str
    NotebookInstanceLifecycleConfigName: str
    OnCreate: List[NotebookInstanceLifecycleHookTypeDef]
    OnStart: List[NotebookInstanceLifecycleHookTypeDef]
    LastModifiedTime: datetime
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigName: str
    OnCreate: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None
    OnStart: Optional[Sequence[NotebookInstanceLifecycleHookTypeDef]] = None

class RetryPipelineExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    ClientRequestToken: str
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class UpdatePipelineExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    PipelineExecutionDescription: Optional[str] = None
    PipelineExecutionDisplayName: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class CreatePipelineRequestRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str
    RoleArn: str
    PipelineDisplayName: Optional[str] = None
    PipelineDefinition: Optional[str] = None
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3LocationTypeDef] = None
    PipelineDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class UpdatePipelineRequestRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    PipelineDisplayName: Optional[str] = None
    PipelineDefinition: Optional[str] = None
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3LocationTypeDef] = None
    PipelineDescription: Optional[str] = None
    RoleArn: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class InferenceExperimentScheduleTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class ListActionsRequestRequestTypeDef(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAlgorithmsInputRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListAppImageConfigsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[AppImageConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None

class ListArtifactsRequestRequestTypeDef(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAssociationsRequestRequestTypeDef(BaseValidatorModel):
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

class ListAutoMLJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListClusterNodesRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    InstanceGroupNameContains: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListClustersRequestRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListCodeRepositoriesInputRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[CodeRepositorySortByType] = None
    SortOrder: Optional[CodeRepositorySortOrderType] = None

class ListCompilationJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListContextsRequestRequestTypeDef(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataQualityJobDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListDeviceFleetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ListDeviceFleetsSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LatestHeartbeatAfter: Optional[TimestampTypeDef] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None

class ListEdgeDeploymentPlansRequestRequestTypeDef(BaseValidatorModel):
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

class ListEdgePackagingJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListEndpointConfigsInputRequestTypeDef(BaseValidatorModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListEndpointsInputRequestTypeDef(BaseValidatorModel):
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

class ListExperimentsRequestRequestTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFeatureGroupsRequestRequestTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    FeatureGroupStatusEquals: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValueType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[FeatureGroupSortOrderType] = None
    SortBy: Optional[FeatureGroupSortByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFlowDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHubContentVersionsRequestRequestTypeDef(BaseValidatorModel):
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

class ListHubContentsRequestRequestTypeDef(BaseValidatorModel):
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

class ListHubsRequestRequestTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[HubSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHumanTaskUisRequestRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHyperParameterTuningJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListImageVersionsRequestRequestTypeDef(BaseValidatorModel):
    ImageName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ImageVersionSortByType] = None
    SortOrder: Optional[ImageVersionSortOrderType] = None

class ListImagesRequestRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ImageSortByType] = None
    SortOrder: Optional[ImageSortOrderType] = None

class ListInferenceComponentsInputRequestTypeDef(BaseValidatorModel):
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

class ListInferenceExperimentsRequestRequestTypeDef(BaseValidatorModel):
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

class ListInferenceRecommendationsJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListLabelingJobsForWorkteamRequestRequestTypeDef(BaseValidatorModel):
    WorkteamArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None

class ListLabelingJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListLineageGroupsRequestRequestTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMlflowTrackingServersRequestRequestTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListModelBiasJobDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListModelCardExportJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListModelCardVersionsRequestRequestTypeDef(BaseValidatorModel):
    ModelCardName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[Literal["Version"]] = None
    SortOrder: Optional[ModelCardSortOrderType] = None

class ListModelCardsRequestRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None

class ListModelExplainabilityJobDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListModelPackageGroupsInputRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None

class ListModelPackagesInputRequestTypeDef(BaseValidatorModel):
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

class ListModelQualityJobDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListModelsInputRequestTypeDef(BaseValidatorModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class ListMonitoringAlertHistoryRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: Optional[str] = None
    MonitoringAlertName: Optional[str] = None
    SortBy: Optional[MonitoringAlertHistorySortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[MonitoringAlertStatusType] = None

class ListMonitoringExecutionsRequestRequestTypeDef(BaseValidatorModel):
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

class ListMonitoringSchedulesRequestRequestTypeDef(BaseValidatorModel):
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

class ListNotebookInstanceLifecycleConfigsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKeyType] = None
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None

class ListNotebookInstancesInputRequestTypeDef(BaseValidatorModel):
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

class ListOptimizationJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListPipelineExecutionsRequestRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPipelinesRequestRequestTypeDef(BaseValidatorModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProcessingJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListProjectsInputRequestTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ProjectSortByType] = None
    SortOrder: Optional[ProjectSortOrderType] = None

class ListResourceCatalogsRequestRequestTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListStudioLifecycleConfigsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTrainingJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTransformJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTrialComponentsRequestRequestTypeDef(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    SourceArn: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialComponentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTrialsRequestRequestTypeDef(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialComponentName: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialsByType] = None
    SortOrder: Optional[SortOrderType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class QueryFiltersTypeDef(BaseValidatorModel):
    Types: Optional[Sequence[str]] = None
    LineageTypes: Optional[Sequence[LineageTypeType]] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    ModifiedBefore: Optional[TimestampTypeDef] = None
    ModifiedAfter: Optional[TimestampTypeDef] = None
    Properties: Optional[Mapping[str, str]] = None

class CreateTrialComponentRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateTrialComponentRequestRequestTypeDef(BaseValidatorModel):
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

class CreateWorkforceRequestRequestTypeDef(BaseValidatorModel):
    WorkforceName: str
    CognitoConfig: Optional[CognitoConfigTypeDef] = None
    OidcConfig: Optional[OidcConfigTypeDef] = None
    SourceIpConfig: Optional[SourceIpConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequestTypeDef] = None

class UpdateWorkforceRequestRequestTypeDef(BaseValidatorModel):
    WorkforceName: str
    SourceIpConfig: Optional[SourceIpConfigTypeDef] = None
    OidcConfig: Optional[OidcConfigTypeDef] = None
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequestTypeDef] = None

class CustomFileSystemConfigTypeDef(BaseValidatorModel):
    EFSFileSystemConfig: Optional[EFSFileSystemConfigTypeDef] = None

class CustomFileSystemTypeDef(BaseValidatorModel):
    EFSFileSystem: Optional[EFSFileSystemTypeDef] = None

class ModelBiasBaselineConfigTypeDef(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None

class ModelExplainabilityBaselineConfigTypeDef(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None

class ModelQualityBaselineConfigTypeDef(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None

class DataQualityBaselineConfigTypeDef(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None
    StatisticsResource: Optional[MonitoringStatisticsResourceTypeDef] = None

class MonitoringBaselineConfigTypeDef(BaseValidatorModel):
    BaseliningJobName: Optional[str] = None
    ConstraintsResource: Optional[MonitoringConstraintsResourceTypeDef] = None
    StatisticsResource: Optional[MonitoringStatisticsResourceTypeDef] = None

class DataSourceExtraOutputTypeDef(BaseValidatorModel):
    S3DataSource: Optional[S3DataSourceExtraOutputTypeDef] = None
    FileSystemDataSource: Optional[FileSystemDataSourceTypeDef] = None

class DataSourceOutputTypeDef(BaseValidatorModel):
    S3DataSource: Optional[S3DataSourceOutputTypeDef] = None
    FileSystemDataSource: Optional[FileSystemDataSourceTypeDef] = None

class DataSourceTypeDef(BaseValidatorModel):
    S3DataSource: Optional[S3DataSourceTypeDef] = None
    FileSystemDataSource: Optional[FileSystemDataSourceTypeDef] = None

class DatasetDefinitionTypeDef(BaseValidatorModel):
    AthenaDatasetDefinition: Optional[AthenaDatasetDefinitionTypeDef] = None
    RedshiftDatasetDefinition: Optional[RedshiftDatasetDefinitionTypeDef] = None
    LocalPath: Optional[str] = None
    DataDistributionType: Optional[DataDistributionTypeType] = None
    InputMode: Optional[InputModeType] = None

class DefaultSpaceStorageSettingsTypeDef(BaseValidatorModel):
    DefaultEbsStorageSettings: Optional[DefaultEbsStorageSettingsTypeDef] = None

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    RetentionPolicy: Optional[RetentionPolicyTypeDef] = None

class InferenceComponentContainerSpecificationSummaryTypeDef(BaseValidatorModel):
    DeployedImage: Optional[DeployedImageTypeDef] = None
    ArtifactUrl: Optional[str] = None
    Environment: Optional[Dict[str, str]] = None

class DeploymentRecommendationTypeDef(BaseValidatorModel):
    RecommendationStatus: RecommendationStatusType
    RealTimeInferenceRecommendations: Optional[       List[RealTimeInferenceRecommendationTypeDef]     ] = None

class DeploymentStageStatusSummaryTypeDef(BaseValidatorModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigOutputTypeDef
    DeploymentConfig: EdgeDeploymentConfigTypeDef
    DeploymentStatus: EdgeDeploymentStatusTypeDef

class DeploymentStageTypeDef(BaseValidatorModel):
    StageName: str
    DeviceSelectionConfig: DeviceSelectionConfigTypeDef
    DeploymentConfig: Optional[EdgeDeploymentConfigTypeDef] = None

class DescribeDeviceResponseTypeDef(BaseValidatorModel):
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

class DescribeEdgePackagingJobResponseTypeDef(BaseValidatorModel):
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

class DescribeEndpointInputEndpointDeletedWaitTypeDef(BaseValidatorModel):
    EndpointName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndpointInputEndpointInServiceWaitTypeDef(BaseValidatorModel):
    EndpointName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageRequestImageCreatedWaitTypeDef(BaseValidatorModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageRequestImageDeletedWaitTypeDef(BaseValidatorModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageRequestImageUpdatedWaitTypeDef(BaseValidatorModel):
    ImageName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageVersionRequestImageVersionCreatedWaitTypeDef(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImageVersionRequestImageVersionDeletedWaitTypeDef(BaseValidatorModel):
    ImageName: str
    Version: Optional[int] = None
    Alias: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef(BaseValidatorModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef(BaseValidatorModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef(BaseValidatorModel):
    NotebookInstanceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef(BaseValidatorModel):
    ProcessingJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef(BaseValidatorModel):
    TrainingJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef(BaseValidatorModel):
    TransformJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ExperimentSummaryTypeDef(BaseValidatorModel):
    ExperimentArn: Optional[str] = None
    ExperimentName: Optional[str] = None
    DisplayName: Optional[str] = None
    ExperimentSource: Optional[ExperimentSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class FeatureGroupSummaryTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    FeatureGroupArn: str
    CreationTime: datetime
    FeatureGroupStatus: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatus: Optional[OfflineStoreStatusTypeDef] = None

class DescribeFeatureMetadataResponseTypeDef(BaseValidatorModel):
    FeatureGroupArn: str
    FeatureGroupName: str
    FeatureName: str
    FeatureType: FeatureTypeType
    CreationTime: datetime
    LastModifiedTime: datetime
    Description: str
    Parameters: List[FeatureParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FeatureMetadataTypeDef(BaseValidatorModel):
    FeatureGroupArn: Optional[str] = None
    FeatureGroupName: Optional[str] = None
    FeatureName: Optional[str] = None
    FeatureType: Optional[FeatureTypeType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Description: Optional[str] = None
    Parameters: Optional[List[FeatureParameterTypeDef]] = None

class UpdateFeatureMetadataRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    FeatureName: str
    Description: Optional[str] = None
    ParameterAdditions: Optional[Sequence[FeatureParameterTypeDef]] = None
    ParameterRemovals: Optional[Sequence[str]] = None

class DescribeHubContentResponseTypeDef(BaseValidatorModel):
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

class DescribeHumanTaskUiResponseTypeDef(BaseValidatorModel):
    HumanTaskUiArn: str
    HumanTaskUiName: str
    HumanTaskUiStatus: HumanTaskUiStatusType
    CreationTime: datetime
    UiTemplate: UiTemplateInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InferenceExperimentSummaryTypeDef(BaseValidatorModel):
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

class DescribeModelCardExportJobResponseTypeDef(BaseValidatorModel):
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

class ListMonitoringExecutionsResponseTypeDef(BaseValidatorModel):
    MonitoringExecutionSummaries: List[MonitoringExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSubscribedWorkteamResponseTypeDef(BaseValidatorModel):
    SubscribedWorkteam: SubscribedWorkteamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribedWorkteamsResponseTypeDef(BaseValidatorModel):
    SubscribedWorkteams: List[SubscribedWorkteamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TrainingJobSummaryTypeDef(BaseValidatorModel):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime
    TrainingJobStatus: TrainingJobStatusType
    TrainingEndTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    WarmPoolStatus: Optional[WarmPoolStatusTypeDef] = None

class TrialSummaryTypeDef(BaseValidatorModel):
    TrialArn: Optional[str] = None
    TrialName: Optional[str] = None
    DisplayName: Optional[str] = None
    TrialSource: Optional[TrialSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class DesiredWeightAndCapacityTypeDef(BaseValidatorModel):
    VariantName: str
    DesiredWeight: Optional[float] = None
    DesiredInstanceCount: Optional[int] = None
    ServerlessUpdateConfig: Optional[ProductionVariantServerlessUpdateConfigTypeDef] = None

class ListStageDevicesResponseTypeDef(BaseValidatorModel):
    DeviceDeploymentSummaries: List[DeviceDeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDeviceFleetsResponseTypeDef(BaseValidatorModel):
    DeviceFleetSummaries: List[DeviceFleetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeviceSummaryTypeDef(BaseValidatorModel):
    DeviceName: str
    DeviceArn: str
    Description: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    IotThingName: Optional[str] = None
    RegistrationTime: Optional[datetime] = None
    LatestHeartbeat: Optional[datetime] = None
    Models: Optional[List[EdgeModelSummaryTypeDef]] = None
    AgentVersion: Optional[str] = None

class RegisterDevicesRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str
    Devices: Sequence[DeviceTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDevicesRequestRequestTypeDef(BaseValidatorModel):
    DeviceFleetName: str
    Devices: Sequence[DeviceTypeDef]

class ListDomainsResponseTypeDef(BaseValidatorModel):
    Domains: List[DomainDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DriftCheckBiasTypeDef(BaseValidatorModel):
    ConfigFile: Optional[FileSourceTypeDef] = None
    PreTrainingConstraints: Optional[MetricsSourceTypeDef] = None
    PostTrainingConstraints: Optional[MetricsSourceTypeDef] = None

class DriftCheckExplainabilityTypeDef(BaseValidatorModel):
    Constraints: Optional[MetricsSourceTypeDef] = None
    ConfigFile: Optional[FileSourceTypeDef] = None

class SpaceStorageSettingsTypeDef(BaseValidatorModel):
    EbsStorageSettings: Optional[EbsStorageSettingsTypeDef] = None

class ListEdgeDeploymentPlansResponseTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanSummaries: List[EdgeDeploymentPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDeviceFleetReportResponseTypeDef(BaseValidatorModel):
    DeviceFleetArn: str
    DeviceFleetName: str
    OutputConfig: EdgeOutputConfigTypeDef
    Description: str
    ReportGenerated: datetime
    DeviceStats: DeviceStatsTypeDef
    AgentVersions: List[AgentVersionTypeDef]
    ModelStats: List[EdgeModelStatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEdgePackagingJobsResponseTypeDef(BaseValidatorModel):
    EdgePackagingJobSummaries: List[EdgePackagingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEndpointConfigsOutputTypeDef(BaseValidatorModel):
    EndpointConfigs: List[EndpointConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EndpointOutputConfigurationTypeDef(BaseValidatorModel):
    EndpointName: str
    VariantName: str
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    InitialInstanceCount: Optional[int] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None

class EndpointPerformanceTypeDef(BaseValidatorModel):
    Metrics: InferenceMetricsTypeDef
    EndpointInfo: EndpointInfoTypeDef

class ListEndpointsOutputTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModelConfigurationTypeDef(BaseValidatorModel):
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameters: Optional[List[EnvironmentParameterTypeDef]] = None
    CompilationJobName: Optional[str] = None

class NestedFiltersTypeDef(BaseValidatorModel):
    NestedPropertyName: str
    Filters: Sequence[FilterTypeDef]

class HyperParameterTrainingJobSummaryTypeDef(BaseValidatorModel):
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

class ListFlowDefinitionsResponseTypeDef(BaseValidatorModel):
    FlowDefinitionSummaries: List[FlowDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetScalingConfigurationRecommendationRequestRequestTypeDef(BaseValidatorModel):
    InferenceRecommendationsJobName: str
    RecommendationId: Optional[str] = None
    EndpointName: Optional[str] = None
    TargetCpuUtilizationPerCore: Optional[int] = None
    ScalingPolicyObjective: Optional[ScalingPolicyObjectiveTypeDef] = None

class GetSearchSuggestionsResponseTypeDef(BaseValidatorModel):
    PropertyNameSuggestions: List[PropertyNameSuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeRepositoryInputRequestTypeDef(BaseValidatorModel):
    CodeRepositoryName: str
    GitConfig: Optional[GitConfigForUpdateTypeDef] = None

class ListHubContentVersionsResponseTypeDef(BaseValidatorModel):
    HubContentSummaries: List[HubContentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHubContentsResponseTypeDef(BaseValidatorModel):
    HubContentSummaries: List[HubContentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHubsResponseTypeDef(BaseValidatorModel):
    HubSummaries: List[HubInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class HumanLoopActivationConfigTypeDef(BaseValidatorModel):
    HumanLoopActivationConditionsConfig: HumanLoopActivationConditionsConfigTypeDef

class ListHumanTaskUisResponseTypeDef(BaseValidatorModel):
    HumanTaskUiSummaries: List[HumanTaskUiSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetworkConfigExtraOutputTypeDef(BaseValidatorModel):
    EnableInterContainerTrafficEncryption: Optional[bool] = None
    EnableNetworkIsolation: Optional[bool] = None
    VpcConfig: Optional[VpcConfigExtraOutputTypeDef] = None

class HyperParameterTuningResourceConfigExtraOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal["Prioritized"]] = None
    InstanceConfigs: Optional[List[HyperParameterTuningInstanceConfigTypeDef]] = None

class HyperParameterTuningResourceConfigOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal["Prioritized"]] = None
    InstanceConfigs: Optional[List[HyperParameterTuningInstanceConfigTypeDef]] = None

class HyperParameterTuningResourceConfigTypeDef(BaseValidatorModel):
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeSizeInGB: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    AllocationStrategy: Optional[Literal["Prioritized"]] = None
    InstanceConfigs: Optional[Sequence[HyperParameterTuningInstanceConfigTypeDef]] = None

class HyperParameterTuningJobSummaryTypeDef(BaseValidatorModel):
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

class HyperParameterTuningJobStrategyConfigTypeDef(BaseValidatorModel):
    HyperbandStrategyConfig: Optional[HyperbandStrategyConfigTypeDef] = None

class HyperParameterTuningJobWarmStartConfigExtraOutputTypeDef(BaseValidatorModel):
    ParentHyperParameterTuningJobs: List[ParentHyperParameterTuningJobTypeDef]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType

class HyperParameterTuningJobWarmStartConfigOutputTypeDef(BaseValidatorModel):
    ParentHyperParameterTuningJobs: List[ParentHyperParameterTuningJobTypeDef]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType

class HyperParameterTuningJobWarmStartConfigTypeDef(BaseValidatorModel):
    ParentHyperParameterTuningJobs: Sequence[ParentHyperParameterTuningJobTypeDef]
    WarmStartType: HyperParameterTuningJobWarmStartTypeType

class UserContextTypeDef(BaseValidatorModel):
    UserProfileArn: Optional[str] = None
    UserProfileName: Optional[str] = None
    DomainId: Optional[str] = None
    IamIdentity: Optional[IamIdentityTypeDef] = None

class S3PresignTypeDef(BaseValidatorModel):
    IamPolicyConstraints: Optional[IamPolicyConstraintsTypeDef] = None

class ImageConfigTypeDef(BaseValidatorModel):
    RepositoryAccessMode: RepositoryAccessModeType
    RepositoryAuthConfig: Optional[RepositoryAuthConfigTypeDef] = None

class ListImagesResponseTypeDef(BaseValidatorModel):
    Images: List[ImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListImageVersionsResponseTypeDef(BaseValidatorModel):
    ImageVersions: List[ImageVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InferenceComponentSpecificationTypeDef(BaseValidatorModel):
    ComputeResourceRequirements: InferenceComponentComputeResourceRequirementsTypeDef
    ModelName: Optional[str] = None
    Container: Optional[InferenceComponentContainerSpecificationTypeDef] = None
    StartupParameters: Optional[InferenceComponentStartupParametersTypeDef] = None

class ListInferenceComponentsOutputTypeDef(BaseValidatorModel):
    InferenceComponents: List[InferenceComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListInferenceRecommendationsJobsResponseTypeDef(BaseValidatorModel):
    InferenceRecommendationsJobs: List[InferenceRecommendationsJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResourceConfigExtraOutputTypeDef(BaseValidatorModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroupTypeDef]] = None

class ResourceConfigOutputTypeDef(BaseValidatorModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[List[InstanceGroupTypeDef]] = None

class ResourceConfigTypeDef(BaseValidatorModel):
    VolumeSizeInGB: int
    InstanceType: Optional[TrainingInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    VolumeKmsKeyId: Optional[str] = None
    KeepAlivePeriodInSeconds: Optional[int] = None
    InstanceGroups: Optional[Sequence[InstanceGroupTypeDef]] = None

class ParameterRangeOutputTypeDef(BaseValidatorModel):
    IntegerParameterRangeSpecification: Optional[       IntegerParameterRangeSpecificationTypeDef     ] = None
    ContinuousParameterRangeSpecification: Optional[       ContinuousParameterRangeSpecificationTypeDef     ] = None
    CategoricalParameterRangeSpecification: Optional[       CategoricalParameterRangeSpecificationOutputTypeDef     ] = None

class ParameterRangeTypeDef(BaseValidatorModel):
    IntegerParameterRangeSpecification: Optional[       IntegerParameterRangeSpecificationTypeDef     ] = None
    ContinuousParameterRangeSpecification: Optional[       ContinuousParameterRangeSpecificationTypeDef     ] = None
    CategoricalParameterRangeSpecification: Optional[       CategoricalParameterRangeSpecificationTypeDef     ] = None

class ParameterRangesExtraOutputTypeDef(BaseValidatorModel):
    IntegerParameterRanges: Optional[List[IntegerParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRangeTypeDef]] = None
    CategoricalParameterRanges: Optional[       List[CategoricalParameterRangeExtraOutputTypeDef]     ] = None
    AutoParameters: Optional[List[AutoParameterTypeDef]] = None

class ParameterRangesOutputTypeDef(BaseValidatorModel):
    IntegerParameterRanges: Optional[List[IntegerParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRangeTypeDef]] = None
    CategoricalParameterRanges: Optional[List[CategoricalParameterRangeOutputTypeDef]] = None
    AutoParameters: Optional[List[AutoParameterTypeDef]] = None

class ParameterRangesTypeDef(BaseValidatorModel):
    IntegerParameterRanges: Optional[Sequence[IntegerParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[Sequence[ContinuousParameterRangeTypeDef]] = None
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterRangeTypeDef]] = None
    AutoParameters: Optional[Sequence[AutoParameterTypeDef]] = None

class KernelGatewayImageConfigExtraOutputTypeDef(BaseValidatorModel):
    KernelSpecs: List[KernelSpecTypeDef]
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None

class KernelGatewayImageConfigOutputTypeDef(BaseValidatorModel):
    KernelSpecs: List[KernelSpecTypeDef]
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None

class KernelGatewayImageConfigTypeDef(BaseValidatorModel):
    KernelSpecs: Sequence[KernelSpecTypeDef]
    FileSystemConfig: Optional[FileSystemConfigTypeDef] = None

class LabelingJobForWorkteamSummaryTypeDef(BaseValidatorModel):
    JobReferenceCode: str
    WorkRequesterAccountId: str
    CreationTime: datetime
    LabelingJobName: Optional[str] = None
    LabelCounters: Optional[LabelCountersForWorkteamTypeDef] = None
    NumberOfHumanWorkersPerDataObject: Optional[int] = None

class LabelingJobDataSourceTypeDef(BaseValidatorModel):
    S3DataSource: Optional[LabelingJobS3DataSourceTypeDef] = None
    SnsDataSource: Optional[LabelingJobSnsDataSourceTypeDef] = None

class ListLineageGroupsResponseTypeDef(BaseValidatorModel):
    LineageGroupSummaries: List[LineageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListActionsRequestListActionsPaginateTypeDef(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ActionType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortActionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAlgorithmsInputListAlgorithmsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[AlgorithmSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAliasesRequestListAliasesPaginateTypeDef(BaseValidatorModel):
    ImageName: str
    Alias: Optional[str] = None
    Version: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppImageConfigsRequestListAppImageConfigsPaginateTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[AppImageConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppsRequestListAppsPaginateTypeDef(BaseValidatorModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameEquals: Optional[str] = None
    SpaceNameEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArtifactsRequestListArtifactsPaginateTypeDef(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ArtifactType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociationsRequestListAssociationsPaginateTypeDef(BaseValidatorModel):
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

class ListAutoMLJobsRequestListAutoMLJobsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[AutoMLJobStatusType] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[AutoMLSortByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef(BaseValidatorModel):
    AutoMLJobName: str
    StatusEquals: Optional[CandidateStatusType] = None
    CandidateNameEquals: Optional[str] = None
    SortOrder: Optional[AutoMLSortOrderType] = None
    SortBy: Optional[CandidateSortByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterNodesRequestListClusterNodesPaginateTypeDef(BaseValidatorModel):
    ClusterName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    InstanceGroupNameContains: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ClusterSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCodeRepositoriesInputListCodeRepositoriesPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[CodeRepositorySortByType] = None
    SortOrder: Optional[CodeRepositorySortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCompilationJobsRequestListCompilationJobsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[CompilationJobStatusType] = None
    SortBy: Optional[ListCompilationJobsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContextsRequestListContextsPaginateTypeDef(BaseValidatorModel):
    SourceUri: Optional[str] = None
    ContextType: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortContextsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataQualityJobDefinitionsRequestListDataQualityJobDefinitionsPaginateTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceFleetsRequestListDeviceFleetsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ListDeviceFleetsSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicesRequestListDevicesPaginateTypeDef(BaseValidatorModel):
    LatestHeartbeatAfter: Optional[TimestampTypeDef] = None
    ModelName: Optional[str] = None
    DeviceFleetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEdgeDeploymentPlansRequestListEdgeDeploymentPlansPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    DeviceFleetNameContains: Optional[str] = None
    SortBy: Optional[ListEdgeDeploymentPlansSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEdgePackagingJobsRequestListEdgePackagingJobsPaginateTypeDef(BaseValidatorModel):
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

class ListEndpointConfigsInputListEndpointConfigsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[EndpointConfigSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointsInputListEndpointsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[EndpointSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[EndpointStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExperimentsRequestListExperimentsPaginateTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortExperimentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFeatureGroupsRequestListFeatureGroupsPaginateTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    FeatureGroupStatusEquals: Optional[FeatureGroupStatusType] = None
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValueType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[FeatureGroupSortOrderType] = None
    SortBy: Optional[FeatureGroupSortByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowDefinitionsRequestListFlowDefinitionsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHumanTaskUisRequestListHumanTaskUisPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHyperParameterTuningJobsRequestListHyperParameterTuningJobsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[HyperParameterTuningJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[HyperParameterTuningJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImageVersionsRequestListImageVersionsPaginateTypeDef(BaseValidatorModel):
    ImageName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[ImageVersionSortByType] = None
    SortOrder: Optional[ImageVersionSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImagesRequestListImagesPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ImageSortByType] = None
    SortOrder: Optional[ImageSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInferenceComponentsInputListInferenceComponentsPaginateTypeDef(BaseValidatorModel):
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

class ListInferenceExperimentsRequestListInferenceExperimentsPaginateTypeDef(BaseValidatorModel):
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

class ListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef(BaseValidatorModel):
    JobName: str
    Status: Optional[RecommendationJobStatusType] = None
    StepType: Optional[Literal["BENCHMARK"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInferenceRecommendationsJobsRequestListInferenceRecommendationsJobsPaginateTypeDef(BaseValidatorModel):
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

class ListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef(BaseValidatorModel):
    WorkteamArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    JobReferenceCodeContains: Optional[str] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLabelingJobsRequestListLabelingJobsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[LabelingJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLineageGroupsRequestListLineageGroupsPaginateTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortLineageGroupsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMlflowTrackingServersRequestListMlflowTrackingServersPaginateTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    TrackingServerStatus: Optional[TrackingServerStatusType] = None
    MlflowVersion: Optional[str] = None
    SortBy: Optional[SortTrackingServerByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelBiasJobDefinitionsRequestListModelBiasJobDefinitionsPaginateTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef(BaseValidatorModel):
    ModelCardName: str
    ModelCardVersion: Optional[int] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    ModelCardExportJobNameContains: Optional[str] = None
    StatusEquals: Optional[ModelCardExportJobStatusType] = None
    SortBy: Optional[ModelCardExportJobSortByType] = None
    SortOrder: Optional[ModelCardExportJobSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef(BaseValidatorModel):
    ModelCardName: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SortBy: Optional[Literal["Version"]] = None
    SortOrder: Optional[ModelCardSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCardsRequestListModelCardsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    ModelCardStatus: Optional[ModelCardStatusType] = None
    SortBy: Optional[ModelCardSortByType] = None
    SortOrder: Optional[ModelCardSortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelExplainabilityJobDefinitionsRequestListModelExplainabilityJobDefinitionsPaginateTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelPackageGroupsInputListModelPackageGroupsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    SortBy: Optional[ModelPackageGroupSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelPackagesInputListModelPackagesPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ModelPackageGroupName: Optional[str] = None
    ModelPackageType: Optional[ModelPackageTypeType] = None
    SortBy: Optional[ModelPackageSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelQualityJobDefinitionsRequestListModelQualityJobDefinitionsPaginateTypeDef(BaseValidatorModel):
    EndpointName: Optional[str] = None
    SortBy: Optional[MonitoringJobDefinitionSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelsInputListModelsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[ModelSortKeyType] = None
    SortOrder: Optional[OrderKeyType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringAlertHistoryRequestListMonitoringAlertHistoryPaginateTypeDef(BaseValidatorModel):
    MonitoringScheduleName: Optional[str] = None
    MonitoringAlertName: Optional[str] = None
    SortBy: Optional[MonitoringAlertHistorySortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    StatusEquals: Optional[MonitoringAlertStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoringExecutionsRequestListMonitoringExecutionsPaginateTypeDef(BaseValidatorModel):
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

class ListMonitoringSchedulesRequestListMonitoringSchedulesPaginateTypeDef(BaseValidatorModel):
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

class ListNotebookInstanceLifecycleConfigsInputListNotebookInstanceLifecycleConfigsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKeyType] = None
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrderType] = None
    NameContains: Optional[str] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotebookInstancesInputListNotebookInstancesPaginateTypeDef(BaseValidatorModel):
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

class ListOptimizationJobsRequestListOptimizationJobsPaginateTypeDef(BaseValidatorModel):
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

class ListPipelineExecutionStepsRequestListPipelineExecutionStepsPaginateTypeDef(BaseValidatorModel):
    PipelineExecutionArn: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef(BaseValidatorModel):
    PipelineName: str
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelineExecutionsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef(BaseValidatorModel):
    PipelineExecutionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesRequestListPipelinesPaginateTypeDef(BaseValidatorModel):
    PipelineNamePrefix: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortPipelinesByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProcessingJobsRequestListProcessingJobsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[ProcessingJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceCatalogsRequestListResourceCatalogsPaginateTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[ResourceCatalogSortOrderType] = None
    SortBy: Optional[Literal["CreationTime"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpacesRequestListSpacesPaginateTypeDef(BaseValidatorModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[SpaceSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    SpaceNameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStageDevicesRequestListStageDevicesPaginateTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    StageName: str
    ExcludeDevicesDeployedInOtherStage: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioLifecycleConfigsRequestListStudioLifecycleConfigsPaginateTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    AppTypeEquals: Optional[StudioLifecycleConfigAppTypeType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    ModifiedTimeBefore: Optional[TimestampTypeDef] = None
    ModifiedTimeAfter: Optional[TimestampTypeDef] = None
    SortBy: Optional[StudioLifecycleConfigSortKeyType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscribedWorkteamsRequestListSubscribedWorkteamsPaginateTypeDef(BaseValidatorModel):
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsInputListTagsPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: str
    StatusEquals: Optional[TrainingJobStatusType] = None
    SortBy: Optional[TrainingJobSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingJobsRequestListTrainingJobsPaginateTypeDef(BaseValidatorModel):
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

class ListTransformJobsRequestListTransformJobsPaginateTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    LastModifiedTimeAfter: Optional[TimestampTypeDef] = None
    LastModifiedTimeBefore: Optional[TimestampTypeDef] = None
    NameContains: Optional[str] = None
    StatusEquals: Optional[TransformJobStatusType] = None
    SortBy: Optional[SortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrialComponentsRequestListTrialComponentsPaginateTypeDef(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialName: Optional[str] = None
    SourceArn: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialComponentsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrialsRequestListTrialsPaginateTypeDef(BaseValidatorModel):
    ExperimentName: Optional[str] = None
    TrialComponentName: Optional[str] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    SortBy: Optional[SortTrialsByType] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserProfilesRequestListUserProfilesPaginateTypeDef(BaseValidatorModel):
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[UserProfileSortKeyType] = None
    DomainIdEquals: Optional[str] = None
    UserProfileNameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkforcesRequestListWorkforcesPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[ListWorkforcesSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkteamsRequestListWorkteamsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[ListWorkteamsSortByOptionsType] = None
    SortOrder: Optional[SortOrderType] = None
    NameContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataQualityJobDefinitionsResponseTypeDef(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelBiasJobDefinitionsResponseTypeDef(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelExplainabilityJobDefinitionsResponseTypeDef(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelQualityJobDefinitionsResponseTypeDef(BaseValidatorModel):
    JobDefinitionSummaries: List[MonitoringJobDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMlflowTrackingServersResponseTypeDef(BaseValidatorModel):
    TrackingServerSummaries: List[TrackingServerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelCardExportJobsResponseTypeDef(BaseValidatorModel):
    ModelCardExportJobSummaries: List[ModelCardExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelCardVersionsResponseTypeDef(BaseValidatorModel):
    ModelCardVersionSummaryList: List[ModelCardVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelCardsResponseTypeDef(BaseValidatorModel):
    ModelCardSummaries: List[ModelCardSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelMetadataResponseTypeDef(BaseValidatorModel):
    ModelMetadataSummaries: List[ModelMetadataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelPackageGroupsOutputTypeDef(BaseValidatorModel):
    ModelPackageGroupSummaryList: List[ModelPackageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelPackagesOutputTypeDef(BaseValidatorModel):
    ModelPackageSummaryList: List[ModelPackageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListModelsOutputTypeDef(BaseValidatorModel):
    Models: List[ModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMonitoringAlertHistoryResponseTypeDef(BaseValidatorModel):
    MonitoringAlertHistory: List[MonitoringAlertHistorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMonitoringSchedulesResponseTypeDef(BaseValidatorModel):
    MonitoringScheduleSummaries: List[MonitoringScheduleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNotebookInstanceLifecycleConfigsOutputTypeDef(BaseValidatorModel):
    NotebookInstanceLifecycleConfigs: List[NotebookInstanceLifecycleConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNotebookInstancesOutputTypeDef(BaseValidatorModel):
    NotebookInstances: List[NotebookInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOptimizationJobsResponseTypeDef(BaseValidatorModel):
    OptimizationJobSummaries: List[OptimizationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPipelineExecutionsResponseTypeDef(BaseValidatorModel):
    PipelineExecutionSummaries: List[PipelineExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPipelineParametersForExecutionResponseTypeDef(BaseValidatorModel):
    PipelineParameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPipelinesResponseTypeDef(BaseValidatorModel):
    PipelineSummaries: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProcessingJobsResponseTypeDef(BaseValidatorModel):
    ProcessingJobSummaries: List[ProcessingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProjectsOutputTypeDef(BaseValidatorModel):
    ProjectSummaryList: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceCatalogsResponseTypeDef(BaseValidatorModel):
    ResourceCatalogs: List[ResourceCatalogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStudioLifecycleConfigsResponseTypeDef(BaseValidatorModel):
    StudioLifecycleConfigs: List[StudioLifecycleConfigDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTransformJobsResponseTypeDef(BaseValidatorModel):
    TransformJobSummaries: List[TransformJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUserProfilesResponseTypeDef(BaseValidatorModel):
    UserProfiles: List[UserProfileDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MemberDefinitionExtraOutputTypeDef(BaseValidatorModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinitionTypeDef] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionExtraOutputTypeDef] = None

class MemberDefinitionOutputTypeDef(BaseValidatorModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinitionTypeDef] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionOutputTypeDef] = None

class MemberDefinitionTypeDef(BaseValidatorModel):
    CognitoMemberDefinition: Optional[CognitoMemberDefinitionTypeDef] = None
    OidcMemberDefinition: Optional[OidcMemberDefinitionTypeDef] = None

class MetricSpecificationTypeDef(BaseValidatorModel):
    Predefined: Optional[PredefinedMetricSpecificationTypeDef] = None
    Customized: Optional[CustomizedMetricSpecificationTypeDef] = None

class S3ModelDataSourceTypeDef(BaseValidatorModel):
    S3Uri: str
    S3DataType: S3ModelDataTypeType
    CompressionType: ModelCompressionTypeType
    ModelAccessConfig: Optional[ModelAccessConfigTypeDef] = None
    HubAccessConfig: Optional[InferenceHubAccessConfigTypeDef] = None

class TextGenerationJobConfigOutputTypeDef(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    BaseValidatorModelName: Optional[str] = None
    TextGenerationHyperParameters: Optional[Dict[str, str]] = None
    ModelAccessConfig: Optional[ModelAccessConfigTypeDef] = None

class TextGenerationJobConfigTypeDef(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    BaseValidatorModelName: Optional[str] = None
    TextGenerationHyperParameters: Optional[Mapping[str, str]] = None
    ModelAccessConfig: Optional[ModelAccessConfigTypeDef] = None

class MonitoringAlertActionsTypeDef(BaseValidatorModel):
    ModelDashboardIndicator: Optional[ModelDashboardIndicatorActionTypeDef] = None

class ModelInfrastructureConfigTypeDef(BaseValidatorModel):
    InfrastructureType: Literal["RealTimeInference"]
    RealTimeInferenceConfig: RealTimeInferenceConfigTypeDef

class RecommendationJobStoppingConditionsOutputTypeDef(BaseValidatorModel):
    MaxInvocations: Optional[int] = None
    ModelLatencyThresholds: Optional[List[ModelLatencyThresholdTypeDef]] = None
    FlatInvocations: Optional[FlatInvocationsType] = None

class RecommendationJobStoppingConditionsTypeDef(BaseValidatorModel):
    MaxInvocations: Optional[int] = None
    ModelLatencyThresholds: Optional[Sequence[ModelLatencyThresholdTypeDef]] = None
    FlatInvocations: Optional[FlatInvocationsType] = None

class ModelMetadataSearchExpressionTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ModelMetadataFilterTypeDef]] = None

class ModelPackageStatusDetailsTypeDef(BaseValidatorModel):
    ValidationStatuses: List[ModelPackageStatusItemTypeDef]
    ImageScanStatuses: Optional[List[ModelPackageStatusItemTypeDef]] = None

class OptimizationConfigOutputTypeDef(BaseValidatorModel):
    ModelQuantizationConfig: Optional[ModelQuantizationConfigOutputTypeDef] = None
    ModelCompilationConfig: Optional[ModelCompilationConfigOutputTypeDef] = None

class OptimizationConfigTypeDef(BaseValidatorModel):
    ModelQuantizationConfig: Optional[ModelQuantizationConfigTypeDef] = None
    ModelCompilationConfig: Optional[ModelCompilationConfigTypeDef] = None

class MonitoringResourcesTypeDef(BaseValidatorModel):
    ClusterConfig: MonitoringClusterConfigTypeDef

class MonitoringDatasetFormatExtraOutputTypeDef(BaseValidatorModel):
    Csv: Optional[MonitoringCsvDatasetFormatTypeDef] = None
    Json: Optional[MonitoringJsonDatasetFormatTypeDef] = None
    Parquet: Optional[Dict[str, Any]] = None

class MonitoringDatasetFormatOutputTypeDef(BaseValidatorModel):
    Csv: Optional[MonitoringCsvDatasetFormatTypeDef] = None
    Json: Optional[MonitoringJsonDatasetFormatTypeDef] = None
    Parquet: Optional[Dict[str, Any]] = None

class MonitoringDatasetFormatTypeDef(BaseValidatorModel):
    Csv: Optional[MonitoringCsvDatasetFormatTypeDef] = None
    Json: Optional[MonitoringJsonDatasetFormatTypeDef] = None
    Parquet: Optional[Mapping[str, Any]] = None

class MonitoringOutputTypeDef(BaseValidatorModel):
    S3Output: MonitoringS3OutputTypeDef

class OfflineStoreConfigTypeDef(BaseValidatorModel):
    S3StorageConfig: S3StorageConfigTypeDef
    DisableGlueTableCreation: Optional[bool] = None
    DataCatalogConfig: Optional[DataCatalogConfigTypeDef] = None
    TableFormat: Optional[TableFormatType] = None

class OnlineStoreConfigTypeDef(BaseValidatorModel):
    SecurityConfig: Optional[OnlineStoreSecurityConfigTypeDef] = None
    EnableOnlineStore: Optional[bool] = None
    TtlDuration: Optional[TtlDurationTypeDef] = None
    StorageType: Optional[StorageTypeType] = None

class OnlineStoreConfigUpdateTypeDef(BaseValidatorModel):
    TtlDuration: Optional[TtlDurationTypeDef] = None

class OptimizationJobModelSourceS3TypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None
    ModelAccessConfig: Optional[OptimizationModelAccessConfigTypeDef] = None

class OutputConfigTypeDef(BaseValidatorModel):
    S3OutputLocation: str
    TargetDevice: Optional[TargetDeviceType] = None
    TargetPlatform: Optional[TargetPlatformTypeDef] = None
    CompilerOptions: Optional[str] = None
    KmsKeyId: Optional[str] = None

class PendingProductionVariantSummaryTypeDef(BaseValidatorModel):
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

class ProductionVariantSummaryTypeDef(BaseValidatorModel):
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

class ProcessingResourcesTypeDef(BaseValidatorModel):
    ClusterConfig: ProcessingClusterConfigTypeDef

class ProcessingOutputTypeDef(BaseValidatorModel):
    OutputName: str
    S3Output: Optional[ProcessingS3OutputTypeDef] = None
    FeatureStoreOutput: Optional[ProcessingFeatureStoreOutputTypeDef] = None
    AppManaged: Optional[bool] = None

class ProductionVariantTypeDef(BaseValidatorModel):
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

class SuggestionQueryTypeDef(BaseValidatorModel):
    PropertyNameQuery: Optional[PropertyNameQueryTypeDef] = None

class ServiceCatalogProvisioningDetailsExtraOutputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameterTypeDef]] = None

class ServiceCatalogProvisioningDetailsOutputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameterTypeDef]] = None

class ServiceCatalogProvisioningDetailsTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[Sequence[ProvisioningParameterTypeDef]] = None

class ServiceCatalogProvisioningUpdateDetailsTypeDef(BaseValidatorModel):
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningParameters: Optional[Sequence[ProvisioningParameterTypeDef]] = None

class PublicWorkforceTaskPriceTypeDef(BaseValidatorModel):
    AmountInUsd: Optional[USDTypeDef] = None

class QueryLineageResponseTypeDef(BaseValidatorModel):
    Vertices: List[VertexTypeDef]
    Edges: List[EdgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RecommendationJobOutputConfigTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    CompiledOutputConfig: Optional[RecommendationJobCompiledOutputConfigTypeDef] = None

class RecommendationJobContainerConfigOutputTypeDef(BaseValidatorModel):
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

class RecommendationJobContainerConfigTypeDef(BaseValidatorModel):
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

class RenderUiTemplateRequestRequestTypeDef(BaseValidatorModel):
    Task: RenderableTaskTypeDef
    RoleArn: str
    UiTemplate: Optional[UiTemplateTypeDef] = None
    HumanTaskUiArn: Optional[str] = None

class RenderUiTemplateResponseTypeDef(BaseValidatorModel):
    RenderedContent: str
    Errors: List[RenderingErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRequestRequestTypeDef(BaseValidatorModel):
    Resource: ResourceTypeType
    SearchExpression: Optional["SearchExpressionTypeDef"] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[Sequence[VisibilityConditionsTypeDef]] = None

class SelectiveExecutionConfigExtraOutputTypeDef(BaseValidatorModel):
    SelectedSteps: List[SelectedStepTypeDef]
    SourcePipelineExecutionArn: Optional[str] = None

class SelectiveExecutionConfigOutputTypeDef(BaseValidatorModel):
    SelectedSteps: List[SelectedStepTypeDef]
    SourcePipelineExecutionArn: Optional[str] = None

class SelectiveExecutionConfigTypeDef(BaseValidatorModel):
    SelectedSteps: Sequence[SelectedStepTypeDef]
    SourcePipelineExecutionArn: Optional[str] = None

class ShadowModeConfigOutputTypeDef(BaseValidatorModel):
    SourceModelVariantName: str
    ShadowModelVariants: List[ShadowModelVariantConfigTypeDef]

class ShadowModeConfigTypeDef(BaseValidatorModel):
    SourceModelVariantName: str
    ShadowModelVariants: Sequence[ShadowModelVariantConfigTypeDef]

class TrafficPatternOutputTypeDef(BaseValidatorModel):
    TrafficType: Optional[TrafficTypeType] = None
    Phases: Optional[List[PhaseTypeDef]] = None
    Stairs: Optional[StairsTypeDef] = None

class TrafficPatternTypeDef(BaseValidatorModel):
    TrafficType: Optional[TrafficTypeType] = None
    Phases: Optional[Sequence[PhaseTypeDef]] = None
    Stairs: Optional[StairsTypeDef] = None

class TrainingImageConfigTypeDef(BaseValidatorModel):
    TrainingRepositoryAccessMode: TrainingRepositoryAccessModeType
    TrainingRepositoryAuthConfig: Optional[TrainingRepositoryAuthConfigTypeDef] = None

class TransformDataSourceTypeDef(BaseValidatorModel):
    S3DataSource: TransformS3DataSourceTypeDef

class WorkforceTypeDef(BaseValidatorModel):
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

class ListActionsResponseTypeDef(BaseValidatorModel):
    ActionSummaries: List[ActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAppsResponseTypeDef(BaseValidatorModel):
    Apps: List[AppDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DomainSettingsForUpdateTypeDef(BaseValidatorModel):
    RStudioServerProDomainSettingsForUpdate: Optional[       RStudioServerProDomainSettingsForUpdateTypeDef     ] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    DockerSettings: Optional[DockerSettingsTypeDef] = None
    AmazonQSettings: Optional[AmazonQSettingsTypeDef] = None

class DomainSettingsOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettingsTypeDef] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    DockerSettings: Optional[DockerSettingsOutputTypeDef] = None
    AmazonQSettings: Optional[AmazonQSettingsTypeDef] = None

class DomainSettingsTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettingsTypeDef] = None
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfigType] = None
    DockerSettings: Optional[DockerSettingsTypeDef] = None
    AmazonQSettings: Optional[AmazonQSettingsTypeDef] = None

class ArtifactSummaryTypeDef(BaseValidatorModel):
    ArtifactArn: Optional[str] = None
    ArtifactName: Optional[str] = None
    Source: Optional[ArtifactSourceOutputTypeDef] = None
    ArtifactType: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class CreateArtifactRequestRequestTypeDef(BaseValidatorModel):
    Source: ArtifactSourceTypeDef
    ArtifactType: str
    ArtifactName: Optional[str] = None
    Properties: Optional[Mapping[str, str]] = None
    MetadataProperties: Optional[MetadataPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DeleteArtifactRequestRequestTypeDef(BaseValidatorModel):
    ArtifactArn: Optional[str] = None
    Source: Optional[ArtifactSourceTypeDef] = None

class AsyncInferenceConfigOutputTypeDef(BaseValidatorModel):
    OutputConfig: AsyncInferenceOutputConfigOutputTypeDef
    ClientConfig: Optional[AsyncInferenceClientConfigTypeDef] = None

class AsyncInferenceConfigTypeDef(BaseValidatorModel):
    OutputConfig: AsyncInferenceOutputConfigTypeDef
    ClientConfig: Optional[AsyncInferenceClientConfigTypeDef] = None

class TabularJobConfigOutputTypeDef(BaseValidatorModel):
    TargetAttributeName: str
    CandidateGenerationConfig: Optional[CandidateGenerationConfigOutputTypeDef] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    FeatureSpecificationS3Uri: Optional[str] = None
    Mode: Optional[AutoMLModeType] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    ProblemType: Optional[ProblemTypeType] = None
    SampleWeightAttributeName: Optional[str] = None

class TimeSeriesForecastingJobConfigOutputTypeDef(BaseValidatorModel):
    ForecastFrequency: str
    ForecastHorizon: int
    TimeSeriesConfig: TimeSeriesConfigOutputTypeDef
    FeatureSpecificationS3Uri: Optional[str] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    ForecastQuantiles: Optional[List[str]] = None
    Transformations: Optional[TimeSeriesTransformationsOutputTypeDef] = None
    HolidayConfig: Optional[List[HolidayConfigAttributesTypeDef]] = None
    CandidateGenerationConfig: Optional[CandidateGenerationConfigOutputTypeDef] = None

class TabularJobConfigTypeDef(BaseValidatorModel):
    TargetAttributeName: str
    CandidateGenerationConfig: Optional[CandidateGenerationConfigTypeDef] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    FeatureSpecificationS3Uri: Optional[str] = None
    Mode: Optional[AutoMLModeType] = None
    GenerateCandidateDefinitionsOnly: Optional[bool] = None
    ProblemType: Optional[ProblemTypeType] = None
    SampleWeightAttributeName: Optional[str] = None

class TimeSeriesForecastingJobConfigTypeDef(BaseValidatorModel):
    ForecastFrequency: str
    ForecastHorizon: int
    TimeSeriesConfig: TimeSeriesConfigTypeDef
    FeatureSpecificationS3Uri: Optional[str] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    ForecastQuantiles: Optional[Sequence[str]] = None
    Transformations: Optional[TimeSeriesTransformationsTypeDef] = None
    HolidayConfig: Optional[Sequence[HolidayConfigAttributesTypeDef]] = None
    CandidateGenerationConfig: Optional[CandidateGenerationConfigTypeDef] = None

class AutoMLChannelTypeDef(BaseValidatorModel):
    TargetAttributeName: str
    DataSource: Optional[AutoMLDataSourceTypeDef] = None
    CompressionType: Optional[CompressionTypeType] = None
    ContentType: Optional[str] = None
    ChannelType: Optional[AutoMLChannelTypeType] = None
    SampleWeightAttributeName: Optional[str] = None

class AutoMLJobChannelTypeDef(BaseValidatorModel):
    ChannelType: Optional[AutoMLChannelTypeType] = None
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    DataSource: Optional[AutoMLDataSourceTypeDef] = None

class ListAutoMLJobsResponseTypeDef(BaseValidatorModel):
    AutoMLJobSummaries: List[AutoMLJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoMLResolvedAttributesTypeDef(BaseValidatorModel):
    AutoMLJobObjective: Optional[AutoMLJobObjectiveTypeDef] = None
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    AutoMLProblemTypeResolvedAttributes: Optional[       AutoMLProblemTypeResolvedAttributesTypeDef     ] = None

class AutoMLJobConfigOutputTypeDef(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    SecurityConfig: Optional[AutoMLSecurityConfigOutputTypeDef] = None
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfigOutputTypeDef] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfigTypeDef] = None
    Mode: Optional[AutoMLModeType] = None

class LabelingJobAlgorithmsConfigOutputTypeDef(BaseValidatorModel):
    LabelingJobAlgorithmSpecificationArn: str
    InitialActiveLearningModelArn: Optional[str] = None
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfigOutputTypeDef] = None

class AutoMLJobConfigTypeDef(BaseValidatorModel):
    CompletionCriteria: Optional[AutoMLJobCompletionCriteriaTypeDef] = None
    SecurityConfig: Optional[AutoMLSecurityConfigTypeDef] = None
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfigTypeDef] = None
    DataSplitConfig: Optional[AutoMLDataSplitConfigTypeDef] = None
    Mode: Optional[AutoMLModeType] = None

class LabelingJobAlgorithmsConfigTypeDef(BaseValidatorModel):
    LabelingJobAlgorithmSpecificationArn: str
    InitialActiveLearningModelArn: Optional[str] = None
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfigTypeDef] = None

class ModelMetricsTypeDef(BaseValidatorModel):
    ModelQuality: Optional[ModelQualityTypeDef] = None
    ModelDataQuality: Optional[ModelDataQualityTypeDef] = None
    Bias: Optional[BiasTypeDef] = None
    Explainability: Optional[ExplainabilityTypeDef] = None

class PipelineExecutionStepMetadataTypeDef(BaseValidatorModel):
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

class AutoMLCandidateTypeDef(BaseValidatorModel):
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

class BlueGreenUpdatePolicyTypeDef(BaseValidatorModel):
    TrafficRoutingConfiguration: TrafficRoutingConfigTypeDef
    TerminationWaitInSeconds: Optional[int] = None
    MaximumExecutionTimeoutInSeconds: Optional[int] = None

class EndpointInputConfigurationOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameterRanges: Optional[EnvironmentParameterRangesOutputTypeDef] = None

class EndpointInputConfigurationTypeDef(BaseValidatorModel):
    InstanceType: Optional[ProductionVariantInstanceTypeType] = None
    ServerlessConfig: Optional[ProductionVariantServerlessConfigTypeDef] = None
    InferenceSpecificationName: Optional[str] = None
    EnvironmentParameterRanges: Optional[EnvironmentParameterRangesTypeDef] = None

class ClarifyExplainerConfigOutputTypeDef(BaseValidatorModel):
    ShapConfig: ClarifyShapConfigTypeDef
    EnableExplanations: Optional[str] = None
    InferenceConfig: Optional[ClarifyInferenceConfigOutputTypeDef] = None

class ClarifyExplainerConfigTypeDef(BaseValidatorModel):
    ShapConfig: ClarifyShapConfigTypeDef
    EnableExplanations: Optional[str] = None
    InferenceConfig: Optional[ClarifyInferenceConfigTypeDef] = None

class ClusterInstanceGroupDetailsTypeDef(BaseValidatorModel):
    CurrentCount: Optional[int] = None
    TargetCount: Optional[int] = None
    InstanceGroupName: Optional[str] = None
    InstanceType: Optional[ClusterInstanceTypeType] = None
    LifeCycleConfig: Optional[ClusterLifeCycleConfigTypeDef] = None
    ExecutionRole: Optional[str] = None
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[List[ClusterInstanceStorageConfigTypeDef]] = None

class ClusterInstanceGroupSpecificationTypeDef(BaseValidatorModel):
    InstanceCount: int
    InstanceGroupName: str
    InstanceType: ClusterInstanceTypeType
    LifeCycleConfig: ClusterLifeCycleConfigTypeDef
    ExecutionRole: str
    ThreadsPerCore: Optional[int] = None
    InstanceStorageConfigs: Optional[Sequence[ClusterInstanceStorageConfigTypeDef]] = None

class ClusterNodeDetailsTypeDef(BaseValidatorModel):
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

class ListClusterNodesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ClusterNodeSummaries: List[ClusterNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCodeRepositoriesOutputTypeDef(BaseValidatorModel):
    CodeRepositorySummaryList: List[CodeRepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FeatureDefinitionTypeDef(BaseValidatorModel):
    FeatureName: str
    FeatureType: FeatureTypeType
    CollectionType: Optional[CollectionTypeType] = None
    CollectionConfig: Optional[CollectionConfigTypeDef] = None

class ListContextsResponseTypeDef(BaseValidatorModel):
    ContextSummaries: List[ContextSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class QueryLineageRequestRequestTypeDef(BaseValidatorModel):
    StartArns: Optional[Sequence[str]] = None
    Direction: Optional[DirectionType] = None
    IncludeEdges: Optional[bool] = None
    Filters: Optional[QueryFiltersTypeDef] = None
    MaxDepth: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ChannelExtraOutputTypeDef(BaseValidatorModel):
    ChannelName: str
    DataSource: DataSourceExtraOutputTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfigTypeDef] = None

class ChannelOutputTypeDef(BaseValidatorModel):
    ChannelName: str
    DataSource: DataSourceOutputTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfigTypeDef] = None

class ChannelTypeDef(BaseValidatorModel):
    ChannelName: str
    DataSource: DataSourceTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    RecordWrapperType: Optional[RecordWrapperType] = None
    InputMode: Optional[TrainingInputModeType] = None
    ShuffleConfig: Optional[ShuffleConfigTypeDef] = None

class ProcessingInputTypeDef(BaseValidatorModel):
    InputName: str
    AppManaged: Optional[bool] = None
    S3Input: Optional[ProcessingS3InputTypeDef] = None
    DatasetDefinition: Optional[DatasetDefinitionTypeDef] = None

class DefaultSpaceSettingsOutputTypeDef(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutputTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutputTypeDef] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsOutputTypeDef] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettingsTypeDef] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfigTypeDef] = None
    CustomFileSystemConfigs: Optional[List[CustomFileSystemConfigTypeDef]] = None

class DefaultSpaceSettingsTypeDef(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[JupyterLabAppSettingsTypeDef] = None
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettingsTypeDef] = None
    CustomPosixUserConfig: Optional[CustomPosixUserConfigTypeDef] = None
    CustomFileSystemConfigs: Optional[Sequence[CustomFileSystemConfigTypeDef]] = None

class UserSettingsOutputTypeDef(BaseValidatorModel):
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

class UserSettingsTypeDef(BaseValidatorModel):
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

class InferenceComponentSpecificationSummaryTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    Container: Optional[InferenceComponentContainerSpecificationSummaryTypeDef] = None
    StartupParameters: Optional[InferenceComponentStartupParametersTypeDef] = None
    ComputeResourceRequirements: Optional[       InferenceComponentComputeResourceRequirementsTypeDef     ] = None

class DescribeEdgeDeploymentPlanResponseTypeDef(BaseValidatorModel):
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

class CreateEdgeDeploymentPlanRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    ModelConfigs: Sequence[EdgeDeploymentModelConfigTypeDef]
    DeviceFleetName: str
    Stages: Optional[Sequence[DeploymentStageTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEdgeDeploymentStageRequestRequestTypeDef(BaseValidatorModel):
    EdgeDeploymentPlanName: str
    Stages: Sequence[DeploymentStageTypeDef]

class ListExperimentsResponseTypeDef(BaseValidatorModel):
    ExperimentSummaries: List[ExperimentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFeatureGroupsResponseTypeDef(BaseValidatorModel):
    FeatureGroupSummaries: List[FeatureGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListInferenceExperimentsResponseTypeDef(BaseValidatorModel):
    InferenceExperiments: List[InferenceExperimentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrainingJobsResponseTypeDef(BaseValidatorModel):
    TrainingJobSummaries: List[TrainingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrialsResponseTypeDef(BaseValidatorModel):
    TrialSummaries: List[TrialSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    DesiredWeightsAndCapacities: Sequence[DesiredWeightAndCapacityTypeDef]

class ListDevicesResponseTypeDef(BaseValidatorModel):
    DeviceSummaries: List[DeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DriftCheckBaselinesTypeDef(BaseValidatorModel):
    Bias: Optional[DriftCheckBiasTypeDef] = None
    Explainability: Optional[DriftCheckExplainabilityTypeDef] = None
    ModelQuality: Optional[DriftCheckModelQualityTypeDef] = None
    ModelDataQuality: Optional[DriftCheckModelDataQualityTypeDef] = None

class SpaceSettingsOutputTypeDef(BaseValidatorModel):
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsOutputTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsOutputTypeDef] = None
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettingsOutputTypeDef] = None
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettingsTypeDef] = None
    CustomFileSystems: Optional[List[CustomFileSystemTypeDef]] = None

class SpaceSettingsSummaryTypeDef(BaseValidatorModel):
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettingsTypeDef] = None

class SpaceSettingsTypeDef(BaseValidatorModel):
    JupyterServerAppSettings: Optional[JupyterServerAppSettingsTypeDef] = None
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettingsTypeDef] = None
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettingsTypeDef] = None
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettingsTypeDef] = None
    AppType: Optional[AppTypeType] = None
    SpaceStorageSettings: Optional[SpaceStorageSettingsTypeDef] = None
    CustomFileSystems: Optional[Sequence[CustomFileSystemTypeDef]] = None

class InferenceRecommendationTypeDef(BaseValidatorModel):
    EndpointConfiguration: EndpointOutputConfigurationTypeDef
    ModelConfiguration: ModelConfigurationTypeDef
    RecommendationId: Optional[str] = None
    Metrics: Optional[RecommendationMetricsTypeDef] = None
    InvocationEndTime: Optional[datetime] = None
    InvocationStartTime: Optional[datetime] = None

class RecommendationJobInferenceBenchmarkTypeDef(BaseValidatorModel):
    ModelConfiguration: ModelConfigurationTypeDef
    Metrics: Optional[RecommendationMetricsTypeDef] = None
    EndpointMetrics: Optional[InferenceMetricsTypeDef] = None
    EndpointConfiguration: Optional[EndpointOutputConfigurationTypeDef] = None
    FailureReason: Optional[str] = None
    InvocationEndTime: Optional[datetime] = None
    InvocationStartTime: Optional[datetime] = None

class SearchExpressionTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NestedFilters: Optional[Sequence[NestedFiltersTypeDef]] = None
    SubExpressions: Optional[Sequence[Dict[str, Any]]] = None
    Operator: Optional[BooleanOperatorType] = None

class ListTrainingJobsForHyperParameterTuningJobResponseTypeDef(BaseValidatorModel):
    TrainingJobSummaries: List[HyperParameterTrainingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHyperParameterTuningJobsResponseTypeDef(BaseValidatorModel):
    HyperParameterTuningJobSummaries: List[HyperParameterTuningJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociationSummaryTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceType: Optional[str] = None
    DestinationType: Optional[str] = None
    AssociationType: Optional[AssociationEdgeTypeType] = None
    SourceName: Optional[str] = None
    DestinationName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None

class DescribeActionResponseTypeDef(BaseValidatorModel):
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

class DescribeArtifactResponseTypeDef(BaseValidatorModel):
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

class DescribeContextResponseTypeDef(BaseValidatorModel):
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

class DescribeExperimentResponseTypeDef(BaseValidatorModel):
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

class DescribeLineageGroupResponseTypeDef(BaseValidatorModel):
    LineageGroupName: str
    LineageGroupArn: str
    DisplayName: str
    Description: str
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    LastModifiedTime: datetime
    LastModifiedBy: UserContextTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMlflowTrackingServerResponseTypeDef(BaseValidatorModel):
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

class DescribeModelCardResponseTypeDef(BaseValidatorModel):
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

class DescribeModelPackageGroupOutputTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    ModelPackageGroupDescription: str
    CreationTime: datetime
    CreatedBy: UserContextTypeDef
    ModelPackageGroupStatus: ModelPackageGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePipelineResponseTypeDef(BaseValidatorModel):
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

class DescribeTrialComponentResponseTypeDef(BaseValidatorModel):
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

class DescribeTrialResponseTypeDef(BaseValidatorModel):
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

class ExperimentTypeDef(BaseValidatorModel):
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

class ModelCardTypeDef(BaseValidatorModel):
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

class ModelDashboardModelCardTypeDef(BaseValidatorModel):
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

class ModelPackageGroupTypeDef(BaseValidatorModel):
    ModelPackageGroupName: Optional[str] = None
    ModelPackageGroupArn: Optional[str] = None
    ModelPackageGroupDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None
    ModelPackageGroupStatus: Optional[ModelPackageGroupStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None

class PipelineTypeDef(BaseValidatorModel):
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

class TrialComponentSimpleSummaryTypeDef(BaseValidatorModel):
    TrialComponentName: Optional[str] = None
    TrialComponentArn: Optional[str] = None
    TrialComponentSource: Optional[TrialComponentSourceTypeDef] = None
    CreationTime: Optional[datetime] = None
    CreatedBy: Optional[UserContextTypeDef] = None

class TrialComponentSummaryTypeDef(BaseValidatorModel):
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

class WorkerAccessConfigurationTypeDef(BaseValidatorModel):
    S3Presign: Optional[S3PresignTypeDef] = None

class CreateInferenceComponentInputRequestTypeDef(BaseValidatorModel):
    InferenceComponentName: str
    EndpointName: str
    VariantName: str
    Specification: InferenceComponentSpecificationTypeDef
    RuntimeConfig: InferenceComponentRuntimeConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateInferenceComponentInputRequestTypeDef(BaseValidatorModel):
    InferenceComponentName: str
    Specification: Optional[InferenceComponentSpecificationTypeDef] = None
    RuntimeConfig: Optional[InferenceComponentRuntimeConfigTypeDef] = None

class HyperParameterSpecificationOutputTypeDef(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    Description: Optional[str] = None
    Range: Optional[ParameterRangeOutputTypeDef] = None
    IsTunable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    DefaultValue: Optional[str] = None

class HyperParameterSpecificationTypeDef(BaseValidatorModel):
    Name: str
    Type: ParameterTypeType
    Description: Optional[str] = None
    Range: Optional[ParameterRangeTypeDef] = None
    IsTunable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    DefaultValue: Optional[str] = None

class HyperParameterTuningJobConfigExtraOutputTypeDef(BaseValidatorModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimitsTypeDef
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfigTypeDef] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    ParameterRanges: Optional[ParameterRangesExtraOutputTypeDef] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteriaTypeDef] = None
    RandomSeed: Optional[int] = None

class HyperParameterTuningJobConfigOutputTypeDef(BaseValidatorModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimitsTypeDef
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfigTypeDef] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    ParameterRanges: Optional[ParameterRangesOutputTypeDef] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteriaTypeDef] = None
    RandomSeed: Optional[int] = None

class HyperParameterTuningJobConfigTypeDef(BaseValidatorModel):
    Strategy: HyperParameterTuningJobStrategyTypeType
    ResourceLimits: ResourceLimitsTypeDef
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfigTypeDef] = None
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjectiveTypeDef] = None
    ParameterRanges: Optional[ParameterRangesTypeDef] = None
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingTypeType] = None
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteriaTypeDef] = None
    RandomSeed: Optional[int] = None

class AppImageConfigDetailsTypeDef(BaseValidatorModel):
    AppImageConfigArn: Optional[str] = None
    AppImageConfigName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigOutputTypeDef] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigOutputTypeDef] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigOutputTypeDef] = None

class DescribeAppImageConfigResponseTypeDef(BaseValidatorModel):
    AppImageConfigArn: str
    AppImageConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    KernelGatewayImageConfig: KernelGatewayImageConfigOutputTypeDef
    JupyterLabAppImageConfig: JupyterLabAppImageConfigOutputTypeDef
    CodeEditorAppImageConfig: CodeEditorAppImageConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppImageConfigRequestRequestTypeDef(BaseValidatorModel):
    AppImageConfigName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigTypeDef] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigTypeDef] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigTypeDef] = None

class UpdateAppImageConfigRequestRequestTypeDef(BaseValidatorModel):
    AppImageConfigName: str
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfigTypeDef] = None
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfigTypeDef] = None
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfigTypeDef] = None

class ListLabelingJobsForWorkteamResponseTypeDef(BaseValidatorModel):
    LabelingJobSummaryList: List[LabelingJobForWorkteamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LabelingJobInputConfigExtraOutputTypeDef(BaseValidatorModel):
    DataSource: LabelingJobDataSourceTypeDef
    DataAttributes: Optional[LabelingJobDataAttributesExtraOutputTypeDef] = None

class LabelingJobInputConfigOutputTypeDef(BaseValidatorModel):
    DataSource: LabelingJobDataSourceTypeDef
    DataAttributes: Optional[LabelingJobDataAttributesOutputTypeDef] = None

class LabelingJobInputConfigTypeDef(BaseValidatorModel):
    DataSource: LabelingJobDataSourceTypeDef
    DataAttributes: Optional[LabelingJobDataAttributesTypeDef] = None

class TargetTrackingScalingPolicyConfigurationTypeDef(BaseValidatorModel):
    MetricSpecification: Optional[MetricSpecificationTypeDef] = None
    TargetValue: Optional[float] = None

class AdditionalModelDataSourceTypeDef(BaseValidatorModel):
    ChannelName: str
    S3DataSource: S3ModelDataSourceTypeDef

class ModelDataSourceTypeDef(BaseValidatorModel):
    S3DataSource: Optional[S3ModelDataSourceTypeDef] = None

class MonitoringAlertSummaryTypeDef(BaseValidatorModel):
    MonitoringAlertName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    AlertStatus: MonitoringAlertStatusType
    DatapointsToAlert: int
    EvaluationPeriod: int
    Actions: MonitoringAlertActionsTypeDef

class ModelVariantConfigSummaryTypeDef(BaseValidatorModel):
    ModelName: str
    VariantName: str
    InfrastructureConfig: ModelInfrastructureConfigTypeDef
    Status: ModelVariantStatusType

class ModelVariantConfigTypeDef(BaseValidatorModel):
    ModelName: str
    VariantName: str
    InfrastructureConfig: ModelInfrastructureConfigTypeDef

class ListModelMetadataRequestListModelMetadataPaginateTypeDef(BaseValidatorModel):
    SearchExpression: Optional[ModelMetadataSearchExpressionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelMetadataRequestRequestTypeDef(BaseValidatorModel):
    SearchExpression: Optional[ModelMetadataSearchExpressionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class BatchTransformInputExtraOutputTypeDef(BaseValidatorModel):
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

class BatchTransformInputOutputTypeDef(BaseValidatorModel):
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

class BatchTransformInputTypeDef(BaseValidatorModel):
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

class MonitoringOutputConfigExtraOutputTypeDef(BaseValidatorModel):
    MonitoringOutputs: List[MonitoringOutputTypeDef]
    KmsKeyId: Optional[str] = None

class MonitoringOutputConfigOutputTypeDef(BaseValidatorModel):
    MonitoringOutputs: List[MonitoringOutputTypeDef]
    KmsKeyId: Optional[str] = None

class MonitoringOutputConfigTypeDef(BaseValidatorModel):
    MonitoringOutputs: Sequence[MonitoringOutputTypeDef]
    KmsKeyId: Optional[str] = None

class OptimizationJobModelSourceTypeDef(BaseValidatorModel):
    S3: Optional[OptimizationJobModelSourceS3TypeDef] = None

class CreateCompilationJobRequestRequestTypeDef(BaseValidatorModel):
    CompilationJobName: str
    RoleArn: str
    OutputConfig: OutputConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    ModelPackageVersionArn: Optional[str] = None
    InputConfig: Optional[InputConfigTypeDef] = None
    VpcConfig: Optional[NeoVpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeCompilationJobResponseTypeDef(BaseValidatorModel):
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

class PendingDeploymentSummaryTypeDef(BaseValidatorModel):
    EndpointConfigName: str
    ProductionVariants: Optional[List[PendingProductionVariantSummaryTypeDef]] = None
    StartTime: Optional[datetime] = None
    ShadowProductionVariants: Optional[List[PendingProductionVariantSummaryTypeDef]] = None

class ProcessingOutputConfigExtraOutputTypeDef(BaseValidatorModel):
    Outputs: List[ProcessingOutputTypeDef]
    KmsKeyId: Optional[str] = None

class ProcessingOutputConfigOutputTypeDef(BaseValidatorModel):
    Outputs: List[ProcessingOutputTypeDef]
    KmsKeyId: Optional[str] = None

class ProcessingOutputConfigTypeDef(BaseValidatorModel):
    Outputs: Sequence[ProcessingOutputTypeDef]
    KmsKeyId: Optional[str] = None

class UpdateTrainingJobRequestRequestTypeDef(BaseValidatorModel):
    TrainingJobName: str
    ProfilerConfig: Optional[ProfilerConfigForUpdateTypeDef] = None
    ProfilerRuleConfigurations: Optional[Sequence[ProfilerRuleConfigurationUnionTypeDef]] = None
    ResourceConfig: Optional[ResourceConfigForUpdateTypeDef] = None
    RemoteDebugConfig: Optional[RemoteDebugConfigForUpdateTypeDef] = None

class GetSearchSuggestionsRequestRequestTypeDef(BaseValidatorModel):
    Resource: ResourceTypeType
    SuggestionQuery: Optional[SuggestionQueryTypeDef] = None

class DescribeProjectOutputTypeDef(BaseValidatorModel):
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

class ProjectTypeDef(BaseValidatorModel):
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

class CreateProjectInputRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsTypeDef
    ProjectDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateProjectInputRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ProjectDescription: Optional[str] = None
    ServiceCatalogProvisioningUpdateDetails: Optional[       ServiceCatalogProvisioningUpdateDetailsTypeDef     ] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class HumanLoopConfigOutputTypeDef(BaseValidatorModel):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    TaskTimeLimitInSeconds: Optional[int] = None
    TaskKeywords: Optional[List[str]] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPriceTypeDef] = None

class HumanLoopConfigTypeDef(BaseValidatorModel):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int
    TaskAvailabilityLifetimeInSeconds: Optional[int] = None
    TaskTimeLimitInSeconds: Optional[int] = None
    TaskKeywords: Optional[Sequence[str]] = None
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPriceTypeDef] = None

class HumanTaskConfigOutputTypeDef(BaseValidatorModel):
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

class HumanTaskConfigTypeDef(BaseValidatorModel):
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

class DescribePipelineExecutionResponseTypeDef(BaseValidatorModel):
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

class PipelineExecutionTypeDef(BaseValidatorModel):
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

class StartPipelineExecutionRequestRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    ClientRequestToken: str
    PipelineExecutionDisplayName: Optional[str] = None
    PipelineParameters: Optional[Sequence[ParameterTypeDef]] = None
    PipelineExecutionDescription: Optional[str] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfigTypeDef] = None

class AlgorithmSpecificationExtraOutputTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfigTypeDef] = None

class AlgorithmSpecificationOutputTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[List[str]] = None
    ContainerArguments: Optional[List[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfigTypeDef] = None

class AlgorithmSpecificationTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    TrainingImage: Optional[str] = None
    AlgorithmName: Optional[str] = None
    MetricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None
    EnableSageMakerMetricsTimeSeries: Optional[bool] = None
    ContainerEntrypoint: Optional[Sequence[str]] = None
    ContainerArguments: Optional[Sequence[str]] = None
    TrainingImageConfig: Optional[TrainingImageConfigTypeDef] = None

class TransformInputTypeDef(BaseValidatorModel):
    DataSource: TransformDataSourceTypeDef
    ContentType: Optional[str] = None
    CompressionType: Optional[CompressionTypeType] = None
    SplitType: Optional[SplitTypeType] = None

class DescribeWorkforceResponseTypeDef(BaseValidatorModel):
    Workforce: WorkforceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkforcesResponseTypeDef(BaseValidatorModel):
    Workforces: List[WorkforceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateWorkforceResponseTypeDef(BaseValidatorModel):
    Workforce: WorkforceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArtifactsResponseTypeDef(BaseValidatorModel):
    ArtifactSummaries: List[ArtifactSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoMLProblemTypeConfigOutputTypeDef(BaseValidatorModel):
    ImageClassificationJobConfig: Optional[ImageClassificationJobConfigTypeDef] = None
    TextClassificationJobConfig: Optional[TextClassificationJobConfigTypeDef] = None
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfigOutputTypeDef] = None
    TabularJobConfig: Optional[TabularJobConfigOutputTypeDef] = None
    TextGenerationJobConfig: Optional[TextGenerationJobConfigOutputTypeDef] = None

class AutoMLProblemTypeConfigTypeDef(BaseValidatorModel):
    ImageClassificationJobConfig: Optional[ImageClassificationJobConfigTypeDef] = None
    TextClassificationJobConfig: Optional[TextClassificationJobConfigTypeDef] = None
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfigTypeDef] = None
    TabularJobConfig: Optional[TabularJobConfigTypeDef] = None
    TextGenerationJobConfig: Optional[TextGenerationJobConfigTypeDef] = None

class CreateAutoMLJobRequestRequestTypeDef(BaseValidatorModel):
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

class PipelineExecutionStepTypeDef(BaseValidatorModel):
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

class DescribeAutoMLJobResponseTypeDef(BaseValidatorModel):
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

class ListCandidatesForAutoMLJobResponseTypeDef(BaseValidatorModel):
    Candidates: List[AutoMLCandidateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeploymentConfigOutputTypeDef(BaseValidatorModel):
    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicyTypeDef] = None
    RollingUpdatePolicy: Optional[RollingUpdatePolicyTypeDef] = None
    AutoRollbackConfiguration: Optional[AutoRollbackConfigOutputTypeDef] = None

class DeploymentConfigTypeDef(BaseValidatorModel):
    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicyTypeDef] = None
    RollingUpdatePolicy: Optional[RollingUpdatePolicyTypeDef] = None
    AutoRollbackConfiguration: Optional[AutoRollbackConfigTypeDef] = None

class RecommendationJobInputConfigOutputTypeDef(BaseValidatorModel):
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

class RecommendationJobInputConfigTypeDef(BaseValidatorModel):
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

class ExplainerConfigOutputTypeDef(BaseValidatorModel):
    ClarifyExplainerConfig: Optional[ClarifyExplainerConfigOutputTypeDef] = None

class ExplainerConfigTypeDef(BaseValidatorModel):
    ClarifyExplainerConfig: Optional[ClarifyExplainerConfigTypeDef] = None

class DescribeClusterResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    ClusterStatus: ClusterStatusType
    CreationTime: datetime
    FailureMessage: str
    InstanceGroups: List[ClusterInstanceGroupDetailsTypeDef]
    VpcConfig: VpcConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    InstanceGroups: Sequence[ClusterInstanceGroupSpecificationTypeDef]
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    InstanceGroups: Sequence[ClusterInstanceGroupSpecificationTypeDef]

class DescribeClusterNodeResponseTypeDef(BaseValidatorModel):
    NodeDetails: ClusterNodeDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFeatureGroupRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeFeatureGroupResponseTypeDef(BaseValidatorModel):
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

class FeatureGroupTypeDef(BaseValidatorModel):
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

class UpdateFeatureGroupRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    FeatureAdditions: Optional[Sequence[FeatureDefinitionTypeDef]] = None
    OnlineStoreConfig: Optional[OnlineStoreConfigUpdateTypeDef] = None
    ThroughputConfig: Optional[ThroughputConfigUpdateTypeDef] = None

class HyperParameterTrainingJobDefinitionExtraOutputTypeDef(BaseValidatorModel):
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

class HyperParameterTrainingJobDefinitionOutputTypeDef(BaseValidatorModel):
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

class TrainingJobDefinitionOutputTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    InputDataConfig: List[ChannelOutputTypeDef]
    OutputDataConfig: OutputDataConfigTypeDef
    ResourceConfig: ResourceConfigOutputTypeDef
    StoppingCondition: StoppingConditionTypeDef
    HyperParameters: Optional[Dict[str, str]] = None

class HyperParameterTrainingJobDefinitionTypeDef(BaseValidatorModel):
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

class TrainingJobDefinitionTypeDef(BaseValidatorModel):
    TrainingInputMode: TrainingInputModeType
    InputDataConfig: Sequence[ChannelTypeDef]
    OutputDataConfig: OutputDataConfigTypeDef
    ResourceConfig: ResourceConfigTypeDef
    StoppingCondition: StoppingConditionTypeDef
    HyperParameters: Optional[Mapping[str, str]] = None

class DescribeDomainResponseTypeDef(BaseValidatorModel):
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

class DescribeUserProfileResponseTypeDef(BaseValidatorModel):
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

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
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

class CreateUserProfileRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    SingleSignOnUserIdentifier: Optional[str] = None
    SingleSignOnUserValue: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UserSettings: Optional[UserSettingsTypeDef] = None

class UpdateDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    DefaultUserSettings: Optional[UserSettingsTypeDef] = None
    DomainSettingsForUpdate: Optional[DomainSettingsForUpdateTypeDef] = None
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagementType] = None
    DefaultSpaceSettings: Optional[DefaultSpaceSettingsTypeDef] = None
    SubnetIds: Optional[Sequence[str]] = None
    AppNetworkAccessType: Optional[AppNetworkAccessTypeType] = None

class UpdateUserProfileRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    UserProfileName: str
    UserSettings: Optional[UserSettingsTypeDef] = None

class DescribeInferenceComponentOutputTypeDef(BaseValidatorModel):
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

class DescribeSpaceResponseTypeDef(BaseValidatorModel):
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

class SpaceDetailsTypeDef(BaseValidatorModel):
    DomainId: Optional[str] = None
    SpaceName: Optional[str] = None
    Status: Optional[SpaceStatusType] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    SpaceSettingsSummary: Optional[SpaceSettingsSummaryTypeDef] = None
    SpaceSharingSettingsSummary: Optional[SpaceSharingSettingsSummaryTypeDef] = None
    OwnershipSettingsSummary: Optional[OwnershipSettingsSummaryTypeDef] = None
    SpaceDisplayName: Optional[str] = None

class CreateSpaceRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpaceName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    SpaceSettings: Optional[SpaceSettingsTypeDef] = None
    OwnershipSettings: Optional[OwnershipSettingsTypeDef] = None
    SpaceSharingSettings: Optional[SpaceSharingSettingsTypeDef] = None
    SpaceDisplayName: Optional[str] = None

class UpdateSpaceRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpaceName: str
    SpaceSettings: Optional[SpaceSettingsTypeDef] = None
    SpaceDisplayName: Optional[str] = None

class InferenceRecommendationsJobStepTypeDef(BaseValidatorModel):
    StepType: Literal["BENCHMARK"]
    JobName: str
    Status: RecommendationJobStatusType
    InferenceBenchmark: Optional[RecommendationJobInferenceBenchmarkTypeDef] = None

class SearchRequestSearchPaginateTypeDef(BaseValidatorModel):
    Resource: ResourceTypeType
    SearchExpression: Optional[SearchExpressionTypeDef] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SearchSortOrderType] = None
    CrossAccountFilterOption: Optional[CrossAccountFilterOptionType] = None
    VisibilityConditions: Optional[Sequence[VisibilityConditionsTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociationsResponseTypeDef(BaseValidatorModel):
    AssociationSummaries: List[AssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TrialTypeDef(BaseValidatorModel):
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

class ListTrialComponentsResponseTypeDef(BaseValidatorModel):
    TrialComponentSummaries: List[TrialComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class WorkteamTypeDef(BaseValidatorModel):
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

class TrainingSpecificationOutputTypeDef(BaseValidatorModel):
    TrainingImage: str
    SupportedTrainingInstanceTypes: List[TrainingInstanceTypeType]
    TrainingChannels: List[ChannelSpecificationOutputTypeDef]
    TrainingImageDigest: Optional[str] = None
    SupportedHyperParameters: Optional[List[HyperParameterSpecificationOutputTypeDef]] = None
    SupportsDistributedTraining: Optional[bool] = None
    MetricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None
    SupportedTuningJobObjectiveMetrics: Optional[       List[HyperParameterTuningJobObjectiveTypeDef]     ] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class TrainingSpecificationTypeDef(BaseValidatorModel):
    TrainingImage: str
    SupportedTrainingInstanceTypes: Sequence[TrainingInstanceTypeType]
    TrainingChannels: Sequence[ChannelSpecificationTypeDef]
    TrainingImageDigest: Optional[str] = None
    SupportedHyperParameters: Optional[Sequence[HyperParameterSpecificationTypeDef]] = None
    SupportsDistributedTraining: Optional[bool] = None
    MetricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None
    SupportedTuningJobObjectiveMetrics: Optional[       Sequence[HyperParameterTuningJobObjectiveTypeDef]     ] = None
    AdditionalS3DataSource: Optional[AdditionalS3DataSourceTypeDef] = None

class ListAppImageConfigsResponseTypeDef(BaseValidatorModel):
    AppImageConfigs: List[AppImageConfigDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LabelingJobSummaryTypeDef(BaseValidatorModel):
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

class CreateWorkteamRequestRequestTypeDef(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: Sequence[MemberDefinitionUnionTypeDef]
    Description: str
    WorkforceName: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateWorkteamRequestRequestTypeDef(BaseValidatorModel):
    WorkteamName: str
    MemberDefinitions: Optional[Sequence[MemberDefinitionUnionTypeDef]] = None
    Description: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    WorkerAccessConfiguration: Optional[WorkerAccessConfigurationTypeDef] = None

class ScalingPolicyTypeDef(BaseValidatorModel):
    TargetTracking: Optional[TargetTrackingScalingPolicyConfigurationTypeDef] = None

class ContainerDefinitionExtraOutputTypeDef(BaseValidatorModel):
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

class ContainerDefinitionOutputTypeDef(BaseValidatorModel):
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

class ContainerDefinitionTypeDef(BaseValidatorModel):
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

class ModelPackageContainerDefinitionExtraOutputTypeDef(BaseValidatorModel):
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

class ModelPackageContainerDefinitionOutputTypeDef(BaseValidatorModel):
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

class ModelPackageContainerDefinitionTypeDef(BaseValidatorModel):
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

class SourceAlgorithmTypeDef(BaseValidatorModel):
    AlgorithmName: str
    ModelDataUrl: Optional[str] = None
    ModelDataSource: Optional[ModelDataSourceTypeDef] = None

class ListMonitoringAlertsResponseTypeDef(BaseValidatorModel):
    MonitoringAlertSummaries: List[MonitoringAlertSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInferenceExperimentResponseTypeDef(BaseValidatorModel):
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

class CreateInferenceExperimentRequestRequestTypeDef(BaseValidatorModel):
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

class StopInferenceExperimentRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ModelVariantActions: Mapping[str, ModelVariantActionType]
    DesiredModelVariants: Optional[Sequence[ModelVariantConfigTypeDef]] = None
    DesiredState: Optional[InferenceExperimentStopDesiredStateType] = None
    Reason: Optional[str] = None

class UpdateInferenceExperimentRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Schedule: Optional[InferenceExperimentScheduleTypeDef] = None
    Description: Optional[str] = None
    ModelVariants: Optional[Sequence[ModelVariantConfigTypeDef]] = None
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfigTypeDef] = None
    ShadowModeConfig: Optional[ShadowModeConfigTypeDef] = None

class MonitoringInputExtraOutputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputExtraOutputTypeDef] = None

class DataQualityJobInputOutputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class ModelBiasJobInputOutputTypeDef(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class ModelExplainabilityJobInputOutputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class ModelQualityJobInputOutputTypeDef(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class MonitoringInputOutputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputOutputTypeDef] = None

class DataQualityJobInputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class ModelBiasJobInputTypeDef(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class ModelExplainabilityJobInputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class ModelQualityJobInputTypeDef(BaseValidatorModel):
    GroundTruthS3Input: MonitoringGroundTruthS3InputTypeDef
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class MonitoringInputTypeDef(BaseValidatorModel):
    EndpointInput: Optional[EndpointInputTypeDef] = None
    BatchTransformInput: Optional[BatchTransformInputTypeDef] = None

class CreateOptimizationJobRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeOptimizationJobResponseTypeDef(BaseValidatorModel):
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

class DescribeProcessingJobResponseTypeDef(BaseValidatorModel):
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

class ProcessingJobTypeDef(BaseValidatorModel):
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

class CreateProcessingJobRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeFlowDefinitionResponseTypeDef(BaseValidatorModel):
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

class CreateFlowDefinitionRequestRequestTypeDef(BaseValidatorModel):
    FlowDefinitionName: str
    OutputConfig: FlowDefinitionOutputConfigTypeDef
    RoleArn: str
    HumanLoopRequestSource: Optional[HumanLoopRequestSourceTypeDef] = None
    HumanLoopActivationConfig: Optional[HumanLoopActivationConfigTypeDef] = None
    HumanLoopConfig: Optional[HumanLoopConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeLabelingJobResponseTypeDef(BaseValidatorModel):
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

class CreateLabelingJobRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeTrainingJobResponseTypeDef(BaseValidatorModel):
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

class TrainingJobTypeDef(BaseValidatorModel):
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

class CreateTransformJobRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeTransformJobResponseTypeDef(BaseValidatorModel):
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

class TransformJobDefinitionExtraOutputTypeDef(BaseValidatorModel):
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None

class TransformJobDefinitionOutputTypeDef(BaseValidatorModel):
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Dict[str, str]] = None

class TransformJobDefinitionTypeDef(BaseValidatorModel):
    TransformInput: TransformInputTypeDef
    TransformOutput: TransformOutputTypeDef
    TransformResources: TransformResourcesTypeDef
    MaxConcurrentTransforms: Optional[int] = None
    MaxPayloadInMB: Optional[int] = None
    BatchStrategy: Optional[BatchStrategyType] = None
    Environment: Optional[Mapping[str, str]] = None

class TransformJobTypeDef(BaseValidatorModel):
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

class DescribeAutoMLJobV2ResponseTypeDef(BaseValidatorModel):
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

class CreateAutoMLJobV2RequestRequestTypeDef(BaseValidatorModel):
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

class ListPipelineExecutionStepsResponseTypeDef(BaseValidatorModel):
    PipelineExecutionSteps: List[PipelineExecutionStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEndpointInputRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: str
    DeploymentConfig: Optional[DeploymentConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateEndpointInputRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    EndpointConfigName: str
    RetainAllVariantProperties: Optional[bool] = None
    ExcludeRetainedVariantProperties: Optional[Sequence[VariantPropertyTypeDef]] = None
    DeploymentConfig: Optional[DeploymentConfigTypeDef] = None
    RetainDeploymentConfig: Optional[bool] = None

class DescribeInferenceRecommendationsJobResponseTypeDef(BaseValidatorModel):
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

class CreateInferenceRecommendationsJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: str
    JobType: RecommendationJobTypeType
    RoleArn: str
    InputConfig: RecommendationJobInputConfigTypeDef
    JobDescription: Optional[str] = None
    StoppingConditions: Optional[RecommendationJobStoppingConditionsTypeDef] = None
    OutputConfig: Optional[RecommendationJobOutputConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeEndpointConfigOutputTypeDef(BaseValidatorModel):
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

class DescribeEndpointOutputTypeDef(BaseValidatorModel):
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

class CreateEndpointConfigInputRequestTypeDef(BaseValidatorModel):
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

class DescribeHyperParameterTuningJobResponseTypeDef(BaseValidatorModel):
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

class HyperParameterTuningJobSearchEntityTypeDef(BaseValidatorModel):
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

class CreateTrainingJobRequestRequestTypeDef(BaseValidatorModel):
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

class ListSpacesResponseTypeDef(BaseValidatorModel):
    Spaces: List[SpaceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListInferenceRecommendationsJobStepsResponseTypeDef(BaseValidatorModel):
    Steps: List[InferenceRecommendationsJobStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeWorkteamResponseTypeDef(BaseValidatorModel):
    Workteam: WorkteamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkteamsResponseTypeDef(BaseValidatorModel):
    Workteams: List[WorkteamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateWorkteamResponseTypeDef(BaseValidatorModel):
    Workteam: WorkteamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLabelingJobsResponseTypeDef(BaseValidatorModel):
    LabelingJobSummaryList: List[LabelingJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DynamicScalingConfigurationTypeDef(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None
    ScalingPolicies: Optional[List[ScalingPolicyTypeDef]] = None

class DescribeModelOutputTypeDef(BaseValidatorModel):
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

class ModelTypeDef(BaseValidatorModel):
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

class AdditionalInferenceSpecificationDefinitionExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Containers: List[ModelPackageContainerDefinitionExtraOutputTypeDef]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class InferenceSpecificationExtraOutputTypeDef(BaseValidatorModel):
    Containers: List[ModelPackageContainerDefinitionExtraOutputTypeDef]
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class AdditionalInferenceSpecificationDefinitionOutputTypeDef(BaseValidatorModel):
    Name: str
    Containers: List[ModelPackageContainerDefinitionOutputTypeDef]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class InferenceSpecificationOutputTypeDef(BaseValidatorModel):
    Containers: List[ModelPackageContainerDefinitionOutputTypeDef]
    SupportedTransformInstanceTypes: Optional[List[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       List[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[List[str]] = None
    SupportedResponseMIMETypes: Optional[List[str]] = None

class AdditionalInferenceSpecificationDefinitionTypeDef(BaseValidatorModel):
    Name: str
    Containers: Sequence[ModelPackageContainerDefinitionTypeDef]
    Description: Optional[str] = None
    SupportedTransformInstanceTypes: Optional[Sequence[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       Sequence[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[Sequence[str]] = None
    SupportedResponseMIMETypes: Optional[Sequence[str]] = None

class InferenceSpecificationTypeDef(BaseValidatorModel):
    Containers: Sequence[ModelPackageContainerDefinitionTypeDef]
    SupportedTransformInstanceTypes: Optional[Sequence[TransformInstanceTypeType]] = None
    SupportedRealtimeInferenceInstanceTypes: Optional[       Sequence[ProductionVariantInstanceTypeType]     ] = None
    SupportedContentTypes: Optional[Sequence[str]] = None
    SupportedResponseMIMETypes: Optional[Sequence[str]] = None

class SourceAlgorithmSpecificationExtraOutputTypeDef(BaseValidatorModel):
    SourceAlgorithms: List[SourceAlgorithmTypeDef]

class SourceAlgorithmSpecificationOutputTypeDef(BaseValidatorModel):
    SourceAlgorithms: List[SourceAlgorithmTypeDef]

class SourceAlgorithmSpecificationTypeDef(BaseValidatorModel):
    SourceAlgorithms: Sequence[SourceAlgorithmTypeDef]

class MonitoringJobDefinitionExtraOutputTypeDef(BaseValidatorModel):
    MonitoringInputs: List[MonitoringInputExtraOutputTypeDef]
    MonitoringOutputConfig: MonitoringOutputConfigExtraOutputTypeDef
    MonitoringResources: MonitoringResourcesTypeDef
    MonitoringAppSpecification: MonitoringAppSpecificationExtraOutputTypeDef
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigExtraOutputTypeDef] = None

class DescribeDataQualityJobDefinitionResponseTypeDef(BaseValidatorModel):
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

class DescribeModelBiasJobDefinitionResponseTypeDef(BaseValidatorModel):
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

class DescribeModelExplainabilityJobDefinitionResponseTypeDef(BaseValidatorModel):
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

class DescribeModelQualityJobDefinitionResponseTypeDef(BaseValidatorModel):
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

class MonitoringJobDefinitionOutputTypeDef(BaseValidatorModel):
    MonitoringInputs: List[MonitoringInputOutputTypeDef]
    MonitoringOutputConfig: MonitoringOutputConfigOutputTypeDef
    MonitoringResources: MonitoringResourcesTypeDef
    MonitoringAppSpecification: MonitoringAppSpecificationOutputTypeDef
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Environment: Optional[Dict[str, str]] = None
    NetworkConfig: Optional[NetworkConfigOutputTypeDef] = None

class CreateDataQualityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
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

class CreateModelBiasJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
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

class CreateModelExplainabilityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
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

class CreateModelQualityJobDefinitionRequestRequestTypeDef(BaseValidatorModel):
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

class MonitoringJobDefinitionTypeDef(BaseValidatorModel):
    MonitoringInputs: Sequence[MonitoringInputTypeDef]
    MonitoringOutputConfig: MonitoringOutputConfigTypeDef
    MonitoringResources: MonitoringResourcesTypeDef
    MonitoringAppSpecification: MonitoringAppSpecificationTypeDef
    RoleArn: str
    BaselineConfig: Optional[MonitoringBaselineConfigTypeDef] = None
    StoppingCondition: Optional[MonitoringStoppingConditionTypeDef] = None
    Environment: Optional[Mapping[str, str]] = None
    NetworkConfig: Optional[NetworkConfigTypeDef] = None

class ModelPackageValidationProfileExtraOutputTypeDef(BaseValidatorModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionExtraOutputTypeDef

class AlgorithmValidationProfileOutputTypeDef(BaseValidatorModel):
    ProfileName: str
    TrainingJobDefinition: TrainingJobDefinitionOutputTypeDef
    TransformJobDefinition: Optional[TransformJobDefinitionOutputTypeDef] = None

class ModelPackageValidationProfileOutputTypeDef(BaseValidatorModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionOutputTypeDef

class AlgorithmValidationProfileTypeDef(BaseValidatorModel):
    ProfileName: str
    TrainingJobDefinition: TrainingJobDefinitionTypeDef
    TransformJobDefinition: Optional[TransformJobDefinitionTypeDef] = None

class ModelPackageValidationProfileTypeDef(BaseValidatorModel):
    ProfileName: str
    TransformJobDefinition: TransformJobDefinitionTypeDef

class TrialComponentSourceDetailTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None
    TrainingJob: Optional[TrainingJobTypeDef] = None
    ProcessingJob: Optional[ProcessingJobTypeDef] = None
    TransformJob: Optional[TransformJobTypeDef] = None

class CreateHyperParameterTuningJobRequestRequestTypeDef(BaseValidatorModel):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfigTypeDef
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinitionTypeDef] = None
    TrainingJobDefinitions: Optional[       Sequence[HyperParameterTrainingJobDefinitionUnionTypeDef]     ] = None
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Autotune: Optional[AutotuneTypeDef] = None

class GetScalingConfigurationRecommendationResponseTypeDef(BaseValidatorModel):
    InferenceRecommendationsJobName: str
    RecommendationId: str
    EndpointName: str
    TargetCpuUtilizationPerCore: int
    ScalingPolicyObjective: ScalingPolicyObjectiveTypeDef
    Metric: ScalingPolicyMetricTypeDef
    DynamicScalingConfiguration: DynamicScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelInputRequestTypeDef(BaseValidatorModel):
    ModelName: str
    PrimaryContainer: Optional[ContainerDefinitionTypeDef] = None
    Containers: Optional[Sequence[ContainerDefinitionUnionTypeDef]] = None
    InferenceExecutionConfig: Optional[InferenceExecutionConfigTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    EnableNetworkIsolation: Optional[bool] = None

class BatchDescribeModelPackageSummaryTypeDef(BaseValidatorModel):
    ModelPackageGroupName: str
    ModelPackageArn: str
    CreationTime: datetime
    InferenceSpecification: InferenceSpecificationOutputTypeDef
    ModelPackageStatus: ModelPackageStatusType
    ModelPackageVersion: Optional[int] = None
    ModelPackageDescription: Optional[str] = None
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None

class MonitoringScheduleConfigExtraOutputTypeDef(BaseValidatorModel):
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionExtraOutputTypeDef] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class MonitoringScheduleConfigOutputTypeDef(BaseValidatorModel):
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionOutputTypeDef] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class MonitoringScheduleConfigTypeDef(BaseValidatorModel):
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None
    MonitoringJobDefinition: Optional[MonitoringJobDefinitionTypeDef] = None
    MonitoringJobDefinitionName: Optional[str] = None
    MonitoringType: Optional[MonitoringTypeType] = None

class ModelPackageValidationSpecificationExtraOutputTypeDef(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[ModelPackageValidationProfileExtraOutputTypeDef]

class AlgorithmValidationSpecificationOutputTypeDef(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[AlgorithmValidationProfileOutputTypeDef]

class ModelPackageValidationSpecificationOutputTypeDef(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: List[ModelPackageValidationProfileOutputTypeDef]

class AlgorithmValidationSpecificationTypeDef(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: Sequence[AlgorithmValidationProfileTypeDef]

class ModelPackageValidationSpecificationTypeDef(BaseValidatorModel):
    ValidationRole: str
    ValidationProfiles: Sequence[ModelPackageValidationProfileTypeDef]

class TrialComponentTypeDef(BaseValidatorModel):
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

class BatchDescribeModelPackageOutputTypeDef(BaseValidatorModel):
    ModelPackageSummaries: Dict[str, BatchDescribeModelPackageSummaryTypeDef]
    BatchDescribeModelPackageErrorMap: Dict[str, BatchDescribeModelPackageErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelPackageInputRequestTypeDef(BaseValidatorModel):
    ModelPackageArn: str
    ModelApprovalStatus: Optional[ModelApprovalStatusType] = None
    ApprovalDescription: Optional[str] = None
    CustomerMetadataProperties: Optional[Mapping[str, str]] = None
    CustomerMetadataPropertiesToRemove: Optional[Sequence[str]] = None
    AdditionalInferenceSpecificationsToAdd: Optional[       Sequence[AdditionalInferenceSpecificationDefinitionUnionTypeDef]     ] = None
    InferenceSpecification: Optional[InferenceSpecificationTypeDef] = None
    SourceUri: Optional[str] = None
    ModelCard: Optional[ModelPackageModelCardTypeDef] = None

class DescribeMonitoringScheduleResponseTypeDef(BaseValidatorModel):
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

class ModelDashboardMonitoringScheduleTypeDef(BaseValidatorModel):
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

class MonitoringScheduleTypeDef(BaseValidatorModel):
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

class CreateMonitoringScheduleRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateMonitoringScheduleRequestRequestTypeDef(BaseValidatorModel):
    MonitoringScheduleName: str
    MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef

class DescribeAlgorithmOutputTypeDef(BaseValidatorModel):
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

class DescribeModelPackageOutputTypeDef(BaseValidatorModel):
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

class ModelPackageTypeDef(BaseValidatorModel):
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

class CreateAlgorithmInputRequestTypeDef(BaseValidatorModel):
    AlgorithmName: str
    TrainingSpecification: TrainingSpecificationTypeDef
    AlgorithmDescription: Optional[str] = None
    InferenceSpecification: Optional[InferenceSpecificationTypeDef] = None
    ValidationSpecification: Optional[AlgorithmValidationSpecificationTypeDef] = None
    CertifyForMarketplace: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelPackageInputRequestTypeDef(BaseValidatorModel):
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

class ModelDashboardModelTypeDef(BaseValidatorModel):
    Model: Optional[ModelTypeDef] = None
    Endpoints: Optional[List[ModelDashboardEndpointTypeDef]] = None
    LastBatchTransformJob: Optional[TransformJobTypeDef] = None
    MonitoringSchedules: Optional[List[ModelDashboardMonitoringScheduleTypeDef]] = None
    ModelCard: Optional[ModelDashboardModelCardTypeDef] = None

class EndpointTypeDef(BaseValidatorModel):
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

class SearchRecordTypeDef(BaseValidatorModel):
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

class SearchResponseTypeDef(BaseValidatorModel):
    Results: List[SearchRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

