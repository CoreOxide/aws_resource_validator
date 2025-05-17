from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessTokenSummary(BaseValidatorModel):
    id: str
    name: str
    expiresTime: Optional[datetime] = None

Timestamp = Union[datetime, str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class IdeConfiguration(BaseValidatorModel):
    runtime: Optional[str] = None
    name: Optional[str] = None


class PersistentStorageConfiguration(BaseValidatorModel):
    sizeInGiB: int


class RepositoryInput(BaseValidatorModel):
    repositoryName: str
    branchName: Optional[str] = None


# This class is the input for the 'create_project' function.
class CreateProjectRequest(BaseValidatorModel):
    spaceName: str
    displayName: str
    description: Optional[str] = None


# This class is the input for the 'create_source_repository_branch' function.
class CreateSourceRepositoryBranchRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    name: str
    headCommitId: Optional[str] = None


# This class is the input for the 'create_source_repository' function.
class CreateSourceRepositoryRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: Optional[str] = None


class DeleteAccessTokenRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_dev_environment' function.
class DeleteDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str


# This class is the input for the 'delete_project' function.
class DeleteProjectRequest(BaseValidatorModel):
    spaceName: str
    name: str


# This class is the input for the 'delete_source_repository' function.
class DeleteSourceRepositoryRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str


# This class is the input for the 'delete_space' function.
class DeleteSpaceRequest(BaseValidatorModel):
    name: str


class DevEnvironmentAccessDetails(BaseValidatorModel):
    streamUrl: str
    tokenValue: str


class DevEnvironmentRepositorySummary(BaseValidatorModel):
    repositoryName: str
    branchName: Optional[str] = None


class ExecuteCommandSessionConfiguration(BaseValidatorModel):
    command: str
    arguments: Optional[List[str]] = None


class DevEnvironmentSessionSummary(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    startedTime: datetime
    id: str


class Ide(BaseValidatorModel):
    runtime: Optional[str] = None
    name: Optional[str] = None


class PersistentStorage(BaseValidatorModel):
    sizeInGiB: int


class EmailAddress(BaseValidatorModel):
    email: Optional[str] = None
    verified: Optional[bool] = None


class EventPayload(BaseValidatorModel):
    contentType: Optional[str] = None
    data: Optional[str] = None


class ProjectInformation(BaseValidatorModel):
    name: Optional[str] = None
    projectId: Optional[str] = None


class UserIdentity(BaseValidatorModel):
    userType: UserTypeType
    principalId: str
    userName: Optional[str] = None
    awsAccountId: Optional[str] = None


class Filter(BaseValidatorModel):
    key: str
    values: List[str]
    comparisonOperator: Optional[str] = None


# This class is the input for the 'get_dev_environment' function.
class GetDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str


# This class is the input for the 'get_project' function.
class GetProjectRequest(BaseValidatorModel):
    spaceName: str
    name: str


# This class is the input for the 'get_source_repository_clone_urls' function.
class GetSourceRepositoryCloneUrlsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str


# This class is the input for the 'get_source_repository' function.
class GetSourceRepositoryRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str


# This class is the input for the 'get_space' function.
class GetSpaceRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'get_subscription' function.
class GetSubscriptionRequest(BaseValidatorModel):
    spaceName: str


# This class is the input for the 'get_user_details' function.
class GetUserDetailsRequest(BaseValidatorModel):
    id: Optional[str] = None
    userName: Optional[str] = None


# This class is the input for the 'get_workflow' function.
class GetWorkflowRequest(BaseValidatorModel):
    spaceName: str
    id: str
    projectName: str


class WorkflowDefinition(BaseValidatorModel):
    path: str


# This class is the input for the 'get_workflow_run' function.
class GetWorkflowRunRequest(BaseValidatorModel):
    spaceName: str
    id: str
    projectName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_access_tokens' function.
class ListAccessTokensRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_dev_environment_sessions' function.
class ListDevEnvironmentSessionsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ProjectListFilter(BaseValidatorModel):
    key: FilterKeyType
    values: List[str]
    comparisonOperator: Optional[ComparisonOperatorType] = None


class ProjectSummary(BaseValidatorModel):
    name: str
    displayName: Optional[str] = None
    description: Optional[str] = None


class ListSourceRepositoriesItem(BaseValidatorModel):
    id: str
    name: str
    lastUpdatedTime: datetime
    createdTime: datetime
    description: Optional[str] = None


# This class is the input for the 'list_source_repositories' function.
class ListSourceRepositoriesRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSourceRepositoryBranchesItem(BaseValidatorModel):
    ref: Optional[str] = None
    name: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    headCommitId: Optional[str] = None


# This class is the input for the 'list_source_repository_branches' function.
class ListSourceRepositoryBranchesRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_spaces' function.
class ListSpacesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class SpaceSummary(BaseValidatorModel):
    name: str
    regionName: str
    displayName: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'list_workflow_runs' function.
class ListWorkflowRunsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[List[Dict[str, Any]]] = None


class WorkflowRunSummary(BaseValidatorModel):
    id: str
    workflowId: str
    workflowName: str
    status: WorkflowRunStatusType
    startTime: datetime
    lastUpdatedTime: datetime
    statusReasons: Optional[List[Dict[str, Any]]] = None
    endTime: Optional[datetime] = None


# This class is the input for the 'list_workflows' function.
class ListWorkflowsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[List[Dict[str, Any]]] = None


# This class is the input for the 'start_workflow_run' function.
class StartWorkflowRunRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: str
    clientToken: Optional[str] = None


# This class is the input for the 'stop_dev_environment' function.
class StopDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str


# This class is the input for the 'stop_dev_environment_session' function.
class StopDevEnvironmentSessionRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    sessionId: str


# This class is the input for the 'update_project' function.
class UpdateProjectRequest(BaseValidatorModel):
    spaceName: str
    name: str
    description: Optional[str] = None


# This class is the input for the 'update_space' function.
class UpdateSpaceRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class WorkflowDefinitionSummary(BaseValidatorModel):
    path: str


# This class is the input for the 'create_access_token' function.
class CreateAccessTokenRequest(BaseValidatorModel):
    name: str
    expiresTime: Optional[Timestamp] = None


# This class is the input for the 'list_event_logs' function.
class ListEventLogsRequest(BaseValidatorModel):
    spaceName: str
    startTime: Timestamp
    endTime: Timestamp
    eventName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'create_access_token' function.
class CreateAccessTokenResponse(BaseValidatorModel):
    secret: str
    name: str
    expiresTime: datetime
    accessTokenId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_dev_environment' function.
class CreateDevEnvironmentResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    vpcConnectionName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_project' function.
class CreateProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_source_repository_branch' function.
class CreateSourceRepositoryBranchResponse(BaseValidatorModel):
    ref: str
    name: str
    lastUpdatedTime: datetime
    headCommitId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_source_repository' function.
class CreateSourceRepositoryResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_dev_environment' function.
class DeleteDevEnvironmentResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_project' function.
class DeleteProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_source_repository' function.
class DeleteSourceRepositoryResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_space' function.
class DeleteSpaceResponse(BaseValidatorModel):
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_project' function.
class GetProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_source_repository_clone_urls' function.
class GetSourceRepositoryCloneUrlsResponse(BaseValidatorModel):
    https: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_source_repository' function.
class GetSourceRepositoryResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    lastUpdatedTime: datetime
    createdTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_space' function.
class GetSpaceResponse(BaseValidatorModel):
    name: str
    regionName: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subscription' function.
class GetSubscriptionResponse(BaseValidatorModel):
    subscriptionType: str
    awsAccountName: str
    pendingSubscriptionType: str
    pendingSubscriptionStartTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_workflow_run' function.
class GetWorkflowRunResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    workflowId: str
    status: WorkflowRunStatusType
    statusReasons: List[Dict[str, Any]]
    startTime: datetime
    endTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_access_tokens' function.
class ListAccessTokensResponse(BaseValidatorModel):
    items: List[AccessTokenSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_dev_environment' function.
class StartDevEnvironmentResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    status: DevEnvironmentStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_workflow_run' function.
class StartWorkflowRunResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    workflowId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_dev_environment' function.
class StopDevEnvironmentResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    status: DevEnvironmentStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_dev_environment_session' function.
class StopDevEnvironmentSessionResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project' function.
class UpdateProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_space' function.
class UpdateSpaceResponse(BaseValidatorModel):
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


class VerifySessionResponse(BaseValidatorModel):
    identity: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_dev_environment' function.
class StartDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    ides: Optional[List[IdeConfiguration]] = None
    instanceType: Optional[InstanceTypeType] = None
    inactivityTimeoutMinutes: Optional[int] = None


# This class is the input for the 'update_dev_environment' function.
class UpdateDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    alias: Optional[str] = None
    ides: Optional[List[IdeConfiguration]] = None
    instanceType: Optional[InstanceTypeType] = None
    inactivityTimeoutMinutes: Optional[int] = None
    clientToken: Optional[str] = None


# This class is the output for the 'update_dev_environment' function.
class UpdateDevEnvironmentResponse(BaseValidatorModel):
    id: str
    spaceName: str
    projectName: str
    alias: str
    ides: List[IdeConfiguration]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_dev_environment' function.
class CreateDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    instanceType: InstanceTypeType
    persistentStorage: PersistentStorageConfiguration
    repositories: Optional[List[RepositoryInput]] = None
    clientToken: Optional[str] = None
    alias: Optional[str] = None
    ides: Optional[List[IdeConfiguration]] = None
    inactivityTimeoutMinutes: Optional[int] = None
    vpcConnectionName: Optional[str] = None


# This class is the output for the 'start_dev_environment_session' function.
class StartDevEnvironmentSessionResponse(BaseValidatorModel):
    accessDetails: DevEnvironmentAccessDetails
    sessionId: str
    spaceName: str
    projectName: str
    id: str
    ResponseMetadata: ResponseMetadata


class DevEnvironmentSessionConfiguration(BaseValidatorModel):
    sessionType: DevEnvironmentSessionTypeType
    executeCommandSessionConfiguration: Optional[ExecuteCommandSessionConfiguration] = None


# This class is the output for the 'list_dev_environment_sessions' function.
class ListDevEnvironmentSessionsResponse(BaseValidatorModel):
    items: List[DevEnvironmentSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DevEnvironmentSummary(BaseValidatorModel):
    id: str
    lastUpdatedTime: datetime
    creatorId: str
    status: DevEnvironmentStatusType
    repositories: List[DevEnvironmentRepositorySummary]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    persistentStorage: PersistentStorage
    spaceName: Optional[str] = None
    projectName: Optional[str] = None
    statusReason: Optional[str] = None
    alias: Optional[str] = None
    ides: Optional[List[Ide]] = None
    vpcConnectionName: Optional[str] = None


# This class is the output for the 'get_dev_environment' function.
class GetDevEnvironmentResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    lastUpdatedTime: datetime
    creatorId: str
    status: DevEnvironmentStatusType
    statusReason: str
    repositories: List[DevEnvironmentRepositorySummary]
    alias: str
    ides: List[Ide]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    persistentStorage: PersistentStorage
    vpcConnectionName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user_details' function.
class GetUserDetailsResponse(BaseValidatorModel):
    userId: str
    userName: str
    displayName: str
    primaryEmail: EmailAddress
    version: str
    ResponseMetadata: ResponseMetadata


class EventLogEntry(BaseValidatorModel):
    id: str
    eventName: str
    eventType: str
    eventCategory: str
    eventSource: str
    eventTime: datetime
    operationType: OperationTypeType
    userIdentity: UserIdentity
    projectInformation: Optional[ProjectInformation] = None
    requestId: Optional[str] = None
    requestPayload: Optional[EventPayload] = None
    responsePayload: Optional[EventPayload] = None
    errorCode: Optional[str] = None
    sourceIpAddress: Optional[str] = None
    userAgent: Optional[str] = None


# This class is the input for the 'list_dev_environments' function.
class ListDevEnvironmentsRequest(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[List[Filter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'get_workflow' function.
class GetWorkflowResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    name: str
    sourceRepositoryName: str
    sourceBranchName: str
    definition: WorkflowDefinition
    createdTime: datetime
    lastUpdatedTime: datetime
    runMode: WorkflowRunModeType
    status: WorkflowStatusType
    ResponseMetadata: ResponseMetadata


class ListAccessTokensRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDevEnvironmentSessionsRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDevEnvironmentsRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventLogsRequestPaginate(BaseValidatorModel):
    spaceName: str
    startTime: Timestamp
    endTime: Timestamp
    eventName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSourceRepositoriesRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSourceRepositoryBranchesRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSpacesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowRunsRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    sortBy: Optional[List[Dict[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowsRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: str
    sortBy: Optional[List[Dict[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    spaceName: str
    filters: Optional[List[ProjectListFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_projects' function.
class ListProjectsRequest(BaseValidatorModel):
    spaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[ProjectListFilter]] = None


# This class is the output for the 'list_projects' function.
class ListProjectsResponse(BaseValidatorModel):
    items: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_source_repositories' function.
class ListSourceRepositoriesResponse(BaseValidatorModel):
    items: List[ListSourceRepositoriesItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_source_repository_branches' function.
class ListSourceRepositoryBranchesResponse(BaseValidatorModel):
    items: List[ListSourceRepositoryBranchesItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_spaces' function.
class ListSpacesResponse(BaseValidatorModel):
    items: List[SpaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_workflow_runs' function.
class ListWorkflowRunsResponse(BaseValidatorModel):
    items: List[WorkflowRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkflowSummary(BaseValidatorModel):
    id: str
    name: str
    sourceRepositoryName: str
    sourceBranchName: str
    definition: WorkflowDefinitionSummary
    createdTime: datetime
    lastUpdatedTime: datetime
    runMode: WorkflowRunModeType
    status: WorkflowStatusType


# This class is the input for the 'start_dev_environment_session' function.
class StartDevEnvironmentSessionRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    sessionConfiguration: DevEnvironmentSessionConfiguration


# This class is the output for the 'list_dev_environments' function.
class ListDevEnvironmentsResponse(BaseValidatorModel):
    items: List[DevEnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_event_logs' function.
class ListEventLogsResponse(BaseValidatorModel):
    items: List[EventLogEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_workflows' function.
class ListWorkflowsResponse(BaseValidatorModel):
    items: List[WorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None