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
from aws_resource_validator.pydantic_models.deadline_constants import *

class AcceleratorSelectionTypeDef(BaseValidatorModel):
    name: AcceleratorNameType
    runtime: Optional[str] = None


class AcquiredLimitTypeDef(BaseValidatorModel):
    limitId: str
    count: int


class AssignedEnvironmentEnterSessionActionDefinitionTypeDef(BaseValidatorModel):
    environmentId: str


class AssignedEnvironmentExitSessionActionDefinitionTypeDef(BaseValidatorModel):
    environmentId: str


class AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None


class LogConfigurationTypeDef(BaseValidatorModel):
    logDriver: str
    options: Optional[Dict[str, str]] = None
    parameters: Optional[Dict[str, str]] = None
    error: Optional[str] = None


class AssociateMemberToFarmRequestTypeDef(BaseValidatorModel):
    farmId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssociateMemberToFleetRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssociateMemberToJobRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssociateMemberToQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssumeFleetRoleForReadRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str


class AwsCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str
    expiration: datetime


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssumeFleetRoleForWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str


class AssumeQueueRoleForReadRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str


class AssumeQueueRoleForUserRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str


class AssumeQueueRoleForWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    queueId: str


class ManifestPropertiesOutputTypeDef(BaseValidatorModel):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: Optional[str] = None
    outputRelativeDirectories: Optional[List[str]] = None
    inputManifestPath: Optional[str] = None
    inputManifestHash: Optional[str] = None


class ManifestPropertiesTypeDef(BaseValidatorModel):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: Optional[str] = None
    outputRelativeDirectories: Optional[Sequence[str]] = None
    inputManifestPath: Optional[str] = None
    inputManifestHash: Optional[str] = None


class FixedBudgetScheduleOutputTypeDef(BaseValidatorModel):
    startTime: datetime
    endTime: datetime


class ConsumedUsagesTypeDef(BaseValidatorModel):
    approximateDollarUsage: float


class UsageTrackingResourceTypeDef(BaseValidatorModel):
    queueId: Optional[str] = None


class S3LocationTypeDef(BaseValidatorModel):
    bucketName: str
    key: str


class CreateFarmRequestTypeDef(BaseValidatorModel):
    displayName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateLicenseEndpointRequestTypeDef(BaseValidatorModel):
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateLimitRequestTypeDef(BaseValidatorModel):
    displayName: str
    amountRequirementName: str
    maxCount: int
    farmId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class CreateMonitorRequestTypeDef(BaseValidatorModel):
    displayName: str
    identityCenterInstanceArn: str
    subdomain: str
    roleArn: str
    clientToken: Optional[str] = None


class CreateQueueEnvironmentRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    priority: int
    templateType: EnvironmentTemplateTypeType
    template: str
    clientToken: Optional[str] = None


class CreateQueueFleetAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str


class CreateQueueLimitAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str


class JobAttachmentSettingsTypeDef(BaseValidatorModel):
    s3BucketName: str
    rootPrefix: str


class FleetAttributeCapabilityOutputTypeDef(BaseValidatorModel):
    name: str
    values: List[str]


class FleetAttributeCapabilityTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]


class DeleteBudgetRequestTypeDef(BaseValidatorModel):
    farmId: str
    budgetId: str


class DeleteFarmRequestTypeDef(BaseValidatorModel):
    farmId: str


class DeleteFleetRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None


class DeleteLicenseEndpointRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str


class DeleteLimitRequestTypeDef(BaseValidatorModel):
    farmId: str
    limitId: str


class DeleteMeteredProductRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    productId: str


class DeleteMonitorRequestTypeDef(BaseValidatorModel):
    monitorId: str


class DeleteQueueEnvironmentRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    queueEnvironmentId: str


class DeleteQueueFleetAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str


class DeleteQueueLimitAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str


class DeleteQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str


class DeleteStorageProfileRequestTypeDef(BaseValidatorModel):
    farmId: str
    storageProfileId: str


class DeleteWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str


class DependencyCountsTypeDef(BaseValidatorModel):
    dependenciesResolved: int
    dependenciesUnresolved: int
    consumersResolved: int
    consumersUnresolved: int


class DisassociateMemberFromFarmRequestTypeDef(BaseValidatorModel):
    farmId: str
    principalId: str


class DisassociateMemberFromFleetRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str


class DisassociateMemberFromJobRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    principalId: str


class DisassociateMemberFromQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: str


class Ec2EbsVolumeTypeDef(BaseValidatorModel):
    sizeGiB: Optional[int] = None
    iops: Optional[int] = None
    throughputMiB: Optional[int] = None


class EnvironmentDetailsEntityTypeDef(BaseValidatorModel):
    jobId: str
    environmentId: str
    schemaVersion: str
    template: Dict[str, Any]


class EnvironmentDetailsErrorTypeDef(BaseValidatorModel):
    jobId: str
    environmentId: str
    code: JobEntityErrorCodeType
    message: str


class EnvironmentDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str
    environmentId: str


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
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class FarmSummaryTypeDef(BaseValidatorModel):
    farmId: str
    displayName: str
    createdAt: datetime
    createdBy: str
    kmsKeyArn: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class FieldSortExpressionTypeDef(BaseValidatorModel):
    sortOrder: SortOrderType
    name: str


class FleetMemberTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class GetBudgetRequestTypeDef(BaseValidatorModel):
    farmId: str
    budgetId: str


class GetFarmRequestTypeDef(BaseValidatorModel):
    farmId: str


class GetFleetRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class JobAttachmentDetailsErrorTypeDef(BaseValidatorModel):
    jobId: str
    code: JobEntityErrorCodeType
    message: str


class JobDetailsErrorTypeDef(BaseValidatorModel):
    jobId: str
    code: JobEntityErrorCodeType
    message: str


class StepDetailsErrorTypeDef(BaseValidatorModel):
    jobId: str
    stepId: str
    code: JobEntityErrorCodeType
    message: str


class GetJobRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str


class GetLicenseEndpointRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str


class GetLimitRequestTypeDef(BaseValidatorModel):
    farmId: str
    limitId: str


class GetMonitorRequestTypeDef(BaseValidatorModel):
    monitorId: str


class GetQueueEnvironmentRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    queueEnvironmentId: str


class GetQueueFleetAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str


class GetQueueLimitAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str


class GetQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str


class GetSessionActionRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionActionId: str


class GetSessionRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetSessionsStatisticsAggregationRequestTypeDef(BaseValidatorModel):
    farmId: str
    aggregationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetStepRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str


class GetStorageProfileForQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    storageProfileId: str


class GetStorageProfileRequestTypeDef(BaseValidatorModel):
    farmId: str
    storageProfileId: str


class GetTaskRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    taskId: str


class GetWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str


class IpAddressesOutputTypeDef(BaseValidatorModel):
    ipV4Addresses: Optional[List[str]] = None
    ipV6Addresses: Optional[List[str]] = None


class IpAddressesTypeDef(BaseValidatorModel):
    ipV4Addresses: Optional[Sequence[str]] = None
    ipV6Addresses: Optional[Sequence[str]] = None


class JobAttachmentDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str


class PathMappingRuleTypeDef(BaseValidatorModel):
    sourcePathFormat: PathFormatType
    sourcePath: str
    destinationPath: str


class JobDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str


class StepDetailsIdentifiersTypeDef(BaseValidatorModel):
    jobId: str
    stepId: str


class StepDetailsEntityTypeDef(BaseValidatorModel):
    jobId: str
    stepId: str
    schemaVersion: str
    template: Dict[str, Any]
    dependencies: List[str]


class JobMemberTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class PosixUserTypeDef(BaseValidatorModel):
    user: str
    group: str


class WindowsUserTypeDef(BaseValidatorModel):
    user: str
    passwordArn: str


class JobSummaryTypeDef(BaseValidatorModel):
    jobId: str
    name: str
    lifecycleStatus: JobLifecycleStatusType
    lifecycleStatusMessage: str
    priority: int
    createdAt: datetime
    createdBy: str
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    taskRunStatus: Optional[TaskRunStatusType] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None
    taskRunStatusCounts: Optional[Dict[TaskRunStatusType, int]] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    maxWorkerCount: Optional[int] = None
    sourceJobId: Optional[str] = None


class LicenseEndpointSummaryTypeDef(BaseValidatorModel):
    licenseEndpointId: Optional[str] = None
    status: Optional[LicenseEndpointStatusType] = None
    statusMessage: Optional[str] = None
    vpcId: Optional[str] = None


class LimitSummaryTypeDef(BaseValidatorModel):
    displayName: str
    amountRequirementName: str
    maxCount: int
    createdAt: datetime
    createdBy: str
    farmId: str
    limitId: str
    currentCount: int
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListAvailableMeteredProductsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MeteredProductSummaryTypeDef(BaseValidatorModel):
    productId: str
    family: str
    vendor: str
    port: int


class ListBudgetsRequestTypeDef(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[BudgetStatusType] = None


class ListFarmMembersRequestTypeDef(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFarmsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    maxResults: Optional[int] = None


class ListFleetMembersRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFleetsRequestTypeDef(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[FleetStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobMembersRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobParameterDefinitionsRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListLicenseEndpointsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListLimitsRequestTypeDef(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMeteredProductsRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMonitorsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MonitorSummaryTypeDef(BaseValidatorModel):
    monitorId: str
    displayName: str
    subdomain: str
    url: str
    roleArn: str
    identityCenterInstanceArn: str
    identityCenterApplicationArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListQueueEnvironmentsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueEnvironmentSummaryTypeDef(BaseValidatorModel):
    queueEnvironmentId: str
    name: str
    priority: int


class ListQueueFleetAssociationsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    fleetId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueFleetAssociationSummaryTypeDef(BaseValidatorModel):
    queueId: str
    fleetId: str
    status: QueueFleetAssociationStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListQueueLimitAssociationsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    limitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueLimitAssociationSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    queueId: str
    limitId: str
    status: QueueLimitAssociationStatusType
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListQueueMembersRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueMemberTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class ListQueuesRequestTypeDef(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueSummaryTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    displayName: str
    status: QueueStatusType
    defaultBudgetAction: DefaultQueueBudgetActionType
    createdAt: datetime
    createdBy: str
    blockedReason: Optional[QueueBlockedReasonType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListSessionActionsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionId: Optional[str] = None
    taskId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSessionsForWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkerSessionSummaryTypeDef(BaseValidatorModel):
    sessionId: str
    queueId: str
    jobId: str
    startedAt: datetime
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: Optional[datetime] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None


class ListSessionsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SessionSummaryTypeDef(BaseValidatorModel):
    sessionId: str
    fleetId: str
    workerId: str
    startedAt: datetime
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None


class ListStepConsumersRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StepConsumerTypeDef(BaseValidatorModel):
    stepId: str
    status: DependencyConsumerResolutionStatusType


class ListStepDependenciesRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StepDependencyTypeDef(BaseValidatorModel):
    stepId: str
    status: DependencyConsumerResolutionStatusType


class ListStepsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListStorageProfilesForQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StorageProfileSummaryTypeDef(BaseValidatorModel):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType


class ListStorageProfilesRequestTypeDef(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTasksRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkersRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ParameterSortExpressionTypeDef(BaseValidatorModel):
    sortOrder: SortOrderType
    name: str


class PutMeteredProductRequestTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    productId: str


class SearchTermFilterExpressionTypeDef(BaseValidatorModel):
    searchTerm: str


class UserJobsFirstTypeDef(BaseValidatorModel):
    userIdentityId: str


class SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None


class TaskRunSessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    taskId: str
    stepId: str


class SyncInputJobAttachmentsSessionActionDefinitionTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None


class SessionsStatisticsResourcesTypeDef(BaseValidatorModel):
    queueIds: Optional[Sequence[str]] = None
    fleetIds: Optional[Sequence[str]] = None


class StepAttributeCapabilityTypeDef(BaseValidatorModel):
    name: str
    anyOf: Optional[List[str]] = None
    allOf: Optional[List[str]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateFarmRequestTypeDef(BaseValidatorModel):
    farmId: str
    displayName: Optional[str] = None
    description: Optional[str] = None


class UpdateJobRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    clientToken: Optional[str] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None
    priority: Optional[int] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    lifecycleStatus: Optional[Literal["ARCHIVED"]] = None
    maxWorkerCount: Optional[int] = None


class UpdateLimitRequestTypeDef(BaseValidatorModel):
    farmId: str
    limitId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    maxCount: Optional[int] = None


class UpdateMonitorRequestTypeDef(BaseValidatorModel):
    monitorId: str
    subdomain: Optional[str] = None
    displayName: Optional[str] = None
    roleArn: Optional[str] = None


class UpdateQueueEnvironmentRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    queueEnvironmentId: str
    clientToken: Optional[str] = None
    priority: Optional[int] = None
    templateType: Optional[EnvironmentTemplateTypeType] = None
    template: Optional[str] = None


class UpdateQueueFleetAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str
    status: UpdateQueueFleetAssociationStatusType


class UpdateQueueLimitAssociationRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str
    status: UpdateQueueLimitAssociationStatusType


class UpdateSessionRequestTypeDef(BaseValidatorModel):
    targetLifecycleStatus: Literal["ENDED"]
    farmId: str
    queueId: str
    jobId: str
    sessionId: str
    clientToken: Optional[str] = None


class UpdateStepRequestTypeDef(BaseValidatorModel):
    targetTaskRunStatus: StepTargetTaskRunStatusType
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    clientToken: Optional[str] = None


class UpdateTaskRequestTypeDef(BaseValidatorModel):
    targetRunStatus: TaskTargetRunStatusType
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    taskId: str
    clientToken: Optional[str] = None


class WorkerAmountCapabilityTypeDef(BaseValidatorModel):
    name: str
    value: float


class WorkerAttributeCapabilityTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]


class AcceleratorCountRangeTypeDef(BaseValidatorModel):
    pass


class AcceleratorCapabilitiesOutputTypeDef(BaseValidatorModel):
    selections: List[AcceleratorSelectionTypeDef]
    count: Optional[AcceleratorCountRangeTypeDef] = None


class AcceleratorCapabilitiesTypeDef(BaseValidatorModel):
    selections: Sequence[AcceleratorSelectionTypeDef]
    count: Optional[AcceleratorCountRangeTypeDef] = None


class TaskParameterValueTypeDef(BaseValidatorModel):
    pass


class AssignedTaskRunSessionActionDefinitionTypeDef(BaseValidatorModel):
    taskId: str
    stepId: str
    parameters: Dict[str, TaskParameterValueTypeDef]


class TaskRunSessionActionDefinitionTypeDef(BaseValidatorModel):
    taskId: str
    stepId: str
    parameters: Dict[str, TaskParameterValueTypeDef]


class TaskSearchSummaryTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    stepId: Optional[str] = None
    jobId: Optional[str] = None
    queueId: Optional[str] = None
    runStatus: Optional[TaskRunStatusType] = None
    targetRunStatus: Optional[TaskTargetRunStatusType] = None
    parameters: Optional[Dict[str, TaskParameterValueTypeDef]] = None
    failureRetryCount: Optional[int] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None


class TaskSummaryTypeDef(BaseValidatorModel):
    taskId: str
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    targetRunStatus: Optional[TaskTargetRunStatusType] = None
    failureRetryCount: Optional[int] = None
    parameters: Optional[Dict[str, TaskParameterValueTypeDef]] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    latestSessionActionId: Optional[str] = None


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


class CreateLimitResponseTypeDef(BaseValidatorModel):
    limitId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMonitorResponseTypeDef(BaseValidatorModel):
    monitorId: str
    identityCenterApplicationArn: str
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
    farmId: str
    displayName: str
    description: str
    kmsKeyArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetLicenseEndpointResponseTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    status: LicenseEndpointStatusType
    statusMessage: str
    vpcId: str
    dnsName: str
    subnetIds: List[str]
    securityGroupIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetLimitResponseTypeDef(BaseValidatorModel):
    displayName: str
    amountRequirementName: str
    maxCount: int
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    farmId: str
    limitId: str
    currentCount: int
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMonitorResponseTypeDef(BaseValidatorModel):
    monitorId: str
    displayName: str
    subdomain: str
    url: str
    roleArn: str
    identityCenterInstanceArn: str
    identityCenterApplicationArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueueEnvironmentResponseTypeDef(BaseValidatorModel):
    queueEnvironmentId: str
    name: str
    priority: int
    templateType: EnvironmentTemplateTypeType
    template: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueueFleetAssociationResponseTypeDef(BaseValidatorModel):
    queueId: str
    fleetId: str
    status: QueueFleetAssociationStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueueLimitAssociationResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    queueId: str
    limitId: str
    status: QueueLimitAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    targetRunStatus: TaskTargetRunStatusType
    failureRetryCount: int
    parameters: Dict[str, TaskParameterValueTypeDef]
    startedAt: datetime
    endedAt: datetime
    updatedAt: datetime
    updatedBy: str
    latestSessionActionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobParameterDefinitionsResponseTypeDef(BaseValidatorModel):
    jobParameterDefinitions: List[Dict[str, Any]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartSessionsStatisticsAggregationResponseTypeDef(BaseValidatorModel):
    aggregationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWorkerResponseTypeDef(BaseValidatorModel):
    log: LogConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AttachmentsOutputTypeDef(BaseValidatorModel):
    manifests: List[ManifestPropertiesOutputTypeDef]
    fileSystem: Optional[JobAttachmentsFileSystemType] = None


class AttachmentsTypeDef(BaseValidatorModel):
    manifests: Sequence[ManifestPropertiesTypeDef]
    fileSystem: Optional[JobAttachmentsFileSystemType] = None


class BudgetScheduleOutputTypeDef(BaseValidatorModel):
    fixed: Optional[FixedBudgetScheduleOutputTypeDef] = None


class BudgetSummaryTypeDef(BaseValidatorModel):
    budgetId: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    status: BudgetStatusType
    displayName: str
    approximateDollarLimit: float
    usages: ConsumedUsagesTypeDef
    createdBy: str
    createdAt: datetime
    description: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedAt: Optional[datetime] = None


class CopyJobTemplateRequestTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    targetS3Location: S3LocationTypeDef


class JobParameterTypeDef(BaseValidatorModel):
    pass


class JobSearchSummaryTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    queueId: Optional[str] = None
    name: Optional[str] = None
    lifecycleStatus: Optional[JobLifecycleStatusType] = None
    lifecycleStatusMessage: Optional[str] = None
    taskRunStatus: Optional[TaskRunStatusType] = None
    targetTaskRunStatus: Optional[JobTargetTaskRunStatusType] = None
    taskRunStatusCounts: Optional[Dict[TaskRunStatusType, int]] = None
    priority: Optional[int] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    createdBy: Optional[str] = None
    createdAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    jobParameters: Optional[Dict[str, JobParameterTypeDef]] = None
    maxWorkerCount: Optional[int] = None
    sourceJobId: Optional[str] = None


class FileSystemLocationTypeDef(BaseValidatorModel):
    pass


class CreateStorageProfileRequestTypeDef(BaseValidatorModel):
    farmId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    clientToken: Optional[str] = None
    fileSystemLocations: Optional[Sequence[FileSystemLocationTypeDef]] = None


class GetStorageProfileForQueueResponseTypeDef(BaseValidatorModel):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    fileSystemLocations: List[FileSystemLocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetStorageProfileResponseTypeDef(BaseValidatorModel):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    fileSystemLocations: List[FileSystemLocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateStorageProfileRequestTypeDef(BaseValidatorModel):
    farmId: str
    storageProfileId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    osFamily: Optional[StorageProfileOperatingSystemFamilyType] = None
    fileSystemLocationsToAdd: Optional[Sequence[FileSystemLocationTypeDef]] = None
    fileSystemLocationsToRemove: Optional[Sequence[FileSystemLocationTypeDef]] = None


class FleetAmountCapabilityTypeDef(BaseValidatorModel):
    pass


class FleetCapabilitiesTypeDef(BaseValidatorModel):
    amounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    attributes: Optional[List[FleetAttributeCapabilityOutputTypeDef]] = None


class MemoryMiBRangeTypeDef(BaseValidatorModel):
    pass


class VCpuCountRangeTypeDef(BaseValidatorModel):
    pass


class AcceleratorTotalMemoryMiBRangeTypeDef(BaseValidatorModel):
    pass


class CustomerManagedWorkerCapabilitiesOutputTypeDef(BaseValidatorModel):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    acceleratorTypes: Optional[List[Literal["gpu"]]] = None
    acceleratorCount: Optional[AcceleratorCountRangeTypeDef] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRangeTypeDef] = None
    customAmounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityOutputTypeDef]] = None


class CustomerManagedWorkerCapabilitiesTypeDef(BaseValidatorModel):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    acceleratorTypes: Optional[Sequence[Literal["gpu"]]] = None
    acceleratorCount: Optional[AcceleratorCountRangeTypeDef] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRangeTypeDef] = None
    customAmounts: Optional[Sequence[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapabilityTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class FixedBudgetScheduleTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef


class UpdatedSessionActionInfoTypeDef(BaseValidatorModel):
    completedStatus: Optional[CompletedStatusType] = None
    processExitCode: Optional[int] = None
    progressMessage: Optional[str] = None
    startedAt: Optional[TimestampTypeDef] = None
    endedAt: Optional[TimestampTypeDef] = None
    updatedAt: Optional[TimestampTypeDef] = None
    progressPercent: Optional[float] = None


class StepSummaryTypeDef(BaseValidatorModel):
    stepId: str
    name: str
    lifecycleStatus: StepLifecycleStatusType
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    createdAt: datetime
    createdBy: str
    lifecycleStatusMessage: Optional[str] = None
    targetTaskRunStatus: Optional[StepTargetTaskRunStatusType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    dependencyCounts: Optional[DependencyCountsTypeDef] = None


class ListFarmMembersResponseTypeDef(BaseValidatorModel):
    members: List[FarmMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFarmsResponseTypeDef(BaseValidatorModel):
    farms: List[FarmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFleetMembersResponseTypeDef(BaseValidatorModel):
    members: List[FleetMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetFleetRequestWaitTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetJobRequestWaitTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetLicenseEndpointRequestWaitExtraTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetLicenseEndpointRequestWaitTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetQueueFleetAssociationRequestWaitTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetQueueLimitAssociationRequestWaitTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetQueueRequestWaitExtraTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetQueueRequestWaitTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetJobEntityErrorTypeDef(BaseValidatorModel):
    jobDetails: Optional[JobDetailsErrorTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsErrorTypeDef] = None
    stepDetails: Optional[StepDetailsErrorTypeDef] = None
    environmentDetails: Optional[EnvironmentDetailsErrorTypeDef] = None


class GetSessionsStatisticsAggregationRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    aggregationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAvailableMeteredProductsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBudgetsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    status: Optional[BudgetStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFarmMembersRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFarmsRequestPaginateTypeDef(BaseValidatorModel):
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetMembersRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[FleetStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobMembersRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobParameterDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLicenseEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLimitsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMeteredProductsRequestPaginateTypeDef(BaseValidatorModel):
    licenseEndpointId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueueEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueueFleetAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    fleetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueueLimitAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    limitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueueMembersRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueuesRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSessionActionsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionId: Optional[str] = None
    taskId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSessionsForWorkerRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSessionsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStepConsumersRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStepDependenciesRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStepsRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStorageProfilesForQueueRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStorageProfilesRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTasksRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkersRequestPaginateTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class HostPropertiesResponseTypeDef(BaseValidatorModel):
    ipAddresses: Optional[IpAddressesOutputTypeDef] = None
    hostName: Optional[str] = None
    ec2InstanceArn: Optional[str] = None
    ec2InstanceType: Optional[str] = None


class JobEntityIdentifiersUnionTypeDef(BaseValidatorModel):
    jobDetails: Optional[JobDetailsIdentifiersTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsIdentifiersTypeDef] = None
    stepDetails: Optional[StepDetailsIdentifiersTypeDef] = None
    environmentDetails: Optional[EnvironmentDetailsIdentifiersTypeDef] = None


class ListJobMembersResponseTypeDef(BaseValidatorModel):
    members: List[JobMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobRunAsUserTypeDef(BaseValidatorModel):
    runAs: RunAsType
    posix: Optional[PosixUserTypeDef] = None
    windows: Optional[WindowsUserTypeDef] = None


class ListJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListLicenseEndpointsResponseTypeDef(BaseValidatorModel):
    licenseEndpoints: List[LicenseEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListLimitsResponseTypeDef(BaseValidatorModel):
    limits: List[LimitSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAvailableMeteredProductsResponseTypeDef(BaseValidatorModel):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMeteredProductsResponseTypeDef(BaseValidatorModel):
    meteredProducts: List[MeteredProductSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMonitorsResponseTypeDef(BaseValidatorModel):
    monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListQueueEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[QueueEnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListQueueFleetAssociationsResponseTypeDef(BaseValidatorModel):
    queueFleetAssociations: List[QueueFleetAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListQueueLimitAssociationsResponseTypeDef(BaseValidatorModel):
    queueLimitAssociations: List[QueueLimitAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListQueueMembersResponseTypeDef(BaseValidatorModel):
    members: List[QueueMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListQueuesResponseTypeDef(BaseValidatorModel):
    queues: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSessionsForWorkerResponseTypeDef(BaseValidatorModel):
    sessions: List[WorkerSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSessionsResponseTypeDef(BaseValidatorModel):
    sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStepConsumersResponseTypeDef(BaseValidatorModel):
    consumers: List[StepConsumerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStepDependenciesResponseTypeDef(BaseValidatorModel):
    dependencies: List[StepDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStorageProfilesForQueueResponseTypeDef(BaseValidatorModel):
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStorageProfilesResponseTypeDef(BaseValidatorModel):
    storageProfiles: List[StorageProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StepParameterTypeDef(BaseValidatorModel):
    pass


class ParameterSpaceTypeDef(BaseValidatorModel):
    parameters: List[StepParameterTypeDef]
    combination: Optional[str] = None


class SearchSortExpressionTypeDef(BaseValidatorModel):
    userJobsFirst: Optional[UserJobsFirstTypeDef] = None
    fieldSort: Optional[FieldSortExpressionTypeDef] = None
    parameterSort: Optional[ParameterSortExpressionTypeDef] = None


class SessionActionDefinitionSummaryTypeDef(BaseValidatorModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionSummaryTypeDef] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionSummaryTypeDef] = None
    taskRun: Optional[TaskRunSessionActionDefinitionSummaryTypeDef] = None
    syncInputJobAttachments: Optional[ SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef ] = None


class StartSessionsStatisticsAggregationRequestTypeDef(BaseValidatorModel):
    farmId: str
    resourceIds: SessionsStatisticsResourcesTypeDef
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    groupBy: Sequence[UsageGroupByFieldType]
    statistics: Sequence[UsageStatisticType]
    timezone: Optional[str] = None
    period: Optional[PeriodType] = None


class StatsTypeDef(BaseValidatorModel):
    pass


class StatisticsTypeDef(BaseValidatorModel):
    count: int
    costInUsd: StatsTypeDef
    runtimeInSeconds: StatsTypeDef
    queueId: Optional[str] = None
    fleetId: Optional[str] = None
    jobId: Optional[str] = None
    jobName: Optional[str] = None
    userId: Optional[str] = None
    usageType: Optional[UsageTypeType] = None
    licenseProduct: Optional[str] = None
    instanceType: Optional[str] = None
    aggregationStartTime: Optional[datetime] = None
    aggregationEndTime: Optional[datetime] = None


class StepAmountCapabilityTypeDef(BaseValidatorModel):
    pass


class StepRequiredCapabilitiesTypeDef(BaseValidatorModel):
    attributes: List[StepAttributeCapabilityTypeDef]
    amounts: List[StepAmountCapabilityTypeDef]


class WorkerCapabilitiesTypeDef(BaseValidatorModel):
    amounts: Sequence[WorkerAmountCapabilityTypeDef]
    attributes: Sequence[WorkerAttributeCapabilityTypeDef]


class ServiceManagedEc2InstanceCapabilitiesOutputTypeDef(BaseValidatorModel):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    rootEbsVolume: Optional[Ec2EbsVolumeTypeDef] = None
    acceleratorCapabilities: Optional[AcceleratorCapabilitiesOutputTypeDef] = None
    allowedInstanceTypes: Optional[List[str]] = None
    excludedInstanceTypes: Optional[List[str]] = None
    customAmounts: Optional[List[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityOutputTypeDef]] = None


class ServiceManagedEc2InstanceCapabilitiesTypeDef(BaseValidatorModel):
    vCpuCount: VCpuCountRangeTypeDef
    memoryMiB: MemoryMiBRangeTypeDef
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    rootEbsVolume: Optional[Ec2EbsVolumeTypeDef] = None
    acceleratorCapabilities: Optional[AcceleratorCapabilitiesTypeDef] = None
    allowedInstanceTypes: Optional[Sequence[str]] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    customAmounts: Optional[Sequence[FleetAmountCapabilityTypeDef]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapabilityTypeDef]] = None


class AssignedSessionActionDefinitionTypeDef(BaseValidatorModel):
    envEnter: Optional[AssignedEnvironmentEnterSessionActionDefinitionTypeDef] = None
    envExit: Optional[AssignedEnvironmentExitSessionActionDefinitionTypeDef] = None
    taskRun: Optional[AssignedTaskRunSessionActionDefinitionTypeDef] = None
    syncInputJobAttachments: Optional[ AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef ] = None


class SessionActionDefinitionTypeDef(BaseValidatorModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionTypeDef] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionTypeDef] = None
    taskRun: Optional[TaskRunSessionActionDefinitionTypeDef] = None
    syncInputJobAttachments: Optional[SyncInputJobAttachmentsSessionActionDefinitionTypeDef] = None


class SearchTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[TaskSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[TaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    name: str
    lifecycleStatus: JobLifecycleStatusType
    lifecycleStatusMessage: str
    priority: int
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    startedAt: datetime
    endedAt: datetime
    taskRunStatus: TaskRunStatusType
    targetTaskRunStatus: JobTargetTaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    storageProfileId: str
    maxFailedTasksCount: int
    maxRetriesPerTask: int
    parameters: Dict[str, JobParameterTypeDef]
    attachments: AttachmentsOutputTypeDef
    description: str
    maxWorkerCount: int
    sourceJobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class JobAttachmentDetailsEntityTypeDef(BaseValidatorModel):
    jobId: str
    attachments: AttachmentsOutputTypeDef


class ResponseBudgetActionTypeDef(BaseValidatorModel):
    pass


class GetBudgetResponseTypeDef(BaseValidatorModel):
    budgetId: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    status: BudgetStatusType
    displayName: str
    description: str
    approximateDollarLimit: float
    usages: ConsumedUsagesTypeDef
    actions: List[ResponseBudgetActionTypeDef]
    schedule: BudgetScheduleOutputTypeDef
    createdBy: str
    createdAt: datetime
    updatedBy: str
    updatedAt: datetime
    queueStoppedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListBudgetsResponseTypeDef(BaseValidatorModel):
    budgets: List[BudgetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef


class CustomerManagedFleetConfigurationOutputTypeDef(BaseValidatorModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesOutputTypeDef
    storageProfileId: Optional[str] = None


class CustomerManagedFleetConfigurationTypeDef(BaseValidatorModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesTypeDef
    storageProfileId: Optional[str] = None


class DateTimeFilterExpressionTypeDef(BaseValidatorModel):
    pass


class StringFilterExpressionTypeDef(BaseValidatorModel):
    pass


class ParameterFilterExpressionTypeDef(BaseValidatorModel):
    pass


class SearchFilterExpressionTypeDef(BaseValidatorModel):
    dateTimeFilter: Optional[DateTimeFilterExpressionTypeDef] = None
    parameterFilter: Optional[ParameterFilterExpressionTypeDef] = None
    searchTermFilter: Optional[SearchTermFilterExpressionTypeDef] = None
    stringFilter: Optional[StringFilterExpressionTypeDef] = None
    groupFilter: Optional[Mapping[str, Any]] = None


class BudgetScheduleTypeDef(BaseValidatorModel):
    fixed: Optional[FixedBudgetScheduleTypeDef] = None


class UpdateWorkerScheduleRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    updatedSessionActions: Optional[Mapping[str, UpdatedSessionActionInfoTypeDef]] = None


class ListStepsResponseTypeDef(BaseValidatorModel):
    steps: List[StepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetSessionResponseTypeDef(BaseValidatorModel):
    sessionId: str
    fleetId: str
    workerId: str
    startedAt: datetime
    log: LogConfigurationTypeDef
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: datetime
    updatedAt: datetime
    updatedBy: str
    targetLifecycleStatus: Literal["ENDED"]
    hostProperties: HostPropertiesResponseTypeDef
    workerLog: LogConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkerResponseTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    hostProperties: HostPropertiesResponseTypeDef
    status: WorkerStatusType
    log: LogConfigurationTypeDef
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class WorkerSearchSummaryTypeDef(BaseValidatorModel):
    fleetId: Optional[str] = None
    workerId: Optional[str] = None
    status: Optional[WorkerStatusType] = None
    hostProperties: Optional[HostPropertiesResponseTypeDef] = None
    createdBy: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    updatedAt: Optional[datetime] = None


class WorkerSummaryTypeDef(BaseValidatorModel):
    workerId: str
    farmId: str
    fleetId: str
    status: WorkerStatusType
    createdAt: datetime
    createdBy: str
    hostProperties: Optional[HostPropertiesResponseTypeDef] = None
    log: Optional[LogConfigurationTypeDef] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class IpAddressesUnionTypeDef(BaseValidatorModel):
    pass


class HostPropertiesRequestTypeDef(BaseValidatorModel):
    ipAddresses: Optional[IpAddressesUnionTypeDef] = None
    hostName: Optional[str] = None


class BatchGetJobEntityRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    identifiers: Sequence[JobEntityIdentifiersUnionTypeDef]


class CreateQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    displayName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    defaultBudgetAction: Optional[DefaultQueueBudgetActionType] = None
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    roleArn: Optional[str] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    requiredFileSystemLocationNames: Optional[Sequence[str]] = None
    allowedStorageProfileIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class GetQueueResponseTypeDef(BaseValidatorModel):
    queueId: str
    displayName: str
    description: str
    farmId: str
    status: QueueStatusType
    defaultBudgetAction: DefaultQueueBudgetActionType
    blockedReason: QueueBlockedReasonType
    jobAttachmentSettings: JobAttachmentSettingsTypeDef
    roleArn: str
    requiredFileSystemLocationNames: List[str]
    allowedStorageProfileIds: List[str]
    jobRunAsUser: JobRunAsUserTypeDef
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class JobDetailsEntityTypeDef(BaseValidatorModel):
    jobId: str
    logGroupName: str
    schemaVersion: str
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    queueRoleArn: Optional[str] = None
    parameters: Optional[Dict[str, JobParameterTypeDef]] = None
    pathMappingRules: Optional[List[PathMappingRuleTypeDef]] = None


class UpdateQueueRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    defaultBudgetAction: Optional[DefaultQueueBudgetActionType] = None
    jobAttachmentSettings: Optional[JobAttachmentSettingsTypeDef] = None
    roleArn: Optional[str] = None
    jobRunAsUser: Optional[JobRunAsUserTypeDef] = None
    requiredFileSystemLocationNamesToAdd: Optional[Sequence[str]] = None
    requiredFileSystemLocationNamesToRemove: Optional[Sequence[str]] = None
    allowedStorageProfileIdsToAdd: Optional[Sequence[str]] = None
    allowedStorageProfileIdsToRemove: Optional[Sequence[str]] = None


class StepSearchSummaryTypeDef(BaseValidatorModel):
    stepId: Optional[str] = None
    jobId: Optional[str] = None
    queueId: Optional[str] = None
    name: Optional[str] = None
    lifecycleStatus: Optional[StepLifecycleStatusType] = None
    lifecycleStatusMessage: Optional[str] = None
    taskRunStatus: Optional[TaskRunStatusType] = None
    targetTaskRunStatus: Optional[StepTargetTaskRunStatusType] = None
    taskRunStatusCounts: Optional[Dict[TaskRunStatusType, int]] = None
    createdAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    parameterSpace: Optional[ParameterSpaceTypeDef] = None


class SessionActionSummaryTypeDef(BaseValidatorModel):
    sessionActionId: str
    status: SessionActionStatusType
    definition: SessionActionDefinitionSummaryTypeDef
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    workerUpdatedAt: Optional[datetime] = None
    progressPercent: Optional[float] = None


class GetSessionsStatisticsAggregationResponseTypeDef(BaseValidatorModel):
    statistics: List[StatisticsTypeDef]
    status: SessionsStatisticsAggregationStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetStepResponseTypeDef(BaseValidatorModel):
    stepId: str
    name: str
    lifecycleStatus: StepLifecycleStatusType
    lifecycleStatusMessage: str
    taskRunStatus: TaskRunStatusType
    taskRunStatusCounts: Dict[TaskRunStatusType, int]
    targetTaskRunStatus: StepTargetTaskRunStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    startedAt: datetime
    endedAt: datetime
    dependencyCounts: DependencyCountsTypeDef
    requiredCapabilities: StepRequiredCapabilitiesTypeDef
    parameterSpace: ParameterSpaceTypeDef
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceManagedEc2InstanceMarketOptionsTypeDef(BaseValidatorModel):
    pass


class ServiceManagedEc2FleetConfigurationOutputTypeDef(BaseValidatorModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesOutputTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef


class ServiceManagedEc2FleetConfigurationTypeDef(BaseValidatorModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesTypeDef
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptionsTypeDef


class AssignedSessionActionTypeDef(BaseValidatorModel):
    sessionActionId: str
    definition: AssignedSessionActionDefinitionTypeDef


class GetSessionActionResponseTypeDef(BaseValidatorModel):
    sessionActionId: str
    status: SessionActionStatusType
    startedAt: datetime
    endedAt: datetime
    workerUpdatedAt: datetime
    progressPercent: float
    sessionId: str
    processExitCode: int
    progressMessage: str
    definition: SessionActionDefinitionTypeDef
    acquiredLimits: List[AcquiredLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AttachmentsUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueId: str
    priority: int
    clientToken: Optional[str] = None
    template: Optional[str] = None
    templateType: Optional[JobTemplateTypeType] = None
    parameters: Optional[Mapping[str, JobParameterTypeDef]] = None
    attachments: Optional[AttachmentsUnionTypeDef] = None
    storageProfileId: Optional[str] = None
    targetTaskRunStatus: Optional[CreateJobTargetTaskRunStatusType] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    maxWorkerCount: Optional[int] = None
    sourceJobId: Optional[str] = None


class SearchWorkersResponseTypeDef(BaseValidatorModel):
    workers: List[WorkerSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListWorkersResponseTypeDef(BaseValidatorModel):
    workers: List[WorkerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    hostProperties: Optional[HostPropertiesRequestTypeDef] = None
    clientToken: Optional[str] = None


class UpdateWorkerRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    status: Optional[UpdatedWorkerStatusType] = None
    capabilities: Optional[WorkerCapabilitiesTypeDef] = None
    hostProperties: Optional[HostPropertiesRequestTypeDef] = None


class JobEntityTypeDef(BaseValidatorModel):
    jobDetails: Optional[JobDetailsEntityTypeDef] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsEntityTypeDef] = None
    stepDetails: Optional[StepDetailsEntityTypeDef] = None
    environmentDetails: Optional[EnvironmentDetailsEntityTypeDef] = None


class SearchStepsResponseTypeDef(BaseValidatorModel):
    steps: List[StepSearchSummaryTypeDef]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListSessionActionsResponseTypeDef(BaseValidatorModel):
    sessionActions: List[SessionActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FleetConfigurationOutputTypeDef(BaseValidatorModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationOutputTypeDef] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationOutputTypeDef] = None


class FleetConfigurationTypeDef(BaseValidatorModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationTypeDef] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationTypeDef] = None


class AssignedSessionTypeDef(BaseValidatorModel):
    queueId: str
    jobId: str
    sessionActions: List[AssignedSessionActionTypeDef]
    logConfiguration: LogConfigurationTypeDef


class SearchGroupedFilterExpressionsTypeDef(BaseValidatorModel):
    pass


class SearchJobsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    filterExpressions: Optional[SearchGroupedFilterExpressionsTypeDef] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None
    pageSize: Optional[int] = None


class SearchStepsRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    jobId: Optional[str] = None
    filterExpressions: Optional[SearchGroupedFilterExpressionsTypeDef] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None
    pageSize: Optional[int] = None


class SearchTasksRequestTypeDef(BaseValidatorModel):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    jobId: Optional[str] = None
    filterExpressions: Optional[SearchGroupedFilterExpressionsTypeDef] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None
    pageSize: Optional[int] = None


class SearchWorkersRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetIds: Sequence[str]
    itemOffset: int
    filterExpressions: Optional[SearchGroupedFilterExpressionsTypeDef] = None
    sortExpressions: Optional[Sequence[SearchSortExpressionTypeDef]] = None
    pageSize: Optional[int] = None


class BudgetScheduleUnionTypeDef(BaseValidatorModel):
    pass


class BudgetActionToAddTypeDef(BaseValidatorModel):
    pass


class CreateBudgetRequestTypeDef(BaseValidatorModel):
    farmId: str
    usageTrackingResource: UsageTrackingResourceTypeDef
    displayName: str
    approximateDollarLimit: float
    actions: Sequence[BudgetActionToAddTypeDef]
    schedule: BudgetScheduleUnionTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None


class BudgetActionToRemoveTypeDef(BaseValidatorModel):
    pass


class UpdateBudgetRequestTypeDef(BaseValidatorModel):
    farmId: str
    budgetId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    status: Optional[BudgetStatusType] = None
    approximateDollarLimit: Optional[float] = None
    actionsToAdd: Optional[Sequence[BudgetActionToAddTypeDef]] = None
    actionsToRemove: Optional[Sequence[BudgetActionToRemoveTypeDef]] = None
    schedule: Optional[BudgetScheduleUnionTypeDef] = None


class BatchGetJobEntityResponseTypeDef(BaseValidatorModel):
    entities: List[JobEntityTypeDef]
    errors: List[GetJobEntityErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FleetSummaryTypeDef(BaseValidatorModel):
    fleetId: str
    farmId: str
    displayName: str
    status: FleetStatusType
    workerCount: int
    minWorkerCount: int
    maxWorkerCount: int
    configuration: FleetConfigurationOutputTypeDef
    createdAt: datetime
    createdBy: str
    autoScalingStatus: Optional[AutoScalingStatusType] = None
    targetWorkerCount: Optional[int] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class GetFleetResponseTypeDef(BaseValidatorModel):
    fleetId: str
    farmId: str
    displayName: str
    description: str
    status: FleetStatusType
    autoScalingStatus: AutoScalingStatusType
    targetWorkerCount: int
    workerCount: int
    minWorkerCount: int
    maxWorkerCount: int
    configuration: FleetConfigurationOutputTypeDef
    capabilities: FleetCapabilitiesTypeDef
    roleArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWorkerScheduleResponseTypeDef(BaseValidatorModel):
    assignedSessions: Dict[str, AssignedSessionTypeDef]
    cancelSessionActions: Dict[str, List[str]]
    desiredWorkerStatus: Literal["STOPPED"]
    updateIntervalSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListFleetsResponseTypeDef(BaseValidatorModel):
    fleets: List[FleetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FleetConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateFleetRequestTypeDef(BaseValidatorModel):
    farmId: str
    displayName: str
    roleArn: str
    maxWorkerCount: int
    configuration: FleetConfigurationUnionTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None
    minWorkerCount: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFleetRequestTypeDef(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    roleArn: Optional[str] = None
    minWorkerCount: Optional[int] = None
    maxWorkerCount: Optional[int] = None
    configuration: Optional[FleetConfigurationUnionTypeDef] = None


