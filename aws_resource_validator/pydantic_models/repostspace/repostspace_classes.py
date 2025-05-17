from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.repostspace.repostspace_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'batch_add_role' function.
class BatchAddRoleInput(BaseValidatorModel):
    accessorIds: List[str]
    role: RoleType
    spaceId: str


class BatchError(BaseValidatorModel):
    accessorId: str
    error: int
    message: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'batch_remove_role' function.
class BatchRemoveRoleInput(BaseValidatorModel):
    accessorIds: List[str]
    role: RoleType
    spaceId: str


# This class is the input for the 'create_space' function.
class CreateSpaceInput(BaseValidatorModel):
    name: str
    subdomain: str
    tier: TierLevelType
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    userKMSKey: Optional[str] = None


# This class is the input for the 'delete_space' function.
class DeleteSpaceInput(BaseValidatorModel):
    spaceId: str


# This class is the input for the 'deregister_admin' function.
class DeregisterAdminInput(BaseValidatorModel):
    adminId: str
    spaceId: str


# This class is the input for the 'get_space' function.
class GetSpaceInput(BaseValidatorModel):
    spaceId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_spaces' function.
class ListSpacesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SpaceData(BaseValidatorModel):
    arn: str
    configurationStatus: ConfigurationStatusType
    createDateTime: datetime
    name: str
    randomDomain: str
    spaceId: str
    status: str
    storageLimit: int
    tier: TierLevelType
    vanityDomain: str
    vanityDomainStatus: VanityDomainStatusType
    contentSize: Optional[int] = None
    deleteDateTime: Optional[datetime] = None
    description: Optional[str] = None
    userCount: Optional[int] = None
    userKMSKey: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'register_admin' function.
class RegisterAdminInput(BaseValidatorModel):
    adminId: str
    spaceId: str


# This class is the input for the 'send_invites' function.
class SendInvitesInput(BaseValidatorModel):
    accessorIds: List[str]
    body: str
    spaceId: str
    title: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_space' function.
class UpdateSpaceInput(BaseValidatorModel):
    spaceId: str
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tier: Optional[TierLevelType] = None


# This class is the output for the 'batch_add_role' function.
class BatchAddRoleOutput(BaseValidatorModel):
    addedAccessorIds: List[str]
    errors: List[BatchError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_remove_role' function.
class BatchRemoveRoleOutput(BaseValidatorModel):
    errors: List[BatchError]
    removedAccessorIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_space' function.
class CreateSpaceOutput(BaseValidatorModel):
    spaceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_space' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_space' function.
class GetSpaceOutput(BaseValidatorModel):
    arn: str
    clientId: str
    configurationStatus: ConfigurationStatusType
    contentSize: int
    createDateTime: datetime
    customerRoleArn: str
    deleteDateTime: datetime
    description: str
    groupAdmins: List[str]
    name: str
    randomDomain: str
    roles: Dict[str, List[RoleType]]
    spaceId: str
    status: str
    storageLimit: int
    tier: TierLevelType
    userAdmins: List[str]
    userCount: int
    userKMSKey: str
    vanityDomain: str
    vanityDomainStatus: VanityDomainStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListSpacesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_spaces' function.
class ListSpacesOutput(BaseValidatorModel):
    spaces: List[SpaceData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None