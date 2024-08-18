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
from aws_resource_validator.pydantic_models.deadline_constants import *

class AcceleratorCountRangeTypeDef(BaseValidatorModel):
    min: int
    max: Optional[int] = None

class AcceleratorTotalMemoryMiBRangeTypeDef(BaseValidatorModel):
    min: int
    max: Optional[int] = None

class AssignedEnvironmentEnterSessionActionDefinitionTypeDef(BaseValidatorModel):
    environmentId: str

class AssignedEnvironmentExitSessionActionDefinitionTypeDef(BaseValidatorModel):
    environmentId: str

class AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None

class LogConfigurationTypeDef(BaseValidatorModel):
    logDriver: str
    error: Optional[str] = None
    options: Optional[Dict[str, str]] = None
    parameters: Optional[Dict[str, str]] = None

class TaskParameterValueTypeDef(BaseValidatorModel):
    float: Optional[str] = None
    int: Optional[str] = None
    path: Optional[str] = None
    string: Optional[str] = None

class AssociateMemberToFarmRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class AssociateMemberToFleetRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class AssociateMemberToJobRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    identityStoreId: str
    jobId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class AssociateMemberToQueueRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class AssumeFleetRoleForReadRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str

class AwsCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: str
    expiration: datetime
    secretAccessKey: str
    sessionToken: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssumeFleetRoleForWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str

class AssumeQueueRoleForReadRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str

class AssumeQueueRoleForUserRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str

class AssumeQueueRoleForWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    queueId: str
    workerId: str

class ManifestPropertiesTypeDef(BaseValidatorModel):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: Optional[str] = None
    inputManifestHash: Optional[str] = None
    inputManifestPath: Optional[str] = None
    outputRelativeDirectories: Optional[List[str]] = None

class BudgetActionToAddTypeDef(BaseValidatorModel):
    thresholdPercentage: float
    type: BudgetActionTypeType
    description: Optional[str] = None

class BudgetActionToRemoveTypeDef(BaseValidatorModel):
    thresholdPercentage: float
    type: BudgetActionTypeType

class ConsumedUsagesTypeDef(BaseValidatorModel):
    approximateDollarUsage: float

class UsageTrackingResourceTypeDef(BaseValidatorModel):
    queueId: Optional[str] = None

class S3LocationTypeDef(BaseValidatorModel):
    bucketName: str
    key: str

class CreateFarmRequestRequestTypeDef(BaseValidatorModel):
    displayName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class JobParameterTypeDef(BaseValidatorModel):
    float: Optional[str] = None
    int: Optional[str] = None
    path: Optional[str] = None
    string: Optional[str] = None

class CreateLicenseEndpointRequestRequestTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateMonitorRequestRequestTypeDef(BaseValidatorModel):
    displayName: str
    identityCenterInstanceArn: str
    roleArn: str
    subdomain: str
    clientToken: Optional[str] = None

class CreateQueueEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    priority: int
    queueId: str
    template: str
    templateType: EnvironmentTemplateTypeType
    clientToken: Optional[str] = None

class CreateQueueFleetAssociationRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    queueId: str

class JobAttachmentSettingsTypeDef(BaseValidatorModel):
    rootPrefix: str
    s3BucketName: str

class FileSystemLocationTypeDef(BaseValidatorModel):
    name: str
    path: str
    type: FileSystemLocationTypeType

class FleetAmountCapabilityTypeDef(BaseValidatorModel):
    min: float
    name: str
    max: Optional[float] = None

class FleetAttributeCapabilityPaginatorTypeDef(BaseValidatorModel):
    name: str
    values: List[str]

class MemoryMiBRangeTypeDef(BaseValidatorModel):
    min: int
    max: Optional[int] = None

class VCpuCountRangeTypeDef(BaseValidatorModel):
    min: int
    max: Optional[int] = None

class FleetAttributeCapabilityTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]

class DeleteBudgetRequestRequestTypeDef(BaseValidatorModel):
    budgetId: str
    farmId: str

class DeleteFarmRequestRequestTypeDef(BaseValidatorModel):
    farmId: str

class DeleteFleetRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None

class DeleteLicenseEndpointRequestRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str

class DeleteMeteredProductRequestRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    productId: str

class DeleteMonitorRequestRequestTypeDef(BaseValidatorModel):
    monitorId: str

class DeleteQueueEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueEnvironmentId: str
    queueId: str

class DeleteQueueFleetAssociationRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    queueId: str

class DeleteQueueRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str

class DeleteStorageProfileRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    storageProfileId: str

class DeleteWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str

class DependencyCountsTypeDef(BaseValidatorModel):
    consumersResolved: int
    consumersUnresolved: int
    dependenciesResolved: int
    dependenciesUnresolved: int

class DisassociateMemberFromFarmRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    principalId: str

class DisassociateMemberFromFleetRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str

class DisassociateMemberFromJobRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    principalId: str
    queueId: str

class DisassociateMemberFromQueueRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    principalId: str
    queueId: str

class Ec2EbsVolumeTypeDef(BaseValidatorModel):
    iops: Optional[int] = None
    sizeGiB: Optional[int] = None
    throughputMiB: Optional[int] = None

class EnvironmentDetailsEntityTypeDef(BaseValidatorModel):
    environmentId: str
    jobId: str
    schemaVersion: str
    template: Dict[str, Any]

class EnvironmentDetailsErrorTypeDef(BaseValidatorModel):
    code: JobEntityErrorCodeType
    environmentId: str
    jobId: str
    message: str

class EnvironmentDetailsIdentifiersTypeDef(BaseValidatorModel):
    environmentId: str
    jobId: str

class EnvironmentEnterSessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    environmentId: str

class EnvironmentEnterSessionActionDefinitionTypeDef(BaseValidatorModel):
    environmentId: str

class EnvironmentExitSessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    environmentId: str

class EnvironmentExitSessionActionDefinitionTypeDef(BaseValidatorModel):
    environmentId: str

class FarmMemberTypeDef(BaseValidatorModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class FarmSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    displayName: str
    farmId: str
    kmsKeyArn: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class FieldSortExpressionTypeDef(BaseValidatorModel):
    name: str
    sortOrder: SortOrderType

class FleetMemberTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType

class GetBudgetRequestRequestTypeDef(BaseValidatorModel):
    budgetId: str
    farmId: str

class ResponseBudgetActionTypeDef(BaseValidatorModel):
    thresholdPercentage: float
    type: BudgetActionTypeType
    description: Optional[str] = None

class GetFarmRequestRequestTypeDef(BaseValidatorModel):
    farmId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetFleetRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str

class JobAttachmentDetailsErrorTypeDef(BaseValidatorModel):
    code: JobEntityErrorCodeType
    jobId: str
    message: str

class JobDetailsErrorTypeDef(BaseValidatorModel):
    code: JobEntityErrorCodeType
    jobId: str
    message: str

class StepDetailsErrorTypeDef(BaseValidatorModel):
    code: JobEntityErrorCodeType
    jobId: str
    message: str
    stepId: str

class GetJobRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str

class GetLicenseEndpointRequestRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str

class GetMonitorRequestRequestTypeDef(BaseValidatorModel):
    monitorId: str

class GetQueueEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueEnvironmentId: str
    queueId: str

class GetQueueFleetAssociationRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    queueId: str

class GetQueueRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str

class GetSessionActionRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    sessionActionId: str

class GetSessionRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    sessionId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetSessionsStatisticsAggregationRequestRequestTypeDef(BaseValidatorModel):
    aggregationId: str
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetStepRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str

class GetStorageProfileForQueueRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    storageProfileId: str

class GetStorageProfileRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    storageProfileId: str

class GetTaskRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    taskId: str

class GetWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str

class IpAddressesTypeDef(BaseValidatorModel):
    ipV4Addresses: Optional[Sequence[str]] = None
    ipV6Addresses: Optional[Sequence[str]] = None

class IpAddressesPaginatorTypeDef(BaseValidatorModel):
    ipV4Addresses: Optional[List[str]] = None
    ipV6Addresses: Optional[List[str]] = None

class JobAttachmentDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str

class PathMappingRuleTypeDef(BaseValidatorModel):
    destinationPath: str
    sourcePath: str
    sourcePathFormat: PathFormatType

class JobDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str

class StepDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str
    stepId: str

class StepDetailsEntityTypeDef(BaseValidatorModel):
    dependencies: List[str]
    jobId: str
    schemaVersion: str
    stepId: str
    template: Dict[str, Any]

class JobMemberTypeDef(BaseValidatorModel):
    farmId: str
    identityStoreId: str
    jobId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class PosixUserTypeDef(BaseValidatorModel):
    group: str
    user: str

class WindowsUserTypeDef(BaseValidatorModel):
    passwordArn: str
    user: str

class JobSummaryTypeDef(BaseValidatorModel):
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

class LicenseEndpointSummaryTypeDef(BaseValidatorModel):
    licenseEndpointId: Optional[str] = None
    status: Optional[LicenseEndpointStatusType] = None
    statusMessage: Optional[str] = None
    vpcId: Optional[str] = None

class ListAvailableMeteredProductsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MeteredProductSummaryTypeDef(BaseValidatorModel):
    family: str
    port: int
    productId: str
    vendor: str

class ListBudgetsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[BudgetStatusType] = None

class ListFarmMembersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFarmsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None

class ListFleetMembersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFleetsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    displayName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    status: Optional[FleetStatusType] = None

class ListJobMembersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None

class ListLicenseEndpointsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMeteredProductsRequestRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMonitorsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MonitorSummaryTypeDef(BaseValidatorModel):
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

class ListQueueEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueueEnvironmentSummaryTypeDef(BaseValidatorModel):
    name: str
    priority: int
    queueEnvironmentId: str

class ListQueueFleetAssociationsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    queueId: Optional[str] = None

class QueueFleetAssociationSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    fleetId: str
    queueId: str
    status: QueueFleetAssociationStatusType
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ListQueueMembersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueueMemberTypeDef(BaseValidatorModel):
    farmId: str
    identityStoreId: str
    membershipLevel: MembershipLevelType
    principalId: str
    principalType: PrincipalTypeType
    queueId: str

class ListQueuesRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None

class QueueSummaryTypeDef(BaseValidatorModel):
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

class ListSessionActionsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sessionId: Optional[str] = None
    taskId: Optional[str] = None

class ListSessionsForWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkerSessionSummaryTypeDef(BaseValidatorModel):
    jobId: str
    lifecycleStatus: SessionLifecycleStatusType
    queueId: str
    sessionId: str
    startedAt: datetime
    endedAt: Optional[datetime] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None

class ListSessionsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SessionSummaryTypeDef(BaseValidatorModel):
    fleetId: str
    lifecycleStatus: SessionLifecycleStatusType
    sessionId: str
    startedAt: datetime
    workerId: str
    endedAt: Optional[datetime] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class ListStepConsumersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StepConsumerTypeDef(BaseValidatorModel):
    status: DependencyConsumerResolutionStatusType
    stepId: str

class ListStepDependenciesRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StepDependencyTypeDef(BaseValidatorModel):
    status: DependencyConsumerResolutionStatusType
    stepId: str

class ListStepsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStorageProfilesForQueueRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StorageProfileSummaryTypeDef(BaseValidatorModel):
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    storageProfileId: str

class ListStorageProfilesRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTasksRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ParameterFilterExpressionTypeDef(BaseValidatorModel):
    name: str
    operator: ComparisonOperatorType
    value: str

class ParameterSortExpressionTypeDef(BaseValidatorModel):
    name: str
    sortOrder: SortOrderType

class StepParameterTypeDef(BaseValidatorModel):
    name: str
    type: StepParameterTypeType

class PutMeteredProductRequestRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    productId: str

class SearchTermFilterExpressionTypeDef(BaseValidatorModel):
    searchTerm: str

class StringFilterExpressionTypeDef(BaseValidatorModel):
    name: str
    operator: ComparisonOperatorType
    value: str

class SearchGroupedFilterExpressionsTypeDef(BaseValidatorModel):
    filters: Sequence["SearchFilterExpressionTypeDef"]
    operator: LogicalOperatorType

class UserJobsFirstTypeDef(BaseValidatorModel):
    userIdentityId: str

class ServiceManagedEc2InstanceMarketOptionsTypeDef(BaseValidatorModel):
    type: Ec2MarketTypeType

class SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None

class TaskRunSessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    stepId: str
    taskId: str

class SyncInputJobAttachmentsSessionActionDefinitionTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None

class SessionsStatisticsResourcesTypeDef(BaseValidatorModel):
    fleetIds: Optional[Sequence[str]] = None
    queueIds: Optional[Sequence[str]] = None

class StatsTypeDef(BaseValidatorModel):
    avg: Optional[float] = None
    max: Optional[float] = None
    min: Optional[float] = None
    sum: Optional[float] = None

class StepAmountCapabilityTypeDef(BaseValidatorModel):
    name: str
    max: Optional[float] = None
    min: Optional[float] = None
    value: Optional[float] = None

class StepAttributeCapabilityTypeDef(BaseValidatorModel):
    name: str
    allOf: Optional[List[str]] = None
    anyOf: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateFarmRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    description: Optional[str] = None
    displayName: Optional[str] = None

class UpdateJobRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    clientToken: Optional[str] = None
    lifecycleStatus: Optional[Literal["ARCHIVED"]] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    priority: Optional[int] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None

class UpdateMonitorRequestRequestTypeDef(BaseValidatorModel):
    monitorId: str
    displayName: Optional[str] = None
    roleArn: Optional[str] = None
    subdomain: Optional[str] = None

class UpdateQueueEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueEnvironmentId: str
    queueId: str
    clientToken: Optional[str] = None
    priority: Optional[int] = None
    template: Optional[str] = None
    templateType: Optional[EnvironmentTemplateTypeType] = None

class UpdateQueueFleetAssociationRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    queueId: str
    status: UpdateQueueFleetAssociationStatusType

class UpdateSessionRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    sessionId: str
    targetLifecycleStatus: Literal["ENDED"]
    clientToken: Optional[str] = None

class UpdateStepRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    targetTaskRunStatus: StepTargetTaskRunStatusType
    clientToken: Optional[str] = None

class UpdateTaskRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    targetRunStatus: TaskTargetRunStatusType
    taskId: str
    clientToken: Optional[str] = None

class WorkerAmountCapabilityTypeDef(BaseValidatorModel):
    name: str
    value: float

class WorkerAttributeCapabilityTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]

class AssignedTaskRunSessionActionDefinitionTypeDef(BaseValidatorModel):
    parameters: Dict[str, TaskParameterValueTypeDef]
    stepId: str
    taskId: str

class TaskRunSessionActionDefinitionTypeDef(BaseValidatorModel):
    parameters: Dict[str, TaskParameterValueTypeDef]
    stepId: str
    taskId: str

class TaskSearchSummaryTypeDef(BaseValidatorModel):
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

class TaskSummaryTypeDef(BaseValidatorModel):
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

class AssumeFleetRoleForReadResponseTypeDef(BaseValidatorModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeFleetRoleForWorkerResponseTypeDef(BaseValidatorModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForReadResponseTypeDef(BaseValidatorModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForUserResponseTypeDef(BaseValidatorModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeQueueRoleForWorkerResponseTypeDef(BaseValidatorModel):
    credentials: AwsCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyJobTemplateResponseTypeDef(BaseValidatorModel):
    templateType: JobTemplateTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetResponseTypeDef(BaseValidatorModel):
    budgetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFarmResponseTypeDef(BaseValidatorModel):
    farmId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseValidatorModel):
    fleetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseEndpointResponseTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitorResponseTypeDef(BaseValidatorModel):
    identityCenterApplicationArn: str
    monitorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueEnvironmentResponseTypeDef(BaseValidatorModel):
    queueEnvironmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResponseTypeDef(BaseValidatorModel):
    queueId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageProfileResponseTypeDef(BaseValidatorModel):
    storageProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkerResponseTypeDef(BaseValidatorModel):
    workerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFarmResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    displayName: str
    farmId: str
    kmsKeyArn: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseEndpointResponseTypeDef(BaseValidatorModel):
    dnsName: str
    licenseEndpointId: str
    securityGroupIds: List[str]
    status: LicenseEndpointStatusType
    statusMessage: str
    subnetIds: List[str]
    vpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMonitorResponseTypeDef(BaseValidatorModel):
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

class GetQueueEnvironmentResponseTypeDef(BaseValidatorModel):
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

class GetQueueFleetAssociationResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    fleetId: str
    queueId: str
    status: QueueFleetAssociationStatusType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaskResponseTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionsStatisticsAggregationResponseTypeDef(BaseValidatorModel):
    aggregationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkerResponseTypeDef(BaseValidatorModel):
    log: LogConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentsTypeDef(BaseValidatorModel):
    manifests: List[ManifestPropertiesTypeDef]
    fileSystem: Optional[JobAttachmentsFileSystemType] = None

class BudgetSummaryTypeDef(BaseValidatorModel):
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

class CopyJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    targetS3Location: S3LocationTypeDef

class JobSearchSummaryTypeDef(BaseValidatorModel):
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

class CreateStorageProfileRequestRequestTypeDef(BaseValidatorModel):
    displayName: str
    farmId: str
    osFamily: StorageProfileOperatingSystemFamilyType
    clientToken: Optional[str] = None
    fileSystemLocations: Optional[Sequence[FileSystemLocationTypeDef]] = None

class GetStorageProfileForQueueResponseTypeDef(BaseValidatorModel):
    displayName: str
    fileSystemLocations: List[FileSystemLocationTypeDef]
    osFamily: StorageProfileOperatingSystemFamilyType
    storageProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStorageProfileResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    displayName: str
    fileSystemLocations: List[FileSystemLocationTypeDef]
    osFamily: StorageProfileOperatingSystemFamilyType
    storageProfileId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStorageProfileRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    storageProfileId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    fileSystemLocationsToAdd: Optional[Sequence[FileSystemLocationTypeDef]] = None
    fileSystemLocationsToRemove: Optional[Sequence[FileSystemLocationTypeDef]] = None
    osFamily: Optional[StorageProfileOperatingSystemFamilyType] = None

class CustomerManagedWorkerCapabilitiesPaginatorTypeDef(BaseValidatorModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    acceleratorCount: Optional[AcceleratorCountRangeTypeDef] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRangeTypeDef] = None
    acceleratorTypes: Optional[List[Literal["gpu"]]] = None
    customAmounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityPaginatorTypeDef]] = None

class CustomerManagedWorkerCapabilitiesTypeDef(BaseValidatorModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    acceleratorCount: Optional[AcceleratorCountRangeTypeDef] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRangeTypeDef] = None
    acceleratorTypes: Optional[Sequence[Literal["gpu"]]] = None
    customAmounts: Optional[Sequence[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapabilityTypeDef]] = None

class FleetCapabilitiesTypeDef(BaseValidatorModel):
    amounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    attributes: Optional[List[FleetAttributeCapabilityTypeDef]] = None

class DateTimeFilterExpressionTypeDef(BaseValidatorModel):
    dateTime: TimestampTypeDef
    name: str
    operator: ComparisonOperatorType

class FixedBudgetScheduleTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef

class UpdatedSessionActionInfoTypeDef(BaseValidatorModel):
    completedStatus: Optional[CompletedStatusType] = None
    endedAt: Optional[TimestampTypeDef] = None
    processExitCode: Optional[int] = None
    progressMessage: Optional[str] = None
    progressPercent: Optional[float] = None
    startedAt: Optional[TimestampTypeDef] = None
    updatedAt: Optional[TimestampTypeDef] = None

class StepSummaryTypeDef(BaseValidatorModel):
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

class ServiceManagedEc2InstanceCapabilitiesPaginatorTypeDef(BaseValidatorModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    allowedInstanceTypes: Optional[List[str]] = None
    customAmounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityPaginatorTypeDef]] = None
    excludedInstanceTypes: Optional[List[str]] = None
    rootEbsVolume: Optional[Ec2EbsVolumeTypeDef] = None

class ServiceManagedEc2InstanceCapabilitiesTypeDef(BaseValidatorModel):
    cpuArchitectureType: CpuArchitectureTypeType
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    vCpuCount: VCpuCountRangeTypeDef
    allowedInstanceTypes: Optional[Sequence[str]] = None
    customAmounts: Optional[Sequence[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapabilityTypeDef]] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    rootEbsVolume: Optional[Ec2EbsVolumeTypeDef] = None

class ListFarmMembersResponseTypeDef(BaseValidatorModel):
    members: List[FarmMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFarmsResponseTypeDef(BaseValidatorModel):
    farms: List[FarmSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetMembersResponseTypeDef(BaseValidatorModel):
    members: List[FleetMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFleetRequestFleetActiveWaitTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetJobRequestJobCreateCompleteWaitTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLicenseEndpointRequestLicenseEndpointDeletedWaitTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLicenseEndpointRequestLicenseEndpointValidWaitTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetQueueFleetAssociationRequestQueueFleetAssociationStoppedWaitTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetQueueRequestQueueSchedulingBlockedWaitTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetQueueRequestQueueSchedulingWaitTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetJobEntityErrorTypeDef(BaseValidatorModel):
    environmentDetails: Optional[EnvironmentDetailsErrorTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsErrorTypeDef] = None
    jobDetails: Optional[JobDetailsErrorTypeDef] = None
    stepDetails: Optional[StepDetailsErrorTypeDef] = None

class GetSessionsStatisticsAggregationRequestGetSessionsStatisticsAggregationPaginateTypeDef(BaseValidatorModel):
    aggregationId: str
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAvailableMeteredProductsRequestListAvailableMeteredProductsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBudgetsRequestListBudgetsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    status: Optional[BudgetStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFarmMembersRequestListFarmMembersPaginateTypeDef(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFarmsRequestListFarmsPaginateTypeDef(BaseValidatorModel):
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetMembersRequestListFleetMembersPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsRequestListFleetsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    displayName: Optional[str] = None
    principalId: Optional[str] = None
    status: Optional[FleetStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobMembersRequestListJobMembersPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLicenseEndpointsRequestListLicenseEndpointsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMeteredProductsRequestListMeteredProductsPaginateTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsRequestListMonitorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueEnvironmentsRequestListQueueEnvironmentsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueFleetAssociationsRequestListQueueFleetAssociationsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: Optional[str] = None
    queueId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueMembersRequestListQueueMembersPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSessionActionsRequestListSessionActionsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    sessionId: Optional[str] = None
    taskId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSessionsForWorkerRequestListSessionsForWorkerPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSessionsRequestListSessionsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepConsumersRequestListStepConsumersPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepDependenciesRequestListStepDependenciesPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStepsRequestListStepsPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStorageProfilesForQueueRequestListStorageProfilesForQueuePaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStorageProfilesRequestListStorageProfilesPaginateTypeDef(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksRequestListTasksPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkersRequestListWorkersPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class HostPropertiesRequestTypeDef(BaseValidatorModel):
    hostName: Optional[str] = None
    ipAddresses: Optional[IpAddressesTypeDef] = None

class HostPropertiesResponseTypeDef(BaseValidatorModel):
    ec2InstanceArn: Optional[str] = None
    ec2InstanceType: Optional[str] = None
    hostName: Optional[str] = None
    ipAddresses: Optional[IpAddressesTypeDef] = None

class HostPropertiesResponsePaginatorTypeDef(BaseValidatorModel):
    ec2InstanceArn: Optional[str] = None
    ec2InstanceType: Optional[str] = None
    hostName: Optional[str] = None
    ipAddresses: Optional[IpAddressesPaginatorTypeDef] = None

class JobEntityIdentifiersUnionTypeDef(BaseValidatorModel):
    environmentDetails: Optional[EnvironmentDetailsIdentifiersTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsIdentifiersTypeDef] = None
    jobDetails: Optional[JobDetailsIdentifiersTypeDef] = None
    stepDetails: Optional[StepDetailsIdentifiersTypeDef] = None

class ListJobMembersResponseTypeDef(BaseValidatorModel):
    members: List[JobMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobRunAsUserTypeDef(BaseValidatorModel):
    runAs: RunAsType
    posix: Optional[PosixUserTypeDef] = None
    windows: Optional[WindowsUserTypeDef] = None

class ListJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseEndpointsResponseTypeDef(BaseValidatorModel):
    licenseEndpoints: List[LicenseEndpointSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableMeteredProductsResponseTypeDef(BaseValidatorModel):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMeteredProductsResponseTypeDef(BaseValidatorModel):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMonitorsResponseTypeDef(BaseValidatorModel):
    monitors: List[MonitorSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueueEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[QueueEnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueueFleetAssociationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    queueFleetAssociations: List[QueueFleetAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueueMembersResponseTypeDef(BaseValidatorModel):
    members: List[QueueMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueuesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    queues: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsForWorkerResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sessions: List[WorkerSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStepConsumersResponseTypeDef(BaseValidatorModel):
    consumers: List[StepConsumerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStepDependenciesResponseTypeDef(BaseValidatorModel):
    dependencies: List[StepDependencyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageProfilesForQueueResponseTypeDef(BaseValidatorModel):
    nextToken: str
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageProfilesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ParameterSpaceTypeDef(BaseValidatorModel):
    parameters: List[StepParameterTypeDef]
    combination: Optional[str] = None

class SearchSortExpressionTypeDef(BaseValidatorModel):
    fieldSort: Optional[FieldSortExpressionTypeDef] = None
    parameterSort: Optional[ParameterSortExpressionTypeDef] = None
    userJobsFirst: Optional[UserJobsFirstTypeDef] = None

class SessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionSummaryTypeDef] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionSummaryTypeDef] = None
    syncInputJobAttachments: Optional[       SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef     ] = None
    taskRun: Optional[TaskRunSessionActionDefinitionSummaryTypeDef] = None

class StartSessionsStatisticsAggregationRequestRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    farmId: str
    groupBy: Sequence[UsageGroupByFieldType]
    resourceIds: SessionsStatisticsResourcesTypeDef
    startTime: TimestampTypeDef
    statistics: Sequence[UsageStatisticType]
    period: Optional[PeriodType] = None
    timezone: Optional[str] = None

class StatisticsTypeDef(BaseValidatorModel):
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

class StepRequiredCapabilitiesTypeDef(BaseValidatorModel):
    amounts: List[StepAmountCapabilityTypeDef]
    attributes: List[StepAttributeCapabilityTypeDef]

class WorkerCapabilitiesTypeDef(BaseValidatorModel):
    amounts: Sequence[WorkerAmountCapabilityTypeDef]
    attributes: Sequence[WorkerAttributeCapabilityTypeDef]

class AssignedSessionActionDefinitionTypeDef(BaseValidatorModel):
    envEnter: Optional[AssignedEnvironmentEnterSessionActionDefinitionTypeDef] = None
    envExit: Optional[AssignedEnvironmentExitSessionActionDefinitionTypeDef] = None
    syncInputJobAttachments: Optional[       AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef     ] = None
    taskRun: Optional[AssignedTaskRunSessionActionDefinitionTypeDef] = None

class SessionActionDefinitionTypeDef(BaseValidatorModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionTypeDef] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionTypeDef] = None
    syncInputJobAttachments: Optional[       SyncInputJobAttachmentsSessionActionDefinitionTypeDef     ] = None
    taskRun: Optional[TaskRunSessionActionDefinitionTypeDef] = None

class SearchTasksResponseTypeDef(BaseValidatorModel):
    nextItemOffset: int
    tasks: List[TaskSearchSummaryTypeDef]
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTasksResponseTypeDef(BaseValidatorModel):
    nextToken: str
    tasks: List[TaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestRequestTypeDef(BaseValidatorModel):
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

class GetJobResponseTypeDef(BaseValidatorModel):
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

class JobAttachmentDetailsEntityTypeDef(BaseValidatorModel):
    attachments: AttachmentsTypeDef
    jobId: str

class ListBudgetsResponseTypeDef(BaseValidatorModel):
    budgets: List[BudgetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerManagedFleetConfigurationPaginatorTypeDef(BaseValidatorModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesPaginatorTypeDef
    storageProfileId: Optional[str] = None

class CustomerManagedFleetConfigurationTypeDef(BaseValidatorModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesTypeDef
    storageProfileId: Optional[str] = None

class SearchFilterExpressionTypeDef(BaseValidatorModel):
    dateTimeFilter: Optional[DateTimeFilterExpressionTypeDef] = None
    groupFilter: Optional[Dict[str, Any]] = None
    parameterFilter: Optional[ParameterFilterExpressionTypeDef] = None
    searchTermFilter: Optional[SearchTermFilterExpressionTypeDef] = None
    stringFilter: Optional[StringFilterExpressionTypeDef] = None

class BudgetScheduleTypeDef(BaseValidatorModel):
    fixed: Optional[FixedBudgetScheduleTypeDef] = None

class UpdateWorkerScheduleRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    updatedSessionActions: Optional[Mapping[str, UpdatedSessionActionInfoTypeDef]] = None

class ListStepsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    steps: List[StepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceManagedEc2FleetConfigurationPaginatorTypeDef(BaseValidatorModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesPaginatorTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef

class ServiceManagedEc2FleetConfigurationTypeDef(BaseValidatorModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef

class CreateWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None
    hostProperties: Optional[HostPropertiesRequestTypeDef] = None

class GetSessionResponseTypeDef(BaseValidatorModel):
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

class GetWorkerResponseTypeDef(BaseValidatorModel):
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

class WorkerSearchSummaryTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    fleetId: Optional[str] = None
    hostProperties: Optional[HostPropertiesResponseTypeDef] = None
    status: Optional[WorkerStatusType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    workerId: Optional[str] = None

class WorkerSummaryTypeDef(BaseValidatorModel):
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

class WorkerSummaryPaginatorTypeDef(BaseValidatorModel):
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

class BatchGetJobEntityRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    identifiers: Sequence[JobEntityIdentifiersUnionTypeDef]
    workerId: str

class CreateQueueRequestRequestTypeDef(BaseValidatorModel):
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

class GetQueueResponseTypeDef(BaseValidatorModel):
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

class JobDetailsEntityTypeDef(BaseValidatorModel):
    jobId: str
    logGroupName: str
    schemaVersion: str
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    parameters: Optional[Dict[str, JobParameterTypeDef]] = None
    pathMappingRules: Optional[List[PathMappingRuleTypeDef]] = None
    queueRoleArn: Optional[str] = None

class UpdateQueueRequestRequestTypeDef(BaseValidatorModel):
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

class StepSearchSummaryTypeDef(BaseValidatorModel):
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

class SearchJobsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    itemOffset: int
    queueIds: Sequence[str]
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SearchStepsRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    itemOffset: int
    queueIds: Sequence[str]
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    jobId: Optional[str] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SearchTasksRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    itemOffset: int
    queueIds: Sequence[str]
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    jobId: Optional[str] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SearchWorkersRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetIds: Sequence[str]
    itemOffset: int
    filterExpressions: Optional["SearchGroupedFilterExpressionsTypeDef"] = None
    pageSize: Optional[int] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None

class SessionActionSummaryTypeDef(BaseValidatorModel):
    definition: SessionActionDefinitionSummaryTypeDef
    sessionActionId: str
    status: SessionActionStatusType
    endedAt: Optional[datetime] = None
    progressPercent: Optional[float] = None
    startedAt: Optional[datetime] = None
    workerUpdatedAt: Optional[datetime] = None

class GetSessionsStatisticsAggregationResponseTypeDef(BaseValidatorModel):
    nextToken: str
    statistics: List[StatisticsTypeDef]
    status: SessionsStatisticsAggregationStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStepResponseTypeDef(BaseValidatorModel):
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

class UpdateWorkerRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    capabilities: Optional[WorkerCapabilitiesTypeDef] = None
    hostProperties: Optional[HostPropertiesRequestTypeDef] = None
    status: Optional[UpdatedWorkerStatusType] = None

class AssignedSessionActionTypeDef(BaseValidatorModel):
    definition: AssignedSessionActionDefinitionTypeDef
    sessionActionId: str

class GetSessionActionResponseTypeDef(BaseValidatorModel):
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

class CreateBudgetRequestRequestTypeDef(BaseValidatorModel):
    actions: Sequence[BudgetActionToAddTypeDef]
    approximateDollarLimit: float
    displayName: str
    farmId: str
    schedule: BudgetScheduleTypeDef
    usageTrackingResource: UsageTrackingResourceTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None

class GetBudgetResponseTypeDef(BaseValidatorModel):
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

class UpdateBudgetRequestRequestTypeDef(BaseValidatorModel):
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

class FleetConfigurationPaginatorTypeDef(BaseValidatorModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationPaginatorTypeDef] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationPaginatorTypeDef] = None

class FleetConfigurationTypeDef(BaseValidatorModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationTypeDef] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationTypeDef] = None

class SearchWorkersResponseTypeDef(BaseValidatorModel):
    nextItemOffset: int
    totalResults: int
    workers: List[WorkerSearchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersResponseTypeDef(BaseValidatorModel):
    nextToken: str
    workers: List[WorkerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersResponsePaginatorTypeDef(BaseValidatorModel):
    nextToken: str
    workers: List[WorkerSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class JobEntityTypeDef(BaseValidatorModel):
    environmentDetails: Optional[EnvironmentDetailsEntityTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsEntityTypeDef] = None
    jobDetails: Optional[JobDetailsEntityTypeDef] = None
    stepDetails: Optional[StepDetailsEntityTypeDef] = None

class SearchStepsResponseTypeDef(BaseValidatorModel):
    nextItemOffset: int
    steps: List[StepSearchSummaryTypeDef]
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionActionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sessionActions: List[SessionActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssignedSessionTypeDef(BaseValidatorModel):
    jobId: str
    logConfiguration: LogConfigurationTypeDef
    queueId: str
    sessionActions: List[AssignedSessionActionTypeDef]

class FleetSummaryPaginatorTypeDef(BaseValidatorModel):
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

class CreateFleetRequestRequestTypeDef(BaseValidatorModel):
    configuration: FleetConfigurationTypeDef
    displayName: str
    farmId: str
    maxWorkerCount: int
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    minWorkerCount: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class FleetSummaryTypeDef(BaseValidatorModel):
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

class GetFleetResponseTypeDef(BaseValidatorModel):
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

class UpdateFleetRequestRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None
    configuration: Optional[FleetConfigurationTypeDef] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    maxWorkerCount: Optional[int] = None
    minWorkerCount: Optional[int] = None
    roleArn: Optional[str] = None

class BatchGetJobEntityResponseTypeDef(BaseValidatorModel):
    entities: List[JobEntityTypeDef]
    errors: List[GetJobEntityErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkerScheduleResponseTypeDef(BaseValidatorModel):
    assignedSessions: Dict[str, AssignedSessionTypeDef]
    cancelSessionActions: Dict[str, List[str]]
    desiredWorkerStatus: Literal["STOPPED"]
    updateIntervalSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponsePaginatorTypeDef(BaseValidatorModel):
    fleets: List[FleetSummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(BaseValidatorModel):
    fleets: List[FleetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

