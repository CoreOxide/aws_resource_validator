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
from aws_resource_validator.pydantic_models.timestream_write_constants import *

class BatchLoadProgressReportTypeDef(BaseValidatorModel):
    RecordsProcessed: Optional[int] = None
    RecordsIngested: Optional[int] = None
    ParseFailures: Optional[int] = None
    RecordIngestionFailures: Optional[int] = None
    FileFailures: Optional[int] = None
    BytesMetered: Optional[int] = None

class BatchLoadTaskTypeDef(BaseValidatorModel):
    TaskId: Optional[str] = None
    TaskStatus: Optional[BatchLoadStatusType] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ResumableUntil: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class DatabaseTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableCount: Optional[int] = None
    KmsKeyId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class RetentionPropertiesTypeDef(BaseValidatorModel):
    MemoryStoreRetentionPeriodInHours: int
    MagneticStoreRetentionPeriodInDays: int

class CsvConfigurationTypeDef(BaseValidatorModel):
    ColumnSeparator: Optional[str] = None
    EscapeChar: Optional[str] = None
    QuoteChar: Optional[str] = None
    NullValue: Optional[str] = None
    TrimWhiteSpace: Optional[bool] = None

class DataModelS3ConfigurationTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectKey: Optional[str] = None

class DimensionMappingTypeDef(BaseValidatorModel):
    SourceColumn: Optional[str] = None
    DestinationColumn: Optional[str] = None

class DataSourceS3ConfigurationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None

class DeleteDatabaseRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str

class DeleteTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str

class DescribeBatchLoadTaskRequestRequestTypeDef(BaseValidatorModel):
    TaskId: str

class DescribeDatabaseRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str

class EndpointTypeDef(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int

class DescribeTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str

class DimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str
    DimensionValueType: Optional[Literal["VARCHAR"]] = None

class ListBatchLoadTasksRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TaskStatus: Optional[BatchLoadStatusType] = None

class ListDatabasesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTablesRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class S3ConfigurationTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None
    KmsKeyId: Optional[str] = None

class MeasureValueTypeDef(BaseValidatorModel):
    Name: str
    Value: str
    Type: MeasureValueTypeType

class MultiMeasureAttributeMappingTypeDef(BaseValidatorModel):
    SourceColumn: str
    TargetMultiMeasureAttributeName: Optional[str] = None
    MeasureValueType: Optional[ScalarMeasureValueTypeType] = None

class PartitionKeyTypeDef(BaseValidatorModel):
    Type: PartitionKeyTypeType
    Name: Optional[str] = None
    EnforcementInRecord: Optional[PartitionKeyEnforcementLevelType] = None

class RecordsIngestedTypeDef(BaseValidatorModel):
    Total: Optional[int] = None
    MemoryStore: Optional[int] = None
    MagneticStore: Optional[int] = None

class ReportS3ConfigurationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None
    KmsKeyId: Optional[str] = None

class ResumeBatchLoadTaskRequestRequestTypeDef(BaseValidatorModel):
    TaskId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDatabaseRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    KmsKeyId: str

class CreateBatchLoadTaskResponseTypeDef(BaseValidatorModel):
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListBatchLoadTasksResponseTypeDef(BaseValidatorModel):
    NextToken: str
    BatchLoadTasks: List[BatchLoadTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatabaseRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateDatabaseResponseTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatabaseResponseTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesResponseTypeDef(BaseValidatorModel):
    Databases: List[DatabaseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatabaseResponseTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationTypeDef(BaseValidatorModel):
    DataSourceS3Configuration: DataSourceS3ConfigurationTypeDef
    DataFormat: Literal["CSV"]
    CsvConfiguration: Optional[CsvConfigurationTypeDef] = None

class DescribeEndpointsResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MagneticStoreRejectedDataLocationTypeDef(BaseValidatorModel):
    S3Configuration: Optional[S3ConfigurationTypeDef] = None

class RecordTypeDef(BaseValidatorModel):
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    MeasureName: Optional[str] = None
    MeasureValue: Optional[str] = None
    MeasureValueType: Optional[MeasureValueTypeType] = None
    Time: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    Version: Optional[int] = None
    MeasureValues: Optional[Sequence[MeasureValueTypeDef]] = None

class MixedMeasureMappingTypeDef(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[Sequence[MultiMeasureAttributeMappingTypeDef]] = None

class MultiMeasureMappingsTypeDef(BaseValidatorModel):
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: Optional[str] = None

class SchemaTypeDef(BaseValidatorModel):
    CompositePartitionKey: Optional[Sequence[PartitionKeyTypeDef]] = None

class WriteRecordsResponseTypeDef(BaseValidatorModel):
    RecordsIngested: RecordsIngestedTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReportConfigurationTypeDef(BaseValidatorModel):
    ReportS3Configuration: Optional[ReportS3ConfigurationTypeDef] = None

class MagneticStoreWritePropertiesTypeDef(BaseValidatorModel):
    EnableMagneticStoreWrites: bool
    MagneticStoreRejectedDataLocation: Optional[MagneticStoreRejectedDataLocationTypeDef] = None

class WriteRecordsRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Records: Sequence[RecordTypeDef]
    CommonAttributes: Optional[RecordTypeDef] = None

class DataModelTypeDef(BaseValidatorModel):
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    TimeColumn: Optional[str] = None
    TimeUnit: Optional[TimeUnitType] = None
    MultiMeasureMappings: Optional[MultiMeasureMappingsTypeDef] = None
    MixedMeasureMappings: Optional[Sequence[MixedMeasureMappingTypeDef]] = None
    MeasureNameColumn: Optional[str] = None

class CreateTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    RetentionProperties: Optional[RetentionPropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWritePropertiesTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None

class TableTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    TableName: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    RetentionProperties: Optional[RetentionPropertiesTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWritePropertiesTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None

class UpdateTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    RetentionProperties: Optional[RetentionPropertiesTypeDef] = None
    MagneticStoreWriteProperties: Optional[MagneticStoreWritePropertiesTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None

class DataModelConfigurationTypeDef(BaseValidatorModel):
    DataModel: Optional[DataModelTypeDef] = None
    DataModelS3Configuration: Optional[DataModelS3ConfigurationTypeDef] = None

class CreateTableResponseTypeDef(BaseValidatorModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableResponseTypeDef(BaseValidatorModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesResponseTypeDef(BaseValidatorModel):
    Tables: List[TableTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableResponseTypeDef(BaseValidatorModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchLoadTaskDescriptionTypeDef(BaseValidatorModel):
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

class CreateBatchLoadTaskRequestRequestTypeDef(BaseValidatorModel):
    DataSourceConfiguration: DataSourceConfigurationTypeDef
    ReportConfiguration: ReportConfigurationTypeDef
    TargetDatabaseName: str
    TargetTableName: str
    ClientToken: Optional[str] = None
    DataModelConfiguration: Optional[DataModelConfigurationTypeDef] = None
    RecordVersion: Optional[int] = None

class DescribeBatchLoadTaskResponseTypeDef(BaseValidatorModel):
    BatchLoadTaskDescription: BatchLoadTaskDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

