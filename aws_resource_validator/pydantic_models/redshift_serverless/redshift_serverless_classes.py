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


class CreateCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str


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


class DeleteEndpointAccessRequest(BaseValidatorModel):
    endpointName: str


class DeleteNamespaceRequest(BaseValidatorModel):
    namespaceName: str
    finalSnapshotName: Optional[str] = None
    finalSnapshotRetentionPeriod: Optional[int] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


class DeleteScheduledActionRequest(BaseValidatorModel):
    scheduledActionName: str


class DeleteSnapshotCopyConfigurationRequest(BaseValidatorModel):
    snapshotCopyConfigurationId: str


class DeleteSnapshotRequest(BaseValidatorModel):
    snapshotName: str


class DeleteUsageLimitRequest(BaseValidatorModel):
    usageLimitId: str


class DeleteWorkgroupRequest(BaseValidatorModel):
    workgroupName: str


class VpcSecurityGroupMembership(BaseValidatorModel):
    status: Optional[str] = None
    vpcSecurityGroupId: Optional[str] = None


class GetCredentialsRequest(BaseValidatorModel):
    customDomainName: Optional[str] = None
    dbName: Optional[str] = None
    durationSeconds: Optional[int] = None
    workgroupName: Optional[str] = None


class GetCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainName: str
    workgroupName: str


class GetEndpointAccessRequest(BaseValidatorModel):
    endpointName: str


class GetNamespaceRequest(BaseValidatorModel):
    namespaceName: str


class GetRecoveryPointRequest(BaseValidatorModel):
    recoveryPointId: str


class RecoveryPoint(BaseValidatorModel):
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    recoveryPointCreateTime: Optional[datetime] = None
    recoveryPointId: Optional[str] = None
    totalSizeInMegaBytes: Optional[float] = None
    workgroupName: Optional[str] = None


class GetResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


class ResourcePolicy(BaseValidatorModel):
    policy: Optional[str] = None
    resourceArn: Optional[str] = None


class GetScheduledActionRequest(BaseValidatorModel):
    scheduledActionName: str


