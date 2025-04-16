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
from aws_resource_validator.pydantic_models.codecatalyst_constants import *

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


class CreateProjectRequest(BaseValidatorModel):
    spaceName: str
    displayName: str
    description: Optional[str] = None


class CreateSourceRepositoryBranchRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    name: str
    headCommitId: Optional[str] = None


class CreateSourceRepositoryRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: Optional[str] = None


class DeleteProjectRequest(BaseValidatorModel):
    spaceName: str
    name: str


class DeleteSourceRepositoryRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str


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
    arguments: Optional[Sequence[str]] = None


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
    values: Sequence[str]
    comparisonOperator: Optional[str] = None


class GetProjectRequest(BaseValidatorModel):
    spaceName: str
    name: str


class GetSourceRepositoryCloneUrlsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str


class GetSourceRepositoryRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str


class GetSpaceRequest(BaseValidatorModel):
    name: str


class GetSubscriptionRequest(BaseValidatorModel):
    spaceName: str


class WorkflowDefinition(BaseValidatorModel):
    path: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessTokensRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDevEnvironmentSessionsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ProjectListFilter(BaseValidatorModel):
    key: FilterKeyType
    values: Sequence[str]
    comparisonOperator: Optional[ComparisonOperatorType] = None


class ProjectSummary(BaseValidatorModel):
    name: str
    displayName: Optional[str] = None
    description: Optional[str] = None


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


class ListSourceRepositoryBranchesRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSpacesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class SpaceSummary(BaseValidatorModel):
    name: str
    regionName: str
    displayName: Optional[str] = None
    description: Optional[str] = None


class ListWorkflowRunsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None


class ListWorkflowsRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None


class StartWorkflowRunRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: str
    clientToken: Optional[str] = None


class UpdateProjectRequest(BaseValidatorModel):
    spaceName: str
    name: str
    description: Optional[str] = None


class UpdateSpaceRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class WorkflowDefinitionSummary(BaseValidatorModel):
    path: str


class Timestamp(BaseValidatorModel):
    pass


class CreateAccessTokenRequest(BaseValidatorModel):
    name: str
    expiresTime: Optional[Timestamp] = None


class ListEventLogsRequest(BaseValidatorModel):
    spaceName: str
    startTime: Timestamp
    endTime: Timestamp
    eventName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class CreateAccessTokenResponse(BaseValidatorModel):
    secret: str
    name: str
    expiresTime: datetime
    accessTokenId: str
    ResponseMetadata: ResponseMetadata


class CreateProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


class CreateSourceRepositoryBranchResponse(BaseValidatorModel):
    ref: str
    name: str
    lastUpdatedTime: datetime
    headCommitId: str
    ResponseMetadata: ResponseMetadata


class CreateSourceRepositoryResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    ResponseMetadata: ResponseMetadata


class DeleteProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadata


class DeleteSourceRepositoryResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    ResponseMetadata: ResponseMetadata


class DeleteSpaceResponse(BaseValidatorModel):
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadata


class GetProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


class GetSourceRepositoryCloneUrlsResponse(BaseValidatorModel):
    https: str
    ResponseMetadata: ResponseMetadata


class GetSourceRepositoryResponse(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    lastUpdatedTime: datetime
    createdTime: datetime
    ResponseMetadata: ResponseMetadata


class GetSpaceResponse(BaseValidatorModel):
    name: str
    regionName: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


class GetSubscriptionResponse(BaseValidatorModel):
    subscriptionType: str
    awsAccountName: str
    pendingSubscriptionType: str
    pendingSubscriptionStartTime: datetime
    ResponseMetadata: ResponseMetadata


class AccessTokenSummary(BaseValidatorModel):
    pass


class ListAccessTokensResponse(BaseValidatorModel):
    items: List[AccessTokenSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateProjectResponse(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


class UpdateSpaceResponse(BaseValidatorModel):
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadata


class VerifySessionResponse(BaseValidatorModel):
    identity: str
    ResponseMetadata: ResponseMetadata


class CreateDevEnvironmentRequest(BaseValidatorModel):
    spaceName: str
    projectName: str
    instanceType: InstanceTypeType
    persistentStorage: PersistentStorageConfiguration
    repositories: Optional[Sequence[RepositoryInput]] = None
    clientToken: Optional[str] = None
    alias: Optional[str] = None
    ides: Optional[Sequence[IdeConfiguration]] = None
    inactivityTimeoutMinutes: Optional[int] = None
    vpcConnectionName: Optional[str] = None


class DevEnvironmentSessionConfiguration(BaseValidatorModel):
    sessionType: DevEnvironmentSessionTypeType
    executeCommandSessionConfiguration: Optional[ExecuteCommandSessionConfiguration] = None


class DevEnvironmentSessionSummary(BaseValidatorModel):
    pass


class ListDevEnvironmentSessionsResponse(BaseValidatorModel):
    items: List[DevEnvironmentSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetUserDetailsResponse(BaseValidatorModel):
    userId: str
    userName: str
    displayName: str
    primaryEmail: EmailAddress
    version: str
    ResponseMetadata: ResponseMetadata


class ListDevEnvironmentsRequest(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[Filter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


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
    filters: Optional[Sequence[Filter]] = None
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
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowsRequestPaginate(BaseValidatorModel):
    spaceName: str
    projectName: str
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    spaceName: str
    filters: Optional[Sequence[ProjectListFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequest(BaseValidatorModel):
    spaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[ProjectListFilter]] = None


class ListProjectsResponse(BaseValidatorModel):
    items: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSourceRepositoriesItem(BaseValidatorModel):
    pass


class ListSourceRepositoriesResponse(BaseValidatorModel):
    items: List[ListSourceRepositoriesItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSourceRepositoryBranchesResponse(BaseValidatorModel):
    items: List[ListSourceRepositoryBranchesItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSpacesResponse(BaseValidatorModel):
    items: List[SpaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkflowRunSummary(BaseValidatorModel):
    pass


class ListWorkflowRunsResponse(BaseValidatorModel):
    items: List[WorkflowRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DevEnvironmentSummary(BaseValidatorModel):
    pass


class ListDevEnvironmentsResponse(BaseValidatorModel):
    items: List[DevEnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EventLogEntry(BaseValidatorModel):
    pass


class ListEventLogsResponse(BaseValidatorModel):
    items: List[EventLogEntry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkflowSummary(BaseValidatorModel):
    pass


class ListWorkflowsResponse(BaseValidatorModel):
    items: List[WorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


