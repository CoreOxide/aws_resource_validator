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
from aws_resource_validator.pydantic_models.cognito_identity_constants import *

class CognitoIdentityProviderTypeDef(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ClientId: Optional[str] = None
    ServerSideTokenCheck: Optional[bool] = None


class CredentialsTypeDef(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretKey: Optional[str] = None
    SessionToken: Optional[str] = None
    Expiration: Optional[datetime] = None


class DeleteIdentitiesInputTypeDef(BaseValidatorModel):
    IdentityIdsToDelete: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedIdentityIdTypeDef(BaseValidatorModel):
    IdentityId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None


class DeleteIdentityPoolInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class DescribeIdentityInputTypeDef(BaseValidatorModel):
    IdentityId: str


class DescribeIdentityPoolInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class GetCredentialsForIdentityInputTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Mapping[str, str]] = None
    CustomRoleArn: Optional[str] = None


class GetIdInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    AccountId: Optional[str] = None
    Logins: Optional[Mapping[str, str]] = None


class GetIdentityPoolRolesInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class GetOpenIdTokenForDeveloperIdentityInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Logins: Mapping[str, str]
    IdentityId: Optional[str] = None
    PrincipalTags: Optional[Mapping[str, str]] = None
    TokenDuration: Optional[int] = None


class GetOpenIdTokenInputTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Mapping[str, str]] = None


class GetPrincipalTagAttributeMapInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str


class IdentityDescriptionTypeDef(BaseValidatorModel):
    IdentityId: Optional[str] = None
    Logins: Optional[List[str]] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class IdentityPoolShortDescriptionTypeDef(BaseValidatorModel):
    IdentityPoolId: Optional[str] = None
    IdentityPoolName: Optional[str] = None


class ListIdentitiesInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    MaxResults: int
    NextToken: Optional[str] = None
    HideDisabled: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIdentityPoolsInputTypeDef(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class LookupDeveloperIdentityInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: Optional[str] = None
    DeveloperUserIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MappingRuleTypeDef(BaseValidatorModel):
    Claim: str
    MatchType: MappingRuleMatchTypeType
    Value: str
    RoleARN: str


class MergeDeveloperIdentitiesInputTypeDef(BaseValidatorModel):
    SourceUserIdentifier: str
    DestinationUserIdentifier: str
    DeveloperProviderName: str
    IdentityPoolId: str


class SetPrincipalTagAttributeMapInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: Optional[bool] = None
    PrincipalTags: Optional[Mapping[str, str]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UnlinkDeveloperIdentityInputTypeDef(BaseValidatorModel):
    IdentityId: str
    IdentityPoolId: str
    DeveloperProviderName: str
    DeveloperUserIdentifier: str


class UnlinkIdentityInputTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: Mapping[str, str]
    LoginsToRemove: Sequence[str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class CreateIdentityPoolInputTypeDef(BaseValidatorModel):
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: Optional[bool] = None
    SupportedLoginProviders: Optional[Mapping[str, str]] = None
    DeveloperProviderName: Optional[str] = None
    OpenIdConnectProviderARNs: Optional[Sequence[str]] = None
    CognitoIdentityProviders: Optional[Sequence[CognitoIdentityProviderTypeDef]] = None
    SamlProviderARNs: Optional[Sequence[str]] = None
    IdentityPoolTags: Optional[Mapping[str, str]] = None


class IdentityPoolRequestTypeDef(BaseValidatorModel):
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


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCredentialsForIdentityResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    Credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetOpenIdTokenForDeveloperIdentityResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetOpenIdTokenResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPrincipalTagAttributeMapResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class IdentityDescriptionResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: List[str]
    CreationDate: datetime
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class IdentityPoolTypeDef(BaseValidatorModel):
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


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class LookupDeveloperIdentityResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    DeveloperUserIdentifierList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MergeDeveloperIdentitiesResponseTypeDef(BaseValidatorModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetPrincipalTagAttributeMapResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteIdentitiesResponseTypeDef(BaseValidatorModel):
    UnprocessedIdentityIds: List[UnprocessedIdentityIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListIdentitiesResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Identities: List[IdentityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIdentityPoolsResponseTypeDef(BaseValidatorModel):
    IdentityPools: List[IdentityPoolShortDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIdentityPoolsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class RulesConfigurationTypeOutputTypeDef(BaseValidatorModel):
    Rules: List[MappingRuleTypeDef]


class RulesConfigurationTypeTypeDef(BaseValidatorModel):
    Rules: Sequence[MappingRuleTypeDef]


class RoleMappingOutputTypeDef(BaseValidatorModel):
    pass


class GetIdentityPoolRolesResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Dict[str, RoleMappingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RoleMappingUnionTypeDef(BaseValidatorModel):
    pass


class SetIdentityPoolRolesInputTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Mapping[str, str]
    RoleMappings: Optional[Mapping[str, RoleMappingUnionTypeDef]] = None


