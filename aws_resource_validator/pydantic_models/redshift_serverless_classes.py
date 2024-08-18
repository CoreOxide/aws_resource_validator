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

class CreateCustomDomainAssociationRequestRequestTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str

class CreateEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
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

class CreateSnapshotCopyConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class CreateUsageLimitRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteCustomDomainAssociationRequestRequestTypeDef(BaseValidatorModel):
    customDomainName: str
    workgroupName: str

class DeleteEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    endpointName: str

class DeleteNamespaceRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    finalSnapshotName: Optional[str] = None
    finalSnapshotRetentionPeriod: Optional[int] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class DeleteScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    scheduledActionName: str

class DeleteSnapshotCopyConfigurationRequestRequestTypeDef(BaseValidatorModel):
    snapshotCopyConfigurationId: str

class DeleteSnapshotRequestRequestTypeDef(BaseValidatorModel):
    snapshotName: str

class DeleteUsageLimitRequestRequestTypeDef(BaseValidatorModel):
    usageLimitId: str

class DeleteWorkgroupRequestRequestTypeDef(BaseValidatorModel):
    workgroupName: str

class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    status: Optional[str] = None
    vpcSecurityGroupId: Optional[str] = None

class GetCredentialsRequestRequestTypeDef(BaseValidatorModel):
    customDomainName: Optional[str] = None
    dbName: Optional[str] = None
    durationSeconds: Optional[int] = None
    workgroupName: Optional[str] = None

class GetCustomDomainAssociationRequestRequestTypeDef(BaseValidatorModel):
    customDomainName: str
    workgroupName: str

class GetEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    endpointName: str

class GetNamespaceRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: str

class GetRecoveryPointRequestRequestTypeDef(BaseValidatorModel):
    recoveryPointId: str

class RecoveryPointTypeDef(BaseValidatorModel):
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    recoveryPointCreateTime: Optional[datetime] = None
    recoveryPointId: Optional[str] = None
    totalSizeInMegaBytes: Optional[float] = None
    workgroupName: Optional[str] = None

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResourcePolicyTypeDef(BaseValidatorModel):
    policy: Optional[str] = None
    resourceArn: Optional[str] = None

class GetScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    scheduledActionName: str

class GetSnapshotRequestRequestTypeDef(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None

class GetTableRestoreStatusRequestRequestTypeDef(BaseValidatorModel):
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

class GetUsageLimitRequestRequestTypeDef(BaseValidatorModel):
    usageLimitId: str

class GetWorkgroupRequestRequestTypeDef(BaseValidatorModel):
    workgroupName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCustomDomainAssociationsRequestRequestTypeDef(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None

class ListNamespacesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListScheduledActionsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None

class ScheduledActionAssociationTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    scheduledActionName: Optional[str] = None

class ListSnapshotCopyConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None

class ListTableRestoreStatusRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    workgroupName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListUsageLimitsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None

class ListWorkgroupsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ownerAccount: Optional[str] = None

class NetworkInterfaceTypeDef(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    subnetId: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str

class RestoreFromRecoveryPointRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    recoveryPointId: str
    workgroupName: str

class RestoreFromSnapshotRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    workgroupName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    manageAdminPassword: Optional[bool] = None
    ownerAccount: Optional[str] = None
    snapshotArn: Optional[str] = None
    snapshotName: Optional[str] = None

class RestoreTableFromRecoveryPointRequestRequestTypeDef(BaseValidatorModel):
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

class RestoreTableFromSnapshotRequestRequestTypeDef(BaseValidatorModel):
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

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateCustomDomainAssociationRequestRequestTypeDef(BaseValidatorModel):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str

class UpdateEndpointAccessRequestRequestTypeDef(BaseValidatorModel):
    endpointName: str
    vpcSecurityGroupIds: Optional[Sequence[str]] = None

class UpdateNamespaceRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    adminPasswordSecretKmsKeyId: Optional[str] = None
    adminUserPassword: Optional[str] = None
    adminUsername: Optional[str] = None
    defaultIamRoleArn: Optional[str] = None
    iamRoles: Optional[Sequence[str]] = None
    kmsKeyId: Optional[str] = None
    logExports: Optional[Sequence[LogExportType]] = None
    manageAdminPassword: Optional[bool] = None

class UpdateSnapshotCopyConfigurationRequestRequestTypeDef(BaseValidatorModel):
    snapshotCopyConfigurationId: str
    snapshotRetentionPeriod: Optional[int] = None

class UpdateSnapshotRequestRequestTypeDef(BaseValidatorModel):
    snapshotName: str
    retentionPeriod: Optional[int] = None

class UpdateUsageLimitRequestRequestTypeDef(BaseValidatorModel):
    usageLimitId: str
    amount: Optional[int] = None
    breachAction: Optional[UsageLimitBreachActionType] = None

class UpdateWorkgroupRequestRequestTypeDef(BaseValidatorModel):
    workgroupName: str
    baseCapacity: Optional[int] = None
    configParameters: Optional[Sequence[ConfigParameterTypeDef]] = None
    enhancedVpcRouting: Optional[bool] = None
    maxCapacity: Optional[int] = None
    port: Optional[int] = None
    publiclyAccessible: Optional[bool] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None

class ConvertRecoveryPointToSnapshotRequestRequestTypeDef(BaseValidatorModel):
    recoveryPointId: str
    snapshotName: str
    retentionPeriod: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateNamespaceRequestRequestTypeDef(BaseValidatorModel):
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

class CreateSnapshotRequestRequestTypeDef(BaseValidatorModel):
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

class CreateWorkgroupRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListRecoveryPointsRequestRequestTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class ListSnapshotsRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    snapshotCopyConfigurations: List[SnapshotCopyConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    usageLimits: List[UsageLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUsageLimitResponseTypeDef(BaseValidatorModel):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryPointResponseTypeDef(BaseValidatorModel):
    recoveryPoint: RecoveryPointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    recoveryPoints: List[RecoveryPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    tableRestoreStatuses: List[TableRestoreStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromRecoveryPointResponseTypeDef(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromSnapshotResponseTypeDef(BaseValidatorModel):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomDomainAssociationsRequestListCustomDomainAssociationsPaginateTypeDef(BaseValidatorModel):
    customDomainCertificateArn: Optional[str] = None
    customDomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointAccessRequestListEndpointAccessPaginateTypeDef(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    vpcId: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamespacesRequestListNamespacesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsRequestListRecoveryPointsPaginateTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduledActionsRequestListScheduledActionsPaginateTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSnapshotCopyConfigurationsRequestListSnapshotCopyConfigurationsPaginateTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSnapshotsRequestListSnapshotsPaginateTypeDef(BaseValidatorModel):
    endTime: Optional[TimestampTypeDef] = None
    namespaceArn: Optional[str] = None
    namespaceName: Optional[str] = None
    ownerAccount: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTableRestoreStatusRequestListTableRestoreStatusPaginateTypeDef(BaseValidatorModel):
    namespaceName: Optional[str] = None
    workgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsageLimitsRequestListUsageLimitsPaginateTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    usageType: Optional[UsageLimitUsageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkgroupsRequestListWorkgroupsPaginateTypeDef(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduledActionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    scheduledActions: List[ScheduledActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcEndpointTypeDef(BaseValidatorModel):
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    vpcEndpointId: Optional[str] = None
    vpcId: Optional[str] = None

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

class CreateScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    namespaceName: str
    roleArn: str
    schedule: ScheduleTypeDef
    scheduledActionName: str
    targetAction: TargetActionTypeDef
    enabled: Optional[bool] = None
    endTime: Optional[TimestampTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class UpdateScheduledActionRequestRequestTypeDef(BaseValidatorModel):
    scheduledActionName: str
    enabled: Optional[bool] = None
    endTime: Optional[TimestampTypeDef] = None
    roleArn: Optional[str] = None
    schedule: Optional[ScheduleTypeDef] = None
    scheduledActionDescription: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    targetAction: Optional[TargetActionTypeDef] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    workgroups: List[WorkgroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkgroupResponseTypeDef(BaseValidatorModel):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

