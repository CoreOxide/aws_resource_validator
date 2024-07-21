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
from aws_resource_validator.pydantic_models.firehose_constants import *

class AmazonOpenSearchServerlessBufferingHintsTypeDef(BaseModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class AmazonOpenSearchServerlessRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class CloudWatchLoggingOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LogGroupName: Optional[str] = None
    LogStreamName: Optional[str] = None

class VpcConfigurationTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    RoleARN: str
    SecurityGroupIds: Sequence[str]

class VpcConfigurationDescriptionTypeDef(BaseModel):
    SubnetIds: List[str]
    RoleARN: str
    SecurityGroupIds: List[str]
    VpcId: str

class AmazonopensearchserviceBufferingHintsTypeDef(BaseModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class AmazonopensearchserviceRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class DocumentIdOptionsTypeDef(BaseModel):
    DefaultDocumentIdFormat: DefaultDocumentIdFormatType

class AuthenticationConfigurationTypeDef(BaseModel):
    RoleARN: str
    Connectivity: ConnectivityType

class BufferingHintsTypeDef(BaseModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None

class CopyCommandTypeDef(BaseModel):
    DataTableName: str
    DataTableColumns: Optional[str] = None
    CopyOptions: Optional[str] = None

class DeliveryStreamEncryptionConfigurationInputTypeDef(BaseModel):
    KeyType: KeyTypeType
    KeyARN: Optional[str] = None

class KinesisStreamSourceConfigurationTypeDef(BaseModel):
    KinesisStreamARN: str
    RoleARN: str

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SchemaConfigurationTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Region: Optional[str] = None
    VersionId: Optional[str] = None

class DeleteDeliveryStreamInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    AllowForceDelete: Optional[bool] = None

class FailureDescriptionTypeDef(BaseModel):
    Type: DeliveryStreamFailureTypeType
    Details: str

class DescribeDeliveryStreamInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    Limit: Optional[int] = None
    ExclusiveStartDestinationId: Optional[str] = None

class HiveJsonSerDeOutputTypeDef(BaseModel):
    TimestampFormats: Optional[List[str]] = None

class OpenXJsonSerDeOutputTypeDef(BaseModel):
    ConvertDotsInJsonKeysToUnderscores: Optional[bool] = None
    CaseInsensitive: Optional[bool] = None
    ColumnToJsonKeyMappings: Optional[Dict[str, str]] = None

class HiveJsonSerDeTypeDef(BaseModel):
    TimestampFormats: Optional[Sequence[str]] = None

class OpenXJsonSerDeTypeDef(BaseModel):
    ConvertDotsInJsonKeysToUnderscores: Optional[bool] = None
    CaseInsensitive: Optional[bool] = None
    ColumnToJsonKeyMappings: Optional[Mapping[str, str]] = None

class RetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class ElasticsearchBufferingHintsTypeDef(BaseModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class ElasticsearchRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class KMSEncryptionConfigTypeDef(BaseModel):
    AWSKMSKeyARN: str

class HttpEndpointBufferingHintsTypeDef(BaseModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None

class HttpEndpointCommonAttributeTypeDef(BaseModel):
    AttributeName: str
    AttributeValue: str

class HttpEndpointConfigurationTypeDef(BaseModel):
    Url: str
    Name: Optional[str] = None
    AccessKey: Optional[str] = None

class HttpEndpointDescriptionTypeDef(BaseModel):
    Url: Optional[str] = None
    Name: Optional[str] = None

class HttpEndpointRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class SecretsManagerConfigurationTypeDef(BaseModel):
    Enabled: bool
    SecretARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisStreamSourceDescriptionTypeDef(BaseModel):
    KinesisStreamARN: Optional[str] = None
    RoleARN: Optional[str] = None
    DeliveryStartTimestamp: Optional[datetime] = None

class ListDeliveryStreamsInputRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    DeliveryStreamType: Optional[DeliveryStreamTypeType] = None
    ExclusiveStartDeliveryStreamName: Optional[str] = None

class ListTagsForDeliveryStreamInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None

class OrcSerDeOutputTypeDef(BaseModel):
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

class OrcSerDeTypeDef(BaseModel):
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

class ParquetSerDeTypeDef(BaseModel):
    BlockSizeBytes: Optional[int] = None
    PageSizeBytes: Optional[int] = None
    Compression: Optional[ParquetCompressionType] = None
    EnableDictionaryCompression: Optional[bool] = None
    MaxPaddingBytes: Optional[int] = None
    WriterVersion: Optional[ParquetWriterVersionType] = None

class ProcessorParameterTypeDef(BaseModel):
    ParameterName: ProcessorParameterNameType
    ParameterValue: str

class PutRecordBatchResponseEntryTypeDef(BaseModel):
    RecordId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class RedshiftRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class SnowflakeRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class SnowflakeRoleConfigurationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    SnowflakeRole: Optional[str] = None

class SnowflakeVpcConfigurationTypeDef(BaseModel):
    PrivateLinkVpceId: str

class SplunkBufferingHintsTypeDef(BaseModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class SplunkRetryOptionsTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None

class StopDeliveryStreamEncryptionInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str

class UntagDeliveryStreamInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    TagKeys: Sequence[str]

class MSKSourceConfigurationTypeDef(BaseModel):
    MSKClusterARN: str
    TopicName: str
    AuthenticationConfiguration: AuthenticationConfigurationTypeDef

class MSKSourceDescriptionTypeDef(BaseModel):
    MSKClusterARN: Optional[str] = None
    TopicName: Optional[str] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None
    DeliveryStartTimestamp: Optional[datetime] = None

class RecordTypeDef(BaseModel):
    Data: BlobTypeDef

class StartDeliveryStreamEncryptionInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    DeliveryStreamEncryptionConfigurationInput: Optional[       DeliveryStreamEncryptionConfigurationInputTypeDef     ] = None

class TagDeliveryStreamInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    Tags: Sequence[TagTypeDef]

class CreateDeliveryStreamOutputTypeDef(BaseModel):
    DeliveryStreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeliveryStreamsOutputTypeDef(BaseModel):
    DeliveryStreamNames: List[str]
    HasMoreDeliveryStreams: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForDeliveryStreamOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordOutputTypeDef(BaseModel):
    RecordId: str
    Encrypted: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeliveryStreamEncryptionConfigurationTypeDef(BaseModel):
    KeyARN: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Status: Optional[DeliveryStreamEncryptionStatusType] = None
    FailureDescription: Optional[FailureDescriptionTypeDef] = None

class DeserializerOutputTypeDef(BaseModel):
    OpenXJsonSerDe: Optional[OpenXJsonSerDeOutputTypeDef] = None
    HiveJsonSerDe: Optional[HiveJsonSerDeOutputTypeDef] = None

class DeserializerTypeDef(BaseModel):
    OpenXJsonSerDe: Optional[OpenXJsonSerDeTypeDef] = None
    HiveJsonSerDe: Optional[HiveJsonSerDeTypeDef] = None

class DynamicPartitioningConfigurationTypeDef(BaseModel):
    RetryOptions: Optional[RetryOptionsTypeDef] = None
    Enabled: Optional[bool] = None

class EncryptionConfigurationTypeDef(BaseModel):
    NoEncryptionConfig: Optional[Literal["NoEncryption"]] = None
    KMSEncryptionConfig: Optional[KMSEncryptionConfigTypeDef] = None

class HttpEndpointRequestConfigurationOutputTypeDef(BaseModel):
    ContentEncoding: Optional[ContentEncodingType] = None
    CommonAttributes: Optional[List[HttpEndpointCommonAttributeTypeDef]] = None

class HttpEndpointRequestConfigurationTypeDef(BaseModel):
    ContentEncoding: Optional[ContentEncodingType] = None
    CommonAttributes: Optional[Sequence[HttpEndpointCommonAttributeTypeDef]] = None

class SerializerOutputTypeDef(BaseModel):
    ParquetSerDe: Optional[ParquetSerDeTypeDef] = None
    OrcSerDe: Optional[OrcSerDeOutputTypeDef] = None

class SerializerTypeDef(BaseModel):
    ParquetSerDe: Optional[ParquetSerDeTypeDef] = None
    OrcSerDe: Optional[OrcSerDeTypeDef] = None

class ProcessorOutputTypeDef(BaseModel):
    Type: ProcessorTypeType
    Parameters: Optional[List[ProcessorParameterTypeDef]] = None

class ProcessorTypeDef(BaseModel):
    Type: ProcessorTypeType
    Parameters: Optional[Sequence[ProcessorParameterTypeDef]] = None

class PutRecordBatchOutputTypeDef(BaseModel):
    FailedPutCount: int
    Encrypted: bool
    RequestResponses: List[PutRecordBatchResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SourceDescriptionTypeDef(BaseModel):
    KinesisStreamSourceDescription: Optional[KinesisStreamSourceDescriptionTypeDef] = None
    MSKSourceDescription: Optional[MSKSourceDescriptionTypeDef] = None

class PutRecordBatchInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    Records: Sequence[RecordTypeDef]

class PutRecordInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    Record: RecordTypeDef

class InputFormatConfigurationOutputTypeDef(BaseModel):
    Deserializer: Optional[DeserializerOutputTypeDef] = None

class InputFormatConfigurationTypeDef(BaseModel):
    Deserializer: Optional[DeserializerTypeDef] = None

class S3DestinationConfigurationTypeDef(BaseModel):
    RoleARN: str
    BucketARN: str
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHintsTypeDef] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class S3DestinationDescriptionTypeDef(BaseModel):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHintsTypeDef
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class S3DestinationUpdateTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    BucketARN: Optional[str] = None
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHintsTypeDef] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class OutputFormatConfigurationOutputTypeDef(BaseModel):
    Serializer: Optional[SerializerOutputTypeDef] = None

class OutputFormatConfigurationTypeDef(BaseModel):
    Serializer: Optional[SerializerTypeDef] = None

class ProcessingConfigurationOutputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Processors: Optional[List[ProcessorOutputTypeDef]] = None

class ProcessingConfigurationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    Processors: Optional[Sequence[ProcessorTypeDef]] = None

class DataFormatConversionConfigurationOutputTypeDef(BaseModel):
    SchemaConfiguration: Optional[SchemaConfigurationTypeDef] = None
    InputFormatConfiguration: Optional[InputFormatConfigurationOutputTypeDef] = None
    OutputFormatConfiguration: Optional[OutputFormatConfigurationOutputTypeDef] = None
    Enabled: Optional[bool] = None

class DataFormatConversionConfigurationTypeDef(BaseModel):
    SchemaConfiguration: Optional[SchemaConfigurationTypeDef] = None
    InputFormatConfiguration: Optional[InputFormatConfigurationTypeDef] = None
    OutputFormatConfiguration: Optional[OutputFormatConfigurationTypeDef] = None
    Enabled: Optional[bool] = None

class AmazonOpenSearchServerlessDestinationDescriptionTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    CollectionEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptionsTypeDef] = None
    S3BackupMode: Optional[AmazonOpenSearchServerlessS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    VpcConfigurationDescription: Optional[VpcConfigurationDescriptionTypeDef] = None

class AmazonopensearchserviceDestinationDescriptionTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[AmazonopensearchserviceIndexRotationPeriodType] = None
    BufferingHints: Optional[AmazonopensearchserviceBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonopensearchserviceRetryOptionsTypeDef] = None
    S3BackupMode: Optional[AmazonopensearchserviceS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    VpcConfigurationDescription: Optional[VpcConfigurationDescriptionTypeDef] = None
    DocumentIdOptions: Optional[DocumentIdOptionsTypeDef] = None

class ElasticsearchDestinationDescriptionTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[ElasticsearchIndexRotationPeriodType] = None
    BufferingHints: Optional[ElasticsearchBufferingHintsTypeDef] = None
    RetryOptions: Optional[ElasticsearchRetryOptionsTypeDef] = None
    S3BackupMode: Optional[ElasticsearchS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    VpcConfigurationDescription: Optional[VpcConfigurationDescriptionTypeDef] = None
    DocumentIdOptions: Optional[DocumentIdOptionsTypeDef] = None

class HttpEndpointDestinationDescriptionTypeDef(BaseModel):
    EndpointConfiguration: Optional[HttpEndpointDescriptionTypeDef] = None
    BufferingHints: Optional[HttpEndpointBufferingHintsTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    RequestConfiguration: Optional[HttpEndpointRequestConfigurationOutputTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[HttpEndpointRetryOptionsTypeDef] = None
    S3BackupMode: Optional[HttpEndpointS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class RedshiftDestinationDescriptionTypeDef(BaseModel):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: CopyCommandTypeDef
    S3DestinationDescription: S3DestinationDescriptionTypeDef
    Username: Optional[str] = None
    RetryOptions: Optional[RedshiftRetryOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    S3BackupMode: Optional[RedshiftS3BackupModeType] = None
    S3BackupDescription: Optional[S3DestinationDescriptionTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class SnowflakeDestinationDescriptionTypeDef(BaseModel):
    AccountUrl: Optional[str] = None
    User: Optional[str] = None
    Database: Optional[str] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    SnowflakeRoleConfiguration: Optional[SnowflakeRoleConfigurationTypeDef] = None
    DataLoadingOption: Optional[SnowflakeDataLoadingOptionType] = None
    MetaDataColumnName: Optional[str] = None
    ContentColumnName: Optional[str] = None
    SnowflakeVpcConfiguration: Optional[SnowflakeVpcConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[SnowflakeRetryOptionsTypeDef] = None
    S3BackupMode: Optional[SnowflakeS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class SplunkDestinationDescriptionTypeDef(BaseModel):
    HECEndpoint: Optional[str] = None
    HECEndpointType: Optional[HECEndpointTypeType] = None
    HECToken: Optional[str] = None
    HECAcknowledgmentTimeoutInSeconds: Optional[int] = None
    RetryOptions: Optional[SplunkRetryOptionsTypeDef] = None
    S3BackupMode: Optional[SplunkS3BackupModeType] = None
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    BufferingHints: Optional[SplunkBufferingHintsTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class AmazonOpenSearchServerlessDestinationConfigurationTypeDef(BaseModel):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfigurationTypeDef
    CollectionEndpoint: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptionsTypeDef] = None
    S3BackupMode: Optional[AmazonOpenSearchServerlessS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class AmazonOpenSearchServerlessDestinationUpdateTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    CollectionEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptionsTypeDef] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class AmazonopensearchserviceDestinationConfigurationTypeDef(BaseModel):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfigurationTypeDef
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[AmazonopensearchserviceIndexRotationPeriodType] = None
    BufferingHints: Optional[AmazonopensearchserviceBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonopensearchserviceRetryOptionsTypeDef] = None
    S3BackupMode: Optional[AmazonopensearchserviceS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    DocumentIdOptions: Optional[DocumentIdOptionsTypeDef] = None

class AmazonopensearchserviceDestinationUpdateTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[AmazonopensearchserviceIndexRotationPeriodType] = None
    BufferingHints: Optional[AmazonopensearchserviceBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonopensearchserviceRetryOptionsTypeDef] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    DocumentIdOptions: Optional[DocumentIdOptionsTypeDef] = None

class ElasticsearchDestinationConfigurationTypeDef(BaseModel):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfigurationTypeDef
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[ElasticsearchIndexRotationPeriodType] = None
    BufferingHints: Optional[ElasticsearchBufferingHintsTypeDef] = None
    RetryOptions: Optional[ElasticsearchRetryOptionsTypeDef] = None
    S3BackupMode: Optional[ElasticsearchS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    DocumentIdOptions: Optional[DocumentIdOptionsTypeDef] = None

class ElasticsearchDestinationUpdateTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    DomainARN: Optional[str] = None
    ClusterEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    TypeName: Optional[str] = None
    IndexRotationPeriod: Optional[ElasticsearchIndexRotationPeriodType] = None
    BufferingHints: Optional[ElasticsearchBufferingHintsTypeDef] = None
    RetryOptions: Optional[ElasticsearchRetryOptionsTypeDef] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    DocumentIdOptions: Optional[DocumentIdOptionsTypeDef] = None

class HttpEndpointDestinationConfigurationTypeDef(BaseModel):
    EndpointConfiguration: HttpEndpointConfigurationTypeDef
    S3Configuration: S3DestinationConfigurationTypeDef
    BufferingHints: Optional[HttpEndpointBufferingHintsTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    RequestConfiguration: Optional[HttpEndpointRequestConfigurationTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[HttpEndpointRetryOptionsTypeDef] = None
    S3BackupMode: Optional[HttpEndpointS3BackupModeType] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class HttpEndpointDestinationUpdateTypeDef(BaseModel):
    EndpointConfiguration: Optional[HttpEndpointConfigurationTypeDef] = None
    BufferingHints: Optional[HttpEndpointBufferingHintsTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    RequestConfiguration: Optional[HttpEndpointRequestConfigurationTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[HttpEndpointRetryOptionsTypeDef] = None
    S3BackupMode: Optional[HttpEndpointS3BackupModeType] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class RedshiftDestinationConfigurationTypeDef(BaseModel):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: CopyCommandTypeDef
    S3Configuration: S3DestinationConfigurationTypeDef
    Username: Optional[str] = None
    Password: Optional[str] = None
    RetryOptions: Optional[RedshiftRetryOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    S3BackupMode: Optional[RedshiftS3BackupModeType] = None
    S3BackupConfiguration: Optional[S3DestinationConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class RedshiftDestinationUpdateTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    ClusterJDBCURL: Optional[str] = None
    CopyCommand: Optional[CopyCommandTypeDef] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    RetryOptions: Optional[RedshiftRetryOptionsTypeDef] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    S3BackupMode: Optional[RedshiftS3BackupModeType] = None
    S3BackupUpdate: Optional[S3DestinationUpdateTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class SnowflakeDestinationConfigurationTypeDef(BaseModel):
    AccountUrl: str
    Database: str
    Schema: str
    Table: str
    RoleARN: str
    S3Configuration: S3DestinationConfigurationTypeDef
    PrivateKey: Optional[str] = None
    KeyPassphrase: Optional[str] = None
    User: Optional[str] = None
    SnowflakeRoleConfiguration: Optional[SnowflakeRoleConfigurationTypeDef] = None
    DataLoadingOption: Optional[SnowflakeDataLoadingOptionType] = None
    MetaDataColumnName: Optional[str] = None
    ContentColumnName: Optional[str] = None
    SnowflakeVpcConfiguration: Optional[SnowflakeVpcConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    RetryOptions: Optional[SnowflakeRetryOptionsTypeDef] = None
    S3BackupMode: Optional[SnowflakeS3BackupModeType] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class SnowflakeDestinationUpdateTypeDef(BaseModel):
    AccountUrl: Optional[str] = None
    PrivateKey: Optional[str] = None
    KeyPassphrase: Optional[str] = None
    User: Optional[str] = None
    Database: Optional[str] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    SnowflakeRoleConfiguration: Optional[SnowflakeRoleConfigurationTypeDef] = None
    DataLoadingOption: Optional[SnowflakeDataLoadingOptionType] = None
    MetaDataColumnName: Optional[str] = None
    ContentColumnName: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    RoleARN: Optional[str] = None
    RetryOptions: Optional[SnowflakeRetryOptionsTypeDef] = None
    S3BackupMode: Optional[SnowflakeS3BackupModeType] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class SplunkDestinationConfigurationTypeDef(BaseModel):
    HECEndpoint: str
    HECEndpointType: HECEndpointTypeType
    S3Configuration: S3DestinationConfigurationTypeDef
    HECToken: Optional[str] = None
    HECAcknowledgmentTimeoutInSeconds: Optional[int] = None
    RetryOptions: Optional[SplunkRetryOptionsTypeDef] = None
    S3BackupMode: Optional[SplunkS3BackupModeType] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    BufferingHints: Optional[SplunkBufferingHintsTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class SplunkDestinationUpdateTypeDef(BaseModel):
    HECEndpoint: Optional[str] = None
    HECEndpointType: Optional[HECEndpointTypeType] = None
    HECToken: Optional[str] = None
    HECAcknowledgmentTimeoutInSeconds: Optional[int] = None
    RetryOptions: Optional[SplunkRetryOptionsTypeDef] = None
    S3BackupMode: Optional[SplunkS3BackupModeType] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    BufferingHints: Optional[SplunkBufferingHintsTypeDef] = None
    SecretsManagerConfiguration: Optional[SecretsManagerConfigurationTypeDef] = None

class ExtendedS3DestinationDescriptionTypeDef(BaseModel):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHintsTypeDef
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationOutputTypeDef] = None
    S3BackupMode: Optional[S3BackupModeType] = None
    S3BackupDescription: Optional[S3DestinationDescriptionTypeDef] = None
    DataFormatConversionConfiguration: Optional[       DataFormatConversionConfigurationOutputTypeDef     ] = None
    DynamicPartitioningConfiguration: Optional[DynamicPartitioningConfigurationTypeDef] = None
    FileExtension: Optional[str] = None
    CustomTimeZone: Optional[str] = None

class ExtendedS3DestinationConfigurationTypeDef(BaseModel):
    RoleARN: str
    BucketARN: str
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHintsTypeDef] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    S3BackupMode: Optional[S3BackupModeType] = None
    S3BackupConfiguration: Optional[S3DestinationConfigurationTypeDef] = None
    DataFormatConversionConfiguration: Optional[DataFormatConversionConfigurationTypeDef] = None
    DynamicPartitioningConfiguration: Optional[DynamicPartitioningConfigurationTypeDef] = None
    FileExtension: Optional[str] = None
    CustomTimeZone: Optional[str] = None

class ExtendedS3DestinationUpdateTypeDef(BaseModel):
    RoleARN: Optional[str] = None
    BucketARN: Optional[str] = None
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHintsTypeDef] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    S3BackupMode: Optional[S3BackupModeType] = None
    S3BackupUpdate: Optional[S3DestinationUpdateTypeDef] = None
    DataFormatConversionConfiguration: Optional[DataFormatConversionConfigurationTypeDef] = None
    DynamicPartitioningConfiguration: Optional[DynamicPartitioningConfigurationTypeDef] = None
    FileExtension: Optional[str] = None
    CustomTimeZone: Optional[str] = None

class DestinationDescriptionTypeDef(BaseModel):
    DestinationId: str
    S3DestinationDescription: Optional[S3DestinationDescriptionTypeDef] = None
    ExtendedS3DestinationDescription: Optional[ExtendedS3DestinationDescriptionTypeDef] = None
    RedshiftDestinationDescription: Optional[RedshiftDestinationDescriptionTypeDef] = None
    ElasticsearchDestinationDescription: Optional[       ElasticsearchDestinationDescriptionTypeDef     ] = None
    AmazonopensearchserviceDestinationDescription: Optional[       AmazonopensearchserviceDestinationDescriptionTypeDef     ] = None
    SplunkDestinationDescription: Optional[SplunkDestinationDescriptionTypeDef] = None
    HttpEndpointDestinationDescription: Optional[       HttpEndpointDestinationDescriptionTypeDef     ] = None
    SnowflakeDestinationDescription: Optional[SnowflakeDestinationDescriptionTypeDef] = None
    AmazonOpenSearchServerlessDestinationDescription: Optional[       AmazonOpenSearchServerlessDestinationDescriptionTypeDef     ] = None

class CreateDeliveryStreamInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    DeliveryStreamType: Optional[DeliveryStreamTypeType] = None
    KinesisStreamSourceConfiguration: Optional[KinesisStreamSourceConfigurationTypeDef] = None
    DeliveryStreamEncryptionConfigurationInput: Optional[       DeliveryStreamEncryptionConfigurationInputTypeDef     ] = None
    S3DestinationConfiguration: Optional[S3DestinationConfigurationTypeDef] = None
    ExtendedS3DestinationConfiguration: Optional[       ExtendedS3DestinationConfigurationTypeDef     ] = None
    RedshiftDestinationConfiguration: Optional[RedshiftDestinationConfigurationTypeDef] = None
    ElasticsearchDestinationConfiguration: Optional[       ElasticsearchDestinationConfigurationTypeDef     ] = None
    AmazonopensearchserviceDestinationConfiguration: Optional[       AmazonopensearchserviceDestinationConfigurationTypeDef     ] = None
    SplunkDestinationConfiguration: Optional[SplunkDestinationConfigurationTypeDef] = None
    HttpEndpointDestinationConfiguration: Optional[       HttpEndpointDestinationConfigurationTypeDef     ] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AmazonOpenSearchServerlessDestinationConfiguration: Optional[       AmazonOpenSearchServerlessDestinationConfigurationTypeDef     ] = None
    MSKSourceConfiguration: Optional[MSKSourceConfigurationTypeDef] = None
    SnowflakeDestinationConfiguration: Optional[SnowflakeDestinationConfigurationTypeDef] = None

class UpdateDestinationInputRequestTypeDef(BaseModel):
    DeliveryStreamName: str
    CurrentDeliveryStreamVersionId: str
    DestinationId: str
    S3DestinationUpdate: Optional[S3DestinationUpdateTypeDef] = None
    ExtendedS3DestinationUpdate: Optional[ExtendedS3DestinationUpdateTypeDef] = None
    RedshiftDestinationUpdate: Optional[RedshiftDestinationUpdateTypeDef] = None
    ElasticsearchDestinationUpdate: Optional[ElasticsearchDestinationUpdateTypeDef] = None
    AmazonopensearchserviceDestinationUpdate: Optional[       AmazonopensearchserviceDestinationUpdateTypeDef     ] = None
    SplunkDestinationUpdate: Optional[SplunkDestinationUpdateTypeDef] = None
    HttpEndpointDestinationUpdate: Optional[HttpEndpointDestinationUpdateTypeDef] = None
    AmazonOpenSearchServerlessDestinationUpdate: Optional[       AmazonOpenSearchServerlessDestinationUpdateTypeDef     ] = None
    SnowflakeDestinationUpdate: Optional[SnowflakeDestinationUpdateTypeDef] = None

class DeliveryStreamDescriptionTypeDef(BaseModel):
    DeliveryStreamName: str
    DeliveryStreamARN: str
    DeliveryStreamStatus: DeliveryStreamStatusType
    DeliveryStreamType: DeliveryStreamTypeType
    VersionId: str
    Destinations: List[DestinationDescriptionTypeDef]
    HasMoreDestinations: bool
    FailureDescription: Optional[FailureDescriptionTypeDef] = None
    DeliveryStreamEncryptionConfiguration: Optional[       DeliveryStreamEncryptionConfigurationTypeDef     ] = None
    CreateTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    Source: Optional[SourceDescriptionTypeDef] = None

class DescribeDeliveryStreamOutputTypeDef(BaseModel):
    DeliveryStreamDescription: DeliveryStreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

