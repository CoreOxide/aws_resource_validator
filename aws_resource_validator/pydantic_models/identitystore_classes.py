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
from aws_resource_validator.pydantic_models.identitystore_constants import *

class AddressTypeDef(BaseModel):
    StreetAddress: Optional[str] = None
    Locality: Optional[str] = None
    Region: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None
    Formatted: Optional[str] = None
    Type: Optional[str] = None
    Primary: Optional[bool] = None

class ExternalIdTypeDef(BaseModel):
    Issuer: str
    Id: str

class UniqueAttributeTypeDef(BaseModel):
    AttributePath: str
    AttributeValue: Mapping[str, Any]

class AttributeOperationTypeDef(BaseModel):
    AttributePath: str
    AttributeValue: Optional[Mapping[str, Any]] = None

class MemberIdTypeDef(BaseModel):
    UserId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateGroupRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None

class EmailTypeDef(BaseModel):
    Value: Optional[str] = None
    Type: Optional[str] = None
    Primary: Optional[bool] = None

class NameTypeDef(BaseModel):
    Formatted: Optional[str] = None
    FamilyName: Optional[str] = None
    GivenName: Optional[str] = None
    MiddleName: Optional[str] = None
    HonorificPrefix: Optional[str] = None
    HonorificSuffix: Optional[str] = None

class PhoneNumberTypeDef(BaseModel):
    Value: Optional[str] = None
    Type: Optional[str] = None
    Primary: Optional[bool] = None

class DeleteGroupMembershipRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    MembershipId: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    UserId: str

class DescribeGroupMembershipRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    MembershipId: str

class DescribeGroupRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str

class DescribeUserRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    UserId: str

class FilterTypeDef(BaseModel):
    AttributePath: str
    AttributeValue: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListGroupMembershipsRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GroupTypeDef(BaseModel):
    GroupId: str
    IdentityStoreId: str
    DisplayName: Optional[str] = None
    ExternalIds: Optional[List[ExternalIdTypeDef]] = None
    Description: Optional[str] = None

class AlternateIdentifierTypeDef(BaseModel):
    ExternalId: Optional[ExternalIdTypeDef] = None
    UniqueAttribute: Optional[UniqueAttributeTypeDef] = None

class UpdateGroupRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str
    Operations: Sequence[AttributeOperationTypeDef]

class UpdateUserRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    UserId: str
    Operations: Sequence[AttributeOperationTypeDef]

class CreateGroupMembershipRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberIdTypeDef

class GetGroupMembershipIdRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberIdTypeDef

class GroupMembershipExistenceResultTypeDef(BaseModel):
    GroupId: Optional[str] = None
    MemberId: Optional[MemberIdTypeDef] = None
    MembershipExists: Optional[bool] = None

class GroupMembershipTypeDef(BaseModel):
    IdentityStoreId: str
    MembershipId: Optional[str] = None
    GroupId: Optional[str] = None
    MemberId: Optional[MemberIdTypeDef] = None

class IsMemberInGroupsRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    GroupIds: Sequence[str]

class ListGroupMembershipsForMemberRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class CreateGroupMembershipResponseTypeDef(BaseModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupMembershipResponseTypeDef(BaseModel):
    IdentityStoreId: str
    MembershipId: str
    GroupId: str
    MemberId: MemberIdTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupResponseTypeDef(BaseModel):
    GroupId: str
    DisplayName: str
    ExternalIds: List[ExternalIdTypeDef]
    Description: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupIdResponseTypeDef(BaseModel):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupMembershipIdResponseTypeDef(BaseModel):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserIdResponseTypeDef(BaseModel):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestRequestTypeDef(BaseModel):
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

class DescribeUserResponseTypeDef(BaseModel):
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

class UserTypeDef(BaseModel):
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

class ListGroupsRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListGroupMembershipsForMemberRequestListGroupMembershipsForMemberPaginateTypeDef(BaseModel):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef(BaseModel):
    IdentityStoreId: str
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    IdentityStoreId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    IdentityStoreId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupIdRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifierTypeDef

class GetUserIdRequestRequestTypeDef(BaseModel):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifierTypeDef

class IsMemberInGroupsResponseTypeDef(BaseModel):
    Results: List[GroupMembershipExistenceResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupMembershipsForMemberResponseTypeDef(BaseModel):
    GroupMemberships: List[GroupMembershipTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupMembershipsResponseTypeDef(BaseModel):
    GroupMemberships: List[GroupMembershipTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

