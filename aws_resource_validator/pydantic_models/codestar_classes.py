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
from aws_resource_validator.pydantic_models.codestar_constants import *

class AssociateTeamMemberRequestRequestTypeDef(BaseModel):
    projectId: str
    userArn: str
    projectRole: str
    clientRequestToken: Optional[str] = None
    remoteAccessAllowed: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CodeCommitCodeDestinationTypeDef(BaseModel):
    name: str

class GitHubCodeDestinationTypeDef(BaseModel):
    name: str
    type: str
    owner: str
    privateRepository: bool
    issuesEnabled: bool
    token: str
    description: Optional[str] = None

class S3LocationTypeDef(BaseModel):
    bucketName: Optional[str] = None
    bucketKey: Optional[str] = None

class CreateUserProfileRequestRequestTypeDef(BaseModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseModel):
    id: str
    clientRequestToken: Optional[str] = None
    deleteStack: Optional[bool] = None

class DeleteUserProfileRequestRequestTypeDef(BaseModel):
    userArn: str

class DescribeProjectRequestRequestTypeDef(BaseModel):
    id: str

class ProjectStatusTypeDef(BaseModel):
    state: str
    reason: Optional[str] = None

class DescribeUserProfileRequestRequestTypeDef(BaseModel):
    userArn: str

class DisassociateTeamMemberRequestRequestTypeDef(BaseModel):
    projectId: str
    userArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummaryTypeDef(BaseModel):
    projectId: Optional[str] = None
    projectArn: Optional[str] = None

class ListResourcesRequestRequestTypeDef(BaseModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ResourceTypeDef(BaseModel):
    id: str

class ListTagsForProjectRequestRequestTypeDef(BaseModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTeamMembersRequestRequestTypeDef(BaseModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TeamMemberTypeDef(BaseModel):
    userArn: str
    projectRole: str
    remoteAccessAllowed: Optional[bool] = None

class ListUserProfilesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class UserProfileSummaryTypeDef(BaseModel):
    userArn: Optional[str] = None
    displayName: Optional[str] = None
    emailAddress: Optional[str] = None
    sshPublicKey: Optional[str] = None

class TagProjectRequestRequestTypeDef(BaseModel):
    id: str
    tags: Mapping[str, str]

class UntagProjectRequestRequestTypeDef(BaseModel):
    id: str
    tags: Sequence[str]

class UpdateProjectRequestRequestTypeDef(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateTeamMemberRequestRequestTypeDef(BaseModel):
    projectId: str
    userArn: str
    projectRole: Optional[str] = None
    remoteAccessAllowed: Optional[bool] = None

class UpdateUserProfileRequestRequestTypeDef(BaseModel):
    userArn: str
    displayName: Optional[str] = None
    emailAddress: Optional[str] = None
    sshPublicKey: Optional[str] = None

class AssociateTeamMemberResultTypeDef(BaseModel):
    clientRequestToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResultTypeDef(BaseModel):
    id: str
    arn: str
    clientRequestToken: str
    projectTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserProfileResultTypeDef(BaseModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResultTypeDef(BaseModel):
    stackId: str
    projectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserProfileResultTypeDef(BaseModel):
    userArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserProfileResultTypeDef(BaseModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForProjectResultTypeDef(BaseModel):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagProjectResultTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTeamMemberResultTypeDef(BaseModel):
    userArn: str
    projectRole: str
    remoteAccessAllowed: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserProfileResultTypeDef(BaseModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CodeDestinationTypeDef(BaseModel):
    codeCommit: Optional[CodeCommitCodeDestinationTypeDef] = None
    gitHub: Optional[GitHubCodeDestinationTypeDef] = None

class CodeSourceTypeDef(BaseModel):
    s3: S3LocationTypeDef

class ToolchainSourceTypeDef(BaseModel):
    s3: S3LocationTypeDef

class DescribeProjectResultTypeDef(BaseModel):
    name: str
    id: str
    arn: str
    description: str
    clientRequestToken: str
    createdTimeStamp: datetime
    stackId: str
    projectTemplateId: str
    status: ProjectStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesRequestListResourcesPaginateTypeDef(BaseModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTeamMembersRequestListTeamMembersPaginateTypeDef(BaseModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserProfilesRequestListUserProfilesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsResultTypeDef(BaseModel):
    projects: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesResultTypeDef(BaseModel):
    resources: List[ResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTeamMembersResultTypeDef(BaseModel):
    teamMembers: List[TeamMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserProfilesResultTypeDef(BaseModel):
    userProfiles: List[UserProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CodeTypeDef(BaseModel):
    source: CodeSourceTypeDef
    destination: CodeDestinationTypeDef

class ToolchainTypeDef(BaseModel):
    source: ToolchainSourceTypeDef
    roleArn: Optional[str] = None
    stackParameters: Optional[Mapping[str, str]] = None

class CreateProjectRequestRequestTypeDef(BaseModel):
    name: str
    id: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    sourceCode: Optional[Sequence[CodeTypeDef]] = None
    toolchain: Optional[ToolchainTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

