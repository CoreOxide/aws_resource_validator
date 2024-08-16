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
from aws_resource_validator.pydantic_models.kinesisanalyticsv2_constants import *

class CloudWatchLoggingOptionTypeDef(BaseValidatorModel):
    LogStreamARN: str

class CloudWatchLoggingOptionDescriptionTypeDef(BaseValidatorModel):
    LogStreamARN: str
    CloudWatchLoggingOptionId: Optional[str] = None
    RoleARN: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class VpcConfigurationTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class VpcConfigurationDescriptionTypeDef(BaseValidatorModel):
    VpcConfigurationId: str
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]

class ApplicationSnapshotConfigurationDescriptionTypeDef(BaseValidatorModel):
    SnapshotsEnabled: bool

class ApplicationSystemRollbackConfigurationDescriptionTypeDef(BaseValidatorModel):
    RollbackEnabled: bool

class ApplicationSnapshotConfigurationTypeDef(BaseValidatorModel):
    SnapshotsEnabled: bool

class ApplicationSystemRollbackConfigurationTypeDef(BaseValidatorModel):
    RollbackEnabled: bool

class ApplicationSnapshotConfigurationUpdateTypeDef(BaseValidatorModel):
    SnapshotsEnabledUpdate: bool

class ApplicationSystemRollbackConfigurationUpdateTypeDef(BaseValidatorModel):
    RollbackEnabledUpdate: bool

class VpcConfigurationUpdateTypeDef(BaseValidatorModel):
    VpcConfigurationId: str
    SubnetIdUpdates: Optional[Sequence[str]] = None
    SecurityGroupIdUpdates: Optional[Sequence[str]] = None

class ApplicationMaintenanceConfigurationDescriptionTypeDef(BaseValidatorModel):
    ApplicationMaintenanceWindowStartTime: str
    ApplicationMaintenanceWindowEndTime: str

class ApplicationMaintenanceConfigurationUpdateTypeDef(BaseValidatorModel):
    ApplicationMaintenanceWindowStartTimeUpdate: str

class ApplicationVersionChangeDetailsTypeDef(BaseValidatorModel):
    ApplicationVersionUpdatedFrom: int
    ApplicationVersionUpdatedTo: int

class ApplicationOperationInfoTypeDef(BaseValidatorModel):
    Operation: Optional[str] = None
    OperationId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OperationStatus: Optional[OperationStatusType] = None

class ApplicationRestoreConfigurationTypeDef(BaseValidatorModel):
    ApplicationRestoreType: ApplicationRestoreTypeType
    SnapshotName: Optional[str] = None

class ApplicationSummaryTypeDef(BaseValidatorModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationMode: Optional[ApplicationModeType] = None

class ApplicationVersionSummaryTypeDef(BaseValidatorModel):
    ApplicationVersionId: int
    ApplicationStatus: ApplicationStatusType

class CSVMappingParametersTypeDef(BaseValidatorModel):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str

class GlueDataCatalogConfigurationDescriptionTypeDef(BaseValidatorModel):
    DatabaseARN: str

class GlueDataCatalogConfigurationTypeDef(BaseValidatorModel):
    DatabaseARN: str

class GlueDataCatalogConfigurationUpdateTypeDef(BaseValidatorModel):
    DatabaseARNUpdate: str

class CheckpointConfigurationDescriptionTypeDef(BaseValidatorModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    CheckpointingEnabled: Optional[bool] = None
    CheckpointInterval: Optional[int] = None
    MinPauseBetweenCheckpoints: Optional[int] = None

class CheckpointConfigurationTypeDef(BaseValidatorModel):
    ConfigurationType: ConfigurationTypeType
    CheckpointingEnabled: Optional[bool] = None
    CheckpointInterval: Optional[int] = None
    MinPauseBetweenCheckpoints: Optional[int] = None

class CheckpointConfigurationUpdateTypeDef(BaseValidatorModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    CheckpointingEnabledUpdate: Optional[bool] = None
    CheckpointIntervalUpdate: Optional[int] = None
    MinPauseBetweenCheckpointsUpdate: Optional[int] = None

class CloudWatchLoggingOptionUpdateTypeDef(BaseValidatorModel):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: Optional[str] = None

class S3ApplicationCodeLocationDescriptionTypeDef(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ObjectVersion: Optional[str] = None

class S3ContentLocationTypeDef(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ObjectVersion: Optional[str] = None

class S3ContentLocationUpdateTypeDef(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None
    ObjectVersionUpdate: Optional[str] = None

class CreateApplicationPresignedUrlRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    UrlType: UrlTypeType
    SessionExpirationDurationInSeconds: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class CreateApplicationSnapshotRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    SnapshotName: str

class MavenReferenceTypeDef(BaseValidatorModel):
    GroupId: str
    ArtifactId: str
    Version: str

class DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CloudWatchLoggingOptionId: str
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str

class DeleteApplicationOutputRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    OutputId: str

class DeleteApplicationReferenceDataSourceRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceId: str

class DeleteApplicationVpcConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    VpcConfigurationId: str
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class S3ContentBaseLocationDescriptionTypeDef(BaseValidatorModel):
    BucketARN: str
    BasePath: Optional[str] = None

class S3ContentBaseLocationTypeDef(BaseValidatorModel):
    BucketARN: str
    BasePath: Optional[str] = None

class S3ContentBaseLocationUpdateTypeDef(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    BasePathUpdate: Optional[str] = None

class DescribeApplicationOperationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    OperationId: str

class DescribeApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    IncludeAdditionalDetails: Optional[bool] = None

class DescribeApplicationSnapshotRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    SnapshotName: str

class SnapshotDetailsTypeDef(BaseValidatorModel):
    SnapshotName: str
    SnapshotStatus: SnapshotStatusType
    ApplicationVersionId: int
    SnapshotCreationTimestamp: Optional[datetime] = None
    RuntimeEnvironment: Optional[RuntimeEnvironmentType] = None

class DescribeApplicationVersionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    ApplicationVersionId: int

class DestinationSchemaTypeDef(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType

class InputStartingPositionConfigurationTypeDef(BaseValidatorModel):
    InputStartingPosition: Optional[InputStartingPositionType] = None

class S3ConfigurationTypeDef(BaseValidatorModel):
    BucketARN: str
    FileKey: str

class PropertyGroupTypeDef(BaseValidatorModel):
    PropertyGroupId: str
    PropertyMap: Mapping[str, str]

class PropertyGroupOutputTypeDef(BaseValidatorModel):
    PropertyGroupId: str
    PropertyMap: Dict[str, str]

class ErrorInfoTypeDef(BaseValidatorModel):
    ErrorString: Optional[str] = None

class MonitoringConfigurationDescriptionTypeDef(BaseValidatorModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    MetricsLevel: Optional[MetricsLevelType] = None
    LogLevel: Optional[LogLevelType] = None

class ParallelismConfigurationDescriptionTypeDef(BaseValidatorModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    Parallelism: Optional[int] = None
    ParallelismPerKPU: Optional[int] = None
    CurrentParallelism: Optional[int] = None
    AutoScalingEnabled: Optional[bool] = None

class MonitoringConfigurationTypeDef(BaseValidatorModel):
    ConfigurationType: ConfigurationTypeType
    MetricsLevel: Optional[MetricsLevelType] = None
    LogLevel: Optional[LogLevelType] = None

class ParallelismConfigurationTypeDef(BaseValidatorModel):
    ConfigurationType: ConfigurationTypeType
    Parallelism: Optional[int] = None
    ParallelismPerKPU: Optional[int] = None
    AutoScalingEnabled: Optional[bool] = None

class MonitoringConfigurationUpdateTypeDef(BaseValidatorModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    MetricsLevelUpdate: Optional[MetricsLevelType] = None
    LogLevelUpdate: Optional[LogLevelType] = None

class ParallelismConfigurationUpdateTypeDef(BaseValidatorModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    ParallelismUpdate: Optional[int] = None
    ParallelismPerKPUUpdate: Optional[int] = None
    AutoScalingEnabledUpdate: Optional[bool] = None

class FlinkRunConfigurationTypeDef(BaseValidatorModel):
    AllowNonRestoredState: Optional[bool] = None

class InputParallelismTypeDef(BaseValidatorModel):
    Count: Optional[int] = None

class KinesisFirehoseInputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class KinesisStreamsInputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class InputLambdaProcessorDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class InputLambdaProcessorTypeDef(BaseValidatorModel):
    ResourceARN: str

class InputLambdaProcessorUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: str

class InputParallelismUpdateTypeDef(BaseValidatorModel):
    CountUpdate: int

class RecordColumnTypeDef(BaseValidatorModel):
    Name: str
    SqlType: str
    Mapping: Optional[str] = None

class KinesisFirehoseInputTypeDef(BaseValidatorModel):
    ResourceARN: str

class KinesisStreamsInputTypeDef(BaseValidatorModel):
    ResourceARN: str

class KinesisFirehoseInputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: str

class KinesisStreamsInputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: str

class JSONMappingParametersTypeDef(BaseValidatorModel):
    RecordRowPath: str

class KinesisFirehoseOutputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class KinesisFirehoseOutputTypeDef(BaseValidatorModel):
    ResourceARN: str

class KinesisFirehoseOutputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: str

class KinesisStreamsOutputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class KinesisStreamsOutputTypeDef(BaseValidatorModel):
    ResourceARN: str

class KinesisStreamsOutputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: str

class LambdaOutputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class LambdaOutputTypeDef(BaseValidatorModel):
    ResourceARN: str

class LambdaOutputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationOperationsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    OperationStatus: Optional[OperationStatusType] = None

class ListApplicationSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationVersionsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class S3ReferenceDataSourceDescriptionTypeDef(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: Optional[str] = None

class S3ReferenceDataSourceTypeDef(BaseValidatorModel):
    BucketARN: Optional[str] = None
    FileKey: Optional[str] = None

class S3ReferenceDataSourceUpdateTypeDef(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None

class RollbackApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int

class StopApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    Force: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ZeppelinMonitoringConfigurationDescriptionTypeDef(BaseValidatorModel):
    LogLevel: Optional[LogLevelType] = None

class ZeppelinMonitoringConfigurationTypeDef(BaseValidatorModel):
    LogLevel: LogLevelType

class ZeppelinMonitoringConfigurationUpdateTypeDef(BaseValidatorModel):
    LogLevelUpdate: LogLevelType

class AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class AddApplicationCloudWatchLoggingOptionResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescriptionTypeDef]
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationPresignedUrlResponseTypeDef(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationCloudWatchLoggingOptionResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescriptionTypeDef]
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationInputProcessingConfigurationResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationOutputResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationReferenceDataSourceResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationVpcConfigurationResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopApplicationResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationVpcConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    VpcConfiguration: VpcConfigurationTypeDef
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class AddApplicationVpcConfigurationResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    VpcConfigurationDescription: VpcConfigurationDescriptionTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationMaintenanceConfigurationResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationMaintenanceConfigurationDescription: ApplicationMaintenanceConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    ApplicationMaintenanceConfigurationUpdate: ApplicationMaintenanceConfigurationUpdateTypeDef

class ListApplicationOperationsResponseTypeDef(BaseValidatorModel):
    ApplicationOperationInfoList: List[ApplicationOperationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListApplicationVersionsResponseTypeDef(BaseValidatorModel):
    ApplicationVersionSummaries: List[ApplicationVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CatalogConfigurationDescriptionTypeDef(BaseValidatorModel):
    GlueDataCatalogConfigurationDescription: GlueDataCatalogConfigurationDescriptionTypeDef

class CatalogConfigurationTypeDef(BaseValidatorModel):
    GlueDataCatalogConfiguration: GlueDataCatalogConfigurationTypeDef

class CatalogConfigurationUpdateTypeDef(BaseValidatorModel):
    GlueDataCatalogConfigurationUpdate: GlueDataCatalogConfigurationUpdateTypeDef

class CodeContentDescriptionTypeDef(BaseValidatorModel):
    TextContent: Optional[str] = None
    CodeMD5: Optional[str] = None
    CodeSize: Optional[int] = None
    S3ApplicationCodeLocationDescription: Optional[       S3ApplicationCodeLocationDescriptionTypeDef     ] = None

class CodeContentTypeDef(BaseValidatorModel):
    TextContent: Optional[str] = None
    ZipFileContent: Optional[BlobTypeDef] = None
    S3ContentLocation: Optional[S3ContentLocationTypeDef] = None

class CodeContentUpdateTypeDef(BaseValidatorModel):
    TextContentUpdate: Optional[str] = None
    ZipFileContentUpdate: Optional[BlobTypeDef] = None
    S3ContentLocationUpdate: Optional[S3ContentLocationUpdateTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CustomArtifactConfigurationDescriptionTypeDef(BaseValidatorModel):
    ArtifactType: Optional[ArtifactTypeType] = None
    S3ContentLocationDescription: Optional[S3ContentLocationTypeDef] = None
    MavenReferenceDescription: Optional[MavenReferenceTypeDef] = None

class CustomArtifactConfigurationTypeDef(BaseValidatorModel):
    ArtifactType: ArtifactTypeType
    S3ContentLocation: Optional[S3ContentLocationTypeDef] = None
    MavenReference: Optional[MavenReferenceTypeDef] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CreateTimestamp: TimestampTypeDef

class DeleteApplicationSnapshotRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    SnapshotName: str
    SnapshotCreationTimestamp: TimestampTypeDef

class DeployAsApplicationConfigurationDescriptionTypeDef(BaseValidatorModel):
    S3ContentLocationDescription: S3ContentBaseLocationDescriptionTypeDef

class DeployAsApplicationConfigurationTypeDef(BaseValidatorModel):
    S3ContentLocation: S3ContentBaseLocationTypeDef

class DeployAsApplicationConfigurationUpdateTypeDef(BaseValidatorModel):
    S3ContentLocationUpdate: Optional[S3ContentBaseLocationUpdateTypeDef] = None

class DescribeApplicationSnapshotResponseTypeDef(BaseValidatorModel):
    SnapshotDetails: SnapshotDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationSnapshotsResponseTypeDef(BaseValidatorModel):
    SnapshotSummaries: List[SnapshotDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SqlRunConfigurationTypeDef(BaseValidatorModel):
    InputId: str
    InputStartingPositionConfiguration: InputStartingPositionConfigurationTypeDef

class EnvironmentPropertiesTypeDef(BaseValidatorModel):
    PropertyGroups: Sequence[PropertyGroupTypeDef]

class EnvironmentPropertyUpdatesTypeDef(BaseValidatorModel):
    PropertyGroups: Sequence[PropertyGroupTypeDef]

class EnvironmentPropertyDescriptionsTypeDef(BaseValidatorModel):
    PropertyGroupDescriptions: Optional[List[PropertyGroupOutputTypeDef]] = None

class OperationFailureDetailsTypeDef(BaseValidatorModel):
    RollbackOperationId: Optional[str] = None
    ErrorInfo: Optional[ErrorInfoTypeDef] = None

class FlinkApplicationConfigurationDescriptionTypeDef(BaseValidatorModel):
    CheckpointConfigurationDescription: Optional[       CheckpointConfigurationDescriptionTypeDef     ] = None
    MonitoringConfigurationDescription: Optional[       MonitoringConfigurationDescriptionTypeDef     ] = None
    ParallelismConfigurationDescription: Optional[       ParallelismConfigurationDescriptionTypeDef     ] = None
    JobPlanDescription: Optional[str] = None

class FlinkApplicationConfigurationTypeDef(BaseValidatorModel):
    CheckpointConfiguration: Optional[CheckpointConfigurationTypeDef] = None
    MonitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class FlinkApplicationConfigurationUpdateTypeDef(BaseValidatorModel):
    CheckpointConfigurationUpdate: Optional[CheckpointConfigurationUpdateTypeDef] = None
    MonitoringConfigurationUpdate: Optional[MonitoringConfigurationUpdateTypeDef] = None
    ParallelismConfigurationUpdate: Optional[ParallelismConfigurationUpdateTypeDef] = None

class RunConfigurationDescriptionTypeDef(BaseValidatorModel):
    ApplicationRestoreConfigurationDescription: Optional[       ApplicationRestoreConfigurationTypeDef     ] = None
    FlinkRunConfigurationDescription: Optional[FlinkRunConfigurationTypeDef] = None

class RunConfigurationUpdateTypeDef(BaseValidatorModel):
    FlinkRunConfiguration: Optional[FlinkRunConfigurationTypeDef] = None
    ApplicationRestoreConfiguration: Optional[ApplicationRestoreConfigurationTypeDef] = None

class InputProcessingConfigurationDescriptionTypeDef(BaseValidatorModel):
    InputLambdaProcessorDescription: Optional[InputLambdaProcessorDescriptionTypeDef] = None

class InputProcessingConfigurationTypeDef(BaseValidatorModel):
    InputLambdaProcessor: InputLambdaProcessorTypeDef

class InputProcessingConfigurationUpdateTypeDef(BaseValidatorModel):
    InputLambdaProcessorUpdate: InputLambdaProcessorUpdateTypeDef

class MappingParametersTypeDef(BaseValidatorModel):
    JSONMappingParameters: Optional[JSONMappingParametersTypeDef] = None
    CSVMappingParameters: Optional[CSVMappingParametersTypeDef] = None

class OutputDescriptionTypeDef(BaseValidatorModel):
    OutputId: Optional[str] = None
    Name: Optional[str] = None
    KinesisStreamsOutputDescription: Optional[KinesisStreamsOutputDescriptionTypeDef] = None
    KinesisFirehoseOutputDescription: Optional[KinesisFirehoseOutputDescriptionTypeDef] = None
    LambdaOutputDescription: Optional[LambdaOutputDescriptionTypeDef] = None
    DestinationSchema: Optional[DestinationSchemaTypeDef] = None

class OutputTypeDef(BaseValidatorModel):
    Name: str
    DestinationSchema: DestinationSchemaTypeDef
    KinesisStreamsOutput: Optional[KinesisStreamsOutputTypeDef] = None
    KinesisFirehoseOutput: Optional[KinesisFirehoseOutputTypeDef] = None
    LambdaOutput: Optional[LambdaOutputTypeDef] = None

class OutputUpdateTypeDef(BaseValidatorModel):
    OutputId: str
    NameUpdate: Optional[str] = None
    KinesisStreamsOutputUpdate: Optional[KinesisStreamsOutputUpdateTypeDef] = None
    KinesisFirehoseOutputUpdate: Optional[KinesisFirehoseOutputUpdateTypeDef] = None
    LambdaOutputUpdate: Optional[LambdaOutputUpdateTypeDef] = None
    DestinationSchemaUpdate: Optional[DestinationSchemaTypeDef] = None

class ListApplicationOperationsRequestListApplicationOperationsPaginateTypeDef(BaseValidatorModel):
    ApplicationName: str
    Operation: Optional[str] = None
    OperationStatus: Optional[OperationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationSnapshotsRequestListApplicationSnapshotsPaginateTypeDef(BaseValidatorModel):
    ApplicationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef(BaseValidatorModel):
    ApplicationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ApplicationCodeConfigurationDescriptionTypeDef(BaseValidatorModel):
    CodeContentType: CodeContentTypeType
    CodeContentDescription: Optional[CodeContentDescriptionTypeDef] = None

class ApplicationCodeConfigurationTypeDef(BaseValidatorModel):
    CodeContentType: CodeContentTypeType
    CodeContent: Optional[CodeContentTypeDef] = None

class ApplicationCodeConfigurationUpdateTypeDef(BaseValidatorModel):
    CodeContentTypeUpdate: Optional[CodeContentTypeType] = None
    CodeContentUpdate: Optional[CodeContentUpdateTypeDef] = None

class ZeppelinApplicationConfigurationDescriptionTypeDef(BaseValidatorModel):
    MonitoringConfigurationDescription: ZeppelinMonitoringConfigurationDescriptionTypeDef
    CatalogConfigurationDescription: Optional[CatalogConfigurationDescriptionTypeDef] = None
    DeployAsApplicationConfigurationDescription: Optional[       DeployAsApplicationConfigurationDescriptionTypeDef     ] = None
    CustomArtifactsConfigurationDescription: Optional[       List[CustomArtifactConfigurationDescriptionTypeDef]     ] = None

class ZeppelinApplicationConfigurationTypeDef(BaseValidatorModel):
    MonitoringConfiguration: Optional[ZeppelinMonitoringConfigurationTypeDef] = None
    CatalogConfiguration: Optional[CatalogConfigurationTypeDef] = None
    DeployAsApplicationConfiguration: Optional[DeployAsApplicationConfigurationTypeDef] = None
    CustomArtifactsConfiguration: Optional[Sequence[CustomArtifactConfigurationTypeDef]] = None

class ZeppelinApplicationConfigurationUpdateTypeDef(BaseValidatorModel):
    MonitoringConfigurationUpdate: Optional[ZeppelinMonitoringConfigurationUpdateTypeDef] = None
    CatalogConfigurationUpdate: Optional[CatalogConfigurationUpdateTypeDef] = None
    DeployAsApplicationConfigurationUpdate: Optional[       DeployAsApplicationConfigurationUpdateTypeDef     ] = None
    CustomArtifactsConfigurationUpdate: Optional[       Sequence[CustomArtifactConfigurationTypeDef]     ] = None

class RunConfigurationTypeDef(BaseValidatorModel):
    FlinkRunConfiguration: Optional[FlinkRunConfigurationTypeDef] = None
    SqlRunConfigurations: Optional[Sequence[SqlRunConfigurationTypeDef]] = None
    ApplicationRestoreConfiguration: Optional[ApplicationRestoreConfigurationTypeDef] = None

class ApplicationOperationInfoDetailsTypeDef(BaseValidatorModel):
    Operation: str
    StartTime: datetime
    EndTime: datetime
    OperationStatus: OperationStatusType
    ApplicationVersionChangeDetails: Optional[ApplicationVersionChangeDetailsTypeDef] = None
    OperationFailureDetails: Optional[OperationFailureDetailsTypeDef] = None

class AddApplicationInputProcessingConfigurationResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    InputId: str
    InputProcessingConfigurationDescription: InputProcessingConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationInputProcessingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfigurationTypeDef

class DiscoverInputSchemaRequestRequestTypeDef(BaseValidatorModel):
    ServiceExecutionRole: str
    ResourceARN: Optional[str] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None
    S3Configuration: Optional[S3ConfigurationTypeDef] = None
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None

class RecordFormatTypeDef(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: Optional[MappingParametersTypeDef] = None

class AddApplicationOutputResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    OutputDescriptions: List[OutputDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationOutputRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: OutputTypeDef

class StartApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    RunConfiguration: Optional[RunConfigurationTypeDef] = None

class DescribeApplicationOperationResponseTypeDef(BaseValidatorModel):
    ApplicationOperationInfoDetails: ApplicationOperationInfoDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InputSchemaUpdateTypeDef(BaseValidatorModel):
    RecordFormatUpdate: Optional[RecordFormatTypeDef] = None
    RecordEncodingUpdate: Optional[str] = None
    RecordColumnUpdates: Optional[Sequence[RecordColumnTypeDef]] = None

class SourceSchemaOutputTypeDef(BaseValidatorModel):
    RecordFormat: RecordFormatTypeDef
    RecordColumns: List[RecordColumnTypeDef]
    RecordEncoding: Optional[str] = None

class SourceSchemaTypeDef(BaseValidatorModel):
    RecordFormat: RecordFormatTypeDef
    RecordColumns: Sequence[RecordColumnTypeDef]
    RecordEncoding: Optional[str] = None

class InputUpdateTypeDef(BaseValidatorModel):
    InputId: str
    NamePrefixUpdate: Optional[str] = None
    InputProcessingConfigurationUpdate: Optional[       InputProcessingConfigurationUpdateTypeDef     ] = None
    KinesisStreamsInputUpdate: Optional[KinesisStreamsInputUpdateTypeDef] = None
    KinesisFirehoseInputUpdate: Optional[KinesisFirehoseInputUpdateTypeDef] = None
    InputSchemaUpdate: Optional[InputSchemaUpdateTypeDef] = None
    InputParallelismUpdate: Optional[InputParallelismUpdateTypeDef] = None

class DiscoverInputSchemaResponseTypeDef(BaseValidatorModel):
    InputSchema: SourceSchemaOutputTypeDef
    ParsedInputRecords: List[List[str]]
    ProcessedInputRecords: List[str]
    RawInputRecords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class InputDescriptionTypeDef(BaseValidatorModel):
    InputId: Optional[str] = None
    NamePrefix: Optional[str] = None
    InAppStreamNames: Optional[List[str]] = None
    InputProcessingConfigurationDescription: Optional[       InputProcessingConfigurationDescriptionTypeDef     ] = None
    KinesisStreamsInputDescription: Optional[KinesisStreamsInputDescriptionTypeDef] = None
    KinesisFirehoseInputDescription: Optional[KinesisFirehoseInputDescriptionTypeDef] = None
    InputSchema: Optional[SourceSchemaOutputTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None

class ReferenceDataSourceDescriptionTypeDef(BaseValidatorModel):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: S3ReferenceDataSourceDescriptionTypeDef
    ReferenceSchema: Optional[SourceSchemaOutputTypeDef] = None

class InputTypeDef(BaseValidatorModel):
    NamePrefix: str
    InputSchema: SourceSchemaTypeDef
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None
    KinesisStreamsInput: Optional[KinesisStreamsInputTypeDef] = None
    KinesisFirehoseInput: Optional[KinesisFirehoseInputTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None

class ReferenceDataSourceTypeDef(BaseValidatorModel):
    TableName: str
    ReferenceSchema: SourceSchemaTypeDef
    S3ReferenceDataSource: Optional[S3ReferenceDataSourceTypeDef] = None

class ReferenceDataSourceUpdateTypeDef(BaseValidatorModel):
    ReferenceId: str
    TableNameUpdate: Optional[str] = None
    S3ReferenceDataSourceUpdate: Optional[S3ReferenceDataSourceUpdateTypeDef] = None
    ReferenceSchemaUpdate: Optional[SourceSchemaTypeDef] = None

class AddApplicationInputResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    InputDescriptions: List[InputDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationReferenceDataSourceResponseTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ReferenceDataSourceDescriptions: List[ReferenceDataSourceDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SqlApplicationConfigurationDescriptionTypeDef(BaseValidatorModel):
    InputDescriptions: Optional[List[InputDescriptionTypeDef]] = None
    OutputDescriptions: Optional[List[OutputDescriptionTypeDef]] = None
    ReferenceDataSourceDescriptions: Optional[List[ReferenceDataSourceDescriptionTypeDef]] = None

class AddApplicationInputRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: InputTypeDef

class AddApplicationReferenceDataSourceRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSourceTypeDef

class SqlApplicationConfigurationTypeDef(BaseValidatorModel):
    Inputs: Optional[Sequence[InputTypeDef]] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None
    ReferenceDataSources: Optional[Sequence[ReferenceDataSourceTypeDef]] = None

class SqlApplicationConfigurationUpdateTypeDef(BaseValidatorModel):
    InputUpdates: Optional[Sequence[InputUpdateTypeDef]] = None
    OutputUpdates: Optional[Sequence[OutputUpdateTypeDef]] = None
    ReferenceDataSourceUpdates: Optional[Sequence[ReferenceDataSourceUpdateTypeDef]] = None

class ApplicationConfigurationDescriptionTypeDef(BaseValidatorModel):
    SqlApplicationConfigurationDescription: Optional[       SqlApplicationConfigurationDescriptionTypeDef     ] = None
    ApplicationCodeConfigurationDescription: Optional[       ApplicationCodeConfigurationDescriptionTypeDef     ] = None
    RunConfigurationDescription: Optional[RunConfigurationDescriptionTypeDef] = None
    FlinkApplicationConfigurationDescription: Optional[       FlinkApplicationConfigurationDescriptionTypeDef     ] = None
    EnvironmentPropertyDescriptions: Optional[EnvironmentPropertyDescriptionsTypeDef] = None
    ApplicationSnapshotConfigurationDescription: Optional[       ApplicationSnapshotConfigurationDescriptionTypeDef     ] = None
    ApplicationSystemRollbackConfigurationDescription: Optional[       ApplicationSystemRollbackConfigurationDescriptionTypeDef     ] = None
    VpcConfigurationDescriptions: Optional[List[VpcConfigurationDescriptionTypeDef]] = None
    ZeppelinApplicationConfigurationDescription: Optional[       ZeppelinApplicationConfigurationDescriptionTypeDef     ] = None

class ApplicationConfigurationTypeDef(BaseValidatorModel):
    SqlApplicationConfiguration: Optional[SqlApplicationConfigurationTypeDef] = None
    FlinkApplicationConfiguration: Optional[FlinkApplicationConfigurationTypeDef] = None
    EnvironmentProperties: Optional[EnvironmentPropertiesTypeDef] = None
    ApplicationCodeConfiguration: Optional[ApplicationCodeConfigurationTypeDef] = None
    ApplicationSnapshotConfiguration: Optional[ApplicationSnapshotConfigurationTypeDef] = None
    ApplicationSystemRollbackConfiguration: Optional[       ApplicationSystemRollbackConfigurationTypeDef     ] = None
    VpcConfigurations: Optional[Sequence[VpcConfigurationTypeDef]] = None
    ZeppelinApplicationConfiguration: Optional[ZeppelinApplicationConfigurationTypeDef] = None

class ApplicationConfigurationUpdateTypeDef(BaseValidatorModel):
    SqlApplicationConfigurationUpdate: Optional[SqlApplicationConfigurationUpdateTypeDef] = None
    ApplicationCodeConfigurationUpdate: Optional[       ApplicationCodeConfigurationUpdateTypeDef     ] = None
    FlinkApplicationConfigurationUpdate: Optional[       FlinkApplicationConfigurationUpdateTypeDef     ] = None
    EnvironmentPropertyUpdates: Optional[EnvironmentPropertyUpdatesTypeDef] = None
    ApplicationSnapshotConfigurationUpdate: Optional[       ApplicationSnapshotConfigurationUpdateTypeDef     ] = None
    ApplicationSystemRollbackConfigurationUpdate: Optional[       ApplicationSystemRollbackConfigurationUpdateTypeDef     ] = None
    VpcConfigurationUpdates: Optional[Sequence[VpcConfigurationUpdateTypeDef]] = None
    ZeppelinApplicationConfigurationUpdate: Optional[       ZeppelinApplicationConfigurationUpdateTypeDef     ] = None

class ApplicationDetailTypeDef(BaseValidatorModel):
    ApplicationARN: str
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    ApplicationDescription: Optional[str] = None
    ServiceExecutionRole: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    ApplicationConfigurationDescription: Optional[       ApplicationConfigurationDescriptionTypeDef     ] = None
    CloudWatchLoggingOptionDescriptions: Optional[       List[CloudWatchLoggingOptionDescriptionTypeDef]     ] = None
    ApplicationMaintenanceConfigurationDescription: Optional[       ApplicationMaintenanceConfigurationDescriptionTypeDef     ] = None
    ApplicationVersionUpdatedFrom: Optional[int] = None
    ApplicationVersionRolledBackFrom: Optional[int] = None
    ApplicationVersionCreateTimestamp: Optional[datetime] = None
    ConditionalToken: Optional[str] = None
    ApplicationVersionRolledBackTo: Optional[int] = None
    ApplicationMode: Optional[ApplicationModeType] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ServiceExecutionRole: str
    ApplicationDescription: Optional[str] = None
    ApplicationConfiguration: Optional[ApplicationConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[Sequence[CloudWatchLoggingOptionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ApplicationMode: Optional[ApplicationModeType] = None

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: Optional[int] = None
    ApplicationConfigurationUpdate: Optional[ApplicationConfigurationUpdateTypeDef] = None
    ServiceExecutionRoleUpdate: Optional[str] = None
    RunConfigurationUpdate: Optional[RunConfigurationUpdateTypeDef] = None
    CloudWatchLoggingOptionUpdates: Optional[       Sequence[CloudWatchLoggingOptionUpdateTypeDef]     ] = None
    ConditionalToken: Optional[str] = None
    RuntimeEnvironmentUpdate: Optional[RuntimeEnvironmentType] = None

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationVersionResponseTypeDef(BaseValidatorModel):
    ApplicationVersionDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationDetail: ApplicationDetailTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationDetail: ApplicationDetailTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

