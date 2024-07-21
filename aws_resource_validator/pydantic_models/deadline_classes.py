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
from aws_resource_validator.pydantic_models.deadline_constants import *

class AcceleratorCountRangeTypeDef(BaseModel):
    min: int
    max: Optional[int] = None

class AcceleratorTotalMemoryMiBRangeTypeDef(BaseModel):
    min: int
    max: Optional[int] = None

class AssignedEnvironmentEnterSessionActionDefinitionTypeDef(BaseModel):
    environmentId: str

class AssignedEnvironmentExitSessionActionDefinitionTypeDef(BaseModel):
    environmentId: str

class AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef(BaseModel):
    stepId: Optional[str] = None

class LogConfigurationTypeDef(BaseModel):
    logDriver: str
    error: Optional[str] = None
    options: Optional[Dict[str, str]] = None
    parameters: Optional[Dict[str, str]] = None

class TaskParameterValueTypeDef(BaseModel):
    float: Optional[str] = None
    int: Optional[str] = None
    path: Optional[str] = None
    string: Optional[str] = None

class AssociateMemberToFarmRequestRequestTypeDef(BaseModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class AssociateMemberToFleetRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class AssociateMemberToJobRequestRequestTypeDef(BaseModel):
    farmId: str
    identityStoreId: str
    jobId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class AssociateMemberToQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class AssumeFleetRoleForReadRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str

class AwsCredentialsTypeDef(BaseModel):
    accessKeyId: str
    expiration: datetime
    secretAccessKey: str
    sessionToken: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssumeFleetRoleForWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str

class AssumeQueueRoleForReadRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str

class AssumeQueueRoleForUserRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str

class AssumeQueueRoleForWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    queueId: str
    workerId: str

class ManifestPropertiesTypeDef(BaseModel):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: Optional[str] = None
    inputManifestHash: Optional[str] = None
    inputManifestPath: Optional[str] = None
    outputRelativeDirectories: Optional[List[str]] = None

class BudgetActionToAddTypeDef(BaseModel):
    thresholdPercentage: float
    type: BudgetActionTypeType
    description: Optional[str] = None

class BudgetActionToRemoveTypeDef(BaseModel):
    thresholdPercentage: float
    type: BudgetActionTypeType

class ConsumedUsagesTypeDef(BaseModel):
    approximateDollarUsage: float

class UsageTrackingResourceTypeDef(BaseModel):
    queueId: Optional[str] = None

class S3LocationTypeDef(BaseModel):
    bucketName: str
    key: str

class CreateFarmRequestRequestTypeDef(BaseModel):
    displayName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class JobParameterTypeDef(BaseModel):
    float: Optional[str] = None
    int: Optional[str] = None
    path: Optional[str] = None
    string: Optional[str] = None

class CreateLicenseEndpointRequestRequestTypeDef(BaseModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateMonitorRequestRequestTypeDef(BaseModel):
    displayName: str
    identityCenterInstanceArn: str
    roleArn: str
    subdomain: str
    clientToken: Optional[str] = None

class CreateQueueEnvironmentRequestRequestTypeDef(BaseModel):
    farmId: str
    priority: int
    queueId: str
    template: str
    templateType: EnvironmentTemplateTypeType
    clientToken: Optional[str] = None

class CreateQueueFleetAssociationRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    queueId: str

class JobAttachmentSettingsTypeDef(BaseModel):
    rootPrefix: str
    s3BucketName: str

class FileSystemLocationTypeDef(BaseModel):
    name: str
    path: str
    type: FileSystemLocationTypeType

class FleetAmountCapabilityTypeDef(BaseModel):
    min: float
    name: str
    max: Optional[float] = None

class FleetAttributeCapabilityPaginatorTypeDef(BaseModel):
    name: str
    values: List[str]

class MemoryMiBRangeTypeDef(BaseModel):
    min: int
    max: Optional[int] = None

class VCpuCountRangeTypeDef(BaseModel):
    min: int
    max: Optional[int] = None

class FleetAttributeCapabilityTypeDef(BaseModel):
    name: str
    values: Sequence[str]

class DeleteBudgetRequestRequestTypeDef(BaseModel):
    budgetId: str
    farmId: str

class DeleteFarmRequestRequestTypeDef(BaseModel):
    farmId: str

class DeleteFleetRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None

class DeleteLicenseEndpointRequestRequestTypeDef(BaseModel):
    licenseEndpointId: str

class DeleteMeteredProductRequestRequestTypeDef(BaseModel):
    licenseEndpointId: str
    productId: str

class DeleteMonitorRequestRequestTypeDef(BaseModel):
    monitorId: str

class DeleteQueueEnvironmentRequestRequestTypeDef(BaseModel):
    farmId: str
    queueEnvironmentId: str
    queueId: str

class DeleteQueueFleetAssociationRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    queueId: str

class DeleteQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str

class DeleteStorageProfileRequestRequestTypeDef(BaseModel):
    farmId: str
    storageProfileId: str

class DeleteWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str

class DependencyCountsTypeDef(BaseModel):
    consumersResolved: int
    consumersUnresolved: int
    dependenciesResolved: int
    dependenciesUnresolved: int

class DisassociateMemberFromFarmRequestRequestTypeDef(BaseModel):
    farmId: str
    principalId: str

class DisassociateMemberFromFleetRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    principalId: str

class DisassociateMemberFromJobRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    principalId: str
    queueId: str

class DisassociateMemberFromQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    principalId: str
    queueId: str

class Ec2EbsVolumeTypeDef(BaseModel):
    iops: Optional[int] = None
    sizeGiB: Optional[int] = None
    throughputMiB: Optional[int] = None

class EnvironmentDetailsEntityTypeDef(BaseModel):
    environmentId: str
    jobId: str
    schemaVersion: str
    template: Dict[str, Any]

class EnvironmentDetailsErrorTypeDef(BaseModel):
    code: JobEntityErrorCodeType
    environmentId: str
    jobId: str
    message: str

class EnvironmentDetailsIdentifiersTypeDef(BaseModel):
    environmentId: str
    jobId: str

class EnvironmentEnterSessionActionDefinitionSummaryTypeDef(BaseModel):
    environmentId: str

class EnvironmentEnterSessionActionDefinitionTypeDef(BaseModel):
    environmentId: str

class EnvironmentExitSessionActionDefinitionSummaryTypeDef(BaseModel):
    environmentId: str

class EnvironmentExitSessionActionDefinitionTypeDef(BaseModel):
    environmentId: str

class FarmMemberTypeDef(BaseModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class FarmSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    displayName: str
    farmId: str
    kmsKeyArn: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class FieldSortExpressionTypeDef(BaseModel):
    name: str
    sortOrder: SortOrderType

class FleetMemberTypeDef(BaseModel):
    farmId: str
    fleetId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class GetBudgetRequestRequestTypeDef(BaseModel):
    budgetId: str
    farmId: str

class ResponseBudgetActionTypeDef(BaseModel):
    thresholdPercentage: float
    type: BudgetActionTypeType
    description: Optional[str] = None

class GetFarmRequestRequestTypeDef(BaseModel):
    farmId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetFleetRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str

class JobAttachmentDetailsErrorTypeDef(BaseModel):
    code: JobEntityErrorCodeType
    jobId: str
    message: str

class JobDetailsErrorTypeDef(BaseModel):
    code: JobEntityErrorCodeType
    jobId: str
    message: str

class StepDetailsErrorTypeDef(BaseModel):
    code: JobEntityErrorCodeType
    jobId: str
    message: str
    stepId: str

class GetJobRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str

class GetLicenseEndpointRequestRequestTypeDef(BaseModel):
    licenseEndpointId: str

class GetMonitorRequestRequestTypeDef(BaseModel):
    monitorId: str

class GetQueueEnvironmentRequestRequestTypeDef(BaseModel):
    farmId: str
    queueEnvironmentId: str
    queueId: str

class GetQueueFleetAssociationRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    queueId: str

class GetQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str

class GetSessionActionRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    sessionActionId: str

class GetSessionRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    sessionId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetSessionsStatisticsAggregationRequestRequestTypeDef(BaseModel):
    aggregationId: str
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetStepRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str

class GetStorageProfileForQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str
    storageProfileId: str

class GetStorageProfileRequestRequestTypeDef(BaseModel):
    farmId: str
    storageProfileId: str

class GetTaskRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    taskId: str

class GetWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str

class IpAddressesTypeDef(BaseModel):
    ipV4Addresses: Optional[Sequence[str]] = None
    ipV6Addresses: Optional[Sequence[str]] = None

class IpAddressesPaginatorTypeDef(BaseModel):
    ipV4Addresses: Optional[List[str]] = None
    ipV6Addresses: Optional[List[str]] = None

class JobAttachmentDetailsIdentifiersTypeDef(BaseModel):
    jobId: str

class PathMappingRuleTypeDef(BaseModel):
    destinationPath: str
    sourcePath: str
    sourcePathFormat: PathFormatType

class JobDetailsIdentifiersTypeDef(BaseModel):
    jobId: str

class StepDetailsIdentifiersTypeDef(BaseModel):
    jobId: str
    stepId: str

class StepDetailsEntityTypeDef(BaseModel):
    dependencies: List[str]
    jobId: str
    schemaVersion: str
    stepId: str
    template: Dict[str, Any]

class JobMemberTypeDef(BaseModel):
    farmId: str
    identityStoreId: str
    jobId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class PosixUserTypeDef(BaseModel):
    group: str
    user: str

class WindowsUserTypeDef(BaseModel):
    passwordArn: str
    user: str

class JobSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    jobId: str
    lifecycleStatus: JobLifecycleStatusType
    lifecycleStatusMessage: str
    name: str
    priority: int
    endedAt: Optional[datetime] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    startedAt: Optional[datetime] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None
    taskRunStatus: Optional[TaskRunStatusType] = None
    taskRunStatusCounts: Optional[Dict[TaskRunStatusType, int]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class LicenseEndpointSummaryTypeDef(BaseModel):
    licenseEndpointId: Optional[str] = None
    status: Optional[LicenseEndpointStatusType] = None
    statusMessage: Optional[str] = None
    vpcId: Optional[str] = None

class ListAvailableMeteredProductsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MeteredProductSummaryTypeDef(BaseModel):
    family: str
    port: int
    productId: str
    vendor: str

class ListBudgetsRequestRequestTypeDef(BaseModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[BudgetStatusType] = None

class ListFarmMembersRequestRequestTypeDef(BaseModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFarmsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None

class ListFleetMembersRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFleetsRequestRequestTypeDef(BaseModel):
    farmId: str
    displayName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    status: Optional[FleetStatusType] = None

class ListJobMembersRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None

class ListLicenseEndpointsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMeteredProductsRequestRequestTypeDef(BaseModel):
    licenseEndpointId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMonitorsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MonitorSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    displayName: str
    identityCenterApplicationArn: str
    identityCenterInstanceArn: str
    monitorId: str
    roleArn: str
    subdomain: str
    url: str
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ListQueueEnvironmentsRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueueEnvironmentSummaryTypeDef(BaseModel):
    name: str
    priority: int
    queueEnvironmentId: str

class ListQueueFleetAssociationsRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    queueId: Optional[str] = None

class QueueFleetAssociationSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    fleetId: str
    queueId: str
    status: QueueFleetAssociationStatusType
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ListQueueMembersRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueueMemberTypeDef(BaseModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class ListQueuesRequestRequestTypeDef(BaseModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None

class QueueSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    defaultBudgetAction: DefaultQueueBudgetActionType
    displayName: str
    farmId: str
    queueId: str
    status: QueueStatusType
    blockedReason: Optional[QueueBlockedReasonType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ListSessionActionsRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sessionId: Optional[str] = None
    taskId: Optional[str] = None

class ListSessionsForWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkerSessionSummaryTypeDef(BaseModel):
    jobId: str
    lifecycleStatus: SessionLifecycleStatusType
    queueId: str
    sessionId: str
    startedAt: datetime
    endedAt: Optional[datetime] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None

class ListSessionsRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SessionSummaryTypeDef(BaseModel):
    fleetId: str
    lifecycleStatus: SessionLifecycleStatusType
    sessionId: str
    startedAt: datetime
    workerId: str
    endedAt: Optional[datetime] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ListStepConsumersRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StepConsumerTypeDef(BaseModel):
    status: DependencyConsumerResolutionStatusType
    stepId: str

class ListStepDependenciesRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StepDependencyTypeDef(BaseModel):
    status: DependencyConsumerResolutionStatusType
    stepId: str

class ListStepsRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStorageProfilesForQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StorageProfileSummaryTypeDef(BaseModel):
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    storageProfileId: str

class ListStorageProfilesRequestRequestTypeDef(BaseModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTasksRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkersRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ParameterFilterExpressionTypeDef(BaseModel):
    name: str
    operator: ComparisonOperatorType
    value: str

class ParameterSortExpressionTypeDef(BaseModel):
    name: str
    sortOrder: SortOrderType

class StepParameterTypeDef(BaseModel):
    name: str
    type: StepParameterTypeType

class PutMeteredProductRequestRequestTypeDef(BaseModel):
    licenseEndpointId: str
    productId: str

class SearchTermFilterExpressionTypeDef(BaseModel):
    searchTerm: str

class StringFilterExpressionTypeDef(BaseModel):
    name: str
    operator: ComparisonOperatorType
    value: str

class SearchGroupedFilterExpressionsTypeDef(BaseModel):
    filters: Sequence["SearchFilterExpressionTypeDef"]
    operator: LogicalOperatorType

class UserJobsFirstTypeDef(BaseModel):
    userIdentityId: str

class ServiceManagedEc2InstanceMarketOptionsTypeDef(BaseModel):
    type: Ec2MarketTypeType

class SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef(BaseModel):
    stepId: Optional[str] = None

class TaskRunSessionActionDefinitionSummaryTypeDef(BaseModel):
    stepId: str
    taskId: str

class SyncInputJobAttachmentsSessionActionDefinitionTypeDef(BaseModel):
    stepId: Optional[str] = None

class SessionsStatisticsResourcesTypeDef(BaseModel):
    fleetIds: Optional[Sequence[str]] = None
    queueIds: Optional[Sequence[str]] = None

class StatsTypeDef(BaseModel):
    avg: Optional[float] = None
    max: Optional[float] = None
    min: Optional[float] = None
    sum: Optional[float] = None

class StepAmountCapabilityTypeDef(BaseModel):
    name: str
    max: Optional[float] = None
    min: Optional[float] = None
    value: Optional[float] = None

class StepAttributeCapabilityTypeDef(BaseModel):
    name: str
    allOf: Optional[List[str]] = None
    anyOf: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateFarmRequestRequestTypeDef(BaseModel):
    farmId: str
    description: Optional[str] = None
    displayName: Optional[str] = None

class UpdateJobRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    clientToken: Optional[str] = None
    lifecycleStatus: Optional[Literal["ARCHIVED"]] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    priority: Optional[int] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None

class UpdateMonitorRequestRequestTypeDef(BaseModel):
    monitorId: str
    displayName: Optional[str] = None
    roleArn: Optional[str] = None
    subdomain: Optional[str] = None

class UpdateQueueEnvironmentRequestRequestTypeDef(BaseModel):
    farmId: str
    queueEnvironmentId: str
    queueId: str
    clientToken: Optional[str] = None
    priority: Optional[int] = None
    template: Optional[str] = None
    templateType: Optional[EnvironmentTemplateTypeType] = None

class UpdateQueueFleetAssociationRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    queueId: str
    status: UpdateQueueFleetAssociationStatusType

class UpdateSessionRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    sessionId: str
    targetLifecycleStatus: Literal["ENDED"]
    clientToken: Optional[str] = None

class UpdateStepRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    targetTaskRunStatus: StepTargetTaskRunStatusType
    clientToken: Optional[str] = None

class UpdateTaskRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    targetRunStatus: TaskTargetRunStatusType
    taskId: str
    clientToken: Optional[str] = None

class WorkerAmountCapabilityTypeDef(BaseModel):
    name: str
    value: float

class WorkerAttributeCapabilityTypeDef(BaseModel):
    name: str
    values: Sequence[str]

class AssignedTaskRunSessionActionDefinitionTypeDef(BaseModel):
    parameters: Dict[str, TaskParameterValueTypeDef]
    stepId: str
    taskId: str

class TaskRunSessionActionDefinitionTypeDef(BaseModel):
    parameters: Dict[str, TaskParameterValueTypeDef]
    stepId: str
    taskId: str

class TaskSearchSummaryTypeDef(BaseModel):
    endedAt: Optional[datetime] = None
    failureRetryCount: Optional[int] = None
    jobId: Optional[str] = None
    parameters: Optional[Dict[str, TaskParameterValueTypeDef]] = None
    queueId: Optional[str] = None
    runStatus: Optional[TaskRunStatusType] = None
    startedAt: Optional[datetime] = None
    stepId: Optional[str] = None
    targetRunStatus: Optional[TaskTargetRunStatusType] = None
    taskId: Optional[str] = None

class TaskSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    taskId: str
    endedAt: Optional[datetime] = None
    failureRetryCount: Optional[int] = None
    latestSessionActionId: Optional[str] = None
    parameters: Optional[Dict[str, TaskParameterValueTypeDef]] = None
    startedAt: Optional[datetime] = None
    targetRunStatus: Optional[TaskTargetRunStatusType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class AssumeFleetRoleForReadResponseTypeDef(BaseModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeFleetRoleForWorkerResponseTypeDef(BaseModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForReadResponseTypeDef(BaseModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForUserResponseTypeDef(BaseModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForWorkerResponseTypeDef(BaseModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyJobTemplateResponseTypeDef(BaseModel):
    templateType: JobTemplateTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetResponseTypeDef(BaseModel):
    budgetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFarmResponseTypeDef(BaseModel):
    farmId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseModel):
    fleetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResponseTypeDef(BaseModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseEndpointResponseTypeDef(BaseModel):
    licenseEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitorResponseTypeDef(BaseModel):
    identityCenterApplicationArn: str
    monitorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueEnvironmentResponseTypeDef(BaseModel):
    queueEnvironmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResponseTypeDef(BaseModel):
    queueId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageProfileResponseTypeDef(BaseModel):
    storageProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkerResponseTypeDef(BaseModel):
    workerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFarmResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    description: str
    displayName: str
    farmId: str
    kmsKeyArn: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseEndpointResponseTypeDef(BaseModel):
    dnsName: str
    licenseEndpointId: str
    securityGroupIds: List[str]
    status: LicenseEndpointStatusType
    statusMessage: str
    subnetIds: List[str]
    vpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMonitorResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    displayName: str
    identityCenterApplicationArn: str
    identityCenterInstanceArn: str
    monitorId: str
    roleArn: str
    subdomain: str
    updatedAt: datetime
    updatedBy: str
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueEnvironmentResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    name: str
    priority: int
    queueEnvironmentId: str
    template: str
    templateType: EnvironmentTemplateTypeType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueFleetAssociationResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    fleetId: str
    queueId: str
    status: QueueFleetAssociationStatusType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaskResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    endedAt: datetime
    failureRetryCount: int
    latestSessionActionId: str
    parameters: Dict[str, TaskParameterValueTypeDef]
    runStatus: TaskRunStatusType
    startedAt: datetime
    targetRunStatus: TaskTargetRunStatusType
    taskId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionsStatisticsAggregationResponseTypeDef(BaseModel):
    aggregationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkerResponseTypeDef(BaseModel):
    log: LogConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentsTypeDef(BaseModel):
    manifests: List[ManifestPropertiesTypeDef]
    fileSystem: Optional[JobAttachmentsFileSystemType] = None

class BudgetSummaryTypeDef(BaseModel):
    approximateDollarLimit: float
    budgetId: str
    createdAt: datetime
    createdBy: str
    displayName: str
    status: BudgetStatusType
    usageTrackingResource: UsageTrackingResourceTypeDef
    usages: ConsumedUsagesTypeDef
    description: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class CopyJobTemplateRequestRequestTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    targetS3Location: S3LocationTypeDef

class JobSearchSummaryTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    endedAt: Optional[datetime] = None
    jobId: Optional[str] = None
    jobParameters: Optional[Dict[str, JobParameterTypeDef]] = None
    lifecycleStatus: Optional[JobLifecycleStatusType] = None
    lifecycleStatusMessage: Optional[str] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    queueId: Optional[str] = None
    startedAt: Optional[datetime] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None
    taskRunStatus: Optional[TaskRunStatusType] = None
    taskRunStatusCounts: Optional[Dict[TaskRunStatusType, int]] = None

class CreateStorageProfileRequestRequestTypeDef(BaseModel):
    displayName: str
    farmId: str
    osFamily: StorageProfileOperatingSystemFamilyType
    clientToken: Optional[str] = None
    fileSystemLocations: Optional[Sequence[FileSystemLocationTypeDef]] = None

class GetStorageProfileForQueueResponseTypeDef(BaseModel):
    displayName: str
    fileSystemLocations: List[FileSystemLocationTypeDef]
    osFamily: StorageProfileOperatingSystemFamilyType
    storageProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStorageProfileResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    displayName: str
    fileSystemLocations: List[FileSystemLocationTypeDef]
    osFamily: StorageProfileOperatingSystemFamilyType
    storageProfileId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStorageProfileRequestRequestTypeDef(BaseModel):
    farmId: str
    storageProfileId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    fileSystemLocationsToAdd: Optional[Sequence[FileSystemLocationTypeDef]] = None
    fileSystemLocationsToRemove: Optional[Sequence[FileSystemLocationTypeDef]] = None
    osFamily: Optional[StorageProfileOperatingSystemFamilyType] = None

class CustomerManagedWorkerCapabilitiesPaginatorTypeDef(BaseModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    acceleratorCount: Optional[AcceleratorCountRangeTypeDef] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRangeTypeDef] = None
    acceleratorTypes: Optional[List[Literal["gpu"]]] = None
    customAmounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityPaginatorTypeDef]] = None

class CustomerManagedWorkerCapabilitiesTypeDef(BaseModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    acceleratorCount: Optional[AcceleratorCountRangeTypeDef] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRangeTypeDef] = None
    acceleratorTypes: Optional[Sequence[Literal["gpu"]]] = None
    customAmounts: Optional[Sequence[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapabilityTypeDef]] = None

class FleetCapabilitiesTypeDef(BaseModel):
    amounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    attributes: Optional[List[FleetAttributeCapabilityTypeDef]] = None

class DateTimeFilterExpressionTypeDef(BaseModel):
    dateTime: TimestampTypeDef
    name: str
    operator: ComparisonOperatorType

class FixedBudgetScheduleTypeDef(BaseModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef

class UpdatedSessionActionInfoTypeDef(BaseModel):
    completedStatus: Optional[CompletedStatusType] = None
    endedAt: Optional[TimestampTypeDef] = None
    processExitCode: Optional[int] = None
    progressMessage: Optional[str] = None
    progressPercent: Optional[float] = None
    startedAt: Optional[TimestampTypeDef] = None
    updatedAt: Optional[TimestampTypeDef] = None

class StepSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    lifecycleStatus: StepLifecycleStatusType
    name: str
    stepId: str
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    dependencyCounts: Optional[DependencyCountsTypeDef] = None
    endedAt: Optional[datetime] = None
    lifecycleStatusMessage: Optional[str] = None
    startedAt: Optional[datetime] = None
    targetTaskRunStatus: Optional[StepTargetTaskRunStatusType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ServiceManagedEc2InstanceCapabilitiesPaginatorTypeDef(BaseModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    allowedInstanceTypes: Optional[List[str]] = None
    customAmounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityPaginatorTypeDef]] = None
    excludedInstanceTypes: Optional[List[str]] = None
    rootEbsVolume: Optional[Ec2EbsVolumeTypeDef] = None

class ServiceManagedEc2InstanceCapabilitiesTypeDef(BaseModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    allowedInstanceTypes: Optional[Sequence[str]] = None
    customAmounts: Optional[Sequence[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapabilityTypeDef]] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    rootEbsVolume: Optional[Ec2EbsVolumeTypeDef] = None

class ListFarmMembersResponseTypeDef(BaseModel):
    members: List[FarmMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFarmsResponseTypeDef(BaseModel):
    farms: List[FarmSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetMembersResponseTypeDef(BaseModel):
    members: List[FleetMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFleetRequestFleetActiveWaitTypeDef(BaseModel):
    farmId: str
    fleetId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetJobRequestJobCreateCompleteWaitTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLicenseEndpointRequestLicenseEndpointDeletedWaitTypeDef(BaseModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLicenseEndpointRequestLicenseEndpointValidWaitTypeDef(BaseModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetQueueFleetAssociationRequestQueueFleetAssociationStoppedWaitTypeDef(BaseModel):
    farmId: str
    fleetId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetQueueRequestQueueSchedulingBlockedWaitTypeDef(BaseModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetQueueRequestQueueSchedulingWaitTypeDef(BaseModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetJobEntityErrorTypeDef(BaseModel):
    environmentDetails: Optional[EnvironmentDetailsErrorTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsErrorTypeDef] = None
    jobDetails: Optional[JobDetailsErrorTypeDef] = None
    stepDetails: Optional[StepDetailsErrorTypeDef] = None

class GetSessionsStatisticsAggregationRequestGetSessionsStatisticsAggregationPaginateTypeDef(BaseModel):
    aggregationId: str
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAvailableMeteredProductsRequestListAvailableMeteredProductsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBudgetsRequestListBudgetsPaginateTypeDef(BaseModel):
    farmId: str
    status: Optional[BudgetStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFarmMembersRequestListFarmMembersPaginateTypeDef(BaseModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFarmsRequestListFarmsPaginateTypeDef(BaseModel):
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetMembersRequestListFleetMembersPaginateTypeDef(BaseModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsRequestListFleetsPaginateTypeDef(BaseModel):
    farmId: str
    displayName: Optional[str] = None
    principalId: Optional[str] = None
    status: Optional[FleetStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobMembersRequestListJobMembersPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    farmId: str
    queueId: str
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLicenseEndpointsRequestListLicenseEndpointsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMeteredProductsRequestListMeteredProductsPaginateTypeDef(BaseModel):
    licenseEndpointId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsRequestListMonitorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueEnvironmentsRequestListQueueEnvironmentsPaginateTypeDef(BaseModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueFleetAssociationsRequestListQueueFleetAssociationsPaginateTypeDef(BaseModel):
    farmId: str
    fleetId: Optional[str] = None
    queueId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueMembersRequestListQueueMembersPaginateTypeDef(BaseModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseModel):
    farmId: str
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSessionActionsRequestListSessionActionsPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    sessionId: Optional[str] = None
    taskId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSessionsForWorkerRequestListSessionsForWorkerPaginateTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSessionsRequestListSessionsPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepConsumersRequestListStepConsumersPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepDependenciesRequestListStepDependenciesPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepsRequestListStepsPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStorageProfilesForQueueRequestListStorageProfilesForQueuePaginateTypeDef(BaseModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStorageProfilesRequestListStorageProfilesPaginateTypeDef(BaseModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksRequestListTasksPaginateTypeDef(BaseModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkersRequestListWorkersPaginateTypeDef(BaseModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class HostPropertiesRequestTypeDef(BaseModel):
    hostName: Optional[str] = None
    ipAddresses: Optional[IpAddressesTypeDef] = None

class HostPropertiesResponseTypeDef(BaseModel):
    ec2InstanceArn: Optional[str] = None
    ec2InstanceType: Optional[str] = None
    hostName: Optional[str] = None
    ipAddresses: Optional[IpAddressesTypeDef] = None

class HostPropertiesResponsePaginatorTypeDef(BaseModel):
    ec2InstanceArn: Optional[str] = None
    ec2InstanceType: Optional[str] = None
    hostName: Optional[str] = None
    ipAddresses: Optional[IpAddressesPaginatorTypeDef] = None

class JobEntityIdentifiersUnionTypeDef(BaseModel):
    environmentDetails: Optional[EnvironmentDetailsIdentifiersTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsIdentifiersTypeDef] = None
    jobDetails: Optional[JobDetailsIdentifiersTypeDef] = None
    stepDetails: Optional[StepDetailsIdentifiersTypeDef] = None

class ListJobMembersResponseTypeDef(BaseModel):
    members: List[JobMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobRunAsUserTypeDef(BaseModel):
    runAs: RunAsType
    posix: Optional[PosixUserTypeDef] = None
    windows: Optional[WindowsUserTypeDef] = None

class ListJobsResponseTypeDef(BaseModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseEndpointsResponseTypeDef(BaseModel):
    licenseEndpoints: List[LicenseEndpointSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableMeteredProductsResponseTypeDef(BaseModel):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMeteredProductsResponseTypeDef(BaseModel):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMonitorsResponseTypeDef(BaseModel):
    monitors: List[MonitorSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueueEnvironmentsResponseTypeDef(BaseModel):
    environments: List[QueueEnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueueFleetAssociationsResponseTypeDef(BaseModel):
    nextToken: str
    queueFleetAssociations: List[QueueFleetAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueueMembersResponseTypeDef(BaseModel):
    members: List[QueueMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueuesResponseTypeDef(BaseModel):
    nextToken: str
    queues: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsForWorkerResponseTypeDef(BaseModel):
    nextToken: str
    sessions: List[WorkerSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsResponseTypeDef(BaseModel):
    nextToken: str
    sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStepConsumersResponseTypeDef(BaseModel):
    consumers: List[StepConsumerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStepDependenciesResponseTypeDef(BaseModel):
    dependencies: List[StepDependencyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageProfilesForQueueResponseTypeDef(BaseModel):
    nextToken: str
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageProfilesResponseTypeDef(BaseModel):
    nextToken: str
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ParameterSpaceTypeDef(BaseModel):
    parameters: List[StepParameterTypeDef]
    combination: Optional[str] = None

class SearchSortExpressionTypeDef(BaseModel):
    fieldSort: Optional[FieldSortExpressionTypeDef] = None
    parameterSort: Optional[ParameterSortExpressionTypeDef] = None
    userJobsFirst: Optional[UserJobsFirstTypeDef] = None

class SessionActionDefinitionSummaryTypeDef(BaseModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionSummaryTypeDef] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionSummaryTypeDef] = None
    syncInputJobAttachments: Optional[       SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef     ] = None
    taskRun: Optional[TaskRunSessionActionDefinitionSummaryTypeDef] = None

class StartSessionsStatisticsAggregationRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    farmId: str
    groupBy: Sequence[UsageGroupByFieldType]
    resourceIds: SessionsStatisticsResourcesTypeDef
    startTime: TimestampTypeDef
    statistics: Sequence[UsageStatisticType]
    period: Optional[PeriodType] = None
    timezone: Optional[str] = None

class StatisticsTypeDef(BaseModel):
    costInUsd: StatsTypeDef
    count: int
    runtimeInSeconds: StatsTypeDef
    aggregationEndTime: Optional[datetime] = None
    aggregationStartTime: Optional[datetime] = None
    fleetId: Optional[str] = None
    instanceType: Optional[str] = None
    jobId: Optional[str] = None
    jobName: Optional[str] = None
    licenseProduct: Optional[str] = None
    queueId: Optional[str] = None
    usageType: Optional[UsageTypeType] = None
    userId: Optional[str] = None

class StepRequiredCapabilitiesTypeDef(BaseModel):
    amounts: List[StepAmountCapabilityTypeDef]
    attributes: List[StepAttributeCapabilityTypeDef]

class WorkerCapabilitiesTypeDef(BaseModel):
    amounts: Sequence[WorkerAmountCapabilityTypeDef]
    attributes: Sequence[WorkerAttributeCapabilityTypeDef]

class AssignedSessionActionDefinitionTypeDef(BaseModel):
    envEnter: Optional[AssignedEnvironmentEnterSessionActionDefinitionTypeDef] = None
    envExit: Optional[AssignedEnvironmentExitSessionActionDefinitionTypeDef] = None
    syncInputJobAttachments: Optional[       AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef     ] = None
    taskRun: Optional[AssignedTaskRunSessionActionDefinitionTypeDef] = None

class SessionActionDefinitionTypeDef(BaseModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionTypeDef] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionTypeDef] = None
    syncInputJobAttachments: Optional[       SyncInputJobAttachmentsSessionActionDefinitionTypeDef     ] = None
    taskRun: Optional[TaskRunSessionActionDefinitionTypeDef] = None

class SearchTasksResponseTypeDef(BaseModel):
    nextItemOffset: int
    tasks: List[TaskSearchSummaryTypeDef]
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTasksResponseTypeDef(BaseModel):
    nextToken: str
    tasks: List[TaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestRequestTypeDef(BaseModel):
    farmId: str
    priority: int
    queueId: str
    template: str
    templateType: JobTemplateTypeType
    attachments: Optional[AttachmentsTypeDef] = None
    clientToken: Optional[str] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    parameters: Optional[Mapping[str, JobParameterTypeDef]] = None
    storageProfileId: Optional[str] = None
    targetTaskRunStatus: Optional[CreateJobTargetTaskRunStatusType] = None

class GetJobResponseTypeDef(BaseModel):
    attachments: AttachmentsTypeDef
    createdAt: datetime
    createdBy: str
    description: str
    endedAt: datetime
    jobId: str
    lifecycleStatus: JobLifecycleStatusType
    lifecycleStatusMessage: str
    maxFailedTasksCount: int
    maxRetriesPerTask: int
    name: str
    parameters: Dict[str, JobParameterTypeDef]
    priority: int
    startedAt: datetime
    storageProfileId: str
    targetTaskRunStatus: JobTargetTaskRunStatusType
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobAttachmentDetailsEntityTypeDef(BaseModel):
    attachments: AttachmentsTypeDef
    jobId: str

class ListBudgetsResponseTypeDef(BaseModel):
    budgets: List[BudgetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchJobsResponseTypeDef(BaseModel):
    jobs: List[JobSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerManagedFleetConfigurationPaginatorTypeDef(BaseModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesPaginatorTypeDef
    storageProfileId: Optional[str] = None

class CustomerManagedFleetConfigurationTypeDef(BaseModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesTypeDef
    storageProfileId: Optional[str] = None

class SearchFilterExpressionTypeDef(BaseModel):
    dateTimeFilter: Optional[DateTimeFilterExpressionTypeDef] = None
    groupFilter: Optional[Dict[str, Any]] = None
    parameterFilter: Optional[ParameterFilterExpressionTypeDef] = None
    searchTermFilter: Optional[SearchTermFilterExpressionTypeDef] = None
    stringFilter: Optional[StringFilterExpressionTypeDef] = None

class BudgetScheduleTypeDef(BaseModel):
    fixed: Optional[FixedBudgetScheduleTypeDef] = None

class UpdateWorkerScheduleRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str
    updatedSessionActions: Optional[Mapping[str, UpdatedSessionActionInfoTypeDef]] = None

class ListStepsResponseTypeDef(BaseModel):
    nextToken: str
    steps: List[StepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceManagedEc2FleetConfigurationPaginatorTypeDef(BaseModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesPaginatorTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef

class ServiceManagedEc2FleetConfigurationTypeDef(BaseModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef

class CreateWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None
    hostProperties: Optional[HostPropertiesRequestTypeDef] = None

class GetSessionResponseTypeDef(BaseModel):
    endedAt: datetime
    fleetId: str
    hostProperties: HostPropertiesResponseTypeDef
    lifecycleStatus: SessionLifecycleStatusType
    log: LogConfigurationTypeDef
    sessionId: str
    startedAt: datetime
    targetLifecycleStatus: Literal["ENDED"]
    updatedAt: datetime
    updatedBy: str
    workerId: str
    workerLog: LogConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkerResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    farmId: str
    fleetId: str
    hostProperties: HostPropertiesResponseTypeDef
    log: LogConfigurationTypeDef
    status: WorkerStatusType
    updatedAt: datetime
    updatedBy: str
    workerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkerSearchSummaryTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    fleetId: Optional[str] = None
    hostProperties: Optional[HostPropertiesResponseTypeDef] = None
    status: Optional[WorkerStatusType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    workerId: Optional[str] = None

class WorkerSummaryTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    farmId: str
    fleetId: str
    status: WorkerStatusType
    workerId: str
    hostProperties: Optional[HostPropertiesResponseTypeDef] = None
    log: Optional[LogConfigurationTypeDef] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class WorkerSummaryPaginatorTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    farmId: str
    fleetId: str
    status: WorkerStatusType
    workerId: str
    hostProperties: Optional[HostPropertiesResponsePaginatorTypeDef] = None
    log: Optional[LogConfigurationTypeDef] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class BatchGetJobEntityRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    identifiers: Sequence[JobEntityIdentifiersUnionTypeDef]
    workerId: str

class CreateQueueRequestRequestTypeDef(BaseModel):
    displayName: str
    farmId: str
    allowedStorageProfileIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    defaultBudgetAction: Optional[DefaultQueueBudgetActionType] = None
    description: Optional[str] = None
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    requiredFileSystemLocationNames: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetQueueResponseTypeDef(BaseModel):
    allowedStorageProfileIds: List[str]
    blockedReason: QueueBlockedReasonType
    createdAt: datetime
    createdBy: str
    defaultBudgetAction: DefaultQueueBudgetActionType
    description: str
    displayName: str
    farmId: str
    jobAttachmentSettings: JobAttachmentSettingsTypeDef
    jobRunAsUser: JobRunAsUserTypeDef
    queueId: str
    requiredFileSystemLocationNames: List[str]
    roleArn: str
    status: QueueStatusType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobDetailsEntityTypeDef(BaseModel):
    jobId: str
    logGroupName: str
    schemaVersion: str
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    parameters: Optional[Dict[str, JobParameterTypeDef]] = None
    pathMappingRules: Optional[List[PathMappingRuleTypeDef]] = None
    queueRoleArn: Optional[str] = None

class UpdateQueueRequestRequestTypeDef(BaseModel):
    farmId: str
    queueId: str
    allowedStorageProfileIdsToAdd: Optional[Sequence[str]] = None
    allowedStorageProfileIdsToRemove: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    defaultBudgetAction: Optional[DefaultQueueBudgetActionType] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    requiredFileSystemLocationNamesToAdd: Optional[Sequence[str]] = None
    requiredFileSystemLocationNamesToRemove: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None

class StepSearchSummaryTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    jobId: Optional[str] = None
    lifecycleStatus: Optional[StepLifecycleStatusType] = None
    lifecycleStatusMessage: Optional[str] = None
    name: Optional[str] = None
    parameterSpace: Optional[ParameterSpaceTypeDef] = None
    queueId: Optional[str] = None
    startedAt: Optional[datetime] = None
    stepId: Optional[str] = None
    targetTaskRunStatus: Optional[StepTargetTaskRunStatusType] = None
    taskRunStatus: Optional[TaskRunStatusType] = None
    taskRunStatusCounts: Optional[Dict[TaskRunStatusType, int]] = None

class SearchJobsRequestRequestTypeDef(BaseModel):
    farmId: str
    itemOffset: int
    queueIds: Sequence[str]
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SearchStepsRequestRequestTypeDef(BaseModel):
    farmId: str
    itemOffset: int
    queueIds: Sequence[str]
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    jobId: Optional[str] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SearchTasksRequestRequestTypeDef(BaseModel):
    farmId: str
    itemOffset: int
    queueIds: Sequence[str]
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    jobId: Optional[str] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SearchWorkersRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetIds: Sequence[str]
    itemOffset: int
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SessionActionSummaryTypeDef(BaseModel):
    definition: SessionActionDefinitionSummaryTypeDef
    sessionActionId: str
    status: SessionActionStatusType
    endedAt: Optional[datetime] = None
    progressPercent: Optional[float] = None
    startedAt: Optional[datetime] = None
    workerUpdatedAt: Optional[datetime] = None

class GetSessionsStatisticsAggregationResponseTypeDef(BaseModel):
    nextToken: str
    statistics: List[StatisticsTypeDef]
    status: SessionsStatisticsAggregationStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStepResponseTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    dependencyCounts: DependencyCountsTypeDef
    description: str
    endedAt: datetime
    lifecycleStatus: StepLifecycleStatusType
    lifecycleStatusMessage: str
    name: str
    parameterSpace: ParameterSpaceTypeDef
    requiredCapabilities: StepRequiredCapabilitiesTypeDef
    startedAt: datetime
    stepId: str
    targetTaskRunStatus: StepTargetTaskRunStatusType
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkerRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    workerId: str
    capabilities: Optional[WorkerCapabilitiesTypeDef] = None
    hostProperties: Optional[HostPropertiesRequestTypeDef] = None
    status: Optional[UpdatedWorkerStatusType] = None

class AssignedSessionActionTypeDef(BaseModel):
    definition: AssignedSessionActionDefinitionTypeDef
    sessionActionId: str

class GetSessionActionResponseTypeDef(BaseModel):
    definition: SessionActionDefinitionTypeDef
    endedAt: datetime
    processExitCode: int
    progressMessage: str
    progressPercent: float
    sessionActionId: str
    sessionId: str
    startedAt: datetime
    status: SessionActionStatusType
    workerUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetRequestRequestTypeDef(BaseModel):
    actions: Sequence[BudgetActionToAddTypeDef]
    approximateDollarLimit: float
    displayName: str
    farmId: str
    schedule: BudgetScheduleTypeDef
    usageTrackingResource: UsageTrackingResourceTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None

class GetBudgetResponseTypeDef(BaseModel):
    actions: List[ResponseBudgetActionTypeDef]
    approximateDollarLimit: float
    budgetId: str
    createdAt: datetime
    createdBy: str
    description: str
    displayName: str
    queueStoppedAt: datetime
    schedule: BudgetScheduleTypeDef
    status: BudgetStatusType
    updatedAt: datetime
    updatedBy: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    usages: ConsumedUsagesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBudgetRequestRequestTypeDef(BaseModel):
    budgetId: str
    farmId: str
    actionsToAdd: Optional[Sequence[BudgetActionToAddTypeDef]] = None
    actionsToRemove: Optional[Sequence[BudgetActionToRemoveTypeDef]] = None
    approximateDollarLimit: Optional[float] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    schedule: Optional[BudgetScheduleTypeDef] = None
    status: Optional[BudgetStatusType] = None

class FleetConfigurationPaginatorTypeDef(BaseModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationPaginatorTypeDef] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationPaginatorTypeDef] = None

class FleetConfigurationTypeDef(BaseModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationTypeDef] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationTypeDef] = None

class SearchWorkersResponseTypeDef(BaseModel):
    nextItemOffset: int
    totalResults: int
    workers: List[WorkerSearchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersResponseTypeDef(BaseModel):
    nextToken: str
    workers: List[WorkerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersResponsePaginatorTypeDef(BaseModel):
    nextToken: str
    workers: List[WorkerSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class JobEntityTypeDef(BaseModel):
    environmentDetails: Optional[EnvironmentDetailsEntityTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsEntityTypeDef] = None
    jobDetails: Optional[JobDetailsEntityTypeDef] = None
    stepDetails: Optional[StepDetailsEntityTypeDef] = None

class SearchStepsResponseTypeDef(BaseModel):
    nextItemOffset: int
    steps: List[StepSearchSummaryTypeDef]
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionActionsResponseTypeDef(BaseModel):
    nextToken: str
    sessionActions: List[SessionActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssignedSessionTypeDef(BaseModel):
    jobId: str
    logConfiguration: LogConfigurationTypeDef
    queueId: str
    sessionActions: List[AssignedSessionActionTypeDef]

class FleetSummaryPaginatorTypeDef(BaseModel):
    configuration: FleetConfigurationPaginatorTypeDef
    createdAt: datetime
    createdBy: str
    displayName: str
    farmId: str
    fleetId: str
    maxWorkerCount: int
    minWorkerCount: int
    status: FleetStatusType
    workerCount: int
    autoScalingStatus: Optional[AutoScalingStatusType] = None
    targetWorkerCount: Optional[int] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class CreateFleetRequestRequestTypeDef(BaseModel):
    configuration: FleetConfigurationTypeDef
    displayName: str
    farmId: str
    maxWorkerCount: int
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    minWorkerCount: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class FleetSummaryTypeDef(BaseModel):
    configuration: FleetConfigurationTypeDef
    createdAt: datetime
    createdBy: str
    displayName: str
    farmId: str
    fleetId: str
    maxWorkerCount: int
    minWorkerCount: int
    status: FleetStatusType
    workerCount: int
    autoScalingStatus: Optional[AutoScalingStatusType] = None
    targetWorkerCount: Optional[int] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class GetFleetResponseTypeDef(BaseModel):
    autoScalingStatus: AutoScalingStatusType
    capabilities: FleetCapabilitiesTypeDef
    configuration: FleetConfigurationTypeDef
    createdAt: datetime
    createdBy: str
    description: str
    displayName: str
    farmId: str
    fleetId: str
    maxWorkerCount: int
    minWorkerCount: int
    roleArn: str
    status: FleetStatusType
    targetWorkerCount: int
    updatedAt: datetime
    updatedBy: str
    workerCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetRequestRequestTypeDef(BaseModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None
    configuration: Optional[FleetConfigurationTypeDef] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    maxWorkerCount: Optional[int] = None
    minWorkerCount: Optional[int] = None
    roleArn: Optional[str] = None

class BatchGetJobEntityResponseTypeDef(BaseModel):
    entities: List[JobEntityTypeDef]
    errors: List[GetJobEntityErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkerScheduleResponseTypeDef(BaseModel):
    assignedSessions: Dict[str, AssignedSessionTypeDef]
    cancelSessionActions: Dict[str, List[str]]
    desiredWorkerStatus: Literal["STOPPED"]
    updateIntervalSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponsePaginatorTypeDef(BaseModel):
    fleets: List[FleetSummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(BaseModel):
    fleets: List[FleetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

