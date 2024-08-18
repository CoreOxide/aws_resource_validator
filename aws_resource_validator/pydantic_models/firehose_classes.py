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
from aws_resource_validator.pydantic_models.firehose_constants import *

class AmazonOpenSearchServerlessBufferingHintsTypeDef(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class AmazonOpenSearchServerlessRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class CloudWatchLoggingOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LogGroupName: Optional[str] = None
    LogStreamName: Optional[str] = None

class VpcConfigurationTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    RoleARN: str
    SecurityGroupIds: Sequence[str]

class VpcConfigurationDescriptionTypeDef(BaseValidatorModel):
    SubnetIds: List[str]
    RoleARN: str
    SecurityGroupIds: List[str]
    VpcId: str

class AmazonopensearchserviceBufferingHintsTypeDef(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class AmazonopensearchserviceRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class DocumentIdOptionsTypeDef(BaseValidatorModel):
    DefaultDocumentIdFormat: DefaultDocumentIdFormatType

class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    RoleARN: str
    Connectivity: ConnectivityType

class BufferingHintsTypeDef(BaseValidatorModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None

class CopyCommandTypeDef(BaseValidatorModel):
    DataTableName: str
    DataTableColumns: Optional[str] = None
    CopyOptions: Optional[str] = None

class DeliveryStreamEncryptionConfigurationInputTypeDef(BaseValidatorModel):
    KeyType: KeyTypeType
    KeyARN: Optional[str] = None

class KinesisStreamSourceConfigurationTypeDef(BaseValidatorModel):
    KinesisStreamARN: str
    RoleARN: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SchemaConfigurationTypeDef(BaseValidatorModel):
    RoleARN: Optional[str] = None
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Region: Optional[str] = None
    VersionId: Optional[str] = None

class DeleteDeliveryStreamInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    AllowForceDelete: Optional[bool] = None

class FailureDescriptionTypeDef(BaseValidatorModel):
    Type: DeliveryStreamFailureTypeType
    Details: str

class DescribeDeliveryStreamInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    Limit: Optional[int] = None
    ExclusiveStartDestinationId: Optional[str] = None

class HiveJsonSerDeOutputTypeDef(BaseValidatorModel):
    TimestampFormats: Optional[List[str]] = None

class OpenXJsonSerDeOutputTypeDef(BaseValidatorModel):
    ConvertDotsInJsonKeysToUnderscores: Optional[bool] = None
    CaseInsensitive: Optional[bool] = None
    ColumnToJsonKeyMappings: Optional[Dict[str, str]] = None

class HiveJsonSerDeTypeDef(BaseValidatorModel):
    TimestampFormats: Optional[Sequence[str]] = None

class OpenXJsonSerDeTypeDef(BaseValidatorModel):
    ConvertDotsInJsonKeysToUnderscores: Optional[bool] = None
    CaseInsensitive: Optional[bool] = None
    ColumnToJsonKeyMappings: Optional[Mapping[str, str]] = None

class RetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class ElasticsearchBufferingHintsTypeDef(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class ElasticsearchRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class KMSEncryptionConfigTypeDef(BaseValidatorModel):
    AWSKMSKeyARN: str

class HttpEndpointBufferingHintsTypeDef(BaseValidatorModel):
    SizeInMBs: Optional[int] = None
    IntervalInSeconds: Optional[int] = None

class HttpEndpointCommonAttributeTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str

class HttpEndpointConfigurationTypeDef(BaseValidatorModel):
    Url: str
    Name: Optional[str] = None
    AccessKey: Optional[str] = None

class HttpEndpointDescriptionTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    Name: Optional[str] = None

class HttpEndpointRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class SecretsManagerConfigurationTypeDef(BaseValidatorModel):
    Enabled: bool
    SecretARN: Optional[str] = None
    RoleARN: Optional[str] = None

class KinesisStreamSourceDescriptionTypeDef(BaseValidatorModel):
    KinesisStreamARN: Optional[str] = None
    RoleARN: Optional[str] = None
    DeliveryStartTimestamp: Optional[datetime] = None

class ListDeliveryStreamsInputRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    DeliveryStreamType: Optional[DeliveryStreamTypeType] = None
    ExclusiveStartDeliveryStreamName: Optional[str] = None

class ListTagsForDeliveryStreamInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None

class OrcSerDeOutputTypeDef(BaseValidatorModel):
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

class OrcSerDeTypeDef(BaseValidatorModel):
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

class ParquetSerDeTypeDef(BaseValidatorModel):
    BlockSizeBytes: Optional[int] = None
    PageSizeBytes: Optional[int] = None
    Compression: Optional[ParquetCompressionType] = None
    EnableDictionaryCompression: Optional[bool] = None
    MaxPaddingBytes: Optional[int] = None
    WriterVersion: Optional[ParquetWriterVersionType] = None

class ProcessorParameterTypeDef(BaseValidatorModel):
    ParameterName: ProcessorParameterNameType
    ParameterValue: str

class PutRecordBatchResponseEntryTypeDef(BaseValidatorModel):
    RecordId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class RedshiftRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class SnowflakeRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class SnowflakeRoleConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SnowflakeRole: Optional[str] = None

class SnowflakeVpcConfigurationTypeDef(BaseValidatorModel):
    PrivateLinkVpceId: str

class SplunkBufferingHintsTypeDef(BaseValidatorModel):
    IntervalInSeconds: Optional[int] = None
    SizeInMBs: Optional[int] = None

class SplunkRetryOptionsTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None

class StopDeliveryStreamEncryptionInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str

class UntagDeliveryStreamInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    TagKeys: Sequence[str]

class MSKSourceConfigurationTypeDef(BaseValidatorModel):
    MSKClusterARN: str
    TopicName: str
    AuthenticationConfiguration: AuthenticationConfigurationTypeDef

class MSKSourceDescriptionTypeDef(BaseValidatorModel):
    MSKClusterARN: Optional[str] = None
    TopicName: Optional[str] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None
    DeliveryStartTimestamp: Optional[datetime] = None

class RecordTypeDef(BaseValidatorModel):
    Data: BlobTypeDef

class StartDeliveryStreamEncryptionInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    DeliveryStreamEncryptionConfigurationInput: Optional[       DeliveryStreamEncryptionConfigurationInputTypeDef     ] = None

class TagDeliveryStreamInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    Tags: Sequence[TagTypeDef]

class CreateDeliveryStreamOutputTypeDef(BaseValidatorModel):
    DeliveryStreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeliveryStreamsOutputTypeDef(BaseValidatorModel):
    DeliveryStreamNames: List[str]
    HasMoreDeliveryStreams: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForDeliveryStreamOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordOutputTypeDef(BaseValidatorModel):
    RecordId: str
    Encrypted: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeliveryStreamEncryptionConfigurationTypeDef(BaseValidatorModel):
    KeyARN: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Status: Optional[DeliveryStreamEncryptionStatusType] = None
    FailureDescription: Optional[FailureDescriptionTypeDef] = None

class DeserializerOutputTypeDef(BaseValidatorModel):
    OpenXJsonSerDe: Optional[OpenXJsonSerDeOutputTypeDef] = None
    HiveJsonSerDe: Optional[HiveJsonSerDeOutputTypeDef] = None

class DeserializerTypeDef(BaseValidatorModel):
    OpenXJsonSerDe: Optional[OpenXJsonSerDeTypeDef] = None
    HiveJsonSerDe: Optional[HiveJsonSerDeTypeDef] = None

class DynamicPartitioningConfigurationTypeDef(BaseValidatorModel):
    RetryOptions: Optional[RetryOptionsTypeDef] = None
    Enabled: Optional[bool] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    NoEncryptionConfig: Optional[Literal["NoEncryption"]] = None
    KMSEncryptionConfig: Optional[KMSEncryptionConfigTypeDef] = None

class HttpEndpointRequestConfigurationOutputTypeDef(BaseValidatorModel):
    ContentEncoding: Optional[ContentEncodingType] = None
    CommonAttributes: Optional[List[HttpEndpointCommonAttributeTypeDef]] = None

class HttpEndpointRequestConfigurationTypeDef(BaseValidatorModel):
    ContentEncoding: Optional[ContentEncodingType] = None
    CommonAttributes: Optional[Sequence[HttpEndpointCommonAttributeTypeDef]] = None

class SerializerOutputTypeDef(BaseValidatorModel):
    ParquetSerDe: Optional[ParquetSerDeTypeDef] = None
    OrcSerDe: Optional[OrcSerDeOutputTypeDef] = None

class SerializerTypeDef(BaseValidatorModel):
    ParquetSerDe: Optional[ParquetSerDeTypeDef] = None
    OrcSerDe: Optional[OrcSerDeTypeDef] = None

class ProcessorOutputTypeDef(BaseValidatorModel):
    Type: ProcessorTypeType
    Parameters: Optional[List[ProcessorParameterTypeDef]] = None

class ProcessorTypeDef(BaseValidatorModel):
    Type: ProcessorTypeType
    Parameters: Optional[Sequence[ProcessorParameterTypeDef]] = None

class PutRecordBatchOutputTypeDef(BaseValidatorModel):
    FailedPutCount: int
    Encrypted: bool
    RequestResponses: List[PutRecordBatchResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SourceDescriptionTypeDef(BaseValidatorModel):
    KinesisStreamSourceDescription: Optional[KinesisStreamSourceDescriptionTypeDef] = None
    MSKSourceDescription: Optional[MSKSourceDescriptionTypeDef] = None

class PutRecordBatchInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    Records: Sequence[RecordTypeDef]

class PutRecordInputRequestTypeDef(BaseValidatorModel):
    DeliveryStreamName: str
    Record: RecordTypeDef

class InputFormatConfigurationOutputTypeDef(BaseValidatorModel):
    Deserializer: Optional[DeserializerOutputTypeDef] = None

class InputFormatConfigurationTypeDef(BaseValidatorModel):
    Deserializer: Optional[DeserializerTypeDef] = None

class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHintsTypeDef] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class S3DestinationDescriptionTypeDef(BaseValidatorModel):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHintsTypeDef
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class S3DestinationUpdateTypeDef(BaseValidatorModel):
    RoleARN: Optional[str] = None
    BucketARN: Optional[str] = None
    Prefix: Optional[str] = None
    ErrorOutputPrefix: Optional[str] = None
    BufferingHints: Optional[BufferingHintsTypeDef] = None
    CompressionFormat: Optional[CompressionFormatType] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class OutputFormatConfigurationOutputTypeDef(BaseValidatorModel):
    Serializer: Optional[SerializerOutputTypeDef] = None

class OutputFormatConfigurationTypeDef(BaseValidatorModel):
    Serializer: Optional[SerializerTypeDef] = None

class ProcessingConfigurationOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Processors: Optional[List[ProcessorOutputTypeDef]] = None

class ProcessingConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Processors: Optional[Sequence[ProcessorTypeDef]] = None

class DataFormatConversionConfigurationOutputTypeDef(BaseValidatorModel):
    SchemaConfiguration: Optional[SchemaConfigurationTypeDef] = None
    InputFormatConfiguration: Optional[InputFormatConfigurationOutputTypeDef] = None
    OutputFormatConfiguration: Optional[OutputFormatConfigurationOutputTypeDef] = None
    Enabled: Optional[bool] = None

class DataFormatConversionConfigurationTypeDef(BaseValidatorModel):
    SchemaConfiguration: Optional[SchemaConfigurationTypeDef] = None
    InputFormatConfiguration: Optional[InputFormatConfigurationTypeDef] = None
    OutputFormatConfiguration: Optional[OutputFormatConfigurationTypeDef] = None
    Enabled: Optional[bool] = None

class AmazonOpenSearchServerlessDestinationDescriptionTypeDef(BaseValidatorModel):
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

class AmazonopensearchserviceDestinationDescriptionTypeDef(BaseValidatorModel):
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

class ElasticsearchDestinationDescriptionTypeDef(BaseValidatorModel):
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

class HttpEndpointDestinationDescriptionTypeDef(BaseValidatorModel):
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

class RedshiftDestinationDescriptionTypeDef(BaseValidatorModel):
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

class SnowflakeDestinationDescriptionTypeDef(BaseValidatorModel):
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

class SplunkDestinationDescriptionTypeDef(BaseValidatorModel):
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

class AmazonOpenSearchServerlessDestinationConfigurationTypeDef(BaseValidatorModel):
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

class AmazonOpenSearchServerlessDestinationUpdateTypeDef(BaseValidatorModel):
    RoleARN: Optional[str] = None
    CollectionEndpoint: Optional[str] = None
    IndexName: Optional[str] = None
    BufferingHints: Optional[AmazonOpenSearchServerlessBufferingHintsTypeDef] = None
    RetryOptions: Optional[AmazonOpenSearchServerlessRetryOptionsTypeDef] = None
    S3Update: Optional[S3DestinationUpdateTypeDef] = None
    ProcessingConfiguration: Optional[ProcessingConfigurationTypeDef] = None
    CloudWatchLoggingOptions: Optional[CloudWatchLoggingOptionsTypeDef] = None

class AmazonopensearchserviceDestinationConfigurationTypeDef(BaseValidatorModel):
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

class AmazonopensearchserviceDestinationUpdateTypeDef(BaseValidatorModel):
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

class ElasticsearchDestinationConfigurationTypeDef(BaseValidatorModel):
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

class ElasticsearchDestinationUpdateTypeDef(BaseValidatorModel):
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

class HttpEndpointDestinationConfigurationTypeDef(BaseValidatorModel):
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

class HttpEndpointDestinationUpdateTypeDef(BaseValidatorModel):
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

class RedshiftDestinationConfigurationTypeDef(BaseValidatorModel):
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

class RedshiftDestinationUpdateTypeDef(BaseValidatorModel):
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

class SnowflakeDestinationConfigurationTypeDef(BaseValidatorModel):
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

class SnowflakeDestinationUpdateTypeDef(BaseValidatorModel):
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

class SplunkDestinationConfigurationTypeDef(BaseValidatorModel):
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

class SplunkDestinationUpdateTypeDef(BaseValidatorModel):
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

class ExtendedS3DestinationDescriptionTypeDef(BaseValidatorModel):
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

class ExtendedS3DestinationConfigurationTypeDef(BaseValidatorModel):
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

class ExtendedS3DestinationUpdateTypeDef(BaseValidatorModel):
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

class DestinationDescriptionTypeDef(BaseValidatorModel):
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

class CreateDeliveryStreamInputRequestTypeDef(BaseValidatorModel):
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

class UpdateDestinationInputRequestTypeDef(BaseValidatorModel):
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

class DeliveryStreamDescriptionTypeDef(BaseValidatorModel):
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

class DescribeDeliveryStreamOutputTypeDef(BaseValidatorModel):
    DeliveryStreamDescription: DeliveryStreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

