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


class CreateProjectRequestTypeDef(BaseValidatorModel):
    spaceName: str
    displayName: str
    description: Optional[str] = None


class CreateSourceRepositoryBranchRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    name: str
    headCommitId: Optional[str] = None


class CreateSourceRepositoryRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str
    description: Optional[str] = None


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    spaceName: str
    name: str


class DeleteSourceRepositoryRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str


class DeleteSpaceRequestTypeDef(BaseValidatorModel):
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


class GetProjectRequestTypeDef(BaseValidatorModel):
    spaceName: str
    name: str


class GetSourceRepositoryCloneUrlsRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str


class GetSourceRepositoryRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    name: str


class GetSpaceRequestTypeDef(BaseValidatorModel):
    name: str


class GetSubscriptionRequestTypeDef(BaseValidatorModel):
    spaceName: str


class WorkflowDefinitionTypeDef(BaseValidatorModel):
    path: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessTokensRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDevEnvironmentSessionsRequestTypeDef(BaseValidatorModel):
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


class ListSourceRepositoriesRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSourceRepositoryBranchesItemTypeDef(BaseValidatorModel):
    ref: Optional[str] = None
    name: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    headCommitId: Optional[str] = None


class ListSourceRepositoryBranchesRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSpacesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class SpaceSummaryTypeDef(BaseValidatorModel):
    name: str
    regionName: str
    displayName: Optional[str] = None
    description: Optional[str] = None


class ListWorkflowRunsRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None


class ListWorkflowsRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None


class StartWorkflowRunRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: str
    clientToken: Optional[str] = None


class UpdateProjectRequestTypeDef(BaseValidatorModel):
    spaceName: str
    name: str
    description: Optional[str] = None


class UpdateSpaceRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None


class WorkflowDefinitionSummaryTypeDef(BaseValidatorModel):
    path: str


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateAccessTokenRequestTypeDef(BaseValidatorModel):
    name: str
    expiresTime: Optional[TimestampTypeDef] = None


class ListEventLogsRequestTypeDef(BaseValidatorModel):
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


class AccessTokenSummaryTypeDef(BaseValidatorModel):
    pass


class ListAccessTokensResponseTypeDef(BaseValidatorModel):
    items: List[AccessTokenSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class CreateDevEnvironmentRequestTypeDef(BaseValidatorModel):
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


class DevEnvironmentSessionConfigurationTypeDef(BaseValidatorModel):
    sessionType: DevEnvironmentSessionTypeType
    executeCommandSessionConfiguration: Optional[ExecuteCommandSessionConfigurationTypeDef] = None


class DevEnvironmentSessionSummaryTypeDef(BaseValidatorModel):
    pass


class ListDevEnvironmentSessionsResponseTypeDef(BaseValidatorModel):
    items: List[DevEnvironmentSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetUserDetailsResponseTypeDef(BaseValidatorModel):
    userId: str
    userName: str
    displayName: str
    primaryEmail: EmailAddressTypeDef
    version: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListDevEnvironmentsRequestTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAccessTokensRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDevEnvironmentSessionsRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDevEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventLogsRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceRepositoriesRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceRepositoryBranchesRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSpacesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowRunsRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    workflowId: Optional[str] = None
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowsRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    projectName: str
    sortBy: Optional[Sequence[Mapping[str, Any]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestPaginateTypeDef(BaseValidatorModel):
    spaceName: str
    filters: Optional[Sequence[ProjectListFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestTypeDef(BaseValidatorModel):
    spaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[ProjectListFilterTypeDef]] = None


class ListProjectsResponseTypeDef(BaseValidatorModel):
    items: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSourceRepositoriesItemTypeDef(BaseValidatorModel):
    pass


class ListSourceRepositoriesResponseTypeDef(BaseValidatorModel):
    items: List[ListSourceRepositoriesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSourceRepositoryBranchesResponseTypeDef(BaseValidatorModel):
    items: List[ListSourceRepositoryBranchesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSpacesResponseTypeDef(BaseValidatorModel):
    items: List[SpaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowRunSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkflowRunsResponseTypeDef(BaseValidatorModel):
    items: List[WorkflowRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DevEnvironmentSummaryTypeDef(BaseValidatorModel):
    pass


class ListDevEnvironmentsResponseTypeDef(BaseValidatorModel):
    items: List[DevEnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EventLogEntryTypeDef(BaseValidatorModel):
    pass


class ListEventLogsResponseTypeDef(BaseValidatorModel):
    items: List[EventLogEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    items: List[WorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


