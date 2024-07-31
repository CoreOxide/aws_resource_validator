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
from aws_resource_validator.pydantic_models.route53profiles_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ProfileAssociationTypeDef(BaseModel):
    CreationTime: Optional[datetime] = None
    Id: Optional[str] = None
    ModificationTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ProfileStatusType] = None
    StatusMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociateResourceToProfileRequestRequestTypeDef(BaseModel):
    Name: str
    ProfileId: str
    ResourceArn: str
    ResourceProperties: Optional[str] = None

class ProfileResourceAssociationTypeDef(BaseModel):
    CreationTime: Optional[datetime] = None
    Id: Optional[str] = None
    ModificationTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceProperties: Optional[str] = None
    ResourceType: Optional[str] = None
    Status: Optional[ProfileStatusType] = None
    StatusMessage: Optional[str] = None

class ProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Id: Optional[str] = None
    ModificationTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    Status: Optional[ProfileStatusType] = None
    StatusMessage: Optional[str] = None

class DeleteProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str

class DisassociateProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str
    ResourceId: str

class DisassociateResourceFromProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str
    ResourceArn: str

class GetProfileAssociationRequestRequestTypeDef(BaseModel):
    ProfileAssociationId: str

class GetProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str

class GetProfileResourceAssociationRequestRequestTypeDef(BaseModel):
    ProfileResourceAssociationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListProfileAssociationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None

class ListProfileResourceAssociationsRequestRequestTypeDef(BaseModel):
    ProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None

class ListProfilesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProfileSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateProfileResourceAssociationRequestRequestTypeDef(BaseModel):
    ProfileResourceAssociationId: str
    Name: Optional[str] = None
    ResourceProperties: Optional[str] = None

class AssociateProfileRequestRequestTypeDef(BaseModel):
    Name: str
    ProfileId: str
    ResourceId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateProfileRequestRequestTypeDef(BaseModel):
    ClientToken: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class AssociateProfileResponseTypeDef(BaseModel):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateProfileResponseTypeDef(BaseModel):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileAssociationResponseTypeDef(BaseModel):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileAssociationsResponseTypeDef(BaseModel):
    ProfileAssociations: List[ProfileAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceToProfileResponseTypeDef(BaseModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceFromProfileResponseTypeDef(BaseModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResourceAssociationResponseTypeDef(BaseModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileResourceAssociationsResponseTypeDef(BaseModel):
    ProfileResourceAssociations: List[ProfileResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateProfileResourceAssociationResponseTypeDef(BaseModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(BaseModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileResponseTypeDef(BaseModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResponseTypeDef(BaseModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileAssociationsRequestListProfileAssociationsPaginateTypeDef(BaseModel):
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfileResourceAssociationsRequestListProfileResourceAssociationsPaginateTypeDef(BaseModel):
    ProfileId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesRequestListProfilesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesResponseTypeDef(BaseModel):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

