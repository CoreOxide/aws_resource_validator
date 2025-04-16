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

class BackendAPIAppSyncAuthSettings(BaseValidatorModel):
    CognitoUserPoolId: Optional[str] = None
    Description: Optional[str] = None
    ExpirationTime: Optional[float] = None
    OpenIDAuthTTL: Optional[str] = None
    OpenIDClientId: Optional[str] = None
    OpenIDIatTTL: Optional[str] = None
    OpenIDIssueURL: Optional[str] = None
    OpenIDProviderName: Optional[str] = None


class BackendAPIConflictResolution(BaseValidatorModel):
    ResolutionStrategy: Optional[ResolutionStrategyType] = None


class BackendAuthAppleProviderConfig(BaseValidatorModel):
    ClientId: Optional[str] = None
    KeyId: Optional[str] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None


class BackendAuthSocialProviderConfig(BaseValidatorModel):
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None


class BackendJobRespObj(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: Optional[str] = None
    Error: Optional[str] = None
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    UpdateTime: Optional[str] = None


class BackendStoragePermissionsOutput(BaseValidatorModel):
    Authenticated: List[AuthenticatedElementType]
    UnAuthenticated: Optional[List[UnAuthenticatedElementType]] = None


class BackendStoragePermissions(BaseValidatorModel):
    Authenticated: Sequence[AuthenticatedElementType]
    UnAuthenticated: Optional[Sequence[UnAuthenticatedElementType]] = None


class CloneBackendRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    TargetEnvironmentName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EmailSettings(BaseValidatorModel):
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None


class SmsSettings(BaseValidatorModel):
    SmsMessage: Optional[str] = None


class CreateBackendAuthIdentityPoolConfig(BaseValidatorModel):
    IdentityPoolName: str
    UnauthenticatedLogin: bool


class SettingsOutput(BaseValidatorModel):
    MfaTypes: Optional[List[MfaTypesElementType]] = None
    SmsMessage: Optional[str] = None


class Settings(BaseValidatorModel):
    MfaTypes: Optional[Sequence[MfaTypesElementType]] = None
    SmsMessage: Optional[str] = None


class CreateBackendAuthPasswordPolicyConfigOutput(BaseValidatorModel):
    MinimumLength: float
    AdditionalConstraints: Optional[List[AdditionalConstraintsElementType]] = None


class CreateBackendAuthPasswordPolicyConfig(BaseValidatorModel):
    MinimumLength: float
    AdditionalConstraints: Optional[Sequence[AdditionalConstraintsElementType]] = None


class CreateBackendConfigRequest(BaseValidatorModel):
    AppId: str
    BackendManagerAppId: Optional[str] = None


class CreateBackendRequest(BaseValidatorModel):
    AppId: str
    AppName: str
    BackendEnvironmentName: str
    ResourceConfig: Optional[Mapping[str, Any]] = None
    ResourceName: Optional[str] = None


class CreateTokenRequest(BaseValidatorModel):
    AppId: str


class DeleteBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class DeleteBackendRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str


class DeleteTokenRequest(BaseValidatorModel):
    AppId: str
    SessionId: str


class GenerateBackendAPIModelsRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetBackendAPIModelsRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetBackendJobRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str


class GetBackendRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: Optional[str] = None


class GetBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


class GetTokenRequest(BaseValidatorModel):
    AppId: str
    SessionId: str


class ImportBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    NativeClientId: str
    UserPoolId: str
    WebClientId: str
    IdentityPoolId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBackendJobsRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None


class ListS3BucketsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class S3BucketInfo(BaseValidatorModel):
    CreationDate: Optional[str] = None
    Name: Optional[str] = None


class LoginAuthConfigReqObj(BaseValidatorModel):
    AwsCognitoIdentityPoolId: Optional[str] = None
    AwsCognitoRegion: Optional[str] = None
    AwsUserPoolsId: Optional[str] = None
    AwsUserPoolsWebClientId: Optional[str] = None


class RemoveAllBackendsRequest(BaseValidatorModel):
    AppId: str
    CleanAmplifyApp: Optional[bool] = None


class RemoveBackendConfigRequest(BaseValidatorModel):
    AppId: str


class UpdateBackendAuthIdentityPoolConfig(BaseValidatorModel):
    UnauthenticatedLogin: Optional[bool] = None


class UpdateBackendAuthPasswordPolicyConfig(BaseValidatorModel):
    AdditionalConstraints: Optional[Sequence[AdditionalConstraintsElementType]] = None
    MinimumLength: Optional[float] = None


class UpdateBackendJobRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Operation: Optional[str] = None
    Status: Optional[str] = None


class BackendAPIAuthType(BaseValidatorModel):
    Mode: Optional[ModeType] = None
    Settings: Optional[BackendAPIAppSyncAuthSettings] = None


class SocialProviderSettings(BaseValidatorModel):
    Facebook: Optional[BackendAuthSocialProviderConfig] = None
    Google: Optional[BackendAuthSocialProviderConfig] = None
    LoginWithAmazon: Optional[BackendAuthSocialProviderConfig] = None
    SignInWithApple: Optional[BackendAuthAppleProviderConfig] = None


class CloneBackendResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateBackendConfigResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateBackendResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateTokenResponse(BaseValidatorModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadata


class DeleteBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class DeleteBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class DeleteBackendResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class DeleteBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


class DeleteTokenResponse(BaseValidatorModel):
    IsSuccess: bool
    ResponseMetadata: ResponseMetadata


class GenerateBackendAPIModelsResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class GetBackendAPIModelsResponse(BaseValidatorModel):
    Models: str
    Status: StatusType
    ModelIntrospectionSchema: str
    ResponseMetadata: ResponseMetadata


class GetBackendJobResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadata


class GetBackendResponse(BaseValidatorModel):
    AmplifyFeatureFlags: str
    AmplifyMetaConfig: str
    AppId: str
    AppName: str
    BackendEnvironmentList: List[str]
    BackendEnvironmentName: str
    Error: str
    ResponseMetadata: ResponseMetadata


class GetTokenResponse(BaseValidatorModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadata


class ImportBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class ImportBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


class ListBackendJobsResponse(BaseValidatorModel):
    Jobs: List[BackendJobRespObj]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RemoveAllBackendsResponse(BaseValidatorModel):
    AppId: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class RemoveBackendConfigResponse(BaseValidatorModel):
    Error: str
    ResponseMetadata: ResponseMetadata


class UpdateBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class UpdateBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


class UpdateBackendJobResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadata


class UpdateBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateBackendAuthForgotPasswordConfig(BaseValidatorModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettings] = None
    SmsSettings: Optional[SmsSettings] = None


class CreateBackendAuthVerificationMessageConfig(BaseValidatorModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettings] = None
    SmsSettings: Optional[SmsSettings] = None


class UpdateBackendAuthForgotPasswordConfig(BaseValidatorModel):
    DeliveryMethod: Optional[DeliveryMethodType] = None
    EmailSettings: Optional[EmailSettings] = None
    SmsSettings: Optional[SmsSettings] = None


class UpdateBackendAuthVerificationMessageConfig(BaseValidatorModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettings] = None
    SmsSettings: Optional[SmsSettings] = None


class CreateBackendAuthMFAConfigOutput(BaseValidatorModel):
    MFAMode: MFAModeType
    Settings: Optional[SettingsOutput] = None


class CreateBackendAuthMFAConfig(BaseValidatorModel):
    MFAMode: MFAModeType
    Settings: Optional[Settings] = None


class ListBackendJobsRequestPaginate(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListS3BucketsResponse(BaseValidatorModel):
    Buckets: List[S3BucketInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateBackendConfigRequest(BaseValidatorModel):
    AppId: str
    LoginAuthConfig: Optional[LoginAuthConfigReqObj] = None


class UpdateBackendConfigResponse(BaseValidatorModel):
    AppId: str
    BackendManagerAppId: str
    Error: str
    LoginAuthConfig: LoginAuthConfigReqObj
    ResponseMetadata: ResponseMetadata


class BackendAPIResourceConfigOutput(BaseValidatorModel):
    AdditionalAuthTypes: Optional[List[BackendAPIAuthType]] = None
    ApiName: Optional[str] = None
    ConflictResolution: Optional[BackendAPIConflictResolution] = None
    DefaultAuthType: Optional[BackendAPIAuthType] = None
    Service: Optional[str] = None
    TransformSchema: Optional[str] = None


class BackendAPIResourceConfig(BaseValidatorModel):
    AdditionalAuthTypes: Optional[Sequence[BackendAPIAuthType]] = None
    ApiName: Optional[str] = None
    ConflictResolution: Optional[BackendAPIConflictResolution] = None
    DefaultAuthType: Optional[BackendAPIAuthType] = None
    Service: Optional[str] = None
    TransformSchema: Optional[str] = None


class CreateBackendAuthOAuthConfigOutput(BaseValidatorModel):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: List[OAuthScopesElementType]
    RedirectSignInURIs: List[str]
    RedirectSignOutURIs: List[str]
    DomainPrefix: Optional[str] = None
    SocialProviderSettings: Optional[SocialProviderSettings] = None


class CreateBackendAuthOAuthConfig(BaseValidatorModel):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: Sequence[OAuthScopesElementType]
    RedirectSignInURIs: Sequence[str]
    RedirectSignOutURIs: Sequence[str]
    DomainPrefix: Optional[str] = None
    SocialProviderSettings: Optional[SocialProviderSettings] = None


class UpdateBackendAuthOAuthConfig(BaseValidatorModel):
    DomainPrefix: Optional[str] = None
    OAuthGrantType: Optional[OAuthGrantTypeType] = None
    OAuthScopes: Optional[Sequence[OAuthScopesElementType]] = None
    RedirectSignInURIs: Optional[Sequence[str]] = None
    RedirectSignOutURIs: Optional[Sequence[str]] = None
    SocialProviderSettings: Optional[SocialProviderSettings] = None


class GetBackendStorageResourceConfig(BaseValidatorModel):
    pass


class GetBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: GetBackendStorageResourceConfig
    ResourceName: str
    ResponseMetadata: ResponseMetadata


class SettingsUnion(BaseValidatorModel):
    pass


class UpdateBackendAuthMFAConfig(BaseValidatorModel):
    MFAMode: Optional[MFAModeType] = None
    Settings: Optional[SettingsUnion] = None


class GetBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: BackendAPIResourceConfigOutput
    ResourceName: str
    ResponseMetadata: ResponseMetadata


class CreateBackendAuthUserPoolConfigOutput(BaseValidatorModel):
    RequiredSignUpAttributes: List[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: Optional[CreateBackendAuthForgotPasswordConfig] = None
    Mfa: Optional[CreateBackendAuthMFAConfigOutput] = None
    OAuth: Optional[CreateBackendAuthOAuthConfigOutput] = None
    PasswordPolicy: Optional[CreateBackendAuthPasswordPolicyConfigOutput] = None
    VerificationMessage: Optional[CreateBackendAuthVerificationMessageConfig] = None


class CreateBackendAuthUserPoolConfig(BaseValidatorModel):
    RequiredSignUpAttributes: Sequence[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: Optional[CreateBackendAuthForgotPasswordConfig] = None
    Mfa: Optional[CreateBackendAuthMFAConfig] = None
    OAuth: Optional[CreateBackendAuthOAuthConfig] = None
    PasswordPolicy: Optional[CreateBackendAuthPasswordPolicyConfig] = None
    VerificationMessage: Optional[CreateBackendAuthVerificationMessageConfig] = None


class CreateBackendStorageResourceConfig(BaseValidatorModel):
    pass


class CreateBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendStorageResourceConfig
    ResourceName: str


class UpdateBackendStorageResourceConfig(BaseValidatorModel):
    pass


class UpdateBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendStorageResourceConfig
    ResourceName: str


class UpdateBackendAuthUserPoolConfig(BaseValidatorModel):
    ForgotPassword: Optional[UpdateBackendAuthForgotPasswordConfig] = None
    Mfa: Optional[UpdateBackendAuthMFAConfig] = None
    OAuth: Optional[UpdateBackendAuthOAuthConfig] = None
    PasswordPolicy: Optional[UpdateBackendAuthPasswordPolicyConfig] = None
    VerificationMessage: Optional[UpdateBackendAuthVerificationMessageConfig] = None


class BackendAPIResourceConfigUnion(BaseValidatorModel):
    pass


class CreateBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: BackendAPIResourceConfigUnion
    ResourceName: str


class DeleteBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnion] = None


class GetBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnion] = None


class UpdateBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnion] = None


class CreateBackendAuthResourceConfigOutput(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfigOutput
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfig] = None


class CreateBackendAuthResourceConfig(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfig
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfig] = None


class UpdateBackendAuthResourceConfig(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: UpdateBackendAuthUserPoolConfig
    IdentityPoolConfigs: Optional[UpdateBackendAuthIdentityPoolConfig] = None


class GetBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: CreateBackendAuthResourceConfigOutput
    ResourceName: str
    ResponseMetadata: ResponseMetadata


class UpdateBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendAuthResourceConfig
    ResourceName: str


class CreateBackendAuthResourceConfigUnion(BaseValidatorModel):
    pass


class CreateBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendAuthResourceConfigUnion
    ResourceName: str


