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


class AssociateResourceToProfileRequestTypeDef(BaseValidatorModel):
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


class DeleteProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str


class DisassociateProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    ResourceId: str


class DisassociateResourceFromProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    ResourceArn: str


class GetProfileAssociationRequestTypeDef(BaseValidatorModel):
    ProfileAssociationId: str


class GetProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str


class GetProfileResourceAssociationRequestTypeDef(BaseValidatorModel):
    ProfileResourceAssociationId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListProfileAssociationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None


class ListProfileResourceAssociationsRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None


class ListProfilesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProfileSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateProfileResourceAssociationRequestTypeDef(BaseValidatorModel):
    ProfileResourceAssociationId: str
    Name: Optional[str] = None
    ResourceProperties: Optional[str] = None


class AssociateProfileRequestTypeDef(BaseValidatorModel):
    Name: str
    ProfileId: str
    ResourceId: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateProfileRequestTypeDef(BaseValidatorModel):
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


class ListProfileAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfileResourceAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    ProfileId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfilesResponseTypeDef(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


