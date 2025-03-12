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
from aws_resource_validator.pydantic_models.amplifybackend_constants import *

class BackendAPIAppSyncAuthSettingsTypeDef(BaseValidatorModel):
    CognitoUserPoolId: Optional[str] = None
    Description: Optional[str] = None
    ExpirationTime: Optional[float] = None
    OpenIDAuthTTL: Optional[str] = None
    OpenIDClientId: Optional[str] = None
    OpenIDIatTTL: Optional[str] = None
    OpenIDIssueURL: Optional[str] = None
    OpenIDProviderName: Optional[str] = None


class BackendAPIConflictResolutionTypeDef(BaseValidatorModel):
    ResolutionStrategy: Optional[ResolutionStrategyType] = None


class BackendAuthAppleProviderConfigTypeDef(BaseValidatorModel):
    ClientId: Optional[str] = None
    KeyId: Optional[str] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None


class BackendAuthSocialProviderConfigTypeDef(BaseValidatorModel):
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None


class BackendJobRespObjTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: Optional[str] = None
    Error: Optional[str] = None
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    UpdateTime: Optional[str] = None


class BackendStoragePermissionsOutputTypeDef(BaseValidatorModel):
    Authenticated: List[AuthenticatedElementType]
    UnAuthenticated: Optional[List[UnAuthenticatedElementType]] = None


class BackendStoragePermissionsTypeDef(BaseValidatorModel):
    Authenticated: Sequence[AuthenticatedElementType]
    UnAuthenticated: Optional[Sequence[UnAuthenticatedElementType]] = None


class CloneBackendRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    TargetEnvironmentName: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EmailSettingsTypeDef(BaseValidatorModel):
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None


class SmsSettingsTypeDef(BaseValidatorModel):
    SmsMessage: Optional[str] = None


class CreateBackendAuthIdentityPoolConfigTypeDef(BaseValidatorModel):
    IdentityPoolName: str
    UnauthenticatedLogin: bool


class SettingsOutputTypeDef(BaseValidatorModel):
    MfaTypes: Optional[List[MfaTypesElementType]] = None
    SmsMessage: Optional[str] = None


class SettingsTypeDef(BaseValidatorModel):
    MfaTypes: Optional[Sequence[MfaTypesElementType]] = None
    SmsMessage: Optional[str] = None


class CreateBackendAuthPasswordPolicyConfigOutputTypeDef(BaseValidatorModel):
    MinimumLength: float
    AdditionalConstraints: Optional[List[AdditionalConstraintsElementType]] = None


class CreateBackendAuthPasswordPolicyConfigTypeDef(BaseValidatorModel):
    MinimumLength: float
    AdditionalConstraints: Optional[Sequence[AdditionalConstraintsElementType]] = None


class CreateBackendConfigRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendManagerAppId: Optional[str] = None


class CreateBackendRequestTypeDef(BaseValidatorModel):
    AppId: str
    AppName: str
    BackendEnvironmentName: str
    ResourceConfig: Optional[Mapping[str, Any]] = None
    ResourceName: Optional[str] = None


class CreateTokenRequestTypeDef(BaseValidatorModel):
    AppId: str


class DeleteBackendAuthRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class DeleteBackendRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str


class DeleteTokenRequestTypeDef(BaseValidatorModel):
    AppId: str
    SessionId: str


class GenerateBackendAPIModelsRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetBackendAPIModelsRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetBackendAuthRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetBackendJobRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str


class GetBackendRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: Optional[str] = None


class GetBackendStorageRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetTokenRequestTypeDef(BaseValidatorModel):
    AppId: str
    SessionId: str


class ImportBackendAuthRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    NativeClientId: str
    UserPoolId: str
    WebClientId: str
    IdentityPoolId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBackendJobsRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None


class ListS3BucketsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class S3BucketInfoTypeDef(BaseValidatorModel):
    CreationDate: Optional[str] = None
    Name: Optional[str] = None


class LoginAuthConfigReqObjTypeDef(BaseValidatorModel):
    AwsCognitoIdentityPoolId: Optional[str] = None
    AwsCognitoRegion: Optional[str] = None
    AwsUserPoolsId: Optional[str] = None
    AwsUserPoolsWebClientId: Optional[str] = None


class RemoveAllBackendsRequestTypeDef(BaseValidatorModel):
    AppId: str
    CleanAmplifyApp: Optional[bool] = None


class RemoveBackendConfigRequestTypeDef(BaseValidatorModel):
    AppId: str


class UpdateBackendAuthIdentityPoolConfigTypeDef(BaseValidatorModel):
    UnauthenticatedLogin: Optional[bool] = None


class UpdateBackendAuthPasswordPolicyConfigTypeDef(BaseValidatorModel):
    AdditionalConstraints: Optional[Sequence[AdditionalConstraintsElementType]] = None
    MinimumLength: Optional[float] = None


class UpdateBackendJobRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Operation: Optional[str] = None
    Status: Optional[str] = None


class BackendAPIAuthTypeTypeDef(BaseValidatorModel):
    Mode: Optional[ModeType] = None
    Settings: Optional[BackendAPIAppSyncAuthSettingsTypeDef] = None


class SocialProviderSettingsTypeDef(BaseValidatorModel):
    Facebook: Optional[BackendAuthSocialProviderConfigTypeDef] = None
    Google: Optional[BackendAuthSocialProviderConfigTypeDef] = None
    LoginWithAmazon: Optional[BackendAuthSocialProviderConfigTypeDef] = None
    SignInWithApple: Optional[BackendAuthAppleProviderConfigTypeDef] = None


class CloneBackendResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendAPIResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendAuthResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendConfigResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendStorageResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTokenResponseTypeDef(BaseValidatorModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBackendAPIResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBackendAuthResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBackendResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBackendStorageResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTokenResponseTypeDef(BaseValidatorModel):
    IsSuccess: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GenerateBackendAPIModelsResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBackendAPIModelsResponseTypeDef(BaseValidatorModel):
    Models: str
    Status: StatusType
    ModelIntrospectionSchema: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBackendJobResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBackendResponseTypeDef(BaseValidatorModel):
    AmplifyFeatureFlags: str
    AmplifyMetaConfig: str
    AppId: str
    AppName: str
    BackendEnvironmentList: List[str]
    BackendEnvironmentName: str
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTokenResponseTypeDef(BaseValidatorModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportBackendAuthResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportBackendStorageResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListBackendJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[BackendJobRespObjTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RemoveAllBackendsResponseTypeDef(BaseValidatorModel):
    AppId: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveBackendConfigResponseTypeDef(BaseValidatorModel):
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBackendAPIResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBackendAuthResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBackendJobResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBackendStorageResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendAuthForgotPasswordConfigTypeDef(BaseValidatorModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None


class CreateBackendAuthVerificationMessageConfigTypeDef(BaseValidatorModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None


class UpdateBackendAuthForgotPasswordConfigTypeDef(BaseValidatorModel):
    DeliveryMethod: Optional[DeliveryMethodType] = None
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None


class UpdateBackendAuthVerificationMessageConfigTypeDef(BaseValidatorModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None


class CreateBackendAuthMFAConfigOutputTypeDef(BaseValidatorModel):
    MFAMode: MFAModeType
    Settings: Optional[SettingsOutputTypeDef] = None


class CreateBackendAuthMFAConfigTypeDef(BaseValidatorModel):
    MFAMode: MFAModeType
    Settings: Optional[SettingsTypeDef] = None


class ListBackendJobsRequestPaginateTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListS3BucketsResponseTypeDef(BaseValidatorModel):
    Buckets: List[S3BucketInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateBackendConfigRequestTypeDef(BaseValidatorModel):
    AppId: str
    LoginAuthConfig: Optional[LoginAuthConfigReqObjTypeDef] = None


class UpdateBackendConfigResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendManagerAppId: str
    Error: str
    LoginAuthConfig: LoginAuthConfigReqObjTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BackendAPIResourceConfigOutputTypeDef(BaseValidatorModel):
    AdditionalAuthTypes: Optional[List[BackendAPIAuthTypeTypeDef]] = None
    ApiName: Optional[str] = None
    ConflictResolution: Optional[BackendAPIConflictResolutionTypeDef] = None
    DefaultAuthType: Optional[BackendAPIAuthTypeTypeDef] = None
    Service: Optional[str] = None
    TransformSchema: Optional[str] = None


class BackendAPIResourceConfigTypeDef(BaseValidatorModel):
    AdditionalAuthTypes: Optional[Sequence[BackendAPIAuthTypeTypeDef]] = None
    ApiName: Optional[str] = None
    ConflictResolution: Optional[BackendAPIConflictResolutionTypeDef] = None
    DefaultAuthType: Optional[BackendAPIAuthTypeTypeDef] = None
    Service: Optional[str] = None
    TransformSchema: Optional[str] = None


class CreateBackendAuthOAuthConfigOutputTypeDef(BaseValidatorModel):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: List[OAuthScopesElementType]
    RedirectSignInURIs: List[str]
    RedirectSignOutURIs: List[str]
    DomainPrefix: Optional[str] = None
    SocialProviderSettings: Optional[SocialProviderSettingsTypeDef] = None


class CreateBackendAuthOAuthConfigTypeDef(BaseValidatorModel):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: Sequence[OAuthScopesElementType]
    RedirectSignInURIs: Sequence[str]
    RedirectSignOutURIs: Sequence[str]
    DomainPrefix: Optional[str] = None
    SocialProviderSettings: Optional[SocialProviderSettingsTypeDef] = None


class UpdateBackendAuthOAuthConfigTypeDef(BaseValidatorModel):
    DomainPrefix: Optional[str] = None
    OAuthGrantType: Optional[OAuthGrantTypeType] = None
    OAuthScopes: Optional[Sequence[OAuthScopesElementType]] = None
    RedirectSignInURIs: Optional[Sequence[str]] = None
    RedirectSignOutURIs: Optional[Sequence[str]] = None
    SocialProviderSettings: Optional[SocialProviderSettingsTypeDef] = None


class GetBackendStorageResourceConfigTypeDef(BaseValidatorModel):
    pass


class GetBackendStorageResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: GetBackendStorageResourceConfigTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef


class SettingsUnionTypeDef(BaseValidatorModel):
    pass


class UpdateBackendAuthMFAConfigTypeDef(BaseValidatorModel):
    MFAMode: Optional[MFAModeType] = None
    Settings: Optional[SettingsUnionTypeDef] = None


class GetBackendAPIResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: BackendAPIResourceConfigOutputTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBackendAuthUserPoolConfigOutputTypeDef(BaseValidatorModel):
    RequiredSignUpAttributes: List[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: Optional[CreateBackendAuthForgotPasswordConfigTypeDef] = None
    Mfa: Optional[CreateBackendAuthMFAConfigOutputTypeDef] = None
    OAuth: Optional[CreateBackendAuthOAuthConfigOutputTypeDef] = None
    PasswordPolicy: Optional[CreateBackendAuthPasswordPolicyConfigOutputTypeDef] = None
    VerificationMessage: Optional[CreateBackendAuthVerificationMessageConfigTypeDef] = None


class CreateBackendAuthUserPoolConfigTypeDef(BaseValidatorModel):
    RequiredSignUpAttributes: Sequence[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: Optional[CreateBackendAuthForgotPasswordConfigTypeDef] = None
    Mfa: Optional[CreateBackendAuthMFAConfigTypeDef] = None
    OAuth: Optional[CreateBackendAuthOAuthConfigTypeDef] = None
    PasswordPolicy: Optional[CreateBackendAuthPasswordPolicyConfigTypeDef] = None
    VerificationMessage: Optional[CreateBackendAuthVerificationMessageConfigTypeDef] = None


class CreateBackendStorageResourceConfigTypeDef(BaseValidatorModel):
    pass


class CreateBackendStorageRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendStorageResourceConfigTypeDef
    ResourceName: str


class UpdateBackendStorageResourceConfigTypeDef(BaseValidatorModel):
    pass


class UpdateBackendStorageRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendStorageResourceConfigTypeDef
    ResourceName: str


class UpdateBackendAuthUserPoolConfigTypeDef(BaseValidatorModel):
    ForgotPassword: Optional[UpdateBackendAuthForgotPasswordConfigTypeDef] = None
    Mfa: Optional[UpdateBackendAuthMFAConfigTypeDef] = None
    OAuth: Optional[UpdateBackendAuthOAuthConfigTypeDef] = None
    PasswordPolicy: Optional[UpdateBackendAuthPasswordPolicyConfigTypeDef] = None
    VerificationMessage: Optional[UpdateBackendAuthVerificationMessageConfigTypeDef] = None


class BackendAPIResourceConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateBackendAPIRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: BackendAPIResourceConfigUnionTypeDef
    ResourceName: str


class DeleteBackendAPIRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnionTypeDef] = None


class GetBackendAPIRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnionTypeDef] = None


class UpdateBackendAPIRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnionTypeDef] = None


class CreateBackendAuthResourceConfigOutputTypeDef(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfigOutputTypeDef
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfigTypeDef] = None


class CreateBackendAuthResourceConfigTypeDef(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfigTypeDef
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfigTypeDef] = None


class UpdateBackendAuthResourceConfigTypeDef(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: UpdateBackendAuthUserPoolConfigTypeDef
    IdentityPoolConfigs: Optional[UpdateBackendAuthIdentityPoolConfigTypeDef] = None


class GetBackendAuthResponseTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: CreateBackendAuthResourceConfigOutputTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBackendAuthRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendAuthResourceConfigTypeDef
    ResourceName: str


class CreateBackendAuthResourceConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateBackendAuthRequestTypeDef(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendAuthResourceConfigUnionTypeDef
    ResourceName: str


