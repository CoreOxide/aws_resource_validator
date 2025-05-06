from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2.pinpoint_sms_voice_v2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountAttribute(BaseValidatorModel):
    Name: AccountAttributeNameType
    Value: str


class AccountLimit(BaseValidatorModel):
    Name: AccountLimitNameType
    Used: int
    Max: int


class AssociateOriginationIdentityRequest(BaseValidatorModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CloudWatchLogsDestination(BaseValidatorModel):
    IamRoleArn: str
    LogGroupArn: str


class ConfigurationSetFilter(BaseValidatorModel):
    Name: ConfigurationSetFilterNameType
    Values: List[str]


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class KinesisFirehoseDestination(BaseValidatorModel):
    IamRoleArn: str
    DeliveryStreamArn: str


class SnsDestination(BaseValidatorModel):
    TopicArn: str


class CreateRegistrationAssociationRequest(BaseValidatorModel):
    RegistrationId: str
    ResourceId: str


class CreateRegistrationVersionRequest(BaseValidatorModel):
    RegistrationId: str


class RegistrationVersionStatusHistory(BaseValidatorModel):
    DraftTimestamp: datetime
    SubmittedTimestamp: Optional[datetime] = None
    ReviewingTimestamp: Optional[datetime] = None
    RequiresAuthenticationTimestamp: Optional[datetime] = None
    ApprovedTimestamp: Optional[datetime] = None
    DiscardedTimestamp: Optional[datetime] = None
    DeniedTimestamp: Optional[datetime] = None
    RevokedTimestamp: Optional[datetime] = None
    ArchivedTimestamp: Optional[datetime] = None


class DeleteConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteDefaultMessageTypeRequest(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteDefaultSenderIdRequest(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteKeywordRequest(BaseValidatorModel):
    OriginationIdentity: str
    Keyword: str


class DeleteOptOutListRequest(BaseValidatorModel):
    OptOutListName: str


class DeleteOptedOutNumberRequest(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumber: str


class DeletePoolRequest(BaseValidatorModel):
    PoolId: str


class DeleteProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str


class DeleteProtectConfigurationRuleSetNumberOverrideRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str


class DeleteRegistrationAttachmentRequest(BaseValidatorModel):
    RegistrationAttachmentId: str


class DeleteRegistrationFieldValueRequest(BaseValidatorModel):
    RegistrationId: str
    FieldPath: str


class DeleteRegistrationRequest(BaseValidatorModel):
    RegistrationId: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteVerifiedDestinationNumberRequest(BaseValidatorModel):
    VerifiedDestinationNumberId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAccountAttributesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeAccountLimitsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class KeywordFilter(BaseValidatorModel):
    Name: Literal['keyword-action']
    Values: List[str]


class KeywordInformation(BaseValidatorModel):
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType


class DescribeOptOutListsRequest(BaseValidatorModel):
    OptOutListNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class OptOutListInformation(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime


class OptedOutFilter(BaseValidatorModel):
    Name: Literal['end-user-opted-out']
    Values: List[str]


class OptedOutNumberInformation(BaseValidatorModel):
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool


class PhoneNumberFilter(BaseValidatorModel):
    Name: PhoneNumberFilterNameType
    Values: List[str]


class PhoneNumberInformation(BaseValidatorModel):
    PhoneNumberArn: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: NumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    DeletionProtectionEnabled: bool
    CreatedTimestamp: datetime
    PhoneNumberId: Optional[str] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    PoolId: Optional[str] = None
    RegistrationId: Optional[str] = None


class PoolFilter(BaseValidatorModel):
    Name: PoolFilterNameType
    Values: List[str]


class PoolInformation(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    DeletionProtectionEnabled: bool
    CreatedTimestamp: datetime
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None


class ProtectConfigurationFilter(BaseValidatorModel):
    Name: ProtectConfigurationFilterNameType
    Values: List[str]


class ProtectConfigurationInformation(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool


class RegistrationAttachmentFilter(BaseValidatorModel):
    Name: Literal['attachment-status']
    Values: List[str]


class RegistrationAttachmentsInformation(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    CreatedTimestamp: datetime
    AttachmentUploadErrorReason: Optional[Literal['INTERNAL_ERROR']] = None


class DescribeRegistrationFieldDefinitionsRequest(BaseValidatorModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationFieldValuesRequest(BaseValidatorModel):
    RegistrationId: str
    VersionNumber: Optional[int] = None
    SectionPath: Optional[str] = None
    FieldPaths: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RegistrationFieldValueInformation(BaseValidatorModel):
    FieldPath: str
    SelectChoices: Optional[List[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None
    DeniedReason: Optional[str] = None


class DescribeRegistrationSectionDefinitionsRequest(BaseValidatorModel):
    RegistrationType: str
    SectionPaths: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RegistrationTypeFilter(BaseValidatorModel):
    Name: RegistrationTypeFilterNameType
    Values: List[str]


class RegistrationVersionFilter(BaseValidatorModel):
    Name: Literal['registration-version-status']
    Values: List[str]


class RegistrationFilter(BaseValidatorModel):
    Name: RegistrationFilterNameType
    Values: List[str]


class RegistrationInformation(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    CreatedTimestamp: datetime
    ApprovedVersionNumber: Optional[int] = None
    LatestDeniedVersionNumber: Optional[int] = None
    AdditionalAttributes: Optional[Dict[str, str]] = None


class SenderIdAndCountry(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str


class SenderIdFilter(BaseValidatorModel):
    Name: SenderIdFilterNameType
    Values: List[str]


class SenderIdInformation(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: Optional[str] = None


class DescribeSpendLimitsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SpendLimit(BaseValidatorModel):
    Name: SpendLimitNameType
    EnforcedLimit: int
    MaxLimit: int
    Overridden: bool


class VerifiedDestinationNumberFilter(BaseValidatorModel):
    Name: Literal['status']
    Values: List[str]


class VerifiedDestinationNumberInformation(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime


class DisassociateOriginationIdentityRequest(BaseValidatorModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None


class DisassociateProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str


class DiscardRegistrationVersionRequest(BaseValidatorModel):
    RegistrationId: str


class GetProtectConfigurationCountryRuleSetRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType


class ProtectConfigurationCountryRuleSetInformation(BaseValidatorModel):
    ProtectStatus: ProtectStatusType


class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class PoolOriginationIdentitiesFilter(BaseValidatorModel):
    Name: PoolOriginationIdentitiesFilterNameType
    Values: List[str]


class OriginationIdentityMetadata(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    NumberCapabilities: List[NumberCapabilityType]
    PhoneNumber: Optional[str] = None


class ProtectConfigurationRuleSetNumberOverrideFilterItem(BaseValidatorModel):
    Name: ProtectConfigurationRuleSetNumberOverrideFilterNameType
    Values: List[str]


class ProtectConfigurationRuleSetNumberOverride(BaseValidatorModel):
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: Optional[str] = None
    ExpirationTimestamp: Optional[datetime] = None


class RegistrationAssociationFilter(BaseValidatorModel):
    Name: RegistrationAssociationFilterNameType
    Values: List[str]


class RegistrationAssociationMetadata(BaseValidatorModel):
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: Optional[str] = None
    PhoneNumber: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PutKeywordRequest(BaseValidatorModel):
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: Optional[KeywordActionType] = None


class PutMessageFeedbackRequest(BaseValidatorModel):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType


class PutOptedOutNumberRequest(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumber: str

Timestamp = Union[datetime, str]


class PutRegistrationFieldValueRequest(BaseValidatorModel):
    RegistrationId: str
    FieldPath: str
    SelectChoices: Optional[List[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RegistrationDeniedReasonInformation(BaseValidatorModel):
    Reason: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None


class SelectValidation(BaseValidatorModel):
    MinChoices: int
    MaxChoices: int
    Options: List[str]


class TextValidation(BaseValidatorModel):
    MinLength: int
    MaxLength: int
    Pattern: str


class SelectOptionDescription(BaseValidatorModel):
    Option: str
    Title: Optional[str] = None
    Description: Optional[str] = None


class RegistrationSectionDisplayHints(BaseValidatorModel):
    Title: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None


class RegistrationTypeDisplayHints(BaseValidatorModel):
    Title: str
    ShortDescription: Optional[str] = None
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None


class SupportedAssociation(BaseValidatorModel):
    ResourceType: str
    AssociationBehavior: RegistrationAssociationBehaviorType
    DisassociationBehavior: RegistrationDisassociationBehaviorType
    IsoCountryCode: Optional[str] = None


class ReleasePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class ReleaseSenderIdRequest(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str


class SendDestinationNumberVerificationCodeRequest(BaseValidatorModel):
    VerifiedDestinationNumberId: str
    VerificationChannel: VerificationChannelType
    LanguageCode: Optional[LanguageCodeType] = None
    OriginationIdentity: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Context: Optional[Dict[str, str]] = None
    DestinationCountryParameters: Optional[Dict[DestinationCountryParameterKeyType, str]] = None


class SendMediaMessageRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    OriginationIdentity: str
    MessageBody: Optional[str] = None
    MediaUrls: Optional[List[str]] = None
    ConfigurationSetName: Optional[str] = None
    MaxPrice: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Dict[str, str]] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None
    MessageFeedbackEnabled: Optional[bool] = None


class SendTextMessageRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    OriginationIdentity: Optional[str] = None
    MessageBody: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    Keyword: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    MaxPrice: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Dict[str, str]] = None
    DestinationCountryParameters: Optional[Dict[DestinationCountryParameterKeyType, str]] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None
    MessageFeedbackEnabled: Optional[bool] = None


class SendVoiceMessageRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    OriginationIdentity: str
    MessageBody: Optional[str] = None
    MessageBodyTextType: Optional[VoiceMessageBodyTextTypeType] = None
    VoiceId: Optional[VoiceIdType] = None
    ConfigurationSetName: Optional[str] = None
    MaxPricePerMinute: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Dict[str, str]] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None
    MessageFeedbackEnabled: Optional[bool] = None


class SetAccountDefaultProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str


class SetDefaultMessageFeedbackEnabledRequest(BaseValidatorModel):
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool


class SetDefaultMessageTypeRequest(BaseValidatorModel):
    ConfigurationSetName: str
    MessageType: MessageTypeType


class SetDefaultSenderIdRequest(BaseValidatorModel):
    ConfigurationSetName: str
    SenderId: str


class SetMediaMessageSpendLimitOverrideRequest(BaseValidatorModel):
    MonthlyLimit: int


class SetTextMessageSpendLimitOverrideRequest(BaseValidatorModel):
    MonthlyLimit: int


class SetVoiceMessageSpendLimitOverrideRequest(BaseValidatorModel):
    MonthlyLimit: int


class SubmitRegistrationVersionRequest(BaseValidatorModel):
    RegistrationId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None


class UpdatePoolRequest(BaseValidatorModel):
    PoolId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    SharedRoutesEnabled: Optional[bool] = None
    DeletionProtectionEnabled: Optional[bool] = None


class UpdateProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    DeletionProtectionEnabled: Optional[bool] = None


class UpdateSenderIdRequest(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str
    DeletionProtectionEnabled: Optional[bool] = None


class VerifyDestinationNumberRequest(BaseValidatorModel):
    VerifiedDestinationNumberId: str
    VerificationCode: str


class AssociateOriginationIdentityResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadata


class AssociateProtectConfigurationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


class CreateRegistrationAssociationResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: str
    PhoneNumber: str
    ResponseMetadata: ResponseMetadata


class DeleteAccountDefaultProtectConfigurationResult(BaseValidatorModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


class DeleteDefaultMessageTypeResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadata


class DeleteDefaultSenderIdResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadata


class DeleteKeywordResult(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadata


class DeleteMediaMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


class DeleteOptOutListResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteOptedOutNumberResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadata


class DeletePoolResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteProtectConfigurationResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


class DeleteProtectConfigurationRuleSetNumberOverrideResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteRegistrationAttachmentResult(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    AttachmentUploadErrorReason: Literal['INTERNAL_ERROR']
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteRegistrationFieldValueResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadata


class DeleteRegistrationResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    ApprovedVersionNumber: int
    LatestDeniedVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteResourcePolicyResult(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteTextMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


class DeleteVerifiedDestinationNumberResult(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteVoiceMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


class DescribeAccountAttributesResult(BaseValidatorModel):
    AccountAttributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAccountLimitsResult(BaseValidatorModel):
    AccountLimits: List[AccountLimit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DisassociateOriginationIdentityResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadata


class DisassociateProtectConfigurationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResult(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class PutKeywordResult(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadata


class PutMessageFeedbackResult(BaseValidatorModel):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType
    ResponseMetadata: ResponseMetadata


class PutOptedOutNumberResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadata


class PutProtectConfigurationRuleSetNumberOverrideResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class PutRegistrationFieldValueResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResult(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ReleasePhoneNumberResult(BaseValidatorModel):
    PhoneNumberArn: str
    PhoneNumberId: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: NumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    RegistrationId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ReleaseSenderIdResult(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadata


class SendDestinationNumberVerificationCodeResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendMediaMessageResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendTextMessageResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SendVoiceMessageResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


class SetAccountDefaultProtectConfigurationResult(BaseValidatorModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


class SetDefaultMessageFeedbackEnabledResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool
    ResponseMetadata: ResponseMetadata


class SetDefaultMessageTypeResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadata


class SetDefaultSenderIdResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadata


class SetMediaMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


class SetTextMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


class SetVoiceMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


class UpdatePhoneNumberResult(BaseValidatorModel):
    PhoneNumberArn: str
    PhoneNumberId: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: NumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    DeletionProtectionEnabled: bool
    RegistrationId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class UpdatePoolResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    DeletionProtectionEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class UpdateProtectConfigurationResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


class UpdateSenderIdResult(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadata


class VerifyDestinationNumberResult(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationSetsRequest(BaseValidatorModel):
    ConfigurationSetNames: Optional[List[str]] = None
    Filters: Optional[List[ConfigurationSetFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CreateConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class CreateConfigurationSetResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateOptOutListRequest(BaseValidatorModel):
    OptOutListName: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class CreateOptOutListResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreatePoolRequest(BaseValidatorModel):
    OriginationIdentity: str
    IsoCountryCode: str
    MessageType: MessageTypeType
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class CreatePoolResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    DeletionProtectionEnabled: bool
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateProtectConfigurationRequest(BaseValidatorModel):
    ClientToken: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class CreateProtectConfigurationResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateRegistrationAttachmentRequest(BaseValidatorModel):
    AttachmentBody: Optional[Blob] = None
    AttachmentUrl: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class CreateRegistrationAttachmentResult(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateRegistrationRequest(BaseValidatorModel):
    RegistrationType: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class CreateRegistrationResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateVerifiedDestinationNumberRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class CreateVerifiedDestinationNumberResult(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResult(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class RequestPhoneNumberRequest(BaseValidatorModel):
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: RequestableNumberTypeType
    OptOutListName: Optional[str] = None
    PoolId: Optional[str] = None
    RegistrationId: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class RequestPhoneNumberResult(BaseValidatorModel):
    PhoneNumberArn: str
    PhoneNumberId: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: RequestableNumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    DeletionProtectionEnabled: bool
    PoolId: str
    RegistrationId: str
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class RequestSenderIdRequest(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str
    MessageTypes: Optional[List[MessageTypeType]] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class RequestSenderIdResult(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    MatchingEventTypes: List[EventTypeType]
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestination] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    SnsDestination: Optional[SnsDestination] = None
    ClientToken: Optional[str] = None


class EventDestination(BaseValidatorModel):
    EventDestinationName: str
    Enabled: bool
    MatchingEventTypes: List[EventTypeType]
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestination] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    SnsDestination: Optional[SnsDestination] = None


class UpdateEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[List[EventTypeType]] = None
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestination] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    SnsDestination: Optional[SnsDestination] = None


class CreateRegistrationVersionResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistory
    ResponseMetadata: ResponseMetadata


class DiscardRegistrationVersionResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistory
    ResponseMetadata: ResponseMetadata


class SubmitRegistrationVersionResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistory
    ResponseMetadata: ResponseMetadata


class DescribeAccountAttributesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAccountLimitsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConfigurationSetsRequestPaginate(BaseValidatorModel):
    ConfigurationSetNames: Optional[List[str]] = None
    Filters: Optional[List[ConfigurationSetFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOptOutListsRequestPaginate(BaseValidatorModel):
    OptOutListNames: Optional[List[str]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationFieldDefinitionsRequestPaginate(BaseValidatorModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationFieldValuesRequestPaginate(BaseValidatorModel):
    RegistrationId: str
    VersionNumber: Optional[int] = None
    SectionPath: Optional[str] = None
    FieldPaths: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationSectionDefinitionsRequestPaginate(BaseValidatorModel):
    RegistrationType: str
    SectionPaths: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSpendLimitsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeKeywordsRequestPaginate(BaseValidatorModel):
    OriginationIdentity: str
    Keywords: Optional[List[str]] = None
    Filters: Optional[List[KeywordFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeKeywordsRequest(BaseValidatorModel):
    OriginationIdentity: str
    Keywords: Optional[List[str]] = None
    Filters: Optional[List[KeywordFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeKeywordsResult(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keywords: List[KeywordInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOptOutListsResult(BaseValidatorModel):
    OptOutLists: List[OptOutListInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOptedOutNumbersRequestPaginate(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumbers: Optional[List[str]] = None
    Filters: Optional[List[OptedOutFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOptedOutNumbersRequest(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumbers: Optional[List[str]] = None
    Filters: Optional[List[OptedOutFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeOptedOutNumbersResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumbers: List[OptedOutNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePhoneNumbersRequestPaginate(BaseValidatorModel):
    PhoneNumberIds: Optional[List[str]] = None
    Filters: Optional[List[PhoneNumberFilter]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePhoneNumbersRequest(BaseValidatorModel):
    PhoneNumberIds: Optional[List[str]] = None
    Filters: Optional[List[PhoneNumberFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class DescribePhoneNumbersResult(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePoolsRequestPaginate(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[PoolFilter]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePoolsRequest(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[PoolFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class DescribePoolsResult(BaseValidatorModel):
    Pools: List[PoolInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeProtectConfigurationsRequestPaginate(BaseValidatorModel):
    ProtectConfigurationIds: Optional[List[str]] = None
    Filters: Optional[List[ProtectConfigurationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeProtectConfigurationsRequest(BaseValidatorModel):
    ProtectConfigurationIds: Optional[List[str]] = None
    Filters: Optional[List[ProtectConfigurationFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeProtectConfigurationsResult(BaseValidatorModel):
    ProtectConfigurations: List[ProtectConfigurationInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRegistrationAttachmentsRequestPaginate(BaseValidatorModel):
    RegistrationAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationAttachmentFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationAttachmentsRequest(BaseValidatorModel):
    RegistrationAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationAttachmentFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationAttachmentsResult(BaseValidatorModel):
    RegistrationAttachments: List[RegistrationAttachmentsInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRegistrationFieldValuesResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationFieldValues: List[RegistrationFieldValueInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRegistrationinitionsRequestPaginate(BaseValidatorModel):
    RegistrationTypes: Optional[List[str]] = None
    Filters: Optional[List[RegistrationTypeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationinitionsRequest(BaseValidatorModel):
    RegistrationTypes: Optional[List[str]] = None
    Filters: Optional[List[RegistrationTypeFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationVersionsRequestPaginate(BaseValidatorModel):
    RegistrationId: str
    VersionNumbers: Optional[List[int]] = None
    Filters: Optional[List[RegistrationVersionFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationVersionsRequest(BaseValidatorModel):
    RegistrationId: str
    VersionNumbers: Optional[List[int]] = None
    Filters: Optional[List[RegistrationVersionFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationsRequestPaginate(BaseValidatorModel):
    RegistrationIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistrationsRequest(BaseValidatorModel):
    RegistrationIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationsResult(BaseValidatorModel):
    Registrations: List[RegistrationInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSenderIdsRequestPaginate(BaseValidatorModel):
    SenderIds: Optional[List[SenderIdAndCountry]] = None
    Filters: Optional[List[SenderIdFilter]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSenderIdsRequest(BaseValidatorModel):
    SenderIds: Optional[List[SenderIdAndCountry]] = None
    Filters: Optional[List[SenderIdFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class DescribeSenderIdsResult(BaseValidatorModel):
    SenderIds: List[SenderIdInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSpendLimitsResult(BaseValidatorModel):
    SpendLimits: List[SpendLimit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeVerifiedDestinationNumbersRequestPaginate(BaseValidatorModel):
    VerifiedDestinationNumberIds: Optional[List[str]] = None
    DestinationPhoneNumbers: Optional[List[str]] = None
    Filters: Optional[List[VerifiedDestinationNumberFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeVerifiedDestinationNumbersRequest(BaseValidatorModel):
    VerifiedDestinationNumberIds: Optional[List[str]] = None
    DestinationPhoneNumbers: Optional[List[str]] = None
    Filters: Optional[List[VerifiedDestinationNumberFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeVerifiedDestinationNumbersResult(BaseValidatorModel):
    VerifiedDestinationNumbers: List[VerifiedDestinationNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetProtectConfigurationCountryRuleSetResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformation]
    ResponseMetadata: ResponseMetadata


class UpdateProtectConfigurationCountryRuleSetRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSetUpdates: Dict[str, ProtectConfigurationCountryRuleSetInformation]


class UpdateProtectConfigurationCountryRuleSetResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformation]
    ResponseMetadata: ResponseMetadata


class ListPoolOriginationIdentitiesRequestPaginate(BaseValidatorModel):
    PoolId: str
    Filters: Optional[List[PoolOriginationIdentitiesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPoolOriginationIdentitiesRequest(BaseValidatorModel):
    PoolId: str
    Filters: Optional[List[PoolOriginationIdentitiesFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoolOriginationIdentitiesResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentities: List[OriginationIdentityMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProtectConfigurationRuleSetNumberOverridesRequestPaginate(BaseValidatorModel):
    ProtectConfigurationId: str
    Filters: Optional[List[ProtectConfigurationRuleSetNumberOverrideFilterItem]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtectConfigurationRuleSetNumberOverridesRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    Filters: Optional[List[ProtectConfigurationRuleSetNumberOverrideFilterItem]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProtectConfigurationRuleSetNumberOverridesResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    RuleSetNumberOverrides: List[ProtectConfigurationRuleSetNumberOverride]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRegistrationAssociationsRequestPaginate(BaseValidatorModel):
    RegistrationId: str
    Filters: Optional[List[RegistrationAssociationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegistrationAssociationsRequest(BaseValidatorModel):
    RegistrationId: str
    Filters: Optional[List[RegistrationAssociationFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRegistrationAssociationsResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationAssociations: List[RegistrationAssociationMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutProtectConfigurationRuleSetNumberOverrideRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    Action: ProtectConfigurationRuleOverrideActionType
    ClientToken: Optional[str] = None
    ExpirationTimestamp: Optional[Timestamp] = None


class RegistrationVersionInformation(BaseValidatorModel):
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistory
    DeniedReasons: Optional[List[RegistrationDeniedReasonInformation]] = None


class RegistrationFieldDisplayHints(BaseValidatorModel):
    Title: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None
    SelectOptionDescriptions: Optional[List[SelectOptionDescription]] = None
    TextValidationDescription: Optional[str] = None
    ExampleTextValue: Optional[str] = None


class RegistrationSectionDefinition(BaseValidatorModel):
    SectionPath: str
    DisplayHints: RegistrationSectionDisplayHints


class Registrationinition(BaseValidatorModel):
    RegistrationType: str
    DisplayHints: RegistrationTypeDisplayHints
    SupportedAssociations: Optional[List[SupportedAssociation]] = None


class ConfigurationSetInformation(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestination]
    CreatedTimestamp: datetime
    DefaultMessageType: Optional[MessageTypeType] = None
    DefaultSenderId: Optional[str] = None
    DefaultMessageFeedbackEnabled: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None


class CreateEventDestinationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestination
    ResponseMetadata: ResponseMetadata


class DeleteConfigurationSetResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestination]
    DefaultMessageType: MessageTypeType
    DefaultSenderId: str
    DefaultMessageFeedbackEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteEventDestinationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestination
    ResponseMetadata: ResponseMetadata


class UpdateEventDestinationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestination
    ResponseMetadata: ResponseMetadata


class DescribeRegistrationVersionsResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationVersions: List[RegistrationVersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RegistrationFieldDefinition(BaseValidatorModel):
    SectionPath: str
    FieldPath: str
    FieldType: FieldTypeType
    FieldRequirement: FieldRequirementType
    DisplayHints: RegistrationFieldDisplayHints
    SelectValidation: Optional[SelectValidation] = None
    TextValidation: Optional[TextValidation] = None


class DescribeRegistrationSectionDefinitionsResult(BaseValidatorModel):
    RegistrationType: str
    RegistrationSectionDefinitions: List[RegistrationSectionDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRegistrationinitionsResult(BaseValidatorModel):
    RegistrationTypeDefinitions: List[Registrationinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeConfigurationSetsResult(BaseValidatorModel):
    ConfigurationSets: List[ConfigurationSetInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRegistrationFieldDefinitionsResult(BaseValidatorModel):
    RegistrationType: str
    RegistrationFieldDefinitions: List[RegistrationFieldDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None