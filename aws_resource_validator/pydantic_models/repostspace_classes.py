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
from aws_resource_validator.pydantic_models.repostspace_constants import *

class BatchAddRoleInput(BaseValidatorModel):
    accessorIds: Sequence[str]
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


class BatchRemoveRoleInput(BaseValidatorModel):
    accessorIds: Sequence[str]
    role: RoleType
    spaceId: str


class CreateSpaceInput(BaseValidatorModel):
    name: str
    subdomain: str
    tier: TierLevelType
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    userKMSKey: Optional[str] = None


class DeleteSpaceInput(BaseValidatorModel):
    spaceId: str


class DeregisterAdminInput(BaseValidatorModel):
    adminId: str
    spaceId: str


class GetSpaceInput(BaseValidatorModel):
    spaceId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterAdminInput(BaseValidatorModel):
    adminId: str
    spaceId: str


class SendInvitesInput(BaseValidatorModel):
    accessorIds: Sequence[str]
    body: str
    spaceId: str
    title: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateSpaceInput(BaseValidatorModel):
    spaceId: str
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tier: Optional[TierLevelType] = None


class BatchAddRoleOutput(BaseValidatorModel):
    addedAccessorIds: List[str]
    errors: List[BatchError]
    ResponseMetadata: ResponseMetadata


class BatchRemoveRoleOutput(BaseValidatorModel):
    errors: List[BatchError]
    removedAccessorIds: List[str]
    ResponseMetadata: ResponseMetadata


class CreateSpaceOutput(BaseValidatorModel):
    spaceId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


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


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListSpacesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSpacesOutput(BaseValidatorModel):
    spaces: List[SpaceData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


