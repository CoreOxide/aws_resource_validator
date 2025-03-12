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
from aws_resource_validator.pydantic_models.redshift_serverless_constants import *

class AssociationTypeDef(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainCertificateExpiryTime: Optional[datetime] = None
    customDomainName: Optional[str] = None
    workgroupName: Optional[str] = None


class ConfigParameterTypeDef(BaseValidatorModel):
    parameterKey: Optional[str] = None
    parameterValue: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SnapshotTypeDef(BaseValidatorModel):
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


class CreateCustomDomainAssociationRequestTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str


class CreateEndpointAccessRequestTypeDef(BaseValidatorModel):
    endpointName: str
    subnetIds: Sequence[str]
    workgroupName: str
    ownerAccount: Optional[str] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None


class NamespaceTypeDef(BaseValidatorModel):
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


class CreateSnapshotCopyConfigurationRequestTypeDef(BaseValidatorModel):
    destinationRegion: str
    namespaceName: str
    destinationKmsKeyId: Optional[str] = None
    snapshotRetentionPeriod: Optional[int] = None


class SnapshotCopyConfigurationTypeDef(BaseValidatorModel):
    destinationKmsKeyId: Optional[str] = None
    destinationRegion: Optional[str] = None
    namespaceName: Optional[str] = None
    snapshotCopyConfigurationArn: Optional[str] = None
    snapshotCopyConfigurationId: Optional[str] = None
    snapshotRetentionPeriod: Optional[int] = None


class CreateUsageLimitRequestTypeDef(BaseValidatorModel):
    amount: int
    resourceArn: str
    usageType: UsageLimitUsageTypeType
    breachAction: Optional[UsageLimitBreachActionType] = None
    period: Optional[UsageLimitPeriodType] = None


class UsageLimitTypeDef(BaseValidatorModel):
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None
    period: Optional[UsageLimitPeriodType] = None
    resourceArn: Optional[str] = None
    usageLimitArn: Optional[str] = None
    usageLimitId: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None


class PerformanceTargetTypeDef(BaseValidatorModel):
    level: Optional[int] = None
    status: Optional[PerformanceTargetStatusType] = None


class DeleteCustomDomainAssociationRequestTypeDef(BaseValidatorModel):
    customDomainName: str
    workgroupName: str


class DeleteEndpointAccessRequestTypeDef(BaseValidatorModel):
    endpointName: str


class DeleteNamespaceRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    finalSnapshotName: Optional[str] = None
    finalSnapshotRetentionPeriod: Optional[int] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class DeleteScheduledActionRequestTypeDef(BaseValidatorModel):
    scheduledActionName: str


class DeleteSnapshotCopyConfigurationRequestTypeDef(BaseValidatorModel):
    snapshotCopyConfigurationId: str


class DeleteSnapshotRequestTypeDef(BaseValidatorModel):
    snapshotName: str


class DeleteUsageLimitRequestTypeDef(BaseValidatorModel):
    usageLimitId: str


class DeleteWorkgroupRequestTypeDef(BaseValidatorModel):
    workgroupName: str


class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    status: Optional[str] = None
    vpcSecurityGroupId: Optional[str] = None


class GetCredentialsRequestTypeDef(BaseValidatorModel):
    customDomainName: Optional[str] = None
    dbName: Optional[str] = None
    durationSeconds: Optional[int] = None
    workgroupName: Optional[str] = None


class GetCustomDomainAssociationRequestTypeDef(BaseValidatorModel):
    customDomainName: str
    workgroupName: str


class GetEndpointAccessRequestTypeDef(BaseValidatorModel):
    endpointName: str


class GetNamespaceRequestTypeDef(BaseValidatorModel):
    namespaceName: str


class GetRecoveryPointRequestTypeDef(BaseValidatorModel):
    recoveryPointId: str


class RecoveryPointTypeDef(BaseValidatorModel):
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    recoveryPointCreateTime: Optional[datetime] = None
    recoveryPointId: Optional[str] = None
    totalSizeInMegaBytes: Optional[float] = None
    workgroupName: Optional[str] = None


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ResourcePolicyTypeDef(BaseValidatorModel):
    policy: Optional[str] = None
    resourceArn: Optional[str] = None


class GetScheduledActionRequestTypeDef(BaseValidatorModel):
    scheduledActionName: str


class GetSnapshotRequestTypeDef(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None


class GetTableRestoreStatusRequestTypeDef(BaseValidatorModel):
    tableRestoreRequestId: str


class TableRestoreStatusTypeDef(BaseValidatorModel):
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


class GetTrackRequestTypeDef(BaseValidatorModel):
    trackName: str


class GetUsageLimitRequestTypeDef(BaseValidatorModel):
    usageLimitId: str


class GetWorkgroupRequestTypeDef(BaseValidatorModel):
    workgroupName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCustomDomainAssociationsRequestTypeDef(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEndpointAccessRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None


class ListManagedWorkgroupsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sourceArn: Optional[str] = None


class ManagedWorkgroupListItemTypeDef(BaseValidatorModel):
    creationDate: Optional[datetime] = None
    managedWorkgroupId: Optional[str] = None
    managedWorkgroupName: Optional[str] = None
    sourceArn: Optional[str] = None
    status: Optional[ManagedWorkgroupStatusType] = None


class ListNamespacesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListScheduledActionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None


class ScheduledActionAssociationTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    scheduledActionName: Optional[str] = None


class ListSnapshotCopyConfigurationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None


class ListTableRestoreStatusRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    workgroupName: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTracksRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListUsageLimitsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None


class ListWorkgroupsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    ipv6Address: Optional[str] = None
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    subnetId: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str


class RestoreFromRecoveryPointRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    recoveryPointId: str
    workgroupName: str


class RestoreFromSnapshotRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    workgroupName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    manageAdminPassword: Optional[bool] = None
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None


class RestoreTableFromRecoveryPointRequestTypeDef(BaseValidatorModel):
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


class RestoreTableFromSnapshotRequestTypeDef(BaseValidatorModel):
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


class ScheduleOutputTypeDef(BaseValidatorModel):
    at: Optional[datetime] = None
    cron: Optional[str] = None


class UpdateTargetTypeDef(BaseValidatorModel):
    trackName: Optional[str] = None
    workgroupVersion: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateCustomDomainAssociationRequestTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str


class UpdateEndpointAccessRequestTypeDef(BaseValidatorModel):
    endpointName: str
    vpcSecurityGroupIds: Optional[Sequence[str]] = None


class UpdateNamespaceRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUserPassword: Optional[str] = None
    adminUsername: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[Sequence[LogExportType]] = None
    manageAdminPassword: Optional[bool] = None


class UpdateSnapshotCopyConfigurationRequestTypeDef(BaseValidatorModel):
    snapshotCopyConfigurationId: str
    snapshotRetentionPeriod: Optional[int] = None


class UpdateSnapshotRequestTypeDef(BaseValidatorModel):
    snapshotName: str
    retentionPeriod: Optional[int] = None


class UpdateUsageLimitRequestTypeDef(BaseValidatorModel):
    usageLimitId: str
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None


class ConvertRecoveryPointToSnapshotRequestTypeDef(BaseValidatorModel):
    recoveryPointId: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateNamespaceRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUserPassword: Optional[str] = None
    adminUsername: Optional[str] = None
    dbName: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[Sequence[LogExportType]] = None
    manageAdminPassword: Optional[bool] = None
    redshiftIdcApplicationArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateSnapshotRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateSnapshotScheduleActionParametersOutputTypeDef(BaseValidatorModel):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[TagTypeDef]] = None


class CreateSnapshotScheduleActionParametersTypeDef(BaseValidatorModel):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateCustomDomainAssociationResponseTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCredentialsResponseTypeDef(BaseValidatorModel):
    dbPassword: str
    dbUser: str
    expiration: datetime
    nextRefreshTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetCustomDomainAssociationResponseTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomDomainAssociationsResponseTypeDef(BaseValidatorModel):
    associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCustomDomainAssociationResponseTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ConvertRecoveryPointToSnapshotResponseTypeDef(BaseValidatorModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSnapshotResponseTypeDef(BaseValidatorModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSnapshotResponseTypeDef(BaseValidatorModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSnapshotResponseTypeDef(BaseValidatorModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSnapshotsResponseTypeDef(BaseValidatorModel):
    snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateSnapshotResponseTypeDef(BaseValidatorModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNamespaceResponseTypeDef(BaseValidatorModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteNamespaceResponseTypeDef(BaseValidatorModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetNamespaceResponseTypeDef(BaseValidatorModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListNamespacesResponseTypeDef(BaseValidatorModel):
    namespaces: List[NamespaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RestoreFromRecoveryPointResponseTypeDef(BaseValidatorModel):
    namespace: NamespaceTypeDef
    recoveryPointId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreFromSnapshotResponseTypeDef(BaseValidatorModel):
    namespace: NamespaceTypeDef
    ownerAccount: str
    snapshotName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNamespaceResponseTypeDef(BaseValidatorModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListRecoveryPointsRequestTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None


class ListSnapshotsRequestTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None


class ScheduleTypeDef(BaseValidatorModel):
    at: Optional[TimestampTypeDef] = None
    cron: Optional[str] = None


class CreateSnapshotCopyConfigurationResponseTypeDef(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSnapshotCopyConfigurationResponseTypeDef(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSnapshotCopyConfigurationsResponseTypeDef(BaseValidatorModel):
    snapshotCopyConfigurations: List[SnapshotCopyConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateSnapshotCopyConfigurationResponseTypeDef(BaseValidatorModel):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUsageLimitResponseTypeDef(BaseValidatorModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteUsageLimitResponseTypeDef(BaseValidatorModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUsageLimitResponseTypeDef(BaseValidatorModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListUsageLimitsResponseTypeDef(BaseValidatorModel):
    usageLimits: List[UsageLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateUsageLimitResponseTypeDef(BaseValidatorModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkgroupRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[Sequence[ConfigParameterTypeDef]] = None
    enhancedVpcRouting: Optional[bool] = None
    ipAddressType: Optional[str] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    pricePerformanceTarget: Optional[PerformanceTargetTypeDef] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    trackName: Optional[str] = None


class UpdateWorkgroupRequestTypeDef(BaseValidatorModel):
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[Sequence[ConfigParameterTypeDef]] = None
    enhancedVpcRouting: Optional[bool] = None
    ipAddressType: Optional[str] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    pricePerformanceTarget: Optional[PerformanceTargetTypeDef] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    trackName: Optional[str] = None


class GetRecoveryPointResponseTypeDef(BaseValidatorModel):
    recoveryPoint: RecoveryPointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecoveryPointsResponseTypeDef(BaseValidatorModel):
    recoveryPoints: List[RecoveryPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableRestoreStatusResponseTypeDef(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTableRestoreStatusResponseTypeDef(BaseValidatorModel):
    tableRestoreStatuses: List[TableRestoreStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RestoreTableFromRecoveryPointResponseTypeDef(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreTableFromSnapshotResponseTypeDef(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomDomainAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEndpointAccessRequestPaginateTypeDef(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedWorkgroupsRequestPaginateTypeDef(BaseValidatorModel):
    sourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNamespacesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecoveryPointsRequestPaginateTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListScheduledActionsRequestPaginateTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSnapshotCopyConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTableRestoreStatusRequestPaginateTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTracksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsageLimitsRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkgroupsRequestPaginateTypeDef(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedWorkgroupsResponseTypeDef(BaseValidatorModel):
    managedWorkgroups: List[ManagedWorkgroupListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListScheduledActionsResponseTypeDef(BaseValidatorModel):
    scheduledActions: List[ScheduledActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class VpcEndpointTypeDef(BaseValidatorModel):
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    vpcEndpointId: Optional[str] = None
    vpcId: Optional[str] = None


class ServerlessTrackTypeDef(BaseValidatorModel):
    trackName: Optional[str] = None
    updateTargets: Optional[List[UpdateTargetTypeDef]] = None
    workgroupVersion: Optional[str] = None


class TargetActionOutputTypeDef(BaseValidatorModel):
    createSnapshot: Optional[CreateSnapshotScheduleActionParametersOutputTypeDef] = None


class TargetActionTypeDef(BaseValidatorModel):
    createSnapshot: Optional[CreateSnapshotScheduleActionParametersTypeDef] = None


class EndpointAccessTypeDef(BaseValidatorModel):
    address: Optional[str] = None
    endpointArn: Optional[str] = None
    endpointCreateTime: Optional[datetime] = None
    endpointName: Optional[str] = None
    endpointStatus: Optional[str] = None
    port: Optional[int] = None
    subnetIds: Optional[List[str]] = None
    vpcEndpoint: Optional[VpcEndpointTypeDef] = None
    vpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    workgroupName: Optional[str] = None


class EndpointTypeDef(BaseValidatorModel):
    address: Optional[str] = None
    port: Optional[int] = None
    vpcEndpoints: Optional[List[VpcEndpointTypeDef]] = None


class GetTrackResponseTypeDef(BaseValidatorModel):
    track: ServerlessTrackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTracksResponseTypeDef(BaseValidatorModel):
    tracks: List[ServerlessTrackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ScheduledActionResponseTypeDef(BaseValidatorModel):
    endTime: Optional[datetime] = None
    namespaceName: Optional[str] = None
    nextInvocations: Optional[List[datetime]] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleOutputTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    scheduledActionName: Optional[str] = None
    scheduledActionUuid: Optional[str] = None
    startTime: Optional[datetime] = None
    state: Optional[StateType] = None
    targetAction: Optional[TargetActionOutputTypeDef] = None


class CreateEndpointAccessResponseTypeDef(BaseValidatorModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEndpointAccessResponseTypeDef(BaseValidatorModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetEndpointAccessResponseTypeDef(BaseValidatorModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEndpointAccessResponseTypeDef(BaseValidatorModel):
    endpoints: List[EndpointAccessTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateEndpointAccessResponseTypeDef(BaseValidatorModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WorkgroupTypeDef(BaseValidatorModel):
    baseCapacity: Optional[int] = None
    configParameters: Optional[List[ConfigParameterTypeDef]] = None
    creationDate: Optional[datetime] = None
    crossAccountVpcs: Optional[List[str]] = None
    customDomainCertificateArn: Optional[str] = None
    customDomainCertificateExpiryTime: Optional[datetime] = None
    customDomainName: Optional[str] = None
    endpoint: Optional[EndpointTypeDef] = None
    enhancedVpcRouting: Optional[bool] = None
    ipAddressType: Optional[str] = None
    maxCapacity: Optional[int] = None
    namespaceName: Optional[str] = None
    patchVersion: Optional[str] = None
    pendingTrackName: Optional[str] = None
    port: Optional[int] = None
    pricePerformanceTarget: Optional[PerformanceTargetTypeDef] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[WorkgroupStatusType] = None
    subnetIds: Optional[List[str]] = None
    trackName: Optional[str] = None
    workgroupArn: Optional[str] = None
    workgroupId: Optional[str] = None
    workgroupName: Optional[str] = None
    workgroupVersion: Optional[str] = None


class CreateScheduledActionResponseTypeDef(BaseValidatorModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteScheduledActionResponseTypeDef(BaseValidatorModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetScheduledActionResponseTypeDef(BaseValidatorModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateScheduledActionResponseTypeDef(BaseValidatorModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TargetActionUnionTypeDef(BaseValidatorModel):
    pass


class ScheduleUnionTypeDef(BaseValidatorModel):
    pass


class CreateScheduledActionRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    roleArn: str
    schedule: ScheduleUnionTypeDef
    scheduledActionName: str
    targetAction: TargetActionUnionTypeDef
    enabled: Optional[bool] = None
    endTime: Optional[TimestampTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None


class UpdateScheduledActionRequestTypeDef(BaseValidatorModel):
    scheduledActionName: str
    enabled: Optional[bool] = None
    endTime: Optional[TimestampTypeDef] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleUnionTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    targetAction: Optional[TargetActionUnionTypeDef] = None


class CreateWorkgroupResponseTypeDef(BaseValidatorModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteWorkgroupResponseTypeDef(BaseValidatorModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkgroupResponseTypeDef(BaseValidatorModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListWorkgroupsResponseTypeDef(BaseValidatorModel):
    workgroups: List[WorkgroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateWorkgroupResponseTypeDef(BaseValidatorModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


