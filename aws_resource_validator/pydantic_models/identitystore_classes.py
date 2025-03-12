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
from aws_resource_validator.pydantic_models.identitystore_constants import *

class ExternalIdTypeDef(BaseValidatorModel):
    Issuer: str
    Id: str


class UniqueAttributeTypeDef(BaseValidatorModel):
    AttributePath: str
    AttributeValue: Mapping[str, Any]


class AttributeOperationTypeDef(BaseValidatorModel):
    AttributePath: str
    AttributeValue: Optional[Mapping[str, Any]] = None


class MemberIdTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateGroupRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None


class NameTypeDef(BaseValidatorModel):
    Formatted: Optional[str] = None
    FamilyName: Optional[str] = None
    GivenName: Optional[str] = None
    MiddleName: Optional[str] = None
    HonorificPrefix: Optional[str] = None
    HonorificSuffix: Optional[str] = None


class DeleteGroupMembershipRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str


class DescribeGroupMembershipRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str


class DescribeGroupRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str


class DescribeUserRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str


class FilterTypeDef(BaseValidatorModel):
    AttributePath: str
    AttributeValue: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListGroupMembershipsRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GroupTypeDef(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    ExternalIds: Optional[List[ExternalIdTypeDef]] = None
    Description: Optional[str] = None


class AlternateIdentifierTypeDef(BaseValidatorModel):
    ExternalId: Optional[ExternalIdTypeDef] = None
    UniqueAttribute: Optional[UniqueAttributeTypeDef] = None


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    Operations: Sequence[AttributeOperationTypeDef]


class UpdateUserRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str
    Operations: Sequence[AttributeOperationTypeDef]


class CreateGroupMembershipRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberIdTypeDef


class GetGroupMembershipIdRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberIdTypeDef


class GroupMembershipExistenceResultTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    MemberId: Optional[MemberIdTypeDef] = None
    MembershipExists: Optional[bool] = None


class GroupMembershipTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: Optional[str] = None
    GroupId: Optional[str] = None
    MemberId: Optional[MemberIdTypeDef] = None


class IsMemberInGroupsRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    GroupIds: Sequence[str]


class ListGroupMembershipsForMemberRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class CreateGroupMembershipResponseTypeDef(BaseValidatorModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGroupResponseTypeDef(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserResponseTypeDef(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGroupMembershipResponseTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str
    GroupId: str
    MemberId: MemberIdTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGroupResponseTypeDef(BaseValidatorModel):
    GroupId: str
    DisplayName: str
    ExternalIds: List[ExternalIdTypeDef]
    Description: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupIdResponseTypeDef(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupMembershipIdResponseTypeDef(BaseValidatorModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserIdResponseTypeDef(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddressTypeDef(BaseValidatorModel):
    pass


class PhoneNumberTypeDef(BaseValidatorModel):
    pass


class EmailTypeDef(BaseValidatorModel):
    pass


class CreateUserRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    UserName: Optional[str] = None
    Name: Optional[NameTypeDef] = None
    DisplayName: Optional[str] = None
    NickName: Optional[str] = None
    ProfileUrl: Optional[str] = None
    Emails: Optional[Sequence[EmailTypeDef]] = None
    Addresses: Optional[Sequence[AddressTypeDef]] = None
    PhoneNumbers: Optional[Sequence[PhoneNumberTypeDef]] = None
    UserType: Optional[str] = None
    Title: Optional[str] = None
    PreferredLanguage: Optional[str] = None
    Locale: Optional[str] = None
    Timezone: Optional[str] = None


class DescribeUserResponseTypeDef(BaseValidatorModel):
    UserName: str
    UserId: str
    ExternalIds: List[ExternalIdTypeDef]
    Name: NameTypeDef
    DisplayName: str
    NickName: str
    ProfileUrl: str
    Emails: List[EmailTypeDef]
    Addresses: List[AddressTypeDef]
    PhoneNumbers: List[PhoneNumberTypeDef]
    UserType: str
    Title: str
    PreferredLanguage: str
    Locale: str
    Timezone: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UserTypeDef(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    UserName: Optional[str] = None
    ExternalIds: Optional[List[ExternalIdTypeDef]] = None
    Name: Optional[NameTypeDef] = None
    DisplayName: Optional[str] = None
    NickName: Optional[str] = None
    ProfileUrl: Optional[str] = None
    Emails: Optional[List[EmailTypeDef]] = None
    Addresses: Optional[List[AddressTypeDef]] = None
    PhoneNumbers: Optional[List[PhoneNumberTypeDef]] = None
    UserType: Optional[str] = None
    Title: Optional[str] = None
    PreferredLanguage: Optional[str] = None
    Locale: Optional[str] = None
    Timezone: Optional[str] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListGroupMembershipsForMemberRequestPaginateTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupMembershipsRequestPaginateTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetGroupIdRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifierTypeDef


class GetUserIdRequestTypeDef(BaseValidatorModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifierTypeDef


class IsMemberInGroupsResponseTypeDef(BaseValidatorModel):
    Results: List[GroupMembershipExistenceResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListGroupMembershipsForMemberResponseTypeDef(BaseValidatorModel):
    GroupMemberships: List[GroupMembershipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupMembershipsResponseTypeDef(BaseValidatorModel):
    GroupMemberships: List[GroupMembershipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


