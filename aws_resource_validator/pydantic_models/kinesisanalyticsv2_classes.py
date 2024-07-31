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
from aws_resource_validator.pydantic_models.kinesisanalyticsv2_constants import *

class CloudWatchLoggingOptionTypeDef(BaseModel):
    LogStreamARN: str

class CloudWatchLoggingOptionDescriptionTypeDef(BaseModel):
    LogStreamARN: str
    CloudWatchLoggingOptionId: Optional[str] = None
    RoleARN: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class VpcConfigurationTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class VpcConfigurationDescriptionTypeDef(BaseModel):
    VpcConfigurationId: str
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]

class ApplicationSnapshotConfigurationDescriptionTypeDef(BaseModel):
    SnapshotsEnabled: bool

class ApplicationSystemRollbackConfigurationDescriptionTypeDef(BaseModel):
    RollbackEnabled: bool

class ApplicationSnapshotConfigurationTypeDef(BaseModel):
    SnapshotsEnabled: bool

class ApplicationSystemRollbackConfigurationTypeDef(BaseModel):
    RollbackEnabled: bool

class ApplicationSnapshotConfigurationUpdateTypeDef(BaseModel):
    SnapshotsEnabledUpdate: bool

class ApplicationSystemRollbackConfigurationUpdateTypeDef(BaseModel):
    RollbackEnabledUpdate: bool

class VpcConfigurationUpdateTypeDef(BaseModel):
    VpcConfigurationId: str
    SubnetIdUpdates: Optional[Sequence[str]] = None
    SecurityGroupIdUpdates: Optional[Sequence[str]] = None

class ApplicationMaintenanceConfigurationDescriptionTypeDef(BaseModel):
    ApplicationMaintenanceWindowStartTime: str
    ApplicationMaintenanceWindowEndTime: str

class ApplicationMaintenanceConfigurationUpdateTypeDef(BaseModel):
    ApplicationMaintenanceWindowStartTimeUpdate: str

class ApplicationVersionChangeDetailsTypeDef(BaseModel):
    ApplicationVersionUpdatedFrom: int
    ApplicationVersionUpdatedTo: int

class ApplicationOperationInfoTypeDef(BaseModel):
    Operation: Optional[str] = None
    OperationId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OperationStatus: Optional[OperationStatusType] = None

class ApplicationRestoreConfigurationTypeDef(BaseModel):
    ApplicationRestoreType: ApplicationRestoreTypeType
    SnapshotName: Optional[str] = None

class ApplicationSummaryTypeDef(BaseModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationMode: Optional[ApplicationModeType] = None

class ApplicationVersionSummaryTypeDef(BaseModel):
    ApplicationVersionId: int
    ApplicationStatus: ApplicationStatusType

class CSVMappingParametersTypeDef(BaseModel):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str

class GlueDataCatalogConfigurationDescriptionTypeDef(BaseModel):
    DatabaseARN: str

class GlueDataCatalogConfigurationTypeDef(BaseModel):
    DatabaseARN: str

class GlueDataCatalogConfigurationUpdateTypeDef(BaseModel):
    DatabaseARNUpdate: str

class CheckpointConfigurationDescriptionTypeDef(BaseModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    CheckpointingEnabled: Optional[bool] = None
    CheckpointInterval: Optional[int] = None
    MinPauseBetweenCheckpoints: Optional[int] = None

class CheckpointConfigurationTypeDef(BaseModel):
    ConfigurationType: ConfigurationTypeType
    CheckpointingEnabled: Optional[bool] = None
    CheckpointInterval: Optional[int] = None
    MinPauseBetweenCheckpoints: Optional[int] = None

class CheckpointConfigurationUpdateTypeDef(BaseModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    CheckpointingEnabledUpdate: Optional[bool] = None
    CheckpointIntervalUpdate: Optional[int] = None
    MinPauseBetweenCheckpointsUpdate: Optional[int] = None

class CloudWatchLoggingOptionUpdateTypeDef(BaseModel):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: Optional[str] = None

class S3ApplicationCodeLocationDescriptionTypeDef(BaseModel):
    BucketARN: str
    FileKey: str
    ObjectVersion: Optional[str] = None

class S3ContentLocationTypeDef(BaseModel):
    BucketARN: str
    FileKey: str
    ObjectVersion: Optional[str] = None

class S3ContentLocationUpdateTypeDef(BaseModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None
    ObjectVersionUpdate: Optional[str] = None

class CreateApplicationPresignedUrlRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    UrlType: UrlTypeType
    SessionExpirationDurationInSeconds: Optional[int] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class CreateApplicationSnapshotRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    SnapshotName: str

class MavenReferenceTypeDef(BaseModel):
    GroupId: str
    ArtifactId: str
    Version: str

class DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CloudWatchLoggingOptionId: str
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str

class DeleteApplicationOutputRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    OutputId: str

class DeleteApplicationReferenceDataSourceRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceId: str

class DeleteApplicationVpcConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    VpcConfigurationId: str
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class S3ContentBaseLocationDescriptionTypeDef(BaseModel):
    BucketARN: str
    BasePath: Optional[str] = None

class S3ContentBaseLocationTypeDef(BaseModel):
    BucketARN: str
    BasePath: Optional[str] = None

class S3ContentBaseLocationUpdateTypeDef(BaseModel):
    BucketARNUpdate: Optional[str] = None
    BasePathUpdate: Optional[str] = None

class DescribeApplicationOperationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    OperationId: str

class DescribeApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    IncludeAdditionalDetails: Optional[bool] = None

class DescribeApplicationSnapshotRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    SnapshotName: str

class SnapshotDetailsTypeDef(BaseModel):
    SnapshotName: str
    SnapshotStatus: SnapshotStatusType
    ApplicationVersionId: int
    SnapshotCreationTimestamp: Optional[datetime] = None
    RuntimeEnvironment: Optional[RuntimeEnvironmentType] = None

class DescribeApplicationVersionRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    ApplicationVersionId: int

class DestinationSchemaTypeDef(BaseModel):
    RecordFormatType: RecordFormatTypeType

class InputStartingPositionConfigurationTypeDef(BaseModel):
    InputStartingPosition: Optional[InputStartingPositionType] = None

class S3ConfigurationTypeDef(BaseModel):
    BucketARN: str
    FileKey: str

class PropertyGroupTypeDef(BaseModel):
    PropertyGroupId: str
    PropertyMap: Mapping[str, str]

class PropertyGroupOutputTypeDef(BaseModel):
    PropertyGroupId: str
    PropertyMap: Dict[str, str]

class ErrorInfoTypeDef(BaseModel):
    ErrorString: Optional[str] = None

class MonitoringConfigurationDescriptionTypeDef(BaseModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    MetricsLevel: Optional[MetricsLevelType] = None
    LogLevel: Optional[LogLevelType] = None

class ParallelismConfigurationDescriptionTypeDef(BaseModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    Parallelism: Optional[int] = None
    ParallelismPerKPU: Optional[int] = None
    CurrentParallelism: Optional[int] = None
    AutoScalingEnabled: Optional[bool] = None

class MonitoringConfigurationTypeDef(BaseModel):
    ConfigurationType: ConfigurationTypeType
    MetricsLevel: Optional[MetricsLevelType] = None
    LogLevel: Optional[LogLevelType] = None

class ParallelismConfigurationTypeDef(BaseModel):
    ConfigurationType: ConfigurationTypeType
    Parallelism: Optional[int] = None
    ParallelismPerKPU: Optional[int] = None
    AutoScalingEnabled: Optional[bool] = None

class MonitoringConfigurationUpdateTypeDef(BaseModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    MetricsLevelUpdate: Optional[MetricsLevelType] = None
    LogLevelUpdate: Optional[LogLevelType] = None

class ParallelismConfigurationUpdateTypeDef(BaseModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    ParallelismUpdate: Optional[int] = None
    ParallelismPerKPUUpdate: Optional[int] = None
    AutoScalingEnabledUpdate: Optional[bool] = None

class FlinkRunConfigurationTypeDef(BaseModel):
    AllowNonRestoredState: Optional[bool] = None

class InputParallelismTypeDef(BaseModel):
    Count: Optional[int] = None

class KinesisFirehoseInputDescriptionTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class KinesisStreamsInputDescriptionTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class InputLambdaProcessorDescriptionTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class InputLambdaProcessorTypeDef(BaseModel):
    ResourceARN: str

class InputLambdaProcessorUpdateTypeDef(BaseModel):
    ResourceARNUpdate: str

class InputParallelismUpdateTypeDef(BaseModel):
    CountUpdate: int

class RecordColumnTypeDef(BaseModel):
    Name: str
    SqlType: str
    Mapping: Optional[str] = None

class KinesisFirehoseInputTypeDef(BaseModel):
    ResourceARN: str

class KinesisStreamsInputTypeDef(BaseModel):
    ResourceARN: str

class KinesisFirehoseInputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: str

class KinesisStreamsInputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: str

class JSONMappingParametersTypeDef(BaseModel):
    RecordRowPath: str

class KinesisFirehoseOutputDescriptionTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class KinesisFirehoseOutputTypeDef(BaseModel):
    ResourceARN: str

class KinesisFirehoseOutputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: str

class KinesisStreamsOutputDescriptionTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class KinesisStreamsOutputTypeDef(BaseModel):
    ResourceARN: str

class KinesisStreamsOutputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: str

class LambdaOutputDescriptionTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: Optional[str] = None

class LambdaOutputTypeDef(BaseModel):
    ResourceARN: str

class LambdaOutputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationOperationsRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    OperationStatus: Optional[OperationStatusType] = None

class ListApplicationSnapshotsRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationVersionsRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class S3ReferenceDataSourceDescriptionTypeDef(BaseModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: Optional[str] = None

class S3ReferenceDataSourceTypeDef(BaseModel):
    BucketARN: Optional[str] = None
    FileKey: Optional[str] = None

class S3ReferenceDataSourceUpdateTypeDef(BaseModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None

class RollbackApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int

class StopApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    Force: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ZeppelinMonitoringConfigurationDescriptionTypeDef(BaseModel):
    LogLevel: Optional[LogLevelType] = None

class ZeppelinMonitoringConfigurationTypeDef(BaseModel):
    LogLevel: LogLevelType

class ZeppelinMonitoringConfigurationUpdateTypeDef(BaseModel):
    LogLevelUpdate: LogLevelType

class AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class AddApplicationCloudWatchLoggingOptionResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescriptionTypeDef]
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationPresignedUrlResponseTypeDef(BaseModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationCloudWatchLoggingOptionResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescriptionTypeDef]
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationInputProcessingConfigurationResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationOutputResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationReferenceDataSourceResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationVpcConfigurationResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopApplicationResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationVpcConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    VpcConfiguration: VpcConfigurationTypeDef
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None

class AddApplicationVpcConfigurationResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    VpcConfigurationDescription: VpcConfigurationDescriptionTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationMaintenanceConfigurationResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationMaintenanceConfigurationDescription: ApplicationMaintenanceConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    ApplicationMaintenanceConfigurationUpdate: ApplicationMaintenanceConfigurationUpdateTypeDef

class ListApplicationOperationsResponseTypeDef(BaseModel):
    ApplicationOperationInfoList: List[ApplicationOperationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListApplicationsResponseTypeDef(BaseModel):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListApplicationVersionsResponseTypeDef(BaseModel):
    ApplicationVersionSummaries: List[ApplicationVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CatalogConfigurationDescriptionTypeDef(BaseModel):
    GlueDataCatalogConfigurationDescription: GlueDataCatalogConfigurationDescriptionTypeDef

class CatalogConfigurationTypeDef(BaseModel):
    GlueDataCatalogConfiguration: GlueDataCatalogConfigurationTypeDef

class CatalogConfigurationUpdateTypeDef(BaseModel):
    GlueDataCatalogConfigurationUpdate: GlueDataCatalogConfigurationUpdateTypeDef

class CodeContentDescriptionTypeDef(BaseModel):
    TextContent: Optional[str] = None
    CodeMD5: Optional[str] = None
    CodeSize: Optional[int] = None
    S3ApplicationCodeLocationDescription: Optional[       S3ApplicationCodeLocationDescriptionTypeDef     ] = None

class CodeContentTypeDef(BaseModel):
    TextContent: Optional[str] = None
    ZipFileContent: Optional[BlobTypeDef] = None
    S3ContentLocation: Optional[S3ContentLocationTypeDef] = None

class CodeContentUpdateTypeDef(BaseModel):
    TextContentUpdate: Optional[str] = None
    ZipFileContentUpdate: Optional[BlobTypeDef] = None
    S3ContentLocationUpdate: Optional[S3ContentLocationUpdateTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CustomArtifactConfigurationDescriptionTypeDef(BaseModel):
    ArtifactType: Optional[ArtifactTypeType] = None
    S3ContentLocationDescription: Optional[S3ContentLocationTypeDef] = None
    MavenReferenceDescription: Optional[MavenReferenceTypeDef] = None

class CustomArtifactConfigurationTypeDef(BaseModel):
    ArtifactType: ArtifactTypeType
    S3ContentLocation: Optional[S3ContentLocationTypeDef] = None
    MavenReference: Optional[MavenReferenceTypeDef] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CreateTimestamp: TimestampTypeDef

class DeleteApplicationSnapshotRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    SnapshotName: str
    SnapshotCreationTimestamp: TimestampTypeDef

class DeployAsApplicationConfigurationDescriptionTypeDef(BaseModel):
    S3ContentLocationDescription: S3ContentBaseLocationDescriptionTypeDef

class DeployAsApplicationConfigurationTypeDef(BaseModel):
    S3ContentLocation: S3ContentBaseLocationTypeDef

class DeployAsApplicationConfigurationUpdateTypeDef(BaseModel):
    S3ContentLocationUpdate: Optional[S3ContentBaseLocationUpdateTypeDef] = None

class DescribeApplicationSnapshotResponseTypeDef(BaseModel):
    SnapshotDetails: SnapshotDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationSnapshotsResponseTypeDef(BaseModel):
    SnapshotSummaries: List[SnapshotDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SqlRunConfigurationTypeDef(BaseModel):
    InputId: str
    InputStartingPositionConfiguration: InputStartingPositionConfigurationTypeDef

class EnvironmentPropertiesTypeDef(BaseModel):
    PropertyGroups: Sequence[PropertyGroupTypeDef]

class EnvironmentPropertyUpdatesTypeDef(BaseModel):
    PropertyGroups: Sequence[PropertyGroupTypeDef]

class EnvironmentPropertyDescriptionsTypeDef(BaseModel):
    PropertyGroupDescriptions: Optional[List[PropertyGroupOutputTypeDef]] = None

class OperationFailureDetailsTypeDef(BaseModel):
    RollbackOperationId: Optional[str] = None
    ErrorInfo: Optional[ErrorInfoTypeDef] = None

class FlinkApplicationConfigurationDescriptionTypeDef(BaseModel):
    CheckpointConfigurationDescription: Optional[       CheckpointConfigurationDescriptionTypeDef     ] = None
    MonitoringConfigurationDescription: Optional[       MonitoringConfigurationDescriptionTypeDef     ] = None
    ParallelismConfigurationDescription: Optional[       ParallelismConfigurationDescriptionTypeDef     ] = None
    JobPlanDescription: Optional[str] = None

class FlinkApplicationConfigurationTypeDef(BaseModel):
    CheckpointConfiguration: Optional[CheckpointConfigurationTypeDef] = None
    MonitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None
    ParallelismConfiguration: Optional[ParallelismConfigurationTypeDef] = None

class FlinkApplicationConfigurationUpdateTypeDef(BaseModel):
    CheckpointConfigurationUpdate: Optional[CheckpointConfigurationUpdateTypeDef] = None
    MonitoringConfigurationUpdate: Optional[MonitoringConfigurationUpdateTypeDef] = None
    ParallelismConfigurationUpdate: Optional[ParallelismConfigurationUpdateTypeDef] = None

class RunConfigurationDescriptionTypeDef(BaseModel):
    ApplicationRestoreConfigurationDescription: Optional[       ApplicationRestoreConfigurationTypeDef     ] = None
    FlinkRunConfigurationDescription: Optional[FlinkRunConfigurationTypeDef] = None

class RunConfigurationUpdateTypeDef(BaseModel):
    FlinkRunConfiguration: Optional[FlinkRunConfigurationTypeDef] = None
    ApplicationRestoreConfiguration: Optional[ApplicationRestoreConfigurationTypeDef] = None

class InputProcessingConfigurationDescriptionTypeDef(BaseModel):
    InputLambdaProcessorDescription: Optional[InputLambdaProcessorDescriptionTypeDef] = None

class InputProcessingConfigurationTypeDef(BaseModel):
    InputLambdaProcessor: InputLambdaProcessorTypeDef

class InputProcessingConfigurationUpdateTypeDef(BaseModel):
    InputLambdaProcessorUpdate: InputLambdaProcessorUpdateTypeDef

class MappingParametersTypeDef(BaseModel):
    JSONMappingParameters: Optional[JSONMappingParametersTypeDef] = None
    CSVMappingParameters: Optional[CSVMappingParametersTypeDef] = None

class OutputDescriptionTypeDef(BaseModel):
    OutputId: Optional[str] = None
    Name: Optional[str] = None
    KinesisStreamsOutputDescription: Optional[KinesisStreamsOutputDescriptionTypeDef] = None
    KinesisFirehoseOutputDescription: Optional[KinesisFirehoseOutputDescriptionTypeDef] = None
    LambdaOutputDescription: Optional[LambdaOutputDescriptionTypeDef] = None
    DestinationSchema: Optional[DestinationSchemaTypeDef] = None

class OutputTypeDef(BaseModel):
    Name: str
    DestinationSchema: DestinationSchemaTypeDef
    KinesisStreamsOutput: Optional[KinesisStreamsOutputTypeDef] = None
    KinesisFirehoseOutput: Optional[KinesisFirehoseOutputTypeDef] = None
    LambdaOutput: Optional[LambdaOutputTypeDef] = None

class OutputUpdateTypeDef(BaseModel):
    OutputId: str
    NameUpdate: Optional[str] = None
    KinesisStreamsOutputUpdate: Optional[KinesisStreamsOutputUpdateTypeDef] = None
    KinesisFirehoseOutputUpdate: Optional[KinesisFirehoseOutputUpdateTypeDef] = None
    LambdaOutputUpdate: Optional[LambdaOutputUpdateTypeDef] = None
    DestinationSchemaUpdate: Optional[DestinationSchemaTypeDef] = None

class ListApplicationOperationsRequestListApplicationOperationsPaginateTypeDef(BaseModel):
    ApplicationName: str
    Operation: Optional[str] = None
    OperationStatus: Optional[OperationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationSnapshotsRequestListApplicationSnapshotsPaginateTypeDef(BaseModel):
    ApplicationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef(BaseModel):
    ApplicationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ApplicationCodeConfigurationDescriptionTypeDef(BaseModel):
    CodeContentType: CodeContentTypeType
    CodeContentDescription: Optional[CodeContentDescriptionTypeDef] = None

class ApplicationCodeConfigurationTypeDef(BaseModel):
    CodeContentType: CodeContentTypeType
    CodeContent: Optional[CodeContentTypeDef] = None

class ApplicationCodeConfigurationUpdateTypeDef(BaseModel):
    CodeContentTypeUpdate: Optional[CodeContentTypeType] = None
    CodeContentUpdate: Optional[CodeContentUpdateTypeDef] = None

class ZeppelinApplicationConfigurationDescriptionTypeDef(BaseModel):
    MonitoringConfigurationDescription: ZeppelinMonitoringConfigurationDescriptionTypeDef
    CatalogConfigurationDescription: Optional[CatalogConfigurationDescriptionTypeDef] = None
    DeployAsApplicationConfigurationDescription: Optional[       DeployAsApplicationConfigurationDescriptionTypeDef     ] = None
    CustomArtifactsConfigurationDescription: Optional[       List[CustomArtifactConfigurationDescriptionTypeDef]     ] = None

class ZeppelinApplicationConfigurationTypeDef(BaseModel):
    MonitoringConfiguration: Optional[ZeppelinMonitoringConfigurationTypeDef] = None
    CatalogConfiguration: Optional[CatalogConfigurationTypeDef] = None
    DeployAsApplicationConfiguration: Optional[DeployAsApplicationConfigurationTypeDef] = None
    CustomArtifactsConfiguration: Optional[Sequence[CustomArtifactConfigurationTypeDef]] = None

class ZeppelinApplicationConfigurationUpdateTypeDef(BaseModel):
    MonitoringConfigurationUpdate: Optional[ZeppelinMonitoringConfigurationUpdateTypeDef] = None
    CatalogConfigurationUpdate: Optional[CatalogConfigurationUpdateTypeDef] = None
    DeployAsApplicationConfigurationUpdate: Optional[       DeployAsApplicationConfigurationUpdateTypeDef     ] = None
    CustomArtifactsConfigurationUpdate: Optional[       Sequence[CustomArtifactConfigurationTypeDef]     ] = None

class RunConfigurationTypeDef(BaseModel):
    FlinkRunConfiguration: Optional[FlinkRunConfigurationTypeDef] = None
    SqlRunConfigurations: Optional[Sequence[SqlRunConfigurationTypeDef]] = None
    ApplicationRestoreConfiguration: Optional[ApplicationRestoreConfigurationTypeDef] = None

class ApplicationOperationInfoDetailsTypeDef(BaseModel):
    Operation: str
    StartTime: datetime
    EndTime: datetime
    OperationStatus: OperationStatusType
    ApplicationVersionChangeDetails: Optional[ApplicationVersionChangeDetailsTypeDef] = None
    OperationFailureDetails: Optional[OperationFailureDetailsTypeDef] = None

class AddApplicationInputProcessingConfigurationResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    InputId: str
    InputProcessingConfigurationDescription: InputProcessingConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationInputProcessingConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfigurationTypeDef

class DiscoverInputSchemaRequestRequestTypeDef(BaseModel):
    ServiceExecutionRole: str
    ResourceARN: Optional[str] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None
    S3Configuration: Optional[S3ConfigurationTypeDef] = None
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None

class RecordFormatTypeDef(BaseModel):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: Optional[MappingParametersTypeDef] = None

class AddApplicationOutputResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    OutputDescriptions: List[OutputDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationOutputRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: OutputTypeDef

class StartApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    RunConfiguration: Optional[RunConfigurationTypeDef] = None

class DescribeApplicationOperationResponseTypeDef(BaseModel):
    ApplicationOperationInfoDetails: ApplicationOperationInfoDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InputSchemaUpdateTypeDef(BaseModel):
    RecordFormatUpdate: Optional[RecordFormatTypeDef] = None
    RecordEncodingUpdate: Optional[str] = None
    RecordColumnUpdates: Optional[Sequence[RecordColumnTypeDef]] = None

class SourceSchemaOutputTypeDef(BaseModel):
    RecordFormat: RecordFormatTypeDef
    RecordColumns: List[RecordColumnTypeDef]
    RecordEncoding: Optional[str] = None

class SourceSchemaTypeDef(BaseModel):
    RecordFormat: RecordFormatTypeDef
    RecordColumns: Sequence[RecordColumnTypeDef]
    RecordEncoding: Optional[str] = None

class InputUpdateTypeDef(BaseModel):
    InputId: str
    NamePrefixUpdate: Optional[str] = None
    InputProcessingConfigurationUpdate: Optional[       InputProcessingConfigurationUpdateTypeDef     ] = None
    KinesisStreamsInputUpdate: Optional[KinesisStreamsInputUpdateTypeDef] = None
    KinesisFirehoseInputUpdate: Optional[KinesisFirehoseInputUpdateTypeDef] = None
    InputSchemaUpdate: Optional[InputSchemaUpdateTypeDef] = None
    InputParallelismUpdate: Optional[InputParallelismUpdateTypeDef] = None

class DiscoverInputSchemaResponseTypeDef(BaseModel):
    InputSchema: SourceSchemaOutputTypeDef
    ParsedInputRecords: List[List[str]]
    ProcessedInputRecords: List[str]
    RawInputRecords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class InputDescriptionTypeDef(BaseModel):
    InputId: Optional[str] = None
    NamePrefix: Optional[str] = None
    InAppStreamNames: Optional[List[str]] = None
    InputProcessingConfigurationDescription: Optional[       InputProcessingConfigurationDescriptionTypeDef     ] = None
    KinesisStreamsInputDescription: Optional[KinesisStreamsInputDescriptionTypeDef] = None
    KinesisFirehoseInputDescription: Optional[KinesisFirehoseInputDescriptionTypeDef] = None
    InputSchema: Optional[SourceSchemaOutputTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None

class ReferenceDataSourceDescriptionTypeDef(BaseModel):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: S3ReferenceDataSourceDescriptionTypeDef
    ReferenceSchema: Optional[SourceSchemaOutputTypeDef] = None

class InputTypeDef(BaseModel):
    NamePrefix: str
    InputSchema: SourceSchemaTypeDef
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None
    KinesisStreamsInput: Optional[KinesisStreamsInputTypeDef] = None
    KinesisFirehoseInput: Optional[KinesisFirehoseInputTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None

class ReferenceDataSourceTypeDef(BaseModel):
    TableName: str
    ReferenceSchema: SourceSchemaTypeDef
    S3ReferenceDataSource: Optional[S3ReferenceDataSourceTypeDef] = None

class ReferenceDataSourceUpdateTypeDef(BaseModel):
    ReferenceId: str
    TableNameUpdate: Optional[str] = None
    S3ReferenceDataSourceUpdate: Optional[S3ReferenceDataSourceUpdateTypeDef] = None
    ReferenceSchemaUpdate: Optional[SourceSchemaTypeDef] = None

class AddApplicationInputResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    InputDescriptions: List[InputDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationReferenceDataSourceResponseTypeDef(BaseModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ReferenceDataSourceDescriptions: List[ReferenceDataSourceDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SqlApplicationConfigurationDescriptionTypeDef(BaseModel):
    InputDescriptions: Optional[List[InputDescriptionTypeDef]] = None
    OutputDescriptions: Optional[List[OutputDescriptionTypeDef]] = None
    ReferenceDataSourceDescriptions: Optional[List[ReferenceDataSourceDescriptionTypeDef]] = None

class AddApplicationInputRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: InputTypeDef

class AddApplicationReferenceDataSourceRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSourceTypeDef

class SqlApplicationConfigurationTypeDef(BaseModel):
    Inputs: Optional[Sequence[InputTypeDef]] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None
    ReferenceDataSources: Optional[Sequence[ReferenceDataSourceTypeDef]] = None

class SqlApplicationConfigurationUpdateTypeDef(BaseModel):
    InputUpdates: Optional[Sequence[InputUpdateTypeDef]] = None
    OutputUpdates: Optional[Sequence[OutputUpdateTypeDef]] = None
    ReferenceDataSourceUpdates: Optional[Sequence[ReferenceDataSourceUpdateTypeDef]] = None

class ApplicationConfigurationDescriptionTypeDef(BaseModel):
    SqlApplicationConfigurationDescription: Optional[       SqlApplicationConfigurationDescriptionTypeDef     ] = None
    ApplicationCodeConfigurationDescription: Optional[       ApplicationCodeConfigurationDescriptionTypeDef     ] = None
    RunConfigurationDescription: Optional[RunConfigurationDescriptionTypeDef] = None
    FlinkApplicationConfigurationDescription: Optional[       FlinkApplicationConfigurationDescriptionTypeDef     ] = None
    EnvironmentPropertyDescriptions: Optional[EnvironmentPropertyDescriptionsTypeDef] = None
    ApplicationSnapshotConfigurationDescription: Optional[       ApplicationSnapshotConfigurationDescriptionTypeDef     ] = None
    ApplicationSystemRollbackConfigurationDescription: Optional[       ApplicationSystemRollbackConfigurationDescriptionTypeDef     ] = None
    VpcConfigurationDescriptions: Optional[List[VpcConfigurationDescriptionTypeDef]] = None
    ZeppelinApplicationConfigurationDescription: Optional[       ZeppelinApplicationConfigurationDescriptionTypeDef     ] = None

class ApplicationConfigurationTypeDef(BaseModel):
    SqlApplicationConfiguration: Optional[SqlApplicationConfigurationTypeDef] = None
    FlinkApplicationConfiguration: Optional[FlinkApplicationConfigurationTypeDef] = None
    EnvironmentProperties: Optional[EnvironmentPropertiesTypeDef] = None
    ApplicationCodeConfiguration: Optional[ApplicationCodeConfigurationTypeDef] = None
    ApplicationSnapshotConfiguration: Optional[ApplicationSnapshotConfigurationTypeDef] = None
    ApplicationSystemRollbackConfiguration: Optional[       ApplicationSystemRollbackConfigurationTypeDef     ] = None
    VpcConfigurations: Optional[Sequence[VpcConfigurationTypeDef]] = None
    ZeppelinApplicationConfiguration: Optional[ZeppelinApplicationConfigurationTypeDef] = None

class ApplicationConfigurationUpdateTypeDef(BaseModel):
    SqlApplicationConfigurationUpdate: Optional[SqlApplicationConfigurationUpdateTypeDef] = None
    ApplicationCodeConfigurationUpdate: Optional[       ApplicationCodeConfigurationUpdateTypeDef     ] = None
    FlinkApplicationConfigurationUpdate: Optional[       FlinkApplicationConfigurationUpdateTypeDef     ] = None
    EnvironmentPropertyUpdates: Optional[EnvironmentPropertyUpdatesTypeDef] = None
    ApplicationSnapshotConfigurationUpdate: Optional[       ApplicationSnapshotConfigurationUpdateTypeDef     ] = None
    ApplicationSystemRollbackConfigurationUpdate: Optional[       ApplicationSystemRollbackConfigurationUpdateTypeDef     ] = None
    VpcConfigurationUpdates: Optional[Sequence[VpcConfigurationUpdateTypeDef]] = None
    ZeppelinApplicationConfigurationUpdate: Optional[       ZeppelinApplicationConfigurationUpdateTypeDef     ] = None

class ApplicationDetailTypeDef(BaseModel):
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

class CreateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ServiceExecutionRole: str
    ApplicationDescription: Optional[str] = None
    ApplicationConfiguration: Optional[ApplicationConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[Sequence[CloudWatchLoggingOptionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ApplicationMode: Optional[ApplicationModeType] = None

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: Optional[int] = None
    ApplicationConfigurationUpdate: Optional[ApplicationConfigurationUpdateTypeDef] = None
    ServiceExecutionRoleUpdate: Optional[str] = None
    RunConfigurationUpdate: Optional[RunConfigurationUpdateTypeDef] = None
    CloudWatchLoggingOptionUpdates: Optional[       Sequence[CloudWatchLoggingOptionUpdateTypeDef]     ] = None
    ConditionalToken: Optional[str] = None
    RuntimeEnvironmentUpdate: Optional[RuntimeEnvironmentType] = None

class CreateApplicationResponseTypeDef(BaseModel):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(BaseModel):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationVersionResponseTypeDef(BaseModel):
    ApplicationVersionDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackApplicationResponseTypeDef(BaseModel):
    ApplicationDetail: ApplicationDetailTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseModel):
    ApplicationDetail: ApplicationDetailTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

