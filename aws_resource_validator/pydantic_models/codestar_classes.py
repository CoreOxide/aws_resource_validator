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
from aws_resource_validator.pydantic_models.codestar_constants import *

class AssociateTeamMemberRequestRequest(BaseValidatorModel):
    projectId: str
    userArn: str
    projectRole: str
    clientRequestToken: Optional[str] = None
    remoteAccessAllowed: Optional[bool] = None

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CodeCommitCodeDestination(BaseValidatorModel):
    name: str

class GitHubCodeDestination(BaseValidatorModel):
    name: str
    type: str
    owner: str
    privateRepository: bool
    issuesEnabled: bool
    token: str
    description: Optional[str] = None

class S3Location(BaseValidatorModel):
    bucketName: Optional[str] = None
    bucketKey: Optional[str] = None

class CreateUserProfileRequestRequest(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: Optional[str] = None

class DeleteProjectRequestRequest(BaseValidatorModel):
    id: str
    clientRequestToken: Optional[str] = None
    deleteStack: Optional[bool] = None

class DeleteUserProfileRequestRequest(BaseValidatorModel):
    userArn: str

class DescribeProjectRequestRequest(BaseValidatorModel):
    id: str

class ProjectStatus(BaseValidatorModel):
    state: str
    reason: Optional[str] = None

class DescribeUserProfileRequestRequest(BaseValidatorModel):
    userArn: str

class DisassociateTeamMemberRequestRequest(BaseValidatorModel):
    projectId: str
    userArn: str

class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListProjectsRequestRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummary(BaseValidatorModel):
    projectId: Optional[str] = None
    projectArn: Optional[str] = None

class ListResourcesRequestRequest(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class Resource(BaseValidatorModel):
    id: str

class ListTagsForProjectRequestRequest(BaseValidatorModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTeamMembersRequestRequest(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TeamMember(BaseValidatorModel):
    userArn: str
    projectRole: str
    remoteAccessAllowed: Optional[bool] = None

class ListUserProfilesRequestRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class UserProfileSummary(BaseValidatorModel):
    userArn: Optional[str] = None
    displayName: Optional[str] = None
    emailAddress: Optional[str] = None
    sshPublicKey: Optional[str] = None

class TagProjectRequestRequest(BaseValidatorModel):
    id: str
    tags: Mapping[str, str]

class UntagProjectRequestRequest(BaseValidatorModel):
    id: str
    tags: Sequence[str]

class UpdateProjectRequestRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateTeamMemberRequestRequest(BaseValidatorModel):
    projectId: str
    userArn: str
    projectRole: Optional[str] = None
    remoteAccessAllowed: Optional[bool] = None

class UpdateUserProfileRequestRequest(BaseValidatorModel):
    userArn: str
    displayName: Optional[str] = None
    emailAddress: Optional[str] = None
    sshPublicKey: Optional[str] = None

class AssociateTeamMemberResult(BaseValidatorModel):
    clientRequestToken: str
    ResponseMetadata: ResponseMetadata

class CreateProjectResult(BaseValidatorModel):
    id: str
    arn: str
    clientRequestToken: str
    projectTemplateId: str
    ResponseMetadata: ResponseMetadata

class CreateUserProfileResult(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadata

class DeleteProjectResult(BaseValidatorModel):
    stackId: str
    projectArn: str
    ResponseMetadata: ResponseMetadata

class DeleteUserProfileResult(BaseValidatorModel):
    userArn: str
    ResponseMetadata: ResponseMetadata

class DescribeUserProfileResult(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadata

class ListTagsForProjectResult(BaseValidatorModel):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: ResponseMetadata

class TagProjectResult(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

class UpdateTeamMemberResult(BaseValidatorModel):
    userArn: str
    projectRole: str
    remoteAccessAllowed: bool
    ResponseMetadata: ResponseMetadata

class UpdateUserProfileResult(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadata

class CodeDestination(BaseValidatorModel):
    codeCommit: Optional[CodeCommitCodeDestination] = None
    gitHub: Optional[GitHubCodeDestination] = None

class CodeSource(BaseValidatorModel):
    s3: S3Location

class ToolchainSource(BaseValidatorModel):
    s3: S3Location

class DescribeProjectResult(BaseValidatorModel):
    name: str
    id: str
    arn: str
    description: str
    clientRequestToken: str
    createdTimeStamp: datetime
    stackId: str
    projectTemplateId: str
    status: ProjectStatus
    ResponseMetadata: ResponseMetadata

class ListProjectsRequestListProjectsPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None

class ListResourcesRequestListResourcesPaginate(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfig] = None

class ListTeamMembersRequestListTeamMembersPaginate(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfig] = None

class ListUserProfilesRequestListUserProfilesPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None

class ListProjectsResult(BaseValidatorModel):
    projects: List[ProjectSummary]
    nextToken: str
    ResponseMetadata: ResponseMetadata

class ListResourcesResult(BaseValidatorModel):
    resources: List[Resource]
    nextToken: str
    ResponseMetadata: ResponseMetadata

class ListTeamMembersResult(BaseValidatorModel):
    teamMembers: List[TeamMember]
    nextToken: str
    ResponseMetadata: ResponseMetadata

class ListUserProfilesResult(BaseValidatorModel):
    userProfiles: List[UserProfileSummary]
    nextToken: str
    ResponseMetadata: ResponseMetadata

class Code(BaseValidatorModel):
    source: CodeSource
    destination: CodeDestination

class Toolchain(BaseValidatorModel):
    source: ToolchainSource
    roleArn: Optional[str] = None
    stackParameters: Optional[Mapping[str, str]] = None

class CreateProjectRequestRequest(BaseValidatorModel):
    name: str
    id: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    sourceCode: Optional[Sequence[Code]] = None
    toolchain: Optional[Toolchain] = None
    tags: Optional[Mapping[str, str]] = None

