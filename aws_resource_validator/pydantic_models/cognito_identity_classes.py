from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class DeleteIdentitiesInputRequestTypeDef(BaseValidatorModel):
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

class DeleteIdentityPoolInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class DescribeIdentityInputRequestTypeDef(BaseValidatorModel):
    IdentityId: str

class DescribeIdentityPoolInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class GetCredentialsForIdentityInputRequestTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Mapping[str, str]] = None
    CustomRoleArn: Optional[str] = None

class GetIdInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    AccountId: Optional[str] = None
    Logins: Optional[Mapping[str, str]] = None

class GetIdentityPoolRolesInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Logins: Mapping[str, str]
    IdentityId: Optional[str] = None
    PrincipalTags: Optional[Mapping[str, str]] = None
    TokenDuration: Optional[int] = None

class GetOpenIdTokenInputRequestTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: Optional[Mapping[str, str]] = None

class GetPrincipalTagAttributeMapInputRequestTypeDef(BaseValidatorModel):
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

class ListIdentitiesInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    MaxResults: int
    NextToken: Optional[str] = None
    HideDisabled: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIdentityPoolsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class LookupDeveloperIdentityInputRequestTypeDef(BaseValidatorModel):
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

class MergeDeveloperIdentitiesInputRequestTypeDef(BaseValidatorModel):
    SourceUserIdentifier: str
    DestinationUserIdentifier: str
    DeveloperProviderName: str
    IdentityPoolId: str

class SetPrincipalTagAttributeMapInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: Optional[bool] = None
    PrincipalTags: Optional[Mapping[str, str]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UnlinkDeveloperIdentityInputRequestTypeDef(BaseValidatorModel):
    IdentityId: str
    IdentityPoolId: str
    DeveloperProviderName: str
    DeveloperUserIdentifier: str

class UnlinkIdentityInputRequestTypeDef(BaseValidatorModel):
    IdentityId: str
    Logins: Mapping[str, str]
    LoginsToRemove: Sequence[str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateIdentityPoolInputRequestTypeDef(BaseValidatorModel):
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

class ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class RulesConfigurationTypeOutputTypeDef(BaseValidatorModel):
    Rules: List[MappingRuleTypeDef]

class RulesConfigurationTypeTypeDef(BaseValidatorModel):
    Rules: Sequence[MappingRuleTypeDef]

class RoleMappingOutputTypeDef(BaseValidatorModel):
    Type: RoleMappingTypeType
    AmbiguousRoleResolution: Optional[AmbiguousRoleResolutionTypeType] = None
    RulesConfiguration: Optional[RulesConfigurationTypeOutputTypeDef] = None

class RoleMappingTypeDef(BaseValidatorModel):
    Type: RoleMappingTypeType
    AmbiguousRoleResolution: Optional[AmbiguousRoleResolutionTypeType] = None
    RulesConfiguration: Optional[RulesConfigurationTypeTypeDef] = None

class GetIdentityPoolRolesResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Dict[str, RoleMappingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetIdentityPoolRolesInputRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Roles: Mapping[str, str]
    RoleMappings: Optional[Mapping[str, RoleMappingUnionTypeDef]] = None

