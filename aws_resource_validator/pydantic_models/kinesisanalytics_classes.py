from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class CloudWatchLoggingOption(BaseValidatorModel):
    LogStreamARN: str
    RoleARN: str


class CloudWatchLoggingOptionDescription(BaseValidatorModel):
    LogStreamARN: str
    RoleARN: str
    CloudWatchLoggingOptionId: Optional[str] = None


class ApplicationSummary(BaseValidatorModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType


class CloudWatchLoggingOptionUpdate(BaseValidatorModel):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class CSVMappingParameters(BaseValidatorModel):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteApplicationCloudWatchLoggingOptionRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOptionId: str


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


class DescribeApplicationRequest(BaseValidatorModel):
    ApplicationName: str


class DestinationSchema(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType


class InputStartingPositionConfiguration(BaseValidatorModel):
    InputStartingPosition: Optional[InputStartingPositionType] = None


class S3Configuration(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    FileKey: str


class InputParallelism(BaseValidatorModel):
    Count: Optional[int] = None


class KinesisFirehoseInputDescription(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None


class KinesisStreamsInputDescription(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None


class InputLambdaProcessorDescription(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None


class InputLambdaProcessor(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str


class InputLambdaProcessorUpdate(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class InputParallelismUpdate(BaseValidatorModel):
    CountUpdate: Optional[int] = None


class KinesisFirehoseInput(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str


class KinesisStreamsInput(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str


class KinesisFirehoseInputUpdate(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class KinesisStreamsInputUpdate(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class JSONMappingParameters(BaseValidatorModel):
    RecordRowPath: str


class KinesisFirehoseOutputDescription(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None


class KinesisFirehoseOutput(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str


class KinesisFirehoseOutputUpdate(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class KinesisStreamsOutputDescription(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None


class KinesisStreamsOutput(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str


class KinesisStreamsOutputUpdate(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class LambdaOutputDescription(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None


class LambdaOutput(BaseValidatorModel):
    ResourceARN: str
    RoleARN: str


class LambdaOutputUpdate(BaseValidatorModel):
    ResourceARNUpdate: Optional[str] = None
    RoleARNUpdate: Optional[str] = None


class ListApplicationsRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    ExclusiveStartApplicationName: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class S3ReferenceDataSourceDescription(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str


class S3ReferenceDataSource(BaseValidatorModel):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str


class S3ReferenceDataSourceUpdate(BaseValidatorModel):
    BucketARNUpdate: Optional[str] = None
    FileKeyUpdate: Optional[str] = None
    ReferenceRoleARNUpdate: Optional[str] = None


class StopApplicationRequest(BaseValidatorModel):
    ApplicationName: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class AddApplicationCloudWatchLoggingOptionRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOption: CloudWatchLoggingOption


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateApplicationResponse(BaseValidatorModel):
    ApplicationSummary: ApplicationSummary
    ResponseMetadata: ResponseMetadata


class ListApplicationsResponse(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummary]
    HasMoreApplications: bool
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class DeleteApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    CreateTimestamp: Timestamp


class InputConfiguration(BaseValidatorModel):
    Id: str
    InputStartingPositionConfiguration: InputStartingPositionConfiguration


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


class StartApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    InputConfigurations: Sequence[InputConfiguration]


class AddApplicationInputProcessingConfigurationRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfiguration


class DiscoverInputSchemaRequest(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    RoleARN: Optional[str] = None
    InputStartingPositionConfiguration: Optional[InputStartingPositionConfiguration] = None
    S3Configuration: Optional[S3Configuration] = None
    InputProcessingConfiguration: Optional[InputProcessingConfiguration] = None


class RecordFormat(BaseValidatorModel):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: Optional[MappingParameters] = None


class AddApplicationOutputRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: Output


class RecordColumn(BaseValidatorModel):
    pass


class InputSchemaUpdate(BaseValidatorModel):
    RecordFormatUpdate: Optional[RecordFormat] = None
    RecordEncodingUpdate: Optional[str] = None
    RecordColumnUpdates: Optional[Sequence[RecordColumn]] = None


class SourceSchemaOutput(BaseValidatorModel):
    RecordFormat: RecordFormat
    RecordColumns: List[RecordColumn]
    RecordEncoding: Optional[str] = None


class SourceSchema(BaseValidatorModel):
    RecordFormat: RecordFormat
    RecordColumns: Sequence[RecordColumn]
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
    InputProcessingConfigurationDescription: Optional[ InputProcessingConfigurationDescription ] = None
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


class ApplicationDetail(BaseValidatorModel):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    ApplicationDescription: Optional[str] = None
    CreateTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    InputDescriptions: Optional[List[InputDescription]] = None
    OutputDescriptions: Optional[List[OutputDescription]] = None
    ReferenceDataSourceDescriptions: Optional[List[ReferenceDataSourceDescription]] = None
    CloudWatchLoggingOptionDescriptions: Optional[ List[CloudWatchLoggingOptionDescription] ] = None
    ApplicationCode: Optional[str] = None


class SourceSchemaUnion(BaseValidatorModel):
    pass


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


class DescribeApplicationResponse(BaseValidatorModel):
    ApplicationDetail: ApplicationDetail
    ResponseMetadata: ResponseMetadata


class AddApplicationInputRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: Input


class CreateApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    ApplicationDescription: Optional[str] = None
    Inputs: Optional[Sequence[Input]] = None
    Outputs: Optional[Sequence[Output]] = None
    CloudWatchLoggingOptions: Optional[Sequence[CloudWatchLoggingOption]] = None
    ApplicationCode: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class AddApplicationReferenceDataSourceRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSource


class ApplicationUpdate(BaseValidatorModel):
    InputUpdates: Optional[Sequence[InputUpdate]] = None
    ApplicationCodeUpdate: Optional[str] = None
    OutputUpdates: Optional[Sequence[OutputUpdate]] = None
    ReferenceDataSourceUpdates: Optional[Sequence[ReferenceDataSourceUpdate]] = None
    CloudWatchLoggingOptionUpdates: Optional[Sequence[CloudWatchLoggingOptionUpdate]] = None


class UpdateApplicationRequest(BaseValidatorModel):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ApplicationUpdate: ApplicationUpdate


