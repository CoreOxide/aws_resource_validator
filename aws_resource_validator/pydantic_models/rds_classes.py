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
from aws_resource_validator.pydantic_models.rds_constants import *

class AccountQuotaTypeDef(BaseValidatorModel):
    AccountQuotaName: Optional[str] = None
    Used: Optional[int] = None
    Max: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddRoleToDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class AddRoleToDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    RoleArn: str
    FeatureName: str

class AddSourceIdentifierToSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str

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
    EventSubscriptionArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ApplyPendingMaintenanceActionMessageRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str

class AuthorizeDBSecurityGroupIngressMessageRequestTypeDef(BaseValidatorModel):
    DBSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class AvailableProcessorFeatureTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[str] = None

class BlueGreenDeploymentTaskTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None

class SwitchoverDetailTypeDef(BaseValidatorModel):
    SourceMember: Optional[str] = None
    TargetMember: Optional[str] = None
    Status: Optional[str] = None

class CancelExportTaskMessageRequestTypeDef(BaseValidatorModel):
    ExportTaskIdentifier: str

class CertificateDetailsTypeDef(BaseValidatorModel):
    CAIdentifier: Optional[str] = None
    ValidTill: Optional[datetime] = None

class CertificateTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    CertificateType: Optional[str] = None
    Thumbprint: Optional[str] = None
    ValidFrom: Optional[datetime] = None
    ValidTill: Optional[datetime] = None
    CertificateArn: Optional[str] = None
    CustomerOverride: Optional[bool] = None
    CustomerOverrideValidTill: Optional[datetime] = None

class CharacterSetTypeDef(BaseValidatorModel):
    CharacterSetName: Optional[str] = None
    CharacterSetDescription: Optional[str] = None

class ClientGenerateDbAuthTokenRequestTypeDef(BaseValidatorModel):
    DBHostname: str
    Port: int
    DBUsername: str
    Region: Optional[Optional[str]] = None

class CloudwatchLogsExportConfigurationTypeDef(BaseValidatorModel):
    EnableLogTypes: Optional[Sequence[str]] = None
    DisableLogTypes: Optional[Sequence[str]] = None

class PendingCloudwatchLogsExportsTypeDef(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class RdsCustomClusterConfigurationTypeDef(BaseValidatorModel):
    InterconnectSubnetId: Optional[str] = None
    TransitGatewayMulticastDomainId: Optional[str] = None
    ReplicaMode: Optional[ReplicaModeType] = None

class ConnectionPoolConfigurationInfoTypeDef(BaseValidatorModel):
    MaxConnectionsPercent: Optional[int] = None
    MaxIdleConnectionsPercent: Optional[int] = None
    ConnectionBorrowTimeout: Optional[int] = None
    SessionPinningFilters: Optional[List[str]] = None
    InitQuery: Optional[str] = None

class ConnectionPoolConfigurationTypeDef(BaseValidatorModel):
    MaxConnectionsPercent: Optional[int] = None
    MaxIdleConnectionsPercent: Optional[int] = None
    ConnectionBorrowTimeout: Optional[int] = None
    SessionPinningFilters: Optional[Sequence[str]] = None
    InitQuery: Optional[str] = None

class ContextAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DBClusterParameterGroupTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBClusterParameterGroupArn: Optional[str] = None

class DBParameterGroupTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBParameterGroupArn: Optional[str] = None

class ScalingConfigurationTypeDef(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    AutoPause: Optional[bool] = None
    SecondsUntilAutoPause: Optional[int] = None
    TimeoutAction: Optional[str] = None
    SecondsBeforeTimeout: Optional[int] = None

class ServerlessV2ScalingConfigurationTypeDef(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class ProcessorFeatureTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class DBProxyEndpointTypeDef(BaseValidatorModel):
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

class UserAuthConfigTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    UserName: Optional[str] = None
    AuthScheme: Optional[Literal["SECRETS"]] = None
    SecretArn: Optional[str] = None
    IAMAuth: Optional[IAMAuthModeType] = None
    ClientPasswordAuthType: Optional[ClientPasswordAuthTypeType] = None

class CreateDBShardGroupMessageRequestTypeDef(BaseValidatorModel):
    DBShardGroupIdentifier: str
    DBClusterIdentifier: str
    MaxACU: float
    ComputeRedundancy: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None

class CreateGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None

class CustomDBEngineVersionAMITypeDef(BaseValidatorModel):
    ImageId: Optional[str] = None
    Status: Optional[str] = None

class RestoreWindowTypeDef(BaseValidatorModel):
    EarliestTime: Optional[datetime] = None
    LatestTime: Optional[datetime] = None

class DBClusterBacktrackTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    BacktrackIdentifier: Optional[str] = None
    BacktrackTo: Optional[datetime] = None
    BacktrackedFrom: Optional[datetime] = None
    BacktrackRequestCreationTime: Optional[datetime] = None
    Status: Optional[str] = None

class DBClusterEndpointTypeDef(BaseValidatorModel):
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

class DBClusterMemberTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None

class DBClusterOptionGroupStatusTypeDef(BaseValidatorModel):
    DBClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class ParameterOutputTypeDef(BaseValidatorModel):
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

class DBClusterRoleTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None
    FeatureName: Optional[str] = None

class DBClusterSnapshotAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class DBClusterStatusInfoTypeDef(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class DomainMembershipTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    FQDN: Optional[str] = None
    IAMRoleName: Optional[str] = None
    OU: Optional[str] = None
    AuthSecretArn: Optional[str] = None
    DnsIps: Optional[List[str]] = None

class LimitlessDatabaseTypeDef(BaseValidatorModel):
    Status: Optional[LimitlessDatabaseStatusType] = None
    MinRequiredACU: Optional[float] = None

class MasterUserSecretTypeDef(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SecretStatus: Optional[str] = None
    KmsKeyId: Optional[str] = None

class ScalingConfigurationInfoTypeDef(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    AutoPause: Optional[bool] = None
    SecondsUntilAutoPause: Optional[int] = None
    TimeoutAction: Optional[str] = None
    SecondsBeforeTimeout: Optional[int] = None

class ServerlessV2ScalingConfigurationInfoTypeDef(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class TimezoneTypeDef(BaseValidatorModel):
    TimezoneName: Optional[str] = None

class UpgradeTargetTypeDef(BaseValidatorModel):
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

class DBInstanceAutomatedBackupsReplicationTypeDef(BaseValidatorModel):
    DBInstanceAutomatedBackupsArn: Optional[str] = None

class DBInstanceRoleTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None

class DBInstanceStatusInfoTypeDef(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class DBParameterGroupStatusTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None

class DBSecurityGroupMembershipTypeDef(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None

class OptionGroupMembershipTypeDef(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class TargetHealthTypeDef(BaseValidatorModel):
    State: Optional[TargetStateType] = None
    Reason: Optional[TargetHealthReasonType] = None
    Description: Optional[str] = None

class UserAuthConfigInfoTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    UserName: Optional[str] = None
    AuthScheme: Optional[Literal["SECRETS"]] = None
    SecretArn: Optional[str] = None
    IAMAuth: Optional[IAMAuthModeType] = None
    ClientPasswordAuthType: Optional[ClientPasswordAuthTypeType] = None

class DocLinkTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    Url: Optional[str] = None

class EC2SecurityGroupTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class IPRangeTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None

class DBShardGroupTypeDef(BaseValidatorModel):
    DBShardGroupResourceId: Optional[str] = None
    DBShardGroupIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    MaxACU: Optional[float] = None
    ComputeRedundancy: Optional[int] = None
    Status: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Endpoint: Optional[str] = None

class DBSnapshotAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class DeleteBlueGreenDeploymentRequestRequestTypeDef(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: str
    DeleteTarget: Optional[bool] = None

class DeleteCustomDBEngineVersionMessageRequestTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: str

class DeleteDBClusterAutomatedBackupMessageRequestTypeDef(BaseValidatorModel):
    DbClusterResourceId: str

class DeleteDBClusterEndpointMessageRequestTypeDef(BaseValidatorModel):
    DBClusterEndpointIdentifier: str

class DeleteDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None
    DeleteAutomatedBackups: Optional[bool] = None

class DeleteDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str

class DeleteDBClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str

class DeleteDBInstanceAutomatedBackupMessageRequestTypeDef(BaseValidatorModel):
    DbiResourceId: Optional[str] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None

class DeleteDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None
    DeleteAutomatedBackups: Optional[bool] = None

class DeleteDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str

class DeleteDBProxyEndpointRequestRequestTypeDef(BaseValidatorModel):
    DBProxyEndpointName: str

class DeleteDBProxyRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str

class DeleteDBSecurityGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSecurityGroupName: str

class DeleteDBShardGroupMessageRequestTypeDef(BaseValidatorModel):
    DBShardGroupIdentifier: str

class DeleteDBSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBSnapshotIdentifier: str

class DeleteDBSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str

class DeleteGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str

class DeleteIntegrationMessageRequestTypeDef(BaseValidatorModel):
    IntegrationIdentifier: str

class DeleteOptionGroupMessageRequestTypeDef(BaseValidatorModel):
    OptionGroupName: str

class DeleteTenantDatabaseMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None

class DeregisterDBProxyTargetsRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    DBInstanceIdentifiers: Optional[Sequence[str]] = None
    DBClusterIdentifiers: Optional[Sequence[str]] = None

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDBClusterSnapshotAttributesMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeDBLogFilesDetailsTypeDef(BaseValidatorModel):
    LogFileName: Optional[str] = None
    LastWritten: Optional[int] = None
    Size: Optional[int] = None

class DescribeDBSnapshotAttributesMessageRequestTypeDef(BaseValidatorModel):
    DBSnapshotIdentifier: str

class DescribeValidDBInstanceModificationsMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str

class DisableHttpEndpointRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DoubleRangeTypeDef(BaseValidatorModel):
    From: Optional[float] = None
    To: Optional[float] = None

class DownloadDBLogFilePortionMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    LogFileName: str
    Marker: Optional[str] = None
    NumberOfLines: Optional[int] = None

class EnableHttpEndpointRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class EventCategoriesMapTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None

class EventTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None
    SourceArn: Optional[str] = None

class ExportTaskTypeDef(BaseValidatorModel):
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

class FailoverDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    TargetDBInstanceIdentifier: Optional[str] = None

class FailoverGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str
    AllowDataLoss: Optional[bool] = None
    Switchover: Optional[bool] = None

class FailoverStateTypeDef(BaseValidatorModel):
    Status: Optional[FailoverStatusType] = None
    FromDbClusterArn: Optional[str] = None
    ToDbClusterArn: Optional[str] = None
    IsDataLossAllowed: Optional[bool] = None

class GlobalClusterMemberTypeDef(BaseValidatorModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatusType] = None
    SynchronizationStatus: Optional[GlobalClusterMemberSynchronizationStatusType] = None

class IntegrationErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None

class MinimumEngineVersionPerAllowedValueTypeDef(BaseValidatorModel):
    AllowedValue: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None

class ModifyActivityStreamRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    AuditPolicyState: Optional[AuditPolicyStateType] = None

class ModifyCertificatesMessageRequestTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    RemoveCustomerOverride: Optional[bool] = None

class ModifyCurrentDBClusterCapacityMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    Capacity: Optional[int] = None
    SecondsBeforeTimeout: Optional[int] = None
    TimeoutAction: Optional[str] = None

class ModifyCustomDBEngineVersionMessageRequestTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: str
    Description: Optional[str] = None
    Status: Optional[CustomEngineVersionStatusType] = None

class ModifyDBClusterEndpointMessageRequestTypeDef(BaseValidatorModel):
    DBClusterEndpointIdentifier: str
    EndpointType: Optional[str] = None
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None

class ModifyDBClusterSnapshotAttributeMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None

class ModifyDBProxyEndpointRequestRequestTypeDef(BaseValidatorModel):
    DBProxyEndpointName: str
    NewDBProxyEndpointName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class RecommendedActionUpdateTypeDef(BaseValidatorModel):
    ActionId: str
    Status: str

class ModifyDBShardGroupMessageRequestTypeDef(BaseValidatorModel):
    DBShardGroupIdentifier: str
    MaxACU: Optional[float] = None

class ModifyDBSnapshotAttributeMessageRequestTypeDef(BaseValidatorModel):
    DBSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None

class ModifyDBSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBSnapshotIdentifier: str
    EngineVersion: Optional[str] = None
    OptionGroupName: Optional[str] = None

class ModifyDBSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: Optional[str] = None

class ModifyEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ModifyGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None

class ModifyIntegrationMessageRequestTypeDef(BaseValidatorModel):
    IntegrationIdentifier: str
    IntegrationName: Optional[str] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None

class ModifyTenantDatabaseMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    MasterUserPassword: Optional[str] = None
    NewTenantDBName: Optional[str] = None

class OptionSettingTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    IsCollection: Optional[bool] = None

class OptionVersionTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    IsDefault: Optional[bool] = None

class OutpostTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class ParameterExtraOutputTypeDef(BaseValidatorModel):
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

class ParameterTypeDef(BaseValidatorModel):
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

class PendingMaintenanceActionTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None

class PerformanceInsightsMetricDimensionGroupTypeDef(BaseValidatorModel):
    Dimensions: Optional[List[str]] = None
    Group: Optional[str] = None
    Limit: Optional[int] = None

class PromoteReadReplicaDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class PromoteReadReplicaMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None

class RangeTypeDef(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None
    Step: Optional[int] = None

class RebootDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class RebootDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None

class RebootDBShardGroupMessageRequestTypeDef(BaseValidatorModel):
    DBShardGroupIdentifier: str

class RecommendedActionParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class ScalarReferenceDetailsTypeDef(BaseValidatorModel):
    Value: Optional[float] = None

class RegisterDBProxyTargetsRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    DBInstanceIdentifiers: Optional[Sequence[str]] = None
    DBClusterIdentifiers: Optional[Sequence[str]] = None

class RemoveFromGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None

class RemoveRoleFromDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class RemoveRoleFromDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    RoleArn: str
    FeatureName: str

class RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str

class RemoveTagsFromResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]

class RevokeDBSecurityGroupIngressMessageRequestTypeDef(BaseValidatorModel):
    DBSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class SourceRegionTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None
    Endpoint: Optional[str] = None
    Status: Optional[str] = None
    SupportsDBInstanceAutomatedBackupsReplication: Optional[bool] = None

class StartActivityStreamRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Mode: ActivityStreamModeType
    KmsKeyId: str
    ApplyImmediately: Optional[bool] = None
    EngineNativeAuditFieldsIncluded: Optional[bool] = None

class StartDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef(BaseValidatorModel):
    SourceDBInstanceArn: str
    BackupRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    SourceRegion: Optional[str] = None

class StartDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str

class StartExportTaskMessageRequestTypeDef(BaseValidatorModel):
    ExportTaskIdentifier: str
    SourceArn: str
    S3BucketName: str
    IamRoleArn: str
    KmsKeyId: str
    S3Prefix: Optional[str] = None
    ExportOnly: Optional[Sequence[str]] = None

class StopActivityStreamRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ApplyImmediately: Optional[bool] = None

class StopDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef(BaseValidatorModel):
    SourceDBInstanceArn: str

class StopDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBSnapshotIdentifier: Optional[str] = None

class SwitchoverBlueGreenDeploymentRequestRequestTypeDef(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: str
    SwitchoverTimeout: Optional[int] = None

class SwitchoverGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str

class SwitchoverReadReplicaMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str

class TenantDatabasePendingModifiedValuesTypeDef(BaseValidatorModel):
    MasterUserPassword: Optional[str] = None
    TenantDBName: Optional[str] = None

class AccountAttributesMessageTypeDef(BaseValidatorModel):
    AccountQuotas: List[AccountQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterBacktrackResponseTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: str
    BacktrackTo: datetime
    BacktrackedFrom: datetime
    BacktrackRequestCreationTime: datetime
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterCapacityInfoTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    PendingCapacity: int
    CurrentCapacity: int
    SecondsBeforeTimeout: int
    TimeoutAction: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterEndpointResponseTypeDef(BaseValidatorModel):
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

class DBClusterParameterGroupNameMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupNameMessageTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBShardGroupResponseTypeDef(BaseValidatorModel):
    DBShardGroupResourceId: str
    DBShardGroupIdentifier: str
    DBClusterIdentifier: str
    MaxACU: float
    ComputeRedundancy: int
    Status: str
    PubliclyAccessible: bool
    Endpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableHttpEndpointResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    HttpEndpointEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DownloadDBLogFilePortionDetailsTypeDef(BaseValidatorModel):
    LogFileData: str
    Marker: str
    AdditionalDataPending: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableHttpEndpointResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    HttpEndpointEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTaskResponseTypeDef(BaseValidatorModel):
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

class ModifyActivityStreamResponseTypeDef(BaseValidatorModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    Mode: ActivityStreamModeType
    EngineNativeAuditFieldsIncluded: bool
    PolicyStatus: ActivityStreamPolicyStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartActivityStreamResponseTypeDef(BaseValidatorModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    Mode: ActivityStreamModeType
    ApplyImmediately: bool
    EngineNativeAuditFieldsIncluded: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StopActivityStreamResponseTypeDef(BaseValidatorModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AddSourceIdentifierToSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSourceIdentifierFromSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopyDBClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SourceRegion: Optional[str] = None

class CopyDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopyDBSnapshotMessageRequestTypeDef(BaseValidatorModel):
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

class CopyOptionGroupMessageRequestTypeDef(BaseValidatorModel):
    SourceOptionGroupIdentifier: str
    TargetOptionGroupIdentifier: str
    TargetOptionGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateBlueGreenDeploymentRequestRequestTypeDef(BaseValidatorModel):
    BlueGreenDeploymentName: str
    Source: str
    TargetEngineVersion: Optional[str] = None
    TargetDBParameterGroupName: Optional[str] = None
    TargetDBClusterParameterGroupName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TargetDBInstanceClass: Optional[str] = None
    UpgradeTargetStorageConfig: Optional[bool] = None

class CreateCustomDBEngineVersionMessageRequestTypeDef(BaseValidatorModel):
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

class CreateDBClusterEndpointMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBProxyEndpointRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str
    DBProxyEndpointName: str
    VpcSubnetIds: Sequence[str]
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    TargetRole: Optional[DBProxyEndpointTargetRoleType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSecurityGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSecurityGroupName: str
    DBSecurityGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBSnapshotIdentifier: str
    DBInstanceIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateIntegrationMessageRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None

class CreateOptionGroupMessageRequestTypeDef(BaseValidatorModel):
    OptionGroupName: str
    EngineName: str
    MajorEngineVersion: str
    OptionGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTenantDatabaseMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    MasterUsername: str
    MasterUserPassword: str
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DBClusterSnapshotTypeDef(BaseValidatorModel):
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

class DBSnapshotTenantDatabaseTypeDef(BaseValidatorModel):
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

class PurchaseReservedDBInstancesOfferingMessageRequestTypeDef(BaseValidatorModel):
    ReservedDBInstancesOfferingId: str
    ReservedDBInstanceId: Optional[str] = None
    DBInstanceCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagListMessageTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionTypeDef(BaseValidatorModel):
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

class BacktrackDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackTo: TimestampTypeDef
    Force: Optional[bool] = None
    UseEarliestTimeOnPointInTimeUnavailable: Optional[bool] = None

class BlueGreenDeploymentTypeDef(BaseValidatorModel):
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

class CertificateMessageTypeDef(BaseValidatorModel):
    DefaultCertificateForNewLaunches: str
    Certificates: List[CertificateTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCertificatesResultTypeDef(BaseValidatorModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterPendingModifiedValuesTypeDef(BaseValidatorModel):
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

class DBProxyTargetGroupTypeDef(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    TargetGroupName: Optional[str] = None
    TargetGroupArn: Optional[str] = None
    IsDefault: Optional[bool] = None
    Status: Optional[str] = None
    ConnectionPoolConfig: Optional[ConnectionPoolConfigurationInfoTypeDef] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None

class ModifyDBProxyTargetGroupRequestRequestTypeDef(BaseValidatorModel):
    TargetGroupName: str
    DBProxyName: str
    ConnectionPoolConfig: Optional[ConnectionPoolConfigurationTypeDef] = None
    NewName: Optional[str] = None

class CopyDBClusterParameterGroupResultTypeDef(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterParameterGroupResultTypeDef(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupsMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBParameterGroupResultTypeDef(BaseValidatorModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBParameterGroupResultTypeDef(BaseValidatorModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupsMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBParameterGroups: List[DBParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterMessageRequestTypeDef(BaseValidatorModel):
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

class ModifyDBClusterMessageRequestTypeDef(BaseValidatorModel):
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

class RestoreDBClusterFromS3MessageRequestTypeDef(BaseValidatorModel):
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

class RestoreDBClusterFromSnapshotMessageRequestTypeDef(BaseValidatorModel):
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

class RestoreDBClusterToPointInTimeMessageRequestTypeDef(BaseValidatorModel):
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

class CreateDBInstanceMessageRequestTypeDef(BaseValidatorModel):
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

class CreateDBInstanceReadReplicaMessageRequestTypeDef(BaseValidatorModel):
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

class DBSnapshotTypeDef(BaseValidatorModel):
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

class ModifyDBInstanceMessageRequestTypeDef(BaseValidatorModel):
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

class PendingModifiedValuesTypeDef(BaseValidatorModel):
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

class RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef(BaseValidatorModel):
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

class RestoreDBInstanceFromS3MessageRequestTypeDef(BaseValidatorModel):
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

class RestoreDBInstanceToPointInTimeMessageRequestTypeDef(BaseValidatorModel):
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

class CreateDBProxyEndpointResponseTypeDef(BaseValidatorModel):
    DBProxyEndpoint: DBProxyEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBProxyEndpointResponseTypeDef(BaseValidatorModel):
    DBProxyEndpoint: DBProxyEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBProxyEndpointsResponseTypeDef(BaseValidatorModel):
    DBProxyEndpoints: List[DBProxyEndpointTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBProxyEndpointResponseTypeDef(BaseValidatorModel):
    DBProxyEndpoint: DBProxyEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBProxyRequestRequestTypeDef(BaseValidatorModel):
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

class ModifyDBProxyRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str
    NewDBProxyName: Optional[str] = None
    Auth: Optional[Sequence[UserAuthConfigTypeDef]] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    RoleArn: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None

class DBClusterAutomatedBackupTypeDef(BaseValidatorModel):
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

class DBClusterBacktrackMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterBacktracks: List[DBClusterBacktrackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterEndpointMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupDetailsTypeDef(BaseValidatorModel):
    Parameters: List[ParameterOutputTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupDetailsTypeDef(BaseValidatorModel):
    Parameters: List[ParameterOutputTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterOutputTypeDef]] = None

class DBClusterSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttributeTypeDef]] = None

class DBEngineVersionResponseTypeDef(BaseValidatorModel):
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

class DBEngineVersionTypeDef(BaseValidatorModel):
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

class DBInstanceAutomatedBackupTypeDef(BaseValidatorModel):
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

class DBProxyTargetTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    Endpoint: Optional[str] = None
    TrackedClusterId: Optional[str] = None
    RdsResourceId: Optional[str] = None
    Port: Optional[int] = None
    Type: Optional[TargetTypeType] = None
    Role: Optional[TargetRoleType] = None
    TargetHealth: Optional[TargetHealthTypeDef] = None

class DBProxyTypeDef(BaseValidatorModel):
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

class DBSecurityGroupTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    DBSecurityGroupName: Optional[str] = None
    DBSecurityGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroupTypeDef]] = None
    IPRanges: Optional[List[IPRangeTypeDef]] = None
    DBSecurityGroupArn: Optional[str] = None

class DescribeDBShardGroupsResponseTypeDef(BaseValidatorModel):
    DBShardGroups: List[DBShardGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBSnapshotIdentifier: Optional[str] = None
    DBSnapshotAttributes: Optional[List[DBSnapshotAttributeTypeDef]] = None

class DescribeBlueGreenDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeCertificatesMessageRequestTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterAutomatedBackupsMessageRequestTypeDef(BaseValidatorModel):
    DbClusterResourceId: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterBacktracksMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterEndpointsMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParameterGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParametersMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterSnapshotsMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None

class DescribeDBClustersMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None

class DescribeDBEngineVersionsMessageRequestTypeDef(BaseValidatorModel):
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

class DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef(BaseValidatorModel):
    DbiResourceId: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None

class DescribeDBInstancesMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBLogFilesMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    FilenameContains: Optional[str] = None
    FileLastWritten: Optional[int] = None
    FileSize: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParameterGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParametersMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBProxiesRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBProxyEndpointsRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    DBProxyEndpointName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBProxyTargetGroupsRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBProxyTargetsRequestRequestTypeDef(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBRecommendationsMessageRequestTypeDef(BaseValidatorModel):
    LastUpdatedAfter: Optional[TimestampTypeDef] = None
    LastUpdatedBefore: Optional[TimestampTypeDef] = None
    Locale: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBSecurityGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBShardGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBShardGroupIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DbiResourceId: Optional[str] = None

class DescribeDBSnapshotsMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None

class DescribeDBSubnetGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultClusterParametersMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultParametersMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventCategoriesMessageRequestTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeEventSubscriptionsMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventsMessageRequestTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeExportTasksMessageRequestTypeDef(BaseValidatorModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    SourceType: Optional[ExportSourceTypeType] = None

class DescribeGlobalClustersMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeIntegrationsMessageRequestTypeDef(BaseValidatorModel):
    IntegrationIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeOptionGroupOptionsMessageRequestTypeDef(BaseValidatorModel):
    EngineName: str
    MajorEngineVersion: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeOptionGroupsMessageRequestTypeDef(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None

class DescribeOrderableDBInstanceOptionsMessageRequestTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePendingMaintenanceActionsMessageRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeReservedDBInstancesMessageRequestTypeDef(BaseValidatorModel):
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

class DescribeReservedDBInstancesOfferingsMessageRequestTypeDef(BaseValidatorModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeSourceRegionsMessageRequestTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeTenantDatabasesMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class ListTagsForResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateTypeDef(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    IncludeAll: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateTypeDef(BaseValidatorModel):
    DbiResourceId: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBLogFilesMessageDescribeDBLogFilesPaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    FilenameContains: Optional[str] = None
    FileLastWritten: Optional[int] = None
    FileSize: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxiesRequestDescribeDBProxiesPaginateTypeDef(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateTypeDef(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    DBProxyEndpointName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateTypeDef(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateTypeDef(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBRecommendationsMessageDescribeDBRecommendationsPaginateTypeDef(BaseValidatorModel):
    LastUpdatedAfter: Optional[TimestampTypeDef] = None
    LastUpdatedBefore: Optional[TimestampTypeDef] = None
    Locale: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateTypeDef(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportTasksMessageDescribeExportTasksPaginateTypeDef(BaseValidatorModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SourceType: Optional[ExportSourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIntegrationsMessageDescribeIntegrationsPaginateTypeDef(BaseValidatorModel):
    IntegrationIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateTypeDef(BaseValidatorModel):
    EngineName: str
    MajorEngineVersion: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOptionGroupsMessageDescribeOptionGroupsPaginateTypeDef(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateTypeDef(BaseValidatorModel):
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

class DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateTypeDef(BaseValidatorModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSourceRegionsMessageDescribeSourceRegionsPaginateTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTenantDatabasesMessageDescribeTenantDatabasesPaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    LogFileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitTypeDef(BaseValidatorModel):
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

class DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitTypeDef(BaseValidatorModel):
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

class DescribeDBClustersMessageDBClusterAvailableWaitTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBClustersMessageDBClusterDeletedWaitTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBSnapshotsMessageDBSnapshotAvailableWaitTypeDef(BaseValidatorModel):
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

class DescribeDBSnapshotsMessageDBSnapshotCompletedWaitTypeDef(BaseValidatorModel):
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

class DescribeDBSnapshotsMessageDBSnapshotDeletedWaitTypeDef(BaseValidatorModel):
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

class DescribeTenantDatabasesMessageTenantDatabaseAvailableWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTenantDatabasesMessageTenantDatabaseDeletedWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBLogFilesResponseTypeDef(BaseValidatorModel):
    DescribeDBLogFiles: List[DescribeDBLogFilesDetailsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMessageTypeDef(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventsMessageTypeDef(BaseValidatorModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTasksMessageTypeDef(BaseValidatorModel):
    Marker: str
    ExportTasks: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClusterTypeDef(BaseValidatorModel):
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

class IntegrationResponseTypeDef(BaseValidatorModel):
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

class IntegrationTypeDef(BaseValidatorModel):
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

class OptionGroupOptionSettingTypeDef(BaseValidatorModel):
    SettingName: Optional[str] = None
    SettingDescription: Optional[str] = None
    DefaultValue: Optional[str] = None
    ApplyType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    MinimumEngineVersionPerAllowedValue: Optional[       List[MinimumEngineVersionPerAllowedValueTypeDef]     ] = None

class ModifyDBRecommendationMessageRequestTypeDef(BaseValidatorModel):
    RecommendationId: str
    Locale: Optional[str] = None
    Status: Optional[str] = None
    RecommendedActionUpdates: Optional[Sequence[RecommendedActionUpdateTypeDef]] = None

class OptionConfigurationTypeDef(BaseValidatorModel):
    OptionName: str
    Port: Optional[int] = None
    OptionVersion: Optional[str] = None
    DBSecurityGroupMemberships: Optional[Sequence[str]] = None
    VpcSecurityGroupMemberships: Optional[Sequence[str]] = None
    OptionSettings: Optional[Sequence[OptionSettingTypeDef]] = None

class OptionTypeDef(BaseValidatorModel):
    OptionName: Optional[str] = None
    OptionDescription: Optional[str] = None
    Persistent: Optional[bool] = None
    Permanent: Optional[bool] = None
    Port: Optional[int] = None
    OptionVersion: Optional[str] = None
    OptionSettings: Optional[List[OptionSettingTypeDef]] = None
    DBSecurityGroupMemberships: Optional[List[DBSecurityGroupMembershipTypeDef]] = None
    VpcSecurityGroupMemberships: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None

class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetOutpost: Optional[OutpostTypeDef] = None
    SubnetStatus: Optional[str] = None

class ResourcePendingMaintenanceActionsTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None

class PerformanceInsightsMetricQueryTypeDef(BaseValidatorModel):
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroupTypeDef] = None
    Metric: Optional[str] = None

class ValidStorageOptionsTypeDef(BaseValidatorModel):
    StorageType: Optional[str] = None
    StorageSize: Optional[List[RangeTypeDef]] = None
    ProvisionedIops: Optional[List[RangeTypeDef]] = None
    IopsToStorageRatio: Optional[List[DoubleRangeTypeDef]] = None
    SupportsStorageAutoscaling: Optional[bool] = None
    ProvisionedStorageThroughput: Optional[List[RangeTypeDef]] = None
    StorageThroughputToIopsRatio: Optional[List[DoubleRangeTypeDef]] = None

class ReservedDBInstanceTypeDef(BaseValidatorModel):
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

class ReservedDBInstancesOfferingTypeDef(BaseValidatorModel):
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

class ReferenceDetailsTypeDef(BaseValidatorModel):
    ScalarReferenceDetails: Optional[ScalarReferenceDetailsTypeDef] = None

class SourceRegionMessageTypeDef(BaseValidatorModel):
    Marker: str
    SourceRegions: List[SourceRegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TenantDatabaseTypeDef(BaseValidatorModel):
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

class CopyDBClusterSnapshotResultTypeDef(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterSnapshotResultTypeDef(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterSnapshotMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterSnapshotResultTypeDef(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBSnapshotTenantDatabasesMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBSnapshotTenantDatabases: List[DBSnapshotTenantDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionsMessageTypeDef(BaseValidatorModel):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBlueGreenDeploymentResponseTypeDef(BaseValidatorModel):
    BlueGreenDeployment: BlueGreenDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBlueGreenDeploymentResponseTypeDef(BaseValidatorModel):
    BlueGreenDeployment: BlueGreenDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBlueGreenDeploymentsResponseTypeDef(BaseValidatorModel):
    BlueGreenDeployments: List[BlueGreenDeploymentTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverBlueGreenDeploymentResponseTypeDef(BaseValidatorModel):
    BlueGreenDeployment: BlueGreenDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterTypeDef(BaseValidatorModel):
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

class DescribeDBProxyTargetGroupsResponseTypeDef(BaseValidatorModel):
    TargetGroups: List[DBProxyTargetGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBProxyTargetGroupResponseTypeDef(BaseValidatorModel):
    DBProxyTargetGroup: DBProxyTargetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBSnapshotResultTypeDef(BaseValidatorModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSnapshotResultTypeDef(BaseValidatorModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBSnapshotMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBSnapshots: List[DBSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBSnapshotResultTypeDef(BaseValidatorModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSnapshotResultTypeDef(BaseValidatorModel):
    DBSnapshot: DBSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterAutomatedBackupMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterAutomatedBackups: List[DBClusterAutomatedBackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterAutomatedBackupResultTypeDef(BaseValidatorModel):
    DBClusterAutomatedBackup: DBClusterAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultClusterParametersResultTypeDef(BaseValidatorModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(BaseValidatorModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBClusterSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterSnapshotAttributeResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBEngineVersionMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceAutomatedBackupMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBInstanceAutomatedBackups: List[DBInstanceAutomatedBackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBInstanceAutomatedBackupResultTypeDef(BaseValidatorModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBInstanceAutomatedBackupsReplicationResultTypeDef(BaseValidatorModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBInstanceAutomatedBackupsReplicationResultTypeDef(BaseValidatorModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBProxyTargetsResponseTypeDef(BaseValidatorModel):
    Targets: List[DBProxyTargetTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDBProxyTargetsResponseTypeDef(BaseValidatorModel):
    DBProxyTargets: List[DBProxyTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBProxyResponseTypeDef(BaseValidatorModel):
    DBProxy: DBProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBProxyResponseTypeDef(BaseValidatorModel):
    DBProxy: DBProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBProxiesResponseTypeDef(BaseValidatorModel):
    DBProxies: List[DBProxyTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBProxyResponseTypeDef(BaseValidatorModel):
    DBProxy: DBProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeDBSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    DBSecurityGroup: DBSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSecurityGroupResultTypeDef(BaseValidatorModel):
    DBSecurityGroup: DBSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBSecurityGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBSecurityGroups: List[DBSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeDBSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    DBSecurityGroup: DBSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBSnapshotAttributesResult: DBSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSnapshotAttributeResultTypeDef(BaseValidatorModel):
    DBSnapshotAttributesResult: DBSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClustersMessageTypeDef(BaseValidatorModel):
    Marker: str
    GlobalClusters: List[GlobalClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFromGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIntegrationsResponseTypeDef(BaseValidatorModel):
    Marker: str
    Integrations: List[IntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OptionGroupOptionTypeDef(BaseValidatorModel):
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

class ModifyOptionGroupMessageRequestTypeDef(BaseValidatorModel):
    OptionGroupName: str
    OptionsToInclude: Optional[Sequence[OptionConfigurationTypeDef]] = None
    OptionsToRemove: Optional[Sequence[str]] = None
    ApplyImmediately: Optional[bool] = None

class OptionGroupTypeDef(BaseValidatorModel):
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

class DBSubnetGroupTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    DBSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    DBSubnetGroupArn: Optional[str] = None
    SupportedNetworkTypes: Optional[List[str]] = None

class ModifyDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Parameters: Sequence[ParameterUnionTypeDef]

class ModifyDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    Parameters: Sequence[ParameterUnionTypeDef]

class ResetDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterUnionTypeDef]] = None

class ResetDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterUnionTypeDef]] = None

class ApplyPendingMaintenanceActionResultTypeDef(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingMaintenanceActionsMessageTypeDef(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricQueryTypeDef(BaseValidatorModel):
    PerformanceInsightsMetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None

class ValidDBInstanceModificationsMessageTypeDef(BaseValidatorModel):
    Storage: Optional[List[ValidStorageOptionsTypeDef]] = None
    ValidProcessorFeatures: Optional[List[AvailableProcessorFeatureTypeDef]] = None
    SupportsDedicatedLogVolume: Optional[bool] = None

class PurchaseReservedDBInstancesOfferingResultTypeDef(BaseValidatorModel):
    ReservedDBInstance: ReservedDBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedDBInstanceMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedDBInstances: List[ReservedDBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedDBInstancesOfferingMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedDBInstancesOfferings: List[ReservedDBInstancesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ReferenceDetails: Optional[ReferenceDetailsTypeDef] = None

class CreateTenantDatabaseResultTypeDef(BaseValidatorModel):
    TenantDatabase: TenantDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTenantDatabaseResultTypeDef(BaseValidatorModel):
    TenantDatabase: TenantDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTenantDatabaseResultTypeDef(BaseValidatorModel):
    TenantDatabase: TenantDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TenantDatabasesMessageTypeDef(BaseValidatorModel):
    Marker: str
    TenantDatabases: List[TenantDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusters: List[DBClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteReadReplicaDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterFromS3ResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterFromSnapshotResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterToPointInTimeResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OptionGroupOptionsMessageTypeDef(BaseValidatorModel):
    OptionGroupOptions: List[OptionGroupOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopyOptionGroupResultTypeDef(BaseValidatorModel):
    OptionGroup: OptionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOptionGroupResultTypeDef(BaseValidatorModel):
    OptionGroup: OptionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyOptionGroupResultTypeDef(BaseValidatorModel):
    OptionGroup: OptionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OptionGroupsTypeDef(BaseValidatorModel):
    OptionGroupsList: List[OptionGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSubnetGroupResultTypeDef(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceTypeDef(BaseValidatorModel):
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

class DBSubnetGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSubnetGroupResultTypeDef(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeValidDBInstanceModificationsResultTypeDef(BaseValidatorModel):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MetricTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    References: Optional[List[MetricReferenceTypeDef]] = None
    StatisticsDetails: Optional[str] = None
    MetricQuery: Optional[MetricQueryTypeDef] = None

class CreateDBInstanceReadReplicaResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBInstances: List[DBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteReadReplicaResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBInstanceFromDBSnapshotResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBInstanceFromS3ResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBInstanceToPointInTimeResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverReadReplicaResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceIssueDetailsTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Metrics: Optional[List[MetricTypeDef]] = None
    Analysis: Optional[str] = None

class IssueDetailsTypeDef(BaseValidatorModel):
    PerformanceIssueDetails: Optional[PerformanceIssueDetailsTypeDef] = None

class RecommendedActionTypeDef(BaseValidatorModel):
    ActionId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Operation: Optional[str] = None
    Parameters: Optional[List[RecommendedActionParameterTypeDef]] = None
    ApplyModes: Optional[List[str]] = None
    Status: Optional[str] = None
    IssueDetails: Optional[IssueDetailsTypeDef] = None
    ContextAttributes: Optional[List[ContextAttributeTypeDef]] = None

class DBRecommendationTypeDef(BaseValidatorModel):
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

class DBRecommendationMessageTypeDef(BaseValidatorModel):
    DBRecommendation: DBRecommendationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBRecommendationsMessageTypeDef(BaseValidatorModel):
    DBRecommendations: List[DBRecommendationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

