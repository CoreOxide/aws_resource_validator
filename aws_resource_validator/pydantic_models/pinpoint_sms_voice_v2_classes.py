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
from aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_constants import *

class AccountAttributeTypeDef(BaseValidatorModel):
    Name: AccountAttributeNameType
    Value: str


class AccountLimitTypeDef(BaseValidatorModel):
    Name: AccountLimitNameType
    Used: int
    Max: int


class AssociateOriginationIdentityRequestTypeDef(BaseValidatorModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateProtectConfigurationRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str


class CloudWatchLogsDestinationTypeDef(BaseValidatorModel):
    IamRoleArn: str
    LogGroupArn: str


class ConfigurationSetFilterTypeDef(BaseValidatorModel):
    Name: ConfigurationSetFilterNameType
    Values: Sequence[str]


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class KinesisFirehoseDestinationTypeDef(BaseValidatorModel):
    IamRoleArn: str
    DeliveryStreamArn: str


class SnsDestinationTypeDef(BaseValidatorModel):
    TopicArn: str


class CreateRegistrationAssociationRequestTypeDef(BaseValidatorModel):
    RegistrationId: str
    ResourceId: str


class CreateRegistrationVersionRequestTypeDef(BaseValidatorModel):
    RegistrationId: str


class RegistrationVersionStatusHistoryTypeDef(BaseValidatorModel):
    DraftTimestamp: datetime
    SubmittedTimestamp: Optional[datetime] = None
    ReviewingTimestamp: Optional[datetime] = None
    RequiresAuthenticationTimestamp: Optional[datetime] = None
    ApprovedTimestamp: Optional[datetime] = None
    DiscardedTimestamp: Optional[datetime] = None
    DeniedTimestamp: Optional[datetime] = None
    RevokedTimestamp: Optional[datetime] = None
    ArchivedTimestamp: Optional[datetime] = None


class DeleteConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteDefaultMessageTypeRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteDefaultSenderIdRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str


class DeleteEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str


class DeleteKeywordRequestTypeDef(BaseValidatorModel):
    OriginationIdentity: str
    Keyword: str


class DeleteOptOutListRequestTypeDef(BaseValidatorModel):
    OptOutListName: str


class DeleteOptedOutNumberRequestTypeDef(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumber: str


class DeletePoolRequestTypeDef(BaseValidatorModel):
    PoolId: str


class DeleteProtectConfigurationRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str


class DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str


class DeleteRegistrationAttachmentRequestTypeDef(BaseValidatorModel):
    RegistrationAttachmentId: str


class DeleteRegistrationFieldValueRequestTypeDef(BaseValidatorModel):
    RegistrationId: str
    FieldPath: str


class DeleteRegistrationRequestTypeDef(BaseValidatorModel):
    RegistrationId: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeleteVerifiedDestinationNumberRequestTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAccountAttributesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeAccountLimitsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class KeywordFilterTypeDef(BaseValidatorModel):
    Name: Literal["keyword-action"]
    Values: Sequence[str]


class KeywordInformationTypeDef(BaseValidatorModel):
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType


class DescribeOptOutListsRequestTypeDef(BaseValidatorModel):
    OptOutListNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class OptOutListInformationTypeDef(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime


class OptedOutFilterTypeDef(BaseValidatorModel):
    Name: Literal["end-user-opted-out"]
    Values: Sequence[str]


class OptedOutNumberInformationTypeDef(BaseValidatorModel):
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool


class PhoneNumberFilterTypeDef(BaseValidatorModel):
    Name: PhoneNumberFilterNameType
    Values: Sequence[str]


class PhoneNumberInformationTypeDef(BaseValidatorModel):
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


class PoolFilterTypeDef(BaseValidatorModel):
    Name: PoolFilterNameType
    Values: Sequence[str]


class PoolInformationTypeDef(BaseValidatorModel):
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


class ProtectConfigurationFilterTypeDef(BaseValidatorModel):
    Name: ProtectConfigurationFilterNameType
    Values: Sequence[str]


class ProtectConfigurationInformationTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool


class RegistrationAttachmentFilterTypeDef(BaseValidatorModel):
    Name: Literal["attachment-status"]
    Values: Sequence[str]


class RegistrationAttachmentsInformationTypeDef(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    CreatedTimestamp: datetime
    AttachmentUploadErrorReason: Optional[Literal["INTERNAL_ERROR"]] = None


class DescribeRegistrationFieldDefinitionsRequestTypeDef(BaseValidatorModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationFieldValuesRequestTypeDef(BaseValidatorModel):
    RegistrationId: str
    VersionNumber: Optional[int] = None
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RegistrationFieldValueInformationTypeDef(BaseValidatorModel):
    FieldPath: str
    SelectChoices: Optional[List[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None
    DeniedReason: Optional[str] = None


class DescribeRegistrationSectionDefinitionsRequestTypeDef(BaseValidatorModel):
    RegistrationType: str
    SectionPaths: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RegistrationTypeFilterTypeDef(BaseValidatorModel):
    Name: RegistrationTypeFilterNameType
    Values: Sequence[str]


class RegistrationVersionFilterTypeDef(BaseValidatorModel):
    Name: Literal["registration-version-status"]
    Values: Sequence[str]


class RegistrationFilterTypeDef(BaseValidatorModel):
    Name: RegistrationFilterNameType
    Values: Sequence[str]


class RegistrationInformationTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    CreatedTimestamp: datetime
    ApprovedVersionNumber: Optional[int] = None
    LatestDeniedVersionNumber: Optional[int] = None
    AdditionalAttributes: Optional[Dict[str, str]] = None


class SenderIdAndCountryTypeDef(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str


class SenderIdFilterTypeDef(BaseValidatorModel):
    Name: SenderIdFilterNameType
    Values: Sequence[str]


class SenderIdInformationTypeDef(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: Optional[str] = None


class DescribeSpendLimitsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SpendLimitTypeDef(BaseValidatorModel):
    Name: SpendLimitNameType
    EnforcedLimit: int
    MaxLimit: int
    Overridden: bool


class VerifiedDestinationNumberFilterTypeDef(BaseValidatorModel):
    Name: Literal["status"]
    Values: Sequence[str]


class VerifiedDestinationNumberInformationTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime


class DisassociateOriginationIdentityRequestTypeDef(BaseValidatorModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None


class DisassociateProtectConfigurationRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str


class DiscardRegistrationVersionRequestTypeDef(BaseValidatorModel):
    RegistrationId: str


class GetProtectConfigurationCountryRuleSetRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType


class ProtectConfigurationCountryRuleSetInformationTypeDef(BaseValidatorModel):
    ProtectStatus: ProtectStatusType


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PoolOriginationIdentitiesFilterTypeDef(BaseValidatorModel):
    Name: PoolOriginationIdentitiesFilterNameType
    Values: Sequence[str]


class OriginationIdentityMetadataTypeDef(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    NumberCapabilities: List[NumberCapabilityType]
    PhoneNumber: Optional[str] = None


class ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef(BaseValidatorModel):
    Name: ProtectConfigurationRuleSetNumberOverrideFilterNameType
    Values: Sequence[str]


class ProtectConfigurationRuleSetNumberOverrideTypeDef(BaseValidatorModel):
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: Optional[str] = None
    ExpirationTimestamp: Optional[datetime] = None


class RegistrationAssociationFilterTypeDef(BaseValidatorModel):
    Name: RegistrationAssociationFilterNameType
    Values: Sequence[str]


class RegistrationAssociationMetadataTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: Optional[str] = None
    PhoneNumber: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PutKeywordRequestTypeDef(BaseValidatorModel):
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: Optional[KeywordActionType] = None


class PutMessageFeedbackRequestTypeDef(BaseValidatorModel):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType


class PutOptedOutNumberRequestTypeDef(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumber: str


class PutRegistrationFieldValueRequestTypeDef(BaseValidatorModel):
    RegistrationId: str
    FieldPath: str
    SelectChoices: Optional[Sequence[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RegistrationDeniedReasonInformationTypeDef(BaseValidatorModel):
    Reason: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None


class SelectValidationTypeDef(BaseValidatorModel):
    MinChoices: int
    MaxChoices: int
    Options: List[str]


class SelectOptionDescriptionTypeDef(BaseValidatorModel):
    Option: str
    Title: Optional[str] = None
    Description: Optional[str] = None


class RegistrationSectionDisplayHintsTypeDef(BaseValidatorModel):
    Title: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None


class RegistrationTypeDisplayHintsTypeDef(BaseValidatorModel):
    Title: str
    ShortDescription: Optional[str] = None
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None


class SupportedAssociationTypeDef(BaseValidatorModel):
    ResourceType: str
    AssociationBehavior: RegistrationAssociationBehaviorType
    DisassociationBehavior: RegistrationDisassociationBehaviorType
    IsoCountryCode: Optional[str] = None


class ReleasePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str


class ReleaseSenderIdRequestTypeDef(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str


class SendDestinationNumberVerificationCodeRequestTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberId: str
    VerificationChannel: VerificationChannelType
    LanguageCode: Optional[LanguageCodeType] = None
    OriginationIdentity: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Context: Optional[Mapping[str, str]] = None
    DestinationCountryParameters: Optional[Mapping[DestinationCountryParameterKeyType, str]] = None


class SendMediaMessageRequestTypeDef(BaseValidatorModel):
    DestinationPhoneNumber: str
    OriginationIdentity: str
    MessageBody: Optional[str] = None
    MediaUrls: Optional[Sequence[str]] = None
    ConfigurationSetName: Optional[str] = None
    MaxPrice: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Mapping[str, str]] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None
    MessageFeedbackEnabled: Optional[bool] = None


class SendTextMessageRequestTypeDef(BaseValidatorModel):
    DestinationPhoneNumber: str
    OriginationIdentity: Optional[str] = None
    MessageBody: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    Keyword: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    MaxPrice: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Mapping[str, str]] = None
    DestinationCountryParameters: Optional[Mapping[DestinationCountryParameterKeyType, str]] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None
    MessageFeedbackEnabled: Optional[bool] = None


class SendVoiceMessageRequestTypeDef(BaseValidatorModel):
    DestinationPhoneNumber: str
    OriginationIdentity: str
    MessageBody: Optional[str] = None
    MessageBodyTextType: Optional[VoiceMessageBodyTextTypeType] = None
    VoiceId: Optional[VoiceIdType] = None
    ConfigurationSetName: Optional[str] = None
    MaxPricePerMinute: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Mapping[str, str]] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None
    MessageFeedbackEnabled: Optional[bool] = None


class SetAccountDefaultProtectConfigurationRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str


class SetDefaultMessageFeedbackEnabledRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool


class SetDefaultMessageTypeRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    MessageType: MessageTypeType


class SetDefaultSenderIdRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    SenderId: str


class SetMediaMessageSpendLimitOverrideRequestTypeDef(BaseValidatorModel):
    MonthlyLimit: int


class SetTextMessageSpendLimitOverrideRequestTypeDef(BaseValidatorModel):
    MonthlyLimit: int


class SetVoiceMessageSpendLimitOverrideRequestTypeDef(BaseValidatorModel):
    MonthlyLimit: int


class SubmitRegistrationVersionRequestTypeDef(BaseValidatorModel):
    RegistrationId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdatePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None


class UpdatePoolRequestTypeDef(BaseValidatorModel):
    PoolId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    SharedRoutesEnabled: Optional[bool] = None
    DeletionProtectionEnabled: Optional[bool] = None


class UpdateProtectConfigurationRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    DeletionProtectionEnabled: Optional[bool] = None


class UpdateSenderIdRequestTypeDef(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str
    DeletionProtectionEnabled: Optional[bool] = None


class VerifyDestinationNumberRequestTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberId: str
    VerificationCode: str


class AssociateOriginationIdentityResultTypeDef(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateProtectConfigurationResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRegistrationAssociationResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: str
    PhoneNumber: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAccountDefaultProtectConfigurationResultTypeDef(BaseValidatorModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDefaultMessageTypeResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDefaultSenderIdResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteKeywordResultTypeDef(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMediaMessageSpendLimitOverrideResultTypeDef(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteOptOutListResultTypeDef(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteOptedOutNumberResultTypeDef(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePoolResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProtectConfigurationResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRegistrationAttachmentResultTypeDef(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    AttachmentUploadErrorReason: Literal["INTERNAL_ERROR"]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRegistrationFieldValueResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRegistrationResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    ApprovedVersionNumber: int
    LatestDeniedVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTextMessageSpendLimitOverrideResultTypeDef(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVerifiedDestinationNumberResultTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVoiceMessageSpendLimitOverrideResultTypeDef(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountAttributesResultTypeDef(BaseValidatorModel):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeAccountLimitsResultTypeDef(BaseValidatorModel):
    AccountLimits: List[AccountLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DisassociateOriginationIdentityResultTypeDef(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateProtectConfigurationResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PutKeywordResultTypeDef(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadataTypeDef


class PutMessageFeedbackResultTypeDef(BaseValidatorModel):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class PutOptedOutNumberResultTypeDef(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef


class PutProtectConfigurationRuleSetNumberOverrideResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PutRegistrationFieldValueResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ReleasePhoneNumberResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class ReleaseSenderIdResultTypeDef(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendDestinationNumberVerificationCodeResultTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendMediaMessageResultTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendTextMessageResultTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendVoiceMessageResultTypeDef(BaseValidatorModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetAccountDefaultProtectConfigurationResultTypeDef(BaseValidatorModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetDefaultMessageFeedbackEnabledResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class SetDefaultMessageTypeResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class SetDefaultSenderIdResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetMediaMessageSpendLimitOverrideResultTypeDef(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef


class SetTextMessageSpendLimitOverrideResultTypeDef(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef


class SetVoiceMessageSpendLimitOverrideResultTypeDef(BaseValidatorModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePhoneNumberResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePoolResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProtectConfigurationResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSenderIdResultTypeDef(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class VerifyDestinationNumberResultTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConfigurationSetsRequestTypeDef(BaseValidatorModel):
    ConfigurationSetNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ConfigurationSetFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CreateConfigurationSetRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class CreateConfigurationSetResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOptOutListRequestTypeDef(BaseValidatorModel):
    OptOutListName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class CreateOptOutListResultTypeDef(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePoolRequestTypeDef(BaseValidatorModel):
    OriginationIdentity: str
    IsoCountryCode: str
    MessageType: MessageTypeType
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class CreatePoolResultTypeDef(BaseValidatorModel):
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
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProtectConfigurationRequestTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateProtectConfigurationResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class CreateRegistrationAttachmentRequestTypeDef(BaseValidatorModel):
    AttachmentBody: Optional[BlobTypeDef] = None
    AttachmentUrl: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class CreateRegistrationAttachmentResultTypeDef(BaseValidatorModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRegistrationRequestTypeDef(BaseValidatorModel):
    RegistrationType: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class CreateRegistrationResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVerifiedDestinationNumberRequestTypeDef(BaseValidatorModel):
    DestinationPhoneNumber: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class CreateVerifiedDestinationNumberResultTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RequestPhoneNumberRequestTypeDef(BaseValidatorModel):
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: Sequence[NumberCapabilityType]
    NumberType: RequestableNumberTypeType
    OptOutListName: Optional[str] = None
    PoolId: Optional[str] = None
    RegistrationId: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class RequestPhoneNumberResultTypeDef(BaseValidatorModel):
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
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class RequestSenderIdRequestTypeDef(BaseValidatorModel):
    SenderId: str
    IsoCountryCode: str
    MessageTypes: Optional[Sequence[MessageTypeType]] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class RequestSenderIdResultTypeDef(BaseValidatorModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    MatchingEventTypes: Sequence[EventTypeType]
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    ClientToken: Optional[str] = None


class EventDestinationTypeDef(BaseValidatorModel):
    EventDestinationName: str
    Enabled: bool
    MatchingEventTypes: List[EventTypeType]
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None


class UpdateEventDestinationRequestTypeDef(BaseValidatorModel):
    ConfigurationSetName: str
    EventDestinationName: str
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None


class CreateRegistrationVersionResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DiscardRegistrationVersionResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SubmitRegistrationVersionResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountAttributesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAccountLimitsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConfigurationSetsRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationSetNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ConfigurationSetFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOptOutListsRequestPaginateTypeDef(BaseValidatorModel):
    OptOutListNames: Optional[Sequence[str]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationFieldValuesRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationId: str
    VersionNumber: Optional[int] = None
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationType: str
    SectionPaths: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSpendLimitsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeKeywordsRequestPaginateTypeDef(BaseValidatorModel):
    OriginationIdentity: str
    Keywords: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[KeywordFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeKeywordsRequestTypeDef(BaseValidatorModel):
    OriginationIdentity: str
    Keywords: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[KeywordFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeKeywordsResultTypeDef(BaseValidatorModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keywords: List[KeywordInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeOptOutListsResultTypeDef(BaseValidatorModel):
    OptOutLists: List[OptOutListInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeOptedOutNumbersRequestPaginateTypeDef(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[OptedOutFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOptedOutNumbersRequestTypeDef(BaseValidatorModel):
    OptOutListName: str
    OptedOutNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[OptedOutFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeOptedOutNumbersResultTypeDef(BaseValidatorModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumbers: List[OptedOutNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribePhoneNumbersRequestPaginateTypeDef(BaseValidatorModel):
    PhoneNumberIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PhoneNumberFilterTypeDef]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePhoneNumbersRequestTypeDef(BaseValidatorModel):
    PhoneNumberIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PhoneNumberFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class DescribePhoneNumbersResultTypeDef(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribePoolsRequestPaginateTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PoolFilterTypeDef]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePoolsRequestTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PoolFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class DescribePoolsResultTypeDef(BaseValidatorModel):
    Pools: List[PoolInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeProtectConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    ProtectConfigurationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ProtectConfigurationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeProtectConfigurationsRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ProtectConfigurationFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeProtectConfigurationsResultTypeDef(BaseValidatorModel):
    ProtectConfigurations: List[ProtectConfigurationInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeRegistrationAttachmentsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationAttachmentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationAttachmentsRequestTypeDef(BaseValidatorModel):
    RegistrationAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationAttachmentFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationAttachmentsResultTypeDef(BaseValidatorModel):
    RegistrationAttachments: List[RegistrationAttachmentsInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeRegistrationFieldValuesResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationFieldValues: List[RegistrationFieldValueInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationTypes: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationTypeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationTypeDefinitionsRequestTypeDef(BaseValidatorModel):
    RegistrationTypes: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationTypeFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationVersionsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationId: str
    VersionNumbers: Optional[Sequence[int]] = None
    Filters: Optional[Sequence[RegistrationVersionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationVersionsRequestTypeDef(BaseValidatorModel):
    RegistrationId: str
    VersionNumbers: Optional[Sequence[int]] = None
    Filters: Optional[Sequence[RegistrationVersionFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistrationsRequestTypeDef(BaseValidatorModel):
    RegistrationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeRegistrationsResultTypeDef(BaseValidatorModel):
    Registrations: List[RegistrationInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeSenderIdsRequestPaginateTypeDef(BaseValidatorModel):
    SenderIds: Optional[Sequence[SenderIdAndCountryTypeDef]] = None
    Filters: Optional[Sequence[SenderIdFilterTypeDef]] = None
    Owner: Optional[OwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSenderIdsRequestTypeDef(BaseValidatorModel):
    SenderIds: Optional[Sequence[SenderIdAndCountryTypeDef]] = None
    Filters: Optional[Sequence[SenderIdFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Owner: Optional[OwnerType] = None


class DescribeSenderIdsResultTypeDef(BaseValidatorModel):
    SenderIds: List[SenderIdInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeSpendLimitsResultTypeDef(BaseValidatorModel):
    SpendLimits: List[SpendLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeVerifiedDestinationNumbersRequestPaginateTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberIds: Optional[Sequence[str]] = None
    DestinationPhoneNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VerifiedDestinationNumberFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeVerifiedDestinationNumbersRequestTypeDef(BaseValidatorModel):
    VerifiedDestinationNumberIds: Optional[Sequence[str]] = None
    DestinationPhoneNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VerifiedDestinationNumberFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeVerifiedDestinationNumbersResultTypeDef(BaseValidatorModel):
    VerifiedDestinationNumbers: List[VerifiedDestinationNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetProtectConfigurationCountryRuleSetResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProtectConfigurationCountryRuleSetRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSetUpdates: Mapping[str, ProtectConfigurationCountryRuleSetInformationTypeDef]


class UpdateProtectConfigurationCountryRuleSetResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListPoolOriginationIdentitiesRequestPaginateTypeDef(BaseValidatorModel):
    PoolId: str
    Filters: Optional[Sequence[PoolOriginationIdentitiesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoolOriginationIdentitiesRequestTypeDef(BaseValidatorModel):
    PoolId: str
    Filters: Optional[Sequence[PoolOriginationIdentitiesFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoolOriginationIdentitiesResultTypeDef(BaseValidatorModel):
    PoolArn: str
    PoolId: str
    OriginationIdentities: List[OriginationIdentityMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    Filters: Optional[Sequence[ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    Filters: Optional[Sequence[ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProtectConfigurationRuleSetNumberOverridesResultTypeDef(BaseValidatorModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    RuleSetNumberOverrides: List[ProtectConfigurationRuleSetNumberOverrideTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRegistrationAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    RegistrationId: str
    Filters: Optional[Sequence[RegistrationAssociationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegistrationAssociationsRequestTypeDef(BaseValidatorModel):
    RegistrationId: str
    Filters: Optional[Sequence[RegistrationAssociationFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRegistrationAssociationsResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationAssociations: List[RegistrationAssociationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef(BaseValidatorModel):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    Action: ProtectConfigurationRuleOverrideActionType
    ClientToken: Optional[str] = None
    ExpirationTimestamp: Optional[TimestampTypeDef] = None


class RegistrationVersionInformationTypeDef(BaseValidatorModel):
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    DeniedReasons: Optional[List[RegistrationDeniedReasonInformationTypeDef]] = None


class RegistrationFieldDisplayHintsTypeDef(BaseValidatorModel):
    Title: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None
    SelectOptionDescriptions: Optional[List[SelectOptionDescriptionTypeDef]] = None
    TextValidationDescription: Optional[str] = None
    ExampleTextValue: Optional[str] = None


class RegistrationSectionDefinitionTypeDef(BaseValidatorModel):
    SectionPath: str
    DisplayHints: RegistrationSectionDisplayHintsTypeDef


class RegistrationTypeDefinitionTypeDef(BaseValidatorModel):
    RegistrationType: str
    DisplayHints: RegistrationTypeDisplayHintsTypeDef
    SupportedAssociations: Optional[List[SupportedAssociationTypeDef]] = None


class ConfigurationSetInformationTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestinationTypeDef]
    CreatedTimestamp: datetime
    DefaultMessageType: Optional[MessageTypeType] = None
    DefaultSenderId: Optional[str] = None
    DefaultMessageFeedbackEnabled: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None


class CreateEventDestinationResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteConfigurationSetResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestinationTypeDef]
    DefaultMessageType: MessageTypeType
    DefaultSenderId: str
    DefaultMessageFeedbackEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEventDestinationResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventDestinationResultTypeDef(BaseValidatorModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRegistrationVersionsResultTypeDef(BaseValidatorModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationVersions: List[RegistrationVersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TextValidationTypeDef(BaseValidatorModel):
    pass


class RegistrationFieldDefinitionTypeDef(BaseValidatorModel):
    SectionPath: str
    FieldPath: str
    FieldType: FieldTypeType
    FieldRequirement: FieldRequirementType
    DisplayHints: RegistrationFieldDisplayHintsTypeDef
    SelectValidation: Optional[SelectValidationTypeDef] = None
    TextValidation: Optional[TextValidationTypeDef] = None


class DescribeRegistrationSectionDefinitionsResultTypeDef(BaseValidatorModel):
    RegistrationType: str
    RegistrationSectionDefinitions: List[RegistrationSectionDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeRegistrationTypeDefinitionsResultTypeDef(BaseValidatorModel):
    RegistrationTypeDefinitions: List[RegistrationTypeDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeConfigurationSetsResultTypeDef(BaseValidatorModel):
    ConfigurationSets: List[ConfigurationSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeRegistrationFieldDefinitionsResultTypeDef(BaseValidatorModel):
    RegistrationType: str
    RegistrationFieldDefinitions: List[RegistrationFieldDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


