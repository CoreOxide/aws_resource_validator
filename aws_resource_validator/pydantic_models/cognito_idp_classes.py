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
from aws_resource_validator.pydantic_models.cognito_idp_constants import *

class RecoveryOptionTypeTypeDef(BaseValidatorModel):
    Priority: int
    Name: RecoveryOptionNameTypeType

class AccountTakeoverActionTypeTypeDef(BaseValidatorModel):
    Notify: bool
    EventAction: AccountTakeoverEventActionTypeType

class AdminAddUserToGroupRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    GroupName: str

class AdminConfirmSignUpRequestRequestTypeDef(BaseValidatorModel):
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

class AdminDeleteUserAttributesRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributeNames: Sequence[str]

class AdminDeleteUserRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str

class ProviderUserIdentifierTypeTypeDef(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ProviderAttributeName: Optional[str] = None
    ProviderAttributeValue: Optional[str] = None

class AdminDisableUserRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str

class AdminEnableUserRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str

class AdminForgetDeviceRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    DeviceKey: str

class AdminGetDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceKey: str
    UserPoolId: str
    Username: str

class AdminGetUserRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str

class MFAOptionTypeTypeDef(BaseValidatorModel):
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None

class AnalyticsMetadataTypeTypeDef(BaseValidatorModel):
    AnalyticsEndpointId: Optional[str] = None

class AdminListDevicesRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class AdminListGroupsForUserRequestRequestTypeDef(BaseValidatorModel):
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

class AdminListUserAuthEventsRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class AdminRemoveUserFromGroupRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    GroupName: str

class AdminResetUserPasswordRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    ClientMetadata: Optional[Mapping[str, str]] = None

class SMSMfaSettingsTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None

class SoftwareTokenMfaSettingsTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    PreferredMfa: Optional[bool] = None

class AdminSetUserPasswordRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    Password: str
    Permanent: Optional[bool] = None

class AdminUpdateAuthEventFeedbackRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackValue: FeedbackValueTypeType

class AdminUpdateDeviceStatusRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None

class AdminUserGlobalSignOutRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str

class AnalyticsConfigurationTypeTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    RoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    UserDataShared: Optional[bool] = None

class AssociateSoftwareTokenRequestRequestTypeDef(BaseValidatorModel):
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

class ChangePasswordRequestRequestTypeDef(BaseValidatorModel):
    PreviousPassword: str
    ProposedPassword: str
    AccessToken: str

class CloudWatchLogsConfigurationTypeTypeDef(BaseValidatorModel):
    LogGroupArn: Optional[str] = None

class CodeDeliveryDetailsTypeTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    DeliveryMedium: Optional[DeliveryMediumTypeType] = None
    AttributeName: Optional[str] = None

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

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None

class CreateIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
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

class CreateUserImportJobRequestRequestTypeDef(BaseValidatorModel):
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

class UserAttributeUpdateSettingsTypeTypeDef(BaseValidatorModel):
    AttributesRequireVerificationBeforeUpdate: Optional[       Sequence[VerifiedAttributeTypeType]     ] = None

class UserPoolAddOnsTypeTypeDef(BaseValidatorModel):
    AdvancedSecurityMode: AdvancedSecurityModeTypeType

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

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str

class DeleteIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str

class DeleteResourceServerRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str

class DeleteUserAttributesRequestRequestTypeDef(BaseValidatorModel):
    UserAttributeNames: Sequence[str]
    AccessToken: str

class DeleteUserPoolClientRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str

class DeleteUserPoolDomainRequestRequestTypeDef(BaseValidatorModel):
    Domain: str
    UserPoolId: str

class DeleteUserPoolRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str

class DescribeIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str

class DescribeResourceServerRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str

class DescribeRiskConfigurationRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None

class DescribeUserImportJobRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    JobId: str

class DescribeUserPoolClientRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str

class DescribeUserPoolDomainRequestRequestTypeDef(BaseValidatorModel):
    Domain: str

class DescribeUserPoolRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str

class ForgetDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceKey: str
    AccessToken: Optional[str] = None

class GetCSVHeaderRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str

class GetDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceKey: str
    AccessToken: Optional[str] = None

class GetGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str

class GetIdentityProviderByIdentifierRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    IdpIdentifier: str

class GetLogDeliveryConfigurationRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str

class GetSigningCertificateRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str

class GetUICustomizationRequestRequestTypeDef(BaseValidatorModel):
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

class GetUserAttributeVerificationCodeRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    AttributeName: str
    ClientMetadata: Optional[Mapping[str, str]] = None

class GetUserPoolMfaConfigRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str

class SoftwareTokenMfaConfigTypeTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class GetUserRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str

class GlobalSignOutRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str

class PreTokenGenerationVersionConfigTypeTypeDef(BaseValidatorModel):
    LambdaVersion: PreTokenGenerationLambdaVersionTypeType
    LambdaArn: str

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListIdentityProvidersRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProviderDescriptionTypeDef(BaseValidatorModel):
    ProviderName: Optional[str] = None
    ProviderType: Optional[IdentityProviderTypeTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class ListResourceServersRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListUserImportJobsRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: int
    PaginationToken: Optional[str] = None

class ListUserPoolClientsRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UserPoolClientDescriptionTypeDef(BaseValidatorModel):
    ClientId: Optional[str] = None
    UserPoolId: Optional[str] = None
    ClientName: Optional[str] = None

class ListUserPoolsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: int
    NextToken: Optional[str] = None

class ListUsersInGroupRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    GroupName: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    PaginationToken: Optional[str] = None
    Filter: Optional[str] = None

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
    TemporaryPasswordValidityDays: Optional[int] = None

class RevokeTokenRequestRequestTypeDef(BaseValidatorModel):
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

class StartUserImportJobRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    JobId: str

class StopUserImportJobRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    JobId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAuthEventFeedbackRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    EventId: str
    FeedbackToken: str
    FeedbackValue: FeedbackValueTypeType

class UpdateDeviceStatusRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    DeviceKey: str
    DeviceRememberedStatus: Optional[DeviceRememberedStatusTypeType] = None

class UpdateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    UserPoolId: str
    Description: Optional[str] = None
    RoleArn: Optional[str] = None
    Precedence: Optional[int] = None

class UpdateIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ProviderName: str
    ProviderDetails: Optional[Mapping[str, str]] = None
    AttributeMapping: Optional[Mapping[str, str]] = None
    IdpIdentifiers: Optional[Sequence[str]] = None

class UserAttributeUpdateSettingsTypeOutputTypeDef(BaseValidatorModel):
    AttributesRequireVerificationBeforeUpdate: Optional[List[VerifiedAttributeTypeType]] = None

class VerifySoftwareTokenRequestRequestTypeDef(BaseValidatorModel):
    UserCode: str
    AccessToken: Optional[str] = None
    Session: Optional[str] = None
    FriendlyDeviceName: Optional[str] = None

class VerifyUserAttributeRequestRequestTypeDef(BaseValidatorModel):
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

class AdminCreateUserRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    UserAttributes: Optional[Sequence[AttributeTypeTypeDef]] = None
    ValidationData: Optional[Sequence[AttributeTypeTypeDef]] = None
    TemporaryPassword: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    MessageAction: Optional[MessageActionTypeType] = None
    DesiredDeliveryMediums: Optional[Sequence[DeliveryMediumTypeType]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class AdminUpdateUserAttributesRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateUserAttributesRequestRequestTypeDef(BaseValidatorModel):
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

class CreateUserPoolDomainResponseTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserPoolDomainResponseTypeDef(BaseValidatorModel):
    CloudFrontDomain: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifySoftwareTokenResponseTypeDef(BaseValidatorModel):
    Status: VerifySoftwareTokenResponseTypeType
    Session: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdminDisableProviderForUserRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    User: ProviderUserIdentifierTypeTypeDef

class AdminLinkProviderForUserRequestRequestTypeDef(BaseValidatorModel):
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

class AdminSetUserSettingsRequestRequestTypeDef(BaseValidatorModel):
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

class SetUserSettingsRequestRequestTypeDef(BaseValidatorModel):
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

class AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef(BaseValidatorModel):
    Username: str
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    Username: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceServersRequestListResourceServersPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserPoolsRequestListUserPoolsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersInGroupRequestListUsersInGroupPaginateTypeDef(BaseValidatorModel):
    UserPoolId: str
    GroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
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

class AdminSetUserMFAPreferenceRequestRequestTypeDef(BaseValidatorModel):
    Username: str
    UserPoolId: str
    SMSMfaSettings: Optional[SMSMfaSettingsTypeTypeDef] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsTypeTypeDef] = None

class SetUserMFAPreferenceRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    SMSMfaSettings: Optional[SMSMfaSettingsTypeTypeDef] = None
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsTypeTypeDef] = None

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

class SetUICustomizationRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CSS: Optional[str] = None
    ImageFile: Optional[BlobTypeDef] = None

class LogConfigurationTypeTypeDef(BaseValidatorModel):
    LogLevel: Literal["ERROR"]
    EventSource: Literal["userNotification"]
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationTypeTypeDef] = None

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

class ConfirmDeviceRequestRequestTypeDef(BaseValidatorModel):
    AccessToken: str
    DeviceKey: str
    DeviceSecretVerifierConfig: Optional[DeviceSecretVerifierConfigTypeTypeDef] = None
    DeviceName: Optional[str] = None

class ConfirmForgotPasswordRequestRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    Password: str
    SecretHash: Optional[str] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class ConfirmSignUpRequestRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    ConfirmationCode: str
    SecretHash: Optional[str] = None
    ForceAliasCreation: Optional[bool] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class ForgotPasswordRequestRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class InitiateAuthRequestRequestTypeDef(BaseValidatorModel):
    AuthFlow: AuthFlowTypeType
    ClientId: str
    AuthParameters: Optional[Mapping[str, str]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None

class ResendConfirmationCodeRequestRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    SecretHash: Optional[str] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class RespondToAuthChallengeRequestRequestTypeDef(BaseValidatorModel):
    ClientId: str
    ChallengeName: ChallengeNameTypeType
    Session: Optional[str] = None
    ChallengeResponses: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    UserContextData: Optional[UserContextDataTypeTypeDef] = None
    ClientMetadata: Optional[Mapping[str, str]] = None

class SignUpRequestRequestTypeDef(BaseValidatorModel):
    ClientId: str
    Username: str
    Password: str
    SecretHash: Optional[str] = None
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

class CreateResourceServerRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: Optional[Sequence[ResourceServerScopeTypeTypeDef]] = None

class ResourceServerTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    Identifier: Optional[str] = None
    Name: Optional[str] = None
    Scopes: Optional[List[ResourceServerScopeTypeTypeDef]] = None

class UpdateResourceServerRequestRequestTypeDef(BaseValidatorModel):
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

class CreateUserPoolClientRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateUserPoolClientRequestRequestTypeDef(BaseValidatorModel):
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

class CreateUserPoolDomainRequestRequestTypeDef(BaseValidatorModel):
    Domain: str
    UserPoolId: str
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

class UpdateUserPoolDomainRequestRequestTypeDef(BaseValidatorModel):
    Domain: str
    UserPoolId: str
    CustomDomainConfig: CustomDomainConfigTypeTypeDef

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

class NotifyConfigurationTypeTypeDef(BaseValidatorModel):
    SourceArn: str
    From: Optional[str] = None
    ReplyTo: Optional[str] = None
    BlockEmail: Optional[NotifyEmailTypeTypeDef] = None
    NoActionEmail: Optional[NotifyEmailTypeTypeDef] = None
    MfaEmail: Optional[NotifyEmailTypeTypeDef] = None

class UserPoolPolicyTypeTypeDef(BaseValidatorModel):
    PasswordPolicy: Optional[PasswordPolicyTypeTypeDef] = None

class SchemaAttributeTypeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    AttributeDataType: Optional[AttributeDataTypeType] = None
    DeveloperOnlyAttribute: Optional[bool] = None
    Mutable: Optional[bool] = None
    Required: Optional[bool] = None
    NumberAttributeConstraints: Optional[NumberAttributeConstraintsTypeTypeDef] = None
    StringAttributeConstraints: Optional[StringAttributeConstraintsTypeTypeDef] = None

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

class AdminListUserAuthEventsResponseTypeDef(BaseValidatorModel):
    AuthEvents: List[AuthEventTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AdminInitiateAuthResponseTypeDef(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class RespondToAuthChallengeResponseTypeDef(BaseValidatorModel):
    ChallengeName: ChallengeNameTypeType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: AuthenticationResultTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LogDeliveryConfigurationTypeTypeDef(BaseValidatorModel):
    UserPoolId: str
    LogConfigurations: List[LogConfigurationTypeTypeDef]

class SetLogDeliveryConfigurationRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    LogConfigurations: Sequence[LogConfigurationTypeTypeDef]

class AdminInitiateAuthRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: str
    AuthFlow: AuthFlowTypeType
    AuthParameters: Optional[Mapping[str, str]] = None
    ClientMetadata: Optional[Mapping[str, str]] = None
    AnalyticsMetadata: Optional[AnalyticsMetadataTypeTypeDef] = None
    ContextData: Optional[ContextDataTypeTypeDef] = None

class AdminRespondToAuthChallengeRequestRequestTypeDef(BaseValidatorModel):
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
    MfaConfiguration: UserPoolMfaTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SetUserPoolMfaConfigRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    SmsMfaConfiguration: Optional[SmsMfaConfigTypeTypeDef] = None
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigTypeTypeDef] = None
    MfaConfiguration: Optional[UserPoolMfaTypeType] = None

class SetUserPoolMfaConfigResponseTypeDef(BaseValidatorModel):
    SmsMfaConfiguration: SmsMfaConfigTypeTypeDef
    SoftwareTokenMfaConfiguration: SoftwareTokenMfaConfigTypeTypeDef
    MfaConfiguration: UserPoolMfaTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UserPoolDescriptionTypeTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    LambdaConfig: Optional[LambdaConfigTypeTypeDef] = None
    Status: Optional[StatusTypeType] = None
    LastModifiedDate: Optional[datetime] = None
    CreationDate: Optional[datetime] = None

class AccountTakeoverRiskConfigurationTypeTypeDef(BaseValidatorModel):
    Actions: AccountTakeoverActionsTypeTypeDef
    NotifyConfiguration: Optional[NotifyConfigurationTypeTypeDef] = None

class UpdateUserPoolRequestRequestTypeDef(BaseValidatorModel):
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

class AddCustomAttributesRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    CustomAttributes: Sequence[SchemaAttributeTypeTypeDef]

class CreateUserPoolRequestRequestTypeDef(BaseValidatorModel):
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

class UserPoolTypeTypeDef(BaseValidatorModel):
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

class GetLogDeliveryConfigurationResponseTypeDef(BaseValidatorModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetLogDeliveryConfigurationResponseTypeDef(BaseValidatorModel):
    LogDeliveryConfiguration: LogDeliveryConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUserPoolsResponseTypeDef(BaseValidatorModel):
    UserPools: List[UserPoolDescriptionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RiskConfigurationTypeTypeDef(BaseValidatorModel):
    UserPoolId: Optional[str] = None
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[       CompromisedCredentialsRiskConfigurationTypeOutputTypeDef     ] = None
    AccountTakeoverRiskConfiguration: Optional[       AccountTakeoverRiskConfigurationTypeTypeDef     ] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeOutputTypeDef] = None
    LastModifiedDate: Optional[datetime] = None

class SetRiskConfigurationRequestRequestTypeDef(BaseValidatorModel):
    UserPoolId: str
    ClientId: Optional[str] = None
    CompromisedCredentialsRiskConfiguration: Optional[       CompromisedCredentialsRiskConfigurationTypeTypeDef     ] = None
    AccountTakeoverRiskConfiguration: Optional[       AccountTakeoverRiskConfigurationTypeTypeDef     ] = None
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationTypeTypeDef] = None

class CreateUserPoolResponseTypeDef(BaseValidatorModel):
    UserPool: UserPoolTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserPoolResponseTypeDef(BaseValidatorModel):
    UserPool: UserPoolTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRiskConfigurationResponseTypeDef(BaseValidatorModel):
    RiskConfiguration: RiskConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetRiskConfigurationResponseTypeDef(BaseValidatorModel):
    RiskConfiguration: RiskConfigurationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

