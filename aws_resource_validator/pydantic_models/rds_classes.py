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
from aws_resource_validator.pydantic_models.rds_constants import *

class AccountQuotaTypeDef(BaseModel):
    AccountQuotaName: Optional[str] = None
    Used: Optional[int] = None
    Max: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddRoleToDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class AddRoleToDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    RoleArn: str
    FeatureName: str

class AddSourceIdentifierToSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SourceIdentifier: str

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
    EventSubscriptionArn: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ApplyPendingMaintenanceActionMessageRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str

class AuthorizeDBSecurityGroupIngressMessageRequestTypeDef(BaseModel):
    DBSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class AvailableProcessorFeatureTypeDef(BaseModel):
    Name: Optional[str] = None
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[str] = None

class BlueGreenDeploymentTaskTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None

class SwitchoverDetailTypeDef(BaseModel):
    SourceMember: Optional[str] = None
    TargetMember: Optional[str] = None
    Status: Optional[str] = None

class CancelExportTaskMessageRequestTypeDef(BaseModel):
    ExportTaskIdentifier: str

class CertificateDetailsTypeDef(BaseModel):
    CAIdentifier: Optional[str] = None
    ValidTill: Optional[datetime] = None

class CertificateTypeDef(BaseModel):
    CertificateIdentifier: Optional[str] = None
    CertificateType: Optional[str] = None
    Thumbprint: Optional[str] = None
    ValidFrom: Optional[datetime] = None
    ValidTill: Optional[datetime] = None
    CertificateArn: Optional[str] = None
    CustomerOverride: Optional[bool] = None
    CustomerOverrideValidTill: Optional[datetime] = None

class CharacterSetTypeDef(BaseModel):
    CharacterSetName: Optional[str] = None
    CharacterSetDescription: Optional[str] = None

class ClientGenerateDbAuthTokenRequestTypeDef(BaseModel):
    DBHostname: str
    Port: int
    DBUsername: str
    Region: Optional[Optional[str]] = None

class CloudwatchLogsExportConfigurationTypeDef(BaseModel):
    EnableLogTypes: Optional[Sequence[str]] = None
    DisableLogTypes: Optional[Sequence[str]] = None

