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
from aws_resource_validator.pydantic_models.timestream_write_constants import *

class BatchLoadProgressReportTypeDef(BaseModel):
    RecordsProcessed: Optional[int] = None
    RecordsIngested: Optional[int] = None
    ParseFailures: Optional[int] = None
    RecordIngestionFailures: Optional[int] = None
    FileFailures: Optional[int] = None
    BytesMetered: Optional[int] = None

class BatchLoadTaskTypeDef(BaseModel):
    TaskId: Optional[str] = None
    TaskStatus: Optional[BatchLoadStatusType] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ResumableUntil: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DatabaseTypeDef(BaseModel):
    Arn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableCount: Optional[int] = None
    KmsKeyId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class RetentionPropertiesTypeDef(BaseModel):
    MemoryStoreRetentionPeriodInHours: int
    MagneticStoreRetentionPeriodInDays: int

class CsvConfigurationTypeDef(BaseModel):
    ColumnSeparator: Optional[str] = None
    EscapeChar: Optional[str] = None
    QuoteChar: Optional[str] = None
    NullValue: Optional[str] = None
    TrimWhiteSpace: Optional[bool] = None

class DataModelS3ConfigurationTypeDef(BaseModel):
    BucketName: Optional[str] = None
    ObjectKey: Optional[str] = None

class DimensionMappingTypeDef(BaseModel):
    SourceColumn: Optional[str] = None
    DestinationColumn: Optional[str] = None

