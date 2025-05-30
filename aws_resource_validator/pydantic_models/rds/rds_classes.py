from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.rds.rds_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountQuota(BaseValidatorModel):
    AccountQuotaName: Optional[str] = None
    Used: Optional[int] = None
    Max: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'add_role_to_db_cluster' function.
class AddRoleToDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None


# This class is the input for the 'add_role_to_db_instance' function.
class AddRoleToDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    RoleArn: str
    FeatureName: str


# This class is the input for the 'add_source_identifier_to_subscription' function.
class AddSourceIdentifierToSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


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
    EventSubscriptionArn: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'apply_pending_maintenance_action' function.
class ApplyPendingMaintenanceActionMessage(BaseValidatorModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str


# This class is the input for the 'authorize_db_security_group_ingress' function.
class AuthorizeDBSecurityGroupIngressMessage(BaseValidatorModel):
    DBSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class AvailableProcessorFeature(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[str] = None

Timestamp = Union[datetime, str]


class BlueGreenDeploymentTask(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None


class SwitchoverDetail(BaseValidatorModel):
    SourceMember: Optional[str] = None
    TargetMember: Optional[str] = None
    Status: Optional[str] = None


# This class is the input for the 'cancel_export_task' function.
class CancelExportTaskMessage(BaseValidatorModel):
    ExportTaskIdentifier: str


class CertificateDetails(BaseValidatorModel):
    CAIdentifier: Optional[str] = None
    ValidTill: Optional[datetime] = None


class Certificate(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    CertificateType: Optional[str] = None
    Thumbprint: Optional[str] = None
    ValidFrom: Optional[datetime] = None
    ValidTill: Optional[datetime] = None
    CertificateArn: Optional[str] = None
    CustomerOverride: Optional[bool] = None
    CustomerOverrideValidTill: Optional[datetime] = None


class CharacterSet(BaseValidatorModel):
    CharacterSetName: Optional[str] = None
    CharacterSetDescription: Optional[str] = None


class ClientGenerateDbAuthTokenRequest(BaseValidatorModel):
    DBHostname: str
    Port: int
    DBUsername: str
    Region: Optional[str] = None


class CloudwatchLogsExportConfiguration(BaseValidatorModel):
    EnableLogTypes: Optional[List[str]] = None
    DisableLogTypes: Optional[List[str]] = None


class PendingCloudwatchLogsExports(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


class RdsCustomClusterConfiguration(BaseValidatorModel):
    InterconnectSubnetId: Optional[str] = None
    TransitGatewayMulticastDomainId: Optional[str] = None
    ReplicaMode: Optional[ReplicaModeType] = None


class ConnectionPoolConfigurationInfo(BaseValidatorModel):
    MaxConnectionsPercent: Optional[int] = None
    MaxIdleConnectionsPercent: Optional[int] = None
    ConnectionBorrowTimeout: Optional[int] = None
    SessionPinningFilters: Optional[List[str]] = None
    InitQuery: Optional[str] = None


class ConnectionPoolConfiguration(BaseValidatorModel):
    MaxConnectionsPercent: Optional[int] = None
    MaxIdleConnectionsPercent: Optional[int] = None
    ConnectionBorrowTimeout: Optional[int] = None
    SessionPinningFilters: Optional[List[str]] = None
    InitQuery: Optional[str] = None


class ContextAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DBClusterParameterGroup(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBClusterParameterGroupArn: Optional[str] = None


class DBParameterGroup(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBParameterGroupArn: Optional[str] = None


class ScalingConfiguration(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    AutoPause: Optional[bool] = None
    SecondsUntilAutoPause: Optional[int] = None
    TimeoutAction: Optional[str] = None
    SecondsBeforeTimeout: Optional[int] = None


class ServerlessV2ScalingConfiguration(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None
    SecondsUntilAutoPause: Optional[int] = None


class ProcessorFeature(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class DBProxyEndpoint(BaseValidatorModel):
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


class UserAuthConfig(BaseValidatorModel):
    Description: Optional[str] = None
    UserName: Optional[str] = None
    AuthScheme: Optional[Literal['SECRETS']] = None
    SecretArn: Optional[str] = None
    IAMAuth: Optional[IAMAuthModeType] = None
    ClientPasswordAuthType: Optional[ClientPasswordAuthTypeType] = None


class CustomDBEngineVersionAMI(BaseValidatorModel):
    ImageId: Optional[str] = None
    Status: Optional[str] = None


class RestoreWindow(BaseValidatorModel):
    EarliestTime: Optional[datetime] = None
    LatestTime: Optional[datetime] = None


class DBClusterBacktrack(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    BacktrackIdentifier: Optional[str] = None
    BacktrackTo: Optional[datetime] = None
    BacktrackedFrom: Optional[datetime] = None
    BacktrackRequestCreationTime: Optional[datetime] = None
    Status: Optional[str] = None


class DBClusterEndpoint(BaseValidatorModel):
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


class DBClusterMember(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None


class DBClusterOptionGroupStatus(BaseValidatorModel):
    DBClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None


class ParameterOutput(BaseValidatorModel):
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


class DBClusterRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None
    FeatureName: Optional[str] = None


class DBClusterSnapshotAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class DBClusterStatusInfo(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class DomainMembership(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    FQDN: Optional[str] = None
    IAMRoleName: Optional[str] = None
    OU: Optional[str] = None
    AuthSecretArn: Optional[str] = None
    DnsIps: Optional[List[str]] = None


class LimitlessDatabase(BaseValidatorModel):
    Status: Optional[LimitlessDatabaseStatusType] = None
    MinRequiredACU: Optional[float] = None


class MasterUserSecret(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SecretStatus: Optional[str] = None
    KmsKeyId: Optional[str] = None


class ScalingConfigurationInfo(BaseValidatorModel):
    MinCapacity: Optional[int] = None
    MaxCapacity: Optional[int] = None
    AutoPause: Optional[bool] = None
    SecondsUntilAutoPause: Optional[int] = None
    TimeoutAction: Optional[str] = None
    SecondsBeforeTimeout: Optional[int] = None


class ServerlessV2ScalingConfigurationInfo(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None
    SecondsUntilAutoPause: Optional[int] = None


class VpcSecurityGroupMembership(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class ServerlessV2FeaturesSupport(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None


class Timezone(BaseValidatorModel):
    TimezoneName: Optional[str] = None


class UpgradeTarget(BaseValidatorModel):
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


class DBInstanceAutomatedBackupsReplication(BaseValidatorModel):
    DBInstanceAutomatedBackupsArn: Optional[str] = None


class DBInstanceRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None


class DBInstanceStatusInfo(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class DBParameterGroupStatus(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None


class DBSecurityGroupMembership(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None


class OptionGroupMembership(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None


class TargetHealth(BaseValidatorModel):
    State: Optional[TargetStateType] = None
    Reason: Optional[TargetHealthReasonType] = None
    Description: Optional[str] = None


class UserAuthConfigInfo(BaseValidatorModel):
    Description: Optional[str] = None
    UserName: Optional[str] = None
    AuthScheme: Optional[Literal['SECRETS']] = None
    SecretArn: Optional[str] = None
    IAMAuth: Optional[IAMAuthModeType] = None
    ClientPasswordAuthType: Optional[ClientPasswordAuthTypeType] = None


class DocLink(BaseValidatorModel):
    Text: Optional[str] = None
    Url: Optional[str] = None


class EC2SecurityGroup(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class IPRange(BaseValidatorModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None


class DBSnapshotAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


# This class is the input for the 'delete_blue_green_deployment' function.
class DeleteBlueGreenDeploymentRequest(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: str
    DeleteTarget: Optional[bool] = None


# This class is the input for the 'delete_custom_db_engine_version' function.
class DeleteCustomDBEngineVersionMessage(BaseValidatorModel):
    Engine: str
    EngineVersion: str


# This class is the input for the 'delete_db_cluster_automated_backup' function.
class DeleteDBClusterAutomatedBackupMessage(BaseValidatorModel):
    DbClusterResourceId: str


# This class is the input for the 'delete_db_cluster_endpoint' function.
class DeleteDBClusterEndpointMessage(BaseValidatorModel):
    DBClusterEndpointIdentifier: str


# This class is the input for the 'delete_db_cluster' function.
class DeleteDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None
    DeleteAutomatedBackups: Optional[bool] = None


# This class is the input for the 'delete_db_cluster_parameter_group' function.
class DeleteDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str


# This class is the input for the 'delete_db_cluster_snapshot' function.
class DeleteDBClusterSnapshotMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


# This class is the input for the 'delete_db_instance_automated_backup' function.
class DeleteDBInstanceAutomatedBackupMessage(BaseValidatorModel):
    DbiResourceId: Optional[str] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None


# This class is the input for the 'delete_db_instance' function.
class DeleteDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None
    DeleteAutomatedBackups: Optional[bool] = None


# This class is the input for the 'delete_db_parameter_group' function.
class DeleteDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str


# This class is the input for the 'delete_db_proxy_endpoint' function.
class DeleteDBProxyEndpointRequest(BaseValidatorModel):
    DBProxyEndpointName: str


# This class is the input for the 'delete_db_proxy' function.
class DeleteDBProxyRequest(BaseValidatorModel):
    DBProxyName: str


# This class is the input for the 'delete_db_security_group' function.
class DeleteDBSecurityGroupMessage(BaseValidatorModel):
    DBSecurityGroupName: str


# This class is the input for the 'delete_db_shard_group' function.
class DeleteDBShardGroupMessage(BaseValidatorModel):
    DBShardGroupIdentifier: str


# This class is the input for the 'delete_db_snapshot' function.
class DeleteDBSnapshotMessage(BaseValidatorModel):
    DBSnapshotIdentifier: str


# This class is the input for the 'delete_db_subnet_group' function.
class DeleteDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str


# This class is the input for the 'delete_event_subscription' function.
class DeleteEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str


# This class is the input for the 'delete_global_cluster' function.
class DeleteGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str


# This class is the input for the 'delete_integration' function.
class DeleteIntegrationMessage(BaseValidatorModel):
    IntegrationIdentifier: str


# This class is the input for the 'delete_option_group' function.
class DeleteOptionGroupMessage(BaseValidatorModel):
    OptionGroupName: str


# This class is the input for the 'delete_tenant_database' function.
class DeleteTenantDatabaseMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None


class DeregisterDBProxyTargetsRequest(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    DBInstanceIdentifiers: Optional[List[str]] = None
    DBClusterIdentifiers: Optional[List[str]] = None


class Filter(BaseValidatorModel):
    Name: str
    Values: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_db_cluster_snapshot_attributes' function.
class DescribeDBClusterSnapshotAttributesMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeDBLogFilesDetails(BaseValidatorModel):
    LogFileName: Optional[str] = None
    LastWritten: Optional[int] = None
    Size: Optional[int] = None


# This class is the input for the 'describe_db_snapshot_attributes' function.
class DescribeDBSnapshotAttributesMessage(BaseValidatorModel):
    DBSnapshotIdentifier: str


# This class is the input for the 'describe_valid_db_instance_modifications' function.
class DescribeValidDBInstanceModificationsMessage(BaseValidatorModel):
    DBInstanceIdentifier: str


# This class is the input for the 'disable_http_endpoint' function.
class DisableHttpEndpointRequest(BaseValidatorModel):
    ResourceArn: str


class DoubleRange(BaseValidatorModel):
    From: Optional[float] = None
    To: Optional[float] = None


# This class is the input for the 'download_db_log_file_portion' function.
class DownloadDBLogFilePortionMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    LogFileName: str
    Marker: Optional[str] = None
    NumberOfLines: Optional[int] = None


# This class is the input for the 'enable_http_endpoint' function.
class EnableHttpEndpointRequest(BaseValidatorModel):
    ResourceArn: str


class EventCategoriesMap(BaseValidatorModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None
    SourceArn: Optional[str] = None


class ExportTask(BaseValidatorModel):
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


# This class is the input for the 'failover_db_cluster' function.
class FailoverDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    TargetDBInstanceIdentifier: Optional[str] = None


# This class is the input for the 'failover_global_cluster' function.
class FailoverGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str
    AllowDataLoss: Optional[bool] = None
    Switchover: Optional[bool] = None


class FailoverState(BaseValidatorModel):
    Status: Optional[FailoverStatusType] = None
    FromDbClusterArn: Optional[str] = None
    ToDbClusterArn: Optional[str] = None
    IsDataLossAllowed: Optional[bool] = None


class GlobalClusterMember(BaseValidatorModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatusType] = None
    SynchronizationStatus: Optional[GlobalClusterMemberSynchronizationStatusType] = None


class IntegrationError(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None


class MinimumEngineVersionPerAllowedValue(BaseValidatorModel):
    AllowedValue: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None


# This class is the input for the 'modify_activity_stream' function.
class ModifyActivityStreamRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    AuditPolicyState: Optional[AuditPolicyStateType] = None


# This class is the input for the 'modify_certificates' function.
class ModifyCertificatesMessage(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    RemoveCustomerOverride: Optional[bool] = None


# This class is the input for the 'modify_current_db_cluster_capacity' function.
class ModifyCurrentDBClusterCapacityMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    Capacity: Optional[int] = None
    SecondsBeforeTimeout: Optional[int] = None
    TimeoutAction: Optional[str] = None


# This class is the input for the 'modify_custom_db_engine_version' function.
class ModifyCustomDBEngineVersionMessage(BaseValidatorModel):
    Engine: str
    EngineVersion: str
    Description: Optional[str] = None
    Status: Optional[CustomEngineVersionStatusType] = None


# This class is the input for the 'modify_db_cluster_endpoint' function.
class ModifyDBClusterEndpointMessage(BaseValidatorModel):
    DBClusterEndpointIdentifier: str
    EndpointType: Optional[str] = None
    StaticMembers: Optional[List[str]] = None
    ExcludedMembers: Optional[List[str]] = None


# This class is the input for the 'modify_db_cluster_snapshot_attribute' function.
class ModifyDBClusterSnapshotAttributeMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[List[str]] = None
    ValuesToRemove: Optional[List[str]] = None


# This class is the input for the 'modify_db_proxy_endpoint' function.
class ModifyDBProxyEndpointRequest(BaseValidatorModel):
    DBProxyEndpointName: str
    NewDBProxyEndpointName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None


class RecommendedActionUpdate(BaseValidatorModel):
    ActionId: str
    Status: str


# This class is the input for the 'modify_db_shard_group' function.
class ModifyDBShardGroupMessage(BaseValidatorModel):
    DBShardGroupIdentifier: str
    MaxACU: Optional[float] = None
    MinACU: Optional[float] = None
    ComputeRedundancy: Optional[int] = None


# This class is the input for the 'modify_db_snapshot_attribute' function.
class ModifyDBSnapshotAttributeMessage(BaseValidatorModel):
    DBSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[List[str]] = None
    ValuesToRemove: Optional[List[str]] = None


# This class is the input for the 'modify_db_snapshot' function.
class ModifyDBSnapshotMessage(BaseValidatorModel):
    DBSnapshotIdentifier: str
    EngineVersion: Optional[str] = None
    OptionGroupName: Optional[str] = None


# This class is the input for the 'modify_db_subnet_group' function.
class ModifyDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str
    SubnetIds: List[str]
    DBSubnetGroupDescription: Optional[str] = None


# This class is the input for the 'modify_event_subscription' function.
class ModifyEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Enabled: Optional[bool] = None


# This class is the input for the 'modify_global_cluster' function.
class ModifyGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None


# This class is the input for the 'modify_integration' function.
class ModifyIntegrationMessage(BaseValidatorModel):
    IntegrationIdentifier: str
    IntegrationName: Optional[str] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'modify_tenant_database' function.
class ModifyTenantDatabaseMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    MasterUserPassword: Optional[str] = None
    NewTenantDBName: Optional[str] = None


class OptionSetting(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    IsCollection: Optional[bool] = None


class OptionVersion(BaseValidatorModel):
    Version: Optional[str] = None
    IsDefault: Optional[bool] = None


class Outpost(BaseValidatorModel):
    Arn: Optional[str] = None


class Parameter(BaseValidatorModel):
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


class PendingMaintenanceAction(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None


class PerformanceInsightsMetricDimensionGroup(BaseValidatorModel):
    Dimensions: Optional[List[str]] = None
    Group: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'promote_read_replica_db_cluster' function.
class PromoteReadReplicaDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


# This class is the input for the 'promote_read_replica' function.
class PromoteReadReplicaMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None


class Range(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None
    Step: Optional[int] = None


# This class is the input for the 'reboot_db_cluster' function.
class RebootDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


# This class is the input for the 'reboot_db_instance' function.
class RebootDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None


# This class is the input for the 'reboot_db_shard_group' function.
class RebootDBShardGroupMessage(BaseValidatorModel):
    DBShardGroupIdentifier: str


class RecommendedActionParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class ScalarReferenceDetails(BaseValidatorModel):
    Value: Optional[float] = None


# This class is the input for the 'register_db_proxy_targets' function.
class RegisterDBProxyTargetsRequest(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    DBInstanceIdentifiers: Optional[List[str]] = None
    DBClusterIdentifiers: Optional[List[str]] = None


# This class is the input for the 'remove_from_global_cluster' function.
class RemoveFromGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None


# This class is the input for the 'remove_role_from_db_cluster' function.
class RemoveRoleFromDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None


# This class is the input for the 'remove_role_from_db_instance' function.
class RemoveRoleFromDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    RoleArn: str
    FeatureName: str


# This class is the input for the 'remove_source_identifier_from_subscription' function.
class RemoveSourceIdentifierFromSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


# This class is the input for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: List[str]


# This class is the input for the 'revoke_db_security_group_ingress' function.
class RevokeDBSecurityGroupIngressMessage(BaseValidatorModel):
    DBSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupId: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class SourceRegion(BaseValidatorModel):
    RegionName: Optional[str] = None
    Endpoint: Optional[str] = None
    Status: Optional[str] = None
    SupportsDBInstanceAutomatedBackupsReplication: Optional[bool] = None


# This class is the input for the 'start_activity_stream' function.
class StartActivityStreamRequest(BaseValidatorModel):
    ResourceArn: str
    Mode: ActivityStreamModeType
    KmsKeyId: str
    ApplyImmediately: Optional[bool] = None
    EngineNativeAuditFieldsIncluded: Optional[bool] = None


# This class is the input for the 'start_db_cluster' function.
class StartDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


# This class is the input for the 'start_db_instance_automated_backups_replication' function.
class StartDBInstanceAutomatedBackupsReplicationMessage(BaseValidatorModel):
    SourceDBInstanceArn: str
    BackupRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    SourceRegion: Optional[str] = None


# This class is the input for the 'start_db_instance' function.
class StartDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str


# This class is the input for the 'start_export_task' function.
class StartExportTaskMessage(BaseValidatorModel):
    ExportTaskIdentifier: str
    SourceArn: str
    S3BucketName: str
    IamRoleArn: str
    KmsKeyId: str
    S3Prefix: Optional[str] = None
    ExportOnly: Optional[List[str]] = None


# This class is the input for the 'stop_activity_stream' function.
class StopActivityStreamRequest(BaseValidatorModel):
    ResourceArn: str
    ApplyImmediately: Optional[bool] = None


# This class is the input for the 'stop_db_cluster' function.
class StopDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


# This class is the input for the 'stop_db_instance_automated_backups_replication' function.
class StopDBInstanceAutomatedBackupsReplicationMessage(BaseValidatorModel):
    SourceDBInstanceArn: str


# This class is the input for the 'stop_db_instance' function.
class StopDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBSnapshotIdentifier: Optional[str] = None


# This class is the input for the 'switchover_blue_green_deployment' function.
class SwitchoverBlueGreenDeploymentRequest(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: str
    SwitchoverTimeout: Optional[int] = None


# This class is the input for the 'switchover_global_cluster' function.
class SwitchoverGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str


# This class is the input for the 'switchover_read_replica' function.
class SwitchoverReadReplicaMessage(BaseValidatorModel):
    DBInstanceIdentifier: str


class TenantDatabasePendingModifiedValues(BaseValidatorModel):
    MasterUserPassword: Optional[str] = None
    TenantDBName: Optional[str] = None


class AccountAttributesMessage(BaseValidatorModel):
    AccountQuotas: List[AccountQuota]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'backtrack_db_cluster' function.
class DBClusterBacktrackResponse(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: str
    BacktrackTo: datetime
    BacktrackedFrom: datetime
    BacktrackRequestCreationTime: datetime
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_current_db_cluster_capacity' function.
class DBClusterCapacityInfo(BaseValidatorModel):
    DBClusterIdentifier: str
    PendingCapacity: int
    CurrentCapacity: int
    SecondsBeforeTimeout: int
    TimeoutAction: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_cluster_endpoint' function.
class DBClusterEndpointResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_db_cluster_parameter_group' function.
class DBClusterParameterGroupNameMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_db_parameter_group' function.
class DBParameterGroupNameMessage(BaseValidatorModel):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_http_endpoint' function.
class DisableHttpEndpointResponse(BaseValidatorModel):
    ResourceArn: str
    HttpEndpointEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'download_db_log_file_portion' function.
class DownloadDBLogFilePortionDetails(BaseValidatorModel):
    LogFileData: str
    Marker: str
    AdditionalDataPending: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_tags_from_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_http_endpoint' function.
class EnableHttpEndpointResponse(BaseValidatorModel):
    ResourceArn: str
    HttpEndpointEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_export_task' function.
class ExportTaskResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_activity_stream' function.
class ModifyActivityStreamResponse(BaseValidatorModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    Mode: ActivityStreamModeType
    EngineNativeAuditFieldsIncluded: bool
    PolicyStatus: ActivityStreamPolicyStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_activity_stream' function.
class StartActivityStreamResponse(BaseValidatorModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    Mode: ActivityStreamModeType
    ApplyImmediately: bool
    EngineNativeAuditFieldsIncluded: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_activity_stream' function.
class StopActivityStreamResponse(BaseValidatorModel):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_source_identifier_to_subscription' function.
class AddSourceIdentifierToSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_event_subscription' function.
class CreateEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_event_subscription' function.
class DeleteEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_subscriptions' function.
class EventSubscriptionsMessage(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_event_subscription' function.
class ModifyEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_source_identifier_from_subscription' function.
class RemoveSourceIdentifierFromSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_tags_to_resource' function.
class AddTagsToResourceMessage(BaseValidatorModel):
    ResourceName: str
    Tags: List[Tag]


# This class is the input for the 'copy_db_cluster_parameter_group' function.
class CopyDBClusterParameterGroupMessage(BaseValidatorModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'copy_db_cluster_snapshot' function.
class CopyDBClusterSnapshotMessage(BaseValidatorModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    SourceRegion: Optional[str] = None


# This class is the input for the 'copy_db_parameter_group' function.
class CopyDBParameterGroupMessage(BaseValidatorModel):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'copy_db_snapshot' function.
class CopyDBSnapshotMessage(BaseValidatorModel):
    SourceDBSnapshotIdentifier: str
    TargetDBSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CopyTags: Optional[bool] = None
    PreSignedUrl: Optional[str] = None
    OptionGroupName: Optional[str] = None
    TargetCustomAvailabilityZone: Optional[str] = None
    CopyOptionGroup: Optional[bool] = None
    SourceRegion: Optional[str] = None


# This class is the input for the 'copy_option_group' function.
class CopyOptionGroupMessage(BaseValidatorModel):
    SourceOptionGroupIdentifier: str
    TargetOptionGroupIdentifier: str
    TargetOptionGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_blue_green_deployment' function.
class CreateBlueGreenDeploymentRequest(BaseValidatorModel):
    BlueGreenDeploymentName: str
    Source: str
    TargetEngineVersion: Optional[str] = None
    TargetDBParameterGroupName: Optional[str] = None
    TargetDBClusterParameterGroupName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    TargetDBInstanceClass: Optional[str] = None
    UpgradeTargetStorageConfig: Optional[bool] = None
    TargetIops: Optional[int] = None
    TargetStorageType: Optional[str] = None
    TargetAllocatedStorage: Optional[int] = None
    TargetStorageThroughput: Optional[int] = None


# This class is the input for the 'create_custom_db_engine_version' function.
class CreateCustomDBEngineVersionMessage(BaseValidatorModel):
    Engine: str
    EngineVersion: str
    DatabaseInstallationFilesS3BucketName: Optional[str] = None
    DatabaseInstallationFilesS3Prefix: Optional[str] = None
    ImageId: Optional[str] = None
    KMSKeyId: Optional[str] = None
    Description: Optional[str] = None
    Manifest: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SourceCustomDbEngineVersionIdentifier: Optional[str] = None
    UseAwsProvidedLatestImage: Optional[bool] = None


# This class is the input for the 'create_db_cluster_endpoint' function.
class CreateDBClusterEndpointMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: Optional[List[str]] = None
    ExcludedMembers: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_cluster_parameter_group' function.
class CreateDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_cluster_snapshot' function.
class CreateDBClusterSnapshotMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_parameter_group' function.
class CreateDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_proxy_endpoint' function.
class CreateDBProxyEndpointRequest(BaseValidatorModel):
    DBProxyName: str
    DBProxyEndpointName: str
    VpcSubnetIds: List[str]
    VpcSecurityGroupIds: Optional[List[str]] = None
    TargetRole: Optional[DBProxyEndpointTargetRoleType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_security_group' function.
class CreateDBSecurityGroupMessage(BaseValidatorModel):
    DBSecurityGroupName: str
    DBSecurityGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_shard_group' function.
class CreateDBShardGroupMessage(BaseValidatorModel):
    DBShardGroupIdentifier: str
    DBClusterIdentifier: str
    MaxACU: float
    ComputeRedundancy: Optional[int] = None
    MinACU: Optional[float] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_snapshot' function.
class CreateDBSnapshotMessage(BaseValidatorModel):
    DBSnapshotIdentifier: str
    DBInstanceIdentifier: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_subnet_group' function.
class CreateDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: List[str]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_event_subscription' function.
class CreateEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    SourceIds: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_global_cluster' function.
class CreateGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_integration' function.
class CreateIntegrationMessage(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'create_option_group' function.
class CreateOptionGroupMessage(BaseValidatorModel):
    OptionGroupName: str
    EngineName: str
    MajorEngineVersion: str
    OptionGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_tenant_database' function.
class CreateTenantDatabaseMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    TenantDBName: str
    MasterUsername: str
    MasterUserPassword: str
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DBClusterSnapshot(BaseValidatorModel):
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
    TagList: Optional[List[Tag]] = None
    DBSystemId: Optional[str] = None
    StorageType: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    StorageThroughput: Optional[int] = None


# This class is the output for the 'reboot_db_shard_group' function.
class DBShardGroupResponse(BaseValidatorModel):
    DBShardGroupResourceId: str
    DBShardGroupIdentifier: str
    DBClusterIdentifier: str
    MaxACU: float
    MinACU: float
    ComputeRedundancy: int
    Status: str
    PubliclyAccessible: bool
    Endpoint: str
    DBShardGroupArn: str
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class DBShardGroup(BaseValidatorModel):
    DBShardGroupResourceId: Optional[str] = None
    DBShardGroupIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    MaxACU: Optional[float] = None
    MinACU: Optional[float] = None
    ComputeRedundancy: Optional[int] = None
    Status: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Endpoint: Optional[str] = None
    DBShardGroupArn: Optional[str] = None
    TagList: Optional[List[Tag]] = None


class DBSnapshotTenantDatabase(BaseValidatorModel):
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
    TagList: Optional[List[Tag]] = None


# This class is the input for the 'purchase_reserved_db_instances_offering' function.
class PurchaseReservedDBInstancesOfferingMessage(BaseValidatorModel):
    ReservedDBInstancesOfferingId: str
    ReservedDBInstanceId: Optional[str] = None
    DBInstanceCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class TagListMessage(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class OrderableDBInstanceOption(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
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
    AvailableProcessorFeatures: Optional[List[AvailableProcessorFeature]] = None
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


# This class is the input for the 'backtrack_db_cluster' function.
class BacktrackDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackTo: Timestamp
    Force: Optional[bool] = None
    UseEarliestTimeOnPointInTimeUnavailable: Optional[bool] = None


class BlueGreenDeployment(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    BlueGreenDeploymentName: Optional[str] = None
    Source: Optional[str] = None
    Target: Optional[str] = None
    SwitchoverDetails: Optional[List[SwitchoverDetail]] = None
    Tasks: Optional[List[BlueGreenDeploymentTask]] = None
    Status: Optional[str] = None
    StatusDetails: Optional[str] = None
    CreateTime: Optional[datetime] = None
    DeleteTime: Optional[datetime] = None
    TagList: Optional[List[Tag]] = None


# This class is the output for the 'describe_certificates' function.
class CertificateMessage(BaseValidatorModel):
    DefaultCertificateForNewLaunches: str
    Certificates: List[Certificate]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_certificates' function.
class ModifyCertificatesResult(BaseValidatorModel):
    Certificate: Certificate
    ResponseMetadata: ResponseMetadata


class ClusterPendingModifiedValues(BaseValidatorModel):
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExports] = None
    DBClusterIdentifier: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    EngineVersion: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    AllocatedStorage: Optional[int] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration] = None
    Iops: Optional[int] = None
    StorageType: Optional[str] = None
    CertificateDetails: Optional[CertificateDetails] = None


class DBProxyTargetGroup(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    TargetGroupName: Optional[str] = None
    TargetGroupArn: Optional[str] = None
    IsDefault: Optional[bool] = None
    Status: Optional[str] = None
    ConnectionPoolConfig: Optional[ConnectionPoolConfigurationInfo] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None


# This class is the input for the 'modify_db_proxy_target_group' function.
class ModifyDBProxyTargetGroupRequest(BaseValidatorModel):
    TargetGroupName: str
    DBProxyName: str
    ConnectionPoolConfig: Optional[ConnectionPoolConfiguration] = None
    NewName: Optional[str] = None


# This class is the output for the 'copy_db_cluster_parameter_group' function.
class CopyDBClusterParameterGroupResult(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster_parameter_group' function.
class CreateDBClusterParameterGroupResult(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_parameter_groups' function.
class DBClusterParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_db_parameter_group' function.
class CopyDBParameterGroupResult(BaseValidatorModel):
    DBParameterGroup: DBParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_parameter_group' function.
class CreateDBParameterGroupResult(BaseValidatorModel):
    DBParameterGroup: DBParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_parameter_groups' function.
class DBParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    DBParameterGroups: List[DBParameterGroup]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_db_cluster' function.
class CreateDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    DatabaseName: Optional[str] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfiguration] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration] = None
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
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableLimitlessDatabase: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    NetworkType: Optional[str] = None
    ClusterScalabilityType: Optional[ClusterScalabilityTypeType] = None
    DBSystemId: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    EnableLocalWriteForwarding: Optional[bool] = None
    CACertificateIdentifier: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None
    SourceRegion: Optional[str] = None


# This class is the input for the 'modify_db_cluster' function.
class ModifyDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    DBInstanceParameterGroupName: Optional[str] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfiguration] = None
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
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
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


# This class is the input for the 'restore_db_cluster_from_s3' function.
class RestoreDBClusterFromS3Message(BaseValidatorModel):
    DBClusterIdentifier: str
    Engine: str
    MasterUsername: str
    SourceEngine: str
    SourceEngineVersion: str
    S3BucketName: str
    S3IngestionRoleArn: str
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    DatabaseName: Optional[str] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    S3Prefix: Optional[str] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    NetworkType: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    StorageType: Optional[str] = None
    EngineLifecycleSupport: Optional[str] = None


# This class is the input for the 'restore_db_cluster_from_snapshot' function.
class RestoreDBClusterFromSnapshotMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: Optional[List[str]] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    DatabaseName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfiguration] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DBClusterInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    NetworkType: Optional[str] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EngineLifecycleSupport: Optional[str] = None


# This class is the input for the 'restore_db_cluster_to_point_in_time' function.
class RestoreDBClusterToPointInTimeMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    RestoreType: Optional[str] = None
    SourceDBClusterIdentifier: Optional[str] = None
    RestoreToTime: Optional[Timestamp] = None
    UseLatestRestorableTime: Optional[bool] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    BacktrackWindow: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    ScalingConfiguration: Optional[ScalingConfiguration] = None
    EngineMode: Optional[str] = None
    DBClusterInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Iops: Optional[int] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    NetworkType: Optional[str] = None
    SourceDbClusterResourceId: Optional[str] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EngineLifecycleSupport: Optional[str] = None


# This class is the input for the 'create_db_instance' function.
class CreateDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBName: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    DBSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
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
    Tags: Optional[List[Tag]] = None
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
    DomainDnsIps: Optional[List[str]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
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


# This class is the input for the 'create_db_instance_read_replica' function.
class CreateDBInstanceReadReplicaMessage(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None
    DBSubnetGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    StorageType: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
    UseDefaultProcessorFeatures: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[List[str]] = None
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


class DBSnapshot(BaseValidatorModel):
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
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
    DbiResourceId: Optional[str] = None
    TagList: Optional[List[Tag]] = None
    OriginalSnapshotCreateTime: Optional[datetime] = None
    SnapshotDatabaseTime: Optional[datetime] = None
    SnapshotTarget: Optional[str] = None
    StorageThroughput: Optional[int] = None
    DBSystemId: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None


# This class is the input for the 'modify_db_instance' function.
class ModifyDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    AllocatedStorage: Optional[int] = None
    DBInstanceClass: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    DBSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
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
    DomainDnsIps: Optional[List[str]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    DBPortNumber: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    MonitoringRoleArn: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DisableDomain: Optional[bool] = None
    PromotionTier: Optional[int] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
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


class PendingModifiedValues(BaseValidatorModel):
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
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExports] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    AutomationMode: Optional[AutomationModeType] = None
    ResumeFullAutomationModeTime: Optional[datetime] = None
    StorageThroughput: Optional[int] = None
    Engine: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None


# This class is the input for the 'restore_db_instance_from_db_snapshot' function.
class RestoreDBInstanceFromDBSnapshotMessage(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Domain: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[List[str]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    DomainIAMRoleName: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
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


# This class is the input for the 'restore_db_instance_from_s3' function.
class RestoreDBInstanceFromS3Message(BaseValidatorModel):
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
    DBSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
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
    Tags: Optional[List[Tag]] = None
    StorageType: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    S3Prefix: Optional[str] = None
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
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


# This class is the input for the 'restore_db_instance_to_point_in_time' function.
class RestoreDBInstanceToPointInTimeMessage(BaseValidatorModel):
    TargetDBInstanceIdentifier: str
    SourceDBInstanceIdentifier: Optional[str] = None
    RestoreTime: Optional[Timestamp] = None
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
    Tags: Optional[List[Tag]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Domain: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    DomainFqdn: Optional[str] = None
    DomainOu: Optional[str] = None
    DomainAuthSecretArn: Optional[str] = None
    DomainDnsIps: Optional[List[str]] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
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


# This class is the output for the 'create_db_proxy_endpoint' function.
class CreateDBProxyEndpointResponse(BaseValidatorModel):
    DBProxyEndpoint: DBProxyEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_proxy_endpoint' function.
class DeleteDBProxyEndpointResponse(BaseValidatorModel):
    DBProxyEndpoint: DBProxyEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_proxy_endpoints' function.
class DescribeDBProxyEndpointsResponse(BaseValidatorModel):
    DBProxyEndpoints: List[DBProxyEndpoint]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_proxy_endpoint' function.
class ModifyDBProxyEndpointResponse(BaseValidatorModel):
    DBProxyEndpoint: DBProxyEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_db_proxy' function.
class CreateDBProxyRequest(BaseValidatorModel):
    DBProxyName: str
    EngineFamily: EngineFamilyType
    Auth: List[UserAuthConfig]
    RoleArn: str
    VpcSubnetIds: List[str]
    VpcSecurityGroupIds: Optional[List[str]] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'modify_db_proxy' function.
class ModifyDBProxyRequest(BaseValidatorModel):
    DBProxyName: str
    NewDBProxyName: Optional[str] = None
    Auth: Optional[List[UserAuthConfig]] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    RoleArn: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None


class DBClusterAutomatedBackup(BaseValidatorModel):
    Engine: Optional[str] = None
    VpcId: Optional[str] = None
    DBClusterAutomatedBackupsArn: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    RestoreWindow: Optional[RestoreWindow] = None
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


# This class is the output for the 'describe_db_cluster_backtracks' function.
class DBClusterBacktrackMessage(BaseValidatorModel):
    Marker: str
    DBClusterBacktracks: List[DBClusterBacktrack]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_endpoints' function.
class DBClusterEndpointMessage(BaseValidatorModel):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_parameters' function.
class DBClusterParameterGroupDetails(BaseValidatorModel):
    Parameters: List[ParameterOutput]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_parameters' function.
class DBParameterGroupDetails(BaseValidatorModel):
    Parameters: List[ParameterOutput]
    Marker: str
    ResponseMetadata: ResponseMetadata


class EngineDefaults(BaseValidatorModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterOutput]] = None


class DBClusterSnapshotAttributesResult(BaseValidatorModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttribute]] = None


# This class is the output for the 'modify_custom_db_engine_version' function.
class DBEngineVersionResponse(BaseValidatorModel):
    Engine: str
    EngineVersion: str
    DBParameterGroupFamily: str
    DBEngineDescription: str
    DBEngineVersionDescription: str
    DefaultCharacterSet: CharacterSet
    Image: CustomDBEngineVersionAMI
    DBEngineMediaType: str
    SupportedCharacterSets: List[CharacterSet]
    SupportedNcharCharacterSets: List[CharacterSet]
    ValidUpgradeTarget: List[UpgradeTarget]
    SupportedTimezones: List[Timezone]
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
    TagList: List[Tag]
    SupportsBabelfish: bool
    CustomDBEngineVersionManifest: str
    SupportsLimitlessDatabase: bool
    SupportsCertificateRotationWithoutRestart: bool
    SupportedCACertificateIdentifiers: List[str]
    SupportsLocalWriteForwarding: bool
    SupportsIntegrations: bool
    ServerlessV2FeaturesSupport: ServerlessV2FeaturesSupport
    ResponseMetadata: ResponseMetadata


class DBEngineVersion(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    DBEngineDescription: Optional[str] = None
    DBEngineVersionDescription: Optional[str] = None
    DefaultCharacterSet: Optional[CharacterSet] = None
    Image: Optional[CustomDBEngineVersionAMI] = None
    DBEngineMediaType: Optional[str] = None
    SupportedCharacterSets: Optional[List[CharacterSet]] = None
    SupportedNcharCharacterSets: Optional[List[CharacterSet]] = None
    ValidUpgradeTarget: Optional[List[UpgradeTarget]] = None
    SupportedTimezones: Optional[List[Timezone]] = None
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
    TagList: Optional[List[Tag]] = None
    SupportsBabelfish: Optional[bool] = None
    CustomDBEngineVersionManifest: Optional[str] = None
    SupportsLimitlessDatabase: Optional[bool] = None
    SupportsCertificateRotationWithoutRestart: Optional[bool] = None
    SupportedCACertificateIdentifiers: Optional[List[str]] = None
    SupportsLocalWriteForwarding: Optional[bool] = None
    SupportsIntegrations: Optional[bool] = None
    ServerlessV2FeaturesSupport: Optional[ServerlessV2FeaturesSupport] = None


class DBInstanceAutomatedBackup(BaseValidatorModel):
    DBInstanceArn: Optional[str] = None
    DbiResourceId: Optional[str] = None
    Region: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    RestoreWindow: Optional[RestoreWindow] = None
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
    DBInstanceAutomatedBackupsReplications: Optional[List[DBInstanceAutomatedBackupsReplication]] = None
    BackupTarget: Optional[str] = None
    StorageThroughput: Optional[int] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    MultiTenant: Optional[bool] = None


class DBProxyTarget(BaseValidatorModel):
    TargetArn: Optional[str] = None
    Endpoint: Optional[str] = None
    TrackedClusterId: Optional[str] = None
    RdsResourceId: Optional[str] = None
    Port: Optional[int] = None
    Type: Optional[TargetTypeType] = None
    Role: Optional[TargetRoleType] = None
    TargetHealth: Optional[TargetHealth] = None


class DBProxy(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    DBProxyArn: Optional[str] = None
    Status: Optional[DBProxyStatusType] = None
    EngineFamily: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    VpcSubnetIds: Optional[List[str]] = None
    Auth: Optional[List[UserAuthConfigInfo]] = None
    RoleArn: Optional[str] = None
    Endpoint: Optional[str] = None
    RequireTLS: Optional[bool] = None
    IdleClientTimeout: Optional[int] = None
    DebugLogging: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None


class DBSecurityGroup(BaseValidatorModel):
    OwnerId: Optional[str] = None
    DBSecurityGroupName: Optional[str] = None
    DBSecurityGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroup]] = None
    IPRanges: Optional[List[IPRange]] = None
    DBSecurityGroupArn: Optional[str] = None


class DBSnapshotAttributesResult(BaseValidatorModel):
    DBSnapshotIdentifier: Optional[str] = None
    DBSnapshotAttributes: Optional[List[DBSnapshotAttribute]] = None


# This class is the input for the 'describe_blue_green_deployments' function.
class DescribeBlueGreenDeploymentsRequest(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_certificates' function.
class DescribeCertificatesMessage(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_automated_backups' function.
class DescribeDBClusterAutomatedBackupsMessage(BaseValidatorModel):
    DbClusterResourceId: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_backtracks' function.
class DescribeDBClusterBacktracksMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_endpoints' function.
class DescribeDBClusterEndpointsMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_parameter_groups' function.
class DescribeDBClusterParameterGroupsMessage(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_parameters' function.
class DescribeDBClusterParametersMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_snapshots' function.
class DescribeDBClusterSnapshotsMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None


# This class is the input for the 'describe_db_clusters' function.
class DescribeDBClustersMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None


# This class is the input for the 'describe_db_engine_versions' function.
class DescribeDBEngineVersionsMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    IncludeAll: Optional[bool] = None


# This class is the input for the 'describe_db_instance_automated_backups' function.
class DescribeDBInstanceAutomatedBackupsMessage(BaseValidatorModel):
    DbiResourceId: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None


# This class is the input for the 'describe_db_instances' function.
class DescribeDBInstancesMessage(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_log_files' function.
class DescribeDBLogFilesMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    FilenameContains: Optional[str] = None
    FileLastWritten: Optional[int] = None
    FileSize: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_parameter_groups' function.
class DescribeDBParameterGroupsMessage(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_parameters' function.
class DescribeDBParametersMessage(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_proxies' function.
class DescribeDBProxiesRequest(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_db_proxy_endpoints' function.
class DescribeDBProxyEndpointsRequest(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    DBProxyEndpointName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_db_proxy_target_groups' function.
class DescribeDBProxyTargetGroupsRequest(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_db_proxy_targets' function.
class DescribeDBProxyTargetsRequest(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_db_recommendations' function.
class DescribeDBRecommendationsMessage(BaseValidatorModel):
    LastUpdatedAfter: Optional[Timestamp] = None
    LastUpdatedBefore: Optional[Timestamp] = None
    Locale: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_security_groups' function.
class DescribeDBSecurityGroupsMessage(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_shard_groups' function.
class DescribeDBShardGroupsMessage(BaseValidatorModel):
    DBShardGroupIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_db_snapshot_tenant_databases' function.
class DescribeDBSnapshotTenantDatabasesMessage(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DbiResourceId: Optional[str] = None


# This class is the input for the 'describe_db_snapshots' function.
class DescribeDBSnapshotsMessage(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None


# This class is the input for the 'describe_db_subnet_groups' function.
class DescribeDBSubnetGroupsMessage(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_engine_default_cluster_parameters' function.
class DescribeEngineDefaultClusterParametersMessage(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_engine_default_parameters' function.
class DescribeEngineDefaultParametersMessage(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_event_categories' function.
class DescribeEventCategoriesMessage(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_event_subscriptions' function.
class DescribeEventSubscriptionsMessage(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_events' function.
class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_export_tasks' function.
class DescribeExportTasksMessage(BaseValidatorModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    SourceType: Optional[ExportSourceTypeType] = None


# This class is the input for the 'describe_global_clusters' function.
class DescribeGlobalClustersMessage(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_integrations' function.
class DescribeIntegrationsMessage(BaseValidatorModel):
    IntegrationIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_option_group_options' function.
class DescribeOptionGroupOptionsMessage(BaseValidatorModel):
    EngineName: str
    MajorEngineVersion: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_option_groups' function.
class DescribeOptionGroupsMessage(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None


# This class is the input for the 'describe_orderable_db_instance_options' function.
class DescribeOrderableDBInstanceOptionsMessage(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_pending_maintenance_actions' function.
class DescribePendingMaintenanceActionsMessage(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_reserved_db_instances' function.
class DescribeReservedDBInstancesMessage(BaseValidatorModel):
    ReservedDBInstanceId: Optional[str] = None
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    LeaseId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_reserved_db_instances_offerings' function.
class DescribeReservedDBInstancesOfferingsMessage(BaseValidatorModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_source_regions' function.
class DescribeSourceRegionsMessage(BaseValidatorModel):
    RegionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_tenant_databases' function.
class DescribeTenantDatabasesMessage(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceName: str
    Filters: Optional[List[Filter]] = None


class DescribeBlueGreenDeploymentsRequestPaginate(BaseValidatorModel):
    BlueGreenDeploymentIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCertificatesMessagePaginate(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterAutomatedBackupsMessagePaginate(BaseValidatorModel):
    DbClusterResourceId: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterBacktracksMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: str
    BacktrackIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterEndpointsMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterParameterGroupsMessagePaginate(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterParametersMessagePaginate(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterSnapshotsMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClustersMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    IncludeShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBEngineVersionsMessagePaginate(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    IncludeAll: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBInstanceAutomatedBackupsMessagePaginate(BaseValidatorModel):
    DbiResourceId: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DBInstanceAutomatedBackupsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBInstancesMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBLogFilesMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: str
    FilenameContains: Optional[str] = None
    FileLastWritten: Optional[int] = None
    FileSize: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBParameterGroupsMessagePaginate(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBParametersMessagePaginate(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBProxiesRequestPaginate(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBProxyEndpointsRequestPaginate(BaseValidatorModel):
    DBProxyName: Optional[str] = None
    DBProxyEndpointName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBProxyTargetGroupsRequestPaginate(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBProxyTargetsRequestPaginate(BaseValidatorModel):
    DBProxyName: str
    TargetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBRecommendationsMessagePaginate(BaseValidatorModel):
    LastUpdatedAfter: Optional[Timestamp] = None
    LastUpdatedBefore: Optional[Timestamp] = None
    Locale: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBSecurityGroupsMessagePaginate(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBSnapshotTenantDatabasesMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DbiResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBSnapshotsMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBSubnetGroupsMessagePaginate(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEngineDefaultClusterParametersMessagePaginate(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEngineDefaultParametersMessagePaginate(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventSubscriptionsMessagePaginate(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeExportTasksMessagePaginate(BaseValidatorModel):
    ExportTaskIdentifier: Optional[str] = None
    SourceArn: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SourceType: Optional[ExportSourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGlobalClustersMessagePaginate(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeIntegrationsMessagePaginate(BaseValidatorModel):
    IntegrationIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOptionGroupOptionsMessagePaginate(BaseValidatorModel):
    EngineName: str
    MajorEngineVersion: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOptionGroupsMessagePaginate(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrderableDBInstanceOptionsMessagePaginate(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePendingMaintenanceActionsMessagePaginate(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedDBInstancesMessagePaginate(BaseValidatorModel):
    ReservedDBInstanceId: Optional[str] = None
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    LeaseId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedDBInstancesOfferingsMessagePaginate(BaseValidatorModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSourceRegionsMessagePaginate(BaseValidatorModel):
    RegionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTenantDatabasesMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DownloadDBLogFilePortionMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: str
    LogFileName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterSnapshotsMessageWaitExtra(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBClusterSnapshotsMessageWait(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbClusterResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBClustersMessageWaitExtra(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBClustersMessageWait(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBInstancesMessageWaitExtra(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBInstancesMessageWait(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBSnapshotsMessageWaitExtraExtra(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBSnapshotsMessageWaitExtra(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBSnapshotsMessageWait(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    DbiResourceId: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTenantDatabasesMessageWaitExtra(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTenantDatabasesMessageWait(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    TenantDBName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_db_log_files' function.
class DescribeDBLogFilesResponse(BaseValidatorModel):
    DescribeDBLogFiles: List[DescribeDBLogFilesDetails]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_categories' function.
class EventCategoriesMessage(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMap]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_events' function.
class EventsMessage(BaseValidatorModel):
    Marker: str
    Events: List[Event]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_export_tasks' function.
class ExportTasksMessage(BaseValidatorModel):
    Marker: str
    ExportTasks: List[ExportTask]
    ResponseMetadata: ResponseMetadata


class GlobalCluster(BaseValidatorModel):
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
    GlobalClusterMembers: Optional[List[GlobalClusterMember]] = None
    Endpoint: Optional[str] = None
    FailoverState: Optional[FailoverState] = None
    TagList: Optional[List[Tag]] = None


# This class is the output for the 'modify_integration' function.
class IntegrationResponse(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    IntegrationArn: str
    KMSKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Status: IntegrationStatusType
    Tags: List[Tag]
    CreateTime: datetime
    Errors: List[IntegrationError]
    DataFilter: str
    Description: str
    ResponseMetadata: ResponseMetadata


class Integration(BaseValidatorModel):
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    IntegrationName: Optional[str] = None
    IntegrationArn: Optional[str] = None
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Status: Optional[IntegrationStatusType] = None
    Tags: Optional[List[Tag]] = None
    CreateTime: Optional[datetime] = None
    Errors: Optional[List[IntegrationError]] = None
    DataFilter: Optional[str] = None
    Description: Optional[str] = None


class OptionGroupOptionSetting(BaseValidatorModel):
    SettingName: Optional[str] = None
    SettingDescription: Optional[str] = None
    DefaultValue: Optional[str] = None
    ApplyType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    IsRequired: Optional[bool] = None
    MinimumEngineVersionPerAllowedValue: Optional[List[MinimumEngineVersionPerAllowedValue]] = None


# This class is the input for the 'modify_db_recommendation' function.
class ModifyDBRecommendationMessage(BaseValidatorModel):
    RecommendationId: str
    Locale: Optional[str] = None
    Status: Optional[str] = None
    RecommendedActionUpdates: Optional[List[RecommendedActionUpdate]] = None


class OptionConfiguration(BaseValidatorModel):
    OptionName: str
    Port: Optional[int] = None
    OptionVersion: Optional[str] = None
    DBSecurityGroupMemberships: Optional[List[str]] = None
    VpcSecurityGroupMemberships: Optional[List[str]] = None
    OptionSettings: Optional[List[OptionSetting]] = None


class Option(BaseValidatorModel):
    OptionName: Optional[str] = None
    OptionDescription: Optional[str] = None
    Persistent: Optional[bool] = None
    Permanent: Optional[bool] = None
    Port: Optional[int] = None
    OptionVersion: Optional[str] = None
    OptionSettings: Optional[List[OptionSetting]] = None
    DBSecurityGroupMemberships: Optional[List[DBSecurityGroupMembership]] = None
    VpcSecurityGroupMemberships: Optional[List[VpcSecurityGroupMembership]] = None


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetOutpost: Optional[Outpost] = None
    SubnetStatus: Optional[str] = None

ParameterUnion = Union[Parameter, ParameterOutput]


class ResourcePendingMaintenanceActions(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceAction]] = None


class PerformanceInsightsMetricQuery(BaseValidatorModel):
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroup] = None
    Metric: Optional[str] = None


class ValidStorageOptions(BaseValidatorModel):
    StorageType: Optional[str] = None
    StorageSize: Optional[List[Range]] = None
    ProvisionedIops: Optional[List[Range]] = None
    IopsToStorageRatio: Optional[List[DoubleRange]] = None
    SupportsStorageAutoscaling: Optional[bool] = None
    ProvisionedStorageThroughput: Optional[List[Range]] = None
    StorageThroughputToIopsRatio: Optional[List[DoubleRange]] = None


class ReservedDBInstance(BaseValidatorModel):
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
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ReservedDBInstanceArn: Optional[str] = None
    LeaseId: Optional[str] = None


class ReservedDBInstancesOffering(BaseValidatorModel):
    ReservedDBInstancesOfferingId: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class ReferenceDetails(BaseValidatorModel):
    ScalarReferenceDetails: Optional[ScalarReferenceDetails] = None


# This class is the output for the 'describe_source_regions' function.
class SourceRegionMessage(BaseValidatorModel):
    Marker: str
    SourceRegions: List[SourceRegion]
    ResponseMetadata: ResponseMetadata


class TenantDatabase(BaseValidatorModel):
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
    PendingModifiedValues: Optional[TenantDatabasePendingModifiedValues] = None
    TagList: Optional[List[Tag]] = None


# This class is the output for the 'copy_db_cluster_snapshot' function.
class CopyDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster_snapshot' function.
class CreateDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_snapshots' function.
class DBClusterSnapshotMessage(BaseValidatorModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshot]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster_snapshot' function.
class DeleteDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_shard_groups' function.
class DescribeDBShardGroupsResponse(BaseValidatorModel):
    DBShardGroups: List[DBShardGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_snapshot_tenant_databases' function.
class DBSnapshotTenantDatabasesMessage(BaseValidatorModel):
    Marker: str
    DBSnapshotTenantDatabases: List[DBSnapshotTenantDatabase]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_orderable_db_instance_options' function.
class OrderableDBInstanceOptionsMessage(BaseValidatorModel):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_blue_green_deployment' function.
class CreateBlueGreenDeploymentResponse(BaseValidatorModel):
    BlueGreenDeployment: BlueGreenDeployment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_blue_green_deployment' function.
class DeleteBlueGreenDeploymentResponse(BaseValidatorModel):
    BlueGreenDeployment: BlueGreenDeployment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_blue_green_deployments' function.
class DescribeBlueGreenDeploymentsResponse(BaseValidatorModel):
    BlueGreenDeployments: List[BlueGreenDeployment]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'switchover_blue_green_deployment' function.
class SwitchoverBlueGreenDeploymentResponse(BaseValidatorModel):
    BlueGreenDeployment: BlueGreenDeployment
    ResponseMetadata: ResponseMetadata


class DBCluster(BaseValidatorModel):
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
    DBClusterOptionGroupMemberships: Optional[List[DBClusterOptionGroupStatus]] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    ReadReplicaIdentifiers: Optional[List[str]] = None
    StatusInfos: Optional[List[DBClusterStatusInfo]] = None
    DBClusterMembers: Optional[List[DBClusterMember]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    DBClusterArn: Optional[str] = None
    AssociatedRoles: Optional[List[DBClusterRole]] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    CloneGroupId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    EarliestBacktrackTime: Optional[datetime] = None
    BacktrackWindow: Optional[int] = None
    BacktrackConsumedChangeRecords: Optional[int] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    Capacity: Optional[int] = None
    EngineMode: Optional[str] = None
    ScalingConfigurationInfo: Optional[ScalingConfigurationInfo] = None
    RdsCustomClusterConfiguration: Optional[RdsCustomClusterConfiguration] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamMode: Optional[ActivityStreamModeType] = None
    ActivityStreamStatus: Optional[ActivityStreamStatusType] = None
    ActivityStreamKmsKeyId: Optional[str] = None
    ActivityStreamKinesisStreamName: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[DomainMembership]] = None
    TagList: Optional[List[Tag]] = None
    GlobalWriteForwardingStatus: Optional[WriteForwardingStatusType] = None
    GlobalWriteForwardingRequested: Optional[bool] = None
    PendingModifiedValues: Optional[ClusterPendingModifiedValues] = None
    DBClusterInstanceClass: Optional[str] = None
    StorageType: Optional[str] = None
    Iops: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationInfo] = None
    NetworkType: Optional[str] = None
    DBSystemId: Optional[str] = None
    MasterUserSecret: Optional[MasterUserSecret] = None
    IOOptimizedNextAllowedModificationTime: Optional[datetime] = None
    LocalWriteForwardingStatus: Optional[LocalWriteForwardingStatusType] = None
    AwsBackupRecoveryPointArn: Optional[str] = None
    LimitlessDatabase: Optional[LimitlessDatabase] = None
    StorageThroughput: Optional[int] = None
    ClusterScalabilityType: Optional[ClusterScalabilityTypeType] = None
    CertificateDetails: Optional[CertificateDetails] = None
    EngineLifecycleSupport: Optional[str] = None


# This class is the output for the 'describe_db_proxy_target_groups' function.
class DescribeDBProxyTargetGroupsResponse(BaseValidatorModel):
    TargetGroups: List[DBProxyTargetGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_proxy_target_group' function.
class ModifyDBProxyTargetGroupResponse(BaseValidatorModel):
    DBProxyTargetGroup: DBProxyTargetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_db_snapshot' function.
class CopyDBSnapshotResult(BaseValidatorModel):
    DBSnapshot: DBSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_snapshot' function.
class CreateDBSnapshotResult(BaseValidatorModel):
    DBSnapshot: DBSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_snapshots' function.
class DBSnapshotMessage(BaseValidatorModel):
    Marker: str
    DBSnapshots: List[DBSnapshot]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_snapshot' function.
class DeleteDBSnapshotResult(BaseValidatorModel):
    DBSnapshot: DBSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_snapshot' function.
class ModifyDBSnapshotResult(BaseValidatorModel):
    DBSnapshot: DBSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_automated_backups' function.
class DBClusterAutomatedBackupMessage(BaseValidatorModel):
    Marker: str
    DBClusterAutomatedBackups: List[DBClusterAutomatedBackup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster_automated_backup' function.
class DeleteDBClusterAutomatedBackupResult(BaseValidatorModel):
    DBClusterAutomatedBackup: DBClusterAutomatedBackup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_engine_default_cluster_parameters' function.
class DescribeEngineDefaultClusterParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_engine_default_parameters' function.
class DescribeEngineDefaultParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_snapshot_attributes' function.
class DescribeDBClusterSnapshotAttributesResult(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_cluster_snapshot_attribute' function.
class ModifyDBClusterSnapshotAttributeResult(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_engine_versions' function.
class DBEngineVersionMessage(BaseValidatorModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_instance_automated_backups' function.
class DBInstanceAutomatedBackupMessage(BaseValidatorModel):
    Marker: str
    DBInstanceAutomatedBackups: List[DBInstanceAutomatedBackup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_instance_automated_backup' function.
class DeleteDBInstanceAutomatedBackupResult(BaseValidatorModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_db_instance_automated_backups_replication' function.
class StartDBInstanceAutomatedBackupsReplicationResult(BaseValidatorModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_db_instance_automated_backups_replication' function.
class StopDBInstanceAutomatedBackupsReplicationResult(BaseValidatorModel):
    DBInstanceAutomatedBackup: DBInstanceAutomatedBackup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_proxy_targets' function.
class DescribeDBProxyTargetsResponse(BaseValidatorModel):
    Targets: List[DBProxyTarget]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_db_proxy_targets' function.
class RegisterDBProxyTargetsResponse(BaseValidatorModel):
    DBProxyTargets: List[DBProxyTarget]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_proxy' function.
class CreateDBProxyResponse(BaseValidatorModel):
    DBProxy: DBProxy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_proxy' function.
class DeleteDBProxyResponse(BaseValidatorModel):
    DBProxy: DBProxy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_proxies' function.
class DescribeDBProxiesResponse(BaseValidatorModel):
    DBProxies: List[DBProxy]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_proxy' function.
class ModifyDBProxyResponse(BaseValidatorModel):
    DBProxy: DBProxy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'authorize_db_security_group_ingress' function.
class AuthorizeDBSecurityGroupIngressResult(BaseValidatorModel):
    DBSecurityGroup: DBSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_security_group' function.
class CreateDBSecurityGroupResult(BaseValidatorModel):
    DBSecurityGroup: DBSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_security_groups' function.
class DBSecurityGroupMessage(BaseValidatorModel):
    Marker: str
    DBSecurityGroups: List[DBSecurityGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_db_security_group_ingress' function.
class RevokeDBSecurityGroupIngressResult(BaseValidatorModel):
    DBSecurityGroup: DBSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_snapshot_attributes' function.
class DescribeDBSnapshotAttributesResult(BaseValidatorModel):
    DBSnapshotAttributesResult: DBSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_snapshot_attribute' function.
class ModifyDBSnapshotAttributeResult(BaseValidatorModel):
    DBSnapshotAttributesResult: DBSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_global_cluster' function.
class CreateGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_global_cluster' function.
class DeleteGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'failover_global_cluster' function.
class FailoverGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_global_clusters' function.
class GlobalClustersMessage(BaseValidatorModel):
    Marker: str
    GlobalClusters: List[GlobalCluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_global_cluster' function.
class ModifyGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_from_global_cluster' function.
class RemoveFromGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'switchover_global_cluster' function.
class SwitchoverGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_integrations' function.
class DescribeIntegrationsResponse(BaseValidatorModel):
    Marker: str
    Integrations: List[Integration]
    ResponseMetadata: ResponseMetadata


class OptionGroupOption(BaseValidatorModel):
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
    OptionGroupOptionSettings: Optional[List[OptionGroupOptionSetting]] = None
    OptionGroupOptionVersions: Optional[List[OptionVersion]] = None
    CopyableCrossAccount: Optional[bool] = None


# This class is the input for the 'modify_option_group' function.
class ModifyOptionGroupMessage(BaseValidatorModel):
    OptionGroupName: str
    OptionsToInclude: Optional[List[OptionConfiguration]] = None
    OptionsToRemove: Optional[List[str]] = None
    ApplyImmediately: Optional[bool] = None


class OptionGroup(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    OptionGroupDescription: Optional[str] = None
    EngineName: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    Options: Optional[List[Option]] = None
    AllowsVpcAndNonVpcInstanceMemberships: Optional[bool] = None
    VpcId: Optional[str] = None
    OptionGroupArn: Optional[str] = None
    SourceOptionGroup: Optional[str] = None
    SourceAccountId: Optional[str] = None
    CopyTimestamp: Optional[datetime] = None


class DBSubnetGroup(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    DBSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    DBSubnetGroupArn: Optional[str] = None
    SupportedNetworkTypes: Optional[List[str]] = None


# This class is the input for the 'modify_db_cluster_parameter_group' function.
class ModifyDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Parameters: List[ParameterUnion]


# This class is the input for the 'modify_db_parameter_group' function.
class ModifyDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str
    Parameters: List[ParameterUnion]


# This class is the input for the 'reset_db_cluster_parameter_group' function.
class ResetDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[List[ParameterUnion]] = None


# This class is the input for the 'reset_db_parameter_group' function.
class ResetDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[List[ParameterUnion]] = None


# This class is the output for the 'apply_pending_maintenance_action' function.
class ApplyPendingMaintenanceActionResult(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_pending_maintenance_actions' function.
class PendingMaintenanceActionsMessage(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActions]
    Marker: str
    ResponseMetadata: ResponseMetadata


class MetricQuery(BaseValidatorModel):
    PerformanceInsightsMetricQuery: Optional[PerformanceInsightsMetricQuery] = None


class ValidDBInstanceModificationsMessage(BaseValidatorModel):
    Storage: Optional[List[ValidStorageOptions]] = None
    ValidProcessorFeatures: Optional[List[AvailableProcessorFeature]] = None
    SupportsDedicatedLogVolume: Optional[bool] = None


# This class is the output for the 'purchase_reserved_db_instances_offering' function.
class PurchaseReservedDBInstancesOfferingResult(BaseValidatorModel):
    ReservedDBInstance: ReservedDBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_db_instances' function.
class ReservedDBInstanceMessage(BaseValidatorModel):
    Marker: str
    ReservedDBInstances: List[ReservedDBInstance]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_db_instances_offerings' function.
class ReservedDBInstancesOfferingMessage(BaseValidatorModel):
    Marker: str
    ReservedDBInstancesOfferings: List[ReservedDBInstancesOffering]
    ResponseMetadata: ResponseMetadata


class MetricReference(BaseValidatorModel):
    Name: Optional[str] = None
    ReferenceDetails: Optional[ReferenceDetails] = None


# This class is the output for the 'create_tenant_database' function.
class CreateTenantDatabaseResult(BaseValidatorModel):
    TenantDatabase: TenantDatabase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_tenant_database' function.
class DeleteTenantDatabaseResult(BaseValidatorModel):
    TenantDatabase: TenantDatabase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_tenant_database' function.
class ModifyTenantDatabaseResult(BaseValidatorModel):
    TenantDatabase: TenantDatabase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tenant_databases' function.
class TenantDatabasesMessage(BaseValidatorModel):
    Marker: str
    TenantDatabases: List[TenantDatabase]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster' function.
class CreateDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_clusters' function.
class DBClusterMessage(BaseValidatorModel):
    Marker: str
    DBClusters: List[DBCluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster' function.
class DeleteDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'failover_db_cluster' function.
class FailoverDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_cluster' function.
class ModifyDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'promote_read_replica_db_cluster' function.
class PromoteReadReplicaDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_db_cluster' function.
class RebootDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_cluster_from_s3' function.
class RestoreDBClusterFromS3Result(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_cluster_from_snapshot' function.
class RestoreDBClusterFromSnapshotResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_cluster_to_point_in_time' function.
class RestoreDBClusterToPointInTimeResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_db_cluster' function.
class StartDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_db_cluster' function.
class StopDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_option_group_options' function.
class OptionGroupOptionsMessage(BaseValidatorModel):
    OptionGroupOptions: List[OptionGroupOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_option_group' function.
class CopyOptionGroupResult(BaseValidatorModel):
    OptionGroup: OptionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_option_group' function.
class CreateOptionGroupResult(BaseValidatorModel):
    OptionGroup: OptionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_option_group' function.
class ModifyOptionGroupResult(BaseValidatorModel):
    OptionGroup: OptionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_option_groups' function.
class OptionGroups(BaseValidatorModel):
    OptionGroupsList: List[OptionGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_subnet_group' function.
class CreateDBSubnetGroupResult(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroup
    ResponseMetadata: ResponseMetadata


class DBInstance(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Engine: Optional[str] = None
    DBInstanceStatus: Optional[str] = None
    AutomaticRestartTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[Endpoint] = None
    AllocatedStorage: Optional[int] = None
    InstanceCreateTime: Optional[datetime] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DBSecurityGroups: Optional[List[DBSecurityGroupMembership]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    DBParameterGroups: Optional[List[DBParameterGroupStatus]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroup: Optional[DBSubnetGroup] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValues] = None
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
    OptionGroupMemberships: Optional[List[OptionGroupMembership]] = None
    CharacterSetName: Optional[str] = None
    NcharCharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StatusInfos: Optional[List[DBInstanceStatusInfo]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DBClusterIdentifier: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbiResourceId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DomainMemberships: Optional[List[DomainMembership]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    DBInstanceArn: Optional[str] = None
    Timezone: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    DatabaseInsightsMode: Optional[DatabaseInsightsModeType] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[ProcessorFeature]] = None
    DeletionProtection: Optional[bool] = None
    AssociatedRoles: Optional[List[DBInstanceRole]] = None
    ListenerEndpoint: Optional[Endpoint] = None
    MaxAllocatedStorage: Optional[int] = None
    TagList: Optional[List[Tag]] = None
    DBInstanceAutomatedBackupsReplications: Optional[List[DBInstanceAutomatedBackupsReplication]] = None
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
    MasterUserSecret: Optional[MasterUserSecret] = None
    CertificateDetails: Optional[CertificateDetails] = None
    ReadReplicaSourceDBClusterIdentifier: Optional[str] = None
    PercentProgress: Optional[str] = None
    DedicatedLogVolume: Optional[bool] = None
    IsStorageConfigUpgradeAvailable: Optional[bool] = None
    MultiTenant: Optional[bool] = None
    EngineLifecycleSupport: Optional[str] = None


# This class is the output for the 'describe_db_subnet_groups' function.
class DBSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_subnet_group' function.
class ModifyDBSubnetGroupResult(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_valid_db_instance_modifications' function.
class DescribeValidDBInstanceModificationsResult(BaseValidatorModel):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessage
    ResponseMetadata: ResponseMetadata


class Metric(BaseValidatorModel):
    Name: Optional[str] = None
    References: Optional[List[MetricReference]] = None
    StatisticsDetails: Optional[str] = None
    MetricQuery: Optional[MetricQuery] = None


# This class is the output for the 'create_db_instance_read_replica' function.
class CreateDBInstanceReadReplicaResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_instance' function.
class CreateDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_instances' function.
class DBInstanceMessage(BaseValidatorModel):
    Marker: str
    DBInstances: List[DBInstance]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_instance' function.
class DeleteDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_instance' function.
class ModifyDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'promote_read_replica' function.
class PromoteReadReplicaResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_db_instance' function.
class RebootDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_instance_from_db_snapshot' function.
class RestoreDBInstanceFromDBSnapshotResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_instance_from_s3' function.
class RestoreDBInstanceFromS3Result(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_instance_to_point_in_time' function.
class RestoreDBInstanceToPointInTimeResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_db_instance' function.
class StartDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_db_instance' function.
class StopDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'switchover_read_replica' function.
class SwitchoverReadReplicaResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


class PerformanceIssueDetails(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Metrics: Optional[List[Metric]] = None
    Analysis: Optional[str] = None


class IssueDetails(BaseValidatorModel):
    PerformanceIssueDetails: Optional[PerformanceIssueDetails] = None


class RecommendedAction(BaseValidatorModel):
    ActionId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Operation: Optional[str] = None
    Parameters: Optional[List[RecommendedActionParameter]] = None
    ApplyModes: Optional[List[str]] = None
    Status: Optional[str] = None
    IssueDetails: Optional[IssueDetails] = None
    ContextAttributes: Optional[List[ContextAttribute]] = None


class DBRecommendation(BaseValidatorModel):
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
    RecommendedActions: Optional[List[RecommendedAction]] = None
    Category: Optional[str] = None
    Source: Optional[str] = None
    TypeDetection: Optional[str] = None
    TypeRecommendation: Optional[str] = None
    Impact: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    Links: Optional[List[DocLink]] = None
    IssueDetails: Optional[IssueDetails] = None


# This class is the output for the 'modify_db_recommendation' function.
class DBRecommendationMessage(BaseValidatorModel):
    DBRecommendation: DBRecommendation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_recommendations' function.
class DBRecommendationsMessage(BaseValidatorModel):
    DBRecommendations: List[DBRecommendation]
    Marker: str
    ResponseMetadata: ResponseMetadata