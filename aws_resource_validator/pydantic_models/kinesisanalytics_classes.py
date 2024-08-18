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
from aws_resource_validator.pydantic_models.kinesisanalytics_constants import *

class CloudWatchLoggingOptionTypeDef(BaseValidatorModel):
    LogStreamARN: str
    RoleARN: str

class CloudWatchLoggingOptionDescriptionTypeDef(BaseValidatorModel):
    LogStreamARN: str
    RoleARN: str
    CloudWatchLoggingOptionId: Optional[str] = None

class ApplicationSummaryTypeDef(BaseValidatorModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType

class CloudWatchLoggingOptionUpdateTypeDef(BaseValidatorModel):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class CSVMappingParametersTypeDef(BaseValidatorModel):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOptionId: str

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

class DescribeApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str

class DestinationSchemaTypeDef(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType

class InputStartingPositionConfigurationTypeDef(BaseValidatorModel):
    InputStartingPosition: Optional[InputStartingPositionType] = None

class S3ConfigurationTypeDef(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    FileKey: str

class InputParallelismTypeDef(BaseValidatorModel):
    Count: Optional[int] = None

class KinesisFirehoseInputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisStreamsInputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class InputLambdaProcessorDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class InputLambdaProcessorTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str

class InputLambdaProcessorUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class InputParallelismUpdateTypeDef(BaseValidatorModel):
    CountUpdate: Optional[int] = None

class RecordColumnTypeDef(BaseValidatorModel):
    Name: str
    SqlType: str
    Mapping: Optional[str] = None

class KinesisFirehoseInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str

class KinesisStreamsInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str

class KinesisFirehoseInputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class KinesisStreamsInputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class JSONMappingParametersTypeDef(BaseValidatorModel):
    RecordRowPath: str

class KinesisFirehoseOutputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisFirehoseOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str

class KinesisFirehoseOutputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class KinesisStreamsOutputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisStreamsOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str

class KinesisStreamsOutputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class LambdaOutputDescriptionTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None

class LambdaOutputTypeDef(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str

class LambdaOutputUpdateTypeDef(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    ExclusiveStartApplicationName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class S3ReferenceDataSourceDescriptionTypeDef(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str

class S3ReferenceDataSourceTypeDef(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str

class S3ReferenceDataSourceUpdateTypeDef(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None
    ReferenceRoleARNUpdate: Optional[str] = None

class StopApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationSummary: ApplicationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    HasMoreApplications: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CreateTimestamp: TimestampTypeDef

class InputConfigurationTypeDef(BaseValidatorModel):
    Id: str
    InputStartingPositionConfiguration: InputStartingPositionConfigurationTypeDef

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

class StartApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    InputConfigurations: Sequence[InputConfigurationTypeDef]

class AddApplicationInputProcessingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfigurationTypeDef

class DiscoverInputSchemaRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None
    S3Configuration: Optional[S3ConfigurationTypeDef] = None
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None

class RecordFormatTypeDef(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: Optional[MappingParametersTypeDef] = None

class AddApplicationOutputRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: OutputTypeDef

class InputSchemaUpdateTypeDef(BaseValidatorModel):
    RecordFormatUpdate: Optional[RecordFormatTypeDef] = None
    RecordEncodingUpdate: Optional[str] = None
    RecordColumnUpdates: Optional[Sequence[RecordColumnTypeDef]] = None

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
    InputSchema: SourceSchemaTypeDef
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
    InputSchema: Optional[SourceSchemaTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None
    InputStartingPositionConfiguration: Optional[       InputStartingPositionConfigurationTypeDef     ] = None

class InputTypeDef(BaseValidatorModel):
    NamePrefix: str
    InputSchema: SourceSchemaTypeDef
    InputProcessingConfiguration: Optional[InputProcessingConfigurationTypeDef] = None
    KinesisStreamsInput: Optional[KinesisStreamsInputTypeDef] = None
    KinesisFirehoseInput: Optional[KinesisFirehoseInputTypeDef] = None
    InputParallelism: Optional[InputParallelismTypeDef] = None

class ReferenceDataSourceDescriptionTypeDef(BaseValidatorModel):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: S3ReferenceDataSourceDescriptionTypeDef
    ReferenceSchema: Optional[SourceSchemaTypeDef] = None

class ReferenceDataSourceTypeDef(BaseValidatorModel):
    TableName: str
    ReferenceSchema: SourceSchemaTypeDef
    S3ReferenceDataSource: Optional[S3ReferenceDataSourceTypeDef] = None

class ReferenceDataSourceUpdateTypeDef(BaseValidatorModel):
    ReferenceId: str
    TableNameUpdate: Optional[str] = None
    S3ReferenceDataSourceUpdate: Optional[S3ReferenceDataSourceUpdateTypeDef] = None
    ReferenceSchemaUpdate: Optional[SourceSchemaTypeDef] = None

class AddApplicationInputRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: InputTypeDef

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    ApplicationDescription: Optional[str] = None
    Inputs: Optional[Sequence[InputTypeDef]] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None
    CloudWatchLoggingOptions: Optional[Sequence[CloudWatchLoggingOptionTypeDef]] = None
    ApplicationCode: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ApplicationDetailTypeDef(BaseValidatorModel):
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

class AddApplicationReferenceDataSourceRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSourceTypeDef

class ApplicationUpdateTypeDef(BaseValidatorModel):
    InputUpdates: Optional[Sequence[InputUpdateTypeDef]] = None
    ApplicationCodeUpdate: Optional[str] = None
    OutputUpdates: Optional[Sequence[OutputUpdateTypeDef]] = None
    ReferenceDataSourceUpdates: Optional[Sequence[ReferenceDataSourceUpdateTypeDef]] = None
    CloudWatchLoggingOptionUpdates: Optional[       Sequence[CloudWatchLoggingOptionUpdateTypeDef]     ] = None

class DescribeApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ApplicationUpdate: ApplicationUpdateTypeDef

