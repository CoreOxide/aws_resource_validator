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

class AcceleratorSelection(BaseValidatorModel):
    name: AcceleratorNameType
    runtime: Optional[str] = None


class AcquiredLimit(BaseValidatorModel):
    limitId: str
    count: int


class AssignedEnvironmentEnterSessionActionDefinition(BaseValidatorModel):
    environmentId: str


class AssignedEnvironmentExitSessionActionDefinition(BaseValidatorModel):
    environmentId: str


class AssignedSyncInputJobAttachmentsSessionActionDefinition(BaseValidatorModel):
    stepId: Optional[str] = None


class LogConfiguration(BaseValidatorModel):
    logDriver: str
    options: Optional[Dict[str, str]] = None
    parameters: Optional[Dict[str, str]] = None
    error: Optional[str] = None


class AssociateMemberToFarmRequest(BaseValidatorModel):
    farmId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssociateMemberToFleetRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssociateMemberToJobRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssociateMemberToQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class AssumeFleetRoleForReadRequest(BaseValidatorModel):
    farmId: str
    fleetId: str


class AwsCredentials(BaseValidatorModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str
    expiration: datetime


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssumeFleetRoleForWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str


class AssumeQueueRoleForReadRequest(BaseValidatorModel):
    farmId: str
    queueId: str


class AssumeQueueRoleForUserRequest(BaseValidatorModel):
    farmId: str
    queueId: str


class AssumeQueueRoleForWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    queueId: str


class ManifestPropertiesOutput(BaseValidatorModel):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: Optional[str] = None
    outputRelativeDirectories: Optional[List[str]] = None
    inputManifestPath: Optional[str] = None
    inputManifestHash: Optional[str] = None


class ManifestProperties(BaseValidatorModel):
    rootPath: str
    rootPathFormat: PathFormatType
    fileSystemLocationName: Optional[str] = None
    outputRelativeDirectories: Optional[Sequence[str]] = None
    inputManifestPath: Optional[str] = None
    inputManifestHash: Optional[str] = None


class FixedBudgetScheduleOutput(BaseValidatorModel):
    startTime: datetime
    endTime: datetime


class ConsumedUsages(BaseValidatorModel):
    approximateDollarUsage: float


class UsageTrackingResource(BaseValidatorModel):
    queueId: Optional[str] = None


class S3Location(BaseValidatorModel):
    bucketName: str
    key: str


class CreateFarmRequest(BaseValidatorModel):
    displayName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateLicenseEndpointRequest(BaseValidatorModel):
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateLimitRequest(BaseValidatorModel):
    displayName: str
    amountRequirementName: str
    maxCount: int
    farmId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class CreateMonitorRequest(BaseValidatorModel):
    displayName: str
    identityCenterInstanceArn: str
    subdomain: str
    roleArn: str
    clientToken: Optional[str] = None


class CreateQueueEnvironmentRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    priority: int
    templateType: EnvironmentTemplateTypeType
    template: str
    clientToken: Optional[str] = None


class CreateQueueFleetAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str


class CreateQueueLimitAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str


class JobAttachmentSettings(BaseValidatorModel):
    s3BucketName: str
    rootPrefix: str


class FleetAttributeCapabilityOutput(BaseValidatorModel):
    name: str
    values: List[str]


class FleetAttributeCapability(BaseValidatorModel):
    name: str
    values: Sequence[str]


class DeleteBudgetRequest(BaseValidatorModel):
    farmId: str
    budgetId: str


class DeleteFarmRequest(BaseValidatorModel):
    farmId: str


class DeleteFleetRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None


class DeleteLicenseEndpointRequest(BaseValidatorModel):
    licenseEndpointId: str


class DeleteLimitRequest(BaseValidatorModel):
    farmId: str
    limitId: str


class DeleteMeteredProductRequest(BaseValidatorModel):
    licenseEndpointId: str
    productId: str


class DeleteMonitorRequest(BaseValidatorModel):
    monitorId: str


class DeleteQueueEnvironmentRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    queueEnvironmentId: str


class DeleteQueueFleetAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str


class DeleteQueueLimitAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str


class DeleteQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str


class DeleteStorageProfileRequest(BaseValidatorModel):
    farmId: str
    storageProfileId: str


class DeleteWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str


class DependencyCounts(BaseValidatorModel):
    dependenciesResolved: int
    dependenciesUnresolved: int
    consumersResolved: int
    consumersUnresolved: int


class DisassociateMemberFromFarmRequest(BaseValidatorModel):
    farmId: str
    principalId: str


class DisassociateMemberFromFleetRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str


class DisassociateMemberFromJobRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    principalId: str


class DisassociateMemberFromQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: str


class Ec2EbsVolume(BaseValidatorModel):
    sizeGiB: Optional[int] = None
    iops: Optional[int] = None
    throughputMiB: Optional[int] = None


class EnvironmentDetailsEntity(BaseValidatorModel):
    jobId: str
    environmentId: str
    schemaVersion: str
    template: Dict[str, Any]


class EnvironmentDetailsError(BaseValidatorModel):
    jobId: str
    environmentId: str
    code: JobEntityErrorCodeType
    message: str


class EnvironmentDetailsIdentifiers(BaseValidatorModel):
    jobId: str
    environmentId: str


class EnvironmentEnterSessionActionDefinitionSummary(BaseValidatorModel):
    environmentId: str


class EnvironmentEnterSessionActionDefinition(BaseValidatorModel):
    environmentId: str


class EnvironmentExitSessionActionDefinitionSummary(BaseValidatorModel):
    environmentId: str


class EnvironmentExitSessionActionDefinition(BaseValidatorModel):
    environmentId: str


class FarmMember(BaseValidatorModel):
    farmId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class FarmSummary(BaseValidatorModel):
    farmId: str
    displayName: str
    createdAt: datetime
    createdBy: str
    kmsKeyArn: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class FieldSortExpression(BaseValidatorModel):
    sortOrder: SortOrderType
    name: str


class FleetMember(BaseValidatorModel):
    farmId: str
    fleetId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class GetBudgetRequest(BaseValidatorModel):
    farmId: str
    budgetId: str


class GetFarmRequest(BaseValidatorModel):
    farmId: str


class GetFleetRequest(BaseValidatorModel):
    farmId: str
    fleetId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class JobAttachmentDetailsError(BaseValidatorModel):
    jobId: str
    code: JobEntityErrorCodeType
    message: str


class JobDetailsError(BaseValidatorModel):
    jobId: str
    code: JobEntityErrorCodeType
    message: str


class StepDetailsError(BaseValidatorModel):
    jobId: str
    stepId: str
    code: JobEntityErrorCodeType
    message: str


class GetJobRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str


class GetLicenseEndpointRequest(BaseValidatorModel):
    licenseEndpointId: str


class GetLimitRequest(BaseValidatorModel):
    farmId: str
    limitId: str


class GetMonitorRequest(BaseValidatorModel):
    monitorId: str


class GetQueueEnvironmentRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    queueEnvironmentId: str


class GetQueueFleetAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str


class GetQueueLimitAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str


class GetQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str


class GetSessionActionRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionActionId: str


class GetSessionRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetSessionsStatisticsAggregationRequest(BaseValidatorModel):
    farmId: str
    aggregationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetStepRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str


class GetStorageProfileForQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    storageProfileId: str


class GetStorageProfileRequest(BaseValidatorModel):
    farmId: str
    storageProfileId: str


class GetTaskRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    taskId: str


class GetWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str


class IpAddressesOutput(BaseValidatorModel):
    ipV4Addresses: Optional[List[str]] = None
    ipV6Addresses: Optional[List[str]] = None


class IpAddresses(BaseValidatorModel):
    ipV4Addresses: Optional[Sequence[str]] = None
    ipV6Addresses: Optional[Sequence[str]] = None


class JobAttachmentDetailsIdentifiers(BaseValidatorModel):
    jobId: str


class PathMappingRule(BaseValidatorModel):
    sourcePathFormat: PathFormatType
    sourcePath: str
    destinationPath: str


class JobDetailsIdentifiers(BaseValidatorModel):
    jobId: str


class StepDetailsIdentifiers(BaseValidatorModel):
    jobId: str
    stepId: str


class StepDetailsEntity(BaseValidatorModel):
    jobId: str
    stepId: str
    schemaVersion: str
    template: Dict[str, Any]
    dependencies: List[str]


class JobMember(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class PosixUser(BaseValidatorModel):
    user: str
    group: str


class WindowsUser(BaseValidatorModel):
    user: str
    passwordArn: str


class JobSummary(BaseValidatorModel):
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


class LicenseEndpointSummary(BaseValidatorModel):
    licenseEndpointId: Optional[str] = None
    status: Optional[LicenseEndpointStatusType] = None
    statusMessage: Optional[str] = None
    vpcId: Optional[str] = None


class LimitSummary(BaseValidatorModel):
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


class ListAvailableMeteredProductsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MeteredProductSummary(BaseValidatorModel):
    productId: str
    family: str
    vendor: str
    port: int


class ListBudgetsRequest(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[BudgetStatusType] = None


class ListFarmMembersRequest(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFarmsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    maxResults: Optional[int] = None


class ListFleetMembersRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFleetsRequest(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[FleetStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobMembersRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobParameterDefinitionsRequest(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobsRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListLicenseEndpointsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListLimitsRequest(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMeteredProductsRequest(BaseValidatorModel):
    licenseEndpointId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMonitorsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MonitorSummary(BaseValidatorModel):
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


class ListQueueEnvironmentsRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueEnvironmentSummary(BaseValidatorModel):
    queueEnvironmentId: str
    name: str
    priority: int


class ListQueueFleetAssociationsRequest(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    fleetId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueFleetAssociationSummary(BaseValidatorModel):
    queueId: str
    fleetId: str
    status: QueueFleetAssociationStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListQueueLimitAssociationsRequest(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    limitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueLimitAssociationSummary(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    queueId: str
    limitId: str
    status: QueueLimitAssociationStatusType
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class ListQueueMembersRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueMember(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: str
    principalType: PrincipalTypeType
    identityStoreId: str
    membershipLevel: MembershipLevelType


class ListQueuesRequest(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueSummary(BaseValidatorModel):
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


class ListSessionActionsRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionId: Optional[str] = None
    taskId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSessionsForWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkerSessionSummary(BaseValidatorModel):
    sessionId: str
    queueId: str
    jobId: str
    startedAt: datetime
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: Optional[datetime] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None


class ListSessionsRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SessionSummary(BaseValidatorModel):
    sessionId: str
    fleetId: str
    workerId: str
    startedAt: datetime
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    targetLifecycleStatus: Optional[Literal["ENDED"]] = None


class ListStepConsumersRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StepConsumer(BaseValidatorModel):
    stepId: str
    status: DependencyConsumerResolutionStatusType


class ListStepDependenciesRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StepDependency(BaseValidatorModel):
    stepId: str
    status: DependencyConsumerResolutionStatusType


class ListStepsRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListStorageProfilesForQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StorageProfileSummary(BaseValidatorModel):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType


class ListStorageProfilesRequest(BaseValidatorModel):
    farmId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTasksRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWorkersRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ParameterSortExpression(BaseValidatorModel):
    sortOrder: SortOrderType
    name: str


class PutMeteredProductRequest(BaseValidatorModel):
    licenseEndpointId: str
    productId: str


class SearchTermFilterExpression(BaseValidatorModel):
    searchTerm: str


class UserJobsFirst(BaseValidatorModel):
    userIdentityId: str


class SyncInputJobAttachmentsSessionActionDefinitionSummary(BaseValidatorModel):
    stepId: Optional[str] = None


class TaskRunSessionActionDefinitionSummary(BaseValidatorModel):
    taskId: str
    stepId: str


class SyncInputJobAttachmentsSessionActionDefinition(BaseValidatorModel):
    stepId: Optional[str] = None


class SessionsStatisticsResources(BaseValidatorModel):
    queueIds: Optional[Sequence[str]] = None
    fleetIds: Optional[Sequence[str]] = None


class StepAttributeCapability(BaseValidatorModel):
    name: str
    anyOf: Optional[List[str]] = None
    allOf: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateFarmRequest(BaseValidatorModel):
    farmId: str
    displayName: Optional[str] = None
    description: Optional[str] = None


class UpdateJobRequest(BaseValidatorModel):
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


class UpdateLimitRequest(BaseValidatorModel):
    farmId: str
    limitId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    maxCount: Optional[int] = None


class UpdateMonitorRequest(BaseValidatorModel):
    monitorId: str
    subdomain: Optional[str] = None
    displayName: Optional[str] = None
    roleArn: Optional[str] = None


class UpdateQueueEnvironmentRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    queueEnvironmentId: str
    clientToken: Optional[str] = None
    priority: Optional[int] = None
    templateType: Optional[EnvironmentTemplateTypeType] = None
    template: Optional[str] = None


class UpdateQueueFleetAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str
    status: UpdateQueueFleetAssociationStatusType


class UpdateQueueLimitAssociationRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str
    status: UpdateQueueLimitAssociationStatusType


class UpdateSessionRequest(BaseValidatorModel):
    targetLifecycleStatus: Literal["ENDED"]
    farmId: str
    queueId: str
    jobId: str
    sessionId: str
    clientToken: Optional[str] = None


class UpdateStepRequest(BaseValidatorModel):
    targetTaskRunStatus: StepTargetTaskRunStatusType
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    clientToken: Optional[str] = None


class UpdateTaskRequest(BaseValidatorModel):
    targetRunStatus: TaskTargetRunStatusType
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    taskId: str
    clientToken: Optional[str] = None


class WorkerAmountCapability(BaseValidatorModel):
    name: str
    value: float


class WorkerAttributeCapability(BaseValidatorModel):
    name: str
    values: Sequence[str]


class AcceleratorCountRange(BaseValidatorModel):
    pass


class AcceleratorCapabilitiesOutput(BaseValidatorModel):
    selections: List[AcceleratorSelection]
    count: Optional[AcceleratorCountRange] = None


class AcceleratorCapabilities(BaseValidatorModel):
    selections: Sequence[AcceleratorSelection]
    count: Optional[AcceleratorCountRange] = None


class TaskParameterValue(BaseValidatorModel):
    pass


class AssignedTaskRunSessionActionDefinition(BaseValidatorModel):
    taskId: str
    stepId: str
    parameters: Dict[str, TaskParameterValue]


class TaskRunSessionActionDefinition(BaseValidatorModel):
    taskId: str
    stepId: str
    parameters: Dict[str, TaskParameterValue]


class TaskSearchSummary(BaseValidatorModel):
    taskId: Optional[str] = None
    stepId: Optional[str] = None
    jobId: Optional[str] = None
    queueId: Optional[str] = None
    runStatus: Optional[TaskRunStatusType] = None
    targetRunStatus: Optional[TaskTargetRunStatusType] = None
    parameters: Optional[Dict[str, TaskParameterValue]] = None
    failureRetryCount: Optional[int] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None


class TaskSummary(BaseValidatorModel):
    taskId: str
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    targetRunStatus: Optional[TaskTargetRunStatusType] = None
    failureRetryCount: Optional[int] = None
    parameters: Optional[Dict[str, TaskParameterValue]] = None
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    latestSessionActionId: Optional[str] = None


class AssumeFleetRoleForReadResponse(BaseValidatorModel):
    credentials: AwsCredentials
    ResponseMetadata: ResponseMetadata


class AssumeFleetRoleForWorkerResponse(BaseValidatorModel):
    credentials: AwsCredentials
    ResponseMetadata: ResponseMetadata


class AssumeQueueRoleForReadResponse(BaseValidatorModel):
    credentials: AwsCredentials
    ResponseMetadata: ResponseMetadata


class AssumeQueueRoleForUserResponse(BaseValidatorModel):
    credentials: AwsCredentials
    ResponseMetadata: ResponseMetadata


class AssumeQueueRoleForWorkerResponse(BaseValidatorModel):
    credentials: AwsCredentials
    ResponseMetadata: ResponseMetadata


class CopyJobTemplateResponse(BaseValidatorModel):
    templateType: JobTemplateTypeType
    ResponseMetadata: ResponseMetadata


class CreateBudgetResponse(BaseValidatorModel):
    budgetId: str
    ResponseMetadata: ResponseMetadata


class CreateFarmResponse(BaseValidatorModel):
    farmId: str
    ResponseMetadata: ResponseMetadata


class CreateFleetResponse(BaseValidatorModel):
    fleetId: str
    ResponseMetadata: ResponseMetadata


class CreateJobResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class CreateLicenseEndpointResponse(BaseValidatorModel):
    licenseEndpointId: str
    ResponseMetadata: ResponseMetadata


class CreateLimitResponse(BaseValidatorModel):
    limitId: str
    ResponseMetadata: ResponseMetadata


class CreateMonitorResponse(BaseValidatorModel):
    monitorId: str
    identityCenterApplicationArn: str
    ResponseMetadata: ResponseMetadata


class CreateQueueEnvironmentResponse(BaseValidatorModel):
    queueEnvironmentId: str
    ResponseMetadata: ResponseMetadata


class CreateQueueResponse(BaseValidatorModel):
    queueId: str
    ResponseMetadata: ResponseMetadata


class CreateStorageProfileResponse(BaseValidatorModel):
    storageProfileId: str
    ResponseMetadata: ResponseMetadata


class CreateWorkerResponse(BaseValidatorModel):
    workerId: str
    ResponseMetadata: ResponseMetadata


class GetFarmResponse(BaseValidatorModel):
    farmId: str
    displayName: str
    description: str
    kmsKeyArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class GetLicenseEndpointResponse(BaseValidatorModel):
    licenseEndpointId: str
    status: LicenseEndpointStatusType
    statusMessage: str
    vpcId: str
    dnsName: str
    subnetIds: List[str]
    securityGroupIds: List[str]
    ResponseMetadata: ResponseMetadata


class GetLimitResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class GetMonitorResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class GetQueueEnvironmentResponse(BaseValidatorModel):
    queueEnvironmentId: str
    name: str
    priority: int
    templateType: EnvironmentTemplateTypeType
    template: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class GetQueueFleetAssociationResponse(BaseValidatorModel):
    queueId: str
    fleetId: str
    status: QueueFleetAssociationStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class GetQueueLimitAssociationResponse(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    queueId: str
    limitId: str
    status: QueueLimitAssociationStatusType
    ResponseMetadata: ResponseMetadata


class GetTaskResponse(BaseValidatorModel):
    taskId: str
    createdAt: datetime
    createdBy: str
    runStatus: TaskRunStatusType
    targetRunStatus: TaskTargetRunStatusType
    failureRetryCount: int
    parameters: Dict[str, TaskParameterValue]
    startedAt: datetime
    endedAt: datetime
    updatedAt: datetime
    updatedBy: str
    latestSessionActionId: str
    ResponseMetadata: ResponseMetadata


class ListJobParameterDefinitionsResponse(BaseValidatorModel):
    jobParameterDefinitions: List[Dict[str, Any]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartSessionsStatisticsAggregationResponse(BaseValidatorModel):
    aggregationId: str
    ResponseMetadata: ResponseMetadata


class UpdateWorkerResponse(BaseValidatorModel):
    log: LogConfiguration
    ResponseMetadata: ResponseMetadata


class AttachmentsOutput(BaseValidatorModel):
    manifests: List[ManifestPropertiesOutput]
    fileSystem: Optional[JobAttachmentsFileSystemType] = None


class Attachments(BaseValidatorModel):
    manifests: Sequence[ManifestProperties]
    fileSystem: Optional[JobAttachmentsFileSystemType] = None


class BudgetScheduleOutput(BaseValidatorModel):
    fixed: Optional[FixedBudgetScheduleOutput] = None


class BudgetSummary(BaseValidatorModel):
    budgetId: str
    usageTrackingResource: UsageTrackingResource
    status: BudgetStatusType
    displayName: str
    approximateDollarLimit: float
    usages: ConsumedUsages
    createdBy: str
    createdAt: datetime
    description: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedAt: Optional[datetime] = None


class CopyJobTemplateRequest(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    targetS3Location: S3Location


class JobParameter(BaseValidatorModel):
    pass


class JobSearchSummary(BaseValidatorModel):
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
    jobParameters: Optional[Dict[str, JobParameter]] = None
    maxWorkerCount: Optional[int] = None
    sourceJobId: Optional[str] = None


class FileSystemLocation(BaseValidatorModel):
    pass


class CreateStorageProfileRequest(BaseValidatorModel):
    farmId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    clientToken: Optional[str] = None
    fileSystemLocations: Optional[Sequence[FileSystemLocation]] = None


class GetStorageProfileForQueueResponse(BaseValidatorModel):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    fileSystemLocations: List[FileSystemLocation]
    ResponseMetadata: ResponseMetadata


class GetStorageProfileResponse(BaseValidatorModel):
    storageProfileId: str
    displayName: str
    osFamily: StorageProfileOperatingSystemFamilyType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    fileSystemLocations: List[FileSystemLocation]
    ResponseMetadata: ResponseMetadata


class UpdateStorageProfileRequest(BaseValidatorModel):
    farmId: str
    storageProfileId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    osFamily: Optional[StorageProfileOperatingSystemFamilyType] = None
    fileSystemLocationsToAdd: Optional[Sequence[FileSystemLocation]] = None
    fileSystemLocationsToRemove: Optional[Sequence[FileSystemLocation]] = None


class FleetAmountCapability(BaseValidatorModel):
    pass


class FleetCapabilities(BaseValidatorModel):
    amounts: Optional[List[FleetAmountCapability]] = None
    attributes: Optional[List[FleetAttributeCapabilityOutput]] = None


class MemoryMiBRange(BaseValidatorModel):
    pass


class VCpuCountRange(BaseValidatorModel):
    pass


class AcceleratorTotalMemoryMiBRange(BaseValidatorModel):
    pass


class CustomerManagedWorkerCapabilitiesOutput(BaseValidatorModel):
    vCpuCount: VCpuCountRange
    memoryMiB: MemoryMiBRange
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    acceleratorTypes: Optional[List[Literal["gpu"]]] = None
    acceleratorCount: Optional[AcceleratorCountRange] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRange] = None
    customAmounts: Optional[List[FleetAmountCapability]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityOutput]] = None


class CustomerManagedWorkerCapabilities(BaseValidatorModel):
    vCpuCount: VCpuCountRange
    memoryMiB: MemoryMiBRange
    osFamily: CustomerManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    acceleratorTypes: Optional[Sequence[Literal["gpu"]]] = None
    acceleratorCount: Optional[AcceleratorCountRange] = None
    acceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRange] = None
    customAmounts: Optional[Sequence[FleetAmountCapability]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapability]] = None


class Timestamp(BaseValidatorModel):
    pass


class FixedBudgetSchedule(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp


class UpdatedSessionActionInfo(BaseValidatorModel):
    completedStatus: Optional[CompletedStatusType] = None
    processExitCode: Optional[int] = None
    progressMessage: Optional[str] = None
    startedAt: Optional[Timestamp] = None
    endedAt: Optional[Timestamp] = None
    updatedAt: Optional[Timestamp] = None
    progressPercent: Optional[float] = None


class StepSummary(BaseValidatorModel):
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
    dependencyCounts: Optional[DependencyCounts] = None


class ListFarmMembersResponse(BaseValidatorModel):
    members: List[FarmMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFarmsResponse(BaseValidatorModel):
    farms: List[FarmSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFleetMembersResponse(BaseValidatorModel):
    members: List[FleetMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFleetRequestWait(BaseValidatorModel):
    farmId: str
    fleetId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetJobRequestWait(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetLicenseEndpointRequestWaitExtra(BaseValidatorModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetLicenseEndpointRequestWait(BaseValidatorModel):
    licenseEndpointId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetQueueFleetAssociationRequestWait(BaseValidatorModel):
    farmId: str
    queueId: str
    fleetId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetQueueLimitAssociationRequestWait(BaseValidatorModel):
    farmId: str
    queueId: str
    limitId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetQueueRequestWaitExtra(BaseValidatorModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetQueueRequestWait(BaseValidatorModel):
    farmId: str
    queueId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetJobEntityError(BaseValidatorModel):
    jobDetails: Optional[JobDetailsError] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsError] = None
    stepDetails: Optional[StepDetailsError] = None
    environmentDetails: Optional[EnvironmentDetailsError] = None


class GetSessionsStatisticsAggregationRequestPaginate(BaseValidatorModel):
    farmId: str
    aggregationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAvailableMeteredProductsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBudgetsRequestPaginate(BaseValidatorModel):
    farmId: str
    status: Optional[BudgetStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFarmMembersRequestPaginate(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFarmsRequestPaginate(BaseValidatorModel):
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetMembersRequestPaginate(BaseValidatorModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsRequestPaginate(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    displayName: Optional[str] = None
    status: Optional[FleetStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobMembersRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobParameterDefinitionsRequestPaginate(BaseValidatorModel):
    farmId: str
    jobId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    principalId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLicenseEndpointsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLimitsRequestPaginate(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMeteredProductsRequestPaginate(BaseValidatorModel):
    licenseEndpointId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueueEnvironmentsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueueFleetAssociationsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    fleetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueueLimitAssociationsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: Optional[str] = None
    limitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueueMembersRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueuesRequestPaginate(BaseValidatorModel):
    farmId: str
    principalId: Optional[str] = None
    status: Optional[QueueStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSessionActionsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    sessionId: Optional[str] = None
    taskId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSessionsForWorkerRequestPaginate(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSessionsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStepConsumersRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStepDependenciesRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStepsRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStorageProfilesForQueueRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStorageProfilesRequestPaginate(BaseValidatorModel):
    farmId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTasksRequestPaginate(BaseValidatorModel):
    farmId: str
    queueId: str
    jobId: str
    stepId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkersRequestPaginate(BaseValidatorModel):
    farmId: str
    fleetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class HostPropertiesResponse(BaseValidatorModel):
    ipAddresses: Optional[IpAddressesOutput] = None
    hostName: Optional[str] = None
    ec2InstanceArn: Optional[str] = None
    ec2InstanceType: Optional[str] = None


class JobEntityIdentifiersUnion(BaseValidatorModel):
    jobDetails: Optional[JobDetailsIdentifiers] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsIdentifiers] = None
    stepDetails: Optional[StepDetailsIdentifiers] = None
    environmentDetails: Optional[EnvironmentDetailsIdentifiers] = None


class ListJobMembersResponse(BaseValidatorModel):
    members: List[JobMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobRunAsUser(BaseValidatorModel):
    runAs: RunAsType
    posix: Optional[PosixUser] = None
    windows: Optional[WindowsUser] = None


class ListJobsResponse(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListLicenseEndpointsResponse(BaseValidatorModel):
    licenseEndpoints: List[LicenseEndpointSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListLimitsResponse(BaseValidatorModel):
    limits: List[LimitSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAvailableMeteredProductsResponse(BaseValidatorModel):
    meteredProducts: List[MeteredProductSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMeteredProductsResponse(BaseValidatorModel):
    meteredProducts: List[MeteredProductSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMonitorsResponse(BaseValidatorModel):
    monitors: List[MonitorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQueueEnvironmentsResponse(BaseValidatorModel):
    environments: List[QueueEnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQueueFleetAssociationsResponse(BaseValidatorModel):
    queueFleetAssociations: List[QueueFleetAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQueueLimitAssociationsResponse(BaseValidatorModel):
    queueLimitAssociations: List[QueueLimitAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQueueMembersResponse(BaseValidatorModel):
    members: List[QueueMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQueuesResponse(BaseValidatorModel):
    queues: List[QueueSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSessionsForWorkerResponse(BaseValidatorModel):
    sessions: List[WorkerSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSessionsResponse(BaseValidatorModel):
    sessions: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStepConsumersResponse(BaseValidatorModel):
    consumers: List[StepConsumer]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStepDependenciesResponse(BaseValidatorModel):
    dependencies: List[StepDependency]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStorageProfilesForQueueResponse(BaseValidatorModel):
    storageProfiles: List[StorageProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStorageProfilesResponse(BaseValidatorModel):
    storageProfiles: List[StorageProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StepParameter(BaseValidatorModel):
    pass


class ParameterSpace(BaseValidatorModel):
    parameters: List[StepParameter]
    combination: Optional[str] = None


class SearchSortExpression(BaseValidatorModel):
    userJobsFirst: Optional[UserJobsFirst] = None
    fieldSort: Optional[FieldSortExpression] = None
    parameterSort: Optional[ParameterSortExpression] = None


class SessionActionDefinitionSummary(BaseValidatorModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinitionSummary] = None
    envExit: Optional[EnvironmentExitSessionActionDefinitionSummary] = None
    taskRun: Optional[TaskRunSessionActionDefinitionSummary] = None
    syncInputJobAttachments: Optional[ SyncInputJobAttachmentsSessionActionDefinitionSummary ] = None


class StartSessionsStatisticsAggregationRequest(BaseValidatorModel):
    farmId: str
    resourceIds: SessionsStatisticsResources
    startTime: Timestamp
    endTime: Timestamp
    groupBy: Sequence[UsageGroupByFieldType]
    statistics: Sequence[UsageStatisticType]
    timezone: Optional[str] = None
    period: Optional[PeriodType] = None


class Stats(BaseValidatorModel):
    pass


class Statistics(BaseValidatorModel):
    count: int
    costInUsd: Stats
    runtimeInSeconds: Stats
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


class StepAmountCapability(BaseValidatorModel):
    pass


class StepRequiredCapabilities(BaseValidatorModel):
    attributes: List[StepAttributeCapability]
    amounts: List[StepAmountCapability]


class WorkerCapabilities(BaseValidatorModel):
    amounts: Sequence[WorkerAmountCapability]
    attributes: Sequence[WorkerAttributeCapability]


class ServiceManagedEc2InstanceCapabilitiesOutput(BaseValidatorModel):
    vCpuCount: VCpuCountRange
    memoryMiB: MemoryMiBRange
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    rootEbsVolume: Optional[Ec2EbsVolume] = None
    acceleratorCapabilities: Optional[AcceleratorCapabilitiesOutput] = None
    allowedInstanceTypes: Optional[List[str]] = None
    excludedInstanceTypes: Optional[List[str]] = None
    customAmounts: Optional[List[FleetAmountCapability]] = None
    customAttributes: Optional[List[FleetAttributeCapabilityOutput]] = None


class ServiceManagedEc2InstanceCapabilities(BaseValidatorModel):
    vCpuCount: VCpuCountRange
    memoryMiB: MemoryMiBRange
    osFamily: ServiceManagedFleetOperatingSystemFamilyType
    cpuArchitectureType: CpuArchitectureTypeType
    rootEbsVolume: Optional[Ec2EbsVolume] = None
    acceleratorCapabilities: Optional[AcceleratorCapabilities] = None
    allowedInstanceTypes: Optional[Sequence[str]] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    customAmounts: Optional[Sequence[FleetAmountCapability]] = None
    customAttributes: Optional[Sequence[FleetAttributeCapability]] = None


class AssignedSessionActionDefinition(BaseValidatorModel):
    envEnter: Optional[AssignedEnvironmentEnterSessionActionDefinition] = None
    envExit: Optional[AssignedEnvironmentExitSessionActionDefinition] = None
    taskRun: Optional[AssignedTaskRunSessionActionDefinition] = None
    syncInputJobAttachments: Optional[ AssignedSyncInputJobAttachmentsSessionActionDefinition ] = None


class SessionActionDefinition(BaseValidatorModel):
    envEnter: Optional[EnvironmentEnterSessionActionDefinition] = None
    envExit: Optional[EnvironmentExitSessionActionDefinition] = None
    taskRun: Optional[TaskRunSessionActionDefinition] = None
    syncInputJobAttachments: Optional[SyncInputJobAttachmentsSessionActionDefinition] = None


class SearchTasksResponse(BaseValidatorModel):
    tasks: List[TaskSearchSummary]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadata


class ListTasksResponse(BaseValidatorModel):
    tasks: List[TaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetJobResponse(BaseValidatorModel):
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
    parameters: Dict[str, JobParameter]
    attachments: AttachmentsOutput
    description: str
    maxWorkerCount: int
    sourceJobId: str
    ResponseMetadata: ResponseMetadata


class JobAttachmentDetailsEntity(BaseValidatorModel):
    jobId: str
    attachments: AttachmentsOutput


class ResponseBudgetAction(BaseValidatorModel):
    pass


class GetBudgetResponse(BaseValidatorModel):
    budgetId: str
    usageTrackingResource: UsageTrackingResource
    status: BudgetStatusType
    displayName: str
    description: str
    approximateDollarLimit: float
    usages: ConsumedUsages
    actions: List[ResponseBudgetAction]
    schedule: BudgetScheduleOutput
    createdBy: str
    createdAt: datetime
    updatedBy: str
    updatedAt: datetime
    queueStoppedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListBudgetsResponse(BaseValidatorModel):
    budgets: List[BudgetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchJobsResponse(BaseValidatorModel):
    jobs: List[JobSearchSummary]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadata


class CustomerManagedFleetConfigurationOutput(BaseValidatorModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilitiesOutput
    storageProfileId: Optional[str] = None


class CustomerManagedFleetConfiguration(BaseValidatorModel):
    mode: AutoScalingModeType
    workerCapabilities: CustomerManagedWorkerCapabilities
    storageProfileId: Optional[str] = None


class DateTimeFilterExpression(BaseValidatorModel):
    pass


class StringFilterExpression(BaseValidatorModel):
    pass


class ParameterFilterExpression(BaseValidatorModel):
    pass


class SearchFilterExpression(BaseValidatorModel):
    dateTimeFilter: Optional[DateTimeFilterExpression] = None
    parameterFilter: Optional[ParameterFilterExpression] = None
    searchTermFilter: Optional[SearchTermFilterExpression] = None
    stringFilter: Optional[StringFilterExpression] = None
    groupFilter: Optional[Mapping[str, Any]] = None


class BudgetSchedule(BaseValidatorModel):
    fixed: Optional[FixedBudgetSchedule] = None


class UpdateWorkerScheduleRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    updatedSessionActions: Optional[Mapping[str, UpdatedSessionActionInfo]] = None


class ListStepsResponse(BaseValidatorModel):
    steps: List[StepSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetSessionResponse(BaseValidatorModel):
    sessionId: str
    fleetId: str
    workerId: str
    startedAt: datetime
    log: LogConfiguration
    lifecycleStatus: SessionLifecycleStatusType
    endedAt: datetime
    updatedAt: datetime
    updatedBy: str
    targetLifecycleStatus: Literal["ENDED"]
    hostProperties: HostPropertiesResponse
    workerLog: LogConfiguration
    ResponseMetadata: ResponseMetadata


class GetWorkerResponse(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    hostProperties: HostPropertiesResponse
    status: WorkerStatusType
    log: LogConfiguration
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class WorkerSearchSummary(BaseValidatorModel):
    fleetId: Optional[str] = None
    workerId: Optional[str] = None
    status: Optional[WorkerStatusType] = None
    hostProperties: Optional[HostPropertiesResponse] = None
    createdBy: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    updatedAt: Optional[datetime] = None


class WorkerSummary(BaseValidatorModel):
    workerId: str
    farmId: str
    fleetId: str
    status: WorkerStatusType
    createdAt: datetime
    createdBy: str
    hostProperties: Optional[HostPropertiesResponse] = None
    log: Optional[LogConfiguration] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class IpAddressesUnion(BaseValidatorModel):
    pass


class HostPropertiesRequest(BaseValidatorModel):
    ipAddresses: Optional[IpAddressesUnion] = None
    hostName: Optional[str] = None


class BatchGetJobEntityRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    identifiers: Sequence[JobEntityIdentifiersUnion]


class CreateQueueRequest(BaseValidatorModel):
    farmId: str
    displayName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    defaultBudgetAction: Optional[DefaultQueueBudgetActionType] = None
    jobAttachmentSettings: Optional[JobAttachmentSettings] = None
    roleArn: Optional[str] = None
    jobRunAsUser: Optional[JobRunAsUser] = None
    requiredFileSystemLocationNames: Optional[Sequence[str]] = None
    allowedStorageProfileIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class GetQueueResponse(BaseValidatorModel):
    queueId: str
    displayName: str
    description: str
    farmId: str
    status: QueueStatusType
    defaultBudgetAction: DefaultQueueBudgetActionType
    blockedReason: QueueBlockedReasonType
    jobAttachmentSettings: JobAttachmentSettings
    roleArn: str
    requiredFileSystemLocationNames: List[str]
    allowedStorageProfileIds: List[str]
    jobRunAsUser: JobRunAsUser
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class JobDetailsEntity(BaseValidatorModel):
    jobId: str
    logGroupName: str
    schemaVersion: str
    jobAttachmentSettings: Optional[JobAttachmentSettings] = None
    jobRunAsUser: Optional[JobRunAsUser] = None
    queueRoleArn: Optional[str] = None
    parameters: Optional[Dict[str, JobParameter]] = None
    pathMappingRules: Optional[List[PathMappingRule]] = None


class UpdateQueueRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    defaultBudgetAction: Optional[DefaultQueueBudgetActionType] = None
    jobAttachmentSettings: Optional[JobAttachmentSettings] = None
    roleArn: Optional[str] = None
    jobRunAsUser: Optional[JobRunAsUser] = None
    requiredFileSystemLocationNamesToAdd: Optional[Sequence[str]] = None
    requiredFileSystemLocationNamesToRemove: Optional[Sequence[str]] = None
    allowedStorageProfileIdsToAdd: Optional[Sequence[str]] = None
    allowedStorageProfileIdsToRemove: Optional[Sequence[str]] = None


class StepSearchSummary(BaseValidatorModel):
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
    parameterSpace: Optional[ParameterSpace] = None


class SessionActionSummary(BaseValidatorModel):
    sessionActionId: str
    status: SessionActionStatusType
    definition: SessionActionDefinitionSummary
    startedAt: Optional[datetime] = None
    endedAt: Optional[datetime] = None
    workerUpdatedAt: Optional[datetime] = None
    progressPercent: Optional[float] = None


class GetSessionsStatisticsAggregationResponse(BaseValidatorModel):
    statistics: List[Statistics]
    status: SessionsStatisticsAggregationStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetStepResponse(BaseValidatorModel):
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
    dependencyCounts: DependencyCounts
    requiredCapabilities: StepRequiredCapabilities
    parameterSpace: ParameterSpace
    description: str
    ResponseMetadata: ResponseMetadata


class ServiceManagedEc2InstanceMarketOptions(BaseValidatorModel):
    pass


class ServiceManagedEc2FleetConfigurationOutput(BaseValidatorModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilitiesOutput
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptions


class ServiceManagedEc2FleetConfiguration(BaseValidatorModel):
    instanceCapabilities: ServiceManagedEc2InstanceCapabilities
    instanceMarketOptions: ServiceManagedEc2InstanceMarketOptions


class AssignedSessionAction(BaseValidatorModel):
    sessionActionId: str
    definition: AssignedSessionActionDefinition


class GetSessionActionResponse(BaseValidatorModel):
    sessionActionId: str
    status: SessionActionStatusType
    startedAt: datetime
    endedAt: datetime
    workerUpdatedAt: datetime
    progressPercent: float
    sessionId: str
    processExitCode: int
    progressMessage: str
    definition: SessionActionDefinition
    acquiredLimits: List[AcquiredLimit]
    ResponseMetadata: ResponseMetadata


class AttachmentsUnion(BaseValidatorModel):
    pass


class CreateJobRequest(BaseValidatorModel):
    farmId: str
    queueId: str
    priority: int
    clientToken: Optional[str] = None
    template: Optional[str] = None
    templateType: Optional[JobTemplateTypeType] = None
    parameters: Optional[Mapping[str, JobParameter]] = None
    attachments: Optional[AttachmentsUnion] = None
    storageProfileId: Optional[str] = None
    targetTaskRunStatus: Optional[CreateJobTargetTaskRunStatusType] = None
    maxFailedTasksCount: Optional[int] = None
    maxRetriesPerTask: Optional[int] = None
    maxWorkerCount: Optional[int] = None
    sourceJobId: Optional[str] = None


class SearchWorkersResponse(BaseValidatorModel):
    workers: List[WorkerSearchSummary]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadata


class ListWorkersResponse(BaseValidatorModel):
    workers: List[WorkerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    hostProperties: Optional[HostPropertiesRequest] = None
    clientToken: Optional[str] = None


class UpdateWorkerRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    workerId: str
    status: Optional[UpdatedWorkerStatusType] = None
    capabilities: Optional[WorkerCapabilities] = None
    hostProperties: Optional[HostPropertiesRequest] = None


class JobEntity(BaseValidatorModel):
    jobDetails: Optional[JobDetailsEntity] = None
    jobAttachmentDetails: Optional[JobAttachmentDetailsEntity] = None
    stepDetails: Optional[StepDetailsEntity] = None
    environmentDetails: Optional[EnvironmentDetailsEntity] = None


class SearchStepsResponse(BaseValidatorModel):
    steps: List[StepSearchSummary]
    nextItemOffset: int
    totalResults: int
    ResponseMetadata: ResponseMetadata


class ListSessionActionsResponse(BaseValidatorModel):
    sessionActions: List[SessionActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FleetConfigurationOutput(BaseValidatorModel):
    customerManaged: Optional[CustomerManagedFleetConfigurationOutput] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfigurationOutput] = None


class FleetConfiguration(BaseValidatorModel):
    customerManaged: Optional[CustomerManagedFleetConfiguration] = None
    serviceManagedEc2: Optional[ServiceManagedEc2FleetConfiguration] = None


class AssignedSession(BaseValidatorModel):
    queueId: str
    jobId: str
    sessionActions: List[AssignedSessionAction]
    logConfiguration: LogConfiguration


class SearchGroupedFilterExpressions(BaseValidatorModel):
    pass


class SearchJobsRequest(BaseValidatorModel):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    filterExpressions: Optional[SearchGroupedFilterExpressions] = None
    sortExpressions: Optional[Sequence[SearchSortExpression]] = None
    pageSize: Optional[int] = None


class SearchStepsRequest(BaseValidatorModel):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    jobId: Optional[str] = None
    filterExpressions: Optional[SearchGroupedFilterExpressions] = None
    sortExpressions: Optional[Sequence[SearchSortExpression]] = None
    pageSize: Optional[int] = None


class SearchTasksRequest(BaseValidatorModel):
    farmId: str
    queueIds: Sequence[str]
    itemOffset: int
    jobId: Optional[str] = None
    filterExpressions: Optional[SearchGroupedFilterExpressions] = None
    sortExpressions: Optional[Sequence[SearchSortExpression]] = None
    pageSize: Optional[int] = None


class SearchWorkersRequest(BaseValidatorModel):
    farmId: str
    fleetIds: Sequence[str]
    itemOffset: int
    filterExpressions: Optional[SearchGroupedFilterExpressions] = None
    sortExpressions: Optional[Sequence[SearchSortExpression]] = None
    pageSize: Optional[int] = None


class BudgetScheduleUnion(BaseValidatorModel):
    pass


class BudgetActionToAdd(BaseValidatorModel):
    pass


class CreateBudgetRequest(BaseValidatorModel):
    farmId: str
    usageTrackingResource: UsageTrackingResource
    displayName: str
    approximateDollarLimit: float
    actions: Sequence[BudgetActionToAdd]
    schedule: BudgetScheduleUnion
    clientToken: Optional[str] = None
    description: Optional[str] = None


class BudgetActionToRemove(BaseValidatorModel):
    pass


class UpdateBudgetRequest(BaseValidatorModel):
    farmId: str
    budgetId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    status: Optional[BudgetStatusType] = None
    approximateDollarLimit: Optional[float] = None
    actionsToAdd: Optional[Sequence[BudgetActionToAdd]] = None
    actionsToRemove: Optional[Sequence[BudgetActionToRemove]] = None
    schedule: Optional[BudgetScheduleUnion] = None


class BatchGetJobEntityResponse(BaseValidatorModel):
    entities: List[JobEntity]
    errors: List[GetJobEntityError]
    ResponseMetadata: ResponseMetadata


class FleetSummary(BaseValidatorModel):
    fleetId: str
    farmId: str
    displayName: str
    status: FleetStatusType
    workerCount: int
    minWorkerCount: int
    maxWorkerCount: int
    configuration: FleetConfigurationOutput
    createdAt: datetime
    createdBy: str
    autoScalingStatus: Optional[AutoScalingStatusType] = None
    targetWorkerCount: Optional[int] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class GetFleetResponse(BaseValidatorModel):
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
    configuration: FleetConfigurationOutput
    capabilities: FleetCapabilities
    roleArn: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class UpdateWorkerScheduleResponse(BaseValidatorModel):
    assignedSessions: Dict[str, AssignedSession]
    cancelSessionActions: Dict[str, List[str]]
    desiredWorkerStatus: Literal["STOPPED"]
    updateIntervalSeconds: int
    ResponseMetadata: ResponseMetadata


class ListFleetsResponse(BaseValidatorModel):
    fleets: List[FleetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FleetConfigurationUnion(BaseValidatorModel):
    pass


class CreateFleetRequest(BaseValidatorModel):
    farmId: str
    displayName: str
    roleArn: str
    maxWorkerCount: int
    configuration: FleetConfigurationUnion
    clientToken: Optional[str] = None
    description: Optional[str] = None
    minWorkerCount: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFleetRequest(BaseValidatorModel):
    farmId: str
    fleetId: str
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    roleArn: Optional[str] = None
    minWorkerCount: Optional[int] = None
    maxWorkerCount: Optional[int] = None
    configuration: Optional[FleetConfigurationUnion] = None


