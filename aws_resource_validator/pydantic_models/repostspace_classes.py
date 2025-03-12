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

class BatchAddRoleInputTypeDef(BaseValidatorModel):
    accessorIds: Sequence[str]
    role: RoleType
    spaceId: str


class BatchErrorTypeDef(BaseValidatorModel):
    accessorId: str
    error: int
    message: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchRemoveRoleInputTypeDef(BaseValidatorModel):
    accessorIds: Sequence[str]
    role: RoleType
    spaceId: str


class CreateSpaceInputTypeDef(BaseValidatorModel):
    name: str
    subdomain: str
    tier: TierLevelType
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    userKMSKey: Optional[str] = None


class DeleteSpaceInputTypeDef(BaseValidatorModel):
    spaceId: str


class DeregisterAdminInputTypeDef(BaseValidatorModel):
    adminId: str
    spaceId: str


class GetSpaceInputTypeDef(BaseValidatorModel):
    spaceId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSpacesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SpaceDataTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class RegisterAdminInputTypeDef(BaseValidatorModel):
    adminId: str
    spaceId: str


class SendInvitesInputTypeDef(BaseValidatorModel):
    accessorIds: Sequence[str]
    body: str
    spaceId: str
    title: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateSpaceInputTypeDef(BaseValidatorModel):
    spaceId: str
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tier: Optional[TierLevelType] = None


class BatchAddRoleOutputTypeDef(BaseValidatorModel):
    addedAccessorIds: List[str]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchRemoveRoleOutputTypeDef(BaseValidatorModel):
    errors: List[BatchErrorTypeDef]
    removedAccessorIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSpaceOutputTypeDef(BaseValidatorModel):
    spaceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetSpaceOutputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListSpacesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSpacesOutputTypeDef(BaseValidatorModel):
    spaces: List[SpaceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


