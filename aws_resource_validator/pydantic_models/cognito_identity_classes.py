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
from aws_resource_validator.pydantic_models.cognito_identity_constants import *

class CognitoIdentityProviderTypeDef(BaseModel):
    ProviderName: Optional[str] = None
    ClientId: Optional[str] = None
    ServerSideTokenCheck: Optional[bool] = None

class CredentialsTypeDef(BaseModel):
    AccessKeyId: Optional[str] = None
    SecretKey: Optional[str] = None
    SessionToken: Optional[str] = None
    Expiration: Optional[datetime] = None

class DeleteIdentitiesInputRequestTypeDef(BaseModel):
    IdentityIdsToDelete: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedIdentityIdTypeDef(BaseModel):
    IdentityId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None

class DeleteIdentityPoolInputRequestTypeDef(BaseModel):
    IdentityPoolId: str

class DescribeIdentityInputRequestTypeDef(BaseModel):
    IdentityId: str

class DescribeIdentityPoolInputRequestTypeDef(BaseModel):
    IdentityPoolId: str

class GetCredentialsForIdentityInputRequestTypeDef(BaseModel):
    IdentityId: str
    Logins: Optional[Mapping[str, str]] = None
    CustomRoleArn: Optional[str] = None

class GetIdInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    AccountId: Optional[str] = None
    Logins: Optional[Mapping[str, str]] = None

class GetIdentityPoolRolesInputRequestTypeDef(BaseModel):
    IdentityPoolId: str

class GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    Logins: Mapping[str, str]
    IdentityId: Optional[str] = None
    PrincipalTags: Optional[Mapping[str, str]] = None
    TokenDuration: Optional[int] = None

class GetOpenIdTokenInputRequestTypeDef(BaseModel):
    IdentityId: str
    Logins: Optional[Mapping[str, str]] = None

class GetPrincipalTagAttributeMapInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityProviderName: str

class IdentityDescriptionTypeDef(BaseModel):
    IdentityId: Optional[str] = None
    Logins: Optional[List[str]] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None

class IdentityPoolShortDescriptionTypeDef(BaseModel):
    IdentityPoolId: Optional[str] = None
    IdentityPoolName: Optional[str] = None

class ListIdentitiesInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    MaxResults: int
    NextToken: Optional[str] = None
    HideDisabled: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIdentityPoolsInputRequestTypeDef(BaseModel):
    MaxResults: int
    NextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class LookupDeveloperIdentityInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: Optional[str] = None
    DeveloperUserIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MappingRuleTypeDef(BaseModel):
    Claim: str
    MatchType: MappingRuleMatchTypeType
    Value: str
    RoleARN: str

class MergeDeveloperIdentitiesInputRequestTypeDef(BaseModel):
    SourceUserIdentifier: str
    DestinationUserIdentifier: str
    DeveloperProviderName: str
    IdentityPoolId: str

class SetPrincipalTagAttributeMapInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: Optional[bool] = None
    PrincipalTags: Optional[Mapping[str, str]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UnlinkDeveloperIdentityInputRequestTypeDef(BaseModel):
    IdentityId: str
    IdentityPoolId: str
    DeveloperProviderName: str
    DeveloperUserIdentifier: str

class UnlinkIdentityInputRequestTypeDef(BaseModel):
    IdentityId: str
    Logins: Mapping[str, str]
    LoginsToRemove: Sequence[str]

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateIdentityPoolInputRequestTypeDef(BaseModel):
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: Optional[bool] = None
    SupportedLoginProviders: Optional[Mapping[str, str]] = None
    DeveloperProviderName: Optional[str] = None
    OpenIdConnectProviderARNs: Optional[Sequence[str]] = None
    CognitoIdentityProviders: Optional[Sequence[CognitoIdentityProviderTypeDef]] = None
    SamlProviderARNs: Optional[Sequence[str]] = None
    IdentityPoolTags: Optional[Mapping[str, str]] = None

class IdentityPoolRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: Optional[bool] = None
    SupportedLoginProviders: Optional[Mapping[str, str]] = None
    DeveloperProviderName: Optional[str] = None
    OpenIdConnectProviderARNs: Optional[Sequence[str]] = None
    CognitoIdentityProviders: Optional[Sequence[CognitoIdentityProviderTypeDef]] = None
    SamlProviderARNs: Optional[Sequence[str]] = None
    IdentityPoolTags: Optional[Mapping[str, str]] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialsForIdentityResponseTypeDef(BaseModel):
    IdentityId: str
    Credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdResponseTypeDef(BaseModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOpenIdTokenForDeveloperIdentityResponseTypeDef(BaseModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOpenIdTokenResponseTypeDef(BaseModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrincipalTagAttributeMapResponseTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class IdentityDescriptionResponseTypeDef(BaseModel):
    IdentityId: str
    Logins: List[str]
    CreationDate: datetime
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class IdentityPoolTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: bool
    SupportedLoginProviders: Dict[str, str]
    DeveloperProviderName: str
    OpenIdConnectProviderARNs: List[str]
    CognitoIdentityProviders: List[CognitoIdentityProviderTypeDef]
    SamlProviderARNs: List[str]
    IdentityPoolTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class LookupDeveloperIdentityResponseTypeDef(BaseModel):
    IdentityId: str
    DeveloperUserIdentifierList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MergeDeveloperIdentitiesResponseTypeDef(BaseModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetPrincipalTagAttributeMapResponseTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdentitiesResponseTypeDef(BaseModel):
    UnprocessedIdentityIds: List[UnprocessedIdentityIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentitiesResponseTypeDef(BaseModel):
    IdentityPoolId: str
    Identities: List[IdentityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentityPoolsResponseTypeDef(BaseModel):
    IdentityPools: List[IdentityPoolShortDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class RulesConfigurationTypeOutputTypeDef(BaseModel):
    Rules: List[MappingRuleTypeDef]

class RulesConfigurationTypeTypeDef(BaseModel):
    Rules: Sequence[MappingRuleTypeDef]

class RoleMappingOutputTypeDef(BaseModel):
    Type: RoleMappingTypeType
    AmbiguousRoleResolution: Optional[AmbiguousRoleResolutionTypeType] = None
    RulesConfiguration: Optional[RulesConfigurationTypeOutputTypeDef] = None

class RoleMappingTypeDef(BaseModel):
    Type: RoleMappingTypeType
    AmbiguousRoleResolution: Optional[AmbiguousRoleResolutionTypeType] = None
    RulesConfiguration: Optional[RulesConfigurationTypeTypeDef] = None

class GetIdentityPoolRolesResponseTypeDef(BaseModel):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Dict[str, RoleMappingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetIdentityPoolRolesInputRequestTypeDef(BaseModel):
    IdentityPoolId: str
    Roles: Mapping[str, str]
    RoleMappings: Optional[Mapping[str, RoleMappingUnionTypeDef]] = None

