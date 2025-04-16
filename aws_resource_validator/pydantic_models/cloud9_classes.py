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
from aws_resource_validator.pydantic_models.cloud9_constants import *

class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateEnvironmentMembershipRequest(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType


class EnvironmentMember(BaseValidatorModel):
    permissions: PermissionsType
    userId: str
    userArn: str
    environmentId: str
    lastAccess: Optional[datetime] = None


class DeleteEnvironmentMembershipRequest(BaseValidatorModel):
    environmentId: str
    userArn: str


class DeleteEnvironmentRequest(BaseValidatorModel):
    environmentId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEnvironmentMembershipsRequest(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeEnvironmentStatusRequest(BaseValidatorModel):
    environmentId: str


class DescribeEnvironmentsRequest(BaseValidatorModel):
    environmentIds: Sequence[str]


class EnvironmentLifecycle(BaseValidatorModel):
    status: Optional[EnvironmentLifecycleStatusType] = None
    reason: Optional[str] = None
    failureResource: Optional[str] = None


class ListEnvironmentsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateEnvironmentMembershipRequest(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType


class UpdateEnvironmentRequest(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    managedCredentialsAction: Optional[ManagedCredentialsActionType] = None


class CreateEnvironmentEC2Request(BaseValidatorModel):
    name: str
    instanceType: str
    imageId: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    subnetId: Optional[str] = None
    automaticStopTimeMinutes: Optional[int] = None
    ownerArn: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    connectionType: Optional[ConnectionTypeType] = None
    dryRun: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateEnvironmentEC2Result(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadata


class DescribeEnvironmentStatusResult(BaseValidatorModel):
    status: EnvironmentStatusType
    message: str
    ResponseMetadata: ResponseMetadata


class ListEnvironmentsResult(BaseValidatorModel):
    environmentIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentMembershipResult(BaseValidatorModel):
    membership: EnvironmentMember
    ResponseMetadata: ResponseMetadata


class DescribeEnvironmentMembershipsResult(BaseValidatorModel):
    memberships: List[EnvironmentMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateEnvironmentMembershipResult(BaseValidatorModel):
    membership: EnvironmentMember
    ResponseMetadata: ResponseMetadata


class DescribeEnvironmentMembershipsRequestPaginate(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[Sequence[PermissionsType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class Environment(BaseValidatorModel):
    pass


class DescribeEnvironmentsResult(BaseValidatorModel):
    environments: List[Environment]
    ResponseMetadata: ResponseMetadata