class PendingCloudwatchLogsExportsTypeDef(BaseModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class RdsCustomClusterConfigurationTypeDef(BaseModel):
    InterconnectSubnetId: Optional[str] = None
    TransitGatewayMulticastDomainId: Optional[str] = None
    ReplicaMode: Optional[ReplicaModeType] = None

class ConnectionPoolConfigurationInfoTypeDef(BaseModel):
    MaxConnectionsPercent: Optional[int] = None
    MaxIdleConnectionsPercent: Optional[int] = None
    ConnectionBorrowTimeout: Optional[int] = None
    SessionPinningFilters: Optional[List[str]] = None
    InitQuery: Optional[str] = None

class ConnectionPoolConfigurationTypeDef(BaseModel):
    MaxConnectionsPercent: Optional[int] = None
    MaxIdleConnectionsPercent: Optional[int] = None
    ConnectionBorrowTimeout: Optional[int] = None
    SessionPinningFilters: Optional[Sequence[str]] = None
    InitQuery: Optional[str] = None

class ContextAttributeTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DBClusterParameterGroupTypeDef(BaseModel):
    DBClusterParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBClusterParameterGroupArn: Optional[str] = None

class DBParameterGroupTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBParameterGroupArn: Optional[str] = None

class ScalingConfigurationTypeDef(BaseModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    AutoPause: Optional[bool] = None
    SecondsUntilAutoPause: Optional[int] = None
    TimeoutAction: Optional[str] = None
    SecondsBeforeTimeout: Optional[int] = None

class ServerlessV2ScalingConfigurationTypeDef(BaseModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class ProcessorFeatureTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class DBProxyEndpointTypeDef(BaseModel):
    DBProxyEndpointName: Optional[str] = None
    DBProxyEndpointArn: Optional[str] = None
    DBProxyName: Optional[str] = None
    Status: Optional[DBProxyEndpointStatusType] = None
    VpcId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    VpcSubnetIds: Optional[List[str]] = None
    Endpoint: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    TargetRole: Optional[DBProxyEndpointTargetRoleType] = None
    IsDefault: Optional[bool] = None

class UserAuthConfigTypeDef(BaseModel):
    Description: Optional[str] = None
    UserName: Optional[str] = None
    AuthScheme: Optional[Literal["SECRETS"]] = None
    SecretArn: Optional[str] = None
    IAMAuth: Optional[IAMAuthModeType] = None
    ClientPasswordAuthType: Optional[ClientPasswordAuthTypeType] = None

class CreateDBShardGroupMessageRequestTypeDef(BaseModel):
    DBShardGroupIdentifier: str
    DBClusterIdentifier: str
    MaxACU: float
    ComputeRedundancy: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None

class CreateGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None

class CustomDBEngineVersionAMITypeDef(BaseModel):
    ImageId: Optional[str] = None
    Status: Optional[str] = None

class RestoreWindowTypeDef(BaseModel):
    EarliestTime: Optional[datetime] = None
    LatestTime: Optional[datetime] = None

class DBClusterBacktrackTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    BacktrackIdentifier: Optional[str] = None
    BacktrackTo: Optional[datetime] = None
    BacktrackedFrom: Optional[datetime] = None
    BacktrackRequestCreationTime: Optional[datetime] = None
    Status: Optional[str] = None

class DBClusterEndpointTypeDef(BaseModel):
    DBClusterEndpointIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointResourceIdentifier: Optional[str] = None
    Endpoint: Optional[str] = None
    Status: Optional[str] = None
    EndpointType: Optional[str] = None
    CustomEndpointType: Optional[str] = None
    StaticMembers: Optional[List[str]] = None
    ExcludedMembers: Optional[List[str]] = None
    DBClusterEndpointArn: Optional[str] = None

class DBClusterMemberTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None

class DBClusterOptionGroupStatusTypeDef(BaseModel):
    DBClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class ParameterOutputTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ApplyMethod: Optional[ApplyMethodType] = None
    SupportedEngineModes: Optional[List[str]] = None

class DBClusterRoleTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None
    FeatureName: Optional[str] = None

class DBClusterSnapshotAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class DBClusterStatusInfoTypeDef(BaseModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class DomainMembershipTypeDef(BaseModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    FQDN: Optional[str] = None
    IAMRoleName: Optional[str] = None
    OU: Optional[str] = None
    AuthSecretArn: Optional[str] = None
    DnsIps: Optional[List[str]] = None

class LimitlessDatabaseTypeDef(BaseModel):
    Status: Optional[LimitlessDatabaseStatusType] = None
    MinRequiredACU: Optional[float] = None

class MasterUserSecretTypeDef(BaseModel):
    SecretArn: Optional[str] = None
    SecretStatus: Optional[str] = None
    KmsKeyId: Optional[str] = None

class ScalingConfigurationInfoTypeDef(BaseModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    AutoPause: Optional[bool] = None
    SecondsUntilAutoPause: Optional[int] = None
    TimeoutAction: Optional[str] = None
    SecondsBeforeTimeout: Optional[int] = None

class ServerlessV2ScalingConfigurationInfoTypeDef(BaseModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class VpcSecurityGroupMembershipTypeDef(BaseModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class TimezoneTypeDef(BaseModel):
    TimezoneName: Optional[str] = None

class UpgradeTargetTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Description: Optional[str] = None
    AutoUpgrade: Optional[bool] = None
    IsMajorVersionUpgrade: Optional[bool] = None
    SupportedEngineModes: Optional[List[str]] = None
    SupportsParallelQuery: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None
    SupportsBabelfish: Optional[bool] = None
    SupportsLimitlessDatabase: Optional[bool] = None
    SupportsLocalWriteForwarding: Optional[bool] = None
    SupportsIntegrations: Optional[bool] = None

class DBInstanceAutomatedBackupsReplicationTypeDef(BaseModel):
    DBInstanceAutomatedBackupsArn: Optional[str] = None

class DBInstanceRoleTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None

class DBInstanceStatusInfoTypeDef(BaseModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class DBParameterGroupStatusTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None

class DBSecurityGroupMembershipTypeDef(BaseModel):
    DBSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class EndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None

class OptionGroupMembershipTypeDef(BaseModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class TargetHealthTypeDef(BaseModel):
    State: Optional[TargetStateType] = None
    Reason: Optional[TargetHealthReasonType] = None
    Description: Optional[str] = None

class UserAuthConfigInfoTypeDef(BaseModel):
    Description: Optional[str] = None
    UserName: Optional[str] = None
    AuthScheme: Optional[Literal["SECRETS"]] = None
    SecretArn: Optional[str] = None
    IAMAuth: Optional[IAMAuthModeType] = None
    ClientPasswordAuthType: Optional[ClientPasswordAuthTypeType] = None

class DocLinkTypeDef(BaseModel):
    Text: Optional[str] = None
    Url: Optional[str] = None

class EC2SecurityGroupTypeDef(BaseModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class IPRangeTypeDef(BaseModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None

class DBShardGroupTypeDef(BaseModel):
    DBShardGroupResourceId: Optional[str] = None
    DBShardGroupIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    MaxACU: Optional[float] = None
    ComputeRedundancy: Optional[int] = None
    Status: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Endpoint: Optional[str] = None

class DBSnapshotAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class DeleteBlueGreenDeploymentRequestRequestTypeDef(BaseModel):
    BlueGreenDeploymentIdentifier: str
    DeleteTarget: Optional[bool] = None

class DeleteCustomDBEngineVersionMessageRequestTypeDef(BaseModel):
    Engine: str
    EngineVersion: str

class DeleteDBClusterAutomatedBackupMessageRequestTypeDef(BaseModel):
    DbClusterResourceId: str

class DeleteDBClusterEndpointMessageRequestTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str

class DeleteDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None
    DeleteAutomatedBackups: Optional[bool] = None

class DeleteDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str

class DeleteDBClusterSnapshotMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str

class DeleteDBInstanceAutomatedBackupMessageRequestTypeDef(BaseModel):
    DbiResourceId: Optional[str] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None

class DeleteDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None
    DeleteAutomatedBackups: Optional[bool] = None

class DeleteDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str

class DeleteDBProxyEndpointRequestRequestTypeDef(BaseModel):
    DBProxyEndpointName: str

class DeleteDBProxyRequestRequestTypeDef(BaseModel):
    DBProxyName: str

class DeleteDBSecurityGroupMessageRequestTypeDef(BaseModel):
    DBSecurityGroupName: str

class DeleteDBShardGroupMessageRequestTypeDef(BaseModel):
    DBShardGroupIdentifier: str

class DeleteDBSnapshotMessageRequestTypeDef(BaseModel):
    DBSnapshotIdentifier: str

class DeleteDBSubnetGroupMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str

class DeleteGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str

class DeleteIntegrationMessageRequestTypeDef(BaseModel):
    IntegrationIdentifier: str

class DeleteOptionGroupMessageRequestTypeDef(BaseModel):
    OptionGroupName: str

class DeleteTenantDatabaseMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None

class DeregisterDBProxyTargetsRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    DBInstanceIdentifiers: Optional[Sequence[str]] = None
    DBClusterIdentifiers: Optional[Sequence[str]] = None

class FilterTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDBClusterSnapshotAttributesMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeDBLogFilesDetailsTypeDef(BaseModel):
    LogFileName: Optional[str] = None
    LastWritten: Optional[int] = None
    Size: Optional[int] = None

class DescribeDBSnapshotAttributesMessageRequestTypeDef(BaseModel):
    DBSnapshotIdentifier: str

class DescribeValidDBInstanceModificationsMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str

class DisableHttpEndpointRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DoubleRangeTypeDef(BaseModel):
    From: Optional[float] = None
    To: Optional[float] = None

class DownloadDBLogFilePortionMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    LogFileName: str
    Marker: Optional[str] = None
    NumberOfLines: Optional[int] = None

class EnableHttpEndpointRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class EventCategoriesMapTypeDef(BaseModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None

class EventTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None
    SourceArn: Optional[str] = None

class ExportTaskTypeDef(BaseModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    ExportOnly: Optional[List[str]] = None
    SnapshotTime: Optional[datetime] = None
    TaskStartTime: Optional[datetime] = None
    TaskEndTime: Optional[datetime] = None
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None
    IamRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Status: Optional[str] = None
    PercentProgress: Optional[int] = None
    TotalExtractedDataInGB: Optional[int] = None
    FailureCause: Optional[str] = None
    WarningMessage: Optional[str] = None
    SourceType: Optional[ExportSourceTypeType] = None

class FailoverDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    TargetDBInstanceIdentifier: Optional[str] = None

class FailoverGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str
    AllowDataLoss: Optional[bool] = None
    Switchover: Optional[bool] = None

class FailoverStateTypeDef(BaseModel):
    Status: Optional[FailoverStatusType] = None
    FromDbClusterArn: Optional[str] = None
    ToDbClusterArn: Optional[str] = None
    IsDataLossAllowed: Optional[bool] = None

class GlobalClusterMemberTypeDef(BaseModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatusType] = None
    SynchronizationStatus: Optional[GlobalClusterMemberSynchronizationStatusType] = None

class IntegrationErrorTypeDef(BaseModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None

class MinimumEngineVersionPerAllowedValueTypeDef(BaseModel):
    AllowedValue: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None

class ModifyActivityStreamRequestRequestTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    AuditPolicyState: Optional[AuditPolicyStateType] = None

class ModifyCertificatesMessageRequestTypeDef(BaseModel):
    CertificateIdentifier: Optional[str] = None
    RemoveCustomerOverride: Optional[bool] = None

class ModifyCurrentDBClusterCapacityMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    Capacity: Optional[int] = None
    SecondsBeforeTimeout: Optional[int] = None
    TimeoutAction: Optional[str] = None

class ModifyCustomDBEngineVersionMessageRequestTypeDef(BaseModel):
    Engine: str
    EngineVersion: str
    Description: Optional[str] = None
    Status: Optional[CustomEngineVersionStatusType] = None

class ModifyDBClusterEndpointMessageRequestTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str
    EndpointType: Optional[str] = None
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None

class ModifyDBClusterSnapshotAttributeMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None

class ModifyDBProxyEndpointRequestRequestTypeDef(BaseModel):
    DBProxyEndpointName: str
    NewDBProxyEndpointName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class RecommendedActionUpdateTypeDef(BaseModel):
    ActionId: str
    Status: str

class ModifyDBShardGroupMessageRequestTypeDef(BaseModel):
    DBShardGroupIdentifier: str
    MaxACU: Optional[float] = None

class ModifyDBSnapshotAttributeMessageRequestTypeDef(BaseModel):
    DBSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None

class ModifyDBSnapshotMessageRequestTypeDef(BaseModel):
    DBSnapshotIdentifier: str
    EngineVersion: Optional[str] = None
    OptionGroupName: Optional[str] = None

class ModifyDBSubnetGroupMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: Optional[str] = None

class ModifyEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ModifyGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None

class ModifyIntegrationMessageRequestTypeDef(BaseModel):
    IntegrationIdentifier: str
    IntegrationName: Optional[str] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None

class ModifyTenantDatabaseMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    MasterUserPassword: Optional[str] = None
    NewTenantDBName: Optional[str] = None

class OptionSettingTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    IsCollection: Optional[bool] = None

class OptionVersionTypeDef(BaseModel):
    Version: Optional[str] = None
    IsDefault: Optional[bool] = None

class OutpostTypeDef(BaseModel):
    Arn: Optional[str] = None

class ParameterExtraOutputTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ApplyMethod: Optional[ApplyMethodType] = None
    SupportedEngineModes: Optional[List[str]] = None

class ParameterTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ApplyMethod: Optional[ApplyMethodType] = None
    SupportedEngineModes: Optional[Sequence[str]] = None

class PendingMaintenanceActionTypeDef(BaseModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None

class PerformanceInsightsMetricDimensionGroupTypeDef(BaseModel):
    Dimensions: Optional[List[str]] = None
    Group: Optional[str] = None
    Limit: Optional[int] = None

class PromoteReadReplicaDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class PromoteReadReplicaMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None

class RangeTypeDef(BaseModel):
    From: Optional[int] = None
    To: Optional[int] = None
    Step: Optional[int] = None

class RebootDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class RebootDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None

class RebootDBShardGroupMessageRequestTypeDef(BaseModel):
    DBShardGroupIdentifier: str

class RecommendedActionParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class RecurringChargeTypeDef(BaseModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class ScalarReferenceDetailsTypeDef(BaseModel):
    Value: Optional[float] = None

class RegisterDBProxyTargetsRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    DBInstanceIdentifiers: Optional[Sequence[str]] = None
    DBClusterIdentifiers: Optional[Sequence[str]] = None

class RemoveFromGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None

class RemoveRoleFromDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class RemoveRoleFromDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    RoleArn: str
    FeatureName: str

class RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SourceIdentifier: str

class RemoveTagsFromResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    TagKeys: Sequence[str]

class RevokeDBSecurityGroupIngressMessageRequestTypeDef(BaseModel):
    DBSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class SourceRegionTypeDef(BaseModel):
    RegionName: Optional[str] = None
    Endpoint: Optional[str] = None
    Status: Optional[str] = None
    SupportsDBInstanceAutomatedBackupsReplication: Optional[bool] = None

class StartActivityStreamRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Mode: ActivityStreamModeType
    KmsKeyId: str
    ApplyImmediately: Optional[bool] = None
    EngineNativeAuditFieldsIncluded: Optional[bool] = None

class StartDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef(BaseModel):
    SourceDBInstanceArn: str
    BackupRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    SourceRegion: Optional[str] = None

class StartDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str

class StartExportTaskMessageRequestTypeDef(BaseModel):
    ExportTaskIdentifier: str
    SourceArn: str
    S3BucketName: str
    IamRoleArn: str
    KmsKeyId: str
    S3Prefix: Optional[str] = None
    ExportOnly: Optional[Sequence[str]] = None

class StopActivityStreamRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ApplyImmediately: Optional[bool] = None

class StopDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef(BaseModel):
    SourceDBInstanceArn: str

class StopDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    DBSnapshotIdentifier: Optional[str] = None

class SwitchoverBlueGreenDeploymentRequestRequestTypeDef(BaseModel):
    BlueGreenDeploymentIdentifier: str
    SwitchoverTimeout: Optional[int] = None

class SwitchoverGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str

class SwitchoverReadReplicaMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str

class TenantDatabasePendingModifiedValuesTypeDef(BaseModel):
    MasterUserPassword: Optional[str] = None
    TenantDBName: Optional[str] = None

class AccountAttributesMessageTypeDef(BaseModel):
    AccountQuotas: List[AccountQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterBacktrackResponseTypeDef(BaseModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: str
    BacktrackTo: datetime
    BacktrackedFrom: datetime
    BacktrackRequestCreationTime: datetime
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterCapacityInfoTypeDef(BaseModel):
    DBClusterIdentifier: str
    PendingCapacity: int
    CurrentCapacity: int
    SecondsBeforeTimeout: int
    TimeoutAction: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterEndpointResponseTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupNameMessageTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupNameMessageTypeDef(BaseModel):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBShardGroupResponseTypeDef(BaseModel):
    DBShardGroupResourceId: str
    DBShardGroupIdentifier: str
    DBClusterIdentifier: str
    MaxACU: float
    ComputeRedundancy: int
    Status: str
    PubliclyAccessible: bool
    Endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableHttpEndpointResponseTypeDef(BaseModel):
    ResourceArn: str
    HttpEndpointEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DownloadDBLogFilePortionDetailsTypeDef(BaseModel):
    LogFileData: str
    Marker: str
    AdditionalDataPending: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableHttpEndpointResponseTypeDef(BaseModel):
    ResourceArn: str
    HttpEndpointEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTaskResponseTypeDef(BaseModel):
    ExportTaskIdentifier: str
    SourceArn: str
    ExportOnly: List[str]
    SnapshotTime: datetime
    TaskStartTime: datetime
    TaskEndTime: datetime
    S3Bucket: str
    S3Prefix: str
    IamRoleArn: str
    KmsKeyId: str
    Status: str
    PercentProgress: int
    TotalExtractedDataInGB: int
    FailureCause: str
    WarningMessage: str
    SourceType: ExportSourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyActivityStreamResponseTypeDef(BaseModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    Mode: ActivityStreamModeType
    EngineNativeAuditFieldsIncluded: bool
    PolicyStatus: ActivityStreamPolicyStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartActivityStreamResponseTypeDef(BaseModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    Mode: ActivityStreamModeType
    ApplyImmediately: bool
    EngineNativeAuditFieldsIncluded: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StopActivityStreamResponseTypeDef(BaseModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AddSourceIdentifierToSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(BaseModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSourceIdentifierFromSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopyDBClusterSnapshotMessageRequestTypeDef(BaseModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SourceRegion: Optional[str] = None

class CopyDBParameterGroupMessageRequestTypeDef(BaseModel):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopyDBSnapshotMessageRequestTypeDef(BaseModel):
    SourceDBSnapshotIdentifier: str
    TargetDBSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CopyTags: Optional[bool] = None
    PreSignedUrl: Optional[str] = None
    OptionGroupName: Optional[str] = None
    TargetCustomAvailabilityZone: Optional[str] = None
    CopyOptionGroup: Optional[bool] = None
    SourceRegion: Optional[str] = None

class CopyOptionGroupMessageRequestTypeDef(BaseModel):
    SourceOptionGroupIdentifier: str
    TargetOptionGroupIdentifier: str
    TargetOptionGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateBlueGreenDeploymentRequestRequestTypeDef(BaseModel):
    BlueGreenDeploymentName: str
    Source: str
    TargetEngineVersion: Optional[str] = None
    TargetDBParameterGroupName: Optional[str] = None
    TargetDBClusterParameterGroupName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TargetDBInstanceClass: Optional[str] = None
    UpgradeTargetStorageConfig: Optional[bool] = None

class CreateCustomDBEngineVersionMessageRequestTypeDef(BaseModel):
    Engine: str
    EngineVersion: str
    DatabaseInstallationFilesS3BucketName: Optional[str] = None
    DatabaseInstallationFilesS3Prefix: Optional[str] = None
    ImageId: Optional[str] = None
    KMSKeyId: Optional[str] = None
    Description: Optional[str] = None
    Manifest: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SourceCustomDbEngineVersionIdentifier: Optional[str] = None
    UseAwsProvidedLatestImage: Optional[bool] = None

class CreateDBClusterEndpointMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterSnapshotMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBProxyEndpointRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    DBProxyEndpointName: str
    VpcSubnetIds: Sequence[str]
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    TargetRole: Optional[DBProxyEndpointTargetRoleType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSecurityGroupMessageRequestTypeDef(BaseModel):
    DBSecurityGroupName: str
    DBSecurityGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSnapshotMessageRequestTypeDef(BaseModel):
    DBSnapshotIdentifier: str
    DBInstanceIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSubnetGroupMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateIntegrationMessageRequestTypeDef(BaseModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None

class CreateOptionGroupMessageRequestTypeDef(BaseModel):
    OptionGroupName: str
    EngineName: str
    MajorEngineVersion: str
    OptionGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTenantDatabaseMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    MasterUsername: str
    MasterUserPassword: str
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DBClusterSnapshotTypeDef(BaseModel):
    AvailabilityZones: Optional[List[str]] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[datetime] = None
    Engine: Optional[str] = None
    EngineMode: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DBClusterSnapshotArn: Optional[str] = None
    SourceDBClusterSnapshotArn: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    TagList: Optional[List[TagTypeDef]] = None
    DBSystemId: Optional[str] = None
    StorageType: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    StorageThroughput: Optional[int] = None

class DBSnapshotTenantDatabaseTypeDef(BaseModel):
    DBSnapshotIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DbiResourceId: Optional[str] = None
    EngineName: Optional[str] = None
    SnapshotType: Optional[str] = None
    TenantDatabaseCreateTime: Optional[datetime] = None
    TenantDBName: Optional[str] = None
    MasterUsername: Optional[str] = None
    TenantDatabaseResourceId: Optional[str] = None
    CharacterSetName: Optional[str] = None
    DBSnapshotTenantDatabaseARN: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None

class PurchaseReservedDBInstancesOfferingMessageRequestTypeDef(BaseModel):
    ReservedDBInstancesOfferingId: str
    ReservedDBInstanceId: Optional[str] = None
    DBInstanceCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagListMessageTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    MultiAZCapable: Optional[bool] = None
    ReadReplicaCapable: Optional[bool] = None
    Vpc: Optional[bool] = None
    SupportsStorageEncryption: Optional[bool] = None
    StorageType: Optional[str] = None
    SupportsIops: Optional[bool] = None
    SupportsEnhancedMonitoring: Optional[bool] = None
    SupportsIAMDatabaseAuthentication: Optional[bool] = None
    SupportsPerformanceInsights: Optional[bool] = None
    MinStorageSize: Optional[int] = None
    MaxStorageSize: Optional[int] = None
    MinIopsPerDbInstance: Optional[int] = None
    MaxIopsPerDbInstance: Optional[int] = None
    MinIopsPerGib: Optional[float] = None
    MaxIopsPerGib: Optional[float] = None
    AvailableProcessorFeatures: Optional[List[AvailableProcessorFeatureTypeDef]] = None
    SupportedEngineModes: Optional[List[str]] = None
    SupportsStorageAutoscaling: Optional[bool] = None
    SupportsKerberosAuthentication: Optional[bool] = None
    OutpostCapable: Optional[bool] = None
    SupportedActivityStreamModes: Optional[List[str]] = None
    SupportsGlobalDatabases: Optional[bool] = None
    SupportsClusters: Optional[bool] = None
    SupportedNetworkTypes: Optional[List[str]] = None
    SupportsStorageThroughput: Optional[bool] = None
    MinStorageThroughputPerDbInstance: Optional[int] = None
    MaxStorageThroughputPerDbInstance: Optional[int] = None
    MinStorageThroughputPerIops: Optional[float] = None
    MaxStorageThroughputPerIops: Optional[float] = None
    SupportsDedicatedLogVolume: Optional[bool] = None

class BacktrackDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    BacktrackTo: TimestampTypeDef
    Force: Optional[bool] = None
    UseEarliestTimeOnPointInTimeUnavailable: Optional[bool] = None

class BlueGreenDeploymentTypeDef(BaseModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    BlueGreenDeploymentName: Optional[str] = None
    Source: Optional[str] = None
    Target: Optional[str] = None
    SwitchoverDetails: Optional[List[SwitchoverDetailTypeDef]] = None
    Tasks: Optional[List[BlueGreenDeploymentTaskTypeDef]] = None
    Status: Optional[str] = None
    StatusDetails: Optional[str] = None
    CreateTime: Optional[datetime] = None
    DeleteTime: Optional[datetime] = None
    TagList: Optional[List[TagTypeDef]] = None

class CertificateMessageTypeDef(BaseModel):
    DefaultCertificateForNewLaunches: str
    Certificates: List[CertificateTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCertificatesResultTypeDef(BaseModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterPendingModifiedValuesTypeDef(BaseModel):
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExportsTypeDef] = None
    DBClusterIdentifier: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    EngineVersion: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    AllocatedStorage: Optional[int] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfigurationTypeDef] = None
    Iops: Optional[int] = None
    StorageType: Optional[str] = None
    CertificateDetails: Optional[CertificateDetailsTypeDef] = None

class DBProxyTargetGroupTypeDef(BaseModel):
    DBProxyName: Optional[str] = None
    TargetGroupName: Optional[str] = None
    TargetGroupArn: Optional[str] = None
    IsDefault: Optional[bool] = None
    Status: Optional[str] = None
    ConnectionPoolConfig: Optional[ConnectionPoolConfigurationInfoTypeDef] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None

class ModifyDBProxyTargetGroupRequestRequestTypeDef(BaseModel):
    TargetGroupName: str
    DBProxyName: str
    ConnectionPoolConfig: Optional[ConnectionPoolConfigurationTypeDef] = None
    NewName: Optional[str] = None

class CopyDBClusterParameterGroupResultTypeDef(BaseModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterParameterGroupResultTypeDef(BaseModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupsMessageTypeDef(BaseModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBParameterGroupResultTypeDef(BaseModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBParameterGroupResultTypeDef(BaseModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupsMessageTypeDef(BaseModel):
    Marker: str
    DBParameterGroups: List[DBParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    DatabaseName: Optional[str] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    EngineMode: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfigurationTypeDef] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfigurationTypeDef] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterIdentifier: Optional[str] = None
    EnableHttpEndpoint: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    EnableGlobalWriteForwarding: Optional[bool] = None
    DBClusterInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableLimitlessDatabase: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    NetworkType: Optional[str] = None
    DBSystemId: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    EnableLocalWriteForwarding: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None
    SourceRegion: Optional[str] = None

class ModifyDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfigurationTypeDef] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    DBInstanceParameterGroupName: Optional[str] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfigurationTypeDef] = None
    DeletionProtection: Optional[bool] = None
    EnableHttpEndpoint: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    EnableGlobalWriteForwarding: Optional[bool] = None
    DBClusterInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    NetworkType: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    RotateMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    EngineMode: Optional[str] = None
    AllowEngineModeChange: Optional[bool] = None
    EnableLocalWriteForwarding: Optional[bool] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    EnableLimitlessDatabase: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None

class RestoreDBClusterFromS3MessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    Engine: str
    MasterUsername: str
    SourceEngine: str
    SourceEngineVersion: str
    S3BucketName: str
    S3IngestionRoleArn: str
    AvailabilityZones: Optional[Sequence[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    DatabaseName: Optional[str] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    S3Prefix: Optional[str] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    NetworkType: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    StorageType: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None

class RestoreDBClusterFromSnapshotMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    DatabaseName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    EngineMode: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfigurationTypeDef] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DBClusterInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    NetworkType: Optional[str] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfigurationTypeDef] = None
    EngineLifecycleSupport: Optional[str] = None

class RestoreDBClusterToPointInTimeMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    RestoreType: Optional[str] = None
    SourceDBClusterIdentifier: Optional[str] = None
    RestoreToTime: Optional[TimestampTypeDef] = None
    UseLatestRestorableTime: Optional[bool] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfigurationTypeDef] = None
    EngineMode: Optional[str] = None
    DBClusterInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Iops: Optional[int] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    NetworkType: Optional[str] = None
    SourceDbClusterResourceId: Optional[str] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfigurationTypeDef] = None
    EngineLifecycleSupport: Optional[str] = None

class CreateDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBName: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    DBSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    DBParameterGroupName: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    Port: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DBClusterIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    Domain: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[Sequence[str]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[ProcessorFeatureTypeDef]] = None
    DeletionProtection: Optional[bool] = None
    MaxAllocatedStorage: Optional[int] = None
    EnableCustomerOwnedIp: Optional[bool] = None
    CustomIamInstanceProfile: Optional[str] = None
    BackupTarget: Optional[str] = None
    NetworkType: Optional[str] = None
    StorageThroughput: Optional[int] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DBSystemId: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None
    EngineLifecycleSupport: Optional[str] = None

class CreateDBInstanceReadReplicaMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    SourceDBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Port: Optional[int] = None
    MultiAZ: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    DBParameterGroupName: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DBSubnetGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    StorageType: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[ProcessorFeatureTypeDef]] = None
    UseDefaultProcessorFeatures: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[Sequence[str]] = None
    ReplicaMode: Optional[ReplicaModeType] = None
    MaxAllocatedStorage: Optional[int] = None
    CustomIamInstanceProfile: Optional[str] = None
    NetworkType: Optional[str] = None
    StorageThroughput: Optional[int] = None
    EnableCustomerOwnedIp: Optional[bool] = None
    AllocatedStorage: Optional[int] = None
    SourceDBClusterIdentifier: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    UpgradeStorageConfig: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None
    SourceRegion: Optional[str] = None

class DBSnapshotTypeDef(BaseModel):
    DBSnapshotIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[datetime] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    InstanceCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    PercentProgress: Optional[int] = None
    SourceRegion: Optional[str] = None
    SourceDBSnapshotIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DBSnapshotArn: Optional[str] = None
    Timezone: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    ProcessorFeatures: Optional[List[ProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None
    OriginalSnapshotCreateTime: Optional[datetime] = None
    SnapshotDatabaseTime: Optional[datetime] = None
    SnapshotTarget: Optional[str] = None
    StorageThroughput: Optional[int] = None
    DBSystemId: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None

class ModifyDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    AllocatedStorage: Optional[int] = None
    DBInstanceClass: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    DBSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    ApplyImmediately: Optional[bool] = None
    MasterUserPassword: Optional[str] = None
    DBParameterGroupName: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    NewDBInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    Domain: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[Sequence[str]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    DBPortNumber: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    MonitoringRoleArn: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DisableDomain: Optional[bool] = None
    PromotionTier: Optional[int] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfigurationTypeDef] = None
    ProcessorFeatures: Optional[Sequence[ProcessorFeatureTypeDef]] = None
    UseDefaultProcessorFeatures: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    MaxAllocatedStorage: Optional[int] = None
    CertificateRotationRestart: Optional[bool] = None
    ReplicaMode: Optional[ReplicaModeType] = None
    EnableCustomerOwnedIp: Optional[bool] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    AutomationMode: Optional[AutomationModeType] = None
    ResumeFullAutomationModeMinutes: Optional[int] = None
    NetworkType: Optional[str] = None
    StorageThroughput: Optional[int] = None
    ManageMasterUserPassword: Optional[bool] = None
    RotateMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    Engine: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None

class PendingModifiedValuesTypeDef(BaseModel):
    DBInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    Port: Optional[int] = None
    BackupRetentionPeriod: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    DBInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExportsTypeDef] = None
    ProcessorFeatures: Optional[List[ProcessorFeatureTypeDef]] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    AutomationMode: Optional[AutomationModeType] = None
    ResumeFullAutomationModeTime: Optional[datetime] = None
    StorageThroughput: Optional[int] = None
    Engine: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None

class RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    DBSnapshotIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    MultiAZ: Optional[bool] = None
    PubliclyAccessible: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    DBName: Optional[str] = None
    Engine: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Domain: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[Sequence[str]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    DomainIAMRoleName: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[ProcessorFeatureTypeDef]] = None
    UseDefaultProcessorFeatures: Optional[bool] = None
    DBParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EnableCustomerOwnedIp: Optional[bool] = None
    CustomIamInstanceProfile: Optional[str] = None
    BackupTarget: Optional[str] = None
    NetworkType: Optional[str] = None
    StorageThroughput: Optional[int] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    DedicatedLogVolume: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None

class RestoreDBInstanceFromS3MessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    SourceEngine: str
    SourceEngineVersion: str
    S3BucketName: str
    S3IngestionRoleArn: str
    DBName: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    DBSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    DBParameterGroupName: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    Port: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageType: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    S3Prefix: Optional[str] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[ProcessorFeatureTypeDef]] = None
    UseDefaultProcessorFeatures: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    MaxAllocatedStorage: Optional[int] = None
    NetworkType: Optional[str] = None
    StorageThroughput: Optional[int] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None

class RestoreDBInstanceToPointInTimeMessageRequestTypeDef(BaseModel):
    TargetDBInstanceIdentifier: str
    SourceDBInstanceIdentifier: Optional[str] = None
    RestoreTime: Optional[TimestampTypeDef] = None
    UseLatestRestorableTime: Optional[bool] = None
    DBInstanceClass: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    MultiAZ: Optional[bool] = None
    PubliclyAccessible: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    DBName: Optional[str] = None
    Engine: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[Sequence[str]] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[ProcessorFeatureTypeDef]] = None
    UseDefaultProcessorFeatures: Optional[bool] = None
    DBParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    SourceDbiResourceId: Optional[str] = None
    MaxAllocatedStorage: Optional[int] = None
    SourceDBInstanceAutomatedBackupsArn: Optional[str] = None
    EnableCustomerOwnedIp: Optional[bool] = None
    CustomIamInstanceProfile: Optional[str] = None
    BackupTarget: Optional[str] = None
    NetworkType: Optional[str] = None
    StorageThroughput: Optional[int] = None
    AllocatedStorage: Optional[int] = None
    DedicatedLogVolume: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None

class CreateDBProxyEndpointResponseTypeDef(BaseModel):
    DBProxyEndpoint: DBProxyEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBProxyEndpointResponseTypeDef(BaseModel):
    DBProxyEndpoint: DBProxyEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBProxyEndpointsResponseTypeDef(BaseModel):
    DBProxyEndpoints: List[DBProxyEndpointTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBProxyEndpointResponseTypeDef(BaseModel):
    DBProxyEndpoint: DBProxyEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBProxyRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    EngineFamily: EngineFamilyType
    Auth: Sequence[UserAuthConfigTypeDef]
    RoleArn: str
    VpcSubnetIds: Sequence[str]
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ModifyDBProxyRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    NewDBProxyName: Optional[str] = None
    Auth: Optional[Sequence[UserAuthConfigTypeDef]] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    RoleArn: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None

class DBClusterAutomatedBackupTypeDef(BaseModel):
    Engine: Optional[str] = None
    VpcId: Optional[str] = None
    DBClusterAutomatedBackupsArn: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    RestoreWindow: Optional[RestoreWindowTypeDef] = None
    MasterUsername: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    Region: Optional[str] = None
    LicenseModel: Optional[str] = None
    Status: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    ClusterCreateTime: Optional[datetime] = None
    StorageEncrypted: Optional[bool] = None
    AllocatedStorage: Optional[int] = None
    EngineVersion: Optional[str] = None
    DBClusterArn: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    EngineMode: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    Port: Optional[int] = None
    KmsKeyId: Optional[str] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    StorageThroughput: Optional[int] = None

class DBClusterBacktrackMessageTypeDef(BaseModel):
    Marker: str
    DBClusterBacktracks: List[DBClusterBacktrackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterEndpointMessageTypeDef(BaseModel):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupDetailsTypeDef(BaseModel):
    Parameters: List[ParameterOutputTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupDetailsTypeDef(BaseModel):
    Parameters: List[ParameterOutputTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(BaseModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterOutputTypeDef]] = None

class DBClusterSnapshotAttributesResultTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttributeTypeDef]] = None

class DBEngineVersionResponseTypeDef(BaseModel):
    Engine: str
    EngineVersion: str
    DBParameterGroupFamily: str
    DBEngineDescription: str
    DBEngineVersionDescription: str
    DefaultCharacterSet: CharacterSetTypeDef
    Image: CustomDBEngineVersionAMITypeDef
    DBEngineMediaType: str
    SupportedCharacterSets: List[CharacterSetTypeDef]
    SupportedNcharCharacterSets: List[CharacterSetTypeDef]
    ValidUpgradeTarget: List[UpgradeTargetTypeDef]
    SupportedTimezones: List[TimezoneTypeDef]
    ExportableLogTypes: List[str]
    SupportsLogExportsToCloudwatchLogs: bool
    SupportsReadReplica: bool
    SupportedEngineModes: List[str]
    SupportedFeatureNames: List[str]
    Status: str
    SupportsParallelQuery: bool
    SupportsGlobalDatabases: bool
    MajorEngineVersion: str
    DatabaseInstallationFilesS3BucketName: str
    DatabaseInstallationFilesS3Prefix: str
    DBEngineVersionArn: str
    KMSKeyId: str
    CreateTime: datetime
    TagList: List[TagTypeDef]
    SupportsBabelfish: bool
    CustomDBEngineVersionManifest: str
    SupportsLimitlessDatabase: bool
    SupportsCertificateRotationWithoutRestart: bool
    SupportedCACertificateIdentifiers: List[str]
    SupportsLocalWriteForwarding: bool
    SupportsIntegrations: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DBEngineVersionTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    DBEngineDescription: Optional[str] = None
    DBEngineVersionDescription: Optional[str] = None
    DefaultCharacterSet: Optional[CharacterSetTypeDef] = None
    Image: Optional[CustomDBEngineVersionAMITypeDef] = None
    DBEngineMediaType: Optional[str] = None
    SupportedCharacterSets: Optional[List[CharacterSetTypeDef]] = None
    SupportedNcharCharacterSets: Optional[List[CharacterSetTypeDef]] = None
    ValidUpgradeTarget: Optional[List[UpgradeTargetTypeDef]] = None
    SupportedTimezones: Optional[List[TimezoneTypeDef]] = None
    ExportableLogTypes: Optional[List[str]] = None
    SupportsLogExportsToCloudwatchLogs: Optional[bool] = None
    SupportsReadReplica: Optional[bool] = None
    SupportedEngineModes: Optional[List[str]] = None
    SupportedFeatureNames: Optional[List[str]] = None
    Status: Optional[str] = None
    SupportsParallelQuery: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None
    MajorEngineVersion: Optional[str] = None
    DatabaseInstallationFilesS3BucketName: Optional[str] = None
    DatabaseInstallationFilesS3Prefix: Optional[str] = None
    DBEngineVersionArn: Optional[str] = None
    KMSKeyId: Optional[str] = None
    CreateTime: Optional[datetime] = None
    TagList: Optional[List[TagTypeDef]] = None
    SupportsBabelfish: Optional[bool] = None
    CustomDBEngineVersionManifest: Optional[str] = None
    SupportsLimitlessDatabase: Optional[bool] = None
    SupportsCertificateRotationWithoutRestart: Optional[bool] = None
    SupportedCACertificateIdentifiers: Optional[List[str]] = None
    SupportsLocalWriteForwarding: Optional[bool] = None
    SupportsIntegrations: Optional[bool] = None

class DBInstanceAutomatedBackupTypeDef(BaseModel):
    DBInstanceArn: Optional[str] = None
    DbiResourceId: Optional[str] = None
    Region: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    RestoreWindow: Optional[RestoreWindowTypeDef] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    InstanceCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    Encrypted: Optional[bool] = None
    StorageType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Timezone: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    BackupRetentionPeriod: Optional[int] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None
    DBInstanceAutomatedBackupsReplications: Optional[       List[DBInstanceAutomatedBackupsReplicationTypeDef]     ] = None
    BackupTarget: Optional[str] = None
    StorageThroughput: Optional[int] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None

class DBProxyTargetTypeDef(BaseModel):
    TargetArn: Optional[str] = None
    Endpoint: Optional[str] = None
    TrackedClusterId: Optional[str] = None
    RdsResourceId: Optional[str] = None
    Port: Optional[int] = None
    Type: Optional[TargetTypeType] = None
    Role: Optional[TargetRoleType] = None
    TargetHealth: Optional[TargetHealthTypeDef] = None

class DBProxyTypeDef(BaseModel):
    DBProxyName: Optional[str] = None
    DBProxyArn: Optional[str] = None
    Status: Optional[DBProxyStatusType] = None
    EngineFamily: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    VpcSubnetIds: Optional[List[str]] = None
    Auth: Optional[List[UserAuthConfigInfoTypeDef]] = None
    RoleArn: Optional[str] = None
    Endpoint: Optional[str] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None

class DBSecurityGroupTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    DBSecurityGroupName: Optional[str] = None
    DBSecurityGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroupTypeDef]] = None
    IPRanges: Optional[List[IPRangeTypeDef]] = None
    DBSecurityGroupArn: Optional[str] = None

class DescribeDBShardGroupsResponseTypeDef(BaseModel):
    DBShardGroups: List[DBShardGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBSnapshotAttributesResultTypeDef(BaseModel):
    DBSnapshotIdentifier: Optional[str] = None
    DBSnapshotAttributes: Optional[List[DBSnapshotAttributeTypeDef]] = None

class DescribeBlueGreenDeploymentsRequestRequestTypeDef(BaseModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeCertificatesMessageRequestTypeDef(BaseModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterAutomatedBackupsMessageRequestTypeDef(BaseModel):
    DbClusterResourceId: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterBacktracksMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterEndpointsMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParameterGroupsMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParametersMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterSnapshotsMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None

class DescribeDBClustersMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None

class DescribeDBEngineVersionsMessageRequestTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    IncludeAll: Optional[bool] = None

class DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef(BaseModel):
    DbiResourceId: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None

class DescribeDBInstancesMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBLogFilesMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    FilenameContains: Optional[str] = None
    FileLastWritten: Optional[int] = None
    FileSize: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParameterGroupsMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParametersMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBProxiesRequestRequestTypeDef(BaseModel):
    DBProxyName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBProxyEndpointsRequestRequestTypeDef(BaseModel):
    DBProxyName: Optional[str] = None
    DBProxyEndpointName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBProxyTargetGroupsRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBProxyTargetsRequestRequestTypeDef(BaseModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBRecommendationsMessageRequestTypeDef(BaseModel):
    LastUpdatedAfter: Optional[TimestampTypeDef] = None
    LastUpdatedBefore: Optional[TimestampTypeDef] = None
    Locale: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBSecurityGroupsMessageRequestTypeDef(BaseModel):
    DBSecurityGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBShardGroupsMessageRequestTypeDef(BaseModel):
    DBShardGroupIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DbiResourceId: Optional[str] = None

class DescribeDBSnapshotsMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None

class DescribeDBSubnetGroupsMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultClusterParametersMessageRequestTypeDef(BaseModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultParametersMessageRequestTypeDef(BaseModel):
    DBParameterGroupFamily: str
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
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeExportTasksMessageRequestTypeDef(BaseModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    SourceType: Optional[ExportSourceTypeType] = None

class DescribeGlobalClustersMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeIntegrationsMessageRequestTypeDef(BaseModel):
    IntegrationIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeOptionGroupOptionsMessageRequestTypeDef(BaseModel):
    EngineName: str
    MajorEngineVersion: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeOptionGroupsMessageRequestTypeDef(BaseModel):
    OptionGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None

class DescribeOrderableDBInstanceOptionsMessageRequestTypeDef(BaseModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePendingMaintenanceActionsMessageRequestTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeReservedDBInstancesMessageRequestTypeDef(BaseModel):
    ReservedDBInstanceId: Optional[str] = None
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    LeaseId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedDBInstancesOfferingsMessageRequestTypeDef(BaseModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeSourceRegionsMessageRequestTypeDef(BaseModel):
    RegionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeTenantDatabasesMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class ListTagsForResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateTypeDef(BaseModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef(BaseModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateTypeDef(BaseModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef(BaseModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    IncludeAll: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateTypeDef(BaseModel):
    DbiResourceId: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBLogFilesMessageDescribeDBLogFilesPaginateTypeDef(BaseModel):
    DBInstanceIdentifier: str
    FilenameContains: Optional[str] = None
    FileLastWritten: Optional[int] = None
    FileSize: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef(BaseModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxiesRequestDescribeDBProxiesPaginateTypeDef(BaseModel):
    DBProxyName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateTypeDef(BaseModel):
    DBProxyName: Optional[str] = None
    DBProxyEndpointName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateTypeDef(BaseModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateTypeDef(BaseModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBRecommendationsMessageDescribeDBRecommendationsPaginateTypeDef(BaseModel):
    LastUpdatedAfter: Optional[TimestampTypeDef] = None
    LastUpdatedBefore: Optional[TimestampTypeDef] = None
    Locale: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateTypeDef(BaseModel):
    DBSecurityGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef(BaseModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateTypeDef(BaseModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef(BaseModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportTasksMessageDescribeExportTasksPaginateTypeDef(BaseModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SourceType: Optional[ExportSourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIntegrationsMessageDescribeIntegrationsPaginateTypeDef(BaseModel):
    IntegrationIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateTypeDef(BaseModel):
    EngineName: str
    MajorEngineVersion: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOptionGroupsMessageDescribeOptionGroupsPaginateTypeDef(BaseModel):
    OptionGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef(BaseModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateTypeDef(BaseModel):
    ReservedDBInstanceId: Optional[str] = None
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    LeaseId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateTypeDef(BaseModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceRegionsMessageDescribeSourceRegionsPaginateTypeDef(BaseModel):
    RegionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTenantDatabasesMessageDescribeTenantDatabasesPaginateTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateTypeDef(BaseModel):
    DBInstanceIdentifier: str
    LogFileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBClustersMessageDBClusterAvailableWaitTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBClustersMessageDBClusterDeletedWaitTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBSnapshotsMessageDBSnapshotAvailableWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBSnapshotsMessageDBSnapshotCompletedWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBSnapshotsMessageDBSnapshotDeletedWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTenantDatabasesMessageTenantDatabaseAvailableWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTenantDatabasesMessageTenantDatabaseDeletedWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBLogFilesResponseTypeDef(BaseModel):
    DescribeDBLogFiles: List[DescribeDBLogFilesDetailsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMessageTypeDef(BaseModel):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventsMessageTypeDef(BaseModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTasksMessageTypeDef(BaseModel):
    Marker: str
    ExportTasks: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClusterTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    GlobalClusterResourceId: Optional[str] = None
    GlobalClusterArn: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterMembers: Optional[List[GlobalClusterMemberTypeDef]] = None
    FailoverState: Optional[FailoverStateTypeDef] = None

class IntegrationResponseTypeDef(BaseModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    IntegrationArn: str
    KMSKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Status: IntegrationStatusType
    Tags: List[TagTypeDef]
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    IntegrationName: Optional[str] = None
    IntegrationArn: Optional[str] = None
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Status: Optional[IntegrationStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None
    CreateTime: Optional[datetime] = None
    Errors: Optional[List[IntegrationErrorTypeDef]] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None

class OptionGroupOptionSettingTypeDef(BaseModel):
    SettingName: Optional[str] = None
    SettingDescription: Optional[str] = None
    DefaultValue: Optional[str] = None
    ApplyType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    MinimumEngineVersionPerAllowedValue: Optional[       List[MinimumEngineVersionPerAllowedValueTypeDef]     ] = None

class ModifyDBRecommendationMessageRequestTypeDef(BaseModel):
    RecommendationId: str
    Locale: Optional[str] = None
    Status: Optional[str] = None
    RecommendedActionUpdates: Optional[Sequence[RecommendedActionUpdateTypeDef]] = None

class OptionConfigurationTypeDef(BaseModel):
    OptionName: str
    Port: Optional[int] = None
    OptionVersion: Optional[str] = None
    DBSecurityGroupMemberships: Optional[Sequence[str]] = None
    VpcSecurityGroupMemberships: Optional[Sequence[str]] = None
    OptionSettings: Optional[Sequence[OptionSettingTypeDef]] = None

class OptionTypeDef(BaseModel):
    OptionName: Optional[str] = None
    OptionDescription: Optional[str] = None
    Persistent: Optional[bool] = None
    Permanent: Optional[bool] = None
    Port: Optional[int] = None
    OptionVersion: Optional[str] = None
    OptionSettings: Optional[List[OptionSettingTypeDef]] = None
    DBSecurityGroupMemberships: Optional[List[DBSecurityGroupMembershipTypeDef]] = None
    VpcSecurityGroupMemberships: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None

class SubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetOutpost: Optional[OutpostTypeDef] = None
    SubnetStatus: Optional[str] = None

class ResourcePendingMaintenanceActionsTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None

class PerformanceInsightsMetricQueryTypeDef(BaseModel):
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroupTypeDef] = None
    Metric: Optional[str] = None

class ValidStorageOptionsTypeDef(BaseModel):
    StorageType: Optional[str] = None
    StorageSize: Optional[List[RangeTypeDef]] = None
    ProvisionedIops: Optional[List[RangeTypeDef]] = None
    IopsToStorageRatio: Optional[List[DoubleRangeTypeDef]] = None
    SupportsStorageAutoscaling: Optional[bool] = None
    ProvisionedStorageThroughput: Optional[List[RangeTypeDef]] = None
    StorageThroughputToIopsRatio: Optional[List[DoubleRangeTypeDef]] = None

class ReservedDBInstanceTypeDef(BaseModel):
    ReservedDBInstanceId: Optional[str] = None
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    DBInstanceCount: Optional[int] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    State: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ReservedDBInstanceArn: Optional[str] = None
    LeaseId: Optional[str] = None

class ReservedDBInstancesOfferingTypeDef(BaseModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReferenceDetailsTypeDef(BaseModel):
    ScalarReferenceDetails: Optional[ScalarReferenceDetailsTypeDef] = None

class SourceRegionMessageTypeDef(BaseModel):
    Marker: str
    SourceRegions: List[SourceRegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TenantDatabaseTypeDef(BaseModel):
    TenantDatabaseCreateTime: Optional[datetime] = None
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Status: Optional[str] = None
    MasterUsername: Optional[str] = None
    DbiResourceId: Optional[str] = None
    TenantDatabaseResourceId: Optional[str] = None
    TenantDatabaseARN: Optional[str] = None
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    PendingModifiedValues: Optional[TenantDatabasePendingModifiedValuesTypeDef] = None
    TagList: Optional[List[TagTypeDef]] = None

class CopyDBClusterSnapshotResultTypeDef(BaseModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterSnapshotResultTypeDef(BaseModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterSnapshotMessageTypeDef(BaseModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterSnapshotResultTypeDef(BaseModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBSnapshotTenantDatabasesMessageTypeDef(BaseModel):
    Marker: str
    DBSnapshotTenantDatabases: List[DBSnapshotTenantDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionsMessageTypeDef(BaseModel):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBlueGreenDeploymentResponseTypeDef(BaseModel):
    BlueGreenDeployment: BlueGreenDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBlueGreenDeploymentResponseTypeDef(BaseModel):
    BlueGreenDeployment: BlueGreenDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBlueGreenDeploymentsResponseTypeDef(BaseModel):
    BlueGreenDeployments: List[BlueGreenDeploymentTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverBlueGreenDeploymentResponseTypeDef(BaseModel):
    BlueGreenDeployment: BlueGreenDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterTypeDef(BaseModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    DatabaseName: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBClusterParameterGroup: Optional[str] = None
    DBSubnetGroup: Optional[str] = None
    Status: Optional[str] = None
    AutomaticRestartTime: Optional[datetime] = None
    PercentProgress: Optional[str] = None
    EarliestRestorableTime: Optional[datetime] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    CustomEndpoints: Optional[List[str]] = None
    MultiAZ: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    LatestRestorableTime: Optional[datetime] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    DBClusterOptionGroupMemberships: Optional[List[DBClusterOptionGroupStatusTypeDef]] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    ReadReplicaIdentifiers: Optional[List[str]] = None
    StatusInfos: Optional[List[DBClusterStatusInfoTypeDef]] = None
    DBClusterMembers: Optional[List[DBClusterMemberTypeDef]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    DBClusterArn: Optional[str] = None
    AssociatedRoles: Optional[List[DBClusterRoleTypeDef]] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    CloneGroupId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    EarliestBacktrackTime: Optional[datetime] = None
    BacktrackWindow: Optional[int] = None
    BacktrackConsumedChangeRecords: Optional[int] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    Capacity: Optional[int] = None
    EngineMode: Optional[str] = None
    ScalingConfigurationInfo: Optional[ScalingConfigurationInfoTypeDef] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfigurationTypeDef] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamMode: Optional[ActivityStreamModeType] = None
    ActivityStreamStatus: Optional[ActivityStreamStatusType] = None
    ActivityStreamKmsKeyId: Optional[str] = None
    ActivityStreamKinesisStreamName: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[DomainMembershipTypeDef]] = None
    TagList: Optional[List[TagTypeDef]] = None
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatusType] = None
    GlobalWriteForwardingRequested: Optional[bool] = None
    PendingModifiedValues: Optional[ClusterPendingModifiedValuesTypeDef] = None
    DBClusterInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    ServerlessV2ScalingConfiguration: Optional[       ServerlessV2ScalingConfigurationInfoTypeDef     ] = None
    NetworkType: Optional[str] = None
    DBSystemId: Optional[str] = None
    MasterUserSecret: Optional[MasterUserSecretTypeDef] = None
    IOOptimizedNextAllowedModificationTime: Optional[datetime] = None
    LocalWriteForwardingStatus: Optional[LocalWriteForwardingStatusType] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    LimitlessDatabase: Optional[LimitlessDatabaseTypeDef] = None
    StorageThroughput: Optional[int] = None
    CertificateDetails: Optional[CertificateDetailsTypeDef] = None
    EngineLifecycleSupport: Optional[str] = None

class DescribeDBProxyTargetGroupsResponseTypeDef(BaseModel):
    TargetGroups: List[DBProxyTargetGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBProxyTargetGroupResponseTypeDef(BaseModel):
    DBProxyTargetGroup: DBProxyTargetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBSnapshotResultTypeDef(BaseModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSnapshotResultTypeDef(BaseModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBSnapshotMessageTypeDef(BaseModel):
    Marker: str
    DBSnapshots: List[DBSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBSnapshotResultTypeDef(BaseModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSnapshotResultTypeDef(BaseModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterAutomatedBackupMessageTypeDef(BaseModel):
    Marker: str
    DBClusterAutomatedBackups: List[DBClusterAutomatedBackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterAutomatedBackupResultTypeDef(BaseModel):
    DBClusterAutomatedBackup: DBClusterAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultClusterParametersResultTypeDef(BaseModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(BaseModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBClusterSnapshotAttributesResultTypeDef(BaseModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterSnapshotAttributeResultTypeDef(BaseModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBEngineVersionMessageTypeDef(BaseModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceAutomatedBackupMessageTypeDef(BaseModel):
    Marker: str
    DBInstanceAutomatedBackups: List[DBInstanceAutomatedBackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBInstanceAutomatedBackupResultTypeDef(BaseModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBInstanceAutomatedBackupsReplicationResultTypeDef(BaseModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBInstanceAutomatedBackupsReplicationResultTypeDef(BaseModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBProxyTargetsResponseTypeDef(BaseModel):
    Targets: List[DBProxyTargetTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDBProxyTargetsResponseTypeDef(BaseModel):
    DBProxyTargets: List[DBProxyTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBProxyResponseTypeDef(BaseModel):
    DBProxy: DBProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBProxyResponseTypeDef(BaseModel):
    DBProxy: DBProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBProxiesResponseTypeDef(BaseModel):
    DBProxies: List[DBProxyTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBProxyResponseTypeDef(BaseModel):
    DBProxy: DBProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeDBSecurityGroupIngressResultTypeDef(BaseModel):
    DBSecurityGroup: DBSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSecurityGroupResultTypeDef(BaseModel):
    DBSecurityGroup: DBSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBSecurityGroupMessageTypeDef(BaseModel):
    Marker: str
    DBSecurityGroups: List[DBSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeDBSecurityGroupIngressResultTypeDef(BaseModel):
    DBSecurityGroup: DBSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBSnapshotAttributesResultTypeDef(BaseModel):
    DBSnapshotAttributesResult: DBSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSnapshotAttributeResultTypeDef(BaseModel):
    DBSnapshotAttributesResult: DBSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClustersMessageTypeDef(BaseModel):
    Marker: str
    GlobalClusters: List[GlobalClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFromGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIntegrationsResponseTypeDef(BaseModel):
    Marker: str
    Integrations: List[IntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OptionGroupOptionTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    MinimumRequiredMinorEngineVersion: Optional[str] = None
    PortRequired: Optional[bool] = None
    DefaultPort: Optional[int] = None
    OptionsDependedOn: Optional[List[str]] = None
    OptionsConflictsWith: Optional[List[str]] = None
    Persistent: Optional[bool] = None
    Permanent: Optional[bool] = None
    RequiresAutoMinorEngineVersionUpgrade: Optional[bool] = None
    VpcOnly: Optional[bool] = None
    SupportsOptionVersionDowngrade: Optional[bool] = None
    OptionGroupOptionSettings: Optional[List[OptionGroupOptionSettingTypeDef]] = None
    OptionGroupOptionVersions: Optional[List[OptionVersionTypeDef]] = None
    CopyableCrossAccount: Optional[bool] = None

class ModifyOptionGroupMessageRequestTypeDef(BaseModel):
    OptionGroupName: str
    OptionsToInclude: Optional[Sequence[OptionConfigurationTypeDef]] = None
    OptionsToRemove: Optional[Sequence[str]] = None
    ApplyImmediately: Optional[bool] = None

class OptionGroupTypeDef(BaseModel):
    OptionGroupName: Optional[str] = None
    OptionGroupDescription: Optional[str] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    Options: Optional[List[OptionTypeDef]] = None
    AllowsVpcAndNonVpcInstanceMemberships: Optional[bool] = None
    VpcId: Optional[str] = None
    OptionGroupArn: Optional[str] = None
    SourceOptionGroup: Optional[str] = None
    SourceAccountId: Optional[str] = None
    CopyTimestamp: Optional[datetime] = None

class DBSubnetGroupTypeDef(BaseModel):
    DBSubnetGroupName: Optional[str] = None
    DBSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    DBSubnetGroupArn: Optional[str] = None
    SupportedNetworkTypes: Optional[List[str]] = None

class ModifyDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    Parameters: Sequence[ParameterUnionTypeDef]

class ModifyDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    Parameters: Sequence[ParameterUnionTypeDef]

class ResetDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterUnionTypeDef]] = None

class ResetDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterUnionTypeDef]] = None

class ApplyPendingMaintenanceActionResultTypeDef(BaseModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingMaintenanceActionsMessageTypeDef(BaseModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricQueryTypeDef(BaseModel):
    PerformanceInsightsMetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None

class ValidDBInstanceModificationsMessageTypeDef(BaseModel):
    Storage: Optional[List[ValidStorageOptionsTypeDef]] = None
    ValidProcessorFeatures: Optional[List[AvailableProcessorFeatureTypeDef]] = None
    SupportsDedicatedLogVolume: Optional[bool] = None

class PurchaseReservedDBInstancesOfferingResultTypeDef(BaseModel):
    ReservedDBInstance: ReservedDBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedDBInstanceMessageTypeDef(BaseModel):
    Marker: str
    ReservedDBInstances: List[ReservedDBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedDBInstancesOfferingMessageTypeDef(BaseModel):
    Marker: str
    ReservedDBInstancesOfferings: List[ReservedDBInstancesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    ReferenceDetails: Optional[ReferenceDetailsTypeDef] = None

class CreateTenantDatabaseResultTypeDef(BaseModel):
    TenantDatabase: TenantDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTenantDatabaseResultTypeDef(BaseModel):
    TenantDatabase: TenantDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTenantDatabaseResultTypeDef(BaseModel):
    TenantDatabase: TenantDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TenantDatabasesMessageTypeDef(BaseModel):
    Marker: str
    TenantDatabases: List[TenantDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterMessageTypeDef(BaseModel):
    Marker: str
    DBClusters: List[DBClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteReadReplicaDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterFromS3ResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterFromSnapshotResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterToPointInTimeResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OptionGroupOptionsMessageTypeDef(BaseModel):
    OptionGroupOptions: List[OptionGroupOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopyOptionGroupResultTypeDef(BaseModel):
    OptionGroup: OptionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOptionGroupResultTypeDef(BaseModel):
    OptionGroup: OptionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyOptionGroupResultTypeDef(BaseModel):
    OptionGroup: OptionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OptionGroupsTypeDef(BaseModel):
    OptionGroupsList: List[OptionGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSubnetGroupResultTypeDef(BaseModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Engine: Optional[str] = None
    DBInstanceStatus: Optional[str] = None
    AutomaticRestartTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    AllocatedStorage: Optional[int] = None
    InstanceCreateTime: Optional[datetime] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DBSecurityGroups: Optional[List[DBSecurityGroupMembershipTypeDef]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    DBParameterGroups: Optional[List[DBParameterGroupStatusTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroup: Optional[DBSubnetGroupTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValuesTypeDef] = None
    LatestRestorableTime: Optional[datetime] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    ReplicaMode: Optional[ReplicaModeType] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[OptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StatusInfos: Optional[List[DBInstanceStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DBClusterIdentifier: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbiResourceId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DomainMemberships: Optional[List[DomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    DBInstanceArn: Optional[str] = None
    Timezone: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeatureTypeDef]] = None
    DeletionProtection: Optional[bool] = None
    AssociatedRoles: Optional[List[DBInstanceRoleTypeDef]] = None
    ListenerEndpoint: Optional[EndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None
    TagList: Optional[List[TagTypeDef]] = None
    DBInstanceAutomatedBackupsReplications: Optional[       List[DBInstanceAutomatedBackupsReplicationTypeDef]     ] = None
    CustomerOwnedIpEnabled: Optional[bool] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    ActivityStreamStatus: Optional[ActivityStreamStatusType] = None
    ActivityStreamKmsKeyId: Optional[str] = None
    ActivityStreamKinesisStreamName: Optional[str] = None
    ActivityStreamMode: Optional[ActivityStreamModeType] = None
    ActivityStreamEngineNativeAuditFieldsIncluded: Optional[bool] = None
    AutomationMode: Optional[AutomationModeType] = None
    ResumeFullAutomationModeTime: Optional[datetime] = None
    CustomIamInstanceProfile: Optional[str] = None
    BackupTarget: Optional[str] = None
    NetworkType: Optional[str] = None
    ActivityStreamPolicyStatus: Optional[ActivityStreamPolicyStatusType] = None
    StorageThroughput: Optional[int] = None
    DBSystemId: Optional[str] = None
    MasterUserSecret: Optional[MasterUserSecretTypeDef] = None
    CertificateDetails: Optional[CertificateDetailsTypeDef] = None
    ReadReplicaSourceDBClusterIdentifier: Optional[str] = None
    PercentProgress: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    IsStorageConfigUpgradeAvailable: Optional[bool] = None
    MultiTenant: Optional[bool] = None
    EngineLifecycleSupport: Optional[str] = None

class DBSubnetGroupMessageTypeDef(BaseModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSubnetGroupResultTypeDef(BaseModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeValidDBInstanceModificationsResultTypeDef(BaseModel):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MetricTypeDef(BaseModel):
    Name: Optional[str] = None
    References: Optional[List[MetricReferenceTypeDef]] = None
    StatisticsDetails: Optional[str] = None
    MetricQuery: Optional[MetricQueryTypeDef] = None

class CreateDBInstanceReadReplicaResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceMessageTypeDef(BaseModel):
    Marker: str
    DBInstances: List[DBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteReadReplicaResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBInstanceFromDBSnapshotResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBInstanceFromS3ResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBInstanceToPointInTimeResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverReadReplicaResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceIssueDetailsTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Metrics: Optional[List[MetricTypeDef]] = None
    Analysis: Optional[str] = None

class IssueDetailsTypeDef(BaseModel):
    PerformanceIssueDetails: Optional[PerformanceIssueDetailsTypeDef] = None

class RecommendedActionTypeDef(BaseModel):
    ActionId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Operation: Optional[str] = None
    Parameters: Optional[List[RecommendedActionParameterTypeDef]] = None
    ApplyModes: Optional[List[str]] = None
    Status: Optional[str] = None
    IssueDetails: Optional[IssueDetailsTypeDef] = None
    ContextAttributes: Optional[List[ContextAttributeTypeDef]] = None

class DBRecommendationTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    TypeId: Optional[str] = None
    Severity: Optional[str] = None
    ResourceArn: Optional[str] = None
    Status: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    UpdatedTime: Optional[datetime] = None
    Detection: Optional[str] = None
    Recommendation: Optional[str] = None
    Description: Optional[str] = None
    Reason: Optional[str] = None
    RecommendedActions: Optional[List[RecommendedActionTypeDef]] = None
    Category: Optional[str] = None
    Source: Optional[str] = None
    TypeDetection: Optional[str] = None
    TypeRecommendation: Optional[str] = None
    Impact: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    Links: Optional[List[DocLinkTypeDef]] = None
    IssueDetails: Optional[IssueDetailsTypeDef] = None

class DBRecommendationMessageTypeDef(BaseModel):
    DBRecommendation: DBRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBRecommendationsMessageTypeDef(BaseModel):
    DBRecommendations: List[DBRecommendationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

