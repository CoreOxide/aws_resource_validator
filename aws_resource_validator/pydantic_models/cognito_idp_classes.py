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
from aws_resource_validator.pydantic_models.cognito_idp_constants import *

class RecoveryOptionTypeTypeDef(BaseValidatorModel):
    Priority: int
    Name: RecoveryOptionNameTypeType


class AccountTakeoverActionTypeTypeDef(BaseValidatorModel):
    Notify: bool
    EventAction: AccountTakeoverEventActionTypeType


class AdminAddUserToGroupRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    GroupName: str


class AdminConfirmSignUpRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Mapping[str, str]] = None


class MessageTemplateTypeTypeDef(BaseValidatorModel):
    SMSMessage: Optional[str] = None
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None


class AttributeTypeTypeDef(BaseValidatorModel):
    Name: str
    Value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AdminDeleteUserAttributesRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributeNames: Sequence[str]


class AdminDeleteUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str


class ProviderUserIdentifierTypeTypeDef(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ProviderAttributeName: Optional[str] = None
    ProviderAttributeValue: Optional[str] = None


class AdminDisableUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str


class AdminEnableUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str


class AdminForgetDeviceRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    DeviceKey: str


class AdminGetDeviceRequestTypeDef(BaseValidatorModel):
    DeviceKey: str
    UserPoolId: str
    Username: str


class AdminGetUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str


class MFAOptionTypeTypeDef(BaseValidatorModel):
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None


class AnalyticsMetadataTypeTypeDef(BaseValidatorModel):
    AnalyticsEndpointId: Optional[str] = None


class AdminListDevicesRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class AdminListGroupsForUserRequestTypeDef(BaseValidatorModel):
    Username: str
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GroupTypeTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    UserPoolId: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class AdminListUserAuthEventsRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AdminRemoveUserFromGroupRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    GroupName: str


class AdminResetUserPasswordRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Mapping[str, str]] = None


class EmailMfaSettingsTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None


class SMSMfaSettingsTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None


class SoftwareTokenMfaSettingsTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None


class AdminSetUserPasswordRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    Password: str
    Permanent: Optional[bool] = None


class AdminUpdateAuthEventFeedbackRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackValue: FeedbackValueTypeType


class AdminUpdateDeviceStatusRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None


class AdminUserGlobalSignOutRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str


class AdvancedSecurityAdditionalFlowsTypeTypeDef(BaseValidatorModel):
    CustomAuthMode: Optional[AdvancedSecurityEnabledModeTypeType] = None


class AnalyticsConfigurationTypeTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    RoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    UserDataShared: Optional[bool] = None


class AssetTypeOutputTypeDef(BaseValidatorModel):
    Category: AssetCategoryTypeType
    ColorMode: ColorSchemeModeTypeType
    Extension: AssetExtensionTypeType
    Bytes: Optional[bytes] = None
    ResourceId: Optional[str] = None


class AssociateSoftwareTokenRequestTypeDef(BaseValidatorModel):
    AccessToken: Optional[str] = None
    Session: Optional[str] = None


class ChallengeResponseTypeTypeDef(BaseValidatorModel):
    ChallengeName: Optional[ChallengeNameType] = None
    ChallengeResponse: Optional[ChallengeResponseType] = None


class EventContextDataTypeTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    DeviceName: Optional[str] = None
    Timezone: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None


class EventFeedbackTypeTypeDef(BaseValidatorModel):
    FeedbackValue: FeedbackValueTypeType
    Provider: str
    FeedbackDate: Optional[datetime] = None


class EventRiskTypeTypeDef(BaseValidatorModel):
    RiskDecision: Optional[RiskDecisionTypeType] = None
    RiskLevel: Optional[RiskLevelTypeType] = None
    CompromisedCredentialsDetected: Optional[bool] = None


class NewDeviceMetadataTypeTypeDef(BaseValidatorModel):
    DeviceKey: Optional[str] = None
    DeviceGroupKey: Optional[str] = None


class ChangePasswordRequestTypeDef(BaseValidatorModel):
    ProposedPassword: str
    AccessToken: str
    PreviousPassword: Optional[str] = None


class CloudWatchLogsConfigurationTypeTypeDef(BaseValidatorModel):
    LogGroupArn: Optional[str] = None


class CodeDeliveryDetailsTypeTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None


class CompleteWebAuthnRegistrationRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    Credential: Mapping[str, Any]


class CompromisedCredentialsActionsTypeTypeDef(BaseValidatorModel):
    EventAction: CompromisedCredentialsEventActionTypeType


class DeviceSecretVerifierConfigTypeTypeDef(BaseValidatorModel):
    PasswordVerifier: Optional[str] = None
    Salt: Optional[str] = None


class UserContextDataTypeTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    EncodedData: Optional[str] = None


class HttpHeaderTypeDef(BaseValidatorModel):
    headerName: Optional[str] = None
    headerValue: Optional[str] = None


class CreateGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None


class CreateIdentityProviderRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str
    ProviderType: IdentityProviderTypeTypeType
    ProviderDetails: Mapping[str, str]
    AttributeMapping: Optional[Mapping[str, str]] = None
    IdpIdentifiers: Optional[Sequence[str]] = None


class IdentityProviderTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    ProviderDetails: Optional[Dict[str, str]] = None
    AttributeMapping: Optional[Dict[str, str]] = None
    IdpIdentifiers: Optional[List[str]] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class ResourceServerScopeTypeTypeDef(BaseValidatorModel):
    ScopeName: str
    ScopeDescription: str


class CreateUserImportJobRequestTypeDef(BaseValidatorModel):
    JobName: str
    UserPoolId: str
    CloudWatchLogsRoleArn: str


class UserImportJobTypeTypeDef(BaseValidatorModel):
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


class TokenValidityUnitsTypeTypeDef(BaseValidatorModel):
    AccessToken: Optional[TimeUnitsTypeType] = None
    IdToken: Optional[TimeUnitsTypeType] = None
    RefreshToken: Optional[TimeUnitsTypeType] = None


class CustomDomainConfigTypeTypeDef(BaseValidatorModel):
    CertificateArn: str


class DeviceConfigurationTypeTypeDef(BaseValidatorModel):
    ChallengeRequiredOnNewDevice: Optional[bool] = None
    DeviceOnlyRememberedOnUserPrompt: Optional[bool] = None


class EmailConfigurationTypeTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None
    ReplyToEmailAddress: Optional[str] = None
    EmailSendingAccount: Optional[EmailSendingAccountTypeType] = None
    From: Optional[str] = None
    ConfigurationSet: Optional[str] = None


class SmsConfigurationTypeTypeDef(BaseValidatorModel):
    SnsCallerArn: str
    ExternalId: Optional[str] = None
    SnsRegion: Optional[str] = None


class UsernameConfigurationTypeTypeDef(BaseValidatorModel):
    CaseSensitive: bool


class VerificationMessageTemplateTypeTypeDef(BaseValidatorModel):
    SmsMessage: Optional[str] = None
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None
    EmailMessageByLink: Optional[str] = None
    EmailSubjectByLink: Optional[str] = None
    DefaultEmailOption: Optional[DefaultEmailOptionTypeType] = None


class CustomEmailLambdaVersionConfigTypeTypeDef(BaseValidatorModel):
    LambdaVersion: Literal["V1_0"]
    LambdaArn: str


class CustomSMSLambdaVersionConfigTypeTypeDef(BaseValidatorModel):
    LambdaVersion: Literal["V1_0"]
    LambdaArn: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str


class DeleteIdentityProviderRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str


class DeleteManagedLoginBrandingRequestTypeDef(BaseValidatorModel):
    ManagedLoginBrandingId: str
    UserPoolId: str


class DeleteResourceServerRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str


class DeleteUserAttributesRequestTypeDef(BaseValidatorModel):
    UserAttributeNames: Sequence[str]
    AccessToken: str


class DeleteUserPoolClientRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str


class DeleteUserPoolDomainRequestTypeDef(BaseValidatorModel):
    Domain: str
    UserPoolId: str


class DeleteUserPoolRequestTypeDef(BaseValidatorModel):
    UserPoolId: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    AccessToken: str


class DeleteWebAuthnCredentialRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    CredentialId: str


class DescribeIdentityProviderRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str


class DescribeManagedLoginBrandingByClientRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    ReturnMergedResources: Optional[bool] = None


class DescribeManagedLoginBrandingRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ManagedLoginBrandingId: str
    ReturnMergedResources: Optional[bool] = None


class DescribeResourceServerRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str


class DescribeRiskConfigurationRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None


class DescribeUserImportJobRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    JobId: str


class DescribeUserPoolClientRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str


class DescribeUserPoolDomainRequestTypeDef(BaseValidatorModel):
    Domain: str


class DescribeUserPoolRequestTypeDef(BaseValidatorModel):
    UserPoolId: str


class EmailMfaConfigTypeTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Subject: Optional[str] = None


class FirehoseConfigurationTypeTypeDef(BaseValidatorModel):
    StreamArn: Optional[str] = None


class ForgetDeviceRequestTypeDef(BaseValidatorModel):
    DeviceKey: str
    AccessToken: Optional[str] = None


class GetCSVHeaderRequestTypeDef(BaseValidatorModel):
    UserPoolId: str


class GetDeviceRequestTypeDef(BaseValidatorModel):
    DeviceKey: str
    AccessToken: Optional[str] = None


class GetGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str


class GetIdentityProviderByIdentifierRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    IdpIdentifier: str


class GetLogDeliveryConfigurationRequestTypeDef(BaseValidatorModel):
    UserPoolId: str


class GetSigningCertificateRequestTypeDef(BaseValidatorModel):
    UserPoolId: str


class GetUICustomizationRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None


class UICustomizationTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    ImageUrl: Optional[str] = None
    CSS: Optional[str] = None
    CSSVersion: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class GetUserAttributeVerificationCodeRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    AttributeName: str
    ClientMetadata: Optional[Mapping[str, str]] = None


class GetUserAuthFactorsRequestTypeDef(BaseValidatorModel):
    AccessToken: str


class GetUserPoolMfaConfigRequestTypeDef(BaseValidatorModel):
    UserPoolId: str


class SoftwareTokenMfaConfigTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None


class WebAuthnConfigurationTypeTypeDef(BaseValidatorModel):
    RelyingPartyId: Optional[str] = None
    UserVerification: Optional[UserVerificationTypeType] = None


