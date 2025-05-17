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


# This class is the input for the 'delete_identities' function.
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


# This class is the input for the 'delete_identity_pool' function.
class DeleteIdentityPoolInput(BaseValidatorModel):
    IdentityPoolId: str


# This class is the input for the 'describe_identity' function.
class DescribeIdentityInput(BaseValidatorModel):
    IdentityId: str


# This class is the input for the 'describe_identity_pool' function.
class DescribeIdentityPoolInput(BaseValidatorModel):
    IdentityPoolId: str


# This class is the input for the 'get_credentials_for_identity' function.
class GetCredentialsForIdentityInput(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Dict[str, str]] = None
    CustomRoleArn: Optional[str] = None


# This class is the input for the 'get_id' function.
class GetIdInput(BaseValidatorModel):
    IdentityPoolId: str
    AccountId: Optional[str] = None
    Logins: Optional[Dict[str, str]] = None


# This class is the input for the 'get_identity_pool_roles' function.
class GetIdentityPoolRolesInput(BaseValidatorModel):
    IdentityPoolId: str


# This class is the input for the 'get_open_id_token_for_developer_identity' function.
class GetOpenIdTokenForDeveloperIdentityInput(BaseValidatorModel):
    IdentityPoolId: str
    Logins: Dict[str, str]
    IdentityId: Optional[str] = None
    PrincipalTags: Optional[Dict[str, str]] = None
    TokenDuration: Optional[int] = None


# This class is the input for the 'get_open_id_token' function.
class GetOpenIdTokenInput(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Dict[str, str]] = None


# This class is the input for the 'get_principal_tag_attribute_map' function.
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


# This class is the input for the 'list_identities' function.
class ListIdentitiesInput(BaseValidatorModel):
    IdentityPoolId: str
    MaxResults: int
    NextToken: Optional[str] = None
    HideDisabled: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_identity_pools' function.
class ListIdentityPoolsInput(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'lookup_developer_identity' function.
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


# This class is the input for the 'merge_developer_identities' function.
class MergeDeveloperIdentitiesInput(BaseValidatorModel):
    SourceUserIdentifier: str
    DestinationUserIdentifier: str
    DeveloperProviderName: str
    IdentityPoolId: str


# This class is the input for the 'set_principal_tag_attribute_map' function.
class SetPrincipalTagAttributeMapInput(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: Optional[bool] = None
    PrincipalTags: Optional[Dict[str, str]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


# This class is the input for the 'unlink_developer_identity' function.
class UnlinkDeveloperIdentityInput(BaseValidatorModel):
    IdentityId: str
    IdentityPoolId: str
    DeveloperProviderName: str
    DeveloperUserIdentifier: str


# This class is the input for the 'unlink_identity' function.
class UnlinkIdentityInput(BaseValidatorModel):
    IdentityId: str
    Logins: Dict[str, str]
    LoginsToRemove: List[str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'create_identity_pool' function.
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


# This class is the input for the 'update_identity_pool' function.
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


# This class is the output for the 'unlink_identity' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_credentials_for_identity' function.
class GetCredentialsForIdentityResponse(BaseValidatorModel):
    IdentityId: str
    Credentials: Credentials
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_id' function.
class GetIdResponse(BaseValidatorModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_open_id_token_for_developer_identity' function.
class GetOpenIdTokenForDeveloperIdentityResponse(BaseValidatorModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_open_id_token' function.
class GetOpenIdTokenResponse(BaseValidatorModel):
    IdentityId: str
    Token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_principal_tag_attribute_map' function.
class GetPrincipalTagAttributeMapResponse(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_identity' function.
class IdentityDescriptionResponse(BaseValidatorModel):
    IdentityId: str
    Logins: List[str]
    CreationDate: datetime
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_identity_pool' function.
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


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'lookup_developer_identity' function.
class LookupDeveloperIdentityResponse(BaseValidatorModel):
    IdentityId: str
    DeveloperUserIdentifierList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'merge_developer_identities' function.
class MergeDeveloperIdentitiesResponse(BaseValidatorModel):
    IdentityId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_principal_tag_attribute_map' function.
class SetPrincipalTagAttributeMapResponse(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_identities' function.
class DeleteIdentitiesResponse(BaseValidatorModel):
    UnprocessedIdentityIds: List[UnprocessedIdentityId]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_identities' function.
class ListIdentitiesResponse(BaseValidatorModel):
    IdentityPoolId: str
    Identities: List[IdentityDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_identity_pools' function.
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


# This class is the output for the 'get_identity_pool_roles' function.
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


# This class is the input for the 'set_identity_pool_roles' function.
class SetIdentityPoolRolesInput(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Optional[Dict[str, RoleMappingUnion]] = None