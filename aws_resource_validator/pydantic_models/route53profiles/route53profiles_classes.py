from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53profiles.route53profiles_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ProfileAssociation(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    Id: Optional[str] = None
    ModificationTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ProfileStatusType] = None
    StatusMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_resource_to_profile' function.
class AssociateResourceToProfileRequest(BaseValidatorModel):
    Name: str
    ProfileId: str
    ResourceArn: str
    ResourceProperties: Optional[str] = None


class ProfileResourceAssociation(BaseValidatorModel):
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


class Profile(BaseValidatorModel):
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


# This class is the input for the 'delete_profile' function.
class DeleteProfileRequest(BaseValidatorModel):
    ProfileId: str


# This class is the input for the 'disassociate_profile' function.
class DisassociateProfileRequest(BaseValidatorModel):
    ProfileId: str
    ResourceId: str


# This class is the input for the 'disassociate_resource_from_profile' function.
class DisassociateResourceFromProfileRequest(BaseValidatorModel):
    ProfileId: str
    ResourceArn: str


# This class is the input for the 'get_profile_association' function.
class GetProfileAssociationRequest(BaseValidatorModel):
    ProfileAssociationId: str


# This class is the input for the 'get_profile' function.
class GetProfileRequest(BaseValidatorModel):
    ProfileId: str


# This class is the input for the 'get_profile_resource_association' function.
class GetProfileResourceAssociationRequest(BaseValidatorModel):
    ProfileResourceAssociationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_profile_associations' function.
class ListProfileAssociationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None


# This class is the input for the 'list_profile_resource_associations' function.
class ListProfileResourceAssociationsRequest(BaseValidatorModel):
    ProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None


# This class is the input for the 'list_profiles' function.
class ListProfilesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProfileSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_profile_resource_association' function.
class UpdateProfileResourceAssociationRequest(BaseValidatorModel):
    ProfileResourceAssociationId: str
    Name: Optional[str] = None
    ResourceProperties: Optional[str] = None


# This class is the input for the 'associate_profile' function.
class AssociateProfileRequest(BaseValidatorModel):
    Name: str
    ProfileId: str
    ResourceId: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_profile' function.
class CreateProfileRequest(BaseValidatorModel):
    ClientToken: str
    Name: str
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'associate_profile' function.
class AssociateProfileResponse(BaseValidatorModel):
    ProfileAssociation: ProfileAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_profile' function.
class DisassociateProfileResponse(BaseValidatorModel):
    ProfileAssociation: ProfileAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_profile_association' function.
class GetProfileAssociationResponse(BaseValidatorModel):
    ProfileAssociation: ProfileAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_profile_associations' function.
class ListProfileAssociationsResponse(BaseValidatorModel):
    ProfileAssociations: List[ProfileAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_resource_to_profile' function.
class AssociateResourceToProfileResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resource_from_profile' function.
class DisassociateResourceFromProfileResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_profile_resource_association' function.
class GetProfileResourceAssociationResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_profile_resource_associations' function.
class ListProfileResourceAssociationsResponse(BaseValidatorModel):
    ProfileResourceAssociations: List[ProfileResourceAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_profile_resource_association' function.
class UpdateProfileResourceAssociationResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_profile' function.
class CreateProfileResponse(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_profile' function.
class DeleteProfileResponse(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_profile' function.
class GetProfileResponse(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


class ListProfileAssociationsRequestPaginate(BaseValidatorModel):
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProfileResourceAssociationsRequestPaginate(BaseValidatorModel):
    ProfileId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProfilesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_profiles' function.
class ListProfilesResponse(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None