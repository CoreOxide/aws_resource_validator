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
from aws_resource_validator.pydantic_models.repostspace_constants import *

class CreateSpaceInputRequestTypeDef(BaseModel):
    name: str
    subdomain: str
    tier: TierLevelType
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    userKMSKey: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteSpaceInputRequestTypeDef(BaseModel):
    spaceId: str

class DeregisterAdminInputRequestTypeDef(BaseModel):
    adminId: str
    spaceId: str

class GetSpaceInputRequestTypeDef(BaseModel):
    spaceId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSpacesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SpaceDataTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RegisterAdminInputRequestTypeDef(BaseModel):
    adminId: str
    spaceId: str

class SendInvitesInputRequestTypeDef(BaseModel):
    accessorIds: Sequence[str]
    body: str
    spaceId: str
    title: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateSpaceInputRequestTypeDef(BaseModel):
    spaceId: str
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tier: Optional[TierLevelType] = None

class CreateSpaceOutputTypeDef(BaseModel):
    spaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpaceOutputTypeDef(BaseModel):
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpacesInputListSpacesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpacesOutputTypeDef(BaseModel):
    nextToken: str
    spaces: List[SpaceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

