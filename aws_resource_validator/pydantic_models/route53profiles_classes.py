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
from aws_resource_validator.pydantic_models.route53profiles_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ProfileAssociationTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    Id: Optional[str] = None
    ModificationTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ProfileStatusType] = None
    StatusMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociateResourceToProfileRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ProfileId: str
    ResourceArn: str
    ResourceProperties: Optional[str] = None

class ProfileResourceAssociationTypeDef(BaseValidatorModel):
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

class ProfileTypeDef(BaseValidatorModel):
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

class DeleteProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str

class DisassociateProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    ResourceId: str

class DisassociateResourceFromProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    ResourceArn: str

class GetProfileAssociationRequestRequestTypeDef(BaseValidatorModel):
    ProfileAssociationId: str

class GetProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str

class GetProfileResourceAssociationRequestRequestTypeDef(BaseValidatorModel):
    ProfileResourceAssociationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListProfileAssociationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None

class ListProfileResourceAssociationsRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None

class ListProfilesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProfileSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateProfileResourceAssociationRequestRequestTypeDef(BaseValidatorModel):
    ProfileResourceAssociationId: str
    Name: Optional[str] = None
    ResourceProperties: Optional[str] = None

class AssociateProfileRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ProfileId: str
    ResourceId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateProfileRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class AssociateProfileResponseTypeDef(BaseValidatorModel):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateProfileResponseTypeDef(BaseValidatorModel):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileAssociationResponseTypeDef(BaseValidatorModel):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileAssociationsResponseTypeDef(BaseValidatorModel):
    ProfileAssociations: List[ProfileAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceToProfileResponseTypeDef(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceFromProfileResponseTypeDef(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResourceAssociationResponseTypeDef(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileResourceAssociationsResponseTypeDef(BaseValidatorModel):
    ProfileResourceAssociations: List[ProfileResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateProfileResourceAssociationResponseTypeDef(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(BaseValidatorModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileResponseTypeDef(BaseValidatorModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResponseTypeDef(BaseValidatorModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileAssociationsRequestListProfileAssociationsPaginateTypeDef(BaseValidatorModel):
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfileResourceAssociationsRequestListProfileResourceAssociationsPaginateTypeDef(BaseValidatorModel):
    ProfileId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesRequestListProfilesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesResponseTypeDef(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

