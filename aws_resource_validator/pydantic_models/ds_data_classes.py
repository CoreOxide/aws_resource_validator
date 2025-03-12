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
from aws_resource_validator.pydantic_models.ds_data_constants import *

class AddGroupMemberRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    GroupName: str
    MemberName: str
    ClientToken: Optional[str] = None
    MemberRealm: Optional[str] = None


class AttributeValueOutputTypeDef(BaseValidatorModel):
    BOOL: Optional[bool] = None
    N: Optional[int] = None
    S: Optional[str] = None
    SS: Optional[List[str]] = None


class AttributeValueTypeDef(BaseValidatorModel):
    BOOL: Optional[bool] = None
    N: Optional[int] = None
    S: Optional[str] = None
    SS: Optional[Sequence[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None


class DeleteUserRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None


class DescribeGroupRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    OtherAttributes: Optional[Sequence[str]] = None
    Realm: Optional[str] = None


class DescribeUserRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    OtherAttributes: Optional[Sequence[str]] = None
    Realm: Optional[str] = None


class DisableUserRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None


class GroupSummaryTypeDef(BaseValidatorModel):
    GroupScope: GroupScopeType
    GroupType: GroupTypeType
    SAMAccountName: str
    SID: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListGroupMembersRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MaxResults: Optional[int] = None
    MemberRealm: Optional[str] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class MemberTypeDef(BaseValidatorModel):
    MemberType: MemberTypeType
    SAMAccountName: str
    SID: str


class ListGroupsForMemberRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MaxResults: Optional[int] = None
    MemberRealm: Optional[str] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class UserSummaryTypeDef(BaseValidatorModel):
    Enabled: bool
    SAMAccountName: str
    SID: str
    GivenName: Optional[str] = None
    Surname: Optional[str] = None


class RemoveGroupMemberRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    GroupName: str
    MemberName: str
    ClientToken: Optional[str] = None
    MemberRealm: Optional[str] = None


class SearchGroupsRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class SearchUsersRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Realm: Optional[str] = None


class GroupTypeDef(BaseValidatorModel):
    SAMAccountName: str
    DistinguishedName: Optional[str] = None
    GroupScope: Optional[GroupScopeType] = None
    GroupType: Optional[GroupTypeType] = None
    OtherAttributes: Optional[Dict[str, AttributeValueOutputTypeDef]] = None
    SID: Optional[str] = None


class UserTypeDef(BaseValidatorModel):
    SAMAccountName: str
    DistinguishedName: Optional[str] = None
    EmailAddress: Optional[str] = None
    Enabled: Optional[bool] = None
    GivenName: Optional[str] = None
    OtherAttributes: Optional[Dict[str, AttributeValueOutputTypeDef]] = None
    SID: Optional[str] = None
    Surname: Optional[str] = None
    UserPrincipalName: Optional[str] = None


class CreateGroupResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGroupResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    DistinguishedName: str
    GroupScope: GroupScopeType
    GroupType: GroupTypeType
    OtherAttributes: Dict[str, AttributeValueOutputTypeDef]
    Realm: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    DistinguishedName: str
    EmailAddress: str
    Enabled: bool
    GivenName: str
    OtherAttributes: Dict[str, AttributeValueOutputTypeDef]
    Realm: str
    SAMAccountName: str
    SID: str
    Surname: str
    UserPrincipalName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListGroupsForMemberResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    Groups: List[GroupSummaryTypeDef]
    MemberRealm: str
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupsResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    Groups: List[GroupSummaryTypeDef]
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupMembersRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MemberRealm: Optional[str] = None
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsForMemberRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    MemberRealm: Optional[str] = None
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchGroupsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchUsersRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    Realm: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupMembersResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    MemberRealm: str
    Members: List[MemberTypeDef]
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUsersResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    Realm: str
    Users: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchGroupsResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    Groups: List[GroupTypeDef]
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchUsersResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    Realm: str
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class CreateGroupRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    GroupScope: Optional[GroupScopeType] = None
    GroupType: Optional[GroupTypeType] = None
    OtherAttributes: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    EmailAddress: Optional[str] = None
    GivenName: Optional[str] = None
    OtherAttributes: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None
    Surname: Optional[str] = None


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    GroupScope: Optional[GroupScopeType] = None
    GroupType: Optional[GroupTypeType] = None
    OtherAttributes: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None
    UpdateType: Optional[UpdateTypeType] = None


class UpdateUserRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: Optional[str] = None
    EmailAddress: Optional[str] = None
    GivenName: Optional[str] = None
    OtherAttributes: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None
    Surname: Optional[str] = None
    UpdateType: Optional[UpdateTypeType] = None


