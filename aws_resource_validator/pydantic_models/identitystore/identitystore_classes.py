from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.identitystore.identitystore_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Address(BaseValidatorModel):
    StreetAddress: Optional[str] = None
    Locality: Optional[str] = None
    Region: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None
    Formatted: Optional[str] = None
    Type: Optional[str] = None
    Primary: Optional[bool] = None


class ExternalId(BaseValidatorModel):
    Issuer: str
    Id: str


class UniqueAttribute(BaseValidatorModel):
    AttributePath: str
    AttributeValue: Dict[str, Any]


class AttributeOperation(BaseValidatorModel):
    AttributePath: str
    AttributeValue: Optional[Dict[str, Any]] = None


class MemberId(BaseValidatorModel):
    UserId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_group' function.
class CreateGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None


class Email(BaseValidatorModel):
    Value: Optional[str] = None
    Type: Optional[str] = None
    Primary: Optional[bool] = None


class Name(BaseValidatorModel):
    Formatted: Optional[str] = None
    FamilyName: Optional[str] = None
    GivenName: Optional[str] = None
    MiddleName: Optional[str] = None
    HonorificPrefix: Optional[str] = None
    HonorificSuffix: Optional[str] = None


class PhoneNumber(BaseValidatorModel):
    Value: Optional[str] = None
    Type: Optional[str] = None
    Primary: Optional[bool] = None


class DeleteGroupMembershipRequest(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str


class DeleteGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str


class DeleteUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str


# This class is the input for the 'describe_group_membership' function.
class DescribeGroupMembershipRequest(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str


# This class is the input for the 'describe_group' function.
class DescribeGroupRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str


# This class is the input for the 'describe_user' function.
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


# This class is the input for the 'list_group_memberships' function.
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
    Operations: List[AttributeOperation]


class UpdateUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserId: str
    Operations: List[AttributeOperation]


# This class is the input for the 'create_group_membership' function.
class CreateGroupMembershipRequest(BaseValidatorModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberId


# This class is the input for the 'get_group_membership_id' function.
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


# This class is the input for the 'is_member_in_groups' function.
class IsMemberInGroupsRequest(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberId
    GroupIds: List[str]


# This class is the input for the 'list_group_memberships_for_member' function.
class ListGroupMembershipsForMemberRequest(BaseValidatorModel):
    IdentityStoreId: str
    MemberId: MemberId
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'create_group_membership' function.
class CreateGroupMembershipResponse(BaseValidatorModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_group' function.
class CreateGroupResponse(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_group_membership' function.
class DescribeGroupMembershipResponse(BaseValidatorModel):
    IdentityStoreId: str
    MembershipId: str
    GroupId: str
    MemberId: MemberId
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_group' function.
class DescribeGroupResponse(BaseValidatorModel):
    GroupId: str
    DisplayName: str
    ExternalIds: List[ExternalId]
    Description: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group_id' function.
class GetGroupIdResponse(BaseValidatorModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group_membership_id' function.
class GetGroupMembershipIdResponse(BaseValidatorModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user_id' function.
class GetUserIdResponse(BaseValidatorModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    IdentityStoreId: str
    UserName: Optional[str] = None
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


# This class is the output for the 'describe_user' function.
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


# This class is the input for the 'list_groups' function.
class ListGroupsRequest(BaseValidatorModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_users' function.
class ListUsersRequest(BaseValidatorModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


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
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    IdentityStoreId: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_groups' function.
class ListGroupsResponse(BaseValidatorModel):
    Groups: List[Group]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'get_group_id' function.
class GetGroupIdRequest(BaseValidatorModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifier


# This class is the input for the 'get_user_id' function.
class GetUserIdRequest(BaseValidatorModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifier


# This class is the output for the 'is_member_in_groups' function.
class IsMemberInGroupsResponse(BaseValidatorModel):
    Results: List[GroupMembershipExistenceResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_group_memberships_for_member' function.
class ListGroupMembershipsForMemberResponse(BaseValidatorModel):
    GroupMemberships: List[GroupMembership]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_group_memberships' function.
class ListGroupMembershipsResponse(BaseValidatorModel):
    GroupMemberships: List[GroupMembership]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_users' function.
class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None