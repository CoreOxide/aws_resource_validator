from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.dms.dms_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountQuota(BaseValidatorModel):
    AccountQuotaName: Optional[str] = None
    Used: Optional[int] = None
    Max: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    ResourceArn: Optional[str] = None


class ApplyPendingMaintenanceActionMessage(BaseValidatorModel):
    ReplicationInstanceArn: str
    ApplyAction: str
    OptInType: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class BatchStartRecommendationsErrorEntry(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    Message: Optional[str] = None
    Code: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelReplicationTaskAssessmentRunMessage(BaseValidatorModel):
    ReplicationTaskAssessmentRunArn: str


class Certificate(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    CertificateCreationDate: Optional[datetime] = None
    CertificatePem: Optional[str] = None
    CertificateWallet: Optional[bytes] = None
    CertificateArn: Optional[str] = None
    CertificateOwner: Optional[str] = None
    ValidFromDate: Optional[datetime] = None
    ValidToDate: Optional[datetime] = None
    SigningAlgorithm: Optional[str] = None
    KeyLength: Optional[int] = None


class CollectorHealthCheck(BaseValidatorModel):
    CollectorStatus: Optional[CollectorStatusType] = None
    LocalCollectorS3Access: Optional[bool] = None
    WebCollectorS3Access: Optional[bool] = None
    WebCollectorGrantedRoleBasedAccess: Optional[bool] = None


class InventoryData(BaseValidatorModel):
    NumberOfDatabases: Optional[int] = None
    NumberOfSchemas: Optional[int] = None


class CollectorShortInfoResponse(BaseValidatorModel):
    CollectorReferencedId: Optional[str] = None
    CollectorName: Optional[str] = None


class ComputeConfigOutput(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    DnsNameServers: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MaxCapacityUnits: Optional[int] = None
    MinCapacityUnits: Optional[int] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSubnetGroupId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None


class ComputeConfig(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    DnsNameServers: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MaxCapacityUnits: Optional[int] = None
    MinCapacityUnits: Optional[int] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSubnetGroupId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None


class Connection(BaseValidatorModel):
    ReplicationInstanceArn: Optional[str] = None
    EndpointArn: Optional[str] = None
    Status: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    EndpointIdentifier: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None


class TargetDataSetting(BaseValidatorModel):
    TablePreparationMode: Optional[TablePreparationModeType] = None


class DmsTransferSettings(BaseValidatorModel):
    ServiceAccessRoleArn: Optional[str] = None
    BucketName: Optional[str] = None


class DocDbSettings(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    NestingLevel: Optional[NestingLevelValueType] = None
    ExtractDocId: Optional[bool] = None
    DocsToInvestigate: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    UseUpdateLookUp: Optional[bool] = None
    ReplicateShardCollections: Optional[bool] = None


class DynamoDbSettings(BaseValidatorModel):
    ServiceAccessRoleArn: str


class ElasticsearchSettings(BaseValidatorModel):
    ServiceAccessRoleArn: str
    EndpointUri: str
    FullLoadErrorPercentage: Optional[int] = None
    ErrorRetryDuration: Optional[int] = None
    UseNewMappingType: Optional[bool] = None


class GcpMySQLSettings(BaseValidatorModel):
    AfterConnectScript: Optional[str] = None
    CleanSourceMetadataOnMismatch: Optional[bool] = None
    DatabaseName: Optional[str] = None
    EventsPollInterval: Optional[int] = None
    TargetDbType: Optional[TargetDbTypeType] = None
    MaxFileSize: Optional[int] = None
    ParallelLoadThreads: Optional[int] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    ServerTimezone: Optional[str] = None
    Username: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None


class IBMDb2Settings(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    SetDataCaptureChanges: Optional[bool] = None
    CurrentLsn: Optional[str] = None
    MaxKBytesPerRead: Optional[int] = None
    Username: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    LoadTimeout: Optional[int] = None
    WriteBufferSize: Optional[int] = None
    MaxFileSize: Optional[int] = None
    KeepCsvFiles: Optional[bool] = None


class KafkaSettings(BaseValidatorModel):
    Broker: Optional[str] = None
    Topic: Optional[str] = None
    MessageFormat: Optional[MessageFormatValueType] = None
    IncludeTransactionDetails: Optional[bool] = None
    IncludePartitionValue: Optional[bool] = None
    PartitionIncludeSchemaTable: Optional[bool] = None
    IncludeTableAlterOperations: Optional[bool] = None
    IncludeControlDetails: Optional[bool] = None
    MessageMaxBytes: Optional[int] = None
    IncludeNullAndEmpty: Optional[bool] = None
    SecurityProtocol: Optional[KafkaSecurityProtocolType] = None
    SslClientCertificateArn: Optional[str] = None
    SslClientKeyArn: Optional[str] = None
    SslClientKeyPassword: Optional[str] = None
    SslCaCertificateArn: Optional[str] = None
    SaslUsername: Optional[str] = None
    SaslPassword: Optional[str] = None
    NoHexPrefix: Optional[bool] = None
    SaslMechanism: Optional[KafkaSaslMechanismType] = None
    SslEndpointIdentificationAlgorithm: Optional[KafkaSslEndpointIdentificationAlgorithmType] = None
    UseLargeIntegerValue: Optional[bool] = None


class KinesisSettings(BaseValidatorModel):
    StreamArn: Optional[str] = None
    MessageFormat: Optional[MessageFormatValueType] = None
    ServiceAccessRoleArn: Optional[str] = None
    IncludeTransactionDetails: Optional[bool] = None
    IncludePartitionValue: Optional[bool] = None
    PartitionIncludeSchemaTable: Optional[bool] = None
    IncludeTableAlterOperations: Optional[bool] = None
    IncludeControlDetails: Optional[bool] = None
    IncludeNullAndEmpty: Optional[bool] = None
    NoHexPrefix: Optional[bool] = None
    UseLargeIntegerValue: Optional[bool] = None


class MicrosoftSQLServerSettings(BaseValidatorModel):
    Port: Optional[int] = None
    BcpPacketSize: Optional[int] = None
    DatabaseName: Optional[str] = None
    ControlTablesFileGroup: Optional[str] = None
    Password: Optional[str] = None
    QuerySingleAlwaysOnNode: Optional[bool] = None
    ReadBackupOnly: Optional[bool] = None
    SafeguardPolicy: Optional[SafeguardPolicyType] = None
    ServerName: Optional[str] = None
    Username: Optional[str] = None
    UseBcpFullLoad: Optional[bool] = None
    UseThirdPartyBackupDevice: Optional[bool] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    TrimSpaceInChar: Optional[bool] = None
    TlogAccessMode: Optional[TlogAccessModeType] = None
    ForceLobLookup: Optional[bool] = None
    AuthenticationMethod: Optional[SqlServerAuthenticationMethodType] = None


class MongoDbSettings(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    AuthType: Optional[AuthTypeValueType] = None
    AuthMechanism: Optional[AuthMechanismValueType] = None
    NestingLevel: Optional[NestingLevelValueType] = None
    ExtractDocId: Optional[str] = None
    DocsToInvestigate: Optional[str] = None
    AuthSource: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    UseUpdateLookUp: Optional[bool] = None
    ReplicateShardCollections: Optional[bool] = None


class MySQLSettings(BaseValidatorModel):
    AfterConnectScript: Optional[str] = None
    CleanSourceMetadataOnMismatch: Optional[bool] = None
    DatabaseName: Optional[str] = None
    EventsPollInterval: Optional[int] = None
    TargetDbType: Optional[TargetDbTypeType] = None
    MaxFileSize: Optional[int] = None
    ParallelLoadThreads: Optional[int] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    ServerTimezone: Optional[str] = None
    Username: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    ExecuteTimeout: Optional[int] = None


class NeptuneSettings(BaseValidatorModel):
    S3BucketName: str
    S3BucketFolder: str
    ServiceAccessRoleArn: Optional[str] = None
    ErrorRetryDuration: Optional[int] = None
    MaxFileSize: Optional[int] = None
    MaxRetryCount: Optional[int] = None
    IamAuthEnabled: Optional[bool] = None


class PostgreSQLSettings(BaseValidatorModel):
    AfterConnectScript: Optional[str] = None
    CaptureDdls: Optional[bool] = None
    MaxFileSize: Optional[int] = None
    DatabaseName: Optional[str] = None
    DdlArtifactsSchema: Optional[str] = None
    ExecuteTimeout: Optional[int] = None
    FailTasksOnLobTruncation: Optional[bool] = None
    HeartbeatEnable: Optional[bool] = None
    HeartbeatSchema: Optional[str] = None
    HeartbeatFrequency: Optional[int] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    Username: Optional[str] = None
    SlotName: Optional[str] = None
    PluginName: Optional[PluginNameValueType] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    TrimSpaceInChar: Optional[bool] = None
    MapBooleanAsBoolean: Optional[bool] = None
    MapJsonbAsClob: Optional[bool] = None
    MapLongVarcharAs: Optional[LongVarcharMappingTypeType] = None
    DatabaseMode: Optional[DatabaseModeType] = None
    BabelfishDatabaseName: Optional[str] = None
    DisableUnicodeSourceFilter: Optional[bool] = None


class RedisSettings(BaseValidatorModel):
    ServerName: str
    Port: int
    SslSecurityProtocol: Optional[SslSecurityProtocolValueType] = None
    AuthType: Optional[RedisAuthTypeValueType] = None
    AuthUserName: Optional[str] = None
    AuthPassword: Optional[str] = None
    SslCaCertificateArn: Optional[str] = None


class RedshiftSettings(BaseValidatorModel):
    AcceptAnyDate: Optional[bool] = None
    AfterConnectScript: Optional[str] = None
    BucketFolder: Optional[str] = None
    BucketName: Optional[str] = None
    CaseSensitiveNames: Optional[bool] = None
    CompUpdate: Optional[bool] = None
    ConnectionTimeout: Optional[int] = None
    DatabaseName: Optional[str] = None
    DateFormat: Optional[str] = None
    EmptyAsNull: Optional[bool] = None
    EncryptionMode: Optional[EncryptionModeValueType] = None
    ExplicitIds: Optional[bool] = None
    FileTransferUploadStreams: Optional[int] = None
    LoadTimeout: Optional[int] = None
    MaxFileSize: Optional[int] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    RemoveQuotes: Optional[bool] = None
    ReplaceInvalidChars: Optional[str] = None
    ReplaceChars: Optional[str] = None
    ServerName: Optional[str] = None
    ServiceAccessRoleArn: Optional[str] = None
    ServerSideEncryptionKmsKeyId: Optional[str] = None
    TimeFormat: Optional[str] = None
    TrimBlanks: Optional[bool] = None
    TruncateColumns: Optional[bool] = None
    Username: Optional[str] = None
    WriteBufferSize: Optional[int] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    MapBooleanAsBoolean: Optional[bool] = None


class S3Settings(BaseValidatorModel):
    ServiceAccessRoleArn: Optional[str] = None
    ExternalTableDefinition: Optional[str] = None
    CsvRowDelimiter: Optional[str] = None
    CsvDelimiter: Optional[str] = None
    BucketFolder: Optional[str] = None
    BucketName: Optional[str] = None
    CompressionType: Optional[CompressionTypeValueType] = None
    EncryptionMode: Optional[EncryptionModeValueType] = None
    ServerSideEncryptionKmsKeyId: Optional[str] = None
    DataFormat: Optional[DataFormatValueType] = None
    EncodingType: Optional[EncodingTypeValueType] = None
    DictPageSizeLimit: Optional[int] = None
    RowGroupLength: Optional[int] = None
    DataPageSize: Optional[int] = None
    ParquetVersion: Optional[ParquetVersionValueType] = None
    EnableStatistics: Optional[bool] = None
    IncludeOpForFullLoad: Optional[bool] = None
    CdcInsertsOnly: Optional[bool] = None
    TimestampColumnName: Optional[str] = None
    ParquetTimestampInMillisecond: Optional[bool] = None
    CdcInsertsAndUpdates: Optional[bool] = None
    DatePartitionEnabled: Optional[bool] = None
    DatePartitionSequence: Optional[DatePartitionSequenceValueType] = None
    DatePartitionDelimiter: Optional[DatePartitionDelimiterValueType] = None
    UseCsvNoSupValue: Optional[bool] = None
    CsvNoSupValue: Optional[str] = None
    PreserveTransactions: Optional[bool] = None
    CdcPath: Optional[str] = None
    UseTaskStartTimeForFullLoadTimestamp: Optional[bool] = None
    CannedAclForObjects: Optional[CannedAclForObjectsValueType] = None
    AddColumnName: Optional[bool] = None
    CdcMaxBatchInterval: Optional[int] = None
    CdcMinFileSize: Optional[int] = None
    CsvNullValue: Optional[str] = None
    IgnoreHeaderRows: Optional[int] = None
    MaxFileSize: Optional[int] = None
    Rfc4180: Optional[bool] = None
    DatePartitionTimezone: Optional[str] = None
    AddTrailingPaddingCharacter: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    GlueCatalogGeneration: Optional[bool] = None


class SybaseSettings(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    Username: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None


class TimestreamSettings(BaseValidatorModel):
    DatabaseName: str
    MemoryDuration: int
    MagneticDuration: int
    CdcInsertsAndUpdates: Optional[bool] = None
    EnableMagneticStoreWrites: Optional[bool] = None


class EventSubscription(BaseValidatorModel):
    CustomerAwsId: Optional[str] = None
    CustSubscriptionId: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    EventCategoriesList: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class CreateFleetAdvisorCollectorRequest(BaseValidatorModel):
    CollectorName: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    Description: Optional[str] = None


class InstanceProfile(BaseValidatorModel):
    InstanceProfileArn: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    InstanceProfileCreationTime: Optional[datetime] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[List[str]] = None


class DataProviderDescriptorDefinition(BaseValidatorModel):
    DataProviderIdentifier: str
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None


class SCApplicationAttributes(BaseValidatorModel):
    S3BucketPath: Optional[str] = None
    S3BucketRoleArn: Optional[str] = None


class KerberosAuthenticationSettings(BaseValidatorModel):
    KeyCacheSecretId: Optional[str] = None
    KeyCacheSecretIamArn: Optional[str] = None
    Krb5FileContents: Optional[str] = None

Timestamp = Union[datetime, str]


class DataMigrationSettings(BaseValidatorModel):
    NumberOfJobs: Optional[int] = None
    CloudwatchLogsEnabled: Optional[bool] = None
    SelectionRules: Optional[str] = None


class DataMigrationStatistics(BaseValidatorModel):
    TablesLoaded: Optional[int] = None
    ElapsedTimeMillis: Optional[int] = None
    TablesLoading: Optional[int] = None
    FullLoadPercentage: Optional[int] = None
    CDCLatency: Optional[int] = None
    TablesQueued: Optional[int] = None
    TablesErrored: Optional[int] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None


class SourceDataSettingOutput(BaseValidatorModel):
    CDCStartPosition: Optional[str] = None
    CDCStartTime: Optional[datetime] = None
    CDCStopTime: Optional[datetime] = None
    SlotName: Optional[str] = None


class DataProviderDescriptor(BaseValidatorModel):
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    DataProviderName: Optional[str] = None
    DataProviderArn: Optional[str] = None


class DocDbDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class IbmDb2LuwDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class IbmDb2zOsDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class MariaDbDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class MicrosoftSqlServerDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class MongoDbDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None
    AuthType: Optional[AuthTypeValueType] = None
    AuthSource: Optional[str] = None
    AuthMechanism: Optional[AuthMechanismValueType] = None


class MySqlDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class OracleDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None
    AsmServer: Optional[str] = None
    SecretsManagerOracleAsmSecretId: Optional[str] = None
    SecretsManagerOracleAsmAccessRoleArn: Optional[str] = None
    SecretsManagerSecurityDbEncryptionSecretId: Optional[str] = None
    SecretsManagerSecurityDbEncryptionAccessRoleArn: Optional[str] = None


class PostgreSqlDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class RedshiftDataProviderSettings(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None


class DatabaseInstanceSoftwareDetailsResponse(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineEdition: Optional[str] = None
    ServicePack: Optional[str] = None
    SupportLevel: Optional[str] = None
    OsArchitecture: Optional[int] = None
    Tooltip: Optional[str] = None


class ServerShortInfoResponse(BaseValidatorModel):
    ServerId: Optional[str] = None
    IpAddress: Optional[str] = None
    ServerName: Optional[str] = None


class DatabaseShortInfoResponse(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseIpAddress: Optional[str] = None
    DatabaseEngine: Optional[str] = None


class DefaultErrorDetails(BaseValidatorModel):
    Message: Optional[str] = None


class DeleteCertificateMessage(BaseValidatorModel):
    CertificateArn: str


class DeleteCollectorRequest(BaseValidatorModel):
    CollectorReferencedId: str


class DeleteConnectionMessage(BaseValidatorModel):
    EndpointArn: str
    ReplicationInstanceArn: str


class DeleteDataMigrationMessage(BaseValidatorModel):
    DataMigrationIdentifier: str


class DeleteDataProviderMessage(BaseValidatorModel):
    DataProviderIdentifier: str


class DeleteEndpointMessage(BaseValidatorModel):
    EndpointArn: str


class DeleteEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str


class DeleteFleetAdvisorDatabasesRequest(BaseValidatorModel):
    DatabaseIds: List[str]


class DeleteInstanceProfileMessage(BaseValidatorModel):
    InstanceProfileIdentifier: str


class DeleteMigrationProjectMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str


class DeleteReplicationConfigMessage(BaseValidatorModel):
    ReplicationConfigArn: str


class DeleteReplicationInstanceMessage(BaseValidatorModel):
    ReplicationInstanceArn: str


class DeleteReplicationSubnetGroupMessage(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: str


class DeleteReplicationTaskAssessmentRunMessage(BaseValidatorModel):
    ReplicationTaskAssessmentRunArn: str


class DeleteReplicationTaskMessage(BaseValidatorModel):
    ReplicationTaskArn: str


class DescribeApplicableIndividualAssessmentsMessage(BaseValidatorModel):
    ReplicationTaskArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEngineName: Optional[str] = None
    TargetEngineName: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Values: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeConversionConfigurationMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str


class DescribeEndpointSettingsMessage(BaseValidatorModel):
    EngineName: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class EndpointSetting(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[EndpointSettingTypeValueType] = None
    EnumValues: Optional[List[str]] = None
    Sensitive: Optional[bool] = None
    Units: Optional[str] = None
    Applicability: Optional[str] = None
    IntValueMin: Optional[int] = None
    IntValueMax: Optional[int] = None
    DefaultValue: Optional[str] = None


class SupportedEndpointType(BaseValidatorModel):
    EngineName: Optional[str] = None
    SupportsCDC: Optional[bool] = None
    EndpointType: Optional[ReplicationEndpointTypeValueType] = None
    ReplicationInstanceEngineMinimumVersion: Optional[str] = None
    EngineDisplayName: Optional[str] = None


class DescribeEngineVersionsMessage(BaseValidatorModel):
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class EngineVersion(BaseValidatorModel):
    Version: Optional[str] = None
    Lifecycle: Optional[str] = None
    ReleaseStatus: Optional[ReleaseStatusValuesType] = None
    LaunchDate: Optional[datetime] = None
    AutoUpgradeDate: Optional[datetime] = None
    DeprecationDate: Optional[datetime] = None
    ForceUpgradeDate: Optional[datetime] = None
    AvailableUpgrades: Optional[List[str]] = None


class EventCategoryGroup(BaseValidatorModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal['replication-instance']] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None


class DescribeFleetAdvisorLsaAnalysisRequest(BaseValidatorModel):
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class FleetAdvisorLsaAnalysisResponse(BaseValidatorModel):
    LsaAnalysisId: Optional[str] = None
    Status: Optional[str] = None


class FleetAdvisorSchemaObjectResponse(BaseValidatorModel):
    SchemaId: Optional[str] = None
    ObjectType: Optional[str] = None
    NumberOfObjects: Optional[int] = None
    CodeLineCount: Optional[int] = None
    CodeSize: Optional[int] = None


class DescribeOrderableReplicationInstancesMessage(BaseValidatorModel):
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class OrderableReplicationInstance(BaseValidatorModel):
    EngineVersion: Optional[str] = None
    ReplicationInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    MinAllocatedStorage: Optional[int] = None
    MaxAllocatedStorage: Optional[int] = None
    DefaultAllocatedStorage: Optional[int] = None
    IncludedAllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    ReleaseStatus: Optional[ReleaseStatusValuesType] = None


class Limitation(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    EngineName: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Impact: Optional[str] = None
    Type: Optional[str] = None


class DescribeRefreshSchemasStatusMessage(BaseValidatorModel):
    EndpointArn: str


class RefreshSchemasStatus(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    Status: Optional[RefreshSchemasStatusTypeValueType] = None
    LastRefreshDate: Optional[datetime] = None
    LastFailureMessage: Optional[str] = None


class DescribeReplicationInstanceTaskLogsMessage(BaseValidatorModel):
    ReplicationInstanceArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class ReplicationInstanceTaskLog(BaseValidatorModel):
    ReplicationTaskName: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationInstanceTaskLogSize: Optional[int] = None


class TableStatistics(BaseValidatorModel):
    SchemaName: Optional[str] = None
    TableName: Optional[str] = None
    Inserts: Optional[int] = None
    Deletes: Optional[int] = None
    Updates: Optional[int] = None
    Ddls: Optional[int] = None
    AppliedInserts: Optional[int] = None
    AppliedDeletes: Optional[int] = None
    AppliedUpdates: Optional[int] = None
    AppliedDdls: Optional[int] = None
    FullLoadRows: Optional[int] = None
    FullLoadCondtnlChkFailedRows: Optional[int] = None
    FullLoadErrorRows: Optional[int] = None
    FullLoadStartTime: Optional[datetime] = None
    FullLoadEndTime: Optional[datetime] = None
    FullLoadReloaded: Optional[bool] = None
    LastUpdateTime: Optional[datetime] = None
    TableState: Optional[str] = None
    ValidationPendingRecords: Optional[int] = None
    ValidationFailedRecords: Optional[int] = None
    ValidationSuspendedRecords: Optional[int] = None
    ValidationState: Optional[str] = None
    ValidationStateDetails: Optional[str] = None


class DescribeReplicationTaskAssessmentResultsMessage(BaseValidatorModel):
    ReplicationTaskArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class ReplicationTaskAssessmentResult(BaseValidatorModel):
    ReplicationTaskIdentifier: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationTaskLastAssessmentDate: Optional[datetime] = None
    AssessmentStatus: Optional[str] = None
    AssessmentResultsFile: Optional[str] = None
    AssessmentResults: Optional[str] = None
    S3ObjectUrl: Optional[str] = None


class ReplicationTaskIndividualAssessment(BaseValidatorModel):
    ReplicationTaskIndividualAssessmentArn: Optional[str] = None
    ReplicationTaskAssessmentRunArn: Optional[str] = None
    IndividualAssessmentName: Optional[str] = None
    Status: Optional[str] = None
    ReplicationTaskIndividualAssessmentStartDate: Optional[datetime] = None


class DescribeSchemasMessage(BaseValidatorModel):
    EndpointArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class OracleSettingsOutput(BaseValidatorModel):
    AddSupplementalLogging: Optional[bool] = None
    ArchivedLogDestId: Optional[int] = None
    AdditionalArchivedLogDestId: Optional[int] = None
    ExtraArchivedLogDestIds: Optional[List[int]] = None
    AllowSelectNestedTables: Optional[bool] = None
    ParallelAsmReadThreads: Optional[int] = None
    ReadAheadBlocks: Optional[int] = None
    AccessAlternateDirectly: Optional[bool] = None
    UseAlternateFolderForOnline: Optional[bool] = None
    OraclePathPrefix: Optional[str] = None
    UsePathPrefix: Optional[str] = None
    ReplacePathPrefix: Optional[bool] = None
    EnableHomogenousTablespace: Optional[bool] = None
    DirectPathNoLog: Optional[bool] = None
    ArchivedLogsOnly: Optional[bool] = None
    AsmPassword: Optional[str] = None
    AsmServer: Optional[str] = None
    AsmUser: Optional[str] = None
    CharLengthSemantics: Optional[CharLengthSemanticsType] = None
    DatabaseName: Optional[str] = None
    DirectPathParallelLoad: Optional[bool] = None
    FailTasksOnLobTruncation: Optional[bool] = None
    NumberDatatypeScale: Optional[int] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ReadTableSpaceName: Optional[bool] = None
    RetryInterval: Optional[int] = None
    SecurityDbEncryption: Optional[str] = None
    SecurityDbEncryptionName: Optional[str] = None
    ServerName: Optional[str] = None
    SpatialDataOptionToGeoJsonFunctionName: Optional[str] = None
    StandbyDelayTime: Optional[int] = None
    Username: Optional[str] = None
    UseBFile: Optional[bool] = None
    UseDirectPathFullLoad: Optional[bool] = None
    UseLogminerReader: Optional[bool] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerOracleAsmAccessRoleArn: Optional[str] = None
    SecretsManagerOracleAsmSecretId: Optional[str] = None
    TrimSpaceInChar: Optional[bool] = None
    ConvertTimestampWithZoneToUTC: Optional[bool] = None
    OpenTransactionWindow: Optional[int] = None
    AuthenticationMethod: Optional[OracleAuthenticationMethodType] = None


class ExportMetadataModelAssessmentMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    FileName: Optional[str] = None
    AssessmentReportTypes: Optional[List[AssessmentReportTypeType]] = None


class ExportMetadataModelAssessmentResultEntry(BaseValidatorModel):
    S3ObjectKey: Optional[str] = None
    ObjectURL: Optional[str] = None


class ExportSqlDetails(BaseValidatorModel):
    S3ObjectKey: Optional[str] = None
    ObjectURL: Optional[str] = None


class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceArnList: Optional[List[str]] = None


class ModifyConversionConfigurationMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str


class ModifyEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class ModifyInstanceProfileMessage(BaseValidatorModel):
    InstanceProfileIdentifier: str
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[List[str]] = None


class ModifyReplicationSubnetGroupMessage(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: str
    SubnetIds: List[str]
    ReplicationSubnetGroupDescription: Optional[str] = None


class MoveReplicationTaskMessage(BaseValidatorModel):
    ReplicationTaskArn: str
    TargetReplicationInstanceArn: str


class OracleSettings(BaseValidatorModel):
    AddSupplementalLogging: Optional[bool] = None
    ArchivedLogDestId: Optional[int] = None
    AdditionalArchivedLogDestId: Optional[int] = None
    ExtraArchivedLogDestIds: Optional[List[int]] = None
    AllowSelectNestedTables: Optional[bool] = None
    ParallelAsmReadThreads: Optional[int] = None
    ReadAheadBlocks: Optional[int] = None
    AccessAlternateDirectly: Optional[bool] = None
    UseAlternateFolderForOnline: Optional[bool] = None
    OraclePathPrefix: Optional[str] = None
    UsePathPrefix: Optional[str] = None
    ReplacePathPrefix: Optional[bool] = None
    EnableHomogenousTablespace: Optional[bool] = None
    DirectPathNoLog: Optional[bool] = None
    ArchivedLogsOnly: Optional[bool] = None
    AsmPassword: Optional[str] = None
    AsmServer: Optional[str] = None
    AsmUser: Optional[str] = None
    CharLengthSemantics: Optional[CharLengthSemanticsType] = None
    DatabaseName: Optional[str] = None
    DirectPathParallelLoad: Optional[bool] = None
    FailTasksOnLobTruncation: Optional[bool] = None
    NumberDatatypeScale: Optional[int] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ReadTableSpaceName: Optional[bool] = None
    RetryInterval: Optional[int] = None
    SecurityDbEncryption: Optional[str] = None
    SecurityDbEncryptionName: Optional[str] = None
    ServerName: Optional[str] = None
    SpatialDataOptionToGeoJsonFunctionName: Optional[str] = None
    StandbyDelayTime: Optional[int] = None
    Username: Optional[str] = None
    UseBFile: Optional[bool] = None
    UseDirectPathFullLoad: Optional[bool] = None
    UseLogminerReader: Optional[bool] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerOracleAsmAccessRoleArn: Optional[str] = None
    SecretsManagerOracleAsmSecretId: Optional[str] = None
    TrimSpaceInChar: Optional[bool] = None
    ConvertTimestampWithZoneToUTC: Optional[bool] = None
    OpenTransactionWindow: Optional[int] = None
    AuthenticationMethod: Optional[OracleAuthenticationMethodType] = None


class PendingMaintenanceAction(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None


class ReplicationTaskAssessmentRunProgress(BaseValidatorModel):
    IndividualAssessmentCount: Optional[int] = None
    IndividualAssessmentCompletedCount: Optional[int] = None


class ReplicationTaskAssessmentRunResultStatistic(BaseValidatorModel):
    Passed: Optional[int] = None
    Failed: Optional[int] = None
    Error: Optional[int] = None
    Warning: Optional[int] = None
    Cancelled: Optional[int] = None
    Skipped: Optional[int] = None


class ProvisionData(BaseValidatorModel):
    ProvisionState: Optional[str] = None
    ProvisionedCapacityUnits: Optional[int] = None
    DateProvisioned: Optional[datetime] = None
    IsNewProvisioningAvailable: Optional[bool] = None
    DateNewProvisioningDataAvailable: Optional[datetime] = None
    ReasonForNewProvisioningData: Optional[str] = None


class RdsConfiguration(BaseValidatorModel):
    EngineEdition: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceVcpu: Optional[float] = None
    InstanceMemory: Optional[float] = None
    StorageType: Optional[str] = None
    StorageSize: Optional[int] = None
    StorageIops: Optional[int] = None
    DeploymentOption: Optional[str] = None
    EngineVersion: Optional[str] = None


class RdsRequirements(BaseValidatorModel):
    EngineEdition: Optional[str] = None
    InstanceVcpu: Optional[float] = None
    InstanceMemory: Optional[float] = None
    StorageSize: Optional[int] = None
    StorageIops: Optional[int] = None
    DeploymentOption: Optional[str] = None
    EngineVersion: Optional[str] = None


class RebootReplicationInstanceMessage(BaseValidatorModel):
    ReplicationInstanceArn: str
    ForceFailover: Optional[bool] = None
    ForcePlannedFailover: Optional[bool] = None


class RecommendationSettings(BaseValidatorModel):
    InstanceSizingType: str
    WorkloadType: str


class RefreshSchemasMessage(BaseValidatorModel):
    EndpointArn: str
    ReplicationInstanceArn: str


class TableToReload(BaseValidatorModel):
    SchemaName: str
    TableName: str


class RemoveTagsFromResourceMessage(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class ReplicationPendingModifiedValues(BaseValidatorModel):
    ReplicationInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    NetworkType: Optional[str] = None


class VpcSecurityGroupMembership(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class ReplicationStats(BaseValidatorModel):
    FullLoadProgressPercent: Optional[int] = None
    ElapsedTimeMillis: Optional[int] = None
    TablesLoaded: Optional[int] = None
    TablesLoading: Optional[int] = None
    TablesQueued: Optional[int] = None
    TablesErrored: Optional[int] = None
    FreshStartDate: Optional[datetime] = None
    StartDate: Optional[datetime] = None
    StopDate: Optional[datetime] = None
    FullLoadStartDate: Optional[datetime] = None
    FullLoadFinishDate: Optional[datetime] = None


class ReplicationTaskStats(BaseValidatorModel):
    FullLoadProgressPercent: Optional[int] = None
    ElapsedTimeMillis: Optional[int] = None
    TablesLoaded: Optional[int] = None
    TablesLoading: Optional[int] = None
    TablesQueued: Optional[int] = None
    TablesErrored: Optional[int] = None
    FreshStartDate: Optional[datetime] = None
    StartDate: Optional[datetime] = None
    StopDate: Optional[datetime] = None
    FullLoadStartDate: Optional[datetime] = None
    FullLoadFinishDate: Optional[datetime] = None


class SchemaShortInfoResponse(BaseValidatorModel):
    SchemaId: Optional[str] = None
    SchemaName: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseIpAddress: Optional[str] = None


class StartDataMigrationMessage(BaseValidatorModel):
    DataMigrationIdentifier: str
    StartType: StartReplicationMigrationTypeValueType


class StartExtensionPackAssociationMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str


class StartMetadataModelAssessmentMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str


class StartMetadataModelConversionMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str


class StartMetadataModelExportAsScriptMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    FileName: Optional[str] = None


class StartMetadataModelExportToTargetMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    OverwriteExtensionPack: Optional[bool] = None


class StartMetadataModelImportMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    Refresh: Optional[bool] = None


class StartReplicationTaskAssessmentMessage(BaseValidatorModel):
    ReplicationTaskArn: str


class StopDataMigrationMessage(BaseValidatorModel):
    DataMigrationIdentifier: str


class StopReplicationMessage(BaseValidatorModel):
    ReplicationConfigArn: str


class StopReplicationTaskMessage(BaseValidatorModel):
    ReplicationTaskArn: str


class TestConnectionMessage(BaseValidatorModel):
    ReplicationInstanceArn: str
    EndpointArn: str


class UpdateSubscriptionsToEventBridgeMessage(BaseValidatorModel):
    ForceMove: Optional[bool] = None


class AddTagsToResourceMessage(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    SourceIds: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class CreateInstanceProfileMessage(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[List[str]] = None


class CreateReplicationSubnetGroupMessage(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: str
    ReplicationSubnetGroupDescription: str
    SubnetIds: List[str]
    Tags: Optional[List[Tag]] = None


class StartReplicationTaskAssessmentRunMessage(BaseValidatorModel):
    ReplicationTaskArn: str
    ServiceAccessRoleArn: str
    ResultLocationBucket: str
    AssessmentRunName: str
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    IncludeOnly: Optional[List[str]] = None
    Exclude: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class CreateFleetAdvisorCollectorResponse(BaseValidatorModel):
    CollectorReferencedId: str
    CollectorName: str
    Description: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    ResponseMetadata: ResponseMetadata


class DeleteFleetAdvisorDatabasesResponse(BaseValidatorModel):
    DatabaseIds: List[str]
    ResponseMetadata: ResponseMetadata


class DescribeAccountAttributesResponse(BaseValidatorModel):
    AccountQuotas: List[AccountQuota]
    UniqueAccountIdentifier: str
    ResponseMetadata: ResponseMetadata


class DescribeApplicableIndividualAssessmentsResponse(BaseValidatorModel):
    IndividualAssessmentNames: List[str]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeConversionConfigurationResponse(BaseValidatorModel):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str
    ResponseMetadata: ResponseMetadata


class DescribeSchemasResponse(BaseValidatorModel):
    Marker: str
    Schemas: List[str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class ModifyConversionConfigurationResponse(BaseValidatorModel):
    MigrationProjectIdentifier: str
    ResponseMetadata: ResponseMetadata


class ReloadReplicationTablesResponse(BaseValidatorModel):
    ReplicationConfigArn: str
    ResponseMetadata: ResponseMetadata


class ReloadTablesResponse(BaseValidatorModel):
    ReplicationTaskArn: str
    ResponseMetadata: ResponseMetadata


class RunFleetAdvisorLsaAnalysisResponse(BaseValidatorModel):
    LsaAnalysisId: str
    Status: str
    ResponseMetadata: ResponseMetadata


class StartExtensionPackAssociationResponse(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadata


class StartMetadataModelAssessmentResponse(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadata


class StartMetadataModelConversionResponse(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadata


class StartMetadataModelExportAsScriptResponse(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadata


class StartMetadataModelExportToTargetResponse(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadata


class StartMetadataModelImportResponse(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadata


class UpdateSubscriptionsToEventBridgeResponse(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadata


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetStatus: Optional[str] = None


class BatchStartRecommendationsResponse(BaseValidatorModel):
    ErrorEntries: List[BatchStartRecommendationsErrorEntry]
    ResponseMetadata: ResponseMetadata


class ImportCertificateMessage(BaseValidatorModel):
    CertificateIdentifier: str
    CertificatePem: Optional[str] = None
    CertificateWallet: Optional[Blob] = None
    Tags: Optional[List[Tag]] = None


class DeleteCertificateResponse(BaseValidatorModel):
    Certificate: Certificate
    ResponseMetadata: ResponseMetadata


class DescribeCertificatesResponse(BaseValidatorModel):
    Marker: str
    Certificates: List[Certificate]
    ResponseMetadata: ResponseMetadata


class ImportCertificateResponse(BaseValidatorModel):
    Certificate: Certificate
    ResponseMetadata: ResponseMetadata


class CollectorResponse(BaseValidatorModel):
    CollectorReferencedId: Optional[str] = None
    CollectorName: Optional[str] = None
    CollectorVersion: Optional[str] = None
    VersionStatus: Optional[VersionStatusType] = None
    Description: Optional[str] = None
    S3BucketName: Optional[str] = None
    ServiceAccessRoleArn: Optional[str] = None
    CollectorHealthCheck: Optional[CollectorHealthCheck] = None
    LastDataReceived: Optional[str] = None
    RegisteredDate: Optional[str] = None
    CreatedDate: Optional[str] = None
    ModifiedDate: Optional[str] = None
    InventoryData: Optional[InventoryData] = None


class ReplicationConfig(BaseValidatorModel):
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    ComputeConfig: Optional[ComputeConfigOutput] = None
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    TableMappings: Optional[str] = None
    ReplicationConfigCreateTime: Optional[datetime] = None
    ReplicationConfigUpdateTime: Optional[datetime] = None

ComputeConfigUnion = Union[ComputeConfig, ComputeConfigOutput]


class DeleteConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


class DescribeConnectionsResponse(BaseValidatorModel):
    Marker: str
    Connections: List[Connection]
    ResponseMetadata: ResponseMetadata


class TestConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


class CreateEventSubscriptionResponse(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class DeleteEventSubscriptionResponse(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class DescribeEventSubscriptionsResponse(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscription]
    ResponseMetadata: ResponseMetadata


class ModifyEventSubscriptionResponse(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class CreateInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class DeleteInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class DescribeInstanceProfilesResponse(BaseValidatorModel):
    Marker: str
    InstanceProfiles: List[InstanceProfile]
    ResponseMetadata: ResponseMetadata


class ModifyInstanceProfileResponse(BaseValidatorModel):
    InstanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class CreateMigrationProjectMessage(BaseValidatorModel):
    SourceDataProviderDescriptors: List[DataProviderDescriptorDefinition]
    TargetDataProviderDescriptors: List[DataProviderDescriptorDefinition]
    InstanceProfileIdentifier: str
    MigrationProjectName: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributes] = None


class ModifyMigrationProjectMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    MigrationProjectName: Optional[str] = None
    SourceDataProviderDescriptors: Optional[List[DataProviderDescriptorDefinition]] = None
    TargetDataProviderDescriptors: Optional[List[DataProviderDescriptorDefinition]] = None
    InstanceProfileIdentifier: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributes] = None


class CreateReplicationInstanceMessage(BaseValidatorModel):
    ReplicationInstanceIdentifier: str
    ReplicationInstanceClass: str
    AllocatedStorage: Optional[int] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None
    ReplicationSubnetGroupIdentifier: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    DnsNameServers: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    NetworkType: Optional[str] = None
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettings] = None


class ModifyReplicationInstanceMessage(BaseValidatorModel):
    ReplicationInstanceArn: str
    AllocatedStorage: Optional[int] = None
    ApplyImmediately: Optional[bool] = None
    ReplicationInstanceClass: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReplicationInstanceIdentifier: Optional[str] = None
    NetworkType: Optional[str] = None
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettings] = None


class CreateReplicationTaskMessage(BaseValidatorModel):
    ReplicationTaskIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ReplicationInstanceArn: str
    MigrationType: MigrationTypeValueType
    TableMappings: str
    ReplicationTaskSettings: Optional[str] = None
    CdcStartTime: Optional[Timestamp] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    TaskData: Optional[str] = None
    ResourceIdentifier: Optional[str] = None


class ModifyReplicationTaskMessage(BaseValidatorModel):
    ReplicationTaskArn: str
    ReplicationTaskIdentifier: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationTaskSettings: Optional[str] = None
    CdcStartTime: Optional[Timestamp] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    TaskData: Optional[str] = None


class SourceDataSetting(BaseValidatorModel):
    CDCStartPosition: Optional[str] = None
    CDCStartTime: Optional[Timestamp] = None
    CDCStopTime: Optional[Timestamp] = None
    SlotName: Optional[str] = None


class StartReplicationMessage(BaseValidatorModel):
    ReplicationConfigArn: str
    StartReplicationType: str
    PremigrationAssessmentSettings: Optional[str] = None
    CdcStartTime: Optional[Timestamp] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None


class StartReplicationTaskMessage(BaseValidatorModel):
    ReplicationTaskArn: str
    StartReplicationTaskType: StartReplicationTaskTypeValueType
    CdcStartTime: Optional[Timestamp] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None


class DataMigration(BaseValidatorModel):
    DataMigrationName: Optional[str] = None
    DataMigrationArn: Optional[str] = None
    DataMigrationCreateTime: Optional[datetime] = None
    DataMigrationStartTime: Optional[datetime] = None
    DataMigrationEndTime: Optional[datetime] = None
    ServiceAccessRoleArn: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    DataMigrationType: Optional[MigrationTypeValueType] = None
    DataMigrationSettings: Optional[DataMigrationSettings] = None
    SourceDataSettings: Optional[List[SourceDataSettingOutput]] = None
    TargetDataSettings: Optional[List[TargetDataSetting]] = None
    DataMigrationStatistics: Optional[DataMigrationStatistics] = None
    DataMigrationStatus: Optional[str] = None
    PublicIpAddresses: Optional[List[str]] = None
    DataMigrationCidrBlocks: Optional[List[str]] = None
    LastFailureMessage: Optional[str] = None
    StopReason: Optional[str] = None


class MigrationProject(BaseValidatorModel):
    MigrationProjectName: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    MigrationProjectCreationTime: Optional[datetime] = None
    SourceDataProviderDescriptors: Optional[List[DataProviderDescriptor]] = None
    TargetDataProviderDescriptors: Optional[List[DataProviderDescriptor]] = None
    InstanceProfileArn: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributes] = None


class DataProviderSettings(BaseValidatorModel):
    RedshiftSettings: Optional[RedshiftDataProviderSettings] = None
    PostgreSqlSettings: Optional[PostgreSqlDataProviderSettings] = None
    MySqlSettings: Optional[MySqlDataProviderSettings] = None
    OracleSettings: Optional[OracleDataProviderSettings] = None
    MicrosoftSqlServerSettings: Optional[MicrosoftSqlServerDataProviderSettings] = None
    DocDbSettings: Optional[DocDbDataProviderSettings] = None
    MariaDbSettings: Optional[MariaDbDataProviderSettings] = None
    IbmDb2LuwSettings: Optional[IbmDb2LuwDataProviderSettings] = None
    IbmDb2zOsSettings: Optional[IbmDb2zOsDataProviderSettings] = None
    MongoDbSettings: Optional[MongoDbDataProviderSettings] = None


class DatabaseResponse(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    IpAddress: Optional[str] = None
    NumberOfSchemas: Optional[int] = None
    Server: Optional[ServerShortInfoResponse] = None
    SoftwareDetails: Optional[DatabaseInstanceSoftwareDetailsResponse] = None
    Collectors: Optional[List[CollectorShortInfoResponse]] = None


class ErrorDetails(BaseValidatorModel):
    defaultErrorDetails: Optional[DefaultErrorDetails] = None


class DescribeCertificatesMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeConnectionsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDataMigrationsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WithoutStatistics: Optional[bool] = None


class DescribeDataProvidersMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEndpointTypesMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEndpointsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventCategoriesMessage(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class DescribeEventSubscriptionsMessage(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal['replication-instance']] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeExtensionPackAssociationsMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeFleetAdvisorCollectorsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetAdvisorDatabasesRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetAdvisorSchemaObjectSummaryRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetAdvisorSchemasRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceProfilesMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeMetadataModelAssessmentsMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelConversionsMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelExportsAsScriptMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelExportsToTargetMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelImportsMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMigrationProjectsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribePendingMaintenanceActionsMessage(BaseValidatorModel):
    ReplicationInstanceArn: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeRecommendationLimitationsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeRecommendationsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReplicationConfigsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationInstancesMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationSubnetGroupsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationTableStatisticsMessage(BaseValidatorModel):
    ReplicationConfigArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class DescribeReplicationTaskAssessmentRunsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationTaskIndividualAssessmentsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationTasksMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None


class DescribeReplicationsMessage(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeTableStatisticsMessage(BaseValidatorModel):
    ReplicationTaskArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class DescribeCertificatesMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConnectionsMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataMigrationsMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    WithoutSettings: Optional[bool] = None
    WithoutStatistics: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointTypesMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointsMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventSubscriptionsMessagePaginate(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal['replication-instance']] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrderableReplicationInstancesMessagePaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationInstancesMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationSubnetGroupsMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationTaskAssessmentResultsMessagePaginate(BaseValidatorModel):
    ReplicationTaskArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationTasksMessagePaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    WithoutSettings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSchemasMessagePaginate(BaseValidatorModel):
    EndpointArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTableStatisticsMessagePaginate(BaseValidatorModel):
    ReplicationTaskArn: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConnectionsMessageWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEndpointsMessageWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationInstancesMessageWaitExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationInstancesMessageWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationTasksMessageWaitExtraExtraExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationTasksMessageWaitExtraExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationTasksMessageWaitExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationTasksMessageWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEndpointSettingsResponse(BaseValidatorModel):
    Marker: str
    EndpointSettings: List[EndpointSetting]
    ResponseMetadata: ResponseMetadata


class DescribeEndpointTypesResponse(BaseValidatorModel):
    Marker: str
    SupportedEndpointTypes: List[SupportedEndpointType]
    ResponseMetadata: ResponseMetadata


class DescribeEngineVersionsResponse(BaseValidatorModel):
    EngineVersions: List[EngineVersion]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeEventCategoriesResponse(BaseValidatorModel):
    EventCategoryGroupList: List[EventCategoryGroup]
    ResponseMetadata: ResponseMetadata


class DescribeEventsResponse(BaseValidatorModel):
    Marker: str
    Events: List[Event]
    ResponseMetadata: ResponseMetadata


class DescribeFleetAdvisorLsaAnalysisResponse(BaseValidatorModel):
    Analysis: List[FleetAdvisorLsaAnalysisResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeFleetAdvisorSchemaObjectSummaryResponse(BaseValidatorModel):
    FleetAdvisorSchemaObjects: List[FleetAdvisorSchemaObjectResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOrderableReplicationInstancesResponse(BaseValidatorModel):
    OrderableReplicationInstances: List[OrderableReplicationInstance]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeRecommendationLimitationsResponse(BaseValidatorModel):
    Limitations: List[Limitation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRefreshSchemasStatusResponse(BaseValidatorModel):
    RefreshSchemasStatus: RefreshSchemasStatus
    ResponseMetadata: ResponseMetadata


class RefreshSchemasResponse(BaseValidatorModel):
    RefreshSchemasStatus: RefreshSchemasStatus
    ResponseMetadata: ResponseMetadata


class DescribeReplicationInstanceTaskLogsResponse(BaseValidatorModel):
    ReplicationInstanceArn: str
    ReplicationInstanceTaskLogs: List[ReplicationInstanceTaskLog]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeReplicationTableStatisticsResponse(BaseValidatorModel):
    ReplicationConfigArn: str
    Marker: str
    ReplicationTableStatistics: List[TableStatistics]
    ResponseMetadata: ResponseMetadata


class DescribeTableStatisticsResponse(BaseValidatorModel):
    ReplicationTaskArn: str
    TableStatistics: List[TableStatistics]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeReplicationTaskAssessmentResultsResponse(BaseValidatorModel):
    Marker: str
    BucketName: str
    ReplicationTaskAssessmentResults: List[ReplicationTaskAssessmentResult]
    ResponseMetadata: ResponseMetadata


class DescribeReplicationTaskIndividualAssessmentsResponse(BaseValidatorModel):
    Marker: str
    ReplicationTaskIndividualAssessments: List[ReplicationTaskIndividualAssessment]
    ResponseMetadata: ResponseMetadata


class Endpoint(BaseValidatorModel):
    EndpointIdentifier: Optional[str] = None
    EndpointType: Optional[ReplicationEndpointTypeValueType] = None
    EngineName: Optional[str] = None
    EngineDisplayName: Optional[str] = None
    Username: Optional[str] = None
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    ExtraConnectionAttributes: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    EndpointArn: Optional[str] = None
    CertificateArn: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    ServiceAccessRoleArn: Optional[str] = None
    ExternalTableDefinition: Optional[str] = None
    ExternalId: Optional[str] = None
    DynamoDbSettings: Optional[DynamoDbSettings] = None
    S3Settings: Optional[S3Settings] = None
    DmsTransferSettings: Optional[DmsTransferSettings] = None
    MongoDbSettings: Optional[MongoDbSettings] = None
    KinesisSettings: Optional[KinesisSettings] = None
    KafkaSettings: Optional[KafkaSettings] = None
    ElasticsearchSettings: Optional[ElasticsearchSettings] = None
    NeptuneSettings: Optional[NeptuneSettings] = None
    RedshiftSettings: Optional[RedshiftSettings] = None
    PostgreSQLSettings: Optional[PostgreSQLSettings] = None
    MySQLSettings: Optional[MySQLSettings] = None
    OracleSettings: Optional[OracleSettingsOutput] = None
    SybaseSettings: Optional[SybaseSettings] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettings] = None
    IBMDb2Settings: Optional[IBMDb2Settings] = None
    DocDbSettings: Optional[DocDbSettings] = None
    RedisSettings: Optional[RedisSettings] = None
    GcpMySQLSettings: Optional[GcpMySQLSettings] = None
    TimestreamSettings: Optional[TimestreamSettings] = None


class ExportMetadataModelAssessmentResponse(BaseValidatorModel):
    PdfReport: ExportMetadataModelAssessmentResultEntry
    CsvReport: ExportMetadataModelAssessmentResultEntry
    ResponseMetadata: ResponseMetadata

OracleSettingsUnion = Union[OracleSettings, OracleSettingsOutput]


class ResourcePendingMaintenanceActions(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceAction]] = None


class PremigrationAssessmentStatus(BaseValidatorModel):
    PremigrationAssessmentRunArn: Optional[str] = None
    FailOnAssessmentFailure: Optional[bool] = None
    Status: Optional[str] = None
    PremigrationAssessmentRunCreationDate: Optional[datetime] = None
    AssessmentProgress: Optional[ReplicationTaskAssessmentRunProgress] = None
    LastFailureMessage: Optional[str] = None
    ResultLocationBucket: Optional[str] = None
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    ResultStatistic: Optional[ReplicationTaskAssessmentRunResultStatistic] = None


class ReplicationTaskAssessmentRun(BaseValidatorModel):
    ReplicationTaskAssessmentRunArn: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    Status: Optional[str] = None
    ReplicationTaskAssessmentRunCreationDate: Optional[datetime] = None
    AssessmentProgress: Optional[ReplicationTaskAssessmentRunProgress] = None
    LastFailureMessage: Optional[str] = None
    ServiceAccessRoleArn: Optional[str] = None
    ResultLocationBucket: Optional[str] = None
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    AssessmentRunName: Optional[str] = None
    IsLatestTaskAssessmentRun: Optional[bool] = None
    ResultStatistic: Optional[ReplicationTaskAssessmentRunResultStatistic] = None


class RdsRecommendation(BaseValidatorModel):
    RequirementsToTarget: Optional[RdsRequirements] = None
    TargetConfiguration: Optional[RdsConfiguration] = None


class StartRecommendationsRequestEntry(BaseValidatorModel):
    DatabaseId: str
    Settings: RecommendationSettings


class StartRecommendationsRequest(BaseValidatorModel):
    DatabaseId: str
    Settings: RecommendationSettings


class ReloadReplicationTablesMessage(BaseValidatorModel):
    ReplicationConfigArn: str
    TablesToReload: List[TableToReload]
    ReloadOption: Optional[ReloadOptionValueType] = None


class ReloadTablesMessage(BaseValidatorModel):
    ReplicationTaskArn: str
    TablesToReload: List[TableToReload]
    ReloadOption: Optional[ReloadOptionValueType] = None


class ReplicationTask(BaseValidatorModel):
    ReplicationTaskIdentifier: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationTaskSettings: Optional[str] = None
    Status: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    StopReason: Optional[str] = None
    ReplicationTaskCreationDate: Optional[datetime] = None
    ReplicationTaskStartDate: Optional[datetime] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    RecoveryCheckpoint: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationTaskStats: Optional[ReplicationTaskStats] = None
    TaskData: Optional[str] = None
    TargetReplicationInstanceArn: Optional[str] = None


class SchemaResponse(BaseValidatorModel):
    CodeLineCount: Optional[int] = None
    CodeSize: Optional[int] = None
    Complexity: Optional[str] = None
    Server: Optional[ServerShortInfoResponse] = None
    DatabaseInstance: Optional[DatabaseShortInfoResponse] = None
    SchemaId: Optional[str] = None
    SchemaName: Optional[str] = None
    OriginalSchema: Optional[SchemaShortInfoResponse] = None
    Similarity: Optional[float] = None


class ReplicationSubnetGroup(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None
    ReplicationSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    SupportedNetworkTypes: Optional[List[str]] = None


class DescribeFleetAdvisorCollectorsResponse(BaseValidatorModel):
    Collectors: List[CollectorResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateReplicationConfigResponse(BaseValidatorModel):
    ReplicationConfig: ReplicationConfig
    ResponseMetadata: ResponseMetadata


class DeleteReplicationConfigResponse(BaseValidatorModel):
    ReplicationConfig: ReplicationConfig
    ResponseMetadata: ResponseMetadata


class DescribeReplicationConfigsResponse(BaseValidatorModel):
    Marker: str
    ReplicationConfigs: List[ReplicationConfig]
    ResponseMetadata: ResponseMetadata


class ModifyReplicationConfigResponse(BaseValidatorModel):
    ReplicationConfig: ReplicationConfig
    ResponseMetadata: ResponseMetadata


class CreateReplicationConfigMessage(BaseValidatorModel):
    ReplicationConfigIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ComputeConfig: ComputeConfigUnion
    ReplicationType: MigrationTypeValueType
    TableMappings: str
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ModifyReplicationConfigMessage(BaseValidatorModel):
    ReplicationConfigArn: str
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    ComputeConfig: Optional[ComputeConfigUnion] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None

SourceDataSettingUnion = Union[SourceDataSetting, SourceDataSettingOutput]


class CreateDataMigrationResponse(BaseValidatorModel):
    DataMigration: DataMigration
    ResponseMetadata: ResponseMetadata


class DeleteDataMigrationResponse(BaseValidatorModel):
    DataMigration: DataMigration
    ResponseMetadata: ResponseMetadata


class DescribeDataMigrationsResponse(BaseValidatorModel):
    DataMigrations: List[DataMigration]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ModifyDataMigrationResponse(BaseValidatorModel):
    DataMigration: DataMigration
    ResponseMetadata: ResponseMetadata


class StartDataMigrationResponse(BaseValidatorModel):
    DataMigration: DataMigration
    ResponseMetadata: ResponseMetadata


class StopDataMigrationResponse(BaseValidatorModel):
    DataMigration: DataMigration
    ResponseMetadata: ResponseMetadata


class CreateMigrationProjectResponse(BaseValidatorModel):
    MigrationProject: MigrationProject
    ResponseMetadata: ResponseMetadata


class DeleteMigrationProjectResponse(BaseValidatorModel):
    MigrationProject: MigrationProject
    ResponseMetadata: ResponseMetadata


class DescribeMigrationProjectsResponse(BaseValidatorModel):
    Marker: str
    MigrationProjects: List[MigrationProject]
    ResponseMetadata: ResponseMetadata


class ModifyMigrationProjectResponse(BaseValidatorModel):
    MigrationProject: MigrationProject
    ResponseMetadata: ResponseMetadata


class CreateDataProviderMessage(BaseValidatorModel):
    Engine: str
    Settings: DataProviderSettings
    DataProviderName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DataProvider(BaseValidatorModel):
    DataProviderName: Optional[str] = None
    DataProviderArn: Optional[str] = None
    DataProviderCreationTime: Optional[datetime] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    Settings: Optional[DataProviderSettings] = None


class ModifyDataProviderMessage(BaseValidatorModel):
    DataProviderIdentifier: str
    DataProviderName: Optional[str] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    ExactSettings: Optional[bool] = None
    Settings: Optional[DataProviderSettings] = None


class DescribeFleetAdvisorDatabasesResponse(BaseValidatorModel):
    Databases: List[DatabaseResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SchemaConversionRequest(BaseValidatorModel):
    Status: Optional[str] = None
    RequestIdentifier: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    Error: Optional[ErrorDetails] = None
    ExportSqlDetails: Optional[ExportSqlDetails] = None


class CreateEndpointResponse(BaseValidatorModel):
    Endpoint: Endpoint
    ResponseMetadata: ResponseMetadata


class DeleteEndpointResponse(BaseValidatorModel):
    Endpoint: Endpoint
    ResponseMetadata: ResponseMetadata


class DescribeEndpointsResponse(BaseValidatorModel):
    Marker: str
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata


class ModifyEndpointResponse(BaseValidatorModel):
    Endpoint: Endpoint
    ResponseMetadata: ResponseMetadata


class CreateEndpointMessage(BaseValidatorModel):
    EndpointIdentifier: str
    EndpointType: ReplicationEndpointTypeValueType
    EngineName: str
    Username: Optional[str] = None
    Password: Optional[str] = None
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    ExtraConnectionAttributes: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CertificateArn: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    ServiceAccessRoleArn: Optional[str] = None
    ExternalTableDefinition: Optional[str] = None
    DynamoDbSettings: Optional[DynamoDbSettings] = None
    S3Settings: Optional[S3Settings] = None
    DmsTransferSettings: Optional[DmsTransferSettings] = None
    MongoDbSettings: Optional[MongoDbSettings] = None
    KinesisSettings: Optional[KinesisSettings] = None
    KafkaSettings: Optional[KafkaSettings] = None
    ElasticsearchSettings: Optional[ElasticsearchSettings] = None
    NeptuneSettings: Optional[NeptuneSettings] = None
    RedshiftSettings: Optional[RedshiftSettings] = None
    PostgreSQLSettings: Optional[PostgreSQLSettings] = None
    MySQLSettings: Optional[MySQLSettings] = None
    OracleSettings: Optional[OracleSettingsUnion] = None
    SybaseSettings: Optional[SybaseSettings] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettings] = None
    IBMDb2Settings: Optional[IBMDb2Settings] = None
    ResourceIdentifier: Optional[str] = None
    DocDbSettings: Optional[DocDbSettings] = None
    RedisSettings: Optional[RedisSettings] = None
    GcpMySQLSettings: Optional[GcpMySQLSettings] = None
    TimestreamSettings: Optional[TimestreamSettings] = None


class ModifyEndpointMessage(BaseValidatorModel):
    EndpointArn: str
    EndpointIdentifier: Optional[str] = None
    EndpointType: Optional[ReplicationEndpointTypeValueType] = None
    EngineName: Optional[str] = None
    Username: Optional[str] = None
    Password: Optional[str] = None
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    ExtraConnectionAttributes: Optional[str] = None
    CertificateArn: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    ServiceAccessRoleArn: Optional[str] = None
    ExternalTableDefinition: Optional[str] = None
    DynamoDbSettings: Optional[DynamoDbSettings] = None
    S3Settings: Optional[S3Settings] = None
    DmsTransferSettings: Optional[DmsTransferSettings] = None
    MongoDbSettings: Optional[MongoDbSettings] = None
    KinesisSettings: Optional[KinesisSettings] = None
    KafkaSettings: Optional[KafkaSettings] = None
    ElasticsearchSettings: Optional[ElasticsearchSettings] = None
    NeptuneSettings: Optional[NeptuneSettings] = None
    RedshiftSettings: Optional[RedshiftSettings] = None
    PostgreSQLSettings: Optional[PostgreSQLSettings] = None
    MySQLSettings: Optional[MySQLSettings] = None
    OracleSettings: Optional[OracleSettingsUnion] = None
    SybaseSettings: Optional[SybaseSettings] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettings] = None
    IBMDb2Settings: Optional[IBMDb2Settings] = None
    DocDbSettings: Optional[DocDbSettings] = None
    RedisSettings: Optional[RedisSettings] = None
    ExactSettings: Optional[bool] = None
    GcpMySQLSettings: Optional[GcpMySQLSettings] = None
    TimestreamSettings: Optional[TimestreamSettings] = None


class ApplyPendingMaintenanceActionResponse(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActions
    ResponseMetadata: ResponseMetadata


class DescribePendingMaintenanceActionsResponse(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActions]
    Marker: str
    ResponseMetadata: ResponseMetadata


class Replication(BaseValidatorModel):
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    Status: Optional[str] = None
    ProvisionData: Optional[ProvisionData] = None
    PremigrationAssessmentStatuses: Optional[List[PremigrationAssessmentStatus]] = None
    StopReason: Optional[str] = None
    FailureMessages: Optional[List[str]] = None
    ReplicationStats: Optional[ReplicationStats] = None
    StartReplicationType: Optional[str] = None
    CdcStartTime: Optional[datetime] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    RecoveryCheckpoint: Optional[str] = None
    ReplicationCreateTime: Optional[datetime] = None
    ReplicationUpdateTime: Optional[datetime] = None
    ReplicationLastStopTime: Optional[datetime] = None
    ReplicationDeprovisionTime: Optional[datetime] = None


class CancelReplicationTaskAssessmentRunResponse(BaseValidatorModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRun
    ResponseMetadata: ResponseMetadata


class DeleteReplicationTaskAssessmentRunResponse(BaseValidatorModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRun
    ResponseMetadata: ResponseMetadata


class DescribeReplicationTaskAssessmentRunsResponse(BaseValidatorModel):
    Marker: str
    ReplicationTaskAssessmentRuns: List[ReplicationTaskAssessmentRun]
    ResponseMetadata: ResponseMetadata


class StartReplicationTaskAssessmentRunResponse(BaseValidatorModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRun
    ResponseMetadata: ResponseMetadata


class RecommendationData(BaseValidatorModel):
    RdsEngine: Optional[RdsRecommendation] = None


class BatchStartRecommendationsRequest(BaseValidatorModel):
    Data: Optional[List[StartRecommendationsRequestEntry]] = None


class CreateReplicationTaskResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class DeleteReplicationTaskResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class DescribeReplicationTasksResponse(BaseValidatorModel):
    Marker: str
    ReplicationTasks: List[ReplicationTask]
    ResponseMetadata: ResponseMetadata


class ModifyReplicationTaskResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class MoveReplicationTaskResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class StartReplicationTaskAssessmentResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class StartReplicationTaskResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class StopReplicationTaskResponse(BaseValidatorModel):
    ReplicationTask: ReplicationTask
    ResponseMetadata: ResponseMetadata


class DescribeFleetAdvisorSchemasResponse(BaseValidatorModel):
    FleetAdvisorSchemas: List[SchemaResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateReplicationSubnetGroupResponse(BaseValidatorModel):
    ReplicationSubnetGroup: ReplicationSubnetGroup
    ResponseMetadata: ResponseMetadata


class DescribeReplicationSubnetGroupsResponse(BaseValidatorModel):
    Marker: str
    ReplicationSubnetGroups: List[ReplicationSubnetGroup]
    ResponseMetadata: ResponseMetadata


class ModifyReplicationSubnetGroupResponse(BaseValidatorModel):
    ReplicationSubnetGroup: ReplicationSubnetGroup
    ResponseMetadata: ResponseMetadata


class ReplicationInstance(BaseValidatorModel):
    ReplicationInstanceIdentifier: Optional[str] = None
    ReplicationInstanceClass: Optional[str] = None
    ReplicationInstanceStatus: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    InstanceCreateTime: Optional[datetime] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    AvailabilityZone: Optional[str] = None
    ReplicationSubnetGroup: Optional[ReplicationSubnetGroup] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[ReplicationPendingModifiedValues] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    ReplicationInstancePublicIpAddress: Optional[str] = None
    ReplicationInstancePrivateIpAddress: Optional[str] = None
    ReplicationInstancePublicIpAddresses: Optional[List[str]] = None
    ReplicationInstancePrivateIpAddresses: Optional[List[str]] = None
    ReplicationInstanceIpv6Addresses: Optional[List[str]] = None
    PubliclyAccessible: Optional[bool] = None
    SecondaryAvailabilityZone: Optional[str] = None
    FreeUntil: Optional[datetime] = None
    DnsNameServers: Optional[str] = None
    NetworkType: Optional[str] = None
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettings] = None


class CreateDataMigrationMessage(BaseValidatorModel):
    MigrationProjectIdentifier: str
    DataMigrationType: MigrationTypeValueType
    ServiceAccessRoleArn: str
    DataMigrationName: Optional[str] = None
    EnableCloudwatchLogs: Optional[bool] = None
    SourceDataSettings: Optional[List[SourceDataSettingUnion]] = None
    TargetDataSettings: Optional[List[TargetDataSetting]] = None
    NumberOfJobs: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    SelectionRules: Optional[str] = None


class ModifyDataMigrationMessage(BaseValidatorModel):
    DataMigrationIdentifier: str
    DataMigrationName: Optional[str] = None
    EnableCloudwatchLogs: Optional[bool] = None
    ServiceAccessRoleArn: Optional[str] = None
    DataMigrationType: Optional[MigrationTypeValueType] = None
    SourceDataSettings: Optional[List[SourceDataSettingUnion]] = None
    TargetDataSettings: Optional[List[TargetDataSetting]] = None
    NumberOfJobs: Optional[int] = None
    SelectionRules: Optional[str] = None


class CreateDataProviderResponse(BaseValidatorModel):
    DataProvider: DataProvider
    ResponseMetadata: ResponseMetadata


class DeleteDataProviderResponse(BaseValidatorModel):
    DataProvider: DataProvider
    ResponseMetadata: ResponseMetadata


class DescribeDataProvidersResponse(BaseValidatorModel):
    Marker: str
    DataProviders: List[DataProvider]
    ResponseMetadata: ResponseMetadata


class ModifyDataProviderResponse(BaseValidatorModel):
    DataProvider: DataProvider
    ResponseMetadata: ResponseMetadata


class DescribeExtensionPackAssociationsResponse(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequest]
    ResponseMetadata: ResponseMetadata


class DescribeMetadataModelAssessmentsResponse(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequest]
    ResponseMetadata: ResponseMetadata


class DescribeMetadataModelConversionsResponse(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequest]
    ResponseMetadata: ResponseMetadata


class DescribeMetadataModelExportsAsScriptResponse(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequest]
    ResponseMetadata: ResponseMetadata


class DescribeMetadataModelExportsToTargetResponse(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequest]
    ResponseMetadata: ResponseMetadata


class DescribeMetadataModelImportsResponse(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequest]
    ResponseMetadata: ResponseMetadata


class DescribeReplicationsResponse(BaseValidatorModel):
    Marker: str
    Replications: List[Replication]
    ResponseMetadata: ResponseMetadata


class StartReplicationResponse(BaseValidatorModel):
    Replication: Replication
    ResponseMetadata: ResponseMetadata


class StopReplicationResponse(BaseValidatorModel):
    Replication: Replication
    ResponseMetadata: ResponseMetadata


class Recommendation(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    EngineName: Optional[str] = None
    CreatedDate: Optional[str] = None
    Status: Optional[str] = None
    Preferred: Optional[bool] = None
    Settings: Optional[RecommendationSettings] = None
    Data: Optional[RecommendationData] = None


class CreateReplicationInstanceResponse(BaseValidatorModel):
    ReplicationInstance: ReplicationInstance
    ResponseMetadata: ResponseMetadata


class DeleteReplicationInstanceResponse(BaseValidatorModel):
    ReplicationInstance: ReplicationInstance
    ResponseMetadata: ResponseMetadata


class DescribeReplicationInstancesResponse(BaseValidatorModel):
    Marker: str
    ReplicationInstances: List[ReplicationInstance]
    ResponseMetadata: ResponseMetadata


class ModifyReplicationInstanceResponse(BaseValidatorModel):
    ReplicationInstance: ReplicationInstance
    ResponseMetadata: ResponseMetadata


class RebootReplicationInstanceResponse(BaseValidatorModel):
    ReplicationInstance: ReplicationInstance
    ResponseMetadata: ResponseMetadata


class DescribeRecommendationsResponse(BaseValidatorModel):
    Recommendations: List[Recommendation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None