from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cognito_idp.cognito_idp_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class RecoveryOptionType(BaseValidatorModel):
    Priority: int
    Name: RecoveryOptionNameTypeType


class AccountTakeoverActionType(BaseValidatorModel):
    Notify: bool
    EventAction: AccountTakeoverEventActionTypeType


class AdminAddUserToGroupRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    GroupName: str


class AdminConfirmSignUpRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Dict[str, str]] = None


class MessageTemplateType(BaseValidatorModel):
    SMSMessage: Optional[str] = None
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None


class AttributeType(BaseValidatorModel):
    Name: str
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AdminDeleteUserAttributesRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributeNames: List[str]


class AdminDeleteUserRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str


class ProviderUserIdentifierType(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ProviderAttributeName: Optional[str] = None
    ProviderAttributeValue: Optional[str] = None


class AdminDisableUserRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str


class AdminEnableUserRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str


class AdminForgetDeviceRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    DeviceKey: str


class AdminGetDeviceRequest(BaseValidatorModel):
    DeviceKey: str
    UserPoolId: str
    Username: str


class AdminGetUserRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str


class MFAOptionType(BaseValidatorModel):
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None


class AnalyticsMetadataType(BaseValidatorModel):
    AnalyticsEndpointId: Optional[str] = None


class AdminListDevicesRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class AdminListGroupsForUserRequest(BaseValidatorModel):
    Username: str
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GroupType(BaseValidatorModel):
    GroupName: Optional[str] = None
    UserPoolId: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class AdminListUserAuthEventsRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AdminRemoveUserFromGroupRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    GroupName: str


class AdminResetUserPasswordRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Dict[str, str]] = None


class EmailMfaSettingsType(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None


class SMSMfaSettingsType(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None


class SoftwareTokenMfaSettingsType(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None


class AdminSetUserPasswordRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    Password: str
    Permanent: Optional[bool] = None


class AdminUpdateAuthEventFeedbackRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackValue: FeedbackValueTypeType


class AdminUpdateDeviceStatusRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None


class AdminUserGlobalSignOutRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str


class AdvancedSecurityAdditionalFlowsType(BaseValidatorModel):
    CustomAuthMode: Optional[AdvancedSecurityEnabledModeTypeType] = None


class AnalyticsConfigurationType(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    RoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    UserDataShared: Optional[bool] = None


class AssetTypeOutput(BaseValidatorModel):
    Category: AssetCategoryTypeType
    ColorMode: ColorSchemeModeTypeType
    Extension: AssetExtensionTypeType
    Bytes: Optional[bytes] = None
    ResourceId: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class AssociateSoftwareTokenRequest(BaseValidatorModel):
    AccessToken: Optional[str] = None
    Session: Optional[str] = None


class ChallengeResponseType(BaseValidatorModel):
    ChallengeName: Optional[ChallengeNameType] = None
    ChallengeResponse: Optional[ChallengeResponseType] = None


class EventContextDataType(BaseValidatorModel):
    IpAddress: Optional[str] = None
    DeviceName: Optional[str] = None
    Timezone: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None


class EventFeedbackType(BaseValidatorModel):
    FeedbackValue: FeedbackValueTypeType
    Provider: str
    FeedbackDate: Optional[datetime] = None


class EventRiskType(BaseValidatorModel):
    RiskDecision: Optional[RiskDecisionTypeType] = None
    RiskLevel: Optional[RiskLevelTypeType] = None
    CompromisedCredentialsDetected: Optional[bool] = None


class NewDeviceMetadataType(BaseValidatorModel):
    DeviceKey: Optional[str] = None
    DeviceGroupKey: Optional[str] = None


class ChangePasswordRequest(BaseValidatorModel):
    ProposedPassword: str
    AccessToken: str
    PreviousPassword: Optional[str] = None


class CloudWatchLogsConfigurationType(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class CodeDeliveryDetailsType(BaseValidatorModel):
    Destination: Optional[str] = None
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None


class CompleteWebAuthnRegistrationRequest(BaseValidatorModel):
    AccessToken: str
    Credential: Dict[str, Any]


class CompromisedCredentialsActionsType(BaseValidatorModel):
    EventAction: CompromisedCredentialsEventActionTypeType


class DeviceSecretVerifierConfigType(BaseValidatorModel):
    PasswordVerifier: Optional[str] = None
    Salt: Optional[str] = None


class UserContextDataType(BaseValidatorModel):
    IpAddress: Optional[str] = None
    EncodedData: Optional[str] = None


class HttpHeader(BaseValidatorModel):
    headerName: Optional[str] = None
    headerValue: Optional[str] = None


class CreateGroupRequest(BaseValidatorModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None


class CreateIdentityProviderRequest(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str
    ProviderType: IdentityProviderTypeTypeType
    ProviderDetails: Dict[str, str]
    AttributeMapping: Optional[Dict[str, str]] = None
    IdpIdentifiers: Optional[List[str]] = None


class IdentityProviderType(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    ProviderDetails: Optional[Dict[str, str]] = None
    AttributeMapping: Optional[Dict[str, str]] = None
    IdpIdentifiers: Optional[List[str]] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class ResourceServerScopeType(BaseValidatorModel):
    ScopeName: str
    ScopeDescription: str


class CreateUserImportJobRequest(BaseValidatorModel):
    JobName: str
    UserPoolId: str
    CloudWatchLogsRoleArn: str


class UserImportJobType(BaseValidatorModel):
    JobName: Optional[str] = None
    JobId: Optional[str] = None
    UserPoolId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CreationDate: Optional[datetime] = None
    StartDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    Status: Optional[UserImportJobStatusTypeType] = None
    CloudWatchLogsRoleArn: Optional[str] = None
    ImportedUsers: Optional[int] = None
    SkippedUsers: Optional[int] = None
    FailedUsers: Optional[int] = None
    CompletionMessage: Optional[str] = None


class TokenValidityUnitsType(BaseValidatorModel):
    AccessToken: Optional[TimeUnitsTypeType] = None
    IdToken: Optional[TimeUnitsTypeType] = None
    RefreshToken: Optional[TimeUnitsTypeType] = None


class CustomDomainConfigType(BaseValidatorModel):
    CertificateArn: str


class DeviceConfigurationType(BaseValidatorModel):
    ChallengeRequiredOnNewDevice: Optional[bool] = None
    DeviceOnlyRememberedOnUserPrompt: Optional[bool] = None


class EmailConfigurationType(BaseValidatorModel):
    SourceArn: Optional[str] = None
    ReplyToEmailAddress: Optional[str] = None
    EmailSendingAccount: Optional[EmailSendingAccountTypeType] = None
    From: Optional[str] = None
    ConfigurationSet: Optional[str] = None


class SmsConfigurationType(BaseValidatorModel):
    SnsCallerArn: str
    ExternalId: Optional[str] = None
    SnsRegion: Optional[str] = None


class UsernameConfigurationType(BaseValidatorModel):
    CaseSensitive: bool


class VerificationMessageTemplateType(BaseValidatorModel):
    SmsMessage: Optional[str] = None
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None
    EmailMessageByLink: Optional[str] = None
    EmailSubjectByLink: Optional[str] = None
    DefaultEmailOption: Optional[DefaultEmailOptionTypeType] = None


class CustomEmailLambdaVersionConfigType(BaseValidatorModel):
    LambdaVersion: Literal['V1_0']
    LambdaArn: str


class CustomSMSLambdaVersionConfigType(BaseValidatorModel):
    LambdaVersion: Literal['V1_0']
    LambdaArn: str


class DeleteGroupRequest(BaseValidatorModel):
    GroupName: str
    UserPoolId: str


class DeleteIdentityProviderRequest(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str


class DeleteManagedLoginBrandingRequest(BaseValidatorModel):
    ManagedLoginBrandingId: str
    UserPoolId: str


class DeleteResourceServerRequest(BaseValidatorModel):
    UserPoolId: str
    Identifier: str


class DeleteUserAttributesRequest(BaseValidatorModel):
    UserAttributeNames: List[str]
    AccessToken: str


class DeleteUserPoolClientRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str


class DeleteUserPoolDomainRequest(BaseValidatorModel):
    Domain: str
    UserPoolId: str


class DeleteUserPoolRequest(BaseValidatorModel):
    UserPoolId: str


class DeleteUserRequest(BaseValidatorModel):
    AccessToken: str


class DeleteWebAuthnCredentialRequest(BaseValidatorModel):
    AccessToken: str
    CredentialId: str


class DescribeIdentityProviderRequest(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str


class DescribeManagedLoginBrandingByClientRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    ReturnMergedResources: Optional[bool] = None


class DescribeManagedLoginBrandingRequest(BaseValidatorModel):
    UserPoolId: str
    ManagedLoginBrandingId: str
    ReturnMergedResources: Optional[bool] = None


class DescribeResourceServerRequest(BaseValidatorModel):
    UserPoolId: str
    Identifier: str


class DescribeRiskConfigurationRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None


class DescribeUserImportJobRequest(BaseValidatorModel):
    UserPoolId: str
    JobId: str


class DescribeUserPoolClientRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str


class DescribeUserPoolDomainRequest(BaseValidatorModel):
    Domain: str


class DescribeUserPoolRequest(BaseValidatorModel):
    UserPoolId: str


class EmailMfaConfigType(BaseValidatorModel):
    Message: Optional[str] = None
    Subject: Optional[str] = None


class FirehoseConfigurationType(BaseValidatorModel):
    StreamArn: Optional[str] = None


class ForgetDeviceRequest(BaseValidatorModel):
    DeviceKey: str
    AccessToken: Optional[str] = None


class GetCSVHeaderRequest(BaseValidatorModel):
    UserPoolId: str


class GetDeviceRequest(BaseValidatorModel):
    DeviceKey: str
    AccessToken: Optional[str] = None


class GetGroupRequest(BaseValidatorModel):
    GroupName: str
    UserPoolId: str


class GetIdentityProviderByIdentifierRequest(BaseValidatorModel):
    UserPoolId: str
    IdpIdentifier: str


class GetLogDeliveryConfigurationRequest(BaseValidatorModel):
    UserPoolId: str


class GetSigningCertificateRequest(BaseValidatorModel):
    UserPoolId: str


class GetUICustomizationRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None


class UICustomizationType(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    ImageUrl: Optional[str] = None
    CSS: Optional[str] = None
    CSSVersion: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class GetUserAttributeVerificationCodeRequest(BaseValidatorModel):
    AccessToken: str
    AttributeName: str
    ClientMetadata: Optional[Dict[str, str]] = None


class GetUserAuthFactorsRequest(BaseValidatorModel):
    AccessToken: str


class GetUserPoolMfaConfigRequest(BaseValidatorModel):
    UserPoolId: str


class SoftwareTokenMfaConfigType(BaseValidatorModel):
    Enabled: Optional[bool] = None


class WebAuthnConfigurationType(BaseValidatorModel):
    RelyingPartyId: Optional[str] = None
    UserVerification: Optional[UserVerificationTypeType] = None


class GetUserRequest(BaseValidatorModel):
    AccessToken: str


class GlobalSignOutRequest(BaseValidatorModel):
    AccessToken: str


class PreTokenGenerationVersionConfigType(BaseValidatorModel):
    LambdaVersion: PreTokenGenerationLambdaVersionTypeType
    LambdaArn: str


class ListDevicesRequest(BaseValidatorModel):
    AccessToken: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None


class ListGroupsRequest(BaseValidatorModel):
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListIdentityProvidersRequest(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProviderDescription(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class ListResourceServersRequest(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListUserImportJobsRequest(BaseValidatorModel):
    UserPoolId: str
    MaxResults: int
    PaginationToken: Optional[str] = None


class ListUserPoolClientsRequest(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UserPoolClientDescription(BaseValidatorModel):
    ClientId: Optional[str] = None
    UserPoolId: Optional[str] = None
    ClientName: Optional[str] = None


class ListUserPoolsRequest(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None


class ListUsersInGroupRequest(BaseValidatorModel):
    UserPoolId: str
    GroupName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListUsersRequest(BaseValidatorModel):
    UserPoolId: str
    AttributesToGet: Optional[List[str]] = None
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None
    Filter: Optional[str] = None


class ListWebAuthnCredentialsRequest(BaseValidatorModel):
    AccessToken: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class WebAuthnCredentialDescription(BaseValidatorModel):
    CredentialId: str
    FriendlyCredentialName: str
    RelyingPartyId: str
    AuthenticatorTransports: List[str]
    CreatedAt: datetime
    AuthenticatorAttachment: Optional[str] = None


class S3ConfigurationType(BaseValidatorModel):
    BucketArn: Optional[str] = None


class NotifyEmailType(BaseValidatorModel):
    Subject: str
    HtmlBody: Optional[str] = None
    TextBody: Optional[str] = None


class NumberAttributeConstraintsType(BaseValidatorModel):
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None


class PasswordPolicyType(BaseValidatorModel):
    MinimumLength: Optional[int] = None
    RequireUppercase: Optional[bool] = None
    RequireLowercase: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireSymbols: Optional[bool] = None
    PasswordHistorySize: Optional[int] = None
    TemporaryPasswordValidityDays: Optional[int] = None


class RevokeTokenRequest(BaseValidatorModel):
    Token: str
    ClientId: str
    ClientSecret: Optional[str] = None


class RiskExceptionConfigurationTypeOutput(BaseValidatorModel):
    BlockedIPRangeList: Optional[List[str]] = None
    SkippedIPRangeList: Optional[List[str]] = None


class RiskExceptionConfigurationType(BaseValidatorModel):
    BlockedIPRangeList: Optional[List[str]] = None
    SkippedIPRangeList: Optional[List[str]] = None


class StringAttributeConstraintsType(BaseValidatorModel):
    MinLength: Optional[str] = None
    MaxLength: Optional[str] = None


class SignInPolicyTypeOutput(BaseValidatorModel):
    AllowedFirstAuthFactors: Optional[List[AuthFactorTypeType]] = None


class SignInPolicyType(BaseValidatorModel):
    AllowedFirstAuthFactors: Optional[List[AuthFactorTypeType]] = None


class StartUserImportJobRequest(BaseValidatorModel):
    UserPoolId: str
    JobId: str


class StartWebAuthnRegistrationRequest(BaseValidatorModel):
    AccessToken: str


class StopUserImportJobRequest(BaseValidatorModel):
    UserPoolId: str
    JobId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateAuthEventFeedbackRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackToken: str
    FeedbackValue: FeedbackValueTypeType


class UpdateDeviceStatusRequest(BaseValidatorModel):
    AccessToken: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None


class UpdateGroupRequest(BaseValidatorModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None


class UpdateIdentityProviderRequest(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str
    ProviderDetails: Optional[Dict[str, str]] = None
    AttributeMapping: Optional[Dict[str, str]] = None
    IdpIdentifiers: Optional[List[str]] = None


class UserAttributeUpdateSettingsTypeOutput(BaseValidatorModel):
    AttributesRequireVerificationBeforeUpdate: Optional[List[VerifiedAttributeTypeType]] = None


class UserAttributeUpdateSettingsType(BaseValidatorModel):
    AttributesRequireVerificationBeforeUpdate: Optional[List[VerifiedAttributeTypeType]] = None


class VerifySoftwareTokenRequest(BaseValidatorModel):
    UserCode: str
    AccessToken: Optional[str] = None
    Session: Optional[str] = None
    FriendlyDeviceName: Optional[str] = None


class VerifyUserAttributeRequest(BaseValidatorModel):
    AccessToken: str
    AttributeName: str
    Code: str


class AccountRecoverySettingTypeOutput(BaseValidatorModel):
    RecoveryMechanisms: Optional[List[RecoveryOptionType]] = None


class AccountRecoverySettingType(BaseValidatorModel):
    RecoveryMechanisms: Optional[List[RecoveryOptionType]] = None


class AccountTakeoverActionsType(BaseValidatorModel):
    LowAction: Optional[AccountTakeoverActionType] = None
    MediumAction: Optional[AccountTakeoverActionType] = None
    HighAction: Optional[AccountTakeoverActionType] = None


class AdminCreateUserConfigType(BaseValidatorModel):
    AllowAdminCreateUserOnly: Optional[bool] = None
    UnusedAccountValidityDays: Optional[int] = None
    InviteMessageTemplate: Optional[MessageTemplateType] = None


class AdminCreateUserRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributes: Optional[List[AttributeType]] = None
    ValidationData: Optional[List[AttributeType]] = None
    TemporaryPassword: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    MessageAction: Optional[MessageActionTypeType] = None
    DesiredDeliveryMediums: Optional[List[DeliveryMediumTypeType]] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class AdminUpdateUserAttributesRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributes: List[AttributeType]
    ClientMetadata: Optional[Dict[str, str]] = None


class DeviceType(BaseValidatorModel):
    DeviceKey: Optional[str] = None
    DeviceAttributes: Optional[List[AttributeType]] = None
    DeviceCreateDate: Optional[datetime] = None
    DeviceLastModifiedDate: Optional[datetime] = None
    DeviceLastAuthenticatedDate: Optional[datetime] = None


class UpdateUserAttributesRequest(BaseValidatorModel):
    UserAttributes: List[AttributeType]
    AccessToken: str
    ClientMetadata: Optional[Dict[str, str]] = None


class AssociateSoftwareTokenResponse(BaseValidatorModel):
    SecretCode: str
    Session: str
    ResponseMetadata: ResponseMetadata


class ConfirmDeviceResponse(BaseValidatorModel):
    UserConfirmationNecessary: bool
    ResponseMetadata: ResponseMetadata


class ConfirmSignUpResponse(BaseValidatorModel):
    Session: str
    ResponseMetadata: ResponseMetadata


class CreateUserPoolDomainResponse(BaseValidatorModel):
    ManagedLoginVersion: int
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCSVHeaderResponse(BaseValidatorModel):
    UserPoolId: str
    CSVHeader: List[str]
    ResponseMetadata: ResponseMetadata


class GetSigningCertificateResponse(BaseValidatorModel):
    Certificate: str
    ResponseMetadata: ResponseMetadata


class GetUserAuthFactorsResponse(BaseValidatorModel):
    Username: str
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ConfiguredUserAuthFactors: List[AuthFactorTypeType]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartWebAuthnRegistrationResponse(BaseValidatorModel):
    CredentialCreationOptions: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


class UpdateUserPoolDomainResponse(BaseValidatorModel):
    ManagedLoginVersion: int
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadata


class VerifySoftwareTokenResponse(BaseValidatorModel):
    Status: VerifySoftwareTokenResponseTypeType
    Session: str
    ResponseMetadata: ResponseMetadata


class AdminDisableProviderForUserRequest(BaseValidatorModel):
    UserPoolId: str
    User: ProviderUserIdentifierType


class AdminLinkProviderForUserRequest(BaseValidatorModel):
    UserPoolId: str
    DestinationUser: ProviderUserIdentifierType
    SourceUser: ProviderUserIdentifierType


class AdminGetUserResponse(BaseValidatorModel):
    Username: str
    UserAttributes: List[AttributeType]
    UserCreateDate: datetime
    UserLastModifiedDate: datetime
    Enabled: bool
    UserStatus: UserStatusTypeType
    MFAOptions: List[MFAOptionType]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ResponseMetadata: ResponseMetadata


class AdminSetUserSettingsRequest(BaseValidatorModel):
    UserPoolId: str
    Username: str
    MFAOptions: List[MFAOptionType]


class GetUserResponse(BaseValidatorModel):
    Username: str
    UserAttributes: List[AttributeType]
    MFAOptions: List[MFAOptionType]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ResponseMetadata: ResponseMetadata


class SetUserSettingsRequest(BaseValidatorModel):
    AccessToken: str
    MFAOptions: List[MFAOptionType]


class UserType(BaseValidatorModel):
    Username: Optional[str] = None
    Attributes: Optional[List[AttributeType]] = None
    UserCreateDate: Optional[datetime] = None
    UserLastModifiedDate: Optional[datetime] = None
    Enabled: Optional[bool] = None
    UserStatus: Optional[UserStatusTypeType] = None
    MFAOptions: Optional[List[MFAOptionType]] = None


class AdminListGroupsForUserRequestPaginate(BaseValidatorModel):
    Username: str
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class AdminListUserAuthEventsRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    Username: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdentityProvidersRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceServersRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserPoolClientsRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserPoolsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersInGroupRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    GroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    UserPoolId: str
    AttributesToGet: Optional[List[str]] = None
    Filter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class AdminListGroupsForUserResponse(BaseValidatorModel):
    Groups: List[GroupType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateGroupResponse(BaseValidatorModel):
    Group: GroupType
    ResponseMetadata: ResponseMetadata


class GetGroupResponse(BaseValidatorModel):
    Group: GroupType
    ResponseMetadata: ResponseMetadata


class ListGroupsResponse(BaseValidatorModel):
    Groups: List[GroupType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateGroupResponse(BaseValidatorModel):
    Group: GroupType
    ResponseMetadata: ResponseMetadata


class AdminSetUserMFAPreferenceRequest(BaseValidatorModel):
    Username: str
    UserPoolId: str
    SMSMfaSettings: Optional[SMSMfaSettingsType] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsType] = None
    EmailMfaSettings: Optional[EmailMfaSettingsType] = None


class SetUserMFAPreferenceRequest(BaseValidatorModel):
    AccessToken: str
    SMSMfaSettings: Optional[SMSMfaSettingsType] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsType] = None
    EmailMfaSettings: Optional[EmailMfaSettingsType] = None


class UserPoolAddOnsType(BaseValidatorModel):
    AdvancedSecurityMode: AdvancedSecurityModeTypeType
    AdvancedSecurityAdditionalFlows: Optional[AdvancedSecurityAdditionalFlowsType] = None


class ManagedLoginBrandingType(BaseValidatorModel):
    ManagedLoginBrandingId: Optional[str] = None
    UserPoolId: Optional[str] = None
    UseCognitoProvidedValues: Optional[bool] = None
    Settings: Optional[Dict[str, Any]] = None
    Assets: Optional[List[AssetTypeOutput]] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class AssetType(BaseValidatorModel):
    Category: AssetCategoryTypeType
    ColorMode: ColorSchemeModeTypeType
    Extension: AssetExtensionTypeType
    Bytes: Optional[Blob] = None
    ResourceId: Optional[str] = None


class SetUICustomizationRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CSS: Optional[str] = None
    ImageFile: Optional[Blob] = None


class AuthEventType(BaseValidatorModel):
    EventId: Optional[str] = None
    EventType: Optional[EventTypeType] = None
    CreationDate: Optional[datetime] = None
    EventResponse: Optional[EventResponseTypeType] = None
    EventRisk: Optional[EventRiskType] = None
    ChallengeResponses: Optional[List[ChallengeResponseType]] = None
    EventContextData: Optional[EventContextDataType] = None
    EventFeedback: Optional[EventFeedbackType] = None


class AuthenticationResultType(BaseValidatorModel):
    AccessToken: Optional[str] = None
    ExpiresIn: Optional[int] = None
    TokenType: Optional[str] = None
    RefreshToken: Optional[str] = None
    IdToken: Optional[str] = None
    NewDeviceMetadata: Optional[NewDeviceMetadataType] = None


class ForgotPasswordResponse(BaseValidatorModel):
    CodeDeliveryDetails: CodeDeliveryDetailsType
    ResponseMetadata: ResponseMetadata


class GetUserAttributeVerificationCodeResponse(BaseValidatorModel):
    CodeDeliveryDetails: CodeDeliveryDetailsType
    ResponseMetadata: ResponseMetadata


class ResendConfirmationCodeResponse(BaseValidatorModel):
    CodeDeliveryDetails: CodeDeliveryDetailsType
    ResponseMetadata: ResponseMetadata


class SignUpResponse(BaseValidatorModel):
    UserConfirmed: bool
    CodeDeliveryDetails: CodeDeliveryDetailsType
    UserSub: str
    Session: str
    ResponseMetadata: ResponseMetadata


class UpdateUserAttributesResponse(BaseValidatorModel):
    CodeDeliveryDetailsList: List[CodeDeliveryDetailsType]
    ResponseMetadata: ResponseMetadata


class CompromisedCredentialsRiskConfigurationTypeOutput(BaseValidatorModel):
    Actions: CompromisedCredentialsActionsType
    EventFilter: Optional[List[EventFilterTypeType]] = None


class CompromisedCredentialsRiskConfigurationType(BaseValidatorModel):
    Actions: CompromisedCredentialsActionsType
    EventFilter: Optional[List[EventFilterTypeType]] = None


class ConfirmDeviceRequest(BaseValidatorModel):
    AccessToken: str
    DeviceKey: str
    DeviceSecretVerifierConfig: Optional[DeviceSecretVerifierConfigType] = None
    DeviceName: Optional[str] = None


class ConfirmForgotPasswordRequest(BaseValidatorModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    Password: str
    SecretHash: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    UserContextData: Optional[UserContextDataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class ConfirmSignUpRequest(BaseValidatorModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    SecretHash: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    UserContextData: Optional[UserContextDataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None
    Session: Optional[str] = None


class ForgotPasswordRequest(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataType] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class InitiateAuthRequest(BaseValidatorModel):
    AuthFlow: AuthFlowTypeType
    ClientId: str
    AuthParameters: Optional[Dict[str, str]] = None
    ClientMetadata: Optional[Dict[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    UserContextData: Optional[UserContextDataType] = None
    Session: Optional[str] = None


class ResendConfirmationCodeRequest(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataType] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class RespondToAuthChallengeRequest(BaseValidatorModel):
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    Session: Optional[str] = None
    ChallengeResponses: Optional[Dict[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    UserContextData: Optional[UserContextDataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class SignUpRequest(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    Password: Optional[str] = None
    UserAttributes: Optional[List[AttributeType]] = None
    ValidationData: Optional[List[AttributeType]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    UserContextData: Optional[UserContextDataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class ContextDataType(BaseValidatorModel):
    IpAddress: str
    ServerName: str
    ServerPath: str
    HttpHeaders: List[HttpHeader]
    EncodedData: Optional[str] = None


class CreateIdentityProviderResponse(BaseValidatorModel):
    IdentityProvider: IdentityProviderType
    ResponseMetadata: ResponseMetadata


class DescribeIdentityProviderResponse(BaseValidatorModel):
    IdentityProvider: IdentityProviderType
    ResponseMetadata: ResponseMetadata


class GetIdentityProviderByIdentifierResponse(BaseValidatorModel):
    IdentityProvider: IdentityProviderType
    ResponseMetadata: ResponseMetadata


class UpdateIdentityProviderResponse(BaseValidatorModel):
    IdentityProvider: IdentityProviderType
    ResponseMetadata: ResponseMetadata


class CreateResourceServerRequest(BaseValidatorModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[List[ResourceServerScopeType]] = None


class ResourceServerType(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    Identifier: Optional[str] = None
    Name: Optional[str] = None
    Scopes: Optional[List[ResourceServerScopeType]] = None


class UpdateResourceServerRequest(BaseValidatorModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[List[ResourceServerScopeType]] = None


class CreateUserImportJobResponse(BaseValidatorModel):
    UserImportJob: UserImportJobType
    ResponseMetadata: ResponseMetadata


class DescribeUserImportJobResponse(BaseValidatorModel):
    UserImportJob: UserImportJobType
    ResponseMetadata: ResponseMetadata


class ListUserImportJobsResponse(BaseValidatorModel):
    UserImportJobs: List[UserImportJobType]
    PaginationToken: str
    ResponseMetadata: ResponseMetadata


class StartUserImportJobResponse(BaseValidatorModel):
    UserImportJob: UserImportJobType
    ResponseMetadata: ResponseMetadata


class StopUserImportJobResponse(BaseValidatorModel):
    UserImportJob: UserImportJobType
    ResponseMetadata: ResponseMetadata


class CreateUserPoolClientRequest(BaseValidatorModel):
    UserPoolId: str
    ClientName: str
    GenerateSecret: Optional[bool] = None
    RefreshTokenValidity: Optional[int] = None
    AccessTokenValidity: Optional[int] = None
    IdTokenValidity: Optional[int] = None
    TokenValidityUnits: Optional[TokenValidityUnitsType] = None
    ReadAttributes: Optional[List[str]] = None
    WriteAttributes: Optional[List[str]] = None
    ExplicitAuthFlows: Optional[List[ExplicitAuthFlowsTypeType]] = None
    SupportedIdentityProviders: Optional[List[str]] = None
    CallbackURLs: Optional[List[str]] = None
    LogoutURLs: Optional[List[str]] = None
    DefaultRedirectURI: Optional[str] = None
    AllowedOAuthFlows: Optional[List[OAuthFlowTypeType]] = None
    AllowedOAuthScopes: Optional[List[str]] = None
    AllowedOAuthFlowsUserPoolClient: Optional[bool] = None
    AnalyticsConfiguration: Optional[AnalyticsConfigurationType] = None
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypesType] = None
    EnableTokenRevocation: Optional[bool] = None
    EnablePropagateAdditionalUserContextData: Optional[bool] = None
    AuthSessionValidity: Optional[int] = None


class UpdateUserPoolClientRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    ClientName: Optional[str] = None
    RefreshTokenValidity: Optional[int] = None
    AccessTokenValidity: Optional[int] = None
    IdTokenValidity: Optional[int] = None
    TokenValidityUnits: Optional[TokenValidityUnitsType] = None
    ReadAttributes: Optional[List[str]] = None
    WriteAttributes: Optional[List[str]] = None
    ExplicitAuthFlows: Optional[List[ExplicitAuthFlowsTypeType]] = None
    SupportedIdentityProviders: Optional[List[str]] = None
    CallbackURLs: Optional[List[str]] = None
    LogoutURLs: Optional[List[str]] = None
    DefaultRedirectURI: Optional[str] = None
    AllowedOAuthFlows: Optional[List[OAuthFlowTypeType]] = None
    AllowedOAuthScopes: Optional[List[str]] = None
    AllowedOAuthFlowsUserPoolClient: Optional[bool] = None
    AnalyticsConfiguration: Optional[AnalyticsConfigurationType] = None
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypesType] = None
    EnableTokenRevocation: Optional[bool] = None
    EnablePropagateAdditionalUserContextData: Optional[bool] = None
    AuthSessionValidity: Optional[int] = None


class UserPoolClientType(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientName: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None
    RefreshTokenValidity: Optional[int] = None
    AccessTokenValidity: Optional[int] = None
    IdTokenValidity: Optional[int] = None
    TokenValidityUnits: Optional[TokenValidityUnitsType] = None
    ReadAttributes: Optional[List[str]] = None
    WriteAttributes: Optional[List[str]] = None
    ExplicitAuthFlows: Optional[List[ExplicitAuthFlowsTypeType]] = None
    SupportedIdentityProviders: Optional[List[str]] = None
    CallbackURLs: Optional[List[str]] = None
    LogoutURLs: Optional[List[str]] = None
    DefaultRedirectURI: Optional[str] = None
    AllowedOAuthFlows: Optional[List[OAuthFlowTypeType]] = None
    AllowedOAuthScopes: Optional[List[str]] = None
    AllowedOAuthFlowsUserPoolClient: Optional[bool] = None
    AnalyticsConfiguration: Optional[AnalyticsConfigurationType] = None
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypesType] = None
    EnableTokenRevocation: Optional[bool] = None
    EnablePropagateAdditionalUserContextData: Optional[bool] = None
    AuthSessionValidity: Optional[int] = None


class CreateUserPoolDomainRequest(BaseValidatorModel):
    Domain: str
    UserPoolId: str
    ManagedLoginVersion: Optional[int] = None
    CustomDomainConfig: Optional[CustomDomainConfigType] = None


class DomainDescriptionType(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    AWSAccountId: Optional[str] = None
    Domain: Optional[str] = None
    S3Bucket: Optional[str] = None
    CloudFrontDistribution: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[DomainStatusTypeType] = None
    CustomDomainConfig: Optional[CustomDomainConfigType] = None
    ManagedLoginVersion: Optional[int] = None


class UpdateUserPoolDomainRequest(BaseValidatorModel):
    Domain: str
    UserPoolId: str
    ManagedLoginVersion: Optional[int] = None
    CustomDomainConfig: Optional[CustomDomainConfigType] = None


class SmsMfaConfigType(BaseValidatorModel):
    SmsAuthenticationMessage: Optional[str] = None
    SmsConfiguration: Optional[SmsConfigurationType] = None


class GetUICustomizationResponse(BaseValidatorModel):
    UICustomization: UICustomizationType
    ResponseMetadata: ResponseMetadata


class SetUICustomizationResponse(BaseValidatorModel):
    UICustomization: UICustomizationType
    ResponseMetadata: ResponseMetadata


class LambdaConfigType(BaseValidatorModel):
    PreSignUp: Optional[str] = None
    CustomMessage: Optional[str] = None
    PostConfirmation: Optional[str] = None
    PreAuthentication: Optional[str] = None
    PostAuthentication: Optional[str] = None
    DefineAuthChallenge: Optional[str] = None
    CreateAuthChallenge: Optional[str] = None
    VerifyAuthChallengeResponse: Optional[str] = None
    PreTokenGeneration: Optional[str] = None
    UserMigration: Optional[str] = None
    PreTokenGenerationConfig: Optional[PreTokenGenerationVersionConfigType] = None
    CustomSMSSender: Optional[CustomSMSLambdaVersionConfigType] = None
    CustomEmailSender: Optional[CustomEmailLambdaVersionConfigType] = None
    KMSKeyID: Optional[str] = None


class ListIdentityProvidersResponse(BaseValidatorModel):
    Providers: List[ProviderDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUserPoolClientsResponse(BaseValidatorModel):
    UserPoolClients: List[UserPoolClientDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWebAuthnCredentialsResponse(BaseValidatorModel):
    Credentials: List[WebAuthnCredentialDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LogConfigurationType(BaseValidatorModel):
    LogLevel: LogLevelType
    EventSource: EventSourceNameType
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationType] = None
    S3Configuration: Optional[S3ConfigurationType] = None
    FirehoseConfiguration: Optional[FirehoseConfigurationType] = None


class NotifyConfigurationType(BaseValidatorModel):
    SourceArn: str
    From: Optional[str] = None
    ReplyTo: Optional[str] = None
    BlockEmail: Optional[NotifyEmailType] = None
    NoActionEmail: Optional[NotifyEmailType] = None
    MfaEmail: Optional[NotifyEmailType] = None

RiskExceptionConfigurationTypeUnion = Union[RiskExceptionConfigurationType, RiskExceptionConfigurationTypeOutput]


class SchemaAttributeType(BaseValidatorModel):
    Name: Optional[str] = None
    AttributeDataType: Optional[AttributeDataTypeType] = None
    DeveloperOnlyAttribute: Optional[bool] = None
    Mutable: Optional[bool] = None
    Required: Optional[bool] = None
    NumberAttributeConstraints: Optional[NumberAttributeConstraintsType] = None
    StringAttributeConstraints: Optional[StringAttributeConstraintsType] = None


class UserPoolPolicyTypeOutput(BaseValidatorModel):
    PasswordPolicy: Optional[PasswordPolicyType] = None
    SignInPolicy: Optional[SignInPolicyTypeOutput] = None


class UserPoolPolicyType(BaseValidatorModel):
    PasswordPolicy: Optional[PasswordPolicyType] = None
    SignInPolicy: Optional[SignInPolicyType] = None

UserAttributeUpdateSettingsTypeUnion = Union[UserAttributeUpdateSettingsType, UserAttributeUpdateSettingsTypeOutput]

AccountRecoverySettingTypeUnion = Union[AccountRecoverySettingType, AccountRecoverySettingTypeOutput]


class AdminGetDeviceResponse(BaseValidatorModel):
    Device: DeviceType
    ResponseMetadata: ResponseMetadata


class AdminListDevicesResponse(BaseValidatorModel):
    Devices: List[DeviceType]
    PaginationToken: str
    ResponseMetadata: ResponseMetadata


class GetDeviceResponse(BaseValidatorModel):
    Device: DeviceType
    ResponseMetadata: ResponseMetadata


class ListDevicesResponse(BaseValidatorModel):
    Devices: List[DeviceType]
    PaginationToken: str
    ResponseMetadata: ResponseMetadata


class AdminCreateUserResponse(BaseValidatorModel):
    User: UserType
    ResponseMetadata: ResponseMetadata


class ListUsersInGroupResponse(BaseValidatorModel):
    Users: List[UserType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsersResponse(BaseValidatorModel):
    Users: List[UserType]
    PaginationToken: str
    ResponseMetadata: ResponseMetadata


class CreateManagedLoginBrandingResponse(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingType
    ResponseMetadata: ResponseMetadata


class DescribeManagedLoginBrandingByClientResponse(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingType
    ResponseMetadata: ResponseMetadata


class DescribeManagedLoginBrandingResponse(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingType
    ResponseMetadata: ResponseMetadata


class UpdateManagedLoginBrandingResponse(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingType
    ResponseMetadata: ResponseMetadata

AssetTypeUnion = Union[AssetType, AssetTypeOutput]


class AdminListUserAuthEventsResponse(BaseValidatorModel):
    AuthEvents: List[AuthEventType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AdminInitiateAuthResponse(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultType
    AvailableChallenges: List[ChallengeNameTypeType]
    ResponseMetadata: ResponseMetadata


class AdminRespondToAuthChallengeResponse(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultType
    ResponseMetadata: ResponseMetadata


class InitiateAuthResponse(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultType
    AvailableChallenges: List[ChallengeNameTypeType]
    ResponseMetadata: ResponseMetadata


class RespondToAuthChallengeResponse(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultType
    ResponseMetadata: ResponseMetadata

CompromisedCredentialsRiskConfigurationTypeUnion = Union[CompromisedCredentialsRiskConfigurationType, CompromisedCredentialsRiskConfigurationTypeOutput]


class AdminInitiateAuthRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    AuthFlow: AuthFlowTypeType
    AuthParameters: Optional[Dict[str, str]] = None
    ClientMetadata: Optional[Dict[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    ContextData: Optional[ContextDataType] = None
    Session: Optional[str] = None


class AdminRespondToAuthChallengeRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    ChallengeResponses: Optional[Dict[str, str]] = None
    Session: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataType] = None
    ContextData: Optional[ContextDataType] = None
    ClientMetadata: Optional[Dict[str, str]] = None


class CreateResourceServerResponse(BaseValidatorModel):
    ResourceServer: ResourceServerType
    ResponseMetadata: ResponseMetadata


class DescribeResourceServerResponse(BaseValidatorModel):
    ResourceServer: ResourceServerType
    ResponseMetadata: ResponseMetadata


class ListResourceServersResponse(BaseValidatorModel):
    ResourceServers: List[ResourceServerType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateResourceServerResponse(BaseValidatorModel):
    ResourceServer: ResourceServerType
    ResponseMetadata: ResponseMetadata


class CreateUserPoolClientResponse(BaseValidatorModel):
    UserPoolClient: UserPoolClientType
    ResponseMetadata: ResponseMetadata


class DescribeUserPoolClientResponse(BaseValidatorModel):
    UserPoolClient: UserPoolClientType
    ResponseMetadata: ResponseMetadata


class UpdateUserPoolClientResponse(BaseValidatorModel):
    UserPoolClient: UserPoolClientType
    ResponseMetadata: ResponseMetadata


class DescribeUserPoolDomainResponse(BaseValidatorModel):
    DomainDescription: DomainDescriptionType
    ResponseMetadata: ResponseMetadata


class GetUserPoolMfaConfigResponse(BaseValidatorModel):
    SmsMfaConfiguration: SmsMfaConfigType
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigType
    EmailMfaConfiguration: EmailMfaConfigType
    MfaConfiguration: UserPoolMfaTypeType
    WebAuthnConfiguration: WebAuthnConfigurationType
    ResponseMetadata: ResponseMetadata


class SetUserPoolMfaConfigRequest(BaseValidatorModel):
    UserPoolId: str
    SmsMfaConfiguration: Optional[SmsMfaConfigType] = None
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigType] = None
    EmailMfaConfiguration: Optional[EmailMfaConfigType] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    WebAuthnConfiguration: Optional[WebAuthnConfigurationType] = None


class SetUserPoolMfaConfigResponse(BaseValidatorModel):
    SmsMfaConfiguration: SmsMfaConfigType
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigType
    EmailMfaConfiguration: EmailMfaConfigType
    MfaConfiguration: UserPoolMfaTypeType
    WebAuthnConfiguration: WebAuthnConfigurationType
    ResponseMetadata: ResponseMetadata


class UserPoolDescriptionType(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    LambdaConfig: Optional[LambdaConfigType] = None
    Status: Optional[StatusTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class LogDeliveryConfigurationType(BaseValidatorModel):
    UserPoolId: str
    LogConfigurations: List[LogConfigurationType]


class SetLogDeliveryConfigurationRequest(BaseValidatorModel):
    UserPoolId: str
    LogConfigurations: List[LogConfigurationType]


class AccountTakeoverRiskConfigurationType(BaseValidatorModel):
    Actions: AccountTakeoverActionsType
    NotifyConfiguration: Optional[NotifyConfigurationType] = None


class AddCustomAttributesRequest(BaseValidatorModel):
    UserPoolId: str
    CustomAttributes: List[SchemaAttributeType]


class UserPoolType(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Policies: Optional[UserPoolPolicyTypeOutput] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigType] = None
    Status: Optional[StatusTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None
    SchemaAttributes: Optional[List[SchemaAttributeType]] = None
    AutoVerifiedAttributes: Optional[List[VerifiedAttributeTypeType]] = None
    AliasAttributes: Optional[List[AliasAttributeTypeType]] = None
    UsernameAttributes: Optional[List[UsernameAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateType] = None
    SmsAuthenticationMessage: Optional[str] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeOutput] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    DeviceConfiguration: Optional[DeviceConfigurationType] = None
    EstimatedNumberOfUsers: Optional[int] = None
    EmailConfiguration: Optional[EmailConfigurationType] = None
    SmsConfiguration: Optional[SmsConfigurationType] = None
    UserPoolTags: Optional[Dict[str, str]] = None
    SmsConfigurationFailure: Optional[str] = None
    EmailConfigurationFailure: Optional[str] = None
    Domain: Optional[str] = None
    CustomDomain: Optional[str] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigType] = None
    UserPoolAddOns: Optional[UserPoolAddOnsType] = None
    UsernameConfiguration: Optional[UsernameConfigurationType] = None
    Arn: Optional[str] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeOutput] = None
    UserPoolTier: Optional[UserPoolTierTypeType] = None

UserPoolPolicyTypeUnion = Union[UserPoolPolicyType, UserPoolPolicyTypeOutput]


class CreateManagedLoginBrandingRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    UseCognitoProvidedValues: Optional[bool] = None
    Settings: Optional[Dict[str, Any]] = None
    Assets: Optional[List[AssetTypeUnion]] = None


class UpdateManagedLoginBrandingRequest(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ManagedLoginBrandingId: Optional[str] = None
    UseCognitoProvidedValues: Optional[bool] = None
    Settings: Optional[Dict[str, Any]] = None
    Assets: Optional[List[AssetTypeUnion]] = None


class ListUserPoolsResponse(BaseValidatorModel):
    UserPools: List[UserPoolDescriptionType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetLogDeliveryConfigurationResponse(BaseValidatorModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationType
    ResponseMetadata: ResponseMetadata


class SetLogDeliveryConfigurationResponse(BaseValidatorModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationType
    ResponseMetadata: ResponseMetadata


class RiskConfigurationType(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[CompromisedCredentialsRiskConfigurationTypeOutput] = None
    AccountTakeoverRiskConfiguration: Optional[AccountTakeoverRiskConfigurationType] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeOutput] = None
    LastModifiedDate: Optional[datetime] = None


class SetRiskConfigurationRequest(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[CompromisedCredentialsRiskConfigurationTypeUnion] = None
    AccountTakeoverRiskConfiguration: Optional[AccountTakeoverRiskConfigurationType] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeUnion] = None


class CreateUserPoolResponse(BaseValidatorModel):
    UserPool: UserPoolType
    ResponseMetadata: ResponseMetadata


class DescribeUserPoolResponse(BaseValidatorModel):
    UserPool: UserPoolType
    ResponseMetadata: ResponseMetadata


class CreateUserPoolRequest(BaseValidatorModel):
    PoolName: str
    Policies: Optional[UserPoolPolicyTypeUnion] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigType] = None
    AutoVerifiedAttributes: Optional[List[VerifiedAttributeTypeType]] = None
    AliasAttributes: Optional[List[AliasAttributeTypeType]] = None
    UsernameAttributes: Optional[List[UsernameAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateType] = None
    SmsAuthenticationMessage: Optional[str] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeUnion] = None
    DeviceConfiguration: Optional[DeviceConfigurationType] = None
    EmailConfiguration: Optional[EmailConfigurationType] = None
    SmsConfiguration: Optional[SmsConfigurationType] = None
    UserPoolTags: Optional[Dict[str, str]] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigType] = None
    Schema: Optional[List[SchemaAttributeType]] = None
    UserPoolAddOns: Optional[UserPoolAddOnsType] = None
    UsernameConfiguration: Optional[UsernameConfigurationType] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeUnion] = None
    UserPoolTier: Optional[UserPoolTierTypeType] = None


class UpdateUserPoolRequest(BaseValidatorModel):
    UserPoolId: str
    Policies: Optional[UserPoolPolicyTypeUnion] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigType] = None
    AutoVerifiedAttributes: Optional[List[VerifiedAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateType] = None
    SmsAuthenticationMessage: Optional[str] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeUnion] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    DeviceConfiguration: Optional[DeviceConfigurationType] = None
    EmailConfiguration: Optional[EmailConfigurationType] = None
    SmsConfiguration: Optional[SmsConfigurationType] = None
    UserPoolTags: Optional[Dict[str, str]] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigType] = None
    UserPoolAddOns: Optional[UserPoolAddOnsType] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeUnion] = None
    PoolName: Optional[str] = None
    UserPoolTier: Optional[UserPoolTierTypeType] = None


class DescribeRiskConfigurationResponse(BaseValidatorModel):
    RiskConfiguration: RiskConfigurationType
    ResponseMetadata: ResponseMetadata


class SetRiskConfigurationResponse(BaseValidatorModel):
    RiskConfiguration: RiskConfigurationType
    ResponseMetadata: ResponseMetadata