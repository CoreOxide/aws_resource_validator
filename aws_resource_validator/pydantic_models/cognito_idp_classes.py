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
from aws_resource_validator.pydantic_models.cognito_idp_constants import *

class RecoveryOptionTypeTypeDef(BaseModel):
    Priority: int
    Name: RecoveryOptionNameTypeType

class AccountTakeoverActionTypeTypeDef(BaseModel):
    Notify: bool
    EventAction: AccountTakeoverEventActionTypeType

class AdminAddUserToGroupRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    GroupName: str

class AdminConfirmSignUpRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Mapping[str, str]] = None

class MessageTemplateTypeTypeDef(BaseModel):
    SMSMessage: Optional[str] = None
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None

class AttributeTypeTypeDef(BaseModel):
    Name: str
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AdminDeleteUserAttributesRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    UserAttributeNames: Sequence[str]

class AdminDeleteUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str

class ProviderUserIdentifierTypeTypeDef(BaseModel):
    ProviderName: Optional[str] = None
    ProviderAttributeName: Optional[str] = None
    ProviderAttributeValue: Optional[str] = None

class AdminDisableUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str

class AdminEnableUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str

class AdminForgetDeviceRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    DeviceKey: str

class AdminGetDeviceRequestRequestTypeDef(BaseModel):
    DeviceKey: str
    UserPoolId: str
    Username: str

class AdminGetUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str

class MFAOptionTypeTypeDef(BaseModel):
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None

class AnalyticsMetadataTypeTypeDef(BaseModel):
    AnalyticsEndpointId: Optional[str] = None

class AdminListDevicesRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class AdminListGroupsForUserRequestRequestTypeDef(BaseModel):
    Username: str
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GroupTypeTypeDef(BaseModel):
    GroupName: Optional[str] = None
    UserPoolId: Optional[str] = None
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class AdminListUserAuthEventsRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class AdminRemoveUserFromGroupRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    GroupName: str

class AdminResetUserPasswordRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Mapping[str, str]] = None

class SMSMfaSettingsTypeTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None

class SoftwareTokenMfaSettingsTypeTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None

class AdminSetUserPasswordRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    Password: str
    Permanent: Optional[bool] = None

class AdminUpdateAuthEventFeedbackRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackValue: FeedbackValueTypeType

class AdminUpdateDeviceStatusRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None

class AdminUserGlobalSignOutRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str

class AnalyticsConfigurationTypeTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    RoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    UserDataShared: Optional[bool] = None

class AssociateSoftwareTokenRequestRequestTypeDef(BaseModel):
    AccessToken: Optional[str] = None
    Session: Optional[str] = None

class ChallengeResponseTypeTypeDef(BaseModel):
    ChallengeName: Optional[ChallengeNameType] = None
    ChallengeResponse: Optional[ChallengeResponseType] = None

class EventContextDataTypeTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    DeviceName: Optional[str] = None
    Timezone: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None

class EventFeedbackTypeTypeDef(BaseModel):
    FeedbackValue: FeedbackValueTypeType
    Provider: str
    FeedbackDate: Optional[datetime] = None

class EventRiskTypeTypeDef(BaseModel):
    RiskDecision: Optional[RiskDecisionTypeType] = None
    RiskLevel: Optional[RiskLevelTypeType] = None
    CompromisedCredentialsDetected: Optional[bool] = None

class NewDeviceMetadataTypeTypeDef(BaseModel):
    DeviceKey: Optional[str] = None
    DeviceGroupKey: Optional[str] = None

class ChangePasswordRequestRequestTypeDef(BaseModel):
    PreviousPassword: str
    ProposedPassword: str
    AccessToken: str

class CloudWatchLogsConfigurationTypeTypeDef(BaseModel):
    LogGroupArn: Optional[str] = None

class CodeDeliveryDetailsTypeTypeDef(BaseModel):
    Destination: Optional[str] = None
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None

class CompromisedCredentialsActionsTypeTypeDef(BaseModel):
    EventAction: CompromisedCredentialsEventActionTypeType

class DeviceSecretVerifierConfigTypeTypeDef(BaseModel):
    PasswordVerifier: Optional[str] = None
    Salt: Optional[str] = None

class UserContextDataTypeTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    EncodedData: Optional[str] = None

class HttpHeaderTypeDef(BaseModel):
    headerName: Optional[str] = None
    headerValue: Optional[str] = None

class CreateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None

class CreateIdentityProviderRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ProviderName: str
    ProviderType: IdentityProviderTypeTypeType
    ProviderDetails: Mapping[str, str]
    AttributeMapping: Optional[Mapping[str, str]] = None
    IdpIdentifiers: Optional[Sequence[str]] = None

class IdentityProviderTypeTypeDef(BaseModel):
    UserPoolId: Optional[str] = None
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    ProviderDetails: Optional[Dict[str, str]] = None
    AttributeMapping: Optional[Dict[str, str]] = None
    IdpIdentifiers: Optional[List[str]] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class ResourceServerScopeTypeTypeDef(BaseModel):
    ScopeName: str
    ScopeDescription: str

class CreateUserImportJobRequestRequestTypeDef(BaseModel):
    JobName: str
    UserPoolId: str
    CloudWatchLogsRoleArn: str

class UserImportJobTypeTypeDef(BaseModel):
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

class TokenValidityUnitsTypeTypeDef(BaseModel):
    AccessToken: Optional[TimeUnitsTypeType] = None
    IdToken: Optional[TimeUnitsTypeType] = None
    RefreshToken: Optional[TimeUnitsTypeType] = None

class CustomDomainConfigTypeTypeDef(BaseModel):
    CertificateArn: str

class DeviceConfigurationTypeTypeDef(BaseModel):
    ChallengeRequiredOnNewDevice: Optional[bool] = None
    DeviceOnlyRememberedOnUserPrompt: Optional[bool] = None

class EmailConfigurationTypeTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    ReplyToEmailAddress: Optional[str] = None
    EmailSendingAccount: Optional[EmailSendingAccountTypeType] = None
    From: Optional[str] = None
    ConfigurationSet: Optional[str] = None

class SmsConfigurationTypeTypeDef(BaseModel):
    SnsCallerArn: str
    ExternalId: Optional[str] = None
    SnsRegion: Optional[str] = None

class UserAttributeUpdateSettingsTypeTypeDef(BaseModel):
    AttributesRequireVerificationBeforeUpdate: Optional[       Sequence[VerifiedAttributeTypeType]     ] = None

class UserPoolAddOnsTypeTypeDef(BaseModel):
    AdvancedSecurityMode: AdvancedSecurityModeTypeType

class UsernameConfigurationTypeTypeDef(BaseModel):
    CaseSensitive: bool

class VerificationMessageTemplateTypeTypeDef(BaseModel):
    SmsMessage: Optional[str] = None
    EmailMessage: Optional[str] = None
    EmailSubject: Optional[str] = None
    EmailMessageByLink: Optional[str] = None
    EmailSubjectByLink: Optional[str] = None
    DefaultEmailOption: Optional[DefaultEmailOptionTypeType] = None

class CustomEmailLambdaVersionConfigTypeTypeDef(BaseModel):
    LambdaVersion: Literal["V1_0"]
    LambdaArn: str

class CustomSMSLambdaVersionConfigTypeTypeDef(BaseModel):
    LambdaVersion: Literal["V1_0"]
    LambdaArn: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    UserPoolId: str

class DeleteIdentityProviderRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ProviderName: str

class DeleteResourceServerRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Identifier: str

class DeleteUserAttributesRequestRequestTypeDef(BaseModel):
    UserAttributeNames: Sequence[str]
    AccessToken: str

class DeleteUserPoolClientRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: str

class DeleteUserPoolDomainRequestRequestTypeDef(BaseModel):
    Domain: str
    UserPoolId: str

class DeleteUserPoolRequestRequestTypeDef(BaseModel):
    UserPoolId: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    AccessToken: str

class DescribeIdentityProviderRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ProviderName: str

class DescribeResourceServerRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Identifier: str

class DescribeRiskConfigurationRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: Optional[str] = None

class DescribeUserImportJobRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    JobId: str

class DescribeUserPoolClientRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: str

class DescribeUserPoolDomainRequestRequestTypeDef(BaseModel):
    Domain: str

class DescribeUserPoolRequestRequestTypeDef(BaseModel):
    UserPoolId: str

class ForgetDeviceRequestRequestTypeDef(BaseModel):
    DeviceKey: str
    AccessToken: Optional[str] = None

class GetCSVHeaderRequestRequestTypeDef(BaseModel):
    UserPoolId: str

class GetDeviceRequestRequestTypeDef(BaseModel):
    DeviceKey: str
    AccessToken: Optional[str] = None

class GetGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    UserPoolId: str

class GetIdentityProviderByIdentifierRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    IdpIdentifier: str

class GetLogDeliveryConfigurationRequestRequestTypeDef(BaseModel):
    UserPoolId: str

class GetSigningCertificateRequestRequestTypeDef(BaseModel):
    UserPoolId: str

class GetUICustomizationRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: Optional[str] = None

class UICustomizationTypeTypeDef(BaseModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    ImageUrl: Optional[str] = None
    CSS: Optional[str] = None
    CSSVersion: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class GetUserAttributeVerificationCodeRequestRequestTypeDef(BaseModel):
    AccessToken: str
    AttributeName: str
    ClientMetadata: Optional[Mapping[str, str]] = None

class GetUserPoolMfaConfigRequestRequestTypeDef(BaseModel):
    UserPoolId: str

class SoftwareTokenMfaConfigTypeTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class GetUserRequestRequestTypeDef(BaseModel):
    AccessToken: str

class GlobalSignOutRequestRequestTypeDef(BaseModel):
    AccessToken: str

class PreTokenGenerationVersionConfigTypeTypeDef(BaseModel):
    LambdaVersion: PreTokenGenerationLambdaVersionTypeType
    LambdaArn: str

class ListDevicesRequestRequestTypeDef(BaseModel):
    AccessToken: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListIdentityProvidersRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProviderDescriptionTypeDef(BaseModel):
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class ListResourceServersRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListUserImportJobsRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    MaxResults: int
    PaginationToken: Optional[str] = None

class ListUserPoolClientsRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UserPoolClientDescriptionTypeDef(BaseModel):
    ClientId: Optional[str] = None
    UserPoolId: Optional[str] = None
    ClientName: Optional[str] = None

class ListUserPoolsRequestRequestTypeDef(BaseModel):
    MaxResults: int
    NextToken: Optional[str] = None

class ListUsersInGroupRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    GroupName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None
    Filter: Optional[str] = None

class NotifyEmailTypeTypeDef(BaseModel):
    Subject: str
    HtmlBody: Optional[str] = None
    TextBody: Optional[str] = None

class NumberAttributeConstraintsTypeTypeDef(BaseModel):
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None

class PasswordPolicyTypeTypeDef(BaseModel):
    MinimumLength: Optional[int] = None
    RequireUppercase: Optional[bool] = None
    RequireLowercase: Optional[bool] = None
    RequireNumbers: Optional[bool] = None
    RequireSymbols: Optional[bool] = None
    TemporaryPasswordValidityDays: Optional[int] = None

class RevokeTokenRequestRequestTypeDef(BaseModel):
    Token: str
    ClientId: str
    ClientSecret: Optional[str] = None

class RiskExceptionConfigurationTypeOutputTypeDef(BaseModel):
    BlockedIPRangeList: Optional[List[str]] = None
    SkippedIPRangeList: Optional[List[str]] = None

class RiskExceptionConfigurationTypeTypeDef(BaseModel):
    BlockedIPRangeList: Optional[Sequence[str]] = None
    SkippedIPRangeList: Optional[Sequence[str]] = None

class StringAttributeConstraintsTypeTypeDef(BaseModel):
    MinLength: Optional[str] = None
    MaxLength: Optional[str] = None

class StartUserImportJobRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    JobId: str

class StopUserImportJobRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    JobId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAuthEventFeedbackRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackToken: str
    FeedbackValue: FeedbackValueTypeType

class UpdateDeviceStatusRequestRequestTypeDef(BaseModel):
    AccessToken: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None

class UpdateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None

class UpdateIdentityProviderRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ProviderName: str
    ProviderDetails: Optional[Mapping[str, str]] = None
    AttributeMapping: Optional[Mapping[str, str]] = None
    IdpIdentifiers: Optional[Sequence[str]] = None

class UserAttributeUpdateSettingsTypeOutputTypeDef(BaseModel):
    AttributesRequireVerificationBeforeUpdate: Optional[List[VerifiedAttributeTypeType]] = None

class VerifySoftwareTokenRequestRequestTypeDef(BaseModel):
    UserCode: str
    AccessToken: Optional[str] = None
    Session: Optional[str] = None
    FriendlyDeviceName: Optional[str] = None

class VerifyUserAttributeRequestRequestTypeDef(BaseModel):
    AccessToken: str
    AttributeName: str
    Code: str

class AccountRecoverySettingTypeOutputTypeDef(BaseModel):
    RecoveryMechanisms: Optional[List[RecoveryOptionTypeTypeDef]] = None

class AccountRecoverySettingTypeTypeDef(BaseModel):
    RecoveryMechanisms: Optional[Sequence[RecoveryOptionTypeTypeDef]] = None

class AccountTakeoverActionsTypeTypeDef(BaseModel):
    LowAction: Optional[AccountTakeoverActionTypeTypeDef] = None
    MediumAction: Optional[AccountTakeoverActionTypeTypeDef] = None
    HighAction: Optional[AccountTakeoverActionTypeTypeDef] = None

class AdminCreateUserConfigTypeTypeDef(BaseModel):
    AllowAdminCreateUserOnly: Optional[bool] = None
    UnusedAccountValidityDays: Optional[int] = None
    InviteMessageTemplate: Optional[MessageTemplateTypeTypeDef] = None

class AdminCreateUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    UserAttributes: Optional[Sequence[AttributeTypeTypeDef]] = None
    ValidationData: Optional[Sequence[AttributeTypeTypeDef]] = None
    TemporaryPassword: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    MessageAction: Optional[MessageActionTypeType] = None
    DesiredDeliveryMediums: Optional[Sequence[DeliveryMediumTypeType]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class AdminUpdateUserAttributesRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    UserAttributes: Sequence[AttributeTypeTypeDef]
    ClientMetadata: Optional[Mapping[str, str]] = None

class DeviceTypeTypeDef(BaseModel):
    DeviceKey: Optional[str] = None
    DeviceAttributes: Optional[List[AttributeTypeTypeDef]] = None
    DeviceCreateDate: Optional[datetime] = None
    DeviceLastModifiedDate: Optional[datetime] = None
    DeviceLastAuthenticatedDate: Optional[datetime] = None

class UpdateUserAttributesRequestRequestTypeDef(BaseModel):
    UserAttributes: Sequence[AttributeTypeTypeDef]
    AccessToken: str
    ClientMetadata: Optional[Mapping[str, str]] = None

class AssociateSoftwareTokenResponseTypeDef(BaseModel):
    SecretCode: str
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmDeviceResponseTypeDef(BaseModel):
    UserConfirmationNecessary: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserPoolDomainResponseTypeDef(BaseModel):
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCSVHeaderResponseTypeDef(BaseModel):
    UserPoolId: str
    CSVHeader: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSigningCertificateResponseTypeDef(BaseModel):
    Certificate: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserPoolDomainResponseTypeDef(BaseModel):
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifySoftwareTokenResponseTypeDef(BaseModel):
    Status: VerifySoftwareTokenResponseTypeType
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdminDisableProviderForUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    User: ProviderUserIdentifierTypeTypeDef

class AdminLinkProviderForUserRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    DestinationUser: ProviderUserIdentifierTypeTypeDef
    SourceUser: ProviderUserIdentifierTypeTypeDef

class AdminGetUserResponseTypeDef(BaseModel):
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

class AdminSetUserSettingsRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    MFAOptions: Sequence[MFAOptionTypeTypeDef]

class GetUserResponseTypeDef(BaseModel):
    Username: str
    UserAttributes: List[AttributeTypeTypeDef]
    MFAOptions: List[MFAOptionTypeTypeDef]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SetUserSettingsRequestRequestTypeDef(BaseModel):
    AccessToken: str
    MFAOptions: Sequence[MFAOptionTypeTypeDef]

class UserTypeTypeDef(BaseModel):
    Username: Optional[str] = None
    Attributes: Optional[List[AttributeTypeTypeDef]] = None
    UserCreateDate: Optional[datetime] = None
    UserLastModifiedDate: Optional[datetime] = None
    Enabled: Optional[bool] = None
    UserStatus: Optional[UserStatusTypeType] = None
    MFAOptions: Optional[List[MFAOptionTypeTypeDef]] = None

class AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef(BaseModel):
    Username: str
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef(BaseModel):
    UserPoolId: str
    Username: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef(BaseModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceServersRequestListResourceServersPaginateTypeDef(BaseModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef(BaseModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserPoolsRequestListUserPoolsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersInGroupRequestListUsersInGroupPaginateTypeDef(BaseModel):
    UserPoolId: str
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    UserPoolId: str
    AttributesToGet: Optional[Sequence[str]] = None
    Filter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class AdminListGroupsForUserResponseTypeDef(BaseModel):
    Groups: List[GroupTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGroupResponseTypeDef(BaseModel):
    Group: GroupTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseModel):
    Group: GroupTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGroupResponseTypeDef(BaseModel):
    Group: GroupTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AdminSetUserMFAPreferenceRequestRequestTypeDef(BaseModel):
    Username: str
    UserPoolId: str
    SMSMfaSettings: Optional[SMSMfaSettingsTypeTypeDef] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsTypeTypeDef] = None

class SetUserMFAPreferenceRequestRequestTypeDef(BaseModel):
    AccessToken: str
    SMSMfaSettings: Optional[SMSMfaSettingsTypeTypeDef] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsTypeTypeDef] = None

class AuthEventTypeTypeDef(BaseModel):
    EventId: Optional[str] = None
    EventType: Optional[EventTypeType] = None
    CreationDate: Optional[datetime] = None
    EventResponse: Optional[EventResponseTypeType] = None
    EventRisk: Optional[EventRiskTypeTypeDef] = None
    ChallengeResponses: Optional[List[ChallengeResponseTypeTypeDef]] = None
    EventContextData: Optional[EventContextDataTypeTypeDef] = None
    EventFeedback: Optional[EventFeedbackTypeTypeDef] = None

class AuthenticationResultTypeTypeDef(BaseModel):
    AccessToken: Optional[str] = None
    ExpiresIn: Optional[int] = None
    TokenType: Optional[str] = None
    RefreshToken: Optional[str] = None
    IdToken: Optional[str] = None
    NewDeviceMetadata: Optional[NewDeviceMetadataTypeTypeDef] = None

class SetUICustomizationRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CSS: Optional[str] = None
    ImageFile: Optional[BlobTypeDef] = None

class LogConfigurationTypeTypeDef(BaseModel):
    LogLevel: Literal["ERROR"]
    EventSource: Literal["userNotification"]
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationTypeTypeDef] = None

class ForgotPasswordResponseTypeDef(BaseModel):
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserAttributeVerificationCodeResponseTypeDef(BaseModel):
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResendConfirmationCodeResponseTypeDef(BaseModel):
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SignUpResponseTypeDef(BaseModel):
    UserConfirmed: bool
    CodeDeliveryDetails: CodeDeliveryDetailsTypeTypeDef
    UserSub: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserAttributesResponseTypeDef(BaseModel):
    CodeDeliveryDetailsList: List[CodeDeliveryDetailsTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CompromisedCredentialsRiskConfigurationTypeOutputTypeDef(BaseModel):
    Actions: CompromisedCredentialsActionsTypeTypeDef
    EventFilter: Optional[List[EventFilterTypeType]] = None

class CompromisedCredentialsRiskConfigurationTypeTypeDef(BaseModel):
    Actions: CompromisedCredentialsActionsTypeTypeDef
    EventFilter: Optional[Sequence[EventFilterTypeType]] = None

class ConfirmDeviceRequestRequestTypeDef(BaseModel):
    AccessToken: str
    DeviceKey: str
    DeviceSecretVerifierConfig: Optional[DeviceSecretVerifierConfigTypeTypeDef] = None
    DeviceName: Optional[str] = None

class ConfirmForgotPasswordRequestRequestTypeDef(BaseModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    Password: str
    SecretHash: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class ConfirmSignUpRequestRequestTypeDef(BaseModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    SecretHash: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class ForgotPasswordRequestRequestTypeDef(BaseModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class InitiateAuthRequestRequestTypeDef(BaseModel):
    AuthFlow: AuthFlowTypeType
    ClientId: str
    AuthParameters: Optional[Mapping[str, str]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None

class ResendConfirmationCodeRequestRequestTypeDef(BaseModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class RespondToAuthChallengeRequestRequestTypeDef(BaseModel):
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    Session: Optional[str] = None
    ChallengeResponses: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class SignUpRequestRequestTypeDef(BaseModel):
    ClientId: str
    Username: str
    Password: str
    SecretHash: Optional[str] = None
    UserAttributes: Optional[Sequence[AttributeTypeTypeDef]] = None
    ValidationData: Optional[Sequence[AttributeTypeTypeDef]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class ContextDataTypeTypeDef(BaseModel):
    IpAddress: str
    ServerName: str
    ServerPath: str
    HttpHeaders: Sequence[HttpHeaderTypeDef]
    EncodedData: Optional[str] = None

class CreateIdentityProviderResponseTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityProviderResponseTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityProviderByIdentifierResponseTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentityProviderResponseTypeDef(BaseModel):
    IdentityProvider: IdentityProviderTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceServerRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[Sequence[ResourceServerScopeTypeTypeDef]] = None

class ResourceServerTypeTypeDef(BaseModel):
    UserPoolId: Optional[str] = None
    Identifier: Optional[str] = None
    Name: Optional[str] = None
    Scopes: Optional[List[ResourceServerScopeTypeTypeDef]] = None

class UpdateResourceServerRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[Sequence[ResourceServerScopeTypeTypeDef]] = None

class CreateUserImportJobResponseTypeDef(BaseModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserImportJobResponseTypeDef(BaseModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserImportJobsResponseTypeDef(BaseModel):
    UserImportJobs: List[UserImportJobTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartUserImportJobResponseTypeDef(BaseModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopUserImportJobResponseTypeDef(BaseModel):
    UserImportJob: UserImportJobTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserPoolClientRequestRequestTypeDef(BaseModel):
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

class UpdateUserPoolClientRequestRequestTypeDef(BaseModel):
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

class UserPoolClientTypeTypeDef(BaseModel):
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

class CreateUserPoolDomainRequestRequestTypeDef(BaseModel):
    Domain: str
    UserPoolId: str
    CustomDomainConfig: Optional[CustomDomainConfigTypeTypeDef] = None

class DomainDescriptionTypeTypeDef(BaseModel):
    UserPoolId: Optional[str] = None
    AWSAccountId: Optional[str] = None
    Domain: Optional[str] = None
    S3Bucket: Optional[str] = None
    CloudFrontDistribution: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[DomainStatusTypeType] = None
    CustomDomainConfig: Optional[CustomDomainConfigTypeTypeDef] = None

class UpdateUserPoolDomainRequestRequestTypeDef(BaseModel):
    Domain: str
    UserPoolId: str
    CustomDomainConfig: CustomDomainConfigTypeTypeDef

class SmsMfaConfigTypeTypeDef(BaseModel):
    SmsAuthenticationMessage: Optional[str] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None

class GetUICustomizationResponseTypeDef(BaseModel):
    UICustomization: UICustomizationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetUICustomizationResponseTypeDef(BaseModel):
    UICustomization: UICustomizationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LambdaConfigTypeTypeDef(BaseModel):
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

class ListIdentityProvidersResponseTypeDef(BaseModel):
    Providers: List[ProviderDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUserPoolClientsResponseTypeDef(BaseModel):
    UserPoolClients: List[UserPoolClientDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NotifyConfigurationTypeTypeDef(BaseModel):
    SourceArn: str
    From: Optional[str] = None
    ReplyTo: Optional[str] = None
    BlockEmail: Optional[NotifyEmailTypeTypeDef] = None
    NoActionEmail: Optional[NotifyEmailTypeTypeDef] = None
    MfaEmail: Optional[NotifyEmailTypeTypeDef] = None

class UserPoolPolicyTypeTypeDef(BaseModel):
    PasswordPolicy: Optional[PasswordPolicyTypeTypeDef] = None

class SchemaAttributeTypeTypeDef(BaseModel):
    Name: Optional[str] = None
    AttributeDataType: Optional[AttributeDataTypeType] = None
    DeveloperOnlyAttribute: Optional[bool] = None
    Mutable: Optional[bool] = None
    Required: Optional[bool] = None
    NumberAttributeConstraints: Optional[NumberAttributeConstraintsTypeTypeDef] = None
    StringAttributeConstraints: Optional[StringAttributeConstraintsTypeTypeDef] = None

class AdminGetDeviceResponseTypeDef(BaseModel):
    Device: DeviceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AdminListDevicesResponseTypeDef(BaseModel):
    Devices: List[DeviceTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceResponseTypeDef(BaseModel):
    Device: DeviceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseModel):
    Devices: List[DeviceTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdminCreateUserResponseTypeDef(BaseModel):
    User: UserTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersInGroupResponseTypeDef(BaseModel):
    Users: List[UserTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdminListUserAuthEventsResponseTypeDef(BaseModel):
    AuthEvents: List[AuthEventTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AdminInitiateAuthResponseTypeDef(BaseModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AdminRespondToAuthChallengeResponseTypeDef(BaseModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateAuthResponseTypeDef(BaseModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RespondToAuthChallengeResponseTypeDef(BaseModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LogDeliveryConfigurationTypeTypeDef(BaseModel):
    UserPoolId: str
    LogConfigurations: List[LogConfigurationTypeTypeDef]

class SetLogDeliveryConfigurationRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    LogConfigurations: Sequence[LogConfigurationTypeTypeDef]

class AdminInitiateAuthRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: str
    AuthFlow: AuthFlowTypeType
    AuthParameters: Optional[Mapping[str, str]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ContextData: Optional[ContextDataTypeTypeDef] = None

class AdminRespondToAuthChallengeRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    ChallengeResponses: Optional[Mapping[str, str]] = None
    Session: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ContextData: Optional[ContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class CreateResourceServerResponseTypeDef(BaseModel):
    ResourceServer: ResourceServerTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceServerResponseTypeDef(BaseModel):
    ResourceServer: ResourceServerTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceServersResponseTypeDef(BaseModel):
    ResourceServers: List[ResourceServerTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateResourceServerResponseTypeDef(BaseModel):
    ResourceServer: ResourceServerTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserPoolClientResponseTypeDef(BaseModel):
    UserPoolClient: UserPoolClientTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserPoolClientResponseTypeDef(BaseModel):
    UserPoolClient: UserPoolClientTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserPoolClientResponseTypeDef(BaseModel):
    UserPoolClient: UserPoolClientTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserPoolDomainResponseTypeDef(BaseModel):
    DomainDescription: DomainDescriptionTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserPoolMfaConfigResponseTypeDef(BaseModel):
    SmsMfaConfiguration: SmsMfaConfigTypeTypeDef
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigTypeTypeDef
    MfaConfiguration: UserPoolMfaTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SetUserPoolMfaConfigRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    SmsMfaConfiguration: Optional[SmsMfaConfigTypeTypeDef] = None
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigTypeTypeDef] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None

class SetUserPoolMfaConfigResponseTypeDef(BaseModel):
    SmsMfaConfiguration: SmsMfaConfigTypeTypeDef
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigTypeTypeDef
    MfaConfiguration: UserPoolMfaTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UserPoolDescriptionTypeTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    Status: Optional[StatusTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class AccountTakeoverRiskConfigurationTypeTypeDef(BaseModel):
    Actions: AccountTakeoverActionsTypeTypeDef
    NotifyConfiguration: Optional[NotifyConfigurationTypeTypeDef] = None

class UpdateUserPoolRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    Policies: Optional[UserPoolPolicyTypeTypeDef] = None
    DeletionProtection: Optional[DeletionProtectionTypeType] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    AutoVerifiedAttributes: Optional[Sequence[VerifiedAttributeTypeType]] = None
    SmsVerificationMessage: Optional[str] = None
    EmailVerificationMessage: Optional[str] = None
    EmailVerificationSubject: Optional[str] = None
    VerificationMessageTemplate: Optional[VerificationMessageTemplateTypeTypeDef] = None
    SmsAuthenticationMessage: Optional[str] = None
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeTypeDef] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeTypeDef] = None
    EmailConfiguration: Optional[EmailConfigurationTypeTypeDef] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None
    UserPoolTags: Optional[Mapping[str, str]] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigTypeTypeDef] = None
    UserPoolAddOns: Optional[UserPoolAddOnsTypeTypeDef] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeTypeDef] = None

class AddCustomAttributesRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    CustomAttributes: Sequence[SchemaAttributeTypeTypeDef]

class CreateUserPoolRequestRequestTypeDef(BaseModel):
    PoolName: str
    Policies: Optional[UserPoolPolicyTypeTypeDef] = None
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
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsTypeTypeDef] = None
    DeviceConfiguration: Optional[DeviceConfigurationTypeTypeDef] = None
    EmailConfiguration: Optional[EmailConfigurationTypeTypeDef] = None
    SmsConfiguration: Optional[SmsConfigurationTypeTypeDef] = None
    UserPoolTags: Optional[Mapping[str, str]] = None
    AdminCreateUserConfig: Optional[AdminCreateUserConfigTypeTypeDef] = None
    Schema: Optional[Sequence[SchemaAttributeTypeTypeDef]] = None
    UserPoolAddOns: Optional[UserPoolAddOnsTypeTypeDef] = None
    UsernameConfiguration: Optional[UsernameConfigurationTypeTypeDef] = None
    AccountRecoverySetting: Optional[AccountRecoverySettingTypeTypeDef] = None

class UserPoolTypeTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Policies: Optional[UserPoolPolicyTypeTypeDef] = None
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

class GetLogDeliveryConfigurationResponseTypeDef(BaseModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetLogDeliveryConfigurationResponseTypeDef(BaseModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserPoolsResponseTypeDef(BaseModel):
    UserPools: List[UserPoolDescriptionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RiskConfigurationTypeTypeDef(BaseModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[       CompromisedCredentialsRiskConfigurationTypeOutputTypeDef     ] = None
    AccountTakeoverRiskConfiguration: Optional[       AccountTakeoverRiskConfigurationTypeTypeDef     ] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeOutputTypeDef] = None
    LastModifiedDate: Optional[datetime] = None

class SetRiskConfigurationRequestRequestTypeDef(BaseModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[       CompromisedCredentialsRiskConfigurationTypeTypeDef     ] = None
    AccountTakeoverRiskConfiguration: Optional[       AccountTakeoverRiskConfigurationTypeTypeDef     ] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeTypeDef] = None

class CreateUserPoolResponseTypeDef(BaseModel):
    UserPool: UserPoolTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserPoolResponseTypeDef(BaseModel):
    UserPool: UserPoolTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRiskConfigurationResponseTypeDef(BaseModel):
    RiskConfiguration: RiskConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetRiskConfigurationResponseTypeDef(BaseModel):
    RiskConfiguration: RiskConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

