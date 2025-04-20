from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cognito_identity.cognito_identity_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CognitoIdentityProvider(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ClientId: Optional[str] = None
    ServerSideTokenCheck: Optional[bool] = None


class Credentials(BaseValidatorModel):
    AccessKeyId: Optional[str] = None
    SecretKey: Optional[str] = None
    SessionToken: Optional[str] = None
    Expiration: Optional[datetime] = None


class DeleteIdentitiesInput(BaseValidatorModel):
    IdentityIdsToDelete: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedIdentityId(BaseValidatorModel):
    IdentityId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None


class DeleteIdentityPoolInput(BaseValidatorModel):
    IdentityPoolId: str


class DescribeIdentityInput(BaseValidatorModel):
    IdentityId: str


class DescribeIdentityPoolInput(BaseValidatorModel):
    IdentityPoolId: str


class GetCredentialsForIdentityInput(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Dict[str, str]] = None
    CustomRoleArn: Optional[str] = None


class GetIdInput(BaseValidatorModel):
    IdentityPoolId: str
    AccountId: Optional[str] = None
    Logins: Optional[Dict[str, str]] = None


class GetIdentityPoolRolesInput(BaseValidatorModel):
    IdentityPoolId: str


class GetOpenIdTokenForDeveloperIdentityInput(BaseValidatorModel):
    IdentityPoolId: str
    Logins: Dict[str, str]
    IdentityId: Optional[str] = None
    PrincipalTags: Optional[Dict[str, str]] = None
    TokenDuration: Optional[int] = None


class GetOpenIdTokenInput(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Dict[str, str]] = None


class GetPrincipalTagAttributeMapInput(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str


class IdentityDescription(BaseValidatorModel):
    IdentityId: Optional[str] = None
    Logins: Optional[List[str]] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class IdentityPoolShortDescription(BaseValidatorModel):
    IdentityPoolId: Optional[str] = None
    IdentityPoolName: Optional[str] = None


class ListIdentitiesInput(BaseValidatorModel):
    IdentityPoolId: str
    MaxResults: int
    NextToken: Optional[str] = None
    HideDisabled: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIdentityPoolsInput(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class LookupDeveloperIdentityInput(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: Optional[str] = None
    DeveloperUserIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MappingRule(BaseValidatorModel):
    Claim: str
    MatchType: MappingRuleMatchTypeType
    Value: str
    RoleARN: str


class MergeDeveloperIdentitiesInput(BaseValidatorModel):
    SourceUserIdentifier: str
    DestinationUserIdentifier: str
    DeveloperProviderName: str
    IdentityPoolId: str


class SetPrincipalTagAttributeMapInput(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: Optional[bool] = None
    PrincipalTags: Optional[Dict[str, str]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UnlinkDeveloperIdentityInput(BaseValidatorModel):
    IdentityId: str
    IdentityPoolId: str
    DeveloperProviderName: str
    DeveloperUserIdentifier: str


class UnlinkIdentityInput(BaseValidatorModel):
    IdentityId: str
    Logins: Dict[str, str]
    LoginsToRemove: List[str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class CreateIdentityPoolInput(BaseValidatorModel):
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: Optional[bool] = None
    SupportedLoginProviders: Optional[Dict[str, str]] = None
    DeveloperProviderName: Optional[str] = None
    OpenIdConnectProviderARNs: Optional[List[str]] = None
    CognitoIdentityProviders: Optional[List[CognitoIdentityProvider]] = None
    SamlProviderARNs: Optional[List[str]] = None
    IdentityPoolTags: Optional[Dict[str, str]] = None


class IdentityPoolRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: Optional[bool] = None
    SupportedLoginProviders: Optional[Dict[str, str]] = None
    DeveloperProviderName: Optional[str] = None
    OpenIdConnectProviderARNs: Optional[List[str]] = None
    CognitoIdentityProviders: Optional[List[CognitoIdentityProvider]] = None
    SamlProviderARNs: Optional[List[str]] = None
    IdentityPoolTags: Optional[Dict[str, str]] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCredentialsForIdentityResponse(BaseValidatorModel):
    IdentityId: str
    Credentials: Credentials
    ResponseMetadata: ResponseMetadata


class GetIdResponse(BaseValidatorModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadata


class GetOpenIdTokenForDeveloperIdentityResponse(BaseValidatorModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadata


class GetOpenIdTokenResponse(BaseValidatorModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadata


class GetPrincipalTagAttributeMapResponse(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class IdentityDescriptionResponse(BaseValidatorModel):
    IdentityId: str
    Logins: List[str]
    CreationDate: datetime
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


class IdentityPool(BaseValidatorModel):
    IdentityPoolId: str
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool
    AllowClassicFlow: bool
    SupportedLoginProviders: Dict[str, str]
    DeveloperProviderName: str
    OpenIdConnectProviderARNs: List[str]
    CognitoIdentityProviders: List[CognitoIdentityProvider]
    SamlProviderARNs: List[str]
    IdentityPoolTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class LookupDeveloperIdentityResponse(BaseValidatorModel):
    IdentityId: str
    DeveloperUserIdentifierList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MergeDeveloperIdentitiesResponse(BaseValidatorModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadata


class SetPrincipalTagAttributeMapResponse(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeleteIdentitiesResponse(BaseValidatorModel):
    UnprocessedIdentityIds: List[UnprocessedIdentityId]
    ResponseMetadata: ResponseMetadata


class ListIdentitiesResponse(BaseValidatorModel):
    IdentityPoolId: str
    Identities: List[IdentityDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIdentityPoolsResponse(BaseValidatorModel):
    IdentityPools: List[IdentityPoolShortDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIdentityPoolsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class RulesConfigurationTypeOutput(BaseValidatorModel):
    Rules: List[MappingRule]


class RulesConfigurationType(BaseValidatorModel):
    Rules: List[MappingRule]


class RoleMappingOutput(BaseValidatorModel):
    Type: RoleMappingTypeType
    AmbiguousRoleResolution: Optional[AmbiguousRoleResolutionTypeType] = None
    RulesConfiguration: Optional[RulesConfigurationTypeOutput] = None

RulesConfigurationTypeUnion = Union[RulesConfigurationType, RulesConfigurationTypeOutput]


class GetIdentityPoolRolesResponse(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Dict[str, RoleMappingOutput]
    ResponseMetadata: ResponseMetadata


class RoleMapping(BaseValidatorModel):
    Type: RoleMappingTypeType
    AmbiguousRoleResolution: Optional[AmbiguousRoleResolutionTypeType] = None
    RulesConfiguration: Optional[RulesConfigurationTypeUnion] = None

RoleMappingUnion = Union[RoleMapping, RoleMappingOutput]


class SetIdentityPoolRolesInput(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Optional[Dict[str, RoleMappingUnion]] = None