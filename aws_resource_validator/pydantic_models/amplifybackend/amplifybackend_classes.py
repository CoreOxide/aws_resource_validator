from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    Authenticated: List[AuthenticatedElementType]
    UnAuthenticated: Optional[List[UnAuthenticatedElementType]] = None


# This class is the input for the 'clone_backend' function.
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
    MfaTypes: Optional[List[MfaTypesElementType]] = None
    SmsMessage: Optional[str] = None


class CreateBackendAuthPasswordPolicyConfigOutput(BaseValidatorModel):
    MinimumLength: float
    AdditionalConstraints: Optional[List[AdditionalConstraintsElementType]] = None


class CreateBackendAuthPasswordPolicyConfig(BaseValidatorModel):
    MinimumLength: float
    AdditionalConstraints: Optional[List[AdditionalConstraintsElementType]] = None


# This class is the input for the 'create_backend_config' function.
class CreateBackendConfigRequest(BaseValidatorModel):
    AppId: str
    BackendManagerAppId: Optional[str] = None


# This class is the input for the 'create_backend' function.
class CreateBackendRequest(BaseValidatorModel):
    AppId: str
    AppName: str
    BackendEnvironmentName: str
    ResourceConfig: Optional[Dict[str, Any]] = None
    ResourceName: Optional[str] = None


# This class is the input for the 'create_token' function.
class CreateTokenRequest(BaseValidatorModel):
    AppId: str


# This class is the input for the 'delete_backend_auth' function.
class DeleteBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


# This class is the input for the 'delete_backend' function.
class DeleteBackendRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str


# This class is the input for the 'delete_backend_storage' function.
class DeleteBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ServiceName: Literal['S3']


# This class is the input for the 'delete_token' function.
class DeleteTokenRequest(BaseValidatorModel):
    AppId: str
    SessionId: str


# This class is the input for the 'generate_backend_api_models' function.
class GenerateBackendAPIModelsRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


# This class is the input for the 'get_backend_api_models' function.
class GetBackendAPIModelsRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


# This class is the input for the 'get_backend_auth' function.
class GetBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


# This class is the input for the 'get_backend_job' function.
class GetBackendJobRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str


# This class is the input for the 'get_backend' function.
class GetBackendRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: Optional[str] = None


# This class is the input for the 'get_backend_storage' function.
class GetBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str


# This class is the input for the 'get_token' function.
class GetTokenRequest(BaseValidatorModel):
    AppId: str
    SessionId: str


# This class is the input for the 'import_backend_auth' function.
class ImportBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    NativeClientId: str
    UserPoolId: str
    WebClientId: str
    IdentityPoolId: Optional[str] = None


# This class is the input for the 'import_backend_storage' function.
class ImportBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ServiceName: Literal['S3']
    BucketName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_backend_jobs' function.
class ListBackendJobsRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None


# This class is the input for the 'list_s3_buckets' function.
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


# This class is the input for the 'remove_all_backends' function.
class RemoveAllBackendsRequest(BaseValidatorModel):
    AppId: str
    CleanAmplifyApp: Optional[bool] = None


# This class is the input for the 'remove_backend_config' function.
class RemoveBackendConfigRequest(BaseValidatorModel):
    AppId: str


class UpdateBackendAuthIdentityPoolConfig(BaseValidatorModel):
    UnauthenticatedLogin: Optional[bool] = None


class UpdateBackendAuthPasswordPolicyConfig(BaseValidatorModel):
    AdditionalConstraints: Optional[List[AdditionalConstraintsElementType]] = None
    MinimumLength: Optional[float] = None


# This class is the input for the 'update_backend_job' function.
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


class GetBackendStorageResourceConfig(BaseValidatorModel):
    Imported: bool
    ServiceName: Literal['S3']
    BucketName: Optional[str] = None
    Permissions: Optional[BackendStoragePermissionsOutput] = None

BackendStoragePermissionsUnion = Union[BackendStoragePermissions, BackendStoragePermissionsOutput]


# This class is the output for the 'clone_backend' function.
class CloneBackendResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backend_api' function.
class CreateBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backend_auth' function.
class CreateBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backend_config' function.
class CreateBackendConfigResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backend' function.
class CreateBackendResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backend_storage' function.
class CreateBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_token' function.
class CreateTokenResponse(BaseValidatorModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backend_api' function.
class DeleteBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backend_auth' function.
class DeleteBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backend' function.
class DeleteBackendResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backend_storage' function.
class DeleteBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_token' function.
class DeleteTokenResponse(BaseValidatorModel):
    IsSuccess: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'generate_backend_api_models' function.
class GenerateBackendAPIModelsResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_backend_api_models' function.
class GetBackendAPIModelsResponse(BaseValidatorModel):
    Models: str
    Status: StatusType
    ModelIntrospectionSchema: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_backend_job' function.
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


# This class is the output for the 'get_backend' function.
class GetBackendResponse(BaseValidatorModel):
    AmplifyFeatureFlags: str
    AmplifyMetaConfig: str
    AppId: str
    AppName: str
    BackendEnvironmentList: List[str]
    BackendEnvironmentName: str
    Error: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_token' function.
class GetTokenResponse(BaseValidatorModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_backend_auth' function.
class ImportBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_backend_storage' function.
class ImportBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_backend_jobs' function.
class ListBackendJobsResponse(BaseValidatorModel):
    Jobs: List[BackendJobRespObj]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'remove_all_backends' function.
class RemoveAllBackendsResponse(BaseValidatorModel):
    AppId: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_backend_config' function.
class RemoveBackendConfigResponse(BaseValidatorModel):
    Error: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_backend_api' function.
class UpdateBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_backend_auth' function.
class UpdateBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_backend_job' function.
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


# This class is the output for the 'update_backend_storage' function.
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

SettingsUnion = Union[Settings, SettingsOutput]


class ListBackendJobsRequestPaginate(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_s3_buckets' function.
class ListS3BucketsResponse(BaseValidatorModel):
    Buckets: List[S3BucketInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'update_backend_config' function.
class UpdateBackendConfigRequest(BaseValidatorModel):
    AppId: str
    LoginAuthConfig: Optional[LoginAuthConfigReqObj] = None


# This class is the output for the 'update_backend_config' function.
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
    AdditionalAuthTypes: Optional[List[BackendAPIAuthType]] = None
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
    OAuthScopes: List[OAuthScopesElementType]
    RedirectSignInURIs: List[str]
    RedirectSignOutURIs: List[str]
    DomainPrefix: Optional[str] = None
    SocialProviderSettings: Optional[SocialProviderSettings] = None


class UpdateBackendAuthOAuthConfig(BaseValidatorModel):
    DomainPrefix: Optional[str] = None
    OAuthGrantType: Optional[OAuthGrantTypeType] = None
    OAuthScopes: Optional[List[OAuthScopesElementType]] = None
    RedirectSignInURIs: Optional[List[str]] = None
    RedirectSignOutURIs: Optional[List[str]] = None
    SocialProviderSettings: Optional[SocialProviderSettings] = None


# This class is the output for the 'get_backend_storage' function.
class GetBackendStorageResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: GetBackendStorageResourceConfig
    ResourceName: str
    ResponseMetadata: ResponseMetadata


class CreateBackendStorageResourceConfig(BaseValidatorModel):
    Permissions: BackendStoragePermissionsUnion
    ServiceName: Literal['S3']
    BucketName: Optional[str] = None


class UpdateBackendStorageResourceConfig(BaseValidatorModel):
    Permissions: BackendStoragePermissionsUnion
    ServiceName: Literal['S3']


class UpdateBackendAuthMFAConfig(BaseValidatorModel):
    MFAMode: Optional[MFAModeType] = None
    Settings: Optional[SettingsUnion] = None


# This class is the output for the 'get_backend_api' function.
class GetBackendAPIResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: BackendAPIResourceConfigOutput
    ResourceName: str
    ResponseMetadata: ResponseMetadata

BackendAPIResourceConfigUnion = Union[BackendAPIResourceConfig, BackendAPIResourceConfigOutput]


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
    RequiredSignUpAttributes: List[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: Optional[CreateBackendAuthForgotPasswordConfig] = None
    Mfa: Optional[CreateBackendAuthMFAConfig] = None
    OAuth: Optional[CreateBackendAuthOAuthConfig] = None
    PasswordPolicy: Optional[CreateBackendAuthPasswordPolicyConfig] = None
    VerificationMessage: Optional[CreateBackendAuthVerificationMessageConfig] = None


# This class is the input for the 'create_backend_storage' function.
class CreateBackendStorageRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendStorageResourceConfig
    ResourceName: str


# This class is the input for the 'update_backend_storage' function.
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


# This class is the input for the 'create_backend_api' function.
class CreateBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: BackendAPIResourceConfigUnion
    ResourceName: str


# This class is the input for the 'delete_backend_api' function.
class DeleteBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnion] = None


# This class is the input for the 'get_backend_api' function.
class GetBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnion] = None


# This class is the input for the 'update_backend_api' function.
class UpdateBackendAPIRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigUnion] = None


class CreateBackendAuthResourceConfigOutput(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal['COGNITO']
    UserPoolConfigs: CreateBackendAuthUserPoolConfigOutput
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfig] = None


class CreateBackendAuthResourceConfig(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal['COGNITO']
    UserPoolConfigs: CreateBackendAuthUserPoolConfig
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfig] = None


class UpdateBackendAuthResourceConfig(BaseValidatorModel):
    AuthResources: AuthResourcesType
    Service: Literal['COGNITO']
    UserPoolConfigs: UpdateBackendAuthUserPoolConfig
    IdentityPoolConfigs: Optional[UpdateBackendAuthIdentityPoolConfig] = None


# This class is the output for the 'get_backend_auth' function.
class GetBackendAuthResponse(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: CreateBackendAuthResourceConfigOutput
    ResourceName: str
    ResponseMetadata: ResponseMetadata

CreateBackendAuthResourceConfigUnion = Union[CreateBackendAuthResourceConfig, CreateBackendAuthResourceConfigOutput]


# This class is the input for the 'update_backend_auth' function.
class UpdateBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendAuthResourceConfig
    ResourceName: str


# This class is the input for the 'create_backend_auth' function.
class CreateBackendAuthRequest(BaseValidatorModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendAuthResourceConfigUnion
    ResourceName: str