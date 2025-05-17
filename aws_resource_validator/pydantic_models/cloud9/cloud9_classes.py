from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloud9.cloud9_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_environment_membership' function.
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


# This class is the input for the 'describe_environment_memberships' function.
class DescribeEnvironmentMembershipsRequest(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[List[PermissionsType]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'describe_environment_status' function.
class DescribeEnvironmentStatusRequest(BaseValidatorModel):
    environmentId: str


# This class is the input for the 'describe_environments' function.
class DescribeEnvironmentsRequest(BaseValidatorModel):
    environmentIds: List[str]


class EnvironmentLifecycle(BaseValidatorModel):
    status: Optional[EnvironmentLifecycleStatusType] = None
    reason: Optional[str] = None
    failureResource: Optional[str] = None


# This class is the input for the 'list_environments' function.
class ListEnvironmentsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_environment_membership' function.
class UpdateEnvironmentMembershipRequest(BaseValidatorModel):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType


class UpdateEnvironmentRequest(BaseValidatorModel):
    environmentId: str
    name: Optional[str] = None
    description: Optional[str] = None
    managedCredentialsAction: Optional[ManagedCredentialsActionType] = None


# This class is the input for the 'create_environment_ec2' function.
class CreateEnvironmentEC2Request(BaseValidatorModel):
    name: str
    instanceType: str
    imageId: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    subnetId: Optional[str] = None
    automaticStopTimeMinutes: Optional[int] = None
    ownerArn: Optional[str] = None
    tags: Optional[List[Tag]] = None
    connectionType: Optional[ConnectionTypeType] = None
    dryRun: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_environment_ec2' function.
class CreateEnvironmentEC2Result(BaseValidatorModel):
    environmentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_environment_status' function.
class DescribeEnvironmentStatusResult(BaseValidatorModel):
    status: EnvironmentStatusType
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_environments' function.
class ListEnvironmentsResult(BaseValidatorModel):
    environmentIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_environment_membership' function.
class CreateEnvironmentMembershipResult(BaseValidatorModel):
    membership: EnvironmentMember
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_environment_memberships' function.
class DescribeEnvironmentMembershipsResult(BaseValidatorModel):
    memberships: List[EnvironmentMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_environment_membership' function.
class UpdateEnvironmentMembershipResult(BaseValidatorModel):
    membership: EnvironmentMember
    ResponseMetadata: ResponseMetadata


class DescribeEnvironmentMembershipsRequestPaginate(BaseValidatorModel):
    userArn: Optional[str] = None
    environmentId: Optional[str] = None
    permissions: Optional[List[PermissionsType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class Environment(BaseValidatorModel):
    type: EnvironmentTypeType
    arn: str
    ownerArn: str
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    connectionType: Optional[ConnectionTypeType] = None
    lifecycle: Optional[EnvironmentLifecycle] = None
    managedCredentialsStatus: Optional[ManagedCredentialsStatusType] = None


# This class is the output for the 'describe_environments' function.
class DescribeEnvironmentsResult(BaseValidatorModel):
    environments: List[Environment]
    ResponseMetadata: ResponseMetadata