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

class ExternalId(BaseValidatorModel):
    Issuer: str
    Id: str


class UniqueAttribute(BaseValidatorModel):
    AttributePath: str
    AttributeValue: Mapping[str, Any]


class AttributeOperation(BaseValidatorModel):
    AttributePath: str
    AttributeValue: Optional[Mapping[str, Any]] = None


class MemberId(BaseValidatorModel):
    UserId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None


class Name(BaseValidatorModel):
    Formatted: Optional[str] = None
    FamilyName: Optional[str] = None
    GivenName: Optional[str] = None
    MiddleName: Optional[str] = None
    HonorificPrefix: Optional[str] = None
    HonorificSuffix: Optional[str] = None


class DeleteGroupMembershipRequest(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str


class DeleteGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str


class DeleteUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str


class DescribeGroupMembershipRequest(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str


class DescribeGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str


class DescribeUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str


class Filter(BaseValidatorModel):
    AttributePath: str
    AttributeValue: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListGroupMembershipsRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Group(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    ExternalIds: Optional[List[ExternalId]] = None
    Description: Optional[str] = None


class AlternateIdentifier(BaseValidatorModel):
    ExternalId: Optional[ExternalId] = None
    UniqueAttribute: Optional[UniqueAttribute] = None


class UpdateGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    Operations: Sequence[AttributeOperation]


class UpdateUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str
    Operations: Sequence[AttributeOperation]


class CreateGroupMembershipRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberId


class GetGroupMembershipIdRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberId


class GroupMembershipExistenceResult(BaseValidatorModel):
    GroupId: Optional[str] = None
    MemberId: Optional[MemberId] = None
    MembershipExists: Optional[bool] = None


class GroupMembership(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: Optional[str] = None
    GroupId: Optional[str] = None
    MemberId: Optional[MemberId] = None


class IsMemberInGroupsRequest(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberId
    GroupIds: Sequence[str]


class ListGroupMembershipsForMemberRequest(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberId
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class CreateGroupMembershipResponse(BaseValidatorModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class CreateGroupResponse(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class DescribeGroupMembershipResponse(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str
    GroupId: str
    MemberId: MemberId
    ResponseMetadata: ResponseMetadata


class DescribeGroupResponse(BaseValidatorModel):
    GroupId: str
    DisplayName: str
    ExternalIds: List[ExternalId]
    Description: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class GetGroupIdResponse(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class GetGroupMembershipIdResponse(BaseValidatorModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class GetUserIdResponse(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class Address(BaseValidatorModel):
    pass


class PhoneNumber(BaseValidatorModel):
    pass


class Email(BaseValidatorModel):
    pass


class CreateUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserName: Optional[str] = None
    Name: Optional[Name] = None
    DisplayName: Optional[str] = None
    NickName: Optional[str] = None
    ProfileUrl: Optional[str] = None
    Emails: Optional[Sequence[Email]] = None
    Addresses: Optional[Sequence[Address]] = None
    PhoneNumbers: Optional[Sequence[PhoneNumber]] = None
    UserType: Optional[str] = None
    Title: Optional[str] = None
    PreferredLanguage: Optional[str] = None
    Locale: Optional[str] = None
    Timezone: Optional[str] = None


class DescribeUserResponse(BaseValidatorModel):
    UserName: str
    UserId: str
    ExternalIds: List[ExternalId]
    Name: Name
    DisplayName: str
    NickName: str
    ProfileUrl: str
    Emails: List[Email]
    Addresses: List[Address]
    PhoneNumbers: List[PhoneNumber]
    UserType: str
    Title: str
    PreferredLanguage: str
    Locale: str
    Timezone: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


class User(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    UserName: Optional[str] = None
    ExternalIds: Optional[List[ExternalId]] = None
    Name: Optional[Name] = None
    DisplayName: Optional[str] = None
    NickName: Optional[str] = None
    ProfileUrl: Optional[str] = None
    Emails: Optional[List[Email]] = None
    Addresses: Optional[List[Address]] = None
    PhoneNumbers: Optional[List[PhoneNumber]] = None
    UserType: Optional[str] = None
    Title: Optional[str] = None
    PreferredLanguage: Optional[str] = None
    Locale: Optional[str] = None
    Timezone: Optional[str] = None


class ListGroupsRequest(BaseValidatorModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None


class ListUsersRequest(BaseValidatorModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None


class ListGroupMembershipsForMemberRequestPaginate(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberId
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupMembershipsRequestPaginate(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    IdentityStoreId: str
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    IdentityStoreId: str
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsResponse(BaseValidatorModel):
    Groups: List[Group]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetGroupIdRequest(BaseValidatorModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifier


class GetUserIdRequest(BaseValidatorModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifier


class IsMemberInGroupsResponse(BaseValidatorModel):
    Results: List[GroupMembershipExistenceResult]
    ResponseMetadata: ResponseMetadata


class ListGroupMembershipsForMemberResponse(BaseValidatorModel):
    GroupMemberships: List[GroupMembership]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupMembershipsResponse(BaseValidatorModel):
    GroupMemberships: List[GroupMembership]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


