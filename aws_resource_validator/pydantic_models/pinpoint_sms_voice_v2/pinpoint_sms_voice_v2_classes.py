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


# This class is the input for the 'associate_origination_identity' function.
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


# This class is the input for the 'associate_protect_configuration' function.
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


# This class is the input for the 'create_registration_association' function.
class CreateRegistrationAssociationRequest(BaseValidatorModel):
    RegistrationId: str
    ResourceId: str


# This class is the input for the 'create_registration_version' function.
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


# This class is the input for the 'delete_configuration_set' function.
class DeleteConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str


# This class is the input for the 'delete_default_message_type' function.
class DeleteDefaultMessageTypeRequest(BaseValidatorModel):
    ConfigurationSetName: str


# This class is the input for the 'delete_default_sender_id' function.
class DeleteDefaultSenderIdRequest(BaseValidatorModel):
    ConfigurationSetName: str


# This class is the input for the 'delete_event_destination' function.
class DeleteEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


# This class is the input for the 'delete_keyword' function.
class DeleteKeywordRequest(BaseValidatorModel):
    OriginationIdentity: str
    Keyword: str


# This class is the input for the 'delete_opt_out_list' function.
class DeleteOptOutListRequest(BaseValidatorModel):
    OptOutListName: str


# This class is the input for the 'delete_opted_out_number' function.
class DeleteOptedOutNumberRequest(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumber: str


# This class is the input for the 'delete_pool' function.
class DeletePoolRequest(BaseValidatorModel):
    PoolId: str


# This class is the input for the 'delete_protect_configuration' function.
class DeleteProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str


# This class is the input for the 'delete_protect_configuration_rule_set_number_override' function.
class DeleteProtectConfigurationRuleSetNumberOverrideRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str


# This class is the input for the 'delete_registration_attachment' function.
class DeleteRegistrationAttachmentRequest(BaseValidatorModel):
    RegistrationAttachmentId: str


# This class is the input for the 'delete_registration_field_value' function.
class DeleteRegistrationFieldValueRequest(BaseValidatorModel):
    RegistrationId: str
    FieldPath: str


# This class is the input for the 'delete_registration' function.
class DeleteRegistrationRequest(BaseValidatorModel):
    RegistrationId: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'delete_verified_destination_number' function.
class DeleteVerifiedDestinationNumberRequest(BaseValidatorModel):
    VerifiedDestinationNumberId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_account_attributes' function.
class DescribeAccountAttributesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_account_limits' function.
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


# This class is the input for the 'describe_opt_out_lists' function.
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


# This class is the input for the 'describe_registration_field_definitions' function.
class DescribeRegistrationFieldDefinitionsRequest(BaseValidatorModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_registration_field_values' function.
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


# This class is the input for the 'describe_registration_section_definitions' function.
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


# This class is the input for the 'describe_spend_limits' function.
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


# This class is the input for the 'disassociate_origination_identity' function.
class DisassociateOriginationIdentityRequest(BaseValidatorModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None


# This class is the input for the 'disassociate_protect_configuration' function.
class DisassociateProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str


# This class is the input for the 'discard_registration_version' function.
class DiscardRegistrationVersionRequest(BaseValidatorModel):
    RegistrationId: str


# This class is the input for the 'get_protect_configuration_country_rule_set' function.
class GetProtectConfigurationCountryRuleSetRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType


class ProtectConfigurationCountryRuleSetInformation(BaseValidatorModel):
    ProtectStatus: ProtectStatusType


# This class is the input for the 'get_resource_policy' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'put_keyword' function.
class PutKeywordRequest(BaseValidatorModel):
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: Optional[KeywordActionType] = None


# This class is the input for the 'put_message_feedback' function.
class PutMessageFeedbackRequest(BaseValidatorModel):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType


# This class is the input for the 'put_opted_out_number' function.
class PutOptedOutNumberRequest(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumber: str

Timestamp = Union[datetime, str]


# This class is the input for the 'put_registration_field_value' function.
class PutRegistrationFieldValueRequest(BaseValidatorModel):
    RegistrationId: str
    FieldPath: str
    SelectChoices: Optional[List[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
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


# This class is the input for the 'release_phone_number' function.
class ReleasePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'release_sender_id' function.
class ReleaseSenderIdRequest(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str


# This class is the input for the 'send_destination_number_verification_code' function.
class SendDestinationNumberVerificationCodeRequest(BaseValidatorModel):
    VerifiedDestinationNumberId: str
    VerificationChannel: VerificationChannelType
    LanguageCode: Optional[LanguageCodeType] = None
    OriginationIdentity: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Context: Optional[Dict[str, str]] = None
    DestinationCountryParameters: Optional[Dict[DestinationCountryParameterKeyType, str]] = None


# This class is the input for the 'send_media_message' function.
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


# This class is the input for the 'send_text_message' function.
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


# This class is the input for the 'send_voice_message' function.
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


# This class is the input for the 'set_account_default_protect_configuration' function.
class SetAccountDefaultProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str


# This class is the input for the 'set_default_message_feedback_enabled' function.
class SetDefaultMessageFeedbackEnabledRequest(BaseValidatorModel):
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool


# This class is the input for the 'set_default_message_type' function.
class SetDefaultMessageTypeRequest(BaseValidatorModel):
    ConfigurationSetName: str
    MessageType: MessageTypeType


# This class is the input for the 'set_default_sender_id' function.
class SetDefaultSenderIdRequest(BaseValidatorModel):
    ConfigurationSetName: str
    SenderId: str


# This class is the input for the 'set_media_message_spend_limit_override' function.
class SetMediaMessageSpendLimitOverrideRequest(BaseValidatorModel):
    MonthlyLimit: int


# This class is the input for the 'set_text_message_spend_limit_override' function.
class SetTextMessageSpendLimitOverrideRequest(BaseValidatorModel):
    MonthlyLimit: int


# This class is the input for the 'set_voice_message_spend_limit_override' function.
class SetVoiceMessageSpendLimitOverrideRequest(BaseValidatorModel):
    MonthlyLimit: int


# This class is the input for the 'submit_registration_version' function.
class SubmitRegistrationVersionRequest(BaseValidatorModel):
    RegistrationId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_phone_number' function.
class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None


# This class is the input for the 'update_pool' function.
class UpdatePoolRequest(BaseValidatorModel):
    PoolId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    SharedRoutesEnabled: Optional[bool] = None
    DeletionProtectionEnabled: Optional[bool] = None


# This class is the input for the 'update_protect_configuration' function.
class UpdateProtectConfigurationRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    DeletionProtectionEnabled: Optional[bool] = None


# This class is the input for the 'update_sender_id' function.
class UpdateSenderIdRequest(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str
    DeletionProtectionEnabled: Optional[bool] = None


# This class is the input for the 'verify_destination_number' function.
class VerifyDestinationNumberRequest(BaseValidatorModel):
    VerifiedDestinationNumberId: str
    VerificationCode: str


# This class is the output for the 'associate_origination_identity' function.
class AssociateOriginationIdentityResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_protect_configuration' function.
class AssociateProtectConfigurationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_registration_association' function.
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


# This class is the output for the 'delete_default_message_type' function.
class DeleteDefaultMessageTypeResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_default_sender_id' function.
class DeleteDefaultSenderIdResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_keyword' function.
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


# This class is the output for the 'delete_opt_out_list' function.
class DeleteOptOutListResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_opted_out_number' function.
class DeleteOptedOutNumberResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pool' function.
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


# This class is the output for the 'delete_protect_configuration' function.
class DeleteProtectConfigurationResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_protect_configuration_rule_set_number_override' function.
class DeleteProtectConfigurationRuleSetNumberOverrideResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_registration_attachment' function.
class DeleteRegistrationAttachmentResult(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    AttachmentUploadErrorReason: Literal['INTERNAL_ERROR']
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_registration_field_value' function.
class DeleteRegistrationFieldValueResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_registration' function.
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


# This class is the output for the 'delete_resource_policy' function.
class DeleteResourcePolicyResult(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteTextMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_verified_destination_number' function.
class DeleteVerifiedDestinationNumberResult(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class DeleteVoiceMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_account_attributes' function.
class DescribeAccountAttributesResult(BaseValidatorModel):
    AccountAttributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_account_limits' function.
class DescribeAccountLimitsResult(BaseValidatorModel):
    AccountLimits: List[AccountLimit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disassociate_origination_identity' function.
class DisassociateOriginationIdentityResult(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_protect_configuration' function.
class DisassociateProtectConfigurationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResult(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_keyword' function.
class PutKeywordResult(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_message_feedback' function.
class PutMessageFeedbackResult(BaseValidatorModel):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_opted_out_number' function.
class PutOptedOutNumberResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_protect_configuration_rule_set_number_override' function.
class PutProtectConfigurationRuleSetNumberOverrideResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_registration_field_value' function.
class PutRegistrationFieldValueResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResult(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'release_phone_number' function.
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


# This class is the output for the 'release_sender_id' function.
class ReleaseSenderIdResult(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_destination_number_verification_code' function.
class SendDestinationNumberVerificationCodeResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_media_message' function.
class SendMediaMessageResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_text_message' function.
class SendTextMessageResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_voice_message' function.
class SendVoiceMessageResult(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_account_default_protect_configuration' function.
class SetAccountDefaultProtectConfigurationResult(BaseValidatorModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_default_message_feedback_enabled' function.
class SetDefaultMessageFeedbackEnabledResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_default_message_type' function.
class SetDefaultMessageTypeResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_default_sender_id' function.
class SetDefaultSenderIdResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_media_message_spend_limit_override' function.
class SetMediaMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_text_message_spend_limit_override' function.
class SetTextMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_voice_message_spend_limit_override' function.
class SetVoiceMessageSpendLimitOverrideResult(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_phone_number' function.
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


# This class is the output for the 'update_pool' function.
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


# This class is the output for the 'update_protect_configuration' function.
class UpdateProtectConfigurationResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_sender_id' function.
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


# This class is the output for the 'verify_destination_number' function.
class VerifyDestinationNumberResult(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'describe_configuration_sets' function.
class DescribeConfigurationSetsRequest(BaseValidatorModel):
    ConfigurationSetNames: Optional[List[str]] = None
    Filters: Optional[List[ConfigurationSetFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'create_configuration_set' function.
class CreateConfigurationSetRequest(BaseValidatorModel):
    ConfigurationSetName: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'create_configuration_set' function.
class CreateConfigurationSetResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_opt_out_list' function.
class CreateOptOutListRequest(BaseValidatorModel):
    OptOutListName: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'create_opt_out_list' function.
class CreateOptOutListResult(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_pool' function.
class CreatePoolRequest(BaseValidatorModel):
    OriginationIdentity: str
    IsoCountryCode: str
    MessageType: MessageTypeType
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'create_pool' function.
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


# This class is the input for the 'create_protect_configuration' function.
class CreateProtectConfigurationRequest(BaseValidatorModel):
    ClientToken: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_protect_configuration' function.
class CreateProtectConfigurationResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_registration_attachment' function.
class CreateRegistrationAttachmentRequest(BaseValidatorModel):
    AttachmentBody: Optional[Blob] = None
    AttachmentUrl: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'create_registration_attachment' function.
class CreateRegistrationAttachmentResult(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_registration' function.
class CreateRegistrationRequest(BaseValidatorModel):
    RegistrationType: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'create_registration' function.
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


# This class is the input for the 'create_verified_destination_number' function.
class CreateVerifiedDestinationNumberRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'create_verified_destination_number' function.
class CreateVerifiedDestinationNumberResult(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    Tags: List[Tag]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'request_phone_number' function.
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


# This class is the output for the 'request_phone_number' function.
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


# This class is the input for the 'request_sender_id' function.
class RequestSenderIdRequest(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str
    MessageTypes: Optional[List[MessageTypeType]] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'request_sender_id' function.
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


# This class is the input for the 'create_event_destination' function.
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


# This class is the input for the 'update_event_destination' function.
class UpdateEventDestinationRequest(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[List[EventTypeType]] = None
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestination] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestination] = None
    SnsDestination: Optional[SnsDestination] = None


# This class is the output for the 'create_registration_version' function.
class CreateRegistrationVersionResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistory
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'discard_registration_version' function.
class DiscardRegistrationVersionResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistory
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'submit_registration_version' function.
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


# This class is the input for the 'describe_keywords' function.
class DescribeKeywordsRequest(BaseValidatorModel):
    OriginationIdentity: str
    Keywords: Optional[List[str]] = None
    Filters: Optional[List[KeywordFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_keywords' function.
class DescribeKeywordsResult(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keywords: List[KeywordInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_opt_out_lists' function.
class DescribeOptOutListsResult(BaseValidatorModel):
    OptOutLists: List[OptOutListInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOptedOutNumbersRequestPaginate(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumbers: Optional[List[str]] = None
    Filters: Optional[List[OptedOutFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_opted_out_numbers' function.
class DescribeOptedOutNumbersRequest(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumbers: Optional[List[str]] = None
    Filters: Optional[List[OptedOutFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_opted_out_numbers' function.
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


# This class is the input for the 'describe_phone_numbers' function.
class DescribePhoneNumbersRequest(BaseValidatorModel):
    PhoneNumberIds: Optional[List[str]] = None
    Filters: Optional[List[PhoneNumberFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


# This class is the output for the 'describe_phone_numbers' function.
class DescribePhoneNumbersResult(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePoolsRequestPaginate(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[PoolFilter]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_pools' function.
class DescribePoolsRequest(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[PoolFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


# This class is the output for the 'describe_pools' function.
class DescribePoolsResult(BaseValidatorModel):
    Pools: List[PoolInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeProtectConfigurationsRequestPaginate(BaseValidatorModel):
    ProtectConfigurationIds: Optional[List[str]] = None
    Filters: Optional[List[ProtectConfigurationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_protect_configurations' function.
class DescribeProtectConfigurationsRequest(BaseValidatorModel):
    ProtectConfigurationIds: Optional[List[str]] = None
    Filters: Optional[List[ProtectConfigurationFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_protect_configurations' function.
class DescribeProtectConfigurationsResult(BaseValidatorModel):
    ProtectConfigurations: List[ProtectConfigurationInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRegistrationAttachmentsRequestPaginate(BaseValidatorModel):
    RegistrationAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationAttachmentFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_registration_attachments' function.
class DescribeRegistrationAttachmentsRequest(BaseValidatorModel):
    RegistrationAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationAttachmentFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_registration_attachments' function.
class DescribeRegistrationAttachmentsResult(BaseValidatorModel):
    RegistrationAttachments: List[RegistrationAttachmentsInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_registration_field_values' function.
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


# This class is the input for the 'describe_registration_type_definitions' function.
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


# This class is the input for the 'describe_registration_versions' function.
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


# This class is the input for the 'describe_registrations' function.
class DescribeRegistrationsRequest(BaseValidatorModel):
    RegistrationIds: Optional[List[str]] = None
    Filters: Optional[List[RegistrationFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_registrations' function.
class DescribeRegistrationsResult(BaseValidatorModel):
    Registrations: List[RegistrationInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSenderIdsRequestPaginate(BaseValidatorModel):
    SenderIds: Optional[List[SenderIdAndCountry]] = None
    Filters: Optional[List[SenderIdFilter]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_sender_ids' function.
class DescribeSenderIdsRequest(BaseValidatorModel):
    SenderIds: Optional[List[SenderIdAndCountry]] = None
    Filters: Optional[List[SenderIdFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


# This class is the output for the 'describe_sender_ids' function.
class DescribeSenderIdsResult(BaseValidatorModel):
    SenderIds: List[SenderIdInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_spend_limits' function.
class DescribeSpendLimitsResult(BaseValidatorModel):
    SpendLimits: List[SpendLimit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeVerifiedDestinationNumbersRequestPaginate(BaseValidatorModel):
    VerifiedDestinationNumberIds: Optional[List[str]] = None
    DestinationPhoneNumbers: Optional[List[str]] = None
    Filters: Optional[List[VerifiedDestinationNumberFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_verified_destination_numbers' function.
class DescribeVerifiedDestinationNumbersRequest(BaseValidatorModel):
    VerifiedDestinationNumberIds: Optional[List[str]] = None
    DestinationPhoneNumbers: Optional[List[str]] = None
    Filters: Optional[List[VerifiedDestinationNumberFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_verified_destination_numbers' function.
class DescribeVerifiedDestinationNumbersResult(BaseValidatorModel):
    VerifiedDestinationNumbers: List[VerifiedDestinationNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_protect_configuration_country_rule_set' function.
class GetProtectConfigurationCountryRuleSetResult(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformation]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_protect_configuration_country_rule_set' function.
class UpdateProtectConfigurationCountryRuleSetRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSetUpdates: Dict[str, ProtectConfigurationCountryRuleSetInformation]


# This class is the output for the 'update_protect_configuration_country_rule_set' function.
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


# This class is the input for the 'list_pool_origination_identities' function.
class ListPoolOriginationIdentitiesRequest(BaseValidatorModel):
    PoolId: str
    Filters: Optional[List[PoolOriginationIdentitiesFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_pool_origination_identities' function.
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


# This class is the input for the 'list_protect_configuration_rule_set_number_overrides' function.
class ListProtectConfigurationRuleSetNumberOverridesRequest(BaseValidatorModel):
    ProtectConfigurationId: str
    Filters: Optional[List[ProtectConfigurationRuleSetNumberOverrideFilterItem]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_protect_configuration_rule_set_number_overrides' function.
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


# This class is the input for the 'list_registration_associations' function.
class ListRegistrationAssociationsRequest(BaseValidatorModel):
    RegistrationId: str
    Filters: Optional[List[RegistrationAssociationFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_registration_associations' function.
class ListRegistrationAssociationsResult(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationAssociations: List[RegistrationAssociationMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'put_protect_configuration_rule_set_number_override' function.
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


# This class is the output for the 'create_event_destination' function.
class CreateEventDestinationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_configuration_set' function.
class DeleteConfigurationSetResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestination]
    DefaultMessageType: MessageTypeType
    DefaultSenderId: str
    DefaultMessageFeedbackEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_event_destination' function.
class DeleteEventDestinationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_event_destination' function.
class UpdateEventDestinationResult(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_registration_versions' function.
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


# This class is the output for the 'describe_registration_section_definitions' function.
class DescribeRegistrationSectionDefinitionsResult(BaseValidatorModel):
    RegistrationType: str
    RegistrationSectionDefinitions: List[RegistrationSectionDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_registration_type_definitions' function.
class DescribeRegistrationinitionsResult(BaseValidatorModel):
    RegistrationTypeDefinitions: List[Registrationinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_configuration_sets' function.
class DescribeConfigurationSetsResult(BaseValidatorModel):
    ConfigurationSets: List[ConfigurationSetInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_registration_field_definitions' function.
class DescribeRegistrationFieldDefinitionsResult(BaseValidatorModel):
    RegistrationType: str
    RegistrationFieldDefinitions: List[RegistrationFieldDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None