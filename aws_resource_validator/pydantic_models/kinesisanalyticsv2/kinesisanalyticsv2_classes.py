from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kinesisanalyticsv2.kinesisanalyticsv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CloudWatchLoggingOption(BaseValidatorModel):
    LogStreamARN: str


class CloudWatchLoggingOptionDescription(BaseValidatorModel):
    LogStreamARN: str
    CloudWatchLoggingOptionId: Optional[str] = None
    RoleARN: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class VpcConfiguration(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class VpcConfigurationDescription(BaseValidatorModel):
    VpcConfigurationId: str
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class ApplicationSnapshotConfigurationDescription(BaseValidatorModel):
    SnapshotsEnabled: bool


class ApplicationSystemRollbackConfigurationDescription(BaseValidatorModel):
    RollbackEnabled: bool


class ApplicationSnapshotConfiguration(BaseValidatorModel):
    SnapshotsEnabled: bool


class ApplicationSystemRollbackConfiguration(BaseValidatorModel):
    RollbackEnabled: bool


class ApplicationSnapshotConfigurationUpdate(BaseValidatorModel):
    SnapshotsEnabledUpdate: bool


class ApplicationSystemRollbackConfigurationUpdate(BaseValidatorModel):
    RollbackEnabledUpdate: bool


class VpcConfigurationUpdate(BaseValidatorModel):
    VpcConfigurationId: str
    SubnetIdUpdates: Optional[List[str]] = None
    SecurityGroupIdUpdates: Optional[List[str]] = None


class ApplicationMaintenanceConfigurationDescription(BaseValidatorModel):
    ApplicationMaintenanceWindowStartTime: str
    ApplicationMaintenanceWindowEndTime: str


class ApplicationMaintenanceConfigurationUpdate(BaseValidatorModel):
    ApplicationMaintenanceWindowStartTimeUpdate: str


class ApplicationVersionChangeDetails(BaseValidatorModel):
    ApplicationVersionUpdatedFrom: int
    ApplicationVersionUpdatedTo: int


class ApplicationOperationInfo(BaseValidatorModel):
    Operation: Optional[str] = None
    OperationId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OperationStatus: Optional[OperationStatusType] = None


class ApplicationRestoreConfiguration(BaseValidatorModel):
    ApplicationRestoreType: ApplicationRestoreTypeType
    SnapshotName: Optional[str] = None


class ApplicationSummary(BaseValidatorModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationMode: Optional[ApplicationModeType] = None


class ApplicationVersionSummary(BaseValidatorModel):
    ApplicationVersionId: int
    ApplicationStatus: ApplicationStatusType

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CSVMappingParameters(BaseValidatorModel):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str


class GlueDataCatalogConfigurationDescription(BaseValidatorModel):
    DatabaseARN: str


class GlueDataCatalogConfiguration(BaseValidatorModel):
    DatabaseARN: str


class GlueDataCatalogConfigurationUpdate(BaseValidatorModel):
    DatabaseARNUpdate: str


class CheckpointConfigurationDescription(BaseValidatorModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    CheckpointingEnabled: Optional[bool] = None
    CheckpointInterval: Optional[int] = None
    MinPauseBetweenCheckpoints: Optional[int] = None


class CheckpointConfiguration(BaseValidatorModel):
    ConfigurationType: ConfigurationTypeType
    CheckpointingEnabled: Optional[bool] = None
    CheckpointInterval: Optional[int] = None
    MinPauseBetweenCheckpoints: Optional[int] = None


class CheckpointConfigurationUpdate(BaseValidatorModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    CheckpointingEnabledUpdate: Optional[bool] = None
    CheckpointIntervalUpdate: Optional[int] = None
    MinPauseBetweenCheckpointsUpdate: Optional[int] = None


class CloudWatchLoggingOptionUpdate(BaseValidatorModel):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: Optional[str] = None


class S3ApplicationCodeLocationDescription(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ObjectVersion: Optional[str] = None


class S3ContentLocation(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ObjectVersion: Optional[str] = None


class S3ContentLocationUpdate(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None
    ObjectVersionUpdate: Optional[str] = None


class CreateApplicationPresignedUrlRequest(BaseValidatorModel):
    ApplicationName: str
    UrlType: UrlTypeType
    SessionExpirationDurationInSeconds: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class CreateApplicationSnapshotRequest(BaseValidatorModel):
    ApplicationName: str
    SnapshotName: str


class MavenReference(BaseValidatorModel):
    GroupId: str
    ArtifactId: str
    Version: str


class DeleteApplicationCloudWatchLoggingOptionRequest(BaseValidatorModel):
    ApplicationName: str
    CloudWatchLoggingOptionId: str
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None


class DeleteApplicationInputProcessingConfigurationRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str


class DeleteApplicationOutputRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    OutputId: str


class DeleteApplicationReferenceDataSourceRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceId: str

Timestamp = Union[datetime, str]


class DeleteApplicationVpcConfigurationRequest(BaseValidatorModel):
    ApplicationName: str
    VpcConfigurationId: str
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None


class S3ContentBaseLocationDescription(BaseValidatorModel):
    BucketARN: str
    BasePath: Optional[str] = None


class S3ContentBaseLocation(BaseValidatorModel):
    BucketARN: str
    BasePath: Optional[str] = None


class S3ContentBaseLocationUpdate(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    BasePathUpdate: Optional[str] = None


class DescribeApplicationOperationRequest(BaseValidatorModel):
    ApplicationName: str
    OperationId: str


class DescribeApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    IncludeAdditionalDetails: Optional[bool] = None


class DescribeApplicationSnapshotRequest(BaseValidatorModel):
    ApplicationName: str
    SnapshotName: str


class SnapshotDetails(BaseValidatorModel):
    SnapshotName: str
    SnapshotStatus: SnapshotStatusType
    ApplicationVersionId: int
    SnapshotCreationTimestamp: Optional[datetime] = None
    RuntimeEnvironment: Optional[RuntimeEnvironmentType] = None


class DescribeApplicationVersionRequest(BaseValidatorModel):
    ApplicationName: str
    ApplicationVersionId: int


class DestinationSchema(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType


class InputStartingPositionConfiguration(BaseValidatorModel):
    InputStartingPosition: Optional[InputStartingPositionType] = None


class S3Configuration(BaseValidatorModel):
    BucketARN: str
    FileKey: str


class PropertyGroupOutput(BaseValidatorModel):
    PropertyGroupId: str
    PropertyMap: Dict[str, str]


class ErrorInfo(BaseValidatorModel):
    ErrorString: Optional[str] = None


class MonitoringConfigurationDescription(BaseValidatorModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    MetricsLevel: Optional[MetricsLevelType] = None
    LogLevel: Optional[LogLevelType] = None


class ParallelismConfigurationDescription(BaseValidatorModel):
    ConfigurationType: Optional[ConfigurationTypeType] = None
    Parallelism: Optional[int] = None
    ParallelismPerKPU: Optional[int] = None
    CurrentParallelism: Optional[int] = None
    AutoScalingEnabled: Optional[bool] = None


class MonitoringConfiguration(BaseValidatorModel):
    ConfigurationType: ConfigurationTypeType
    MetricsLevel: Optional[MetricsLevelType] = None
    LogLevel: Optional[LogLevelType] = None


class ParallelismConfiguration(BaseValidatorModel):
    ConfigurationType: ConfigurationTypeType
    Parallelism: Optional[int] = None
    ParallelismPerKPU: Optional[int] = None
    AutoScalingEnabled: Optional[bool] = None


class MonitoringConfigurationUpdate(BaseValidatorModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    MetricsLevelUpdate: Optional[MetricsLevelType] = None
    LogLevelUpdate: Optional[LogLevelType] = None


class ParallelismConfigurationUpdate(BaseValidatorModel):
    ConfigurationTypeUpdate: Optional[ConfigurationTypeType] = None
    ParallelismUpdate: Optional[int] = None
    ParallelismPerKPUUpdate: Optional[int] = None
    AutoScalingEnabledUpdate: Optional[bool] = None


class FlinkRunConfiguration(BaseValidatorModel):
    AllowNonRestoredState: Optional[bool] = None


class InputParallelism(BaseValidatorModel):
    Count: Optional[int] = None


class KinesisFirehoseInputDescription(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None


class KinesisStreamsInputDescription(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None


class InputLambdaProcessorDescription(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None


class InputLambdaProcessor(BaseValidatorModel):
    ResourceARN: str


class InputLambdaProcessorUpdate(BaseValidatorModel):
    ResourceARNUpdate: str


class InputParallelismUpdate(BaseValidatorModel):
    CountUpdate: int


class RecordColumn(BaseValidatorModel):
    Name: str
    SqlType: str
    Mapping: Optional[str] = None


class KinesisFirehoseInput(BaseValidatorModel):
    ResourceARN: str


class KinesisStreamsInput(BaseValidatorModel):
    ResourceARN: str


class KinesisFirehoseInputUpdate(BaseValidatorModel):
    ResourceARNUpdate: str


class KinesisStreamsInputUpdate(BaseValidatorModel):
    ResourceARNUpdate: str


class JSONMappingParameters(BaseValidatorModel):
    RecordRowPath: str


class KinesisFirehoseOutputDescription(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None


class KinesisFirehoseOutput(BaseValidatorModel):
    ResourceARN: str


class KinesisFirehoseOutputUpdate(BaseValidatorModel):
    ResourceARNUpdate: str


class KinesisStreamsOutputDescription(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None


class KinesisStreamsOutput(BaseValidatorModel):
    ResourceARN: str


class KinesisStreamsOutputUpdate(BaseValidatorModel):
    ResourceARNUpdate: str


class LambdaOutputDescription(BaseValidatorModel):
    ResourceARN: str
    RoleARN: Optional[str] = None


class LambdaOutput(BaseValidatorModel):
    ResourceARN: str


class LambdaOutputUpdate(BaseValidatorModel):
    ResourceARNUpdate: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationOperationsRequest(BaseValidatorModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    OperationStatus: Optional[OperationStatusType] = None


class ListApplicationSnapshotsRequest(BaseValidatorModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationVersionsRequest(BaseValidatorModel):
    ApplicationName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationsRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class PropertyGroup(BaseValidatorModel):
    PropertyGroupId: str
    PropertyMap: Dict[str, str]


class S3ReferenceDataSourceDescription(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: Optional[str] = None


class S3ReferenceDataSource(BaseValidatorModel):
    BucketARN: Optional[str] = None
    FileKey: Optional[str] = None


class S3ReferenceDataSourceUpdate(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None


class RollbackApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int


class StopApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    Force: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class ZeppelinMonitoringConfigurationDescription(BaseValidatorModel):
    LogLevel: Optional[LogLevelType] = None


class ZeppelinMonitoringConfiguration(BaseValidatorModel):
    LogLevel: LogLevelType


class ZeppelinMonitoringConfigurationUpdate(BaseValidatorModel):
    LogLevelUpdate: LogLevelType


class AddApplicationCloudWatchLoggingOptionRequest(BaseValidatorModel):
    ApplicationName: str
    CloudWatchLoggingOption: CloudWatchLoggingOption
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None


class AddApplicationCloudWatchLoggingOptionResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescription]
    OperationId: str
    ResponseMetadata: ResponseMetadata


class CreateApplicationPresignedUrlResponse(BaseValidatorModel):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadata


class DeleteApplicationCloudWatchLoggingOptionResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescription]
    OperationId: str
    ResponseMetadata: ResponseMetadata


class DeleteApplicationInputProcessingConfigurationResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadata


class DeleteApplicationOutputResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadata


class DeleteApplicationReferenceDataSourceResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadata


class DeleteApplicationVpcConfigurationResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    OperationId: str
    ResponseMetadata: ResponseMetadata


class StartApplicationResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class StopApplicationResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class AddApplicationVpcConfigurationRequest(BaseValidatorModel):
    ApplicationName: str
    VpcConfiguration: VpcConfiguration
    CurrentApplicationVersionId: Optional[int] = None
    ConditionalToken: Optional[str] = None


class AddApplicationVpcConfigurationResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    VpcConfigurationDescription: VpcConfigurationDescription
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdateApplicationMaintenanceConfigurationResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationMaintenanceConfigurationDescription: ApplicationMaintenanceConfigurationDescription
    ResponseMetadata: ResponseMetadata


class UpdateApplicationMaintenanceConfigurationRequest(BaseValidatorModel):
    ApplicationName: str
    ApplicationMaintenanceConfigurationUpdate: ApplicationMaintenanceConfigurationUpdate


class ListApplicationOperationsResponse(BaseValidatorModel):
    ApplicationOperationInfoList: List[ApplicationOperationInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationsResponse(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationVersionsResponse(BaseValidatorModel):
    ApplicationVersionSummaries: List[ApplicationVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CatalogConfigurationDescription(BaseValidatorModel):
    GlueDataCatalogConfigurationDescription: GlueDataCatalogConfigurationDescription


class CatalogConfiguration(BaseValidatorModel):
    GlueDataCatalogConfiguration: GlueDataCatalogConfiguration


class CatalogConfigurationUpdate(BaseValidatorModel):
    GlueDataCatalogConfigurationUpdate: GlueDataCatalogConfigurationUpdate


class CodeContentDescription(BaseValidatorModel):
    TextContent: Optional[str] = None
    CodeMD5: Optional[str] = None
    CodeSize: Optional[int] = None
    S3ApplicationCodeLocationDescription: Optional[S3ApplicationCodeLocationDescription] = None


class CodeContent(BaseValidatorModel):
    TextContent: Optional[str] = None
    ZipFileContent: Optional[Blob] = None
    S3ContentLocation: Optional[S3ContentLocation] = None


class CodeContentUpdate(BaseValidatorModel):
    TextContentUpdate: Optional[str] = None
    ZipFileContentUpdate: Optional[Blob] = None
    S3ContentLocationUpdate: Optional[S3ContentLocationUpdate] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class CustomArtifactConfigurationDescription(BaseValidatorModel):
    ArtifactType: Optional[ArtifactTypeType] = None
    S3ContentLocationDescription: Optional[S3ContentLocation] = None
    MavenReferenceDescription: Optional[MavenReference] = None


class CustomArtifactConfiguration(BaseValidatorModel):
    ArtifactType: ArtifactTypeType
    S3ContentLocation: Optional[S3ContentLocation] = None
    MavenReference: Optional[MavenReference] = None


class DeleteApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    CreateTimestamp: Timestamp


class DeleteApplicationSnapshotRequest(BaseValidatorModel):
    ApplicationName: str
    SnapshotName: str
    SnapshotCreationTimestamp: Timestamp


class DeployAsApplicationConfigurationDescription(BaseValidatorModel):
    S3ContentLocationDescription: S3ContentBaseLocationDescription


class DeployAsApplicationConfiguration(BaseValidatorModel):
    S3ContentLocation: S3ContentBaseLocation


class DeployAsApplicationConfigurationUpdate(BaseValidatorModel):
    S3ContentLocationUpdate: Optional[S3ContentBaseLocationUpdate] = None


class DescribeApplicationSnapshotResponse(BaseValidatorModel):
    SnapshotDetails: SnapshotDetails
    ResponseMetadata: ResponseMetadata


class ListApplicationSnapshotsResponse(BaseValidatorModel):
    SnapshotSummaries: List[SnapshotDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SqlRunConfiguration(BaseValidatorModel):
    InputId: str
    InputStartingPositionConfiguration: InputStartingPositionConfiguration


class EnvironmentPropertyDescriptions(BaseValidatorModel):
    PropertyGroupDescriptions: Optional[List[PropertyGroupOutput]] = None


class OperationFailureDetails(BaseValidatorModel):
    RollbackOperationId: Optional[str] = None
    ErrorInfo: Optional[ErrorInfo] = None


class FlinkApplicationConfigurationDescription(BaseValidatorModel):
    CheckpointConfigurationDescription: Optional[CheckpointConfigurationDescription] = None
    MonitoringConfigurationDescription: Optional[MonitoringConfigurationDescription] = None
    ParallelismConfigurationDescription: Optional[ParallelismConfigurationDescription] = None
    JobPlanDescription: Optional[str] = None


class FlinkApplicationConfiguration(BaseValidatorModel):
    CheckpointConfiguration: Optional[CheckpointConfiguration] = None
    MonitoringConfiguration: Optional[MonitoringConfiguration] = None
    ParallelismConfiguration: Optional[ParallelismConfiguration] = None


class FlinkApplicationConfigurationUpdate(BaseValidatorModel):
    CheckpointConfigurationUpdate: Optional[CheckpointConfigurationUpdate] = None
    MonitoringConfigurationUpdate: Optional[MonitoringConfigurationUpdate] = None
    ParallelismConfigurationUpdate: Optional[ParallelismConfigurationUpdate] = None


class RunConfigurationDescription(BaseValidatorModel):
    ApplicationRestoreConfigurationDescription: Optional[ApplicationRestoreConfiguration] = None
    FlinkRunConfigurationDescription: Optional[FlinkRunConfiguration] = None


class RunConfigurationUpdate(BaseValidatorModel):
    FlinkRunConfiguration: Optional[FlinkRunConfiguration] = None
    ApplicationRestoreConfiguration: Optional[ApplicationRestoreConfiguration] = None


class InputProcessingConfigurationDescription(BaseValidatorModel):
    InputLambdaProcessorDescription: Optional[InputLambdaProcessorDescription] = None


class InputProcessingConfiguration(BaseValidatorModel):
    InputLambdaProcessor: InputLambdaProcessor


class InputProcessingConfigurationUpdate(BaseValidatorModel):
    InputLambdaProcessorUpdate: InputLambdaProcessorUpdate


class MappingParameters(BaseValidatorModel):
    JSONMappingParameters: Optional[JSONMappingParameters] = None
    CSVMappingParameters: Optional[CSVMappingParameters] = None


class OutputDescription(BaseValidatorModel):
    OutputId: Optional[str] = None
    Name: Optional[str] = None
    KinesisStreamsOutputDescription: Optional[KinesisStreamsOutputDescription] = None
    KinesisFirehoseOutputDescription: Optional[KinesisFirehoseOutputDescription] = None
    LambdaOutputDescription: Optional[LambdaOutputDescription] = None
    DestinationSchema: Optional[DestinationSchema] = None


class Output(BaseValidatorModel):
    Name: str
    DestinationSchema: DestinationSchema
    KinesisStreamsOutput: Optional[KinesisStreamsOutput] = None
    KinesisFirehoseOutput: Optional[KinesisFirehoseOutput] = None
    LambdaOutput: Optional[LambdaOutput] = None


class OutputUpdate(BaseValidatorModel):
    OutputId: str
    NameUpdate: Optional[str] = None
    KinesisStreamsOutputUpdate: Optional[KinesisStreamsOutputUpdate] = None
    KinesisFirehoseOutputUpdate: Optional[KinesisFirehoseOutputUpdate] = None
    LambdaOutputUpdate: Optional[LambdaOutputUpdate] = None
    DestinationSchemaUpdate: Optional[DestinationSchema] = None


class ListApplicationOperationsRequestPaginate(BaseValidatorModel):
    ApplicationName: str
    Operation: Optional[str] = None
    OperationStatus: Optional[OperationStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationSnapshotsRequestPaginate(BaseValidatorModel):
    ApplicationName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationVersionsRequestPaginate(BaseValidatorModel):
    ApplicationName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None

PropertyGroupUnion = Union[PropertyGroup, PropertyGroupOutput]


class ApplicationCodeConfigurationDescription(BaseValidatorModel):
    CodeContentType: CodeContentTypeType
    CodeContentDescription: Optional[CodeContentDescription] = None


class ApplicationCodeConfiguration(BaseValidatorModel):
    CodeContentType: CodeContentTypeType
    CodeContent: Optional[CodeContent] = None


class ApplicationCodeConfigurationUpdate(BaseValidatorModel):
    CodeContentTypeUpdate: Optional[CodeContentTypeType] = None
    CodeContentUpdate: Optional[CodeContentUpdate] = None


class ZeppelinApplicationConfigurationDescription(BaseValidatorModel):
    MonitoringConfigurationDescription: ZeppelinMonitoringConfigurationDescription
    CatalogConfigurationDescription: Optional[CatalogConfigurationDescription] = None
    DeployAsApplicationConfigurationDescription: Optional[DeployAsApplicationConfigurationDescription] = None
    CustomArtifactsConfigurationDescription: Optional[List[CustomArtifactConfigurationDescription]] = None


class ZeppelinApplicationConfiguration(BaseValidatorModel):
    MonitoringConfiguration: Optional[ZeppelinMonitoringConfiguration] = None
    CatalogConfiguration: Optional[CatalogConfiguration] = None
    DeployAsApplicationConfiguration: Optional[DeployAsApplicationConfiguration] = None
    CustomArtifactsConfiguration: Optional[List[CustomArtifactConfiguration]] = None


class ZeppelinApplicationConfigurationUpdate(BaseValidatorModel):
    MonitoringConfigurationUpdate: Optional[ZeppelinMonitoringConfigurationUpdate] = None
    CatalogConfigurationUpdate: Optional[CatalogConfigurationUpdate] = None
    DeployAsApplicationConfigurationUpdate: Optional[DeployAsApplicationConfigurationUpdate] = None
    CustomArtifactsConfigurationUpdate: Optional[List[CustomArtifactConfiguration]] = None


class RunConfiguration(BaseValidatorModel):
    FlinkRunConfiguration: Optional[FlinkRunConfiguration] = None
    SqlRunConfigurations: Optional[List[SqlRunConfiguration]] = None
    ApplicationRestoreConfiguration: Optional[ApplicationRestoreConfiguration] = None


class ApplicationOperationInfoDetails(BaseValidatorModel):
    Operation: str
    StartTime: datetime
    EndTime: datetime
    OperationStatus: OperationStatusType
    ApplicationVersionChangeDetails: Optional[ApplicationVersionChangeDetails] = None
    OperationFailureDetails: Optional[OperationFailureDetails] = None


class AddApplicationInputProcessingConfigurationResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    InputId: str
    InputProcessingConfigurationDescription: InputProcessingConfigurationDescription
    ResponseMetadata: ResponseMetadata


class AddApplicationInputProcessingConfigurationRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfiguration


class DiscoverInputSchemaRequest(BaseValidatorModel):
    ServiceExecutionRole: str
    ResourceARN: Optional[str] = None
    InputStartingPositionConfiguration: Optional[InputStartingPositionConfiguration] = None
    S3Configuration: Optional[S3Configuration] = None
    InputProcessingConfiguration: Optional[InputProcessingConfiguration] = None


class RecordFormat(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: Optional[MappingParameters] = None


class AddApplicationOutputResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    OutputDescriptions: List[OutputDescription]
    ResponseMetadata: ResponseMetadata


class AddApplicationOutputRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: Output


class EnvironmentProperties(BaseValidatorModel):
    PropertyGroups: List[PropertyGroupUnion]


class EnvironmentPropertyUpdates(BaseValidatorModel):
    PropertyGroups: List[PropertyGroupUnion]


class StartApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    RunConfiguration: Optional[RunConfiguration] = None


class DescribeApplicationOperationResponse(BaseValidatorModel):
    ApplicationOperationInfoDetails: ApplicationOperationInfoDetails
    ResponseMetadata: ResponseMetadata


class InputSchemaUpdate(BaseValidatorModel):
    RecordFormatUpdate: Optional[RecordFormat] = None
    RecordEncodingUpdate: Optional[str] = None
    RecordColumnUpdates: Optional[List[RecordColumn]] = None


class SourceSchemaOutput(BaseValidatorModel):
    RecordFormat: RecordFormat
    RecordColumns: List[RecordColumn]
    RecordEncoding: Optional[str] = None


class SourceSchema(BaseValidatorModel):
    RecordFormat: RecordFormat
    RecordColumns: List[RecordColumn]
    RecordEncoding: Optional[str] = None


class InputUpdate(BaseValidatorModel):
    InputId: str
    NamePrefixUpdate: Optional[str] = None
    InputProcessingConfigurationUpdate: Optional[InputProcessingConfigurationUpdate] = None
    KinesisStreamsInputUpdate: Optional[KinesisStreamsInputUpdate] = None
    KinesisFirehoseInputUpdate: Optional[KinesisFirehoseInputUpdate] = None
    InputSchemaUpdate: Optional[InputSchemaUpdate] = None
    InputParallelismUpdate: Optional[InputParallelismUpdate] = None


class DiscoverInputSchemaResponse(BaseValidatorModel):
    InputSchema: SourceSchemaOutput
    ParsedInputRecords: List[List[str]]
    ProcessedInputRecords: List[str]
    RawInputRecords: List[str]
    ResponseMetadata: ResponseMetadata


class InputDescription(BaseValidatorModel):
    InputId: Optional[str] = None
    NamePrefix: Optional[str] = None
    InAppStreamNames: Optional[List[str]] = None
    InputProcessingConfigurationDescription: Optional[InputProcessingConfigurationDescription] = None
    KinesisStreamsInputDescription: Optional[KinesisStreamsInputDescription] = None
    KinesisFirehoseInputDescription: Optional[KinesisFirehoseInputDescription] = None
    InputSchema: Optional[SourceSchemaOutput] = None
    InputParallelism: Optional[InputParallelism] = None
    InputStartingPositionConfiguration: Optional[InputStartingPositionConfiguration] = None


class ReferenceDataSourceDescription(BaseValidatorModel):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: S3ReferenceDataSourceDescription
    ReferenceSchema: Optional[SourceSchemaOutput] = None

SourceSchemaUnion = Union[SourceSchema, SourceSchemaOutput]


class AddApplicationInputResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    InputDescriptions: List[InputDescription]
    ResponseMetadata: ResponseMetadata


class AddApplicationReferenceDataSourceResponse(BaseValidatorModel):
    ApplicationARN: str
    ApplicationVersionId: int
    ReferenceDataSourceDescriptions: List[ReferenceDataSourceDescription]
    ResponseMetadata: ResponseMetadata


class SqlApplicationConfigurationDescription(BaseValidatorModel):
    InputDescriptions: Optional[List[InputDescription]] = None
    OutputDescriptions: Optional[List[OutputDescription]] = None
    ReferenceDataSourceDescriptions: Optional[List[ReferenceDataSourceDescription]] = None


class Input(BaseValidatorModel):
    NamePrefix: str
    InputSchema: SourceSchemaUnion
    InputProcessingConfiguration: Optional[InputProcessingConfiguration] = None
    KinesisStreamsInput: Optional[KinesisStreamsInput] = None
    KinesisFirehoseInput: Optional[KinesisFirehoseInput] = None
    InputParallelism: Optional[InputParallelism] = None


class ReferenceDataSource(BaseValidatorModel):
    TableName: str
    ReferenceSchema: SourceSchemaUnion
    S3ReferenceDataSource: Optional[S3ReferenceDataSource] = None


class ReferenceDataSourceUpdate(BaseValidatorModel):
    ReferenceId: str
    TableNameUpdate: Optional[str] = None
    S3ReferenceDataSourceUpdate: Optional[S3ReferenceDataSourceUpdate] = None
    ReferenceSchemaUpdate: Optional[SourceSchemaUnion] = None


class ApplicationConfigurationDescription(BaseValidatorModel):
    SqlApplicationConfigurationDescription: Optional[SqlApplicationConfigurationDescription] = None
    ApplicationCodeConfigurationDescription: Optional[ApplicationCodeConfigurationDescription] = None
    RunConfigurationDescription: Optional[RunConfigurationDescription] = None
    FlinkApplicationConfigurationDescription: Optional[FlinkApplicationConfigurationDescription] = None
    EnvironmentPropertyDescriptions: Optional[EnvironmentPropertyDescriptions] = None
    ApplicationSnapshotConfigurationDescription: Optional[ApplicationSnapshotConfigurationDescription] = None
    ApplicationSystemRollbackConfigurationDescription: Optional[ApplicationSystemRollbackConfigurationDescription] = None
    VpcConfigurationDescriptions: Optional[List[VpcConfigurationDescription]] = None
    ZeppelinApplicationConfigurationDescription: Optional[ZeppelinApplicationConfigurationDescription] = None


class AddApplicationInputRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: Input


class AddApplicationReferenceDataSourceRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSource


class SqlApplicationConfiguration(BaseValidatorModel):
    Inputs: Optional[List[Input]] = None
    Outputs: Optional[List[Output]] = None
    ReferenceDataSources: Optional[List[ReferenceDataSource]] = None


class SqlApplicationConfigurationUpdate(BaseValidatorModel):
    InputUpdates: Optional[List[InputUpdate]] = None
    OutputUpdates: Optional[List[OutputUpdate]] = None
    ReferenceDataSourceUpdates: Optional[List[ReferenceDataSourceUpdate]] = None


class ApplicationDetail(BaseValidatorModel):
    ApplicationARN: str
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    ApplicationDescription: Optional[str] = None
    ServiceExecutionRole: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    ApplicationConfigurationDescription: Optional[ApplicationConfigurationDescription] = None
    CloudWatchLoggingOptionDescriptions: Optional[List[CloudWatchLoggingOptionDescription]] = None
    ApplicationMaintenanceConfigurationDescription: Optional[ApplicationMaintenanceConfigurationDescription] = None
    ApplicationVersionUpdatedFrom: Optional[int] = None
    ApplicationVersionRolledBackFrom: Optional[int] = None
    ApplicationVersionCreateTimestamp: Optional[datetime] = None
    ConditionalToken: Optional[str] = None
    ApplicationVersionRolledBackTo: Optional[int] = None
    ApplicationMode: Optional[ApplicationModeType] = None


class ApplicationConfiguration(BaseValidatorModel):
    SqlApplicationConfiguration: Optional[SqlApplicationConfiguration] = None
    FlinkApplicationConfiguration: Optional[FlinkApplicationConfiguration] = None
    EnvironmentProperties: Optional[EnvironmentProperties] = None
    ApplicationCodeConfiguration: Optional[ApplicationCodeConfiguration] = None
    ApplicationSnapshotConfiguration: Optional[ApplicationSnapshotConfiguration] = None
    ApplicationSystemRollbackConfiguration: Optional[ApplicationSystemRollbackConfiguration] = None
    VpcConfigurations: Optional[List[VpcConfiguration]] = None
    ZeppelinApplicationConfiguration: Optional[ZeppelinApplicationConfiguration] = None


class ApplicationConfigurationUpdate(BaseValidatorModel):
    SqlApplicationConfigurationUpdate: Optional[SqlApplicationConfigurationUpdate] = None
    ApplicationCodeConfigurationUpdate: Optional[ApplicationCodeConfigurationUpdate] = None
    FlinkApplicationConfigurationUpdate: Optional[FlinkApplicationConfigurationUpdate] = None
    EnvironmentPropertyUpdates: Optional[EnvironmentPropertyUpdates] = None
    ApplicationSnapshotConfigurationUpdate: Optional[ApplicationSnapshotConfigurationUpdate] = None
    ApplicationSystemRollbackConfigurationUpdate: Optional[ApplicationSystemRollbackConfigurationUpdate] = None
    VpcConfigurationUpdates: Optional[List[VpcConfigurationUpdate]] = None
    ZeppelinApplicationConfigurationUpdate: Optional[ZeppelinApplicationConfigurationUpdate] = None


class CreateApplicationResponse(BaseValidatorModel):
    ApplicationDetail: ApplicationDetail
    ResponseMetadata: ResponseMetadata


class DescribeApplicationResponse(BaseValidatorModel):
    ApplicationDetail: ApplicationDetail
    ResponseMetadata: ResponseMetadata


class DescribeApplicationVersionResponse(BaseValidatorModel):
    ApplicationVersionDetail: ApplicationDetail
    ResponseMetadata: ResponseMetadata


class RollbackApplicationResponse(BaseValidatorModel):
    ApplicationDetail: ApplicationDetail
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdateApplicationResponse(BaseValidatorModel):
    ApplicationDetail: ApplicationDetail
    OperationId: str
    ResponseMetadata: ResponseMetadata


class CreateApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ServiceExecutionRole: str
    ApplicationDescription: Optional[str] = None
    ApplicationConfiguration: Optional[ApplicationConfiguration] = None
    CloudWatchLoggingOptions: Optional[List[CloudWatchLoggingOption]] = None
    Tags: Optional[List[Tag]] = None
    ApplicationMode: Optional[ApplicationModeType] = None


class UpdateApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: Optional[int] = None
    ApplicationConfigurationUpdate: Optional[ApplicationConfigurationUpdate] = None
    ServiceExecutionRoleUpdate: Optional[str] = None
    RunConfigurationUpdate: Optional[RunConfigurationUpdate] = None
    CloudWatchLoggingOptionUpdates: Optional[List[CloudWatchLoggingOptionUpdate]] = None
    ConditionalToken: Optional[str] = None
    RuntimeEnvironmentUpdate: Optional[RuntimeEnvironmentType] = None