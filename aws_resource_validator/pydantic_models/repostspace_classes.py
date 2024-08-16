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
from aws_resource_validator.pydantic_models.repostspace_constants import *

class CreateSpaceInputRequestTypeDef(BaseValidatorModel):
    name: str
    subdomain: str
    tier: TierLevelType
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    userKMSKey: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteSpaceInputRequestTypeDef(BaseValidatorModel):
    spaceId: str

class DeregisterAdminInputRequestTypeDef(BaseValidatorModel):
    adminId: str
    spaceId: str

class GetSpaceInputRequestTypeDef(BaseValidatorModel):
    spaceId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSpacesInputRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class RegisterAdminInputRequestTypeDef(BaseValidatorModel):
    adminId: str
    spaceId: str

class SendInvitesInputRequestTypeDef(BaseValidatorModel):
    accessorIds: Sequence[str]
    body: str
    spaceId: str
    title: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateSpaceInputRequestTypeDef(BaseValidatorModel):
    spaceId: str
    description: Optional[str] = None
    roleArn: Optional[str] = None
    tier: Optional[TierLevelType] = None

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

class ListSpacesInputListSpacesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpacesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    spaces: List[SpaceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

