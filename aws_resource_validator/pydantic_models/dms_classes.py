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
from aws_resource_validator.pydantic_models.dms_constants import *

class AccountQuotaTypeDef(BaseValidatorModel):
    AccountQuotaName: Optional[str] = None
    Used: Optional[int] = None
    Max: Optional[int] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    ResourceArn: Optional[str] = None


class ApplyPendingMaintenanceActionMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str
    ApplyAction: str
    OptInType: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class BatchStartRecommendationsErrorEntryTypeDef(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    Message: Optional[str] = None
    Code: Optional[str] = None


class CancelReplicationTaskAssessmentRunMessageTypeDef(BaseValidatorModel):
    ReplicationTaskAssessmentRunArn: str


class CertificateTypeDef(BaseValidatorModel):
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


class CollectorHealthCheckTypeDef(BaseValidatorModel):
    CollectorStatus: Optional[CollectorStatusType] = None
    LocalCollectorS3Access: Optional[bool] = None
    WebCollectorS3Access: Optional[bool] = None
    WebCollectorGrantedRoleBasedAccess: Optional[bool] = None


class InventoryDataTypeDef(BaseValidatorModel):
    NumberOfDatabases: Optional[int] = None
    NumberOfSchemas: Optional[int] = None


class CollectorShortInfoResponseTypeDef(BaseValidatorModel):
    CollectorReferencedId: Optional[str] = None
    CollectorName: Optional[str] = None


class ComputeConfigOutputTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    DnsNameServers: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MaxCapacityUnits: Optional[int] = None
    MinCapacityUnits: Optional[int] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSubnetGroupId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None


class ComputeConfigTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    DnsNameServers: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MaxCapacityUnits: Optional[int] = None
    MinCapacityUnits: Optional[int] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSubnetGroupId: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None


class ConnectionTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: Optional[str] = None
    EndpointArn: Optional[str] = None
    Status: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    EndpointIdentifier: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None


class TargetDataSettingTypeDef(BaseValidatorModel):
    TablePreparationMode: Optional[TablePreparationModeType] = None


class DmsTransferSettingsTypeDef(BaseValidatorModel):
    ServiceAccessRoleArn: Optional[str] = None
    BucketName: Optional[str] = None


class DocDbSettingsTypeDef(BaseValidatorModel):
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


class DynamoDbSettingsTypeDef(BaseValidatorModel):
    ServiceAccessRoleArn: str


class ElasticsearchSettingsTypeDef(BaseValidatorModel):
    ServiceAccessRoleArn: str
    EndpointUri: str
    FullLoadErrorPercentage: Optional[int] = None
    ErrorRetryDuration: Optional[int] = None
    UseNewMappingType: Optional[bool] = None


class GcpMySQLSettingsTypeDef(BaseValidatorModel):
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


class IBMDb2SettingsTypeDef(BaseValidatorModel):
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


class KafkaSettingsTypeDef(BaseValidatorModel):
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


class KinesisSettingsTypeDef(BaseValidatorModel):
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


class MicrosoftSQLServerSettingsTypeDef(BaseValidatorModel):
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


class MongoDbSettingsTypeDef(BaseValidatorModel):
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


class MySQLSettingsTypeDef(BaseValidatorModel):
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


class NeptuneSettingsTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3BucketFolder: str
    ServiceAccessRoleArn: Optional[str] = None
    ErrorRetryDuration: Optional[int] = None
    MaxFileSize: Optional[int] = None
    MaxRetryCount: Optional[int] = None
    IamAuthEnabled: Optional[bool] = None


class PostgreSQLSettingsTypeDef(BaseValidatorModel):
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


class RedisSettingsTypeDef(BaseValidatorModel):
    ServerName: str
    Port: int
    SslSecurityProtocol: Optional[SslSecurityProtocolValueType] = None
    AuthType: Optional[RedisAuthTypeValueType] = None
    AuthUserName: Optional[str] = None
    AuthPassword: Optional[str] = None
    SslCaCertificateArn: Optional[str] = None


class RedshiftSettingsTypeDef(BaseValidatorModel):
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


class S3SettingsTypeDef(BaseValidatorModel):
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


class SybaseSettingsTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    Username: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None


class TimestreamSettingsTypeDef(BaseValidatorModel):
    DatabaseName: str
    MemoryDuration: int
    MagneticDuration: int
    CdcInsertsAndUpdates: Optional[bool] = None
    EnableMagneticStoreWrites: Optional[bool] = None


class EventSubscriptionTypeDef(BaseValidatorModel):
    CustomerAwsId: Optional[str] = None
    CustSubscriptionId: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    EventCategoriesList: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class CreateFleetAdvisorCollectorRequestTypeDef(BaseValidatorModel):
    CollectorName: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    Description: Optional[str] = None


class InstanceProfileTypeDef(BaseValidatorModel):
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


class DataProviderDescriptorDefinitionTypeDef(BaseValidatorModel):
    DataProviderIdentifier: str
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None


class SCApplicationAttributesTypeDef(BaseValidatorModel):
    S3BucketPath: Optional[str] = None
    S3BucketRoleArn: Optional[str] = None


class KerberosAuthenticationSettingsTypeDef(BaseValidatorModel):
    KeyCacheSecretId: Optional[str] = None
    KeyCacheSecretIamArn: Optional[str] = None
    Krb5FileContents: Optional[str] = None


class DataMigrationSettingsTypeDef(BaseValidatorModel):
    NumberOfJobs: Optional[int] = None
    CloudwatchLogsEnabled: Optional[bool] = None
    SelectionRules: Optional[str] = None


class DataMigrationStatisticsTypeDef(BaseValidatorModel):
    TablesLoaded: Optional[int] = None
    ElapsedTimeMillis: Optional[int] = None
    TablesLoading: Optional[int] = None
    FullLoadPercentage: Optional[int] = None
    CDCLatency: Optional[int] = None
    TablesQueued: Optional[int] = None
    TablesErrored: Optional[int] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None


class SourceDataSettingOutputTypeDef(BaseValidatorModel):
    CDCStartPosition: Optional[str] = None
    CDCStartTime: Optional[datetime] = None
    CDCStopTime: Optional[datetime] = None
    SlotName: Optional[str] = None


class DataProviderDescriptorTypeDef(BaseValidatorModel):
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    DataProviderName: Optional[str] = None
    DataProviderArn: Optional[str] = None


class DocDbDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class IbmDb2LuwDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class IbmDb2zOsDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class MariaDbDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class MicrosoftSqlServerDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class MongoDbDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None
    AuthType: Optional[AuthTypeValueType] = None
    AuthSource: Optional[str] = None
    AuthMechanism: Optional[AuthMechanismValueType] = None


class MySqlDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class OracleDataProviderSettingsTypeDef(BaseValidatorModel):
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


class PostgreSqlDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None


class RedshiftDataProviderSettingsTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None


class DatabaseInstanceSoftwareDetailsResponseTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineEdition: Optional[str] = None
    ServicePack: Optional[str] = None
    SupportLevel: Optional[str] = None
    OsArchitecture: Optional[int] = None
    Tooltip: Optional[str] = None


class ServerShortInfoResponseTypeDef(BaseValidatorModel):
    ServerId: Optional[str] = None
    IpAddress: Optional[str] = None
    ServerName: Optional[str] = None


class DatabaseShortInfoResponseTypeDef(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseIpAddress: Optional[str] = None
    DatabaseEngine: Optional[str] = None


class DefaultErrorDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class DeleteCertificateMessageTypeDef(BaseValidatorModel):
    CertificateArn: str


class DeleteCollectorRequestTypeDef(BaseValidatorModel):
    CollectorReferencedId: str


class DeleteConnectionMessageTypeDef(BaseValidatorModel):
    EndpointArn: str
    ReplicationInstanceArn: str


class DeleteDataMigrationMessageTypeDef(BaseValidatorModel):
    DataMigrationIdentifier: str


class DeleteDataProviderMessageTypeDef(BaseValidatorModel):
    DataProviderIdentifier: str


class DeleteEndpointMessageTypeDef(BaseValidatorModel):
    EndpointArn: str


class DeleteEventSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str


class DeleteFleetAdvisorDatabasesRequestTypeDef(BaseValidatorModel):
    DatabaseIds: Sequence[str]


class DeleteInstanceProfileMessageTypeDef(BaseValidatorModel):
    InstanceProfileIdentifier: str


class DeleteMigrationProjectMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str


class DeleteReplicationConfigMessageTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str


class DeleteReplicationInstanceMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str


class DeleteReplicationSubnetGroupMessageTypeDef(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: str


class DeleteReplicationTaskAssessmentRunMessageTypeDef(BaseValidatorModel):
    ReplicationTaskAssessmentRunArn: str


class DeleteReplicationTaskMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str


class DescribeApplicableIndividualAssessmentsMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEngineName: Optional[str] = None
    TargetEngineName: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeConversionConfigurationMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str


class DescribeEndpointSettingsMessageTypeDef(BaseValidatorModel):
    EngineName: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class SupportedEndpointTypeTypeDef(BaseValidatorModel):
    EngineName: Optional[str] = None
    SupportsCDC: Optional[bool] = None
    EndpointType: Optional[ReplicationEndpointTypeValueType] = None
    ReplicationInstanceEngineMinimumVersion: Optional[str] = None
    EngineDisplayName: Optional[str] = None


class DescribeEngineVersionsMessageTypeDef(BaseValidatorModel):
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class EngineVersionTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    Lifecycle: Optional[str] = None
    ReleaseStatus: Optional[ReleaseStatusValuesType] = None
    LaunchDate: Optional[datetime] = None
    AutoUpgradeDate: Optional[datetime] = None
    DeprecationDate: Optional[datetime] = None
    ForceUpgradeDate: Optional[datetime] = None
    AvailableUpgrades: Optional[List[str]] = None


class EventCategoryGroupTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None


class EventTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal["replication-instance"]] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None


class DescribeFleetAdvisorLsaAnalysisRequestTypeDef(BaseValidatorModel):
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class FleetAdvisorLsaAnalysisResponseTypeDef(BaseValidatorModel):
    LsaAnalysisId: Optional[str] = None
    Status: Optional[str] = None


class FleetAdvisorSchemaObjectResponseTypeDef(BaseValidatorModel):
    SchemaId: Optional[str] = None
    ObjectType: Optional[str] = None
    NumberOfObjects: Optional[int] = None
    CodeLineCount: Optional[int] = None
    CodeSize: Optional[int] = None


class DescribeOrderableReplicationInstancesMessageTypeDef(BaseValidatorModel):
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class OrderableReplicationInstanceTypeDef(BaseValidatorModel):
    EngineVersion: Optional[str] = None
    ReplicationInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    MinAllocatedStorage: Optional[int] = None
    MaxAllocatedStorage: Optional[int] = None
    DefaultAllocatedStorage: Optional[int] = None
    IncludedAllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    ReleaseStatus: Optional[ReleaseStatusValuesType] = None


class DescribeRefreshSchemasStatusMessageTypeDef(BaseValidatorModel):
    EndpointArn: str


class RefreshSchemasStatusTypeDef(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    Status: Optional[RefreshSchemasStatusTypeValueType] = None
    LastRefreshDate: Optional[datetime] = None
    LastFailureMessage: Optional[str] = None


class DescribeReplicationInstanceTaskLogsMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class ReplicationInstanceTaskLogTypeDef(BaseValidatorModel):
    ReplicationTaskName: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationInstanceTaskLogSize: Optional[int] = None


class TableStatisticsTypeDef(BaseValidatorModel):
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


class DescribeReplicationTaskAssessmentResultsMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class ReplicationTaskAssessmentResultTypeDef(BaseValidatorModel):
    ReplicationTaskIdentifier: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationTaskLastAssessmentDate: Optional[datetime] = None
    AssessmentStatus: Optional[str] = None
    AssessmentResultsFile: Optional[str] = None
    AssessmentResults: Optional[str] = None
    S3ObjectUrl: Optional[str] = None


class ReplicationTaskIndividualAssessmentTypeDef(BaseValidatorModel):
    ReplicationTaskIndividualAssessmentArn: Optional[str] = None
    ReplicationTaskAssessmentRunArn: Optional[str] = None
    IndividualAssessmentName: Optional[str] = None
    Status: Optional[str] = None
    ReplicationTaskIndividualAssessmentStartDate: Optional[datetime] = None


class DescribeSchemasMessageTypeDef(BaseValidatorModel):
    EndpointArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class OracleSettingsOutputTypeDef(BaseValidatorModel):
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


class ExportMetadataModelAssessmentMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    FileName: Optional[str] = None
    AssessmentReportTypes: Optional[Sequence[AssessmentReportTypeType]] = None


class ExportMetadataModelAssessmentResultEntryTypeDef(BaseValidatorModel):
    S3ObjectKey: Optional[str] = None
    ObjectURL: Optional[str] = None


class ExportSqlDetailsTypeDef(BaseValidatorModel):
    S3ObjectKey: Optional[str] = None
    ObjectURL: Optional[str] = None


class ListTagsForResourceMessageTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceArnList: Optional[Sequence[str]] = None


class ModifyConversionConfigurationMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str


class ModifyEventSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class ModifyInstanceProfileMessageTypeDef(BaseValidatorModel):
    InstanceProfileIdentifier: str
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[str]] = None


class ModifyReplicationSubnetGroupMessageTypeDef(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: str
    SubnetIds: Sequence[str]
    ReplicationSubnetGroupDescription: Optional[str] = None


class MoveReplicationTaskMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    TargetReplicationInstanceArn: str


class OracleSettingsTypeDef(BaseValidatorModel):
    AddSupplementalLogging: Optional[bool] = None
    ArchivedLogDestId: Optional[int] = None
    AdditionalArchivedLogDestId: Optional[int] = None
    ExtraArchivedLogDestIds: Optional[Sequence[int]] = None
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


class PendingMaintenanceActionTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None


class ReplicationTaskAssessmentRunProgressTypeDef(BaseValidatorModel):
    IndividualAssessmentCount: Optional[int] = None
    IndividualAssessmentCompletedCount: Optional[int] = None


class ProvisionDataTypeDef(BaseValidatorModel):
    ProvisionState: Optional[str] = None
    ProvisionedCapacityUnits: Optional[int] = None
    DateProvisioned: Optional[datetime] = None
    IsNewProvisioningAvailable: Optional[bool] = None
    DateNewProvisioningDataAvailable: Optional[datetime] = None
    ReasonForNewProvisioningData: Optional[str] = None


class RdsConfigurationTypeDef(BaseValidatorModel):
    EngineEdition: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceVcpu: Optional[float] = None
    InstanceMemory: Optional[float] = None
    StorageType: Optional[str] = None
    StorageSize: Optional[int] = None
    StorageIops: Optional[int] = None
    DeploymentOption: Optional[str] = None
    EngineVersion: Optional[str] = None


class RdsRequirementsTypeDef(BaseValidatorModel):
    EngineEdition: Optional[str] = None
    InstanceVcpu: Optional[float] = None
    InstanceMemory: Optional[float] = None
    StorageSize: Optional[int] = None
    StorageIops: Optional[int] = None
    DeploymentOption: Optional[str] = None
    EngineVersion: Optional[str] = None


class RebootReplicationInstanceMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str
    ForceFailover: Optional[bool] = None
    ForcePlannedFailover: Optional[bool] = None


class RecommendationSettingsTypeDef(BaseValidatorModel):
    InstanceSizingType: str
    WorkloadType: str


class RefreshSchemasMessageTypeDef(BaseValidatorModel):
    EndpointArn: str
    ReplicationInstanceArn: str


class TableToReloadTypeDef(BaseValidatorModel):
    SchemaName: str
    TableName: str


class RemoveTagsFromResourceMessageTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class ReplicationPendingModifiedValuesTypeDef(BaseValidatorModel):
    ReplicationInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    NetworkType: Optional[str] = None


class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class ReplicationStatsTypeDef(BaseValidatorModel):
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


class ReplicationTaskStatsTypeDef(BaseValidatorModel):
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


class SchemaShortInfoResponseTypeDef(BaseValidatorModel):
    SchemaId: Optional[str] = None
    SchemaName: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseIpAddress: Optional[str] = None


class StartDataMigrationMessageTypeDef(BaseValidatorModel):
    DataMigrationIdentifier: str
    StartType: StartReplicationMigrationTypeValueType


class StartExtensionPackAssociationMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str


class StartMetadataModelAssessmentMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str


class StartMetadataModelConversionMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str


class StartMetadataModelExportAsScriptMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    FileName: Optional[str] = None


class StartMetadataModelExportToTargetMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    OverwriteExtensionPack: Optional[bool] = None


class StartMetadataModelImportMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    Refresh: Optional[bool] = None


class StartReplicationTaskAssessmentMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str


class StopDataMigrationMessageTypeDef(BaseValidatorModel):
    DataMigrationIdentifier: str


class StopReplicationMessageTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str


class StopReplicationTaskMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str


class TestConnectionMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str
    EndpointArn: str


class UpdateSubscriptionsToEventBridgeMessageTypeDef(BaseValidatorModel):
    ForceMove: Optional[bool] = None


class AddTagsToResourceMessageTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateEventSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateInstanceProfileMessageTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[str]] = None


class CreateReplicationSubnetGroupMessageTypeDef(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: str
    ReplicationSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartReplicationTaskAssessmentRunMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    ServiceAccessRoleArn: str
    ResultLocationBucket: str
    AssessmentRunName: str
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    IncludeOnly: Optional[Sequence[str]] = None
    Exclude: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateFleetAdvisorCollectorResponseTypeDef(BaseValidatorModel):
    CollectorReferencedId: str
    CollectorName: str
    Description: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFleetAdvisorDatabasesResponseTypeDef(BaseValidatorModel):
    DatabaseIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountAttributesResponseTypeDef(BaseValidatorModel):
    AccountQuotas: List[AccountQuotaTypeDef]
    UniqueAccountIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeApplicableIndividualAssessmentsResponseTypeDef(BaseValidatorModel):
    IndividualAssessmentNames: List[str]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConversionConfigurationResponseTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSchemasResponseTypeDef(BaseValidatorModel):
    Marker: str
    Schemas: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyConversionConfigurationResponseTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class ReloadReplicationTablesResponseTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ReloadTablesResponseTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class RunFleetAdvisorLsaAnalysisResponseTypeDef(BaseValidatorModel):
    LsaAnalysisId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartExtensionPackAssociationResponseTypeDef(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMetadataModelAssessmentResponseTypeDef(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMetadataModelConversionResponseTypeDef(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMetadataModelExportAsScriptResponseTypeDef(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMetadataModelExportToTargetResponseTypeDef(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMetadataModelImportResponseTypeDef(BaseValidatorModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSubscriptionsToEventBridgeResponseTypeDef(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef


class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None


class BatchStartRecommendationsResponseTypeDef(BaseValidatorModel):
    ErrorEntries: List[BatchStartRecommendationsErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class ImportCertificateMessageTypeDef(BaseValidatorModel):
    CertificateIdentifier: str
    CertificatePem: Optional[str] = None
    CertificateWallet: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DeleteCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCertificatesResponseTypeDef(BaseValidatorModel):
    Marker: str
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ImportCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CollectorResponseTypeDef(BaseValidatorModel):
    CollectorReferencedId: Optional[str] = None
    CollectorName: Optional[str] = None
    CollectorVersion: Optional[str] = None
    VersionStatus: Optional[VersionStatusType] = None
    Description: Optional[str] = None
    S3BucketName: Optional[str] = None
    ServiceAccessRoleArn: Optional[str] = None
    CollectorHealthCheck: Optional[CollectorHealthCheckTypeDef] = None
    LastDataReceived: Optional[str] = None
    RegisteredDate: Optional[str] = None
    CreatedDate: Optional[str] = None
    ModifiedDate: Optional[str] = None
    InventoryData: Optional[InventoryDataTypeDef] = None


class ReplicationConfigTypeDef(BaseValidatorModel):
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    ComputeConfig: Optional[ComputeConfigOutputTypeDef] = None
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    TableMappings: Optional[str] = None
    ReplicationConfigCreateTime: Optional[datetime] = None
    ReplicationConfigUpdateTime: Optional[datetime] = None


class DeleteConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConnectionsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TestConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventSubscriptionResponseTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEventSubscriptionResponseTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEventSubscriptionsResponseTypeDef(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyEventSubscriptionResponseTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstanceProfileResponseTypeDef(BaseValidatorModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInstanceProfileResponseTypeDef(BaseValidatorModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInstanceProfilesResponseTypeDef(BaseValidatorModel):
    Marker: str
    InstanceProfiles: List[InstanceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyInstanceProfileResponseTypeDef(BaseValidatorModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMigrationProjectMessageTypeDef(BaseValidatorModel):
    SourceDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef]
    TargetDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef]
    InstanceProfileIdentifier: str
    MigrationProjectName: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributesTypeDef] = None


class ModifyMigrationProjectMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    MigrationProjectName: Optional[str] = None
    SourceDataProviderDescriptors: Optional[Sequence[DataProviderDescriptorDefinitionTypeDef]] = None
    TargetDataProviderDescriptors: Optional[Sequence[DataProviderDescriptorDefinitionTypeDef]] = None
    InstanceProfileIdentifier: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributesTypeDef] = None


class CreateReplicationInstanceMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceIdentifier: str
    ReplicationInstanceClass: str
    AllocatedStorage: Optional[int] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None
    ReplicationSubnetGroupIdentifier: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    DnsNameServers: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    NetworkType: Optional[str] = None
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettingsTypeDef] = None


class ModifyReplicationInstanceMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str
    AllocatedStorage: Optional[int] = None
    ApplyImmediately: Optional[bool] = None
    ReplicationInstanceClass: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReplicationInstanceIdentifier: Optional[str] = None
    NetworkType: Optional[str] = None
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettingsTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateReplicationTaskMessageTypeDef(BaseValidatorModel):
    ReplicationTaskIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ReplicationInstanceArn: str
    MigrationType: MigrationTypeValueType
    TableMappings: str
    ReplicationTaskSettings: Optional[str] = None
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TaskData: Optional[str] = None
    ResourceIdentifier: Optional[str] = None


class ModifyReplicationTaskMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    ReplicationTaskIdentifier: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationTaskSettings: Optional[str] = None
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    TaskData: Optional[str] = None


class SourceDataSettingTypeDef(BaseValidatorModel):
    CDCStartPosition: Optional[str] = None
    CDCStartTime: Optional[TimestampTypeDef] = None
    CDCStopTime: Optional[TimestampTypeDef] = None
    SlotName: Optional[str] = None


class StartReplicationMessageTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str
    StartReplicationType: str
    PremigrationAssessmentSettings: Optional[str] = None
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None


class StartReplicationTaskMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    StartReplicationTaskType: StartReplicationTaskTypeValueType
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None


class DataMigrationTypeDef(BaseValidatorModel):
    DataMigrationName: Optional[str] = None
    DataMigrationArn: Optional[str] = None
    DataMigrationCreateTime: Optional[datetime] = None
    DataMigrationStartTime: Optional[datetime] = None
    DataMigrationEndTime: Optional[datetime] = None
    ServiceAccessRoleArn: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    DataMigrationType: Optional[MigrationTypeValueType] = None
    DataMigrationSettings: Optional[DataMigrationSettingsTypeDef] = None
    SourceDataSettings: Optional[List[SourceDataSettingOutputTypeDef]] = None
    TargetDataSettings: Optional[List[TargetDataSettingTypeDef]] = None
    DataMigrationStatistics: Optional[DataMigrationStatisticsTypeDef] = None
    DataMigrationStatus: Optional[str] = None
    PublicIpAddresses: Optional[List[str]] = None
    DataMigrationCidrBlocks: Optional[List[str]] = None
    LastFailureMessage: Optional[str] = None
    StopReason: Optional[str] = None


class MigrationProjectTypeDef(BaseValidatorModel):
    MigrationProjectName: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    MigrationProjectCreationTime: Optional[datetime] = None
    SourceDataProviderDescriptors: Optional[List[DataProviderDescriptorTypeDef]] = None
    TargetDataProviderDescriptors: Optional[List[DataProviderDescriptorTypeDef]] = None
    InstanceProfileArn: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributesTypeDef] = None


class DataProviderSettingsTypeDef(BaseValidatorModel):
    RedshiftSettings: Optional[RedshiftDataProviderSettingsTypeDef] = None
    PostgreSqlSettings: Optional[PostgreSqlDataProviderSettingsTypeDef] = None
    MySqlSettings: Optional[MySqlDataProviderSettingsTypeDef] = None
    OracleSettings: Optional[OracleDataProviderSettingsTypeDef] = None
    MicrosoftSqlServerSettings: Optional[MicrosoftSqlServerDataProviderSettingsTypeDef] = None
    DocDbSettings: Optional[DocDbDataProviderSettingsTypeDef] = None
    MariaDbSettings: Optional[MariaDbDataProviderSettingsTypeDef] = None
    IbmDb2LuwSettings: Optional[IbmDb2LuwDataProviderSettingsTypeDef] = None
    IbmDb2zOsSettings: Optional[IbmDb2zOsDataProviderSettingsTypeDef] = None
    MongoDbSettings: Optional[MongoDbDataProviderSettingsTypeDef] = None


class DatabaseResponseTypeDef(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    IpAddress: Optional[str] = None
    NumberOfSchemas: Optional[int] = None
    Server: Optional[ServerShortInfoResponseTypeDef] = None
    SoftwareDetails: Optional[DatabaseInstanceSoftwareDetailsResponseTypeDef] = None
    Collectors: Optional[List[CollectorShortInfoResponseTypeDef]] = None


class ErrorDetailsTypeDef(BaseValidatorModel):
    defaultErrorDetails: Optional[DefaultErrorDetailsTypeDef] = None


class DescribeCertificatesMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeConnectionsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDataMigrationsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WithoutStatistics: Optional[bool] = None


class DescribeDataProvidersMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEndpointTypesMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEndpointsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventCategoriesMessageTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class DescribeEventSubscriptionsMessageTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventsMessageTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal["replication-instance"]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeExtensionPackAssociationsMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeFleetAdvisorCollectorsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetAdvisorDatabasesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFleetAdvisorSchemasRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceProfilesMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeMetadataModelAssessmentsMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelConversionsMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelExportsAsScriptMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelExportsToTargetMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMetadataModelImportsMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeMigrationProjectsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribePendingMaintenanceActionsMessageTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeRecommendationLimitationsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeRecommendationsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReplicationConfigsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationInstancesMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationSubnetGroupsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationTableStatisticsMessageTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class DescribeReplicationTaskAssessmentRunsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationTaskIndividualAssessmentsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReplicationTasksMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None


class DescribeReplicationsMessageTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeTableStatisticsMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class DescribeCertificatesMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConnectionsMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDataMigrationsMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WithoutSettings: Optional[bool] = None
    WithoutStatistics: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEndpointTypesMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEndpointsMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventSubscriptionsMessagePaginateTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventsMessagePaginateTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal["replication-instance"]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOrderableReplicationInstancesMessagePaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReplicationInstancesMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReplicationSubnetGroupsMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef(BaseValidatorModel):
    ReplicationTaskArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReplicationTasksMessagePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WithoutSettings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSchemasMessagePaginateTypeDef(BaseValidatorModel):
    EndpointArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTableStatisticsMessagePaginateTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConnectionsMessageWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeEndpointsMessageWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationInstancesMessageWaitExtraTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationInstancesMessageWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationTasksMessageWaitExtraExtraTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationTasksMessageWaitExtraTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationTasksMessageWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class EndpointSettingTypeDef(BaseValidatorModel):
    pass


class DescribeEndpointSettingsResponseTypeDef(BaseValidatorModel):
    Marker: str
    EndpointSettings: List[EndpointSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEndpointTypesResponseTypeDef(BaseValidatorModel):
    Marker: str
    SupportedEndpointTypes: List[SupportedEndpointTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEngineVersionsResponseTypeDef(BaseValidatorModel):
    EngineVersions: List[EngineVersionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEventCategoriesResponseTypeDef(BaseValidatorModel):
    EventCategoryGroupList: List[EventCategoryGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEventsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFleetAdvisorLsaAnalysisResponseTypeDef(BaseValidatorModel):
    Analysis: List[FleetAdvisorLsaAnalysisResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef(BaseValidatorModel):
    FleetAdvisorSchemaObjects: List[FleetAdvisorSchemaObjectResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeOrderableReplicationInstancesResponseTypeDef(BaseValidatorModel):
    OrderableReplicationInstances: List[OrderableReplicationInstanceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class LimitationTypeDef(BaseValidatorModel):
    pass


class DescribeRecommendationLimitationsResponseTypeDef(BaseValidatorModel):
    Limitations: List[LimitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeRefreshSchemasStatusResponseTypeDef(BaseValidatorModel):
    RefreshSchemasStatus: RefreshSchemasStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RefreshSchemasResponseTypeDef(BaseValidatorModel):
    RefreshSchemasStatus: RefreshSchemasStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationInstanceTaskLogsResponseTypeDef(BaseValidatorModel):
    ReplicationInstanceArn: str
    ReplicationInstanceTaskLogs: List[ReplicationInstanceTaskLogTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationTableStatisticsResponseTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str
    Marker: str
    ReplicationTableStatistics: List[TableStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTableStatisticsResponseTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    TableStatistics: List[TableStatisticsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationTaskAssessmentResultsResponseTypeDef(BaseValidatorModel):
    Marker: str
    BucketName: str
    ReplicationTaskAssessmentResults: List[ReplicationTaskAssessmentResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationTaskIndividualAssessmentsResponseTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationTaskIndividualAssessments: List[ReplicationTaskIndividualAssessmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointTypeDef(BaseValidatorModel):
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
    DynamoDbSettings: Optional[DynamoDbSettingsTypeDef] = None
    S3Settings: Optional[S3SettingsTypeDef] = None
    DmsTransferSettings: Optional[DmsTransferSettingsTypeDef] = None
    MongoDbSettings: Optional[MongoDbSettingsTypeDef] = None
    KinesisSettings: Optional[KinesisSettingsTypeDef] = None
    KafkaSettings: Optional[KafkaSettingsTypeDef] = None
    ElasticsearchSettings: Optional[ElasticsearchSettingsTypeDef] = None
    NeptuneSettings: Optional[NeptuneSettingsTypeDef] = None
    RedshiftSettings: Optional[RedshiftSettingsTypeDef] = None
    PostgreSQLSettings: Optional[PostgreSQLSettingsTypeDef] = None
    MySQLSettings: Optional[MySQLSettingsTypeDef] = None
    OracleSettings: Optional[OracleSettingsOutputTypeDef] = None
    SybaseSettings: Optional[SybaseSettingsTypeDef] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettingsTypeDef] = None
    IBMDb2Settings: Optional[IBMDb2SettingsTypeDef] = None
    DocDbSettings: Optional[DocDbSettingsTypeDef] = None
    RedisSettings: Optional[RedisSettingsTypeDef] = None
    GcpMySQLSettings: Optional[GcpMySQLSettingsTypeDef] = None
    TimestreamSettings: Optional[TimestreamSettingsTypeDef] = None


class ExportMetadataModelAssessmentResponseTypeDef(BaseValidatorModel):
    PdfReport: ExportMetadataModelAssessmentResultEntryTypeDef
    CsvReport: ExportMetadataModelAssessmentResultEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResourcePendingMaintenanceActionsTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None


class ReplicationTaskAssessmentRunResultStatisticTypeDef(BaseValidatorModel):
    pass


class PremigrationAssessmentStatusTypeDef(BaseValidatorModel):
    PremigrationAssessmentRunArn: Optional[str] = None
    FailOnAssessmentFailure: Optional[bool] = None
    Status: Optional[str] = None
    PremigrationAssessmentRunCreationDate: Optional[datetime] = None
    AssessmentProgress: Optional[ReplicationTaskAssessmentRunProgressTypeDef] = None
    LastFailureMessage: Optional[str] = None
    ResultLocationBucket: Optional[str] = None
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    ResultStatistic: Optional[ReplicationTaskAssessmentRunResultStatisticTypeDef] = None


class ReplicationTaskAssessmentRunTypeDef(BaseValidatorModel):
    ReplicationTaskAssessmentRunArn: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    Status: Optional[str] = None
    ReplicationTaskAssessmentRunCreationDate: Optional[datetime] = None
    AssessmentProgress: Optional[ReplicationTaskAssessmentRunProgressTypeDef] = None
    LastFailureMessage: Optional[str] = None
    ServiceAccessRoleArn: Optional[str] = None
    ResultLocationBucket: Optional[str] = None
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    AssessmentRunName: Optional[str] = None
    IsLatestTaskAssessmentRun: Optional[bool] = None
    ResultStatistic: Optional[ReplicationTaskAssessmentRunResultStatisticTypeDef] = None


class RdsRecommendationTypeDef(BaseValidatorModel):
    RequirementsToTarget: Optional[RdsRequirementsTypeDef] = None
    TargetConfiguration: Optional[RdsConfigurationTypeDef] = None


class StartRecommendationsRequestEntryTypeDef(BaseValidatorModel):
    DatabaseId: str
    Settings: RecommendationSettingsTypeDef


class StartRecommendationsRequestTypeDef(BaseValidatorModel):
    DatabaseId: str
    Settings: RecommendationSettingsTypeDef


class ReloadReplicationTablesMessageTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str
    TablesToReload: Sequence[TableToReloadTypeDef]
    ReloadOption: Optional[ReloadOptionValueType] = None


class ReloadTablesMessageTypeDef(BaseValidatorModel):
    ReplicationTaskArn: str
    TablesToReload: Sequence[TableToReloadTypeDef]
    ReloadOption: Optional[ReloadOptionValueType] = None


class ReplicationTaskTypeDef(BaseValidatorModel):
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
    ReplicationTaskStats: Optional[ReplicationTaskStatsTypeDef] = None
    TaskData: Optional[str] = None
    TargetReplicationInstanceArn: Optional[str] = None


class SchemaResponseTypeDef(BaseValidatorModel):
    CodeLineCount: Optional[int] = None
    CodeSize: Optional[int] = None
    Complexity: Optional[str] = None
    Server: Optional[ServerShortInfoResponseTypeDef] = None
    DatabaseInstance: Optional[DatabaseShortInfoResponseTypeDef] = None
    SchemaId: Optional[str] = None
    SchemaName: Optional[str] = None
    OriginalSchema: Optional[SchemaShortInfoResponseTypeDef] = None
    Similarity: Optional[float] = None


class ReplicationSubnetGroupTypeDef(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None
    ReplicationSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    SupportedNetworkTypes: Optional[List[str]] = None


class DescribeFleetAdvisorCollectorsResponseTypeDef(BaseValidatorModel):
    Collectors: List[CollectorResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateReplicationConfigResponseTypeDef(BaseValidatorModel):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteReplicationConfigResponseTypeDef(BaseValidatorModel):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationConfigsResponseTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationConfigs: List[ReplicationConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyReplicationConfigResponseTypeDef(BaseValidatorModel):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ComputeConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateReplicationConfigMessageTypeDef(BaseValidatorModel):
    ReplicationConfigIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ComputeConfig: ComputeConfigUnionTypeDef
    ReplicationType: MigrationTypeValueType
    TableMappings: str
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ModifyReplicationConfigMessageTypeDef(BaseValidatorModel):
    ReplicationConfigArn: str
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    ComputeConfig: Optional[ComputeConfigUnionTypeDef] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None


class CreateDataMigrationResponseTypeDef(BaseValidatorModel):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataMigrationResponseTypeDef(BaseValidatorModel):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDataMigrationsResponseTypeDef(BaseValidatorModel):
    DataMigrations: List[DataMigrationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDataMigrationResponseTypeDef(BaseValidatorModel):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartDataMigrationResponseTypeDef(BaseValidatorModel):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopDataMigrationResponseTypeDef(BaseValidatorModel):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMigrationProjectResponseTypeDef(BaseValidatorModel):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMigrationProjectResponseTypeDef(BaseValidatorModel):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMigrationProjectsResponseTypeDef(BaseValidatorModel):
    Marker: str
    MigrationProjects: List[MigrationProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyMigrationProjectResponseTypeDef(BaseValidatorModel):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataProviderMessageTypeDef(BaseValidatorModel):
    Engine: str
    Settings: DataProviderSettingsTypeDef
    DataProviderName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DataProviderTypeDef(BaseValidatorModel):
    DataProviderName: Optional[str] = None
    DataProviderArn: Optional[str] = None
    DataProviderCreationTime: Optional[datetime] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    Settings: Optional[DataProviderSettingsTypeDef] = None


class ModifyDataProviderMessageTypeDef(BaseValidatorModel):
    DataProviderIdentifier: str
    DataProviderName: Optional[str] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    ExactSettings: Optional[bool] = None
    Settings: Optional[DataProviderSettingsTypeDef] = None


class DescribeFleetAdvisorDatabasesResponseTypeDef(BaseValidatorModel):
    Databases: List[DatabaseResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SchemaConversionRequestTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    RequestIdentifier: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    Error: Optional[ErrorDetailsTypeDef] = None
    ExportSqlDetails: Optional[ExportSqlDetailsTypeDef] = None


class CreateEndpointResponseTypeDef(BaseValidatorModel):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEndpointResponseTypeDef(BaseValidatorModel):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEndpointsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyEndpointResponseTypeDef(BaseValidatorModel):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OracleSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateEndpointMessageTypeDef(BaseValidatorModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    CertificateArn: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    ServiceAccessRoleArn: Optional[str] = None
    ExternalTableDefinition: Optional[str] = None
    DynamoDbSettings: Optional[DynamoDbSettingsTypeDef] = None
    S3Settings: Optional[S3SettingsTypeDef] = None
    DmsTransferSettings: Optional[DmsTransferSettingsTypeDef] = None
    MongoDbSettings: Optional[MongoDbSettingsTypeDef] = None
    KinesisSettings: Optional[KinesisSettingsTypeDef] = None
    KafkaSettings: Optional[KafkaSettingsTypeDef] = None
    ElasticsearchSettings: Optional[ElasticsearchSettingsTypeDef] = None
    NeptuneSettings: Optional[NeptuneSettingsTypeDef] = None
    RedshiftSettings: Optional[RedshiftSettingsTypeDef] = None
    PostgreSQLSettings: Optional[PostgreSQLSettingsTypeDef] = None
    MySQLSettings: Optional[MySQLSettingsTypeDef] = None
    OracleSettings: Optional[OracleSettingsUnionTypeDef] = None
    SybaseSettings: Optional[SybaseSettingsTypeDef] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettingsTypeDef] = None
    IBMDb2Settings: Optional[IBMDb2SettingsTypeDef] = None
    ResourceIdentifier: Optional[str] = None
    DocDbSettings: Optional[DocDbSettingsTypeDef] = None
    RedisSettings: Optional[RedisSettingsTypeDef] = None
    GcpMySQLSettings: Optional[GcpMySQLSettingsTypeDef] = None
    TimestreamSettings: Optional[TimestreamSettingsTypeDef] = None


class ModifyEndpointMessageTypeDef(BaseValidatorModel):
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
    DynamoDbSettings: Optional[DynamoDbSettingsTypeDef] = None
    S3Settings: Optional[S3SettingsTypeDef] = None
    DmsTransferSettings: Optional[DmsTransferSettingsTypeDef] = None
    MongoDbSettings: Optional[MongoDbSettingsTypeDef] = None
    KinesisSettings: Optional[KinesisSettingsTypeDef] = None
    KafkaSettings: Optional[KafkaSettingsTypeDef] = None
    ElasticsearchSettings: Optional[ElasticsearchSettingsTypeDef] = None
    NeptuneSettings: Optional[NeptuneSettingsTypeDef] = None
    RedshiftSettings: Optional[RedshiftSettingsTypeDef] = None
    PostgreSQLSettings: Optional[PostgreSQLSettingsTypeDef] = None
    MySQLSettings: Optional[MySQLSettingsTypeDef] = None
    OracleSettings: Optional[OracleSettingsUnionTypeDef] = None
    SybaseSettings: Optional[SybaseSettingsTypeDef] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettingsTypeDef] = None
    IBMDb2Settings: Optional[IBMDb2SettingsTypeDef] = None
    DocDbSettings: Optional[DocDbSettingsTypeDef] = None
    RedisSettings: Optional[RedisSettingsTypeDef] = None
    ExactSettings: Optional[bool] = None
    GcpMySQLSettings: Optional[GcpMySQLSettingsTypeDef] = None
    TimestreamSettings: Optional[TimestreamSettingsTypeDef] = None


class ApplyPendingMaintenanceActionResponseTypeDef(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePendingMaintenanceActionsResponseTypeDef(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ReplicationTypeDef(BaseValidatorModel):
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    Status: Optional[str] = None
    ProvisionData: Optional[ProvisionDataTypeDef] = None
    PremigrationAssessmentStatuses: Optional[List[PremigrationAssessmentStatusTypeDef]] = None
    StopReason: Optional[str] = None
    FailureMessages: Optional[List[str]] = None
    ReplicationStats: Optional[ReplicationStatsTypeDef] = None
    StartReplicationType: Optional[str] = None
    CdcStartTime: Optional[datetime] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    RecoveryCheckpoint: Optional[str] = None
    ReplicationCreateTime: Optional[datetime] = None
    ReplicationUpdateTime: Optional[datetime] = None
    ReplicationLastStopTime: Optional[datetime] = None
    ReplicationDeprovisionTime: Optional[datetime] = None


class CancelReplicationTaskAssessmentRunResponseTypeDef(BaseValidatorModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteReplicationTaskAssessmentRunResponseTypeDef(BaseValidatorModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationTaskAssessmentRunsResponseTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationTaskAssessmentRuns: List[ReplicationTaskAssessmentRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartReplicationTaskAssessmentRunResponseTypeDef(BaseValidatorModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RecommendationDataTypeDef(BaseValidatorModel):
    RdsEngine: Optional[RdsRecommendationTypeDef] = None


class BatchStartRecommendationsRequestTypeDef(BaseValidatorModel):
    Data: Optional[Sequence[StartRecommendationsRequestEntryTypeDef]] = None


class CreateReplicationTaskResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteReplicationTaskResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationTasksResponseTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationTasks: List[ReplicationTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyReplicationTaskResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MoveReplicationTaskResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartReplicationTaskAssessmentResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartReplicationTaskResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopReplicationTaskResponseTypeDef(BaseValidatorModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFleetAdvisorSchemasResponseTypeDef(BaseValidatorModel):
    FleetAdvisorSchemas: List[SchemaResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateReplicationSubnetGroupResponseTypeDef(BaseValidatorModel):
    ReplicationSubnetGroup: ReplicationSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationSubnetGroupsResponseTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationSubnetGroups: List[ReplicationSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyReplicationSubnetGroupResponseTypeDef(BaseValidatorModel):
    ReplicationSubnetGroup: ReplicationSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReplicationInstanceTypeDef(BaseValidatorModel):
    ReplicationInstanceIdentifier: Optional[str] = None
    ReplicationInstanceClass: Optional[str] = None
    ReplicationInstanceStatus: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    InstanceCreateTime: Optional[datetime] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    ReplicationSubnetGroup: Optional[ReplicationSubnetGroupTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[ReplicationPendingModifiedValuesTypeDef] = None
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
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettingsTypeDef] = None


class SourceDataSettingUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataMigrationMessageTypeDef(BaseValidatorModel):
    MigrationProjectIdentifier: str
    DataMigrationType: MigrationTypeValueType
    ServiceAccessRoleArn: str
    DataMigrationName: Optional[str] = None
    EnableCloudwatchLogs: Optional[bool] = None
    SourceDataSettings: Optional[Sequence[SourceDataSettingUnionTypeDef]] = None
    TargetDataSettings: Optional[Sequence[TargetDataSettingTypeDef]] = None
    NumberOfJobs: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SelectionRules: Optional[str] = None


class ModifyDataMigrationMessageTypeDef(BaseValidatorModel):
    DataMigrationIdentifier: str
    DataMigrationName: Optional[str] = None
    EnableCloudwatchLogs: Optional[bool] = None
    ServiceAccessRoleArn: Optional[str] = None
    DataMigrationType: Optional[MigrationTypeValueType] = None
    SourceDataSettings: Optional[Sequence[SourceDataSettingUnionTypeDef]] = None
    TargetDataSettings: Optional[Sequence[TargetDataSettingTypeDef]] = None
    NumberOfJobs: Optional[int] = None
    SelectionRules: Optional[str] = None


class CreateDataProviderResponseTypeDef(BaseValidatorModel):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataProviderResponseTypeDef(BaseValidatorModel):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDataProvidersResponseTypeDef(BaseValidatorModel):
    Marker: str
    DataProviders: List[DataProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDataProviderResponseTypeDef(BaseValidatorModel):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeExtensionPackAssociationsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetadataModelAssessmentsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetadataModelConversionsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetadataModelExportsAsScriptResponseTypeDef(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetadataModelExportsToTargetResponseTypeDef(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetadataModelImportsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Replications: List[ReplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartReplicationResponseTypeDef(BaseValidatorModel):
    Replication: ReplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopReplicationResponseTypeDef(BaseValidatorModel):
    Replication: ReplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RecommendationTypeDef(BaseValidatorModel):
    DatabaseId: Optional[str] = None
    EngineName: Optional[str] = None
    CreatedDate: Optional[str] = None
    Status: Optional[str] = None
    Preferred: Optional[bool] = None
    Settings: Optional[RecommendationSettingsTypeDef] = None
    Data: Optional[RecommendationDataTypeDef] = None


class CreateReplicationInstanceResponseTypeDef(BaseValidatorModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteReplicationInstanceResponseTypeDef(BaseValidatorModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReplicationInstancesResponseTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationInstances: List[ReplicationInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyReplicationInstanceResponseTypeDef(BaseValidatorModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RebootReplicationInstanceResponseTypeDef(BaseValidatorModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRecommendationsResponseTypeDef(BaseValidatorModel):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


