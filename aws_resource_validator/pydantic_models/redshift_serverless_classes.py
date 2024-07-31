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
from aws_resource_validator.pydantic_models.redshift_serverless_constants import *

class AssociationTypeDef(BaseModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainCertificateExpiryTime: Optional[datetime] = None
    customDomainName: Optional[str] = None
    workgroupName: Optional[str] = None

class ConfigParameterTypeDef(BaseModel):
    parameterKey: Optional[str] = None
    parameterValue: Optional[str] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SnapshotTypeDef(BaseModel):
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

class CreateCustomDomainAssociationRequestRequestTypeDef(BaseModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str

class CreateEndpointAccessRequestRequestTypeDef(BaseModel):
    endpointName: str
    subnetIds: Sequence[str]
    workgroupName: str
    ownerAccount: Optional[str] = None
    vpcSecurityGroupIds: Optional[Sequence[str]] = None

class NamespaceTypeDef(BaseModel):
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

class CreateSnapshotCopyConfigurationRequestRequestTypeDef(BaseModel):
    destinationRegion: str
    namespaceName: str
    destinationKmsKeyId: Optional[str] = None
    snapshotRetentionPeriod: Optional[int] = None

class SnapshotCopyConfigurationTypeDef(BaseModel):
    destinationKmsKeyId: Optional[str] = None
    destinationRegion: Optional[str] = None
    namespaceName: Optional[str] = None
    snapshotCopyConfigurationArn: Optional[str] = None
    snapshotCopyConfigurationId: Optional[str] = None
    snapshotRetentionPeriod: Optional[int] = None

class CreateUsageLimitRequestRequestTypeDef(BaseModel):
    amount: int
    resourceArn: str
    usageType: UsageLimitUsageTypeType
    breachAction: Optional[UsageLimitBreachActionType] = None
    period: Optional[UsageLimitPeriodType] = None

class UsageLimitTypeDef(BaseModel):
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None
    period: Optional[UsageLimitPeriodType] = None
    resourceArn: Optional[str] = None
    usageLimitArn: Optional[str] = None
    usageLimitId: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None

class DeleteCustomDomainAssociationRequestRequestTypeDef(BaseModel):
    customDomainName: str
    workgroupName: str

class DeleteEndpointAccessRequestRequestTypeDef(BaseModel):
    endpointName: str

class DeleteNamespaceRequestRequestTypeDef(BaseModel):
    namespaceName: str
    finalSnapshotName: Optional[str] = None
    finalSnapshotRetentionPeriod: Optional[int] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str

class DeleteScheduledActionRequestRequestTypeDef(BaseModel):
    scheduledActionName: str

class DeleteSnapshotCopyConfigurationRequestRequestTypeDef(BaseModel):
    snapshotCopyConfigurationId: str

class DeleteSnapshotRequestRequestTypeDef(BaseModel):
    snapshotName: str

class DeleteUsageLimitRequestRequestTypeDef(BaseModel):
    usageLimitId: str

class DeleteWorkgroupRequestRequestTypeDef(BaseModel):
    workgroupName: str

class VpcSecurityGroupMembershipTypeDef(BaseModel):
    status: Optional[str] = None
    vpcSecurityGroupId: Optional[str] = None

class GetCredentialsRequestRequestTypeDef(BaseModel):
    customDomainName: Optional[str] = None
    dbName: Optional[str] = None
    durationSeconds: Optional[int] = None
    workgroupName: Optional[str] = None

class GetCustomDomainAssociationRequestRequestTypeDef(BaseModel):
    customDomainName: str
    workgroupName: str

class GetEndpointAccessRequestRequestTypeDef(BaseModel):
    endpointName: str

class GetNamespaceRequestRequestTypeDef(BaseModel):
    namespaceName: str

class GetRecoveryPointRequestRequestTypeDef(BaseModel):
    recoveryPointId: str

class RecoveryPointTypeDef(BaseModel):
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    recoveryPointCreateTime: Optional[datetime] = None
    recoveryPointId: Optional[str] = None
    totalSizeInMegaBytes: Optional[float] = None
    workgroupName: Optional[str] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ResourcePolicyTypeDef(BaseModel):
    policy: Optional[str] = None
    resourceArn: Optional[str] = None

class GetScheduledActionRequestRequestTypeDef(BaseModel):
    scheduledActionName: str

class GetSnapshotRequestRequestTypeDef(BaseModel):
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None

class GetTableRestoreStatusRequestRequestTypeDef(BaseModel):
    tableRestoreRequestId: str

class TableRestoreStatusTypeDef(BaseModel):
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

class GetUsageLimitRequestRequestTypeDef(BaseModel):
    usageLimitId: str

class GetWorkgroupRequestRequestTypeDef(BaseModel):
    workgroupName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCustomDomainAssociationsRequestRequestTypeDef(BaseModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEndpointAccessRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None

class ListNamespacesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListScheduledActionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None

class ScheduledActionAssociationTypeDef(BaseModel):
    namespaceName: Optional[str] = None
    scheduledActionName: Optional[str] = None

class ListSnapshotCopyConfigurationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None

class ListTableRestoreStatusRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    workgroupName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListUsageLimitsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None

class ListWorkgroupsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None

class NetworkInterfaceTypeDef(BaseModel):
    availabilityZone: Optional[str] = None
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    subnetId: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    policy: str
    resourceArn: str

class RestoreFromRecoveryPointRequestRequestTypeDef(BaseModel):
    namespaceName: str
    recoveryPointId: str
    workgroupName: str

class RestoreFromSnapshotRequestRequestTypeDef(BaseModel):
    namespaceName: str
    workgroupName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    manageAdminPassword: Optional[bool] = None
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None

class RestoreTableFromRecoveryPointRequestRequestTypeDef(BaseModel):
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

class RestoreTableFromSnapshotRequestRequestTypeDef(BaseModel):
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

class ScheduleOutputTypeDef(BaseModel):
    at: Optional[datetime] = None
    cron: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateCustomDomainAssociationRequestRequestTypeDef(BaseModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str

class UpdateEndpointAccessRequestRequestTypeDef(BaseModel):
    endpointName: str
    vpcSecurityGroupIds: Optional[Sequence[str]] = None

class UpdateNamespaceRequestRequestTypeDef(BaseModel):
    namespaceName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUserPassword: Optional[str] = None
    adminUsername: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[Sequence[LogExportType]] = None
    manageAdminPassword: Optional[bool] = None

class UpdateSnapshotCopyConfigurationRequestRequestTypeDef(BaseModel):
    snapshotCopyConfigurationId: str
    snapshotRetentionPeriod: Optional[int] = None

class UpdateSnapshotRequestRequestTypeDef(BaseModel):
    snapshotName: str
    retentionPeriod: Optional[int] = None

class UpdateUsageLimitRequestRequestTypeDef(BaseModel):
    usageLimitId: str
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None

class UpdateWorkgroupRequestRequestTypeDef(BaseModel):
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[Sequence[ConfigParameterTypeDef]] = None
    enhancedVpcRouting: Optional[bool] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None

class ConvertRecoveryPointToSnapshotRequestRequestTypeDef(BaseModel):
    recoveryPointId: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateNamespaceRequestRequestTypeDef(BaseModel):
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

class CreateSnapshotRequestRequestTypeDef(BaseModel):
    namespaceName: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotScheduleActionParametersOutputTypeDef(BaseModel):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: Optional[int] = None
    tags: Optional[List[TagTypeDef]] = None

class CreateSnapshotScheduleActionParametersTypeDef(BaseModel):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateWorkgroupRequestRequestTypeDef(BaseModel):
    namespaceName: str
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[Sequence[ConfigParameterTypeDef]] = None
    enhancedVpcRouting: Optional[bool] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateCustomDomainAssociationResponseTypeDef(BaseModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialsResponseTypeDef(BaseModel):
    dbPassword: str
    dbUser: str
    expiration: datetime
    nextRefreshTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomDomainAssociationResponseTypeDef(BaseModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomDomainAssociationsResponseTypeDef(BaseModel):
    associations: List[AssociationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCustomDomainAssociationResponseTypeDef(BaseModel):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConvertRecoveryPointToSnapshotResponseTypeDef(BaseModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResponseTypeDef(BaseModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResponseTypeDef(BaseModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotResponseTypeDef(BaseModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSnapshotsResponseTypeDef(BaseModel):
    nextToken: str
    snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSnapshotResponseTypeDef(BaseModel):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNamespaceResponseTypeDef(BaseModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(BaseModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceResponseTypeDef(BaseModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNamespacesResponseTypeDef(BaseModel):
    namespaces: List[NamespaceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreFromRecoveryPointResponseTypeDef(BaseModel):
    namespace: NamespaceTypeDef
    recoveryPointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreFromSnapshotResponseTypeDef(BaseModel):
    namespace: NamespaceTypeDef
    ownerAccount: str
    snapshotName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNamespaceResponseTypeDef(BaseModel):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsRequestRequestTypeDef(BaseModel):
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class ListSnapshotsRequestRequestTypeDef(BaseModel):
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class ScheduleTypeDef(BaseModel):
    at: Optional[TimestampTypeDef] = None
    cron: Optional[str] = None

class CreateSnapshotCopyConfigurationResponseTypeDef(BaseModel):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotCopyConfigurationResponseTypeDef(BaseModel):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSnapshotCopyConfigurationsResponseTypeDef(BaseModel):
    nextToken: str
    snapshotCopyConfigurations: List[SnapshotCopyConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSnapshotCopyConfigurationResponseTypeDef(BaseModel):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageLimitResponseTypeDef(BaseModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUsageLimitResponseTypeDef(BaseModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUsageLimitResponseTypeDef(BaseModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsageLimitsResponseTypeDef(BaseModel):
    nextToken: str
    usageLimits: List[UsageLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUsageLimitResponseTypeDef(BaseModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryPointResponseTypeDef(BaseModel):
    recoveryPoint: RecoveryPointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsResponseTypeDef(BaseModel):
    nextToken: str
    recoveryPoints: List[RecoveryPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableRestoreStatusResponseTypeDef(BaseModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTableRestoreStatusResponseTypeDef(BaseModel):
    nextToken: str
    tableRestoreStatuses: List[TableRestoreStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromRecoveryPointResponseTypeDef(BaseModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromSnapshotResponseTypeDef(BaseModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomDomainAssociationsRequestListCustomDomainAssociationsPaginateTypeDef(BaseModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointAccessRequestListEndpointAccessPaginateTypeDef(BaseModel):
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestListNamespacesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsRequestListRecoveryPointsPaginateTypeDef(BaseModel):
    endTime: Optional[TimestampTypeDef] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduledActionsRequestListScheduledActionsPaginateTypeDef(BaseModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSnapshotCopyConfigurationsRequestListSnapshotCopyConfigurationsPaginateTypeDef(BaseModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSnapshotsRequestListSnapshotsPaginateTypeDef(BaseModel):
    endTime: Optional[TimestampTypeDef] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTableRestoreStatusRequestListTableRestoreStatusPaginateTypeDef(BaseModel):
    namespaceName: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsageLimitsRequestListUsageLimitsPaginateTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkgroupsRequestListWorkgroupsPaginateTypeDef(BaseModel):
    ownerAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduledActionsResponseTypeDef(BaseModel):
    nextToken: str
    scheduledActions: List[ScheduledActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcEndpointTypeDef(BaseModel):
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    vpcEndpointId: Optional[str] = None
    vpcId: Optional[str] = None

class TargetActionOutputTypeDef(BaseModel):
    createSnapshot: Optional[CreateSnapshotScheduleActionParametersOutputTypeDef] = None

class TargetActionTypeDef(BaseModel):
    createSnapshot: Optional[CreateSnapshotScheduleActionParametersTypeDef] = None

class EndpointAccessTypeDef(BaseModel):
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

class EndpointTypeDef(BaseModel):
    address: Optional[str] = None
    port: Optional[int] = None
    vpcEndpoints: Optional[List[VpcEndpointTypeDef]] = None

class ScheduledActionResponseTypeDef(BaseModel):
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

class CreateScheduledActionRequestRequestTypeDef(BaseModel):
    namespaceName: str
    roleArn: str
    schedule: ScheduleTypeDef
    scheduledActionName: str
    targetAction: TargetActionTypeDef
    enabled: Optional[bool] = None
    endTime: Optional[TimestampTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class UpdateScheduledActionRequestRequestTypeDef(BaseModel):
    scheduledActionName: str
    enabled: Optional[bool] = None
    endTime: Optional[TimestampTypeDef] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    targetAction: Optional[TargetActionTypeDef] = None

class CreateEndpointAccessResponseTypeDef(BaseModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEndpointAccessResponseTypeDef(BaseModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEndpointAccessResponseTypeDef(BaseModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointAccessResponseTypeDef(BaseModel):
    endpoints: List[EndpointAccessTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointAccessResponseTypeDef(BaseModel):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkgroupTypeDef(BaseModel):
    baseCapacity: Optional[int] = None
    configParameters: Optional[List[ConfigParameterTypeDef]] = None
    creationDate: Optional[datetime] = None
    crossAccountVpcs: Optional[List[str]] = None
    customDomainCertificateArn: Optional[str] = None
    customDomainCertificateExpiryTime: Optional[datetime] = None
    customDomainName: Optional[str] = None
    endpoint: Optional[EndpointTypeDef] = None
    enhancedVpcRouting: Optional[bool] = None
    maxCapacity: Optional[int] = None
    namespaceName: Optional[str] = None
    patchVersion: Optional[str] = None
    port: Optional[int] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[WorkgroupStatusType] = None
    subnetIds: Optional[List[str]] = None
    workgroupArn: Optional[str] = None
    workgroupId: Optional[str] = None
    workgroupName: Optional[str] = None
    workgroupVersion: Optional[str] = None

class CreateScheduledActionResponseTypeDef(BaseModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScheduledActionResponseTypeDef(BaseModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetScheduledActionResponseTypeDef(BaseModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduledActionResponseTypeDef(BaseModel):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkgroupResponseTypeDef(BaseModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkgroupResponseTypeDef(BaseModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkgroupResponseTypeDef(BaseModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkgroupsResponseTypeDef(BaseModel):
    nextToken: str
    workgroups: List[WorkgroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkgroupResponseTypeDef(BaseModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

