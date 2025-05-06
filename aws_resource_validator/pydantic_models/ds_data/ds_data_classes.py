from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ds_data.ds_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddGroupMemberRequest(BaseValidatorModel):
    DirectoryId: str
    GroupName: str
    MemberName: str
    ClientToken: Optional[str] = None
    MemberRealm: Optional[str] = None


class AttributeValueOutput(BaseValidatorModel):
    BOOL: Optional[bool] = None
    N: Optional[int] = None
    S: Optional[str] = None
    SS: Optional[List[str]] = None


class AttributeValue(BaseValidatorModel):
    BOOL: Optional[bool] = None
    N: Optional[int] = None
    S: Optional[str] = None
    SS: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteGroupRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None


class DeleteUserRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None


class DescribeGroupRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    OtherAttributes: Optional[List[str]] = None
    Realm: Optional[str] = None


class DescribeUserRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    OtherAttributes: Optional[List[str]] = None
    Realm: Optional[str] = None


class DisableUserRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None


class GroupSummary(BaseValidatorModel):
    GroupScope: GroupScopeType
    GroupType: GroupTypeType
    SAMAccountName: str
    SID: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListGroupMembersRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MaxResults: Optional[int] = None
    MemberRealm: Optional[str] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class Member(BaseValidatorModel):
    MemberType: MemberTypeType
    SAMAccountName: str
    SID: str


class ListGroupsForMemberRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MaxResults: Optional[int] = None
    MemberRealm: Optional[str] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class ListGroupsRequest(BaseValidatorModel):
    DirectoryId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class ListUsersRequest(BaseValidatorModel):
    DirectoryId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class UserSummary(BaseValidatorModel):
    Enabled: bool
    SAMAccountName: str
    SID: str
    GivenName: Optional[str] = None
    Surname: Optional[str] = None


class RemoveGroupMemberRequest(BaseValidatorModel):
    DirectoryId: str
    GroupName: str
    MemberName: str
    ClientToken: Optional[str] = None
    MemberRealm: Optional[str] = None


class SearchGroupsRequest(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: List[str]
    SearchString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class SearchUsersRequest(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: List[str]
    SearchString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class Group(BaseValidatorModel):
    SAMAccountName: str
    DistinguishedName: Optional[str] = None
    GroupScope: Optional[GroupScopeType] = None
    GroupType: Optional[GroupTypeType] = None
    OtherAttributes: Optional[Dict[str, AttributeValueOutput]] = None
    SID: Optional[str] = None


class User(BaseValidatorModel):
    SAMAccountName: str
    DistinguishedName: Optional[str] = None
    EmailAddress: Optional[str] = None
    Enabled: Optional[bool] = None
    GivenName: Optional[str] = None
    OtherAttributes: Optional[Dict[str, AttributeValueOutput]] = None
    SID: Optional[str] = None
    Surname: Optional[str] = None
    UserPrincipalName: Optional[str] = None

AttributeValueUnion = Union[AttributeValue, AttributeValueOutput]


class CreateGroupResult(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadata


class CreateUserResult(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadata


class DescribeGroupResult(BaseValidatorModel):
    DirectoryId: str
    DistinguishedName: str
    GroupScope: GroupScopeType
    GroupType: GroupTypeType
    OtherAttributes: Dict[str, AttributeValueOutput]
    Realm: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadata


class DescribeUserResult(BaseValidatorModel):
    DirectoryId: str
    DistinguishedName: str
    EmailAddress: str
    Enabled: bool
    GivenName: str
    OtherAttributes: Dict[str, AttributeValueOutput]
    Realm: str
    SAMAccountName: str
    SID: str
    Surname: str
    UserPrincipalName: str
    ResponseMetadata: ResponseMetadata


class ListGroupsForMemberResult(BaseValidatorModel):
    DirectoryId: str
    Groups: List[GroupSummary]
    MemberRealm: str
    Realm: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsResult(BaseValidatorModel):
    DirectoryId: str
    Groups: List[GroupSummary]
    Realm: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupMembersRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MemberRealm: Optional[str] = None
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsForMemberRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MemberRealm: Optional[str] = None
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchGroupsRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: List[str]
    SearchString: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchUsersRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: List[str]
    SearchString: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupMembersResult(BaseValidatorModel):
    DirectoryId: str
    MemberRealm: str
    Members: List[Member]
    Realm: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsersResult(BaseValidatorModel):
    DirectoryId: str
    Realm: str
    Users: List[UserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchGroupsResult(BaseValidatorModel):
    DirectoryId: str
    Groups: List[Group]
    Realm: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchUsersResult(BaseValidatorModel):
    DirectoryId: str
    Realm: str
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateGroupRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    GroupScope: Optional[GroupScopeType] = None
    GroupType: Optional[GroupTypeType] = None
    OtherAttributes: Optional[Dict[str, AttributeValueUnion]] = None


class CreateUserRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    EmailAddress: Optional[str] = None
    GivenName: Optional[str] = None
    OtherAttributes: Optional[Dict[str, AttributeValueUnion]] = None
    Surname: Optional[str] = None


class UpdateGroupRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    GroupScope: Optional[GroupScopeType] = None
    GroupType: Optional[GroupTypeType] = None
    OtherAttributes: Optional[Dict[str, AttributeValueUnion]] = None
    UpdateType: Optional[UpdateTypeType] = None


class UpdateUserRequest(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    EmailAddress: Optional[str] = None
    GivenName: Optional[str] = None
    OtherAttributes: Optional[Dict[str, AttributeValueUnion]] = None
    Surname: Optional[str] = None
    UpdateType: Optional[UpdateTypeType] = None