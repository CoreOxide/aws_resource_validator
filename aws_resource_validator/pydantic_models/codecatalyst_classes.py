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
from aws_resource_validator.pydantic_models.codecatalyst_constants import *

class AccessTokenSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    expiresTime: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class IdeConfigurationTypeDef(BaseValidatorModel):
    runtime: Optional[str] = None
    name: Optional[str] = None

class PersistentStorageConfigurationTypeDef(BaseValidatorModel):
    sizeInGiB: int

class RepositoryInputTypeDef(BaseValidatorModel):
    repositoryName: str
    branchName: Optional[str] = None

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    displayName: str
    description: Optional[str] = None

class CreateSourceRepositoryBranchRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    name: str
    headCommitId: Optional[str] = None

class CreateSourceRepositoryRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: Optional[str] = None

class DeleteAccessTokenRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteDevEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    name: str

class DeleteSourceRepositoryRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str

class DeleteSpaceRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DevEnvironmentAccessDetailsTypeDef(BaseValidatorModel):
    streamUrl: str
    tokenValue: str

class DevEnvironmentRepositorySummaryTypeDef(BaseValidatorModel):
    repositoryName: str
    branchName: Optional[str] = None

class ExecuteCommandSessionConfigurationTypeDef(BaseValidatorModel):
    command: str
    arguments: Optional[Sequence[str]] = None

class DevEnvironmentSessionSummaryTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    startedTime: datetime
    id: str

class IdeTypeDef(BaseValidatorModel):
    runtime: Optional[str] = None
    name: Optional[str] = None

class PersistentStorageTypeDef(BaseValidatorModel):
    sizeInGiB: int

class EmailAddressTypeDef(BaseValidatorModel):
    email: Optional[str] = None
    verified: Optional[bool] = None

class EventPayloadTypeDef(BaseValidatorModel):
    contentType: Optional[str] = None
    data: Optional[str] = None

class ProjectInformationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    projectId: Optional[str] = None

class UserIdentityTypeDef(BaseValidatorModel):
    userType: UserTypeType
    principalId: str
    userName: Optional[str] = None
    awsAccountId: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    key: str
    values: Sequence[str]
    comparisonOperator: Optional[str] = None

class GetDevEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str

class GetProjectRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    name: str

class GetSourceRepositoryCloneUrlsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str

class GetSourceRepositoryRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str

class GetSpaceRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str

class GetUserDetailsRequestRequestTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    userName: Optional[str] = None

class GetWorkflowRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    id: str
    projectName: str

class WorkflowDefinitionTypeDef(BaseValidatorModel):
    path: str

class GetWorkflowRunRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    id: str
    projectName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessTokensRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDevEnvironmentSessionsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectListFilterTypeDef(BaseValidatorModel):
    key: FilterKeyType
    values: Sequence[str]
    comparisonOperator: Optional[ComparisonOperatorType] = None

class ProjectSummaryTypeDef(BaseValidatorModel):
    name: str
    displayName: Optional[str] = None
    description: Optional[str] = None

class ListSourceRepositoriesItemTypeDef(BaseValidatorModel):
    id: str
    name: str
    lastUpdatedTime: datetime
    createdTime: datetime
    description: Optional[str] = None

class ListSourceRepositoriesRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSourceRepositoryBranchesItemTypeDef(BaseValidatorModel):
    ref: Optional[str] = None
    name: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    headCommitId: Optional[str] = None

class ListSourceRepositoryBranchesRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSpacesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class SpaceSummaryTypeDef(BaseValidatorModel):
    name: str
    regionName: str
    displayName: Optional[str] = None
    description: Optional[str] = None

class ListWorkflowRunsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None

class WorkflowRunSummaryTypeDef(BaseValidatorModel):
    id: str
    workflowId: str
    workflowName: str
    status: WorkflowRunStatusType
    startTime: datetime
    lastUpdatedTime: datetime
    statusReasons: Optional[List[Dict[str, Any]]] = None
    endTime: Optional[datetime] = None

class ListWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None

class StartWorkflowRunRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: str
    clientToken: Optional[str] = None

class StopDevEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str

class StopDevEnvironmentSessionRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    sessionId: str

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    name: str
    description: Optional[str] = None

class UpdateSpaceRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None

class WorkflowDefinitionSummaryTypeDef(BaseValidatorModel):
    path: str

class CreateAccessTokenRequestRequestTypeDef(BaseValidatorModel):
    name: str
    expiresTime: Optional[TimestampTypeDef] = None

class ListEventLogsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class CreateAccessTokenResponseTypeDef(BaseValidatorModel):
    secret: str
    name: str
    expiresTime: datetime
    accessTokenId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevEnvironmentResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    vpcConnectionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSourceRepositoryBranchResponseTypeDef(BaseValidatorModel):
    ref: str
    name: str
    lastUpdatedTime: datetime
    headCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSourceRepositoryResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDevEnvironmentResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSourceRepositoryResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSpaceResponseTypeDef(BaseValidatorModel):
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResponseTypeDef(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceRepositoryCloneUrlsResponseTypeDef(BaseValidatorModel):
    https: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceRepositoryResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: str
    lastUpdatedTime: datetime
    createdTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpaceResponseTypeDef(BaseValidatorModel):
    name: str
    regionName: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionResponseTypeDef(BaseValidatorModel):
    subscriptionType: str
    awsAccountName: str
    pendingSubscriptionType: str
    pendingSubscriptionStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunResponseTypeDef(BaseValidatorModel):
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

class ListAccessTokensResponseTypeDef(BaseValidatorModel):
    items: List[AccessTokenSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDevEnvironmentResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    status: DevEnvironmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkflowRunResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    workflowId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopDevEnvironmentResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    status: DevEnvironmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDevEnvironmentSessionResponseTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResponseTypeDef(BaseValidatorModel):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSpaceResponseTypeDef(BaseValidatorModel):
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifySessionResponseTypeDef(BaseValidatorModel):
    identity: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDevEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    ides: Optional[Sequence[IdeConfigurationTypeDef]] = None
    instanceType: Optional[InstanceTypeType] = None
    inactivityTimeoutMinutes: Optional[int] = None

class UpdateDevEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    alias: Optional[str] = None
    ides: Optional[Sequence[IdeConfigurationTypeDef]] = None
    instanceType: Optional[InstanceTypeType] = None
    inactivityTimeoutMinutes: Optional[int] = None
    clientToken: Optional[str] = None

class UpdateDevEnvironmentResponseTypeDef(BaseValidatorModel):
    id: str
    spaceName: str
    projectName: str
    alias: str
    ides: List[IdeConfigurationTypeDef]
    instanceType: InstanceTypeType
    inactivityTimeoutMinutes: int
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevEnvironmentRequestRequestTypeDef(BaseValidatorModel):
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

class StartDevEnvironmentSessionResponseTypeDef(BaseValidatorModel):
    accessDetails: DevEnvironmentAccessDetailsTypeDef
    sessionId: str
    spaceName: str
    projectName: str
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DevEnvironmentSessionConfigurationTypeDef(BaseValidatorModel):
    sessionType: DevEnvironmentSessionTypeType
    executeCommandSessionConfiguration: Optional[       ExecuteCommandSessionConfigurationTypeDef     ] = None

class ListDevEnvironmentSessionsResponseTypeDef(BaseValidatorModel):
    items: List[DevEnvironmentSessionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DevEnvironmentSummaryTypeDef(BaseValidatorModel):
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

class GetDevEnvironmentResponseTypeDef(BaseValidatorModel):
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

class GetUserDetailsResponseTypeDef(BaseValidatorModel):
    userId: str
    userName: str
    displayName: str
    primaryEmail: EmailAddressTypeDef
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventLogEntryTypeDef(BaseValidatorModel):
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

class ListDevEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetWorkflowResponseTypeDef(BaseValidatorModel):
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

class ListAccessTokensRequestListAccessTokensPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevEnvironmentSessionsRequestListDevEnvironmentSessionsPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevEnvironmentsRequestListDevEnvironmentsPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventLogsRequestListEventLogsPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceRepositoriesRequestListSourceRepositoriesPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpacesRequestListSpacesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowRunsRequestListWorkflowRunsPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    filters: Optional[Sequence[ProjectListFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[ProjectListFilterTypeDef]] = None

class ListProjectsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSourceRepositoriesResponseTypeDef(BaseValidatorModel):
    items: List[ListSourceRepositoriesItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSourceRepositoryBranchesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[ListSourceRepositoryBranchesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpacesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[SpaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowRunsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[WorkflowRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    sourceRepositoryName: str
    sourceBranchName: str
    definition: WorkflowDefinitionSummaryTypeDef
    createdTime: datetime
    lastUpdatedTime: datetime
    runMode: WorkflowRunModeType
    status: WorkflowStatusType

class StartDevEnvironmentSessionRequestRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    id: str
    sessionConfiguration: DevEnvironmentSessionConfigurationTypeDef

class ListDevEnvironmentsResponseTypeDef(BaseValidatorModel):
    items: List[DevEnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventLogsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[EventLogEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[WorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

