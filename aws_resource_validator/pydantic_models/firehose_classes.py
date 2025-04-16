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
from aws_resource_validator.pydantic_models.firehose_constants import *

class AmazonOpenSearchServerlessBufferingHints(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None


class AmazonOpenSearchServerlessRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class CloudWatchLoggingOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogGroupName: Optional[str] = None
    LogStreamName: Optional[str] = None


class VpcConfiguration(BaseValidatorModel):
    SubnetIds: Sequence[str]
    RoleARN: str
    SecurityGroupIds: Sequence[str]


class VpcConfigurationDescription(BaseValidatorModel):
    SubnetIds: List[str]
    RoleARN: str
    SecurityGroupIds: List[str]
    VpcId: str


class AmazonopensearchserviceBufferingHints(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None


class AmazonopensearchserviceRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class DocumentIdOptions(BaseValidatorModel):
    DefaultDocumentIdFormat: DefaultDocumentIdFormatType


class AuthenticationConfiguration(BaseValidatorModel):
    RoleARN: str
    Connectivity: ConnectivityType


class BufferingHints(BaseValidatorModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None


class CatalogConfiguration(BaseValidatorModel):
    CatalogARN: Optional[str] = None
    WarehouseLocation: Optional[str] = None


class CopyCommand(BaseValidatorModel):
    DataTableName: str
    DataTableColumns: Optional[str] = None
    CopyOptions: Optional[str] = None


class DeliveryStreamEncryptionConfigurationInput(BaseValidatorModel):
    KeyType: KeyTypeType
    KeyARN: Optional[str] = None


class DirectPutSourceConfiguration(BaseValidatorModel):
    ThroughputHintInMBs: int


class KinesisStreamSourceConfiguration(BaseValidatorModel):
    KinesisStreamARN: str
    RoleARN: str


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SchemaConfiguration(BaseValidatorModel):
    RoleARN: Optional[str] = None
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Region: Optional[str] = None
    VersionId: Optional[str] = None


class DatabaseColumnListOutput(BaseValidatorModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None


class DatabaseColumnList(BaseValidatorModel):
    Include: Optional[Sequence[str]] = None
    Exclude: Optional[Sequence[str]] = None


class DatabaseListOutput(BaseValidatorModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None


class DatabaseList(BaseValidatorModel):
    Include: Optional[Sequence[str]] = None
    Exclude: Optional[Sequence[str]] = None


class SecretsManagerConfiguration(BaseValidatorModel):
    Enabled: bool
    SecretARN: Optional[str] = None
    RoleARN: Optional[str] = None


class DatabaseSourceVPCConfiguration(BaseValidatorModel):
    VpcEndpointServiceName: str


class DatabaseTableListOutput(BaseValidatorModel):
    Include: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None


class DatabaseTableList(BaseValidatorModel):
    Include: Optional[Sequence[str]] = None
    Exclude: Optional[Sequence[str]] = None


class DeleteDeliveryStreamInput(BaseValidatorModel):
    DeliveryStreamName: str
    AllowForceDelete: Optional[bool] = None


class DescribeDeliveryStreamInput(BaseValidatorModel):
    DeliveryStreamName: str
    Limit: Optional[int] = None
    ExclusiveStartDestinationId: Optional[str] = None


class HiveJsonSerDeOutput(BaseValidatorModel):
    TimestampFormats: Optional[List[str]] = None


class OpenXJsonSerDeOutput(BaseValidatorModel):
    ConvertDotsInJsonKeysToUnderscores: Optional[bool] = None
    CaseInsensitive: Optional[bool] = None
    ColumnToJsonKeyMappings: Optional[Dict[str, str]] = None


class DirectPutSourceDescription(BaseValidatorModel):
    ThroughputHintInMBs: Optional[int] = None


class RetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class ElasticsearchBufferingHints(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None


class ElasticsearchRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class KMSEncryptionConfig(BaseValidatorModel):
    AWSKMSKeyARN: str


class HiveJsonSerDe(BaseValidatorModel):
    TimestampFormats: Optional[Sequence[str]] = None


class HttpEndpointBufferingHints(BaseValidatorModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None


class HttpEndpointCommonAttribute(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str


class HttpEndpointConfiguration(BaseValidatorModel):
    Url: str
    Name: Optional[str] = None
    AccessKey: Optional[str] = None


class HttpEndpointDescription(BaseValidatorModel):
    Url: Optional[str] = None
    Name: Optional[str] = None


class HttpEndpointRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class SchemaEvolutionConfiguration(BaseValidatorModel):
    Enabled: bool


class TableCreationConfiguration(BaseValidatorModel):
    Enabled: bool


class KinesisStreamSourceDescription(BaseValidatorModel):
    KinesisStreamARN: Optional[str] = None
    RoleARN: Optional[str] = None
    DeliveryStartTimestamp: Optional[datetime] = None


class ListDeliveryStreamsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    DeliveryStreamType: Optional[DeliveryStreamTypeType] = None
    ExclusiveStartDeliveryStreamName: Optional[str] = None


class ListTagsForDeliveryStreamInput(BaseValidatorModel):
    DeliveryStreamName: str
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None


class OpenXJsonSerDe(BaseValidatorModel):
    ConvertDotsInJsonKeysToUnderscores: Optional[bool] = None
    CaseInsensitive: Optional[bool] = None
    ColumnToJsonKeyMappings: Optional[Mapping[str, str]] = None


class OrcSerDeOutput(BaseValidatorModel):
    StripeSizeBytes: Optional[int] = None
    BlockSizeBytes: Optional[int] = None
    RowIndexStride: Optional[int] = None
    EnablePadding: Optional[bool] = None
    PaddingTolerance: Optional[float] = None
    Compression: Optional[OrcCompressionType] = None
    BloomFilterColumns: Optional[List[str]] = None
    BloomFilterFalsePositiveProbability: Optional[float] = None
    DictionaryKeyThreshold: Optional[float] = None
    FormatVersion: Optional[OrcFormatVersionType] = None


class OrcSerDe(BaseValidatorModel):
    StripeSizeBytes: Optional[int] = None
    BlockSizeBytes: Optional[int] = None
    RowIndexStride: Optional[int] = None
    EnablePadding: Optional[bool] = None
    PaddingTolerance: Optional[float] = None
    Compression: Optional[OrcCompressionType] = None
    BloomFilterColumns: Optional[Sequence[str]] = None
    BloomFilterFalsePositiveProbability: Optional[float] = None
    DictionaryKeyThreshold: Optional[float] = None
    FormatVersion: Optional[OrcFormatVersionType] = None


class ParquetSerDe(BaseValidatorModel):
    BlockSizeBytes: Optional[int] = None
    PageSizeBytes: Optional[int] = None
    Compression: Optional[ParquetCompressionType] = None
    EnableDictionaryCompression: Optional[bool] = None
    MaxPaddingBytes: Optional[int] = None
    WriterVersion: Optional[ParquetWriterVersionType] = None


class PartitionField(BaseValidatorModel):
    SourceName: str


class ProcessorParameter(BaseValidatorModel):
    ParameterName: ProcessorParameterNameType
    ParameterValue: str


class PutRecordBatchResponseEntry(BaseValidatorModel):
    RecordId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class RedshiftRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class SnowflakeBufferingHints(BaseValidatorModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None


class SnowflakeRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class SnowflakeRoleConfiguration(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SnowflakeRole: Optional[str] = None


class SnowflakeVpcConfiguration(BaseValidatorModel):
    PrivateLinkVpceId: str


class SplunkBufferingHints(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None


class SplunkRetryOptions(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class StopDeliveryStreamEncryptionInput(BaseValidatorModel):
    DeliveryStreamName: str


class UntagDeliveryStreamInput(BaseValidatorModel):
    DeliveryStreamName: str
    TagKeys: Sequence[str]


class MSKSourceDescription(BaseValidatorModel):
    MSKClusterARN: Optional[str] = None
    TopicName: Optional[str] = None
    AuthenticationConfiguration: Optional[AuthenticationConfiguration] = None
    DeliveryStartTimestamp: Optional[datetime] = None
    ReadFromTimestamp: Optional[datetime] = None


class Blob(BaseValidatorModel):
    pass


class Record(BaseValidatorModel):
    Data: Blob


class StartDeliveryStreamEncryptionInput(BaseValidatorModel):
    DeliveryStreamName: str
    DeliveryStreamEncryptionConfigurationInput: Optional[ DeliveryStreamEncryptionConfigurationInput ] = None


class TagDeliveryStreamInput(BaseValidatorModel):
    DeliveryStreamName: str
    Tags: Sequence[Tag]


class CreateDeliveryStreamOutput(BaseValidatorModel):
    DeliveryStreamARN: str
    ResponseMetadata: ResponseMetadata


class ListDeliveryStreamsOutput(BaseValidatorModel):
    DeliveryStreamNames: List[str]
    HasMoreDeliveryStreams: bool
    ResponseMetadata: ResponseMetadata


class ListTagsForDeliveryStreamOutput(BaseValidatorModel):
    Tags: List[Tag]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadata


class PutRecordOutput(BaseValidatorModel):
    RecordId: str
    Encrypted: bool
    ResponseMetadata: ResponseMetadata


class FailureDescription(BaseValidatorModel):
    pass


class DatabaseSnapshotInfo(BaseValidatorModel):
    Id: str
    Table: str
    RequestTimestamp: datetime
    RequestedBy: SnapshotRequestedByType
    Status: SnapshotStatusType
    FailureDescription: Optional[FailureDescription] = None


class DeliveryStreamEncryptionConfiguration(BaseValidatorModel):
    KeyARN: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Status: Optional[DeliveryStreamEncryptionStatusType] = None
    FailureDescription: Optional[FailureDescription] = None


class DatabaseSourceAuthenticationConfiguration(BaseValidatorModel):
    SecretsManagerConfiguration: SecretsManagerConfiguration


class DeserializerOutput(BaseValidatorModel):
    OpenXJsonSerDe: Optional[OpenXJsonSerDeOutput] = None
    HiveJsonSerDe: Optional[HiveJsonSerDeOutput] = None


class DynamicPartitioningConfiguration(BaseValidatorModel):
    RetryOptions: Optional[RetryOptions] = None
    Enabled: Optional[bool] = None


class EncryptionConfiguration(BaseValidatorModel):
    NoEncryptionConfig: Optional[Literal["NoEncryption"]] = None
    KMSEncryptionConfig: Optional[KMSEncryptionConfig] = None


class HttpEndpointRequestConfigurationOutput(BaseValidatorModel):
    ContentEncoding: Optional[ContentEncodingType] = None
    CommonAttributes: Optional[List[HttpEndpointCommonAttribute]] = None


class HttpEndpointRequestConfiguration(BaseValidatorModel):
    ContentEncoding: Optional[ContentEncodingType] = None
    CommonAttributes: Optional[Sequence[HttpEndpointCommonAttribute]] = None


class Timestamp(BaseValidatorModel):
    pass


class MSKSourceConfiguration(BaseValidatorModel):
    MSKClusterARN: str
    TopicName: str
    AuthenticationConfiguration: AuthenticationConfiguration
    ReadFromTimestamp: Optional[Timestamp] = None


class SerializerOutput(BaseValidatorModel):
    ParquetSerDe: Optional[ParquetSerDe] = None
    OrcSerDe: Optional[OrcSerDeOutput] = None


class PartitionSpecOutput(BaseValidatorModel):
    Identity: Optional[List[PartitionField]] = None


class PartitionSpec(BaseValidatorModel):
    Identity: Optional[Sequence[PartitionField]] = None


class PutRecordBatchOutput(BaseValidatorModel):
    FailedPutCount: int
    Encrypted: bool
    RequestResponses: List[PutRecordBatchResponseEntry]
    ResponseMetadata: ResponseMetadata


class PutRecordBatchInput(BaseValidatorModel):
    DeliveryStreamName: str
    Records: Sequence[Record]


class PutRecordInput(BaseValidatorModel):
    DeliveryStreamName: str
    Record: Record


class InputFormatConfigurationOutput(BaseValidatorModel):
    Deserializer: Optional[DeserializerOutput] = None


class S3DestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHints] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None


class S3DestinationDescription(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHints
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfiguration
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None


class S3DestinationUpdate(BaseValidatorModel):
    RoleARN: Optional[str] = None
    BucketARN: Optional[str] = None
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHints] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None


class OpenXJsonSerDeUnion(BaseValidatorModel):
    pass


class HiveJsonSerDeUnion(BaseValidatorModel):
    pass


class Deserializer(BaseValidatorModel):
    OpenXJsonSerDe: Optional[OpenXJsonSerDeUnion] = None
    HiveJsonSerDe: Optional[HiveJsonSerDeUnion] = None


class OrcSerDeUnion(BaseValidatorModel):
    pass


class Serializer(BaseValidatorModel):
    ParquetSerDe: Optional[ParquetSerDe] = None
    OrcSerDe: Optional[OrcSerDeUnion] = None


class OutputFormatConfigurationOutput(BaseValidatorModel):
    Serializer: Optional[SerializerOutput] = None


class DestinationTableConfigurationOutput(BaseValidatorModel):
    DestinationTableName: str
    DestinationDatabaseName: str
    UniqueKeys: Optional[List[str]] = None
    PartitionSpec: Optional[PartitionSpecOutput] = None
    S3ErrorOutputPrefix: Optional[str] = None


class ProcessorOutput(BaseValidatorModel):
    pass


class ProcessingConfigurationOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Processors: Optional[List[ProcessorOutput]] = None


class DatabaseSourceDescription(BaseValidatorModel):
    pass


class SourceDescription(BaseValidatorModel):
    DirectPutSourceDescription: Optional[DirectPutSourceDescription] = None
    KinesisStreamSourceDescription: Optional[KinesisStreamSourceDescription] = None
    MSKSourceDescription: Optional[MSKSourceDescription] = None
    DatabaseSourceDescription: Optional[DatabaseSourceDescription] = None


class DataFormatConversionConfigurationOutput(BaseValidatorModel):
    SchemaConfiguration: Optional[SchemaConfiguration] = None
    InputFormatConfiguration: Optional[InputFormatConfigurationOutput] = None
    OutputFormatConfiguration: Optional[OutputFormatConfigurationOutput] = None
    Enabled: Optional[bool] = None


class PartitionSpecUnion(BaseValidatorModel):
    pass


class DestinationTableConfiguration(BaseValidatorModel):
    DestinationTableName: str
    DestinationDatabaseName: str
    UniqueKeys: Optional[Sequence[str]] = None
    PartitionSpec: Optional[PartitionSpecUnion] = None
    S3ErrorOutputPrefix: Optional[str] = None


class AmazonOpenSearchServerlessDestinationDescription(BaseValidatorModel):
    RoleARN: Optional[str] = None
    CollectionEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHints] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptions] = None
    S3BackupMode: Optional[AmazonOpenSearchServerlessS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    VpcConfigurationDescription: Optional[VpcConfigurationDescription] = None


class AmazonopensearchserviceDestinationDescription(BaseValidatorModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[AmazonopensearchserviceIndexRotationPeriodType] = None
    BufferingHints: Optional[AmazonopensearchserviceBufferingHints] = None
    RetryOptions: Optional[AmazonopensearchserviceRetryOptions] = None
    S3BackupMode: Optional[AmazonopensearchserviceS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    VpcConfigurationDescription: Optional[VpcConfigurationDescription] = None
    DocumentIdOptions: Optional[DocumentIdOptions] = None


class ElasticsearchDestinationDescription(BaseValidatorModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[ElasticsearchIndexRotationPeriodType] = None
    BufferingHints: Optional[ElasticsearchBufferingHints] = None
    RetryOptions: Optional[ElasticsearchRetryOptions] = None
    S3BackupMode: Optional[ElasticsearchS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    VpcConfigurationDescription: Optional[VpcConfigurationDescription] = None
    DocumentIdOptions: Optional[DocumentIdOptions] = None


class HttpEndpointDestinationDescription(BaseValidatorModel):
    EndpointConfiguration: Optional[HttpEndpointDescription] = None
    BufferingHints: Optional[HttpEndpointBufferingHints] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    RequestConfiguration: Optional[HttpEndpointRequestConfigurationOutput] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[HttpEndpointRetryOptions] = None
    S3BackupMode: Optional[HttpEndpointS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class IcebergDestinationDescription(BaseValidatorModel):
    DestinationTableConfigurationList: Optional[List[DestinationTableConfigurationOutput]] = None
    SchemaEvolutionConfiguration: Optional[SchemaEvolutionConfiguration] = None
    TableCreationConfiguration: Optional[TableCreationConfiguration] = None
    BufferingHints: Optional[BufferingHints] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    S3BackupMode: Optional[IcebergS3BackupModeType] = None
    RetryOptions: Optional[RetryOptions] = None
    RoleARN: Optional[str] = None
    AppendOnly: Optional[bool] = None
    CatalogConfiguration: Optional[CatalogConfiguration] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None


class RedshiftDestinationDescription(BaseValidatorModel):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: CopyCommand
    S3DestinationDescription: S3DestinationDescription
    Username: Optional[str] = None
    RetryOptions: Optional[RedshiftRetryOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    S3BackupMode: Optional[RedshiftS3BackupModeType] = None
    S3BackupDescription: Optional[S3DestinationDescription] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class SnowflakeDestinationDescription(BaseValidatorModel):
    AccountUrl: Optional[str] = None
    User: Optional[str] = None
    Database: Optional[str] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    SnowflakeRoleConfiguration: Optional[SnowflakeRoleConfiguration] = None
    DataLoadingOption: Optional[SnowflakeDataLoadingOptionType] = None
    MetaDataColumnName: Optional[str] = None
    ContentColumnName: Optional[str] = None
    SnowflakeVpcConfiguration: Optional[SnowflakeVpcConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[SnowflakeRetryOptions] = None
    S3BackupMode: Optional[SnowflakeS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None
    BufferingHints: Optional[SnowflakeBufferingHints] = None


class SplunkDestinationDescription(BaseValidatorModel):
    HECEndpoint: Optional[str] = None
    HECEndpointType: Optional[HECEndpointTypeType] = None
    HECToken: Optional[str] = None
    HECAcknowledgmentTimeoutInSeconds: Optional[int] = None
    RetryOptions: Optional[SplunkRetryOptions] = None
    S3BackupMode: Optional[SplunkS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    BufferingHints: Optional[SplunkBufferingHints] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class ProcessorUnion(BaseValidatorModel):
    pass


class ProcessingConfiguration(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Processors: Optional[Sequence[ProcessorUnion]] = None


class DeserializerUnion(BaseValidatorModel):
    pass


class InputFormatConfiguration(BaseValidatorModel):
    Deserializer: Optional[DeserializerUnion] = None


class SerializerUnion(BaseValidatorModel):
    pass


class OutputFormatConfiguration(BaseValidatorModel):
    Serializer: Optional[SerializerUnion] = None


class ExtendedS3DestinationDescription(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHints
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfiguration
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutput] = None
    S3BackupMode: Optional[S3BackupModeType] = None
    S3BackupDescription: Optional[S3DestinationDescription] = None
    DataFormatConversionConfiguration: Optional[DataFormatConversionConfigurationOutput] = None
    DynamicPartitioningConfiguration: Optional[DynamicPartitioningConfiguration] = None
    FileExtension: Optional[str] = None
    CustomTimeZone: Optional[str] = None


class DestinationDescription(BaseValidatorModel):
    DestinationId: str
    S3DestinationDescription: Optional[S3DestinationDescription] = None
    ExtendedS3DestinationDescription: Optional[ExtendedS3DestinationDescription] = None
    RedshiftDestinationDescription: Optional[RedshiftDestinationDescription] = None
    ElasticsearchDestinationDescription: Optional[ElasticsearchDestinationDescription] = None
    AmazonopensearchserviceDestinationDescription: Optional[ AmazonopensearchserviceDestinationDescription ] = None
    SplunkDestinationDescription: Optional[SplunkDestinationDescription] = None
    HttpEndpointDestinationDescription: Optional[HttpEndpointDestinationDescription] = None
    SnowflakeDestinationDescription: Optional[SnowflakeDestinationDescription] = None
    AmazonOpenSearchServerlessDestinationDescription: Optional[ AmazonOpenSearchServerlessDestinationDescription ] = None
    IcebergDestinationDescription: Optional[IcebergDestinationDescription] = None


class ProcessingConfigurationUnion(BaseValidatorModel):
    pass


class AmazonOpenSearchServerlessDestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfiguration
    CollectionEndpoint: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHints] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptions] = None
    S3BackupMode: Optional[AmazonOpenSearchServerlessS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    VpcConfiguration: Optional[VpcConfiguration] = None


class AmazonOpenSearchServerlessDestinationUpdate(BaseValidatorModel):
    RoleARN: Optional[str] = None
    CollectionEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHints] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptions] = None
    S3Update: Optional[S3DestinationUpdate] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None


class AmazonopensearchserviceDestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfiguration
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[AmazonopensearchserviceIndexRotationPeriodType] = None
    BufferingHints: Optional[AmazonopensearchserviceBufferingHints] = None
    RetryOptions: Optional[AmazonopensearchserviceRetryOptions] = None
    S3BackupMode: Optional[AmazonopensearchserviceS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    VpcConfiguration: Optional[VpcConfiguration] = None
    DocumentIdOptions: Optional[DocumentIdOptions] = None


class AmazonopensearchserviceDestinationUpdate(BaseValidatorModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[AmazonopensearchserviceIndexRotationPeriodType] = None
    BufferingHints: Optional[AmazonopensearchserviceBufferingHints] = None
    RetryOptions: Optional[AmazonopensearchserviceRetryOptions] = None
    S3Update: Optional[S3DestinationUpdate] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    DocumentIdOptions: Optional[DocumentIdOptions] = None


class ElasticsearchDestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfiguration
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[ElasticsearchIndexRotationPeriodType] = None
    BufferingHints: Optional[ElasticsearchBufferingHints] = None
    RetryOptions: Optional[ElasticsearchRetryOptions] = None
    S3BackupMode: Optional[ElasticsearchS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    VpcConfiguration: Optional[VpcConfiguration] = None
    DocumentIdOptions: Optional[DocumentIdOptions] = None


class ElasticsearchDestinationUpdate(BaseValidatorModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[ElasticsearchIndexRotationPeriodType] = None
    BufferingHints: Optional[ElasticsearchBufferingHints] = None
    RetryOptions: Optional[ElasticsearchRetryOptions] = None
    S3Update: Optional[S3DestinationUpdate] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    DocumentIdOptions: Optional[DocumentIdOptions] = None


class HttpEndpointRequestConfigurationUnion(BaseValidatorModel):
    pass


class HttpEndpointDestinationConfiguration(BaseValidatorModel):
    EndpointConfiguration: HttpEndpointConfiguration
    S3Configuration: S3DestinationConfiguration
    BufferingHints: Optional[HttpEndpointBufferingHints] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    RequestConfiguration: Optional[HttpEndpointRequestConfigurationUnion] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[HttpEndpointRetryOptions] = None
    S3BackupMode: Optional[HttpEndpointS3BackupModeType] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class HttpEndpointDestinationUpdate(BaseValidatorModel):
    EndpointConfiguration: Optional[HttpEndpointConfiguration] = None
    BufferingHints: Optional[HttpEndpointBufferingHints] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    RequestConfiguration: Optional[HttpEndpointRequestConfigurationUnion] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[HttpEndpointRetryOptions] = None
    S3BackupMode: Optional[HttpEndpointS3BackupModeType] = None
    S3Update: Optional[S3DestinationUpdate] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class DestinationTableConfigurationUnion(BaseValidatorModel):
    pass


class IcebergDestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    CatalogConfiguration: CatalogConfiguration
    S3Configuration: S3DestinationConfiguration
    DestinationTableConfigurationList: Optional[ Sequence[DestinationTableConfigurationUnion] ] = None
    SchemaEvolutionConfiguration: Optional[SchemaEvolutionConfiguration] = None
    TableCreationConfiguration: Optional[TableCreationConfiguration] = None
    BufferingHints: Optional[BufferingHints] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    S3BackupMode: Optional[IcebergS3BackupModeType] = None
    RetryOptions: Optional[RetryOptions] = None
    AppendOnly: Optional[bool] = None


class IcebergDestinationUpdate(BaseValidatorModel):
    DestinationTableConfigurationList: Optional[ Sequence[DestinationTableConfigurationUnion] ] = None
    SchemaEvolutionConfiguration: Optional[SchemaEvolutionConfiguration] = None
    TableCreationConfiguration: Optional[TableCreationConfiguration] = None
    BufferingHints: Optional[BufferingHints] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    S3BackupMode: Optional[IcebergS3BackupModeType] = None
    RetryOptions: Optional[RetryOptions] = None
    RoleARN: Optional[str] = None
    AppendOnly: Optional[bool] = None
    CatalogConfiguration: Optional[CatalogConfiguration] = None
    S3Configuration: Optional[S3DestinationConfiguration] = None


class RedshiftDestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: CopyCommand
    S3Configuration: S3DestinationConfiguration
    Username: Optional[str] = None
    Password: Optional[str] = None
    RetryOptions: Optional[RedshiftRetryOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    S3BackupMode: Optional[RedshiftS3BackupModeType] = None
    S3BackupConfiguration: Optional[S3DestinationConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class RedshiftDestinationUpdate(BaseValidatorModel):
    RoleARN: Optional[str] = None
    ClusterJDBCURL: Optional[str] = None
    CopyCommand: Optional[CopyCommand] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    RetryOptions: Optional[RedshiftRetryOptions] = None
    S3Update: Optional[S3DestinationUpdate] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    S3BackupMode: Optional[RedshiftS3BackupModeType] = None
    S3BackupUpdate: Optional[S3DestinationUpdate] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class SnowflakeDestinationConfiguration(BaseValidatorModel):
    AccountUrl: str
    Database: str
    Schema: str
    Table: str
    RoleARN: str
    S3Configuration: S3DestinationConfiguration
    PrivateKey: Optional[str] = None
    KeyPassphrase: Optional[str] = None
    User: Optional[str] = None
    SnowflakeRoleConfiguration: Optional[SnowflakeRoleConfiguration] = None
    DataLoadingOption: Optional[SnowflakeDataLoadingOptionType] = None
    MetaDataColumnName: Optional[str] = None
    ContentColumnName: Optional[str] = None
    SnowflakeVpcConfiguration: Optional[SnowflakeVpcConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    RetryOptions: Optional[SnowflakeRetryOptions] = None
    S3BackupMode: Optional[SnowflakeS3BackupModeType] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None
    BufferingHints: Optional[SnowflakeBufferingHints] = None


class SnowflakeDestinationUpdate(BaseValidatorModel):
    AccountUrl: Optional[str] = None
    PrivateKey: Optional[str] = None
    KeyPassphrase: Optional[str] = None
    User: Optional[str] = None
    Database: Optional[str] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    SnowflakeRoleConfiguration: Optional[SnowflakeRoleConfiguration] = None
    DataLoadingOption: Optional[SnowflakeDataLoadingOptionType] = None
    MetaDataColumnName: Optional[str] = None
    ContentColumnName: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[SnowflakeRetryOptions] = None
    S3BackupMode: Optional[SnowflakeS3BackupModeType] = None
    S3Update: Optional[S3DestinationUpdate] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None
    BufferingHints: Optional[SnowflakeBufferingHints] = None


class SplunkDestinationConfiguration(BaseValidatorModel):
    HECEndpoint: str
    HECEndpointType: HECEndpointTypeType
    S3Configuration: S3DestinationConfiguration
    HECToken: Optional[str] = None
    HECAcknowledgmentTimeoutInSeconds: Optional[int] = None
    RetryOptions: Optional[SplunkRetryOptions] = None
    S3BackupMode: Optional[SplunkS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    BufferingHints: Optional[SplunkBufferingHints] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class SplunkDestinationUpdate(BaseValidatorModel):
    HECEndpoint: Optional[str] = None
    HECEndpointType: Optional[HECEndpointTypeType] = None
    HECToken: Optional[str] = None
    HECAcknowledgmentTimeoutInSeconds: Optional[int] = None
    RetryOptions: Optional[SplunkRetryOptions] = None
    S3BackupMode: Optional[SplunkS3BackupModeType] = None
    S3Update: Optional[S3DestinationUpdate] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    BufferingHints: Optional[SplunkBufferingHints] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfiguration] = None


class OutputFormatConfigurationUnion(BaseValidatorModel):
    pass


class InputFormatConfigurationUnion(BaseValidatorModel):
    pass


class DataFormatConversionConfiguration(BaseValidatorModel):
    SchemaConfiguration: Optional[SchemaConfiguration] = None
    InputFormatConfiguration: Optional[InputFormatConfigurationUnion] = None
    OutputFormatConfiguration: Optional[OutputFormatConfigurationUnion] = None
    Enabled: Optional[bool] = None


class DeliveryStreamDescription(BaseValidatorModel):
    DeliveryStreamName: str
    DeliveryStreamARN: str
    DeliveryStreamStatus: DeliveryStreamStatusType
    DeliveryStreamType: DeliveryStreamTypeType
    VersionId: str
    Destinations: List[DestinationDescription]
    HasMoreDestinations: bool
    FailureDescription: Optional[FailureDescription] = None
    DeliveryStreamEncryptionConfiguration: Optional[DeliveryStreamEncryptionConfiguration] = None
    CreateTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    Source: Optional[SourceDescription] = None


class DescribeDeliveryStreamOutput(BaseValidatorModel):
    DeliveryStreamDescription: DeliveryStreamDescription
    ResponseMetadata: ResponseMetadata


class DataFormatConversionConfigurationUnion(BaseValidatorModel):
    pass


class ExtendedS3DestinationConfiguration(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHints] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    S3BackupMode: Optional[S3BackupModeType] = None
    S3BackupConfiguration: Optional[S3DestinationConfiguration] = None
    DataFormatConversionConfiguration: Optional[DataFormatConversionConfigurationUnion] = None
    DynamicPartitioningConfiguration: Optional[DynamicPartitioningConfiguration] = None
    FileExtension: Optional[str] = None
    CustomTimeZone: Optional[str] = None


class ExtendedS3DestinationUpdate(BaseValidatorModel):
    RoleARN: Optional[str] = None
    BucketARN: Optional[str] = None
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHints] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptions] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationUnion] = None
    S3BackupMode: Optional[S3BackupModeType] = None
    S3BackupUpdate: Optional[S3DestinationUpdate] = None
    DataFormatConversionConfiguration: Optional[DataFormatConversionConfigurationUnion] = None
    DynamicPartitioningConfiguration: Optional[DynamicPartitioningConfiguration] = None
    FileExtension: Optional[str] = None
    CustomTimeZone: Optional[str] = None


class DatabaseSourceConfiguration(BaseValidatorModel):
    pass


class CreateDeliveryStreamInput(BaseValidatorModel):
    DeliveryStreamName: str
    DeliveryStreamType: Optional[DeliveryStreamTypeType] = None
    DirectPutSourceConfiguration: Optional[DirectPutSourceConfiguration] = None
    KinesisStreamSourceConfiguration: Optional[KinesisStreamSourceConfiguration] = None
    DeliveryStreamEncryptionConfigurationInput: Optional[ DeliveryStreamEncryptionConfigurationInput ] = None
    S3DestinationConfiguration: Optional[S3DestinationConfiguration] = None
    ExtendedS3DestinationConfiguration: Optional[ExtendedS3DestinationConfiguration] = None
    RedshiftDestinationConfiguration: Optional[RedshiftDestinationConfiguration] = None
    ElasticsearchDestinationConfiguration: Optional[ElasticsearchDestinationConfiguration] = None
    AmazonopensearchserviceDestinationConfiguration: Optional[ AmazonopensearchserviceDestinationConfiguration ] = None
    SplunkDestinationConfiguration: Optional[SplunkDestinationConfiguration] = None
    HttpEndpointDestinationConfiguration: Optional[HttpEndpointDestinationConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None
    AmazonOpenSearchServerlessDestinationConfiguration: Optional[ AmazonOpenSearchServerlessDestinationConfiguration ] = None
    MSKSourceConfiguration: Optional[MSKSourceConfiguration] = None
    SnowflakeDestinationConfiguration: Optional[SnowflakeDestinationConfiguration] = None
    IcebergDestinationConfiguration: Optional[IcebergDestinationConfiguration] = None
    DatabaseSourceConfiguration: Optional[DatabaseSourceConfiguration] = None


class UpdateDestinationInput(BaseValidatorModel):
    DeliveryStreamName: str
    CurrentDeliveryStreamVersionId: str
    DestinationId: str
    S3DestinationUpdate: Optional[S3DestinationUpdate] = None
    ExtendedS3DestinationUpdate: Optional[ExtendedS3DestinationUpdate] = None
    RedshiftDestinationUpdate: Optional[RedshiftDestinationUpdate] = None
    ElasticsearchDestinationUpdate: Optional[ElasticsearchDestinationUpdate] = None
    AmazonopensearchserviceDestinationUpdate: Optional[ AmazonopensearchserviceDestinationUpdate ] = None
    SplunkDestinationUpdate: Optional[SplunkDestinationUpdate] = None
    HttpEndpointDestinationUpdate: Optional[HttpEndpointDestinationUpdate] = None
    AmazonOpenSearchServerlessDestinationUpdate: Optional[ AmazonOpenSearchServerlessDestinationUpdate ] = None
    SnowflakeDestinationUpdate: Optional[SnowflakeDestinationUpdate] = None
    IcebergDestinationUpdate: Optional[IcebergDestinationUpdate] = None