class DataSourceS3ConfigurationTypeDef(BaseModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None

class DeleteDatabaseRequestRequestTypeDef(BaseModel):
    DatabaseName: str

class DeleteTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str

class DescribeBatchLoadTaskRequestRequestTypeDef(BaseModel):
    TaskId: str

class DescribeDatabaseRequestRequestTypeDef(BaseModel):
    DatabaseName: str

class EndpointTypeDef(BaseModel):
    Address: str
    CachePeriodInMinutes: int

class DescribeTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str

class DimensionTypeDef(BaseModel):
    Name: str
    Value: str
    DimensionValueType: Optional[Literal["VARCHAR"]] = None

class ListBatchLoadTasksRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TaskStatus: Optional[BatchLoadStatusType] = None

class ListDatabasesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTablesRequestRequestTypeDef(BaseModel):
    DatabaseName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class S3ConfigurationTypeDef(BaseModel):
    BucketName: Optional[str] = None
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None
    KmsKeyId: Optional[str] = None

class MeasureValueTypeDef(BaseModel):
    Name: str
    Value: str
    Type: MeasureValueTypeType

class MultiMeasureAttributeMappingTypeDef(BaseModel):
    SourceColumn: str
    TargetMultiMeasureAttributeName: Optional[str] = None
    MeasureValueType: Optional[ScalarMeasureValueTypeType] = None

class PartitionKeyTypeDef(BaseModel):
    Type: PartitionKeyTypeType
    Name: Optional[str] = None
    EnforcementInRecord: Optional[PartitionKeyEnforcementLevelType] = None

class RecordsIngestedTypeDef(BaseModel):
    Total: Optional[int] = None
    MemoryStore: Optional[int] = None
    MagneticStore: Optional[int] = None

class ReportS3ConfigurationTypeDef(BaseModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None
    KmsKeyId: Optional[str] = None

class ResumeBatchLoadTaskRequestRequestTypeDef(BaseModel):
    TaskId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDatabaseRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    KmsKeyId: str

class CreateBatchLoadTaskResponseTypeDef(BaseModel):
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListBatchLoadTasksResponseTypeDef(BaseModel):
    NextToken: str
    BatchLoadTasks: List[BatchLoadTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatabaseRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateDatabaseResponseTypeDef(BaseModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatabaseResponseTypeDef(BaseModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesResponseTypeDef(BaseModel):
    Databases: List[DatabaseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatabaseResponseTypeDef(BaseModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationTypeDef(BaseModel):
    DataSourceS3Configuration: DataSourceS3ConfigurationTypeDef
    DataFormat: Literal["CSV"]
    CsvConfiguration: Optional[CsvConfigurationTypeDef] = None

class DescribeEndpointsResponseTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MagneticStoreRejectedDataLocationTypeDef(BaseModel):
    S3Configuration: Optional[S3ConfigurationTypeDef] = None

class RecordTypeDef(BaseModel):
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    MeasureName: Optional[str] = None
    MeasureValue: Optional[str] = None
    MeasureValueType: Optional[MeasureValueTypeType] = None
    Time: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    Version: Optional[int] = None
    MeasureValues: Optional[Sequence[MeasureValueTypeDef]] = None

class MixedMeasureMappingTypeDef(BaseModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[Sequence[MultiMeasureAttributeMappingTypeDef]] = None

class MultiMeasureMappingsTypeDef(BaseModel):
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: Optional[str] = None

class SchemaTypeDef(BaseModel):
    CompositePartitionKey: Optional[Sequence[PartitionKeyTypeDef]] = None

class WriteRecordsResponseTypeDef(BaseModel):
    RecordsIngested: RecordsIngestedTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReportConfigurationTypeDef(BaseModel):
    ReportS3Configuration: Optional[ReportS3ConfigurationTypeDef] = None

class MagneticStoreWritePropertiesTypeDef(BaseModel):
    EnableMagneticStoreWrites: bool
    MagneticStoreRejectedDataLocation: Optional[MagneticStoreRejectedDataLocationTypeDef] = None

class WriteRecordsRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    Records: Sequence[RecordTypeDef]
    CommonAttributes: Optional[RecordTypeDef] = None

class DataModelTypeDef(BaseModel):
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    TimeColumn: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    MultiMeasureMappings: Optional[MultiMeasureMappingsTypeDef] = None
    MixedMeasureMappings: Optional[Sequence[MixedMeasureMappingTypeDef]] = None
    MeasureNameColumn: Optional[str] = None

class CreateTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    RetentionProperties: Optional[RetentionPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWritePropertiesTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None

class TableTypeDef(BaseModel):
    Arn: Optional[str] = None
    TableName: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    RetentionProperties: Optional[RetentionPropertiesTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWritePropertiesTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None

class UpdateTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    RetentionProperties: Optional[RetentionPropertiesTypeDef] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWritePropertiesTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None

class DataModelConfigurationTypeDef(BaseModel):
    DataModel: Optional[DataModelTypeDef] = None
    DataModelS3Configuration: Optional[DataModelS3ConfigurationTypeDef] = None

class CreateTableResponseTypeDef(BaseModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableResponseTypeDef(BaseModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesResponseTypeDef(BaseModel):
    Tables: List[TableTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableResponseTypeDef(BaseModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchLoadTaskDescriptionTypeDef(BaseModel):
    TaskId: Optional[str] = None
    ErrorMessage: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None
    ProgressReport: Optional[BatchLoadProgressReportTypeDef] = None
    ReportConfiguration: Optional[ReportConfigurationTypeDef] = None
    DataModelConfiguration: Optional[DataModelConfigurationTypeDef] = None
    TargetDatabaseName: Optional[str] = None
    TargetTableName: Optional[str] = None
    TaskStatus: Optional[BatchLoadStatusType] = None
    RecordVersion: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ResumableUntil: Optional[datetime] = None

class CreateBatchLoadTaskRequestRequestTypeDef(BaseModel):
    DataSourceConfiguration: DataSourceConfigurationTypeDef
    ReportConfiguration: ReportConfigurationTypeDef
    TargetDatabaseName: str
    TargetTableName: str
    ClientToken: Optional[str] = None
    DataModelConfiguration: Optional[DataModelConfigurationTypeDef] = None
    RecordVersion: Optional[int] = None

class DescribeBatchLoadTaskResponseTypeDef(BaseModel):
    BatchLoadTaskDescription: BatchLoadTaskDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

