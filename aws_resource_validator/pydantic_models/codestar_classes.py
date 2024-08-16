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

class AssociateTeamMemberRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    userArn: str
    projectRole: str
    clientRequestToken: Optional[str] = None
    remoteAccessAllowed: Optional[bool] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CodeCommitCodeDestinationTypeDef(BaseValidatorModel):
    name: str

class GitHubCodeDestinationTypeDef(BaseValidatorModel):
    name: str
    type: str
    owner: str
    privateRepository: bool
    issuesEnabled: bool
    token: str
    description: Optional[str] = None

class S3LocationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    bucketKey: Optional[str] = None

class CreateUserProfileRequestRequestTypeDef(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientRequestToken: Optional[str] = None
    deleteStack: Optional[bool] = None

class DeleteUserProfileRequestRequestTypeDef(BaseValidatorModel):
    userArn: str

class DescribeProjectRequestRequestTypeDef(BaseValidatorModel):
    id: str

class ProjectStatusTypeDef(BaseValidatorModel):
    state: str
    reason: Optional[str] = None

class DescribeUserProfileRequestRequestTypeDef(BaseValidatorModel):
    userArn: str

class DisassociateTeamMemberRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    userArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummaryTypeDef(BaseValidatorModel):
    projectId: Optional[str] = None
    projectArn: Optional[str] = None

class ListResourcesRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ResourceTypeDef(BaseValidatorModel):
    id: str

class ListTagsForProjectRequestRequestTypeDef(BaseValidatorModel):
    id: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTeamMembersRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TeamMemberTypeDef(BaseValidatorModel):
    userArn: str
    projectRole: str
    remoteAccessAllowed: Optional[bool] = None

class ListUserProfilesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class UserProfileSummaryTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    displayName: Optional[str] = None
    emailAddress: Optional[str] = None
    sshPublicKey: Optional[str] = None

class TagProjectRequestRequestTypeDef(BaseValidatorModel):
    id: str
    tags: Mapping[str, str]

class UntagProjectRequestRequestTypeDef(BaseValidatorModel):
    id: str
    tags: Sequence[str]

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateTeamMemberRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    userArn: str
    projectRole: Optional[str] = None
    remoteAccessAllowed: Optional[bool] = None

class UpdateUserProfileRequestRequestTypeDef(BaseValidatorModel):
    userArn: str
    displayName: Optional[str] = None
    emailAddress: Optional[str] = None
    sshPublicKey: Optional[str] = None

class AssociateTeamMemberResultTypeDef(BaseValidatorModel):
    clientRequestToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResultTypeDef(BaseValidatorModel):
    id: str
    arn: str
    clientRequestToken: str
    projectTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserProfileResultTypeDef(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResultTypeDef(BaseValidatorModel):
    stackId: str
    projectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserProfileResultTypeDef(BaseValidatorModel):
    userArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserProfileResultTypeDef(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForProjectResultTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagProjectResultTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTeamMemberResultTypeDef(BaseValidatorModel):
    userArn: str
    projectRole: str
    remoteAccessAllowed: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserProfileResultTypeDef(BaseValidatorModel):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CodeDestinationTypeDef(BaseValidatorModel):
    codeCommit: Optional[CodeCommitCodeDestinationTypeDef] = None
    gitHub: Optional[GitHubCodeDestinationTypeDef] = None

class CodeSourceTypeDef(BaseValidatorModel):
    s3: S3LocationTypeDef

class ToolchainSourceTypeDef(BaseValidatorModel):
    s3: S3LocationTypeDef

class DescribeProjectResultTypeDef(BaseValidatorModel):
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

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesRequestListResourcesPaginateTypeDef(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTeamMembersRequestListTeamMembersPaginateTypeDef(BaseValidatorModel):
    projectId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserProfilesRequestListUserProfilesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsResultTypeDef(BaseValidatorModel):
    projects: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesResultTypeDef(BaseValidatorModel):
    resources: List[ResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTeamMembersResultTypeDef(BaseValidatorModel):
    teamMembers: List[TeamMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserProfilesResultTypeDef(BaseValidatorModel):
    userProfiles: List[UserProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CodeTypeDef(BaseValidatorModel):
    source: CodeSourceTypeDef
    destination: CodeDestinationTypeDef

class ToolchainTypeDef(BaseValidatorModel):
    source: ToolchainSourceTypeDef
    roleArn: Optional[str] = None
    stackParameters: Optional[Mapping[str, str]] = None

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
    name: str
    id: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    sourceCode: Optional[Sequence[CodeTypeDef]] = None
    toolchain: Optional[ToolchainTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