class GetSnapshotRequest(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None


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


class GetTrackRequest(BaseValidatorModel):
    trackName: str


class GetUsageLimitRequest(BaseValidatorModel):
    usageLimitId: str


class GetWorkgroupRequest(BaseValidatorModel):
    workgroupName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCustomDomainAssociationsRequest(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEndpointAccessRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None


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


class ListNamespacesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListScheduledActionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None


class ScheduledActionAssociation(BaseValidatorModel):
    namespaceName: Optional[str] = None
    scheduledActionName: Optional[str] = None


class ListSnapshotCopyConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None


class ListTableRestoreStatusRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    workgroupName: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTracksRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListUsageLimitsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None


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


class PutResourcePolicyRequest(BaseValidatorModel):
    policy: str
    resourceArn: str


class RestoreFromRecoveryPointRequest(BaseValidatorModel):
    namespaceName: str
    recoveryPointId: str
    workgroupName: str


class RestoreFromSnapshotRequest(BaseValidatorModel):
    namespaceName: str
    workgroupName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    manageAdminPassword: Optional[bool] = None
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None


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


class UpdateCustomDomainAssociationRequest(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str


class UpdateEndpointAccessRequest(BaseValidatorModel):
    endpointName: str
    vpcSecurityGroupIds: Optional[List[str]] = None


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


class UpdateSnapshotCopyConfigurationRequest(BaseValidatorModel):
    snapshotCopyConfigurationId: str
    snapshotRetentionPeriod: Optional[int] = None


class UpdateSnapshotRequest(BaseValidatorModel):
    snapshotName: str
    retentionPeriod: Optional[int] = None


class UpdateUsageLimitRequest(BaseValidatorModel):
    usageLimitId: str
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None


class ConvertRecoveryPointToSnapshotRequest(BaseValidatorModel):
    recoveryPointId: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[Tag]] = None


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


class CreateCustomDomainAssociationResponse(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadata


class GetCredentialsResponse(BaseValidatorModel):
    dbPassword: str
    dbUser: str
    expiration: datetime
    nextRefreshTime: datetime
    ResponseMetadata: ResponseMetadata


class GetCustomDomainAssociationResponse(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadata


class ListCustomDomainAssociationsResponse(BaseValidatorModel):
    associations: List[Association]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateCustomDomainAssociationResponse(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadata


class ConvertRecoveryPointToSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CreateSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class GetSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class ListSnapshotsResponse(BaseValidatorModel):
    snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateSnapshotResponse(BaseValidatorModel):
    snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CreateNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


class DeleteNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


class GetNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


class ListNamespacesResponse(BaseValidatorModel):
    namespaces: List[Namespace]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RestoreFromRecoveryPointResponse(BaseValidatorModel):
    namespace: Namespace
    recoveryPointId: str
    ResponseMetadata: ResponseMetadata


class RestoreFromSnapshotResponse(BaseValidatorModel):
    namespace: Namespace
    ownerAccount: str
    snapshotName: str
    ResponseMetadata: ResponseMetadata


class UpdateNamespaceResponse(BaseValidatorModel):
    namespace: Namespace
    ResponseMetadata: ResponseMetadata


class ListRecoveryPointsRequest(BaseValidatorModel):
    endTime: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    startTime: Optional[Timestamp] = None


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


class CreateSnapshotCopyConfigurationResponse(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfiguration
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotCopyConfigurationResponse(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfiguration
    ResponseMetadata: ResponseMetadata


class ListSnapshotCopyConfigurationsResponse(BaseValidatorModel):
    snapshotCopyConfigurations: List[SnapshotCopyConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateSnapshotCopyConfigurationResponse(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfiguration
    ResponseMetadata: ResponseMetadata


class CreateUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


class DeleteUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


class GetUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


class ListUsageLimitsResponse(BaseValidatorModel):
    usageLimits: List[UsageLimit]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateUsageLimitResponse(BaseValidatorModel):
    usageLimit: UsageLimit
    ResponseMetadata: ResponseMetadata


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


class GetRecoveryPointResponse(BaseValidatorModel):
    recoveryPoint: RecoveryPoint
    ResponseMetadata: ResponseMetadata


class ListRecoveryPointsResponse(BaseValidatorModel):
    recoveryPoints: List[RecoveryPoint]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetResourcePolicyResponse(BaseValidatorModel):
    resourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    resourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class GetTableRestoreStatusResponse(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


class ListTableRestoreStatusResponse(BaseValidatorModel):
    tableRestoreStatuses: List[TableRestoreStatus]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RestoreTableFromRecoveryPointResponse(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


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


class ListManagedWorkgroupsResponse(BaseValidatorModel):
    managedWorkgroups: List[ManagedWorkgroupListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class GetTrackResponse(BaseValidatorModel):
    track: ServerlessTrack
    ResponseMetadata: ResponseMetadata


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


class CreateEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


class DeleteEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


class GetEndpointAccessResponse(BaseValidatorModel):
    endpoint: EndpointAccess
    ResponseMetadata: ResponseMetadata


class ListEndpointAccessResponse(BaseValidatorModel):
    endpoints: List[EndpointAccess]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class CreateScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


class DeleteScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


class GetScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


class UpdateScheduledActionResponse(BaseValidatorModel):
    scheduledAction: ScheduledActionResponse
    ResponseMetadata: ResponseMetadata


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


class UpdateScheduledActionRequest(BaseValidatorModel):
    scheduledActionName: str
    enabled: Optional[bool] = None
    endTime: Optional[Timestamp] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleUnion] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[Timestamp] = None
    targetAction: Optional[TargetActionUnion] = None


class CreateWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata


class DeleteWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata


class GetWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata


class ListWorkgroupsResponse(BaseValidatorModel):
    workgroups: List[Workgroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateWorkgroupResponse(BaseValidatorModel):
    workgroup: Workgroup
    ResponseMetadata: ResponseMetadata