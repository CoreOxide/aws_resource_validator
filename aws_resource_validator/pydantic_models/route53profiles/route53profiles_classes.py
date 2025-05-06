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


class DeleteProfileRequest(BaseValidatorModel):
    ProfileId: str


class DisassociateProfileRequest(BaseValidatorModel):
    ProfileId: str
    ResourceId: str


class DisassociateResourceFromProfileRequest(BaseValidatorModel):
    ProfileId: str
    ResourceArn: str


class GetProfileAssociationRequest(BaseValidatorModel):
    ProfileAssociationId: str


class GetProfileRequest(BaseValidatorModel):
    ProfileId: str


class GetProfileResourceAssociationRequest(BaseValidatorModel):
    ProfileResourceAssociationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListProfileAssociationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileId: Optional[str] = None
    ResourceId: Optional[str] = None


class ListProfileResourceAssociationsRequest(BaseValidatorModel):
    ProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None


class ListProfilesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProfileSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateProfileResourceAssociationRequest(BaseValidatorModel):
    ProfileResourceAssociationId: str
    Name: Optional[str] = None
    ResourceProperties: Optional[str] = None


class AssociateProfileRequest(BaseValidatorModel):
    Name: str
    ProfileId: str
    ResourceId: str
    Tags: Optional[List[Tag]] = None


class CreateProfileRequest(BaseValidatorModel):
    ClientToken: str
    Name: str
    Tags: Optional[List[Tag]] = None


class AssociateProfileResponse(BaseValidatorModel):
    ProfileAssociation: ProfileAssociation
    ResponseMetadata: ResponseMetadata


class DisassociateProfileResponse(BaseValidatorModel):
    ProfileAssociation: ProfileAssociation
    ResponseMetadata: ResponseMetadata


class GetProfileAssociationResponse(BaseValidatorModel):
    ProfileAssociation: ProfileAssociation
    ResponseMetadata: ResponseMetadata


class ListProfileAssociationsResponse(BaseValidatorModel):
    ProfileAssociations: List[ProfileAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class AssociateResourceToProfileResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


class DisassociateResourceFromProfileResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


class GetProfileResourceAssociationResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


class ListProfileResourceAssociationsResponse(BaseValidatorModel):
    ProfileResourceAssociations: List[ProfileResourceAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateProfileResourceAssociationResponse(BaseValidatorModel):
    ProfileResourceAssociation: ProfileResourceAssociation
    ResponseMetadata: ResponseMetadata


class CreateProfileResponse(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


class DeleteProfileResponse(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


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


class ListProfilesResponse(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None