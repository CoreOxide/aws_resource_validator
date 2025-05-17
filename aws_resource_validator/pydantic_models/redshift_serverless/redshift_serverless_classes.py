from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Association(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainCertificateExpiryTime: Optional[datetime] = None
    customDomainName: Optional[str] = None
    workgroupName: Optional[str] = None


class ConfigParameter(BaseValidatorModel):
    parameterKey: Optional[str] = None
    parameterValue: Optional[str] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Snapshot(BaseValidatorModel):
    accountsWithProvisionedRestoreAccess: Optional[List[str]] = None
    accountsWithRestoreAccess: Optional[List[str]] = None
    actualIncrementalBackupSizeInMegaBytes: Optional[float] = None
    adminPasswordSecretArn: Optional[str] = None
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUsername: Optional[str] = None
    backupProgressInMegaBytes: Optional[float] = None
    currentBackupRateInMegaBytesPerSecond: Optional[float] = None
    elapsedTimeInSeconds: Optional[int] = None
    estimatedSecondsToCompletion: Optional[int] = None
    kmsKeyId: Optional[str] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotCreateTime: Optional[datetime] = None
    snapshotName: Optional[str] = None
    snapshotRemainingDays: Optional[int] = None
    snapshotRetentionPeriod: Optional[int] = None
    snapshotRetentionStartTime: Optional[datetime] = None
    status: Optional[SnapshotStatusType] = None
    totalBackupSizeInMegaBytes: Optional[float] = None


# This class is the input for the 'create_custom_domain_association' function.
class CreateCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str


# This class is the input for the 'create_endpoint_access' function.
class CreateEndpointAccessRequest(BaseValidatorModel):
    endpointName: str
    subnetIds: List[str]
    workgroupName: str
    ownerAccount: Optional[str] = None
    vpcSecurityGroupIds: Optional[List[str]] = None


class Namespace(BaseValidatorModel):
    adminPasswordSecretArn: Optional[str] = None
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUsername: Optional[str] = None
    creationDate: Optional[datetime] = None
    dbName: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[List[LogExportType]] = None
    namespaceArn: Optional[str] = None
    namespaceId: Optional[str] = None
    namespaceName: Optional[str] = None
    status: Optional[NamespaceStatusType] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'create_snapshot_copy_configuration' function.
class CreateSnapshotCopyConfigurationRequest(BaseValidatorModel):
    destinationRegion: str
    namespaceName: str
    destinationKmsKeyId: Optional[str] = None
    snapshotRetentionPeriod: Optional[int] = None


class SnapshotCopyConfiguration(BaseValidatorModel):
    destinationKmsKeyId: Optional[str] = None
    destinationRegion: Optional[str] = None
    namespaceName: Optional[str] = None
    snapshotCopyConfigurationArn: Optional[str] = None
    snapshotCopyConfigurationId: Optional[str] = None
    snapshotRetentionPeriod: Optional[int] = None


# This class is the input for the 'create_usage_limit' function.
class CreateUsageLimitRequest(BaseValidatorModel):
    amount: int
    resourceArn: str
    usageType: UsageLimitUsageTypeType
    breachAction: Optional[UsageLimitBreachActionType] = None
    period: Optional[UsageLimitPeriodType] = None


class UsageLimit(BaseValidatorModel):
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None
    period: Optional[UsageLimitPeriodType] = None
    resourceArn: Optional[str] = None
    usageLimitArn: Optional[str] = None
    usageLimitId: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None


class PerformanceTarget(BaseValidatorModel):
    level: Optional[int] = None
    status: Optional[PerformanceTargetStatusType] = None


class DeleteCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainName: str
    workgroupName: str


# This class is the input for the 'delete_endpoint_access' function.
class DeleteEndpointAccessRequest(BaseValidatorModel):
    endpointName: str


# This class is the input for the 'delete_namespace' function.
class DeleteNamespaceRequest(BaseValidatorModel):
    namespaceName: str
    finalSnapshotName: Optional[str] = None
    finalSnapshotRetentionPeriod: Optional[int] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'delete_scheduled_action' function.
class DeleteScheduledActionRequest(BaseValidatorModel):
    scheduledActionName: str


# This class is the input for the 'delete_snapshot_copy_configuration' function.
class DeleteSnapshotCopyConfigurationRequest(BaseValidatorModel):
    snapshotCopyConfigurationId: str


# This class is the input for the 'delete_snapshot' function.
class DeleteSnapshotRequest(BaseValidatorModel):
    snapshotName: str


# This class is the input for the 'delete_usage_limit' function.
class DeleteUsageLimitRequest(BaseValidatorModel):
    usageLimitId: str


# This class is the input for the 'delete_workgroup' function.
class DeleteWorkgroupRequest(BaseValidatorModel):
    workgroupName: str


class VpcSecurityGroupMembership(BaseValidatorModel):
    status: Optional[str] = None
    vpcSecurityGroupId: Optional[str] = None


# This class is the input for the 'get_credentials' function.
class GetCredentialsRequest(BaseValidatorModel):
    customDomainName: Optional[str] = None
    dbName: Optional[str] = None
    durationSeconds: Optional[int] = None
    workgroupName: Optional[str] = None


# This class is the input for the 'get_custom_domain_association' function.
class GetCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainName: str
    workgroupName: str


# This class is the input for the 'get_endpoint_access' function.
class GetEndpointAccessRequest(BaseValidatorModel):
    endpointName: str


# This class is the input for the 'get_namespace' function.
class GetNamespaceRequest(BaseValidatorModel):
    namespaceName: str


# This class is the input for the 'get_recovery_point' function.
class GetRecoveryPointRequest(BaseValidatorModel):
    recoveryPointId: str


class RecoveryPoint(BaseValidatorModel):
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    recoveryPointCreateTime: Optional[datetime] = None
    recoveryPointId: Optional[str] = None
    totalSizeInMegaBytes: Optional[float] = None
    workgroupName: Optional[str] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


class ResourcePolicy(BaseValidatorModel):
    policy: Optional[str] = None
    resourceArn: Optional[str] = None


# This class is the input for the 'get_scheduled_action' function.
class GetScheduledActionRequest(BaseValidatorModel):
    scheduledActionName: str


# This class is the input for the 'get_snapshot' function.
class GetSnapshotRequest(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None


# This class is the input for the 'get_table_restore_status' function.
class GetTableRestoreStatusRequest(BaseValidatorModel):
    tableRestoreRequestId: str


class TableRestoreStatus(BaseValidatorModel):
    message: Optional[str] = None
    namespaceName: Optional[str] = None
    newTableName: Optional[str] = None
    progressInMegaBytes: Optional[int] = None
    recoveryPointId: Optional[str] = None
    requestTime: Optional[datetime] = None
    snapshotName: Optional[str] = None
    sourceDatabaseName: Optional[str] = None
    sourceSchemaName: Optional[str] = None
    sourceTableName: Optional[str] = None
    status: Optional[str] = None
    tableRestoreRequestId: Optional[str] = None
    targetDatabaseName: Optional[str] = None
    targetSchemaName: Optional[str] = None
    totalDataInMegaBytes: Optional[int] = None
    workgroupName: Optional[str] = None


# This class is the input for the 'get_track' function.
class GetTrackRequest(BaseValidatorModel):
    trackName: str


# This class is the input for the 'get_usage_limit' function.
class GetUsageLimitRequest(BaseValidatorModel):
    usageLimitId: str


# This class is the input for the 'get_workgroup' function.
class GetWorkgroupRequest(BaseValidatorModel):
    workgroupName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_custom_domain_associations' function.
class ListCustomDomainAssociationsRequest(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_endpoint_access' function.
class ListEndpointAccessRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None


# This class is the input for the 'list_managed_workgroups' function.
class ListManagedWorkgroupsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sourceArn: Optional[str] = None


class ManagedWorkgroupListItem(BaseValidatorModel):
    creationDate: Optional[datetime] = None
    managedWorkgroupId: Optional[str] = None
    managedWorkgroupName: Optional[str] = None
    sourceArn: Optional[str] = None
    status: Optional[ManagedWorkgroupStatusType] = None


# This class is the input for the 'list_namespaces' function.
class ListNamespacesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_scheduled_actions' function.
class ListScheduledActionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None


class ScheduledActionAssociation(BaseValidatorModel):
    namespaceName: Optional[str] = None
    scheduledActionName: Optional[str] = None


# This class is the input for the 'list_snapshot_copy_configurations' function.
class ListSnapshotCopyConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_table_restore_status' function.
class ListTableRestoreStatusRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    workgroupName: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_tracks' function.
class ListTracksRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_usage_limits' function.
class ListUsageLimitsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None


# This class is the input for the 'list_workgroups' function.
class ListWorkgroupsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    ipv6Address: Optional[str] = None
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    subnetId: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    policy: str
    resourceArn: str


# This class is the input for the 'restore_from_recovery_point' function.
class RestoreFromRecoveryPointRequest(BaseValidatorModel):
    namespaceName: str
    recoveryPointId: str
    workgroupName: str


# This class is the input for the 'restore_from_snapshot' function.
class RestoreFromSnapshotRequest(BaseValidatorModel):
    namespaceName: str
    workgroupName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    manageAdminPassword: Optional[bool] = None
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None


# This class is the input for the 'restore_table_from_recovery_point' function.
class RestoreTableFromRecoveryPointRequest(BaseValidatorModel):
    namespaceName: str
    newTableName: str
    recoveryPointId: str
    sourceDatabaseName: str
    sourceTableName: str
    workgroupName: str
    activateCaseSensitiveIdentifier: Optional[bool] = None
    sourceSchemaName: Optional[str] = None
    targetDatabaseName: Optional[str] = None
    targetSchemaName: Optional[str] = None


# This class is the input for the 'restore_table_from_snapshot' function.
class RestoreTableFromSnapshotRequest(BaseValidatorModel):
    namespaceName: str
    newTableName: str
    snapshotName: str
    sourceDatabaseName: str
    sourceTableName: str
    workgroupName: str
    activateCaseSensitiveIdentifier: Optional[bool] = None
    sourceSchemaName: Optional[str] = None
    targetDatabaseName: Optional[str] = None
    targetSchemaName: Optional[str] = None


class ScheduleOutput(BaseValidatorModel):
    at: Optional[datetime] = None
    cron: Optional[str] = None


class UpdateTarget(BaseValidatorModel):
    trackName: Optional[str] = None
    workgroupVersion: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_custom_domain_association' function.
class UpdateCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str


# This class is the input for the 'update_endpoint_access' function.
class UpdateEndpointAccessRequest(BaseValidatorModel):
    endpointName: str
    vpcSecurityGroupIds: Optional[List[str]] = None


# This class is the input for the 'update_namespace' function.
class UpdateNamespaceRequest(BaseValidatorModel):
    namespaceName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUserPassword: Optional[str] = None
    adminUsername: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[List[LogExportType]] = None
    manageAdminPassword: Optional[bool] = None


# This class is the input for the 'update_snapshot_copy_configuration' function.
class UpdateSnapshotCopyConfigurationRequest(BaseValidatorModel):
    snapshotCopyConfigurationId: str
    snapshotRetentionPeriod: Optional[int] = None


# This class is the input for the 'update_snapshot' function.
class UpdateSnapshotRequest(BaseValidatorModel):
    snapshotName: str
    retentionPeriod: Optional[int] = None


# This class is the input for the 'update_usage_limit' function.
class UpdateUsageLimitRequest(BaseValidatorModel):
    usageLimitId: str
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None


# This class is the input for the 'convert_recovery_point_to_snapshot' function.
class ConvertRecoveryPointToSnapshotRequest(BaseValidatorModel):
    recoveryPointId: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_namespace' function.
class CreateNamespaceRequest(BaseValidatorModel):
    namespaceName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUserPassword: Optional[str] = None
    adminUsername: Optional[str] = None
    dbName: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[List[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[List[LogExportType]] = None
    manageAdminPassword: Optional[bool] = None
    redshiftIdcApplicationArn: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotRequest(BaseValidatorModel):
    namespaceName: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[Tag]] = None


class CreateSnapshotScheduleActionParametersOutput(BaseValidatorModel):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[Tag]] = None


class CreateSnapshotScheduleActionParameters(BaseValidatorModel):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the output for the 'create_custom_domain_association' function.
class CreateCustomDomainAssociationResponse(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_credentials' function.
class GetCredentialsResponse(BaseValidatorModel):
    dbPassword: str
    dbUser: str
    expiration: datetime
    nextRefreshTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_custom_domain_association' function.
class GetCustomDomainAssociationResponse(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_custom_domain_associations' function.
class ListCustomDomainAssociationsResponse(BaseValidatorModel):
    associations: List[Association]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_custom_domain_association' function.
class UpdateCustomDomainAssociationResponse(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'convert_recovery_point_to_snapshot' function.
class ConvertRecoveryPointToSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_snapshot' function.
class CreateSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot' function.
class DeleteSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_snapshot' function.
class GetSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_snapshots' function.
class ListSnapshotsResponse(BaseValidatorModel):
    snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_snapshot' function.
class UpdateSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_namespace' function.
class CreateNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_namespace' function.
class DeleteNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_namespace' function.
class GetNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_namespaces' function.
class ListNamespacesResponse(BaseValidatorModel):
    namespaces: List[Namespace]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'restore_from_recovery_point' function.
class RestoreFromRecoveryPointResponse(BaseValidatorModel):
    namespace: Namespace
    recoveryPointId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_from_snapshot' function.
class RestoreFromSnapshotResponse(BaseValidatorModel):
    namespace: Namespace
    ownerAccount: str
    snapshotName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_namespace' function.
class UpdateNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'list_recovery_points' function.
class ListRecoveryPointsRequest(BaseValidatorModel):
    endTime: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    startTime: Optional[Timestamp] = None


# This class is the input for the 'list_snapshots' function.
class ListSnapshotsRequest(BaseValidatorModel):
    endTime: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[Timestamp] = None


class Schedule(BaseValidatorModel):
    at: Optional[Timestamp] = None
    cron: Optional[str] = None


# This class is the output for the 'create_snapshot_copy_configuration' function.
class CreateSnapshotCopyConfigurationResponse(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot_copy_configuration' function.
class DeleteSnapshotCopyConfigurationResponse(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_snapshot_copy_configurations' function.
class ListSnapshotCopyConfigurationsResponse(BaseValidatorModel):
    snapshotCopyConfigurations: List[SnapshotCopyConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_snapshot_copy_configuration' function.
class UpdateSnapshotCopyConfigurationResponse(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_usage_limit' function.
class CreateUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_usage_limit' function.
class DeleteUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_usage_limit' function.
class GetUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_usage_limits' function.
class ListUsageLimitsResponse(BaseValidatorModel):
    usageLimits: List[UsageLimit]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_usage_limit' function.
class UpdateUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_workgroup' function.
class CreateWorkgroupRequest(BaseValidatorModel):
    namespaceName: str
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[List[ConfigParameter]] = None
    enhancedVpcRouting: Optional[bool] = None
    ipAddressType: Optional[str] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    pricePerformanceTarget: Optional[PerformanceTarget] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None
    trackName: Optional[str] = None


# This class is the input for the 'update_workgroup' function.
class UpdateWorkgroupRequest(BaseValidatorModel):
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[List[ConfigParameter]] = None
    enhancedVpcRouting: Optional[bool] = None
    ipAddressType: Optional[str] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    pricePerformanceTarget: Optional[PerformanceTarget] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    trackName: Optional[str] = None


# This class is the output for the 'get_recovery_point' function.
class GetRecoveryPointResponse(BaseValidatorModel):
    recoveryPoint: RecoveryPoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_recovery_points' function.
class ListRecoveryPointsResponse(BaseValidatorModel):
    recoveryPoints: List[RecoveryPoint]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    resourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    resourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table_restore_status' function.
class GetTableRestoreStatusResponse(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_table_restore_status' function.
class ListTableRestoreStatusResponse(BaseValidatorModel):
    tableRestoreStatuses: List[TableRestoreStatus]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'restore_table_from_recovery_point' function.
class RestoreTableFromRecoveryPointResponse(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_table_from_snapshot' function.
class RestoreTableFromSnapshotResponse(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


class ListCustomDomainAssociationsRequestPaginate(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEndpointAccessRequestPaginate(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedWorkgroupsRequestPaginate(BaseValidatorModel):
    sourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecoveryPointsRequestPaginate(BaseValidatorModel):
    endTime: Optional[Timestamp] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    startTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScheduledActionsRequestPaginate(BaseValidatorModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSnapshotCopyConfigurationsRequestPaginate(BaseValidatorModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSnapshotsRequestPaginate(BaseValidatorModel):
    endTime: Optional[Timestamp] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTableRestoreStatusRequestPaginate(BaseValidatorModel):
    namespaceName: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTracksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsageLimitsRequestPaginate(BaseValidatorModel):
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkgroupsRequestPaginate(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_managed_workgroups' function.
class ListManagedWorkgroupsResponse(BaseValidatorModel):
    managedWorkgroups: List[ManagedWorkgroupListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_scheduled_actions' function.
class ListScheduledActionsResponse(BaseValidatorModel):
    scheduledActions: List[ScheduledActionAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class VpcEndpoint(BaseValidatorModel):
    networkInterfaces: Optional[List[NetworkInterface]] = None
    vpcEndpointId: Optional[str] = None
    vpcId: Optional[str] = None


class ServerlessTrack(BaseValidatorModel):
    trackName: Optional[str] = None
    updateTargets: Optional[List[UpdateTarget]] = None
    workgroupVersion: Optional[str] = None


class TargetActionOutput(BaseValidatorModel):
    createSnapshot: Optional[CreateSnapshotScheduleActionParametersOutput] = None


class TargetAction(BaseValidatorModel):
    createSnapshot: Optional[CreateSnapshotScheduleActionParameters] = None

ScheduleUnion = Union[Schedule, ScheduleOutput]


class EndpointAccess(BaseValidatorModel):
    address: Optional[str] = None
    endpointArn: Optional[str] = None
    endpointCreateTime: Optional[datetime] = None
    endpointName: Optional[str] = None
    endpointStatus: Optional[str] = None
    port: Optional[int] = None
    subnetIds: Optional[List[str]] = None
    vpcEndpoint: Optional[VpcEndpoint] = None
    vpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    workgroupName: Optional[str] = None


class Endpoint(BaseValidatorModel):
    address: Optional[str] = None
    port: Optional[int] = None
    vpcEndpoints: Optional[List[VpcEndpoint]] = None


# This class is the output for the 'get_track' function.
class GetTrackResponse(BaseValidatorModel):
    track: ServerlessTrack
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tracks' function.
class ListTracksResponse(BaseValidatorModel):
    tracks: List[ServerlessTrack]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ScheduledActionResponse(BaseValidatorModel):
    endTime: Optional[datetime] = None
    namespaceName: Optional[str] = None
    nextInvocations: Optional[List[datetime]] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleOutput] = None
    scheduledActionDescription: Optional[str] = None
    scheduledActionName: Optional[str] = None
    scheduledActionUuid: Optional[str] = None
    startTime: Optional[datetime] = None
    state: Optional[StateType] = None
    targetAction: Optional[TargetActionOutput] = None

TargetActionUnion = Union[TargetAction, TargetActionOutput]


# This class is the output for the 'create_endpoint_access' function.
class CreateEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_endpoint_access' function.
class DeleteEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_endpoint_access' function.
class GetEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_endpoint_access' function.
class ListEndpointAccessResponse(BaseValidatorModel):
    endpoints: List[EndpointAccess]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_endpoint_access' function.
class UpdateEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


class Workgroup(BaseValidatorModel):
    baseCapacity: Optional[int] = None
    configParameters: Optional[List[ConfigParameter]] = None
    creationDate: Optional[datetime] = None
    crossAccountVpcs: Optional[List[str]] = None
    customDomainCertificateArn: Optional[str] = None
    customDomainCertificateExpiryTime: Optional[datetime] = None
    customDomainName: Optional[str] = None
    endpoint: Optional[Endpoint] = None
    enhancedVpcRouting: Optional[bool] = None
    ipAddressType: Optional[str] = None
    maxCapacity: Optional[int] = None
    namespaceName: Optional[str] = None
    patchVersion: Optional[str] = None
    pendingTrackName: Optional[str] = None
    port: Optional[int] = None
    pricePerformanceTarget: Optional[PerformanceTarget] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[WorkgroupStatusType] = None
    subnetIds: Optional[List[str]] = None
    trackName: Optional[str] = None
    workgroupArn: Optional[str] = None
    workgroupId: Optional[str] = None
    workgroupName: Optional[str] = None
    workgroupVersion: Optional[str] = None


# This class is the output for the 'create_scheduled_action' function.
class CreateScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_scheduled_action' function.
class DeleteScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_scheduled_action' function.
class GetScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_scheduled_action' function.
class UpdateScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_scheduled_action' function.
class CreateScheduledActionRequest(BaseValidatorModel):
    namespaceName: str
    roleArn: str
    schedule: ScheduleUnion
    scheduledActionName: str
    targetAction: TargetActionUnion
    enabled: Optional[bool] = None
    endTime: Optional[Timestamp] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[Timestamp] = None


# This class is the input for the 'update_scheduled_action' function.
class UpdateScheduledActionRequest(BaseValidatorModel):
    scheduledActionName: str
    enabled: Optional[bool] = None
    endTime: Optional[Timestamp] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleUnion] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[Timestamp] = None
    targetAction: Optional[TargetActionUnion] = None


# This class is the output for the 'create_workgroup' function.
class CreateWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_workgroup' function.
class DeleteWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_workgroup' function.
class GetWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_workgroups' function.
class ListWorkgroupsResponse(BaseValidatorModel):
    workgroups: List[Workgroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_workgroup' function.
class UpdateWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata