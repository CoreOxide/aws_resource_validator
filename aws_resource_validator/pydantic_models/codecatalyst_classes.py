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
from aws_resource_validator.pydantic_models.codecatalyst_constants import *

class AccessTokenSummaryTypeDef(BaseModel):
    id: str
    name: str
    expiresTime: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class IdeConfigurationTypeDef(BaseModel):
    runtime: Optional[str] = None
    name: Optional[str] = None

class PersistentStorageConfigurationTypeDef(BaseModel):
    sizeInGiB: int

class RepositoryInputTypeDef(BaseModel):
    repositoryName: str
    branchName: Optional[str] = None

class CreateProjectRequestRequestTypeDef(BaseModel):
    spaceName: str
    displayName: str
    description: Optional[str] = None

class CreateSourceRepositoryBranchRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    name: str
    headCommitId: Optional[str] = None

class CreateSourceRepositoryRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    name: str
    description: Optional[str] = None

class DeleteAccessTokenRequestRequestTypeDef(BaseModel):
    id: str

class DeleteDevEnvironmentRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str

class DeleteProjectRequestRequestTypeDef(BaseModel):
    spaceName: str
    name: str

class DeleteSourceRepositoryRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    name: str

class DeleteSpaceRequestRequestTypeDef(BaseModel):
    name: str

class DevEnvironmentAccessDetailsTypeDef(BaseModel):
    streamUrl: str
    tokenValue: str

class DevEnvironmentRepositorySummaryTypeDef(BaseModel):
    repositoryName: str
    branchName: Optional[str] = None

class ExecuteCommandSessionConfigurationTypeDef(BaseModel):
    command: str
    arguments: Optional[Sequence[str]] = None

class DevEnvironmentSessionSummaryTypeDef(BaseModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    startedTime: datetime
    id: str

class IdeTypeDef(BaseModel):
    runtime: Optional[str] = None
    name: Optional[str] = None

class PersistentStorageTypeDef(BaseModel):
    sizeInGiB: int

class EmailAddressTypeDef(BaseModel):
    email: Optional[str] = None
    verified: Optional[bool] = None

class EventPayloadTypeDef(BaseModel):
    contentType: Optional[str] = None
    data: Optional[str] = None

class ProjectInformationTypeDef(BaseModel):
    name: Optional[str] = None
    projectId: Optional[str] = None

class UserIdentityTypeDef(BaseModel):
    userType: UserTypeType
    principalId: str
    userName: Optional[str] = None
    awsAccountId: Optional[str] = None

class FilterTypeDef(BaseModel):
    key: str
    values: Sequence[str]
    comparisonOperator: Optional[str] = None

class GetDevEnvironmentRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str

class GetProjectRequestRequestTypeDef(BaseModel):
    spaceName: str
    name: str

class GetSourceRepositoryCloneUrlsRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str

class GetSourceRepositoryRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    name: str

class GetSpaceRequestRequestTypeDef(BaseModel):
    name: str

class GetSubscriptionRequestRequestTypeDef(BaseModel):
    spaceName: str

class GetUserDetailsRequestRequestTypeDef(BaseModel):
    id: Optional[str] = None
    userName: Optional[str] = None

class GetWorkflowRequestRequestTypeDef(BaseModel):
    spaceName: str
    id: str
    projectName: str

class WorkflowDefinitionTypeDef(BaseModel):
    path: str

class GetWorkflowRunRequestRequestTypeDef(BaseModel):
    spaceName: str
    id: str
    projectName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessTokensRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDevEnvironmentSessionsRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectListFilterTypeDef(BaseModel):
    key: FilterKeyType
    values: Sequence[str]
    comparisonOperator: Optional[ComparisonOperatorType] = None

class ProjectSummaryTypeDef(BaseModel):
    name: str
    displayName: Optional[str] = None
    description: Optional[str] = None

class ListSourceRepositoriesItemTypeDef(BaseModel):
    id: str
    name: str
    lastUpdatedTime: datetime
    createdTime: datetime
    description: Optional[str] = None

class ListSourceRepositoriesRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSourceRepositoryBranchesItemTypeDef(BaseModel):
    ref: Optional[str] = None
    name: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    headCommitId: Optional[str] = None

class ListSourceRepositoryBranchesRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSpacesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class SpaceSummaryTypeDef(BaseModel):
    name: str
    regionName: str
    displayName: Optional[str] = None
    description: Optional[str] = None

class ListWorkflowRunsRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None

class WorkflowRunSummaryTypeDef(BaseModel):
    id: str
    workflowId: str
    workflowName: str
    status: WorkflowRunStatusType
    startTime: datetime
    lastUpdatedTime: datetime
    statusReasons: Optional[List[Dict[str, Any]]] = None
    endTime: Optional[datetime] = None

class ListWorkflowsRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None

class StartWorkflowRunRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    workflowId: str
    clientToken: Optional[str] = None

class StopDevEnvironmentRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str

class StopDevEnvironmentSessionRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    sessionId: str

class UpdateProjectRequestRequestTypeDef(BaseModel):
    spaceName: str
    name: str
    description: Optional[str] = None

class UpdateSpaceRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None

class WorkflowDefinitionSummaryTypeDef(BaseModel):
    path: str

class CreateAccessTokenRequestRequestTypeDef(BaseModel):
    name: str
    expiresTime: Optional[TimestampTypeDef] = None

class ListEventLogsRequestRequestTypeDef(BaseModel):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class CreateAccessTokenResponseTypeDef(BaseModel):
    secret: str
    name: str
    expiresTime: datetime
    accessTokenId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevEnvironmentResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    vpcConnectionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(BaseModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSourceRepositoryBranchResponseTypeDef(BaseModel):
    ref: str
    name: str
    lastUpdatedTime: datetime
    headCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSourceRepositoryResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDevEnvironmentResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(BaseModel):
    spaceName: str
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSourceRepositoryResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSpaceResponseTypeDef(BaseModel):
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResponseTypeDef(BaseModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceRepositoryCloneUrlsResponseTypeDef(BaseModel):
    https: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceRepositoryResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    lastUpdatedTime: datetime
    createdTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpaceResponseTypeDef(BaseModel):
    name: str
    regionName: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionResponseTypeDef(BaseModel):
    subscriptionType: str
    awsAccountName: str
    pendingSubscriptionType: str
    pendingSubscriptionStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    workflowId: str
    status: WorkflowRunStatusType
    statusReasons: List[Dict[str, Any]]
    startTime: datetime
    endTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessTokensResponseTypeDef(BaseModel):
    items: List[AccessTokenSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDevEnvironmentResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    status: DevEnvironmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkflowRunResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    workflowId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopDevEnvironmentResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    status: DevEnvironmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDevEnvironmentSessionResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResponseTypeDef(BaseModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSpaceResponseTypeDef(BaseModel):
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifySessionResponseTypeDef(BaseModel):
    identity: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDevEnvironmentRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    ides: Optional[Sequence[IdeConfigurationTypeDef]] = None
    instanceType: Optional[InstanceTypeType] = None
    inactivityTimeoutMinutes: Optional[int] = None

class UpdateDevEnvironmentRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    alias: Optional[str] = None
    ides: Optional[Sequence[IdeConfigurationTypeDef]] = None
    instanceType: Optional[InstanceTypeType] = None
    inactivityTimeoutMinutes: Optional[int] = None
    clientToken: Optional[str] = None

class UpdateDevEnvironmentResponseTypeDef(BaseModel):
    id: str
    spaceName: str
    projectName: str
    alias: str
    ides: List[IdeConfigurationTypeDef]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevEnvironmentRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    instanceType: InstanceTypeType
    persistentStorage: PersistentStorageConfigurationTypeDef
    repositories: Optional[Sequence[RepositoryInputTypeDef]] = None
    clientToken: Optional[str] = None
    alias: Optional[str] = None
    ides: Optional[Sequence[IdeConfigurationTypeDef]] = None
    inactivityTimeoutMinutes: Optional[int] = None
    vpcConnectionName: Optional[str] = None

class StartDevEnvironmentSessionResponseTypeDef(BaseModel):
    accessDetails: DevEnvironmentAccessDetailsTypeDef
    sessionId: str
    spaceName: str
    projectName: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DevEnvironmentSessionConfigurationTypeDef(BaseModel):
    sessionType: DevEnvironmentSessionTypeType
    executeCommandSessionConfiguration: Optional[       ExecuteCommandSessionConfigurationTypeDef     ] = None

class ListDevEnvironmentSessionsResponseTypeDef(BaseModel):
    items: List[DevEnvironmentSessionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DevEnvironmentSummaryTypeDef(BaseModel):
    id: str
    lastUpdatedTime: datetime
    creatorId: str
    status: DevEnvironmentStatusType
    repositories: List[DevEnvironmentRepositorySummaryTypeDef]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    persistentStorage: PersistentStorageTypeDef
    spaceName: Optional[str] = None
    projectName: Optional[str] = None
    statusReason: Optional[str] = None
    alias: Optional[str] = None
    ides: Optional[List[IdeTypeDef]] = None
    vpcConnectionName: Optional[str] = None

class GetDevEnvironmentResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    lastUpdatedTime: datetime
    creatorId: str
    status: DevEnvironmentStatusType
    statusReason: str
    repositories: List[DevEnvironmentRepositorySummaryTypeDef]
    alias: str
    ides: List[IdeTypeDef]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    persistentStorage: PersistentStorageTypeDef
    vpcConnectionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserDetailsResponseTypeDef(BaseModel):
    userId: str
    userName: str
    displayName: str
    primaryEmail: EmailAddressTypeDef
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventLogEntryTypeDef(BaseModel):
    id: str
    eventName: str
    eventType: str
    eventCategory: str
    eventSource: str
    eventTime: datetime
    operationType: OperationTypeType
    userIdentity: UserIdentityTypeDef
    projectInformation: Optional[ProjectInformationTypeDef] = None
    requestId: Optional[str] = None
    requestPayload: Optional[EventPayloadTypeDef] = None
    responsePayload: Optional[EventPayloadTypeDef] = None
    errorCode: Optional[str] = None
    sourceIpAddress: Optional[str] = None
    userAgent: Optional[str] = None

class ListDevEnvironmentsRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetWorkflowResponseTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    name: str
    sourceRepositoryName: str
    sourceBranchName: str
    definition: WorkflowDefinitionTypeDef
    createdTime: datetime
    lastUpdatedTime: datetime
    runMode: WorkflowRunModeType
    status: WorkflowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessTokensRequestListAccessTokensPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevEnvironmentSessionsRequestListDevEnvironmentSessionsPaginateTypeDef(BaseModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevEnvironmentsRequestListDevEnvironmentsPaginateTypeDef(BaseModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventLogsRequestListEventLogsPaginateTypeDef(BaseModel):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceRepositoriesRequestListSourceRepositoriesPaginateTypeDef(BaseModel):
    spaceName: str
    projectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateTypeDef(BaseModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpacesRequestListSpacesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowRunsRequestListWorkflowRunsPaginateTypeDef(BaseModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseModel):
    spaceName: str
    projectName: str
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    spaceName: str
    filters: Optional[Sequence[ProjectListFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    spaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[ProjectListFilterTypeDef]] = None

class ListProjectsResponseTypeDef(BaseModel):
    nextToken: str
    items: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSourceRepositoriesResponseTypeDef(BaseModel):
    items: List[ListSourceRepositoriesItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSourceRepositoryBranchesResponseTypeDef(BaseModel):
    nextToken: str
    items: List[ListSourceRepositoryBranchesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpacesResponseTypeDef(BaseModel):
    nextToken: str
    items: List[SpaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowRunsResponseTypeDef(BaseModel):
    nextToken: str
    items: List[WorkflowRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowSummaryTypeDef(BaseModel):
    id: str
    name: str
    sourceRepositoryName: str
    sourceBranchName: str
    definition: WorkflowDefinitionSummaryTypeDef
    createdTime: datetime
    lastUpdatedTime: datetime
    runMode: WorkflowRunModeType
    status: WorkflowStatusType

class StartDevEnvironmentSessionRequestRequestTypeDef(BaseModel):
    spaceName: str
    projectName: str
    id: str
    sessionConfiguration: DevEnvironmentSessionConfigurationTypeDef

class ListDevEnvironmentsResponseTypeDef(BaseModel):
    items: List[DevEnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventLogsResponseTypeDef(BaseModel):
    nextToken: str
    items: List[EventLogEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowsResponseTypeDef(BaseModel):
    nextToken: str
    items: List[WorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

