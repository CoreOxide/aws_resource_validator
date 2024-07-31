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
from aws_resource_validator.pydantic_models.kinesisanalytics_constants import *

class CloudWatchLoggingOptionTypeDef(BaseModel):
    LogStreamARN: str
    RoleARN: str

class CloudWatchLoggingOptionDescriptionTypeDef(BaseModel):
    LogStreamARN: str
    RoleARN: str
    CloudWatchLoggingOptionId: Optional[str] = None

class ApplicationSummaryTypeDef(BaseModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType

class CloudWatchLoggingOptionUpdateTypeDef(BaseModel):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class CSVMappingParametersTypeDef(BaseModel):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOptionId: str

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

class DescribeApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str

class DestinationSchemaTypeDef(BaseModel):
    RecordFormatType: RecordFormatTypeType

class InputStartingPositionConfigurationTypeDef(BaseModel):
    InputStartingPosition: Optional[InputStartingPositionType] = None

class S3ConfigurationTypeDef(BaseModel):
    RoleARN: str
    BucketARN: str
    FileKey: str

class InputParallelismTypeDef(BaseModel):
    Count: Optional[int] = None

class KinesisFirehoseInputDescriptionTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisStreamsInputDescriptionTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class InputLambdaProcessorDescriptionTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class InputLambdaProcessorTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: str

class InputLambdaProcessorUpdateTypeDef(BaseModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class InputParallelismUpdateTypeDef(BaseModel):
    CountUpdate: Optional[int] = None

class RecordColumnTypeDef(BaseModel):
    Name: str
    SqlType: str
    Mapping: Optional[str] = None

class KinesisFirehoseInputTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: str

class KinesisStreamsInputTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: str

class KinesisFirehoseInputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class KinesisStreamsInputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class JSONMappingParametersTypeDef(BaseModel):
    RecordRowPath: str

class KinesisFirehoseOutputDescriptionTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisFirehoseOutputTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: str

class KinesisFirehoseOutputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class KinesisStreamsOutputDescriptionTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisStreamsOutputTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: str

class KinesisStreamsOutputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class LambdaOutputDescriptionTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class LambdaOutputTypeDef(BaseModel):
    ResourceARN: str
    RoleARN: str

class LambdaOutputUpdateTypeDef(BaseModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    ExclusiveStartApplicationName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class S3ReferenceDataSourceDescriptionTypeDef(BaseModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str

class S3ReferenceDataSourceTypeDef(BaseModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str

class S3ReferenceDataSourceUpdateTypeDef(BaseModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None
    ReferenceRoleARNUpdate: Optional[str] = None

class StopApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateApplicationResponseTypeDef(BaseModel):
    ApplicationSummary: ApplicationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    HasMoreApplications: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CreateTimestamp: TimestampTypeDef

class InputConfigurationTypeDef(BaseModel):
    Id: str
    InputStartingPositionConfiguration: InputStartingPositionConfigurationTypeDef

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

class StartApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    InputConfigurations: Sequence[InputConfigurationTypeDef]

class AddApplicationInputProcessingConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfigurationTypeDef

class DiscoverInputSchemaRequestRequestTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None
    S3Configuration: Optional[S3ConfigurationTypeDef] = None
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None

class RecordFormatTypeDef(BaseModel):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: Optional[MappingParametersTypeDef] = None

class AddApplicationOutputRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: OutputTypeDef

class InputSchemaUpdateTypeDef(BaseModel):
    RecordFormatUpdate: Optional[RecordFormatTypeDef] = None
    RecordEncodingUpdate: Optional[str] = None
    RecordColumnUpdates: Optional[Sequence[RecordColumnTypeDef]] = None

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
    InputSchema: SourceSchemaTypeDef
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
    InputSchema: Optional[SourceSchemaTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None

class InputTypeDef(BaseModel):
    NamePrefix: str
    InputSchema: SourceSchemaTypeDef
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None
    KinesisStreamsInput: Optional[KinesisStreamsInputTypeDef] = None
    KinesisFirehoseInput: Optional[KinesisFirehoseInputTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None

class ReferenceDataSourceDescriptionTypeDef(BaseModel):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: S3ReferenceDataSourceDescriptionTypeDef
    ReferenceSchema: Optional[SourceSchemaTypeDef] = None

class ReferenceDataSourceTypeDef(BaseModel):
    TableName: str
    ReferenceSchema: SourceSchemaTypeDef
    S3ReferenceDataSource: Optional[S3ReferenceDataSourceTypeDef] = None

class ReferenceDataSourceUpdateTypeDef(BaseModel):
    ReferenceId: str
    TableNameUpdate: Optional[str] = None
    S3ReferenceDataSourceUpdate: Optional[S3ReferenceDataSourceUpdateTypeDef] = None
    ReferenceSchemaUpdate: Optional[SourceSchemaTypeDef] = None

class AddApplicationInputRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: InputTypeDef

class CreateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    ApplicationDescription: Optional[str] = None
    Inputs: Optional[Sequence[InputTypeDef]] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None
    CloudWatchLoggingOptions: Optional[Sequence[CloudWatchLoggingOptionTypeDef]] = None
    ApplicationCode: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ApplicationDetailTypeDef(BaseModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    ApplicationDescription: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    InputDescriptions: Optional[List[InputDescriptionTypeDef]] = None
    OutputDescriptions: Optional[List[OutputDescriptionTypeDef]] = None
    ReferenceDataSourceDescriptions: Optional[List[ReferenceDataSourceDescriptionTypeDef]] = None
    CloudWatchLoggingOptionDescriptions: Optional[       List[CloudWatchLoggingOptionDescriptionTypeDef]     ] = None
    ApplicationCode: Optional[str] = None

class AddApplicationReferenceDataSourceRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSourceTypeDef

class ApplicationUpdateTypeDef(BaseModel):
    InputUpdates: Optional[Sequence[InputUpdateTypeDef]] = None
    ApplicationCodeUpdate: Optional[str] = None
    OutputUpdates: Optional[Sequence[OutputUpdateTypeDef]] = None
    ReferenceDataSourceUpdates: Optional[Sequence[ReferenceDataSourceUpdateTypeDef]] = None
    CloudWatchLoggingOptionUpdates: Optional[       Sequence[CloudWatchLoggingOptionUpdateTypeDef]     ] = None

class DescribeApplicationResponseTypeDef(BaseModel):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ApplicationUpdate: ApplicationUpdateTypeDef