class GetUserRequestTypeDef(BaseValidatorModel):
    AccessToken: str


class GlobalSignOutRequestTypeDef(BaseValidatorModel):
    AccessToken: str


class PreTokenGenerationVersionConfigTypeTypeDef(BaseValidatorModel):
    LambdaVersion: PreTokenGenerationLambdaVersionTypeType
    LambdaArn: str


class ListDevicesRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListIdentityProvidersRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProviderDescriptionTypeDef(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class ListResourceServersRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListUserImportJobsRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: int
    PaginationToken: Optional[str] = None


class ListUserPoolClientsRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UserPoolClientDescriptionTypeDef(BaseValidatorModel):
    ClientId: Optional[str] = None
    UserPoolId: Optional[str] = None
    ClientName: Optional[str] = None


class ListUserPoolsRequestTypeDef(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None


class ListUsersInGroupRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    GroupName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None
    Filter: Optional[str] = None


class ListWebAuthnCredentialsRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class WebAuthnCredentialDescriptionTypeDef(BaseValidatorModel):
    CredentialId: str
    FriendlyCredentialName: str
    RelyingPartyId: str
    AuthenticatorTransports: List[str]
    CreatedAt: datetime
    AuthenticatorAttachment: Optional[str] = None


class S3ConfigurationTypeTypeDef(BaseValidatorModel):
    BucketArn: Optional[str] = None


class NotifyEmailTypeTypeDef(BaseValidatorModel):
    Subject: str
    HtmlBody: Optional[str] = None
    TextBody: Optional[str] = None


class NumberAttributeConstraintsTypeTypeDef(BaseValidatorModel):
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None


class PasswordPolicyTypeTypeDef(BaseValidatorModel):
    MinimumLength: Optional[int] = None
    RequireUppercase: Optional[bool] = None
    RequireLowercase: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireSymbols: Optional[bool] = None
    PasswordHistorySize: Optional[int] = None
    TemporaryPasswordValidityDays: Optional[int] = None


class RevokeTokenRequestTypeDef(BaseValidatorModel):
    Token: str
    ClientId: str
    ClientSecret: Optional[str] = None


class RiskExceptionConfigurationTypeOutputTypeDef(BaseValidatorModel):
    BlockedIPRangeList: Optional[List[str]] = None
    SkippedIPRangeList: Optional[List[str]] = None


class RiskExceptionConfigurationTypeTypeDef(BaseValidatorModel):
    BlockedIPRangeList: Optional[Sequence[str]] = None
    SkippedIPRangeList: Optional[Sequence[str]] = None


class StringAttributeConstraintsTypeTypeDef(BaseValidatorModel):
    MinLength: Optional[str] = None
    MaxLength: Optional[str] = None


class SignInPolicyTypeOutputTypeDef(BaseValidatorModel):
    AllowedFirstAuthFactors: Optional[List[AuthFactorTypeType]] = None


class SignInPolicyTypeTypeDef(BaseValidatorModel):
    AllowedFirstAuthFactors: Optional[Sequence[AuthFactorTypeType]] = None


class StartUserImportJobRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    JobId: str


class StartWebAuthnRegistrationRequestTypeDef(BaseValidatorModel):
    AccessToken: str


class StopUserImportJobRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    JobId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateAuthEventFeedbackRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackToken: str
    FeedbackValue: FeedbackValueTypeType


class UpdateDeviceStatusRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None


class UpdateIdentityProviderRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str
    ProviderDetails: Optional[Mapping[str, str]] = None
    AttributeMapping: Optional[Mapping[str, str]] = None
    IdpIdentifiers: Optional[Sequence[str]] = None


class UserAttributeUpdateSettingsTypeOutputTypeDef(BaseValidatorModel):
    AttributesRequireVerificationBeforeUpdate: Optional[List[VerifiedAttributeTypeType]] = None


class UserAttributeUpdateSettingsTypeTypeDef(BaseValidatorModel):
    AttributesRequireVerificationBeforeUpdate: Optional[Sequence[VerifiedAttributeTypeType]] = None


class VerifySoftwareTokenRequestTypeDef(BaseValidatorModel):
    UserCode: str
    AccessToken: Optional[str] = None
    Session: Optional[str] = None
    FriendlyDeviceName: Optional[str] = None


class VerifyUserAttributeRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    AttributeName: str
    Code: str


class AccountRecoverySettingTypeOutputTypeDef(BaseValidatorModel):
    RecoveryMechanisms: Optional[List[RecoveryOptionTypeTypeDef]] = None


class AccountRecoverySettingTypeTypeDef(BaseValidatorModel):
    RecoveryMechanisms: Optional[Sequence[RecoveryOptionTypeTypeDef]] = None


class AccountTakeoverActionsTypeTypeDef(BaseValidatorModel):
    LowAction: Optional[AccountTakeoverActionTypeTypeDef] = None
    MediumAction: Optional[AccountTakeoverActionTypeTypeDef] = None
    HighAction: Optional[AccountTakeoverActionTypeTypeDef] = None


class AdminCreateUserConfigTypeTypeDef(BaseValidatorModel):
    AllowAdminCreateUserOnly: Optional[bool] = None
    UnusedAccountValidityDays: Optional[int] = None
    InviteMessageTemplate: Optional[MessageTemplateTypeTypeDef] = None


class AdminCreateUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributes: Optional[Sequence[AttributeTypeTypeDef]] = None
    ValidationData: Optional[Sequence[AttributeTypeTypeDef]] = None
    TemporaryPassword: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    MessageAction: Optional[MessageActionTypeType] = None
    DesiredDeliveryMediums: Optional[Sequence[DeliveryMediumTypeType]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class AdminUpdateUserAttributesRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributes: Sequence[AttributeTypeTypeDef]
    ClientMetadata: Optional[Mapping[str, str]] = None


class DeviceTypeTypeDef(BaseValidatorModel):
    DeviceKey: Optional[str] = None
    DeviceAttributes: Optional[List[AttributeTypeTypeDef]] = None
    DeviceCreateDate: Optional[datetime] = None
    DeviceLastModifiedDate: Optional[datetime] = None
    DeviceLastAuthenticatedDate: Optional[datetime] = None


class UpdateUserAttributesRequestTypeDef(BaseValidatorModel):
    UserAttributes: Sequence[AttributeTypeTypeDef]
    AccessToken: str
    ClientMetadata: Optional[Mapping[str, str]] = None


class AssociateSoftwareTokenResponseTypeDef(BaseValidatorModel):
    SecretCode: str
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmDeviceResponseTypeDef(BaseValidatorModel):
    UserConfirmationNecessary: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmSignUpResponseTypeDef(BaseValidatorModel):
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserPoolDomainResponseTypeDef(BaseValidatorModel):
    ManagedLoginVersion: int
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCSVHeaderResponseTypeDef(BaseValidatorModel):
    UserPoolId: str
    CSVHeader: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSigningCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserAuthFactorsResponseTypeDef(BaseValidatorModel):
    Username: str
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ConfiguredUserAuthFactors: List[AuthFactorTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartWebAuthnRegistrationResponseTypeDef(BaseValidatorModel):
    CredentialCreationOptions: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserPoolDomainResponseTypeDef(BaseValidatorModel):
    ManagedLoginVersion: int
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadataTypeDef


class VerifySoftwareTokenResponseTypeDef(BaseValidatorModel):
    Status: VerifySoftwareTokenResponseTypeType
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef


class AdminDisableProviderForUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    User: ProviderUserIdentifierTypeTypeDef


class AdminLinkProviderForUserRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    DestinationUser: ProviderUserIdentifierTypeTypeDef
    SourceUser: ProviderUserIdentifierTypeTypeDef


class AdminGetUserResponseTypeDef(BaseValidatorModel):
    Username: str
    UserAttributes: List[AttributeTypeTypeDef]
    UserCreateDate: datetime
    UserLastModifiedDate: datetime
    Enabled: bool
    UserStatus: UserStatusTypeType
    MFAOptions: List[MFAOptionTypeTypeDef]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class AdminSetUserSettingsRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    MFAOptions: Sequence[MFAOptionTypeTypeDef]


class GetUserResponseTypeDef(BaseValidatorModel):
    Username: str
    UserAttributes: List[AttributeTypeTypeDef]
    MFAOptions: List[MFAOptionTypeTypeDef]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class SetUserSettingsRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    MFAOptions: Sequence[MFAOptionTypeTypeDef]


class UserTypeTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Attributes: Optional[List[AttributeTypeTypeDef]] = None
    UserCreateDate: Optional[datetime] = None
    UserLastModifiedDate: Optional[datetime] = None
    Enabled: Optional[bool] = None
    UserStatus: Optional[UserStatusTypeType] = None
    MFAOptions: Optional[List[MFAOptionTypeTypeDef]] = None


class AdminListGroupsForUserRequestPaginateTypeDef(BaseValidatorModel):
    Username: str
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class AdminListUserAuthEventsRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIdentityProvidersRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceServersRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserPoolClientsRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserPoolsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersInGroupRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    AttributesToGet: Optional[Sequence[str]] = None
    Filter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class AdminListGroupsForUserResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AdminSetUserMFAPreferenceRequestTypeDef(BaseValidatorModel):
    Username: str
    UserPoolId: str
    SMSMfaSettings: Optional[SMSMfaSettingsTypeTypeDef] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsTypeTypeDef] = None
    EmailMfaSettings: Optional[EmailMfaSettingsTypeTypeDef] = None


class SetUserMFAPreferenceRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    SMSMfaSettings: Optional[SMSMfaSettingsTypeTypeDef] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsTypeTypeDef] = None
    EmailMfaSettings: Optional[EmailMfaSettingsTypeTypeDef] = None


class UserPoolAddOnsTypeTypeDef(BaseValidatorModel):
    AdvancedSecurityMode: AdvancedSecurityModeTypeType
    AdvancedSecurityAdditionalFlows: Optional[AdvancedSecurityAdditionalFlowsTypeTypeDef] = None


class ManagedLoginBrandingTypeTypeDef(BaseValidatorModel):
    ManagedLoginBrandingId: Optional[str] = None
    UserPoolId: Optional[str] = None
    UseCognitoProvidedValues: Optional[bool] = None
    Settings: Optional[Dict[str, Any]] = None
    Assets: Optional[List[AssetTypeOutputTypeDef]] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class AssetTypeTypeDef(BaseValidatorModel):
    Category: AssetCategoryTypeType
    ColorMode: ColorSchemeModeTypeType
    Extension: AssetExtensionTypeType
    Bytes: Optional[BlobTypeDef] = None
    ResourceId: Optional[str] = None


class SetUICustomizationRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CSS: Optional[str] = None
    ImageFile: Optional[BlobTypeDef] = None


class AuthEventTypeTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    EventType: Optional[EventTypeType] = None
    CreationDate: Optional[datetime] = None
    EventResponse: Optional[EventResponseTypeType] = None
    EventRisk: Optional[EventRiskTypeTypeDef] = None
    ChallengeResponses: Optional[List[ChallengeResponseTypeTypeDef]] = None
    EventContextData: Optional[EventContextDataTypeTypeDef] = None
    EventFeedback: Optional[EventFeedbackTypeTypeDef] = None


class AuthenticationResultTypeTypeDef(BaseValidatorModel):
    AccessToken: Optional[str] = None
    ExpiresIn: Optional[int] = None
    TokenType: Optional[str] = None
    RefreshToken: Optional[str] = None
    IdToken: Optional[str] = None
    NewDeviceMetadata: Optional[NewDeviceMetadataTypeTypeDef] = None


class ForgotPasswordResponseTypeDef(BaseValidatorModel):
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserAttributeVerificationCodeResponseTypeDef(BaseValidatorModel):
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResendConfirmationCodeResponseTypeDef(BaseValidatorModel):
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SignUpResponseTypeDef(BaseValidatorModel):
    UserConfirmed: bool
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    UserSub: str
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserAttributesResponseTypeDef(BaseValidatorModel):
    CodeDeliveryDetailsList: List[CodeDeliveryDetailsTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CompromisedCredentialsRiskConfigurationTypeOutputTypeDef(BaseValidatorModel):
    Actions: CompromisedCredentialsActionsTypeTypeDef
    EventFilter: Optional[List[EventFilterTypeType]] = None


class CompromisedCredentialsRiskConfigurationTypeTypeDef(BaseValidatorModel):
    Actions: CompromisedCredentialsActionsTypeTypeDef
    EventFilter: Optional[Sequence[EventFilterTypeType]] = None


class ConfirmDeviceRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    DeviceKey: str
    DeviceSecretVerifierConfig: Optional[DeviceSecretVerifierConfigTypeTypeDef] = None
    DeviceName: Optional[str] = None


class ConfirmForgotPasswordRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    Password: str
    SecretHash: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class ConfirmSignUpRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    SecretHash: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    Session: Optional[str] = None


class ForgotPasswordRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class InitiateAuthRequestTypeDef(BaseValidatorModel):
    AuthFlow: AuthFlowTypeType
    ClientId: str
    AuthParameters: Optional[Mapping[str, str]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    Session: Optional[str] = None


class ResendConfirmationCodeRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class RespondToAuthChallengeRequestTypeDef(BaseValidatorModel):
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    Session: Optional[str] = None
    ChallengeResponses: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class SignUpRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    Password: Optional[str] = None
    UserAttributes: Optional[Sequence[AttributeTypeTypeDef]] = None
    ValidationData: Optional[Sequence[AttributeTypeTypeDef]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class ContextDataTypeTypeDef(BaseValidatorModel):
    IpAddress: str
    ServerName: str
    ServerPath: str
    HttpHeaders: Sequence[HttpHeaderTypeDef]
    EncodedData: Optional[str] = None


class CreateIdentityProviderResponseTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeIdentityProviderResponseTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdentityProviderByIdentifierResponseTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIdentityProviderResponseTypeDef(BaseValidatorModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceServerRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[Sequence[ResourceServerScopeTypeTypeDef]] = None


class ResourceServerTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    Identifier: Optional[str] = None
    Name: Optional[str] = None
    Scopes: Optional[List[ResourceServerScopeTypeTypeDef]] = None


class UpdateResourceServerRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[Sequence[ResourceServerScopeTypeTypeDef]] = None


class CreateUserImportJobResponseTypeDef(BaseValidatorModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserImportJobResponseTypeDef(BaseValidatorModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListUserImportJobsResponseTypeDef(BaseValidatorModel):
    UserImportJobs: List[UserImportJobTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartUserImportJobResponseTypeDef(BaseValidatorModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopUserImportJobResponseTypeDef(BaseValidatorModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserPoolClientRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientName: str
    GenerateSecret: Optional[bool] = None
    RefreshTokenValidity: Optional[int] = None
    AccessTokenValidity: Optional[int] = None
    IdTokenValidity: Optional[int] = None
    TokenValidityUnits: Optional[TokenValidityUnitsTypeTypeDef] = None
    ReadAttributes: Optional[Sequence[str]] = None
    WriteAttributes: Optional[Sequence[str]] = None
    ExplicitAuthFlows: Optional[Sequence[ExplicitAuthFlowsTypeType]] = None
    SupportedIdentityProviders: Optional[Sequence[str]] = None
    CallbackURLs: Optional[Sequence[str]] = None
    LogoutURLs: Optional[Sequence[str]] = None
    DefaultRedirectURI: Optional[str] = None
    AllowedOAuthFlows: Optional[Sequence[OAuthFlowTypeType]] = None
    AllowedOAuthScopes: Optional[Sequence[str]] = None
    AllowedOAuthFlowsUserPoolClient: Optional[bool] = None
    AnalyticsConfiguration: Optional[AnalyticsConfigurationTypeTypeDef] = None
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypesType] = None
    EnableTokenRevocation: Optional[bool] = None
    EnablePropagateAdditionalUserContextData: Optional[bool] = None
    AuthSessionValidity: Optional[int] = None


class UpdateUserPoolClientRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    ClientName: Optional[str] = None
    RefreshTokenValidity: Optional[int] = None
    AccessTokenValidity: Optional[int] = None
    IdTokenValidity: Optional[int] = None
    TokenValidityUnits: Optional[TokenValidityUnitsTypeTypeDef] = None
    ReadAttributes: Optional[Sequence[str]] = None
    WriteAttributes: Optional[Sequence[str]] = None
    ExplicitAuthFlows: Optional[Sequence[ExplicitAuthFlowsTypeType]] = None
    SupportedIdentityProviders: Optional[Sequence[str]] = None
    CallbackURLs: Optional[Sequence[str]] = None
    LogoutURLs: Optional[Sequence[str]] = None
    DefaultRedirectURI: Optional[str] = None
    AllowedOAuthFlows: Optional[Sequence[OAuthFlowTypeType]] = None
    AllowedOAuthScopes: Optional[Sequence[str]] = None
    AllowedOAuthFlowsUserPoolClient: Optional[bool] = None
    AnalyticsConfiguration: Optional[AnalyticsConfigurationTypeTypeDef] = None
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypesType] = None
    EnableTokenRevocation: Optional[bool] = None
    EnablePropagateAdditionalUserContextData: Optional[bool] = None
    AuthSessionValidity: Optional[int] = None


class UserPoolClientTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientName: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None
    RefreshTokenValidity: Optional[int] = None
    AccessTokenValidity: Optional[int] = None
    IdTokenValidity: Optional[int] = None
    TokenValidityUnits: Optional[TokenValidityUnitsTypeTypeDef] = None
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
    AnalyticsConfiguration: Optional[AnalyticsConfigurationTypeTypeDef] = None
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypesType] = None
    EnableTokenRevocation: Optional[bool] = None
    EnablePropagateAdditionalUserContextData: Optional[bool] = None
    AuthSessionValidity: Optional[int] = None


class CreateUserPoolDomainRequestTypeDef(BaseValidatorModel):
    Domain: str
    UserPoolId: str
    ManagedLoginVersion: Optional[int] = None
    CustomDomainConfig: Optional[CustomDomainConfigTypeTypeDef] = None


class DomainDescriptionTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    AWSAccountId: Optional[str] = None
    Domain: Optional[str] = None
    S3Bucket: Optional[str] = None
    CloudFrontDistribution: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[DomainStatusTypeType] = None
    CustomDomainConfig: Optional[CustomDomainConfigTypeTypeDef] = None
    ManagedLoginVersion: Optional[int] = None


class UpdateUserPoolDomainRequestTypeDef(BaseValidatorModel):
    Domain: str
    UserPoolId: str
    ManagedLoginVersion: Optional[int] = None
    CustomDomainConfig: Optional[CustomDomainConfigTypeTypeDef] = None


class SmsMfaConfigTypeTypeDef(BaseValidatorModel):
    SmsAuthenticationMessage: Optional[str] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None


class GetUICustomizationResponseTypeDef(BaseValidatorModel):
    UICustomization: UICustomizationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetUICustomizationResponseTypeDef(BaseValidatorModel):
    UICustomization: UICustomizationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LambdaConfigTypeTypeDef(BaseValidatorModel):
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
    PreTokenGenerationConfig: Optional[PreTokenGenerationVersionConfigTypeTypeDef] = None
    CustomSMSSender: Optional[CustomSMSLambdaVersionConfigTypeTypeDef] = None
    CustomEmailSender: Optional[CustomEmailLambdaVersionConfigTypeTypeDef] = None
    KMSKeyID: Optional[str] = None


class ListIdentityProvidersResponseTypeDef(BaseValidatorModel):
    Providers: List[ProviderDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUserPoolClientsResponseTypeDef(BaseValidatorModel):
    UserPoolClients: List[UserPoolClientDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWebAuthnCredentialsResponseTypeDef(BaseValidatorModel):
    Credentials: List[WebAuthnCredentialDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LogConfigurationTypeTypeDef(BaseValidatorModel):
    LogLevel: LogLevelType
    EventSource: EventSourceNameType
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationTypeTypeDef] = None
    S3Configuration: Optional[S3ConfigurationTypeTypeDef] = None
    FirehoseConfiguration: Optional[FirehoseConfigurationTypeTypeDef] = None


class NotifyConfigurationTypeTypeDef(BaseValidatorModel):
    SourceArn: str
    From: Optional[str] = None
    ReplyTo: Optional[str] = None
    BlockEmail: Optional[NotifyEmailTypeTypeDef] = None
    NoActionEmail: Optional[NotifyEmailTypeTypeDef] = None
    MfaEmail: Optional[NotifyEmailTypeTypeDef] = None


class UserPoolPolicyTypeOutputTypeDef(BaseValidatorModel):
    PasswordPolicy: Optional[PasswordPolicyTypeTypeDef] = None
    SignInPolicy: Optional[SignInPolicyTypeOutputTypeDef] = None


class UserPoolPolicyTypeTypeDef(BaseValidatorModel):
    PasswordPolicy: Optional[PasswordPolicyTypeTypeDef] = None
    SignInPolicy: Optional[SignInPolicyTypeTypeDef] = None


class AdminGetDeviceResponseTypeDef(BaseValidatorModel):
    Device: DeviceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AdminListDevicesResponseTypeDef(BaseValidatorModel):
    Devices: List[DeviceTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeviceResponseTypeDef(BaseValidatorModel):
    Device: DeviceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDevicesResponseTypeDef(BaseValidatorModel):
    Devices: List[DeviceTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AdminCreateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListUsersInGroupResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateManagedLoginBrandingResponseTypeDef(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeManagedLoginBrandingByClientResponseTypeDef(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeManagedLoginBrandingResponseTypeDef(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateManagedLoginBrandingResponseTypeDef(BaseValidatorModel):
    ManagedLoginBranding: ManagedLoginBrandingTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AdminListUserAuthEventsResponseTypeDef(BaseValidatorModel):
    AuthEvents: List[AuthEventTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AdminInitiateAuthResponseTypeDef(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    AvailableChallenges: List[ChallengeNameTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class AdminRespondToAuthChallengeResponseTypeDef(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InitiateAuthResponseTypeDef(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    AvailableChallenges: List[ChallengeNameTypeType]
    ResponseMetadata: ResponseMetadataTypeDef


class RespondToAuthChallengeResponseTypeDef(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AdminInitiateAuthRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    AuthFlow: AuthFlowTypeType
    AuthParameters: Optional[Mapping[str, str]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ContextData: Optional[ContextDataTypeTypeDef] = None
    Session: Optional[str] = None


class AdminRespondToAuthChallengeRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    ChallengeResponses: Optional[Mapping[str, str]] = None
    Session: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ContextData: Optional[ContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None


class CreateResourceServerResponseTypeDef(BaseValidatorModel):
    ResourceServer: ResourceServerTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeResourceServerResponseTypeDef(BaseValidatorModel):
    ResourceServer: ResourceServerTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourceServersResponseTypeDef(BaseValidatorModel):
    ResourceServers: List[ResourceServerTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateResourceServerResponseTypeDef(BaseValidatorModel):
    ResourceServer: ResourceServerTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserPoolClientResponseTypeDef(BaseValidatorModel):
    UserPoolClient: UserPoolClientTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserPoolClientResponseTypeDef(BaseValidatorModel):
    UserPoolClient: UserPoolClientTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserPoolClientResponseTypeDef(BaseValidatorModel):
    UserPoolClient: UserPoolClientTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserPoolDomainResponseTypeDef(BaseValidatorModel):
    DomainDescription: DomainDescriptionTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserPoolMfaConfigResponseTypeDef(BaseValidatorModel):
    SmsMfaConfiguration: SmsMfaConfigTypeTypeDef
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigTypeTypeDef
    EmailMfaConfiguration: EmailMfaConfigTypeTypeDef
    MfaConfiguration: UserPoolMfaTypeType
    WebAuthnConfiguration: WebAuthnConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetUserPoolMfaConfigRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    SmsMfaConfiguration: Optional[SmsMfaConfigTypeTypeDef] = None
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigTypeTypeDef] = None
    EmailMfaConfiguration: Optional[EmailMfaConfigTypeTypeDef] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    WebAuthnConfiguration: Optional[WebAuthnConfigurationTypeTypeDef] = None


class SetUserPoolMfaConfigResponseTypeDef(BaseValidatorModel):
    SmsMfaConfiguration: SmsMfaConfigTypeTypeDef
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigTypeTypeDef
    EmailMfaConfiguration: EmailMfaConfigTypeTypeDef
    MfaConfiguration: UserPoolMfaTypeType
    WebAuthnConfiguration: WebAuthnConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UserPoolDescriptionTypeTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    Status: Optional[StatusTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None


class LogDeliveryConfigurationTypeTypeDef(BaseValidatorModel):
    UserPoolId: str
    LogConfigurations: List[LogConfigurationTypeTypeDef]


class SetLogDeliveryConfigurationRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    LogConfigurations: Sequence[LogConfigurationTypeTypeDef]


class AccountTakeoverRiskConfigurationTypeTypeDef(BaseValidatorModel):
    Actions: AccountTakeoverActionsTypeTypeDef
    NotifyConfiguration: Optional[NotifyConfigurationTypeTypeDef] = None


class SchemaAttributeTypeTypeDef(BaseValidatorModel):
    pass


class AddCustomAttributesRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    CustomAttributes: Sequence[SchemaAttributeTypeTypeDef]


class UserPoolTypeTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Policies: Optional[UserPoolPolicyTypeOutputTypeDef] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    Status: Optional[StatusTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None
    SchemaAttributes: Optional[List[SchemaAttributeTypeTypeDef]] = None
    AutoVerifiedAttributes: Optional[List[VerifiedAttributeTypeType]] = None
    AliasAttributes: Optional[List[AliasAttributeTypeType]] = None
    UsernameAttributes: Optional[List[UsernameAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateTypeTypeDef] = None
    SmsAuthenticationMessage: Optional[str] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeOutputTypeDef] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeTypeDef] = None
    EstimatedNumberOfUsers: Optional[int] = None
    EmailConfiguration: Optional[EmailConfigurationTypeTypeDef] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None
    UserPoolTags: Optional[Dict[str, str]] = None
    SmsConfigurationFailure: Optional[str] = None
    EmailConfigurationFailure: Optional[str] = None
    Domain: Optional[str] = None
    CustomDomain: Optional[str] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigTypeTypeDef] = None
    UserPoolAddOns: Optional[UserPoolAddOnsTypeTypeDef] = None
    UsernameConfiguration: Optional[UsernameConfigurationTypeTypeDef] = None
    Arn: Optional[str] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeOutputTypeDef] = None
    UserPoolTier: Optional[UserPoolTierTypeType] = None


class AssetTypeUnionTypeDef(BaseValidatorModel):
    pass


class CreateManagedLoginBrandingRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    UseCognitoProvidedValues: Optional[bool] = None
    Settings: Optional[Mapping[str, Any]] = None
    Assets: Optional[Sequence[AssetTypeUnionTypeDef]] = None


class UpdateManagedLoginBrandingRequestTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ManagedLoginBrandingId: Optional[str] = None
    UseCognitoProvidedValues: Optional[bool] = None
    Settings: Optional[Mapping[str, Any]] = None
    Assets: Optional[Sequence[AssetTypeUnionTypeDef]] = None


class ListUserPoolsResponseTypeDef(BaseValidatorModel):
    UserPools: List[UserPoolDescriptionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetLogDeliveryConfigurationResponseTypeDef(BaseValidatorModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetLogDeliveryConfigurationResponseTypeDef(BaseValidatorModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RiskConfigurationTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[ CompromisedCredentialsRiskConfigurationTypeOutputTypeDef ] = None
    AccountTakeoverRiskConfiguration: Optional[AccountTakeoverRiskConfigurationTypeTypeDef] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeOutputTypeDef] = None
    LastModifiedDate: Optional[datetime] = None


class RiskExceptionConfigurationTypeUnionTypeDef(BaseValidatorModel):
    pass


class CompromisedCredentialsRiskConfigurationTypeUnionTypeDef(BaseValidatorModel):
    pass


class SetRiskConfigurationRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[ CompromisedCredentialsRiskConfigurationTypeUnionTypeDef ] = None
    AccountTakeoverRiskConfiguration: Optional[AccountTakeoverRiskConfigurationTypeTypeDef] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeUnionTypeDef] = None


class CreateUserPoolResponseTypeDef(BaseValidatorModel):
    UserPool: UserPoolTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUserPoolResponseTypeDef(BaseValidatorModel):
    UserPool: UserPoolTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AccountRecoverySettingTypeUnionTypeDef(BaseValidatorModel):
    pass


class UserPoolPolicyTypeUnionTypeDef(BaseValidatorModel):
    pass


class UserAttributeUpdateSettingsTypeUnionTypeDef(BaseValidatorModel):
    pass


class CreateUserPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str
    Policies: Optional[UserPoolPolicyTypeUnionTypeDef] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    AutoVerifiedAttributes: Optional[Sequence[VerifiedAttributeTypeType]] = None
    AliasAttributes: Optional[Sequence[AliasAttributeTypeType]] = None
    UsernameAttributes: Optional[Sequence[UsernameAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateTypeTypeDef] = None
    SmsAuthenticationMessage: Optional[str] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeUnionTypeDef] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeTypeDef] = None
    EmailConfiguration: Optional[EmailConfigurationTypeTypeDef] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None
    UserPoolTags: Optional[Mapping[str, str]] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigTypeTypeDef] = None
    Schema: Optional[Sequence[SchemaAttributeTypeTypeDef]] = None
    UserPoolAddOns: Optional[UserPoolAddOnsTypeTypeDef] = None
    UsernameConfiguration: Optional[UsernameConfigurationTypeTypeDef] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeUnionTypeDef] = None
    UserPoolTier: Optional[UserPoolTierTypeType] = None


class UpdateUserPoolRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Policies: Optional[UserPoolPolicyTypeUnionTypeDef] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    AutoVerifiedAttributes: Optional[Sequence[VerifiedAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateTypeTypeDef] = None
    SmsAuthenticationMessage: Optional[str] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeUnionTypeDef] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeTypeDef] = None
    EmailConfiguration: Optional[EmailConfigurationTypeTypeDef] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None
    UserPoolTags: Optional[Mapping[str, str]] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigTypeTypeDef] = None
    UserPoolAddOns: Optional[UserPoolAddOnsTypeTypeDef] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeUnionTypeDef] = None
    PoolName: Optional[str] = None
    UserPoolTier: Optional[UserPoolTierTypeType] = None


class DescribeRiskConfigurationResponseTypeDef(BaseValidatorModel):
    RiskConfiguration: RiskConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetRiskConfigurationResponseTypeDef(BaseValidatorModel):
    RiskConfiguration: RiskConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


