from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.timestream_write.timestream_write_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BatchLoadProgressReport(BaseValidatorModel):
    RecordsProcessed: Optional[int] = None
    RecordsIngested: Optional[int] = None
    ParseFailures: Optional[int] = None
    RecordIngestionFailures: Optional[int] = None
    FileFailures: Optional[int] = None
    BytesMetered: Optional[int] = None


class BatchLoadTask(BaseValidatorModel):
    TaskId: Optional[str] = None
    TaskStatus: Optional[BatchLoadStatusType] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ResumableUntil: Optional[datetime] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class Database(BaseValidatorModel):
    Arn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableCount: Optional[int] = None
    KmsKeyId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class RetentionProperties(BaseValidatorModel):
    MemoryStoreRetentionPeriodInHours: int
    MagneticStoreRetentionPeriodInDays: int


class CsvConfiguration(BaseValidatorModel):
    ColumnSeparator: Optional[str] = None
    EscapeChar: Optional[str] = None
    QuoteChar: Optional[str] = None
    NullValue: Optional[str] = None
    TrimWhiteSpace: Optional[bool] = None


class DataModelS3Configuration(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectKey: Optional[str] = None


class DimensionMapping(BaseValidatorModel):
    SourceColumn: Optional[str] = None
    DestinationColumn: Optional[str] = None


class DataSourceS3Configuration(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None


# This class is the input for the 'delete_database' function.
class DeleteDatabaseRequest(BaseValidatorModel):
    DatabaseName: str


# This class is the input for the 'delete_table' function.
class DeleteTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


# This class is the input for the 'describe_batch_load_task' function.
class DescribeBatchLoadTaskRequest(BaseValidatorModel):
    TaskId: str


# This class is the input for the 'describe_database' function.
class DescribeDatabaseRequest(BaseValidatorModel):
    DatabaseName: str


class Endpoint(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int


# This class is the input for the 'describe_table' function.
class DescribeTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class Dimension(BaseValidatorModel):
    Name: str
    Value: str
    DimensionValueType: Optional[Literal['VARCHAR']] = None


# This class is the input for the 'list_batch_load_tasks' function.
class ListBatchLoadTasksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TaskStatus: Optional[BatchLoadStatusType] = None


# This class is the input for the 'list_databases' function.
class ListDatabasesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tables' function.
class ListTablesRequest(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class S3Configuration(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None
    KmsKeyId: Optional[str] = None


class MeasureValue(BaseValidatorModel):
    Name: str
    Value: str
    Type: MeasureValueTypeType


class MultiMeasureAttributeMapping(BaseValidatorModel):
    SourceColumn: str
    TargetMultiMeasureAttributeName: Optional[str] = None
    MeasureValueType: Optional[ScalarMeasureValueTypeType] = None


class PartitionKey(BaseValidatorModel):
    Type: PartitionKeyTypeType
    Name: Optional[str] = None
    EnforcementInRecord: Optional[PartitionKeyEnforcementLevelType] = None


class RecordsIngested(BaseValidatorModel):
    Total: Optional[int] = None
    MemoryStore: Optional[int] = None
    MagneticStore: Optional[int] = None


class ReportS3Configuration(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None
    KmsKeyId: Optional[str] = None


class ResumeBatchLoadTaskRequest(BaseValidatorModel):
    TaskId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_database' function.
class UpdateDatabaseRequest(BaseValidatorModel):
    DatabaseName: str
    KmsKeyId: str


# This class is the output for the 'create_batch_load_task' function.
class CreateBatchLoadTaskResponse(BaseValidatorModel):
    TaskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_table' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_batch_load_tasks' function.
class ListBatchLoadTasksResponse(BaseValidatorModel):
    BatchLoadTasks: List[BatchLoadTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_database' function.
class CreateDatabaseRequest(BaseValidatorModel):
    DatabaseName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_database' function.
class CreateDatabaseResponse(BaseValidatorModel):
    Database: Database
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_database' function.
class DescribeDatabaseResponse(BaseValidatorModel):
    Database: Database
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_databases' function.
class ListDatabasesResponse(BaseValidatorModel):
    Databases: List[Database]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_database' function.
class UpdateDatabaseResponse(BaseValidatorModel):
    Database: Database
    ResponseMetadata: ResponseMetadata


class DataSourceConfiguration(BaseValidatorModel):
    DataSourceS3Configuration: DataSourceS3Configuration
    DataFormat: Literal['CSV']
    CsvConfiguration: Optional[CsvConfiguration] = None


class DescribeEndpointsResponse(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata


class MagneticStoreRejectedDataLocation(BaseValidatorModel):
    S3Configuration: Optional[S3Configuration] = None


class Record(BaseValidatorModel):
    Dimensions: Optional[List[Dimension]] = None
    MeasureName: Optional[str] = None
    MeasureValue: Optional[str] = None
    MeasureValueType: Optional[MeasureValueTypeType] = None
    Time: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    Version: Optional[int] = None
    MeasureValues: Optional[List[MeasureValue]] = None


class MixedMeasureMappingOutput(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[List[MultiMeasureAttributeMapping]] = None


class MixedMeasureMapping(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[List[MultiMeasureAttributeMapping]] = None


class MultiMeasureMappingsOutput(BaseValidatorModel):
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMapping]
    TargetMultiMeasureName: Optional[str] = None


class MultiMeasureMappings(BaseValidatorModel):
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMapping]
    TargetMultiMeasureName: Optional[str] = None


class SchemaOutput(BaseValidatorModel):
    CompositePartitionKey: Optional[List[PartitionKey]] = None


class Schema(BaseValidatorModel):
    CompositePartitionKey: Optional[List[PartitionKey]] = None


# This class is the output for the 'write_records' function.
class WriteRecordsResponse(BaseValidatorModel):
    RecordsIngested: RecordsIngested
    ResponseMetadata: ResponseMetadata


class ReportConfiguration(BaseValidatorModel):
    ReportS3Configuration: Optional[ReportS3Configuration] = None


class MagneticStoreWriteProperties(BaseValidatorModel):
    EnableMagneticStoreWrites: bool
    MagneticStoreRejectedDataLocation: Optional[MagneticStoreRejectedDataLocation] = None


# This class is the input for the 'write_records' function.
class WriteRecordsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Records: List[Record]
    CommonAttributes: Optional[Record] = None


class DataModelOutput(BaseValidatorModel):
    DimensionMappings: List[DimensionMapping]
    TimeColumn: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    MultiMeasureMappings: Optional[MultiMeasureMappingsOutput] = None
    MixedMeasureMappings: Optional[List[MixedMeasureMappingOutput]] = None
    MeasureNameColumn: Optional[str] = None


class DataModel(BaseValidatorModel):
    DimensionMappings: List[DimensionMapping]
    TimeColumn: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    MultiMeasureMappings: Optional[MultiMeasureMappings] = None
    MixedMeasureMappings: Optional[List[MixedMeasureMapping]] = None
    MeasureNameColumn: Optional[str] = None

SchemaUnion = Union[Schema, SchemaOutput]


class Table(BaseValidatorModel):
    Arn: Optional[str] = None
    TableName: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    RetentionProperties: Optional[RetentionProperties] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWriteProperties] = None
    Schema: Optional[SchemaOutput] = None


class DataModelConfigurationOutput(BaseValidatorModel):
    DataModel: Optional[DataModelOutput] = None
    DataModelS3Configuration: Optional[DataModelS3Configuration] = None


class DataModelConfiguration(BaseValidatorModel):
    DataModel: Optional[DataModel] = None
    DataModelS3Configuration: Optional[DataModelS3Configuration] = None


# This class is the input for the 'create_table' function.
class CreateTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    RetentionProperties: Optional[RetentionProperties] = None
    Tags: Optional[List[Tag]] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWriteProperties] = None
    Schema: Optional[SchemaUnion] = None


# This class is the input for the 'update_table' function.
class UpdateTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    RetentionProperties: Optional[RetentionProperties] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWriteProperties] = None
    Schema: Optional[SchemaUnion] = None


# This class is the output for the 'create_table' function.
class CreateTableResponse(BaseValidatorModel):
    Table: Table
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_table' function.
class DescribeTableResponse(BaseValidatorModel):
    Table: Table
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tables' function.
class ListTablesResponse(BaseValidatorModel):
    Tables: List[Table]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_table' function.
class UpdateTableResponse(BaseValidatorModel):
    Table: Table
    ResponseMetadata: ResponseMetadata


class BatchLoadTaskDescription(BaseValidatorModel):
    TaskId: Optional[str] = None
    ErrorMessage: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfiguration] = None
    ProgressReport: Optional[BatchLoadProgressReport] = None
    ReportConfiguration: Optional[ReportConfiguration] = None
    DataModelConfiguration: Optional[DataModelConfigurationOutput] = None
    TargetDatabaseName: Optional[str] = None
    TargetTableName: Optional[str] = None
    TaskStatus: Optional[BatchLoadStatusType] = None
    RecordVersion: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ResumableUntil: Optional[datetime] = None

DataModelConfigurationUnion = Union[DataModelConfiguration, DataModelConfigurationOutput]


# This class is the output for the 'describe_batch_load_task' function.
class DescribeBatchLoadTaskResponse(BaseValidatorModel):
    BatchLoadTaskDescription: BatchLoadTaskDescription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_batch_load_task' function.
class CreateBatchLoadTaskRequest(BaseValidatorModel):
    DataSourceConfiguration: DataSourceConfiguration
    ReportConfiguration: ReportConfiguration
    TargetDatabaseName: str
    TargetTableName: str
    ClientToken: Optional[str] = None
    DataModelConfiguration: Optional[DataModelConfigurationUnion] = None
    RecordVersion: Optional[int] = None