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
from aws_resource_validator.pydantic_models.amplifybackend_constants import *

class BackendAPIAppSyncAuthSettingsTypeDef(BaseModel):
    CognitoUserPoolId: Optional[str] = None
    Description: Optional[str] = None
    ExpirationTime: Optional[float] = None
    OpenIDAuthTTL: Optional[str] = None
    OpenIDClientId: Optional[str] = None
    OpenIDIatTTL: Optional[str] = None
    OpenIDIssueURL: Optional[str] = None
    OpenIDProviderName: Optional[str] = None

class BackendAPIConflictResolutionTypeDef(BaseModel):
    ResolutionStrategy: Optional[ResolutionStrategyType] = None

class BackendAuthAppleProviderConfigTypeDef(BaseModel):
    ClientId: Optional[str] = None
    KeyId: Optional[str] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None

class BackendAuthSocialProviderConfigTypeDef(BaseModel):
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None

class BackendJobRespObjTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: Optional[str] = None
    Error: Optional[str] = None
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    UpdateTime: Optional[str] = None

class BackendStoragePermissionsTypeDef(BaseModel):
    Authenticated: Sequence[AuthenticatedElementType]
    UnAuthenticated: Optional[Sequence[UnAuthenticatedElementType]] = None

class CloneBackendRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    TargetEnvironmentName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class EmailSettingsTypeDef(BaseModel):
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None

class SmsSettingsTypeDef(BaseModel):
    SmsMessage: Optional[str] = None

class CreateBackendAuthIdentityPoolConfigTypeDef(BaseModel):
    IdentityPoolName: str
    UnauthenticatedLogin: bool

class SettingsTypeDef(BaseModel):
    MfaTypes: Optional[Sequence[MfaTypesElementType]] = None
    SmsMessage: Optional[str] = None

class CreateBackendAuthPasswordPolicyConfigTypeDef(BaseModel):
    MinimumLength: float
    AdditionalConstraints: Optional[Sequence[AdditionalConstraintsElementType]] = None

class CreateBackendConfigRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendManagerAppId: Optional[str] = None

class CreateBackendRequestRequestTypeDef(BaseModel):
    AppId: str
    AppName: str
    BackendEnvironmentName: str
    ResourceConfig: Optional[Mapping[str, Any]] = None
    ResourceName: Optional[str] = None

class CreateTokenRequestRequestTypeDef(BaseModel):
    AppId: str

class DeleteBackendAuthRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class DeleteBackendRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str

class DeleteBackendStorageRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ServiceName: Literal["S3"]

class DeleteTokenRequestRequestTypeDef(BaseModel):
    AppId: str
    SessionId: str

class GenerateBackendAPIModelsRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetBackendAPIModelsRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetBackendAuthRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetBackendJobRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str

class GetBackendRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: Optional[str] = None

class GetBackendStorageRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetTokenRequestRequestTypeDef(BaseModel):
    AppId: str
    SessionId: str

class ImportBackendAuthRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    NativeClientId: str
    UserPoolId: str
    WebClientId: str
    IdentityPoolId: Optional[str] = None

class ImportBackendStorageRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ServiceName: Literal["S3"]
    BucketName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBackendJobsRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None

class ListS3BucketsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class S3BucketInfoTypeDef(BaseModel):
    CreationDate: Optional[str] = None
    Name: Optional[str] = None

class LoginAuthConfigReqObjTypeDef(BaseModel):
    AwsCognitoIdentityPoolId: Optional[str] = None
    AwsCognitoRegion: Optional[str] = None
    AwsUserPoolsId: Optional[str] = None
    AwsUserPoolsWebClientId: Optional[str] = None

class RemoveAllBackendsRequestRequestTypeDef(BaseModel):
    AppId: str
    CleanAmplifyApp: Optional[bool] = None

class RemoveBackendConfigRequestRequestTypeDef(BaseModel):
    AppId: str

class UpdateBackendAuthIdentityPoolConfigTypeDef(BaseModel):
    UnauthenticatedLogin: Optional[bool] = None

class UpdateBackendAuthPasswordPolicyConfigTypeDef(BaseModel):
    AdditionalConstraints: Optional[Sequence[AdditionalConstraintsElementType]] = None
    MinimumLength: Optional[float] = None

class UpdateBackendJobRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Operation: Optional[str] = None
    Status: Optional[str] = None

class BackendAPIAuthTypeTypeDef(BaseModel):
    Mode: Optional[ModeType] = None
    Settings: Optional[BackendAPIAppSyncAuthSettingsTypeDef] = None

class SocialProviderSettingsTypeDef(BaseModel):
    Facebook: Optional[BackendAuthSocialProviderConfigTypeDef] = None
    Google: Optional[BackendAuthSocialProviderConfigTypeDef] = None
    LoginWithAmazon: Optional[BackendAuthSocialProviderConfigTypeDef] = None
    SignInWithApple: Optional[BackendAuthAppleProviderConfigTypeDef] = None

class CreateBackendStorageResourceConfigTypeDef(BaseModel):
    Permissions: BackendStoragePermissionsTypeDef
    ServiceName: Literal["S3"]
    BucketName: Optional[str] = None

class GetBackendStorageResourceConfigTypeDef(BaseModel):
    Imported: bool
    ServiceName: Literal["S3"]
    BucketName: Optional[str] = None
    Permissions: Optional[BackendStoragePermissionsTypeDef] = None

class UpdateBackendStorageResourceConfigTypeDef(BaseModel):
    Permissions: BackendStoragePermissionsTypeDef
    ServiceName: Literal["S3"]

class CloneBackendResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendAPIResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendAuthResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendConfigResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendStorageResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenResponseTypeDef(BaseModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendAPIResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendAuthResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendStorageResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTokenResponseTypeDef(BaseModel):
    IsSuccess: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateBackendAPIModelsResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendAPIModelsResponseTypeDef(BaseModel):
    Models: str
    Status: StatusType
    ModelIntrospectionSchema: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendJobResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendResponseTypeDef(BaseModel):
    AmplifyFeatureFlags: str
    AmplifyMetaConfig: str
    AppId: str
    AppName: str
    BackendEnvironmentList: List[str]
    BackendEnvironmentName: str
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTokenResponseTypeDef(BaseModel):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportBackendAuthResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportBackendStorageResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackendJobsResponseTypeDef(BaseModel):
    Jobs: List[BackendJobRespObjTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveAllBackendsResponseTypeDef(BaseModel):
    AppId: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBackendConfigResponseTypeDef(BaseModel):
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendAPIResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendAuthResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendJobResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendStorageResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendAuthForgotPasswordConfigTypeDef(BaseModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None

class CreateBackendAuthVerificationMessageConfigTypeDef(BaseModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None

class UpdateBackendAuthForgotPasswordConfigTypeDef(BaseModel):
    DeliveryMethod: Optional[DeliveryMethodType] = None
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None

class UpdateBackendAuthVerificationMessageConfigTypeDef(BaseModel):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: Optional[EmailSettingsTypeDef] = None
    SmsSettings: Optional[SmsSettingsTypeDef] = None

class CreateBackendAuthMFAConfigTypeDef(BaseModel):
    MFAMode: MFAModeType
    Settings: Optional[SettingsTypeDef] = None

class UpdateBackendAuthMFAConfigTypeDef(BaseModel):
    MFAMode: Optional[MFAModeType] = None
    Settings: Optional[SettingsTypeDef] = None

class ListBackendJobsRequestListBackendJobsPaginateTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    JobId: Optional[str] = None
    Operation: Optional[str] = None
    Status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListS3BucketsResponseTypeDef(BaseModel):
    Buckets: List[S3BucketInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendConfigRequestRequestTypeDef(BaseModel):
    AppId: str
    LoginAuthConfig: Optional[LoginAuthConfigReqObjTypeDef] = None

class UpdateBackendConfigResponseTypeDef(BaseModel):
    AppId: str
    BackendManagerAppId: str
    Error: str
    LoginAuthConfig: LoginAuthConfigReqObjTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BackendAPIResourceConfigTypeDef(BaseModel):
    AdditionalAuthTypes: Optional[Sequence[BackendAPIAuthTypeTypeDef]] = None
    ApiName: Optional[str] = None
    ConflictResolution: Optional[BackendAPIConflictResolutionTypeDef] = None
    DefaultAuthType: Optional[BackendAPIAuthTypeTypeDef] = None
    Service: Optional[str] = None
    TransformSchema: Optional[str] = None

class CreateBackendAuthOAuthConfigTypeDef(BaseModel):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: Sequence[OAuthScopesElementType]
    RedirectSignInURIs: Sequence[str]
    RedirectSignOutURIs: Sequence[str]
    DomainPrefix: Optional[str] = None
    SocialProviderSettings: Optional[SocialProviderSettingsTypeDef] = None

class UpdateBackendAuthOAuthConfigTypeDef(BaseModel):
    DomainPrefix: Optional[str] = None
    OAuthGrantType: Optional[OAuthGrantTypeType] = None
    OAuthScopes: Optional[Sequence[OAuthScopesElementType]] = None
    RedirectSignInURIs: Optional[Sequence[str]] = None
    RedirectSignOutURIs: Optional[Sequence[str]] = None
    SocialProviderSettings: Optional[SocialProviderSettingsTypeDef] = None

class CreateBackendStorageRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendStorageResourceConfigTypeDef
    ResourceName: str

class GetBackendStorageResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: GetBackendStorageResourceConfigTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendStorageRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendStorageResourceConfigTypeDef
    ResourceName: str

class CreateBackendAPIRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: BackendAPIResourceConfigTypeDef
    ResourceName: str

class DeleteBackendAPIRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigTypeDef] = None

class GetBackendAPIRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigTypeDef] = None

class GetBackendAPIResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: BackendAPIResourceConfigTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendAPIRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: Optional[BackendAPIResourceConfigTypeDef] = None

class CreateBackendAuthUserPoolConfigTypeDef(BaseModel):
    RequiredSignUpAttributes: Sequence[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: Optional[CreateBackendAuthForgotPasswordConfigTypeDef] = None
    Mfa: Optional[CreateBackendAuthMFAConfigTypeDef] = None
    OAuth: Optional[CreateBackendAuthOAuthConfigTypeDef] = None
    PasswordPolicy: Optional[CreateBackendAuthPasswordPolicyConfigTypeDef] = None
    VerificationMessage: Optional[CreateBackendAuthVerificationMessageConfigTypeDef] = None

class UpdateBackendAuthUserPoolConfigTypeDef(BaseModel):
    ForgotPassword: Optional[UpdateBackendAuthForgotPasswordConfigTypeDef] = None
    Mfa: Optional[UpdateBackendAuthMFAConfigTypeDef] = None
    OAuth: Optional[UpdateBackendAuthOAuthConfigTypeDef] = None
    PasswordPolicy: Optional[UpdateBackendAuthPasswordPolicyConfigTypeDef] = None
    VerificationMessage: Optional[UpdateBackendAuthVerificationMessageConfigTypeDef] = None

class CreateBackendAuthResourceConfigTypeDef(BaseModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfigTypeDef
    IdentityPoolConfigs: Optional[CreateBackendAuthIdentityPoolConfigTypeDef] = None

class UpdateBackendAuthResourceConfigTypeDef(BaseModel):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: UpdateBackendAuthUserPoolConfigTypeDef
    IdentityPoolConfigs: Optional[UpdateBackendAuthIdentityPoolConfigTypeDef] = None

class CreateBackendAuthRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendAuthResourceConfigTypeDef
    ResourceName: str

class GetBackendAuthResponseTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: CreateBackendAuthResourceConfigTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendAuthRequestRequestTypeDef(BaseModel):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendAuthResourceConfigTypeDef
    ResourceName: str

