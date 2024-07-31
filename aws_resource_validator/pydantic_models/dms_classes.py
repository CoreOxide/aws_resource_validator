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
from aws_resource_validator.pydantic_models.dms_constants import *

class AccountQuotaTypeDef(BaseModel):
    AccountQuotaName: Optional[str] = None
    Used: Optional[int] = None
    Max: Optional[int] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    ResourceArn: Optional[str] = None

class ApplyPendingMaintenanceActionMessageRequestTypeDef(BaseModel):
    ReplicationInstanceArn: str
    ApplyAction: str
    OptInType: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class BatchStartRecommendationsErrorEntryTypeDef(BaseModel):
    DatabaseId: Optional[str] = None
    Message: Optional[str] = None
    Code: Optional[str] = None

class CancelReplicationTaskAssessmentRunMessageRequestTypeDef(BaseModel):
    ReplicationTaskAssessmentRunArn: str

class CertificateTypeDef(BaseModel):
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

class CollectorHealthCheckTypeDef(BaseModel):
    CollectorStatus: Optional[CollectorStatusType] = None
    LocalCollectorS3Access: Optional[bool] = None
    WebCollectorS3Access: Optional[bool] = None
    WebCollectorGrantedRoleBasedAccess: Optional[bool] = None

class InventoryDataTypeDef(BaseModel):
    NumberOfDatabases: Optional[int] = None
    NumberOfSchemas: Optional[int] = None

class CollectorShortInfoResponseTypeDef(BaseModel):
    CollectorReferencedId: Optional[str] = None
    CollectorName: Optional[str] = None

class ComputeConfigOutputTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    DnsNameServers: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MaxCapacityUnits: Optional[int] = None
    MinCapacityUnits: Optional[int] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSubnetGroupId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None

class ComputeConfigTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    DnsNameServers: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MaxCapacityUnits: Optional[int] = None
    MinCapacityUnits: Optional[int] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSubnetGroupId: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class ConnectionTypeDef(BaseModel):
    ReplicationInstanceArn: Optional[str] = None
    EndpointArn: Optional[str] = None
    Status: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    EndpointIdentifier: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None

class DmsTransferSettingsTypeDef(BaseModel):
    ServiceAccessRoleArn: Optional[str] = None
    BucketName: Optional[str] = None

class DocDbSettingsTypeDef(BaseModel):
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

class DynamoDbSettingsTypeDef(BaseModel):
    ServiceAccessRoleArn: str

class ElasticsearchSettingsTypeDef(BaseModel):
    ServiceAccessRoleArn: str
    EndpointUri: str
    FullLoadErrorPercentage: Optional[int] = None
    ErrorRetryDuration: Optional[int] = None
    UseNewMappingType: Optional[bool] = None

class GcpMySQLSettingsTypeDef(BaseModel):
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

class IBMDb2SettingsTypeDef(BaseModel):
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

class KafkaSettingsTypeDef(BaseModel):
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
    SslEndpointIdentificationAlgorithm: Optional[       KafkaSslEndpointIdentificationAlgorithmType     ] = None

class KinesisSettingsTypeDef(BaseModel):
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

class MicrosoftSQLServerSettingsTypeDef(BaseModel):
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

class MongoDbSettingsTypeDef(BaseModel):
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

class MySQLSettingsTypeDef(BaseModel):
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

class NeptuneSettingsTypeDef(BaseModel):
    S3BucketName: str
    S3BucketFolder: str
    ServiceAccessRoleArn: Optional[str] = None
    ErrorRetryDuration: Optional[int] = None
    MaxFileSize: Optional[int] = None
    MaxRetryCount: Optional[int] = None
    IamAuthEnabled: Optional[bool] = None

class OracleSettingsTypeDef(BaseModel):
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

class PostgreSQLSettingsTypeDef(BaseModel):
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

class RedisSettingsTypeDef(BaseModel):
    ServerName: str
    Port: int
    SslSecurityProtocol: Optional[SslSecurityProtocolValueType] = None
    AuthType: Optional[RedisAuthTypeValueType] = None
    AuthUserName: Optional[str] = None
    AuthPassword: Optional[str] = None
    SslCaCertificateArn: Optional[str] = None

class RedshiftSettingsTypeDef(BaseModel):
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

class S3SettingsTypeDef(BaseModel):
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

class SybaseSettingsTypeDef(BaseModel):
    DatabaseName: Optional[str] = None
    Password: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    Username: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    SecretsManagerSecretId: Optional[str] = None

class TimestreamSettingsTypeDef(BaseModel):
    DatabaseName: str
    MemoryDuration: int
    MagneticDuration: int
    CdcInsertsAndUpdates: Optional[bool] = None
    EnableMagneticStoreWrites: Optional[bool] = None

class EventSubscriptionTypeDef(BaseModel):
    CustomerAwsId: Optional[str] = None
    CustSubscriptionId: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    EventCategoriesList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class CreateFleetAdvisorCollectorRequestRequestTypeDef(BaseModel):
    CollectorName: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    Description: Optional[str] = None

class InstanceProfileTypeDef(BaseModel):
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

class DataProviderDescriptorDefinitionTypeDef(BaseModel):
    DataProviderIdentifier: str
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None

class SCApplicationAttributesTypeDef(BaseModel):
    S3BucketPath: Optional[str] = None
    S3BucketRoleArn: Optional[str] = None

class DataProviderDescriptorTypeDef(BaseModel):
    SecretsManagerSecretId: Optional[str] = None
    SecretsManagerAccessRoleArn: Optional[str] = None
    DataProviderName: Optional[str] = None
    DataProviderArn: Optional[str] = None

class DocDbDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None

class MariaDbDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None

class MicrosoftSqlServerDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None

class MongoDbDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None
    AuthType: Optional[AuthTypeValueType] = None
    AuthSource: Optional[str] = None
    AuthMechanism: Optional[AuthMechanismValueType] = None

class MySqlDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None

class OracleDataProviderSettingsTypeDef(BaseModel):
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

class PostgreSqlDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None
    SslMode: Optional[DmsSslModeValueType] = None
    CertificateArn: Optional[str] = None

class RedshiftDataProviderSettingsTypeDef(BaseModel):
    ServerName: Optional[str] = None
    Port: Optional[int] = None
    DatabaseName: Optional[str] = None

class DatabaseInstanceSoftwareDetailsResponseTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineEdition: Optional[str] = None
    ServicePack: Optional[str] = None
    SupportLevel: Optional[str] = None
    OsArchitecture: Optional[int] = None
    Tooltip: Optional[str] = None

class ServerShortInfoResponseTypeDef(BaseModel):
    ServerId: Optional[str] = None
    IpAddress: Optional[str] = None
    ServerName: Optional[str] = None

class DatabaseShortInfoResponseTypeDef(BaseModel):
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseIpAddress: Optional[str] = None
    DatabaseEngine: Optional[str] = None

class DefaultErrorDetailsTypeDef(BaseModel):
    Message: Optional[str] = None

class DeleteCertificateMessageRequestTypeDef(BaseModel):
    CertificateArn: str

class DeleteCollectorRequestRequestTypeDef(BaseModel):
    CollectorReferencedId: str

class DeleteConnectionMessageRequestTypeDef(BaseModel):
    EndpointArn: str
    ReplicationInstanceArn: str

class DeleteDataProviderMessageRequestTypeDef(BaseModel):
    DataProviderIdentifier: str

class DeleteEndpointMessageRequestTypeDef(BaseModel):
    EndpointArn: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str

class DeleteFleetAdvisorDatabasesRequestRequestTypeDef(BaseModel):
    DatabaseIds: Sequence[str]

class DeleteInstanceProfileMessageRequestTypeDef(BaseModel):
    InstanceProfileIdentifier: str

class DeleteMigrationProjectMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str

class DeleteReplicationConfigMessageRequestTypeDef(BaseModel):
    ReplicationConfigArn: str

class DeleteReplicationInstanceMessageRequestTypeDef(BaseModel):
    ReplicationInstanceArn: str

class DeleteReplicationSubnetGroupMessageRequestTypeDef(BaseModel):
    ReplicationSubnetGroupIdentifier: str

class DeleteReplicationTaskAssessmentRunMessageRequestTypeDef(BaseModel):
    ReplicationTaskAssessmentRunArn: str

class DeleteReplicationTaskMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str

class DescribeApplicableIndividualAssessmentsMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    SourceEngineName: Optional[str] = None
    TargetEngineName: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeConversionConfigurationMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str

class DescribeEndpointSettingsMessageRequestTypeDef(BaseModel):
    EngineName: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class EndpointSettingTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[EndpointSettingTypeValueType] = None
    EnumValues: Optional[List[str]] = None
    Sensitive: Optional[bool] = None
    Units: Optional[str] = None
    Applicability: Optional[str] = None
    IntValueMin: Optional[int] = None
    IntValueMax: Optional[int] = None
    DefaultValue: Optional[str] = None

class SupportedEndpointTypeTypeDef(BaseModel):
    EngineName: Optional[str] = None
    SupportsCDC: Optional[bool] = None
    EndpointType: Optional[ReplicationEndpointTypeValueType] = None
    ReplicationInstanceEngineMinimumVersion: Optional[str] = None
    EngineDisplayName: Optional[str] = None

class DescribeEngineVersionsMessageRequestTypeDef(BaseModel):
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class EngineVersionTypeDef(BaseModel):
    Version: Optional[str] = None
    Lifecycle: Optional[str] = None
    ReleaseStatus: Optional[ReleaseStatusValuesType] = None
    LaunchDate: Optional[datetime] = None
    AutoUpgradeDate: Optional[datetime] = None
    DeprecationDate: Optional[datetime] = None
    ForceUpgradeDate: Optional[datetime] = None
    AvailableUpgrades: Optional[List[str]] = None

class EventCategoryGroupTypeDef(BaseModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None

class EventTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal["replication-instance"]] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None

class DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef(BaseModel):
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class FleetAdvisorLsaAnalysisResponseTypeDef(BaseModel):
    LsaAnalysisId: Optional[str] = None
    Status: Optional[str] = None

class FleetAdvisorSchemaObjectResponseTypeDef(BaseModel):
    SchemaId: Optional[str] = None
    ObjectType: Optional[str] = None
    NumberOfObjects: Optional[int] = None
    CodeLineCount: Optional[int] = None
    CodeSize: Optional[int] = None

class DescribeOrderableReplicationInstancesMessageRequestTypeDef(BaseModel):
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class OrderableReplicationInstanceTypeDef(BaseModel):
    EngineVersion: Optional[str] = None
    ReplicationInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    MinAllocatedStorage: Optional[int] = None
    MaxAllocatedStorage: Optional[int] = None
    DefaultAllocatedStorage: Optional[int] = None
    IncludedAllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    ReleaseStatus: Optional[ReleaseStatusValuesType] = None

class LimitationTypeDef(BaseModel):
    DatabaseId: Optional[str] = None
    EngineName: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Impact: Optional[str] = None
    Type: Optional[str] = None

class DescribeRefreshSchemasStatusMessageRequestTypeDef(BaseModel):
    EndpointArn: str

class RefreshSchemasStatusTypeDef(BaseModel):
    EndpointArn: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    Status: Optional[RefreshSchemasStatusTypeValueType] = None
    LastRefreshDate: Optional[datetime] = None
    LastFailureMessage: Optional[str] = None

class DescribeReplicationInstanceTaskLogsMessageRequestTypeDef(BaseModel):
    ReplicationInstanceArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class ReplicationInstanceTaskLogTypeDef(BaseModel):
    ReplicationTaskName: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationInstanceTaskLogSize: Optional[int] = None

class TableStatisticsTypeDef(BaseModel):
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

class DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class ReplicationTaskAssessmentResultTypeDef(BaseModel):
    ReplicationTaskIdentifier: Optional[str] = None
    ReplicationTaskArn: Optional[str] = None
    ReplicationTaskLastAssessmentDate: Optional[datetime] = None
    AssessmentStatus: Optional[str] = None
    AssessmentResultsFile: Optional[str] = None
    AssessmentResults: Optional[str] = None
    S3ObjectUrl: Optional[str] = None

class ReplicationTaskIndividualAssessmentTypeDef(BaseModel):
    ReplicationTaskIndividualAssessmentArn: Optional[str] = None
    ReplicationTaskAssessmentRunArn: Optional[str] = None
    IndividualAssessmentName: Optional[str] = None
    Status: Optional[str] = None
    ReplicationTaskIndividualAssessmentStartDate: Optional[datetime] = None

class DescribeSchemasMessageRequestTypeDef(BaseModel):
    EndpointArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class OracleSettingsOutputTypeDef(BaseModel):
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

class ExportMetadataModelAssessmentMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    FileName: Optional[str] = None
    AssessmentReportTypes: Optional[Sequence[AssessmentReportTypeType]] = None

class ExportMetadataModelAssessmentResultEntryTypeDef(BaseModel):
    S3ObjectKey: Optional[str] = None
    ObjectURL: Optional[str] = None

class ExportSqlDetailsTypeDef(BaseModel):
    S3ObjectKey: Optional[str] = None
    ObjectURL: Optional[str] = None

class ListTagsForResourceMessageRequestTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceArnList: Optional[Sequence[str]] = None

class ModifyConversionConfigurationMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str

class ModifyEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ModifyInstanceProfileMessageRequestTypeDef(BaseModel):
    InstanceProfileIdentifier: str
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[str]] = None

class ModifyReplicationInstanceMessageRequestTypeDef(BaseModel):
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

class ModifyReplicationSubnetGroupMessageRequestTypeDef(BaseModel):
    ReplicationSubnetGroupIdentifier: str
    SubnetIds: Sequence[str]
    ReplicationSubnetGroupDescription: Optional[str] = None

class MoveReplicationTaskMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str
    TargetReplicationInstanceArn: str

class OracleSettingsExtraOutputTypeDef(BaseModel):
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

class PendingMaintenanceActionTypeDef(BaseModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None

class ProvisionDataTypeDef(BaseModel):
    ProvisionState: Optional[str] = None
    ProvisionedCapacityUnits: Optional[int] = None
    DateProvisioned: Optional[datetime] = None
    IsNewProvisioningAvailable: Optional[bool] = None
    DateNewProvisioningDataAvailable: Optional[datetime] = None
    ReasonForNewProvisioningData: Optional[str] = None

class RdsConfigurationTypeDef(BaseModel):
    EngineEdition: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceVcpu: Optional[float] = None
    InstanceMemory: Optional[float] = None
    StorageType: Optional[str] = None
    StorageSize: Optional[int] = None
    StorageIops: Optional[int] = None
    DeploymentOption: Optional[str] = None
    EngineVersion: Optional[str] = None

class RdsRequirementsTypeDef(BaseModel):
    EngineEdition: Optional[str] = None
    InstanceVcpu: Optional[float] = None
    InstanceMemory: Optional[float] = None
    StorageSize: Optional[int] = None
    StorageIops: Optional[int] = None
    DeploymentOption: Optional[str] = None
    EngineVersion: Optional[str] = None

class RebootReplicationInstanceMessageRequestTypeDef(BaseModel):
    ReplicationInstanceArn: str
    ForceFailover: Optional[bool] = None
    ForcePlannedFailover: Optional[bool] = None

class RecommendationSettingsTypeDef(BaseModel):
    InstanceSizingType: str
    WorkloadType: str

class RefreshSchemasMessageRequestTypeDef(BaseModel):
    EndpointArn: str
    ReplicationInstanceArn: str

class TableToReloadTypeDef(BaseModel):
    SchemaName: str
    TableName: str

class RemoveTagsFromResourceMessageRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ReplicationPendingModifiedValuesTypeDef(BaseModel):
    ReplicationInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    NetworkType: Optional[str] = None

class VpcSecurityGroupMembershipTypeDef(BaseModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class ReplicationStatsTypeDef(BaseModel):
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

class ReplicationTaskAssessmentRunProgressTypeDef(BaseModel):
    IndividualAssessmentCount: Optional[int] = None
    IndividualAssessmentCompletedCount: Optional[int] = None

class ReplicationTaskStatsTypeDef(BaseModel):
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

class SchemaShortInfoResponseTypeDef(BaseModel):
    SchemaId: Optional[str] = None
    SchemaName: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseIpAddress: Optional[str] = None

class StartExtensionPackAssociationMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str

class StartMetadataModelAssessmentMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    SelectionRules: str

class StartMetadataModelConversionMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    SelectionRules: str

class StartMetadataModelExportAsScriptMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    FileName: Optional[str] = None

class StartMetadataModelExportToTargetMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    OverwriteExtensionPack: Optional[bool] = None

class StartMetadataModelImportMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    Refresh: Optional[bool] = None

class StartReplicationTaskAssessmentMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str

class StartReplicationTaskAssessmentRunMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str
    ServiceAccessRoleArn: str
    ResultLocationBucket: str
    AssessmentRunName: str
    ResultLocationFolder: Optional[str] = None
    ResultEncryptionMode: Optional[str] = None
    ResultKmsKeyArn: Optional[str] = None
    IncludeOnly: Optional[Sequence[str]] = None
    Exclude: Optional[Sequence[str]] = None

class StopReplicationMessageRequestTypeDef(BaseModel):
    ReplicationConfigArn: str

class StopReplicationTaskMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str

class TestConnectionMessageRequestTypeDef(BaseModel):
    ReplicationInstanceArn: str
    EndpointArn: str

class UpdateSubscriptionsToEventBridgeMessageRequestTypeDef(BaseModel):
    ForceMove: Optional[bool] = None

class AddTagsToResourceMessageRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateInstanceProfileMessageRequestTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NetworkType: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Description: Optional[str] = None
    SubnetGroupIdentifier: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[str]] = None

class CreateReplicationInstanceMessageRequestTypeDef(BaseModel):
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

class CreateReplicationSubnetGroupMessageRequestTypeDef(BaseModel):
    ReplicationSubnetGroupIdentifier: str
    ReplicationSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateFleetAdvisorCollectorResponseTypeDef(BaseModel):
    CollectorReferencedId: str
    CollectorName: str
    Description: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFleetAdvisorDatabasesResponseTypeDef(BaseModel):
    DatabaseIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResponseTypeDef(BaseModel):
    AccountQuotas: List[AccountQuotaTypeDef]
    UniqueAccountIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicableIndividualAssessmentsResponseTypeDef(BaseModel):
    IndividualAssessmentNames: List[str]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConversionConfigurationResponseTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSchemasResponseTypeDef(BaseModel):
    Marker: str
    Schemas: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyConversionConfigurationResponseTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReloadReplicationTablesResponseTypeDef(BaseModel):
    ReplicationConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReloadTablesResponseTypeDef(BaseModel):
    ReplicationTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RunFleetAdvisorLsaAnalysisResponseTypeDef(BaseModel):
    LsaAnalysisId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExtensionPackAssociationResponseTypeDef(BaseModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelAssessmentResponseTypeDef(BaseModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelConversionResponseTypeDef(BaseModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelExportAsScriptResponseTypeDef(BaseModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelExportToTargetResponseTypeDef(BaseModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelImportResponseTypeDef(BaseModel):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubscriptionsToEventBridgeResponseTypeDef(BaseModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class BatchStartRecommendationsResponseTypeDef(BaseModel):
    ErrorEntries: List[BatchStartRecommendationsErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateMessageRequestTypeDef(BaseModel):
    CertificateIdentifier: str
    CertificatePem: Optional[str] = None
    CertificateWallet: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DeleteCertificateResponseTypeDef(BaseModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificatesResponseTypeDef(BaseModel):
    Marker: str
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateResponseTypeDef(BaseModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CollectorResponseTypeDef(BaseModel):
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

class ReplicationConfigTypeDef(BaseModel):
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

class CreateReplicationConfigMessageRequestTypeDef(BaseModel):
    ReplicationConfigIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ComputeConfig: ComputeConfigTypeDef
    ReplicationType: MigrationTypeValueType
    TableMappings: str
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ModifyReplicationConfigMessageRequestTypeDef(BaseModel):
    ReplicationConfigArn: str
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationSettings: Optional[str] = None
    SupplementalSettings: Optional[str] = None
    ComputeConfig: Optional[ComputeConfigTypeDef] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None

class DeleteConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectionsResponseTypeDef(BaseModel):
    Marker: str
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TestConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointMessageRequestTypeDef(BaseModel):
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
    OracleSettings: Optional[OracleSettingsTypeDef] = None
    SybaseSettings: Optional[SybaseSettingsTypeDef] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettingsTypeDef] = None
    IBMDb2Settings: Optional[IBMDb2SettingsTypeDef] = None
    ResourceIdentifier: Optional[str] = None
    DocDbSettings: Optional[DocDbSettingsTypeDef] = None
    RedisSettings: Optional[RedisSettingsTypeDef] = None
    GcpMySQLSettings: Optional[GcpMySQLSettingsTypeDef] = None
    TimestreamSettings: Optional[TimestreamSettingsTypeDef] = None

class ModifyEndpointMessageRequestTypeDef(BaseModel):
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
    OracleSettings: Optional[OracleSettingsTypeDef] = None
    SybaseSettings: Optional[SybaseSettingsTypeDef] = None
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettingsTypeDef] = None
    IBMDb2Settings: Optional[IBMDb2SettingsTypeDef] = None
    DocDbSettings: Optional[DocDbSettingsTypeDef] = None
    RedisSettings: Optional[RedisSettingsTypeDef] = None
    ExactSettings: Optional[bool] = None
    GcpMySQLSettings: Optional[GcpMySQLSettingsTypeDef] = None
    TimestreamSettings: Optional[TimestreamSettingsTypeDef] = None

class CreateEventSubscriptionResponseTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventSubscriptionResponseTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventSubscriptionsResponseTypeDef(BaseModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResponseTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResponseTypeDef(BaseModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInstanceProfileResponseTypeDef(BaseModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceProfilesResponseTypeDef(BaseModel):
    Marker: str
    InstanceProfiles: List[InstanceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceProfileResponseTypeDef(BaseModel):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMigrationProjectMessageRequestTypeDef(BaseModel):
    SourceDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef]
    TargetDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef]
    InstanceProfileIdentifier: str
    MigrationProjectName: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributesTypeDef] = None

class ModifyMigrationProjectMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    MigrationProjectName: Optional[str] = None
    SourceDataProviderDescriptors: Optional[       Sequence[DataProviderDescriptorDefinitionTypeDef]     ] = None
    TargetDataProviderDescriptors: Optional[       Sequence[DataProviderDescriptorDefinitionTypeDef]     ] = None
    InstanceProfileIdentifier: Optional[str] = None
    TransformationRules: Optional[str] = None
    Description: Optional[str] = None
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributesTypeDef] = None

class CreateReplicationTaskMessageRequestTypeDef(BaseModel):
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

class ModifyReplicationTaskMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str
    ReplicationTaskIdentifier: Optional[str] = None
    MigrationType: Optional[MigrationTypeValueType] = None
    TableMappings: Optional[str] = None
    ReplicationTaskSettings: Optional[str] = None
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    TaskData: Optional[str] = None

class StartReplicationMessageRequestTypeDef(BaseModel):
    ReplicationConfigArn: str
    StartReplicationType: str
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None

class StartReplicationTaskMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str
    StartReplicationTaskType: StartReplicationTaskTypeValueType
    CdcStartTime: Optional[TimestampTypeDef] = None
    CdcStartPosition: Optional[str] = None
    CdcStopPosition: Optional[str] = None

class MigrationProjectTypeDef(BaseModel):
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

class DataProviderSettingsTypeDef(BaseModel):
    RedshiftSettings: Optional[RedshiftDataProviderSettingsTypeDef] = None
    PostgreSqlSettings: Optional[PostgreSqlDataProviderSettingsTypeDef] = None
    MySqlSettings: Optional[MySqlDataProviderSettingsTypeDef] = None
    OracleSettings: Optional[OracleDataProviderSettingsTypeDef] = None
    MicrosoftSqlServerSettings: Optional[MicrosoftSqlServerDataProviderSettingsTypeDef] = None
    DocDbSettings: Optional[DocDbDataProviderSettingsTypeDef] = None
    MariaDbSettings: Optional[MariaDbDataProviderSettingsTypeDef] = None
    MongoDbSettings: Optional[MongoDbDataProviderSettingsTypeDef] = None

class DatabaseResponseTypeDef(BaseModel):
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    IpAddress: Optional[str] = None
    NumberOfSchemas: Optional[int] = None
    Server: Optional[ServerShortInfoResponseTypeDef] = None
    SoftwareDetails: Optional[DatabaseInstanceSoftwareDetailsResponseTypeDef] = None
    Collectors: Optional[List[CollectorShortInfoResponseTypeDef]] = None

class ErrorDetailsTypeDef(BaseModel):
    defaultErrorDetails: Optional[DefaultErrorDetailsTypeDef] = None

class DescribeCertificatesMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeConnectionsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataProvidersMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEndpointTypesMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEndpointsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventCategoriesMessageRequestTypeDef(BaseModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeEventSubscriptionsMessageRequestTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventsMessageRequestTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal["replication-instance"]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeExtensionPackAssociationsMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeFleetAdvisorCollectorsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetAdvisorDatabasesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFleetAdvisorSchemasRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceProfilesMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeMetadataModelAssessmentsMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeMetadataModelConversionsMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeMetadataModelExportsAsScriptMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeMetadataModelExportsToTargetMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeMetadataModelImportsMessageRequestTypeDef(BaseModel):
    MigrationProjectIdentifier: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeMigrationProjectsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePendingMaintenanceActionsMessageRequestTypeDef(BaseModel):
    ReplicationInstanceArn: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeRecommendationLimitationsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeRecommendationsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReplicationConfigsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReplicationInstancesMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReplicationSubnetGroupsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReplicationTableStatisticsMessageRequestTypeDef(BaseModel):
    ReplicationConfigArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReplicationTasksMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None

class DescribeReplicationsMessageRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeTableStatisticsMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConnectionsMessageDescribeConnectionsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointTypesMessageDescribeEndpointTypesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointsMessageDescribeEndpointsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[Literal["replication-instance"]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableReplicationInstancesMessageDescribeOrderableReplicationInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationInstancesMessageDescribeReplicationInstancesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationSubnetGroupsMessageDescribeReplicationSubnetGroupsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationTaskAssessmentResultsMessageDescribeReplicationTaskAssessmentResultsPaginateTypeDef(BaseModel):
    ReplicationTaskArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationTasksMessageDescribeReplicationTasksPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WithoutSettings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSchemasMessageDescribeSchemasPaginateTypeDef(BaseModel):
    EndpointArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTableStatisticsMessageDescribeTableStatisticsPaginateTypeDef(BaseModel):
    ReplicationTaskArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConnectionsMessageTestConnectionSucceedsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndpointsMessageEndpointDeletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationInstancesMessageReplicationInstanceAvailableWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationInstancesMessageReplicationInstanceDeletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationTasksMessageReplicationTaskDeletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationTasksMessageReplicationTaskReadyWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationTasksMessageReplicationTaskRunningWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationTasksMessageReplicationTaskStoppedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WithoutSettings: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEndpointSettingsResponseTypeDef(BaseModel):
    Marker: str
    EndpointSettings: List[EndpointSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointTypesResponseTypeDef(BaseModel):
    Marker: str
    SupportedEndpointTypes: List[SupportedEndpointTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineVersionsResponseTypeDef(BaseModel):
    EngineVersions: List[EngineVersionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventCategoriesResponseTypeDef(BaseModel):
    EventCategoryGroupList: List[EventCategoryGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsResponseTypeDef(BaseModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAdvisorLsaAnalysisResponseTypeDef(BaseModel):
    Analysis: List[FleetAdvisorLsaAnalysisResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef(BaseModel):
    FleetAdvisorSchemaObjects: List[FleetAdvisorSchemaObjectResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrderableReplicationInstancesResponseTypeDef(BaseModel):
    OrderableReplicationInstances: List[OrderableReplicationInstanceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecommendationLimitationsResponseTypeDef(BaseModel):
    Limitations: List[LimitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRefreshSchemasStatusResponseTypeDef(BaseModel):
    RefreshSchemasStatus: RefreshSchemasStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshSchemasResponseTypeDef(BaseModel):
    RefreshSchemasStatus: RefreshSchemasStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationInstanceTaskLogsResponseTypeDef(BaseModel):
    ReplicationInstanceArn: str
    ReplicationInstanceTaskLogs: List[ReplicationInstanceTaskLogTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTableStatisticsResponseTypeDef(BaseModel):
    ReplicationConfigArn: str
    Marker: str
    ReplicationTableStatistics: List[TableStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableStatisticsResponseTypeDef(BaseModel):
    ReplicationTaskArn: str
    TableStatistics: List[TableStatisticsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTaskAssessmentResultsResponseTypeDef(BaseModel):
    Marker: str
    BucketName: str
    ReplicationTaskAssessmentResults: List[ReplicationTaskAssessmentResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTaskIndividualAssessmentsResponseTypeDef(BaseModel):
    Marker: str
    ReplicationTaskIndividualAssessments: List[ReplicationTaskIndividualAssessmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointTypeDef(BaseModel):
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

class ExportMetadataModelAssessmentResponseTypeDef(BaseModel):
    PdfReport: ExportMetadataModelAssessmentResultEntryTypeDef
    CsvReport: ExportMetadataModelAssessmentResultEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourcePendingMaintenanceActionsTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None

class RdsRecommendationTypeDef(BaseModel):
    RequirementsToTarget: Optional[RdsRequirementsTypeDef] = None
    TargetConfiguration: Optional[RdsConfigurationTypeDef] = None

class StartRecommendationsRequestEntryTypeDef(BaseModel):
    DatabaseId: str
    Settings: RecommendationSettingsTypeDef

class StartRecommendationsRequestRequestTypeDef(BaseModel):
    DatabaseId: str
    Settings: RecommendationSettingsTypeDef

class ReloadReplicationTablesMessageRequestTypeDef(BaseModel):
    ReplicationConfigArn: str
    TablesToReload: Sequence[TableToReloadTypeDef]
    ReloadOption: Optional[ReloadOptionValueType] = None

class ReloadTablesMessageRequestTypeDef(BaseModel):
    ReplicationTaskArn: str
    TablesToReload: Sequence[TableToReloadTypeDef]
    ReloadOption: Optional[ReloadOptionValueType] = None

class ReplicationTypeDef(BaseModel):
    ReplicationConfigIdentifier: Optional[str] = None
    ReplicationConfigArn: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    ReplicationType: Optional[MigrationTypeValueType] = None
    Status: Optional[str] = None
    ProvisionData: Optional[ProvisionDataTypeDef] = None
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

class ReplicationTaskAssessmentRunTypeDef(BaseModel):
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

class ReplicationTaskTypeDef(BaseModel):
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

class SchemaResponseTypeDef(BaseModel):
    CodeLineCount: Optional[int] = None
    CodeSize: Optional[int] = None
    Complexity: Optional[str] = None
    Server: Optional[ServerShortInfoResponseTypeDef] = None
    DatabaseInstance: Optional[DatabaseShortInfoResponseTypeDef] = None
    SchemaId: Optional[str] = None
    SchemaName: Optional[str] = None
    OriginalSchema: Optional[SchemaShortInfoResponseTypeDef] = None
    Similarity: Optional[float] = None

class ReplicationSubnetGroupTypeDef(BaseModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None
    ReplicationSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    SupportedNetworkTypes: Optional[List[str]] = None

class DescribeFleetAdvisorCollectorsResponseTypeDef(BaseModel):
    Collectors: List[CollectorResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateReplicationConfigResponseTypeDef(BaseModel):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationConfigResponseTypeDef(BaseModel):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationConfigsResponseTypeDef(BaseModel):
    Marker: str
    ReplicationConfigs: List[ReplicationConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationConfigResponseTypeDef(BaseModel):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMigrationProjectResponseTypeDef(BaseModel):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMigrationProjectResponseTypeDef(BaseModel):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMigrationProjectsResponseTypeDef(BaseModel):
    Marker: str
    MigrationProjects: List[MigrationProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyMigrationProjectResponseTypeDef(BaseModel):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataProviderMessageRequestTypeDef(BaseModel):
    Engine: str
    Settings: DataProviderSettingsTypeDef
    DataProviderName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DataProviderTypeDef(BaseModel):
    DataProviderName: Optional[str] = None
    DataProviderArn: Optional[str] = None
    DataProviderCreationTime: Optional[datetime] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    Settings: Optional[DataProviderSettingsTypeDef] = None

class ModifyDataProviderMessageRequestTypeDef(BaseModel):
    DataProviderIdentifier: str
    DataProviderName: Optional[str] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    ExactSettings: Optional[bool] = None
    Settings: Optional[DataProviderSettingsTypeDef] = None

class DescribeFleetAdvisorDatabasesResponseTypeDef(BaseModel):
    Databases: List[DatabaseResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SchemaConversionRequestTypeDef(BaseModel):
    Status: Optional[str] = None
    RequestIdentifier: Optional[str] = None
    MigrationProjectArn: Optional[str] = None
    Error: Optional[ErrorDetailsTypeDef] = None
    ExportSqlDetails: Optional[ExportSqlDetailsTypeDef] = None

class CreateEndpointResponseTypeDef(BaseModel):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEndpointResponseTypeDef(BaseModel):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointsResponseTypeDef(BaseModel):
    Marker: str
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEndpointResponseTypeDef(BaseModel):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplyPendingMaintenanceActionResponseTypeDef(BaseModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePendingMaintenanceActionsResponseTypeDef(BaseModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationDataTypeDef(BaseModel):
    RdsEngine: Optional[RdsRecommendationTypeDef] = None

class BatchStartRecommendationsRequestRequestTypeDef(BaseModel):
    Data: Optional[Sequence[StartRecommendationsRequestEntryTypeDef]] = None

class DescribeReplicationsResponseTypeDef(BaseModel):
    Marker: str
    Replications: List[ReplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationResponseTypeDef(BaseModel):
    Replication: ReplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationResponseTypeDef(BaseModel):
    Replication: ReplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelReplicationTaskAssessmentRunResponseTypeDef(BaseModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationTaskAssessmentRunResponseTypeDef(BaseModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTaskAssessmentRunsResponseTypeDef(BaseModel):
    Marker: str
    ReplicationTaskAssessmentRuns: List[ReplicationTaskAssessmentRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationTaskAssessmentRunResponseTypeDef(BaseModel):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationTaskResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationTaskResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTasksResponseTypeDef(BaseModel):
    Marker: str
    ReplicationTasks: List[ReplicationTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationTaskResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MoveReplicationTaskResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationTaskAssessmentResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationTaskResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationTaskResponseTypeDef(BaseModel):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAdvisorSchemasResponseTypeDef(BaseModel):
    FleetAdvisorSchemas: List[SchemaResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateReplicationSubnetGroupResponseTypeDef(BaseModel):
    ReplicationSubnetGroup: ReplicationSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationSubnetGroupsResponseTypeDef(BaseModel):
    Marker: str
    ReplicationSubnetGroups: List[ReplicationSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationSubnetGroupResponseTypeDef(BaseModel):
    ReplicationSubnetGroup: ReplicationSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationInstanceTypeDef(BaseModel):
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

class CreateDataProviderResponseTypeDef(BaseModel):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataProviderResponseTypeDef(BaseModel):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataProvidersResponseTypeDef(BaseModel):
    Marker: str
    DataProviders: List[DataProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDataProviderResponseTypeDef(BaseModel):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExtensionPackAssociationsResponseTypeDef(BaseModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelAssessmentsResponseTypeDef(BaseModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelConversionsResponseTypeDef(BaseModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelExportsAsScriptResponseTypeDef(BaseModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelExportsToTargetResponseTypeDef(BaseModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelImportsResponseTypeDef(BaseModel):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTypeDef(BaseModel):
    DatabaseId: Optional[str] = None
    EngineName: Optional[str] = None
    CreatedDate: Optional[str] = None
    Status: Optional[str] = None
    Preferred: Optional[bool] = None
    Settings: Optional[RecommendationSettingsTypeDef] = None
    Data: Optional[RecommendationDataTypeDef] = None

class CreateReplicationInstanceResponseTypeDef(BaseModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationInstanceResponseTypeDef(BaseModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationInstancesResponseTypeDef(BaseModel):
    Marker: str
    ReplicationInstances: List[ReplicationInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationInstanceResponseTypeDef(BaseModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootReplicationInstanceResponseTypeDef(BaseModel):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecommendationsResponseTypeDef(BaseModel):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

