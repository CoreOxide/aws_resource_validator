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
from aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_constants import *

class AccountAttributeTypeDef(BaseModel):
    Name: AccountAttributeNameType
    Value: str

class AccountLimitTypeDef(BaseModel):
    Name: AccountLimitNameType
    Used: int
    Max: int

class AssociateOriginationIdentityRequestRequestTypeDef(BaseModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociateProtectConfigurationRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str

class CloudWatchLogsDestinationTypeDef(BaseModel):
    IamRoleArn: str
    LogGroupArn: str

class ConfigurationSetFilterTypeDef(BaseModel):
    Name: ConfigurationSetFilterNameType
    Values: Sequence[str]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class KinesisFirehoseDestinationTypeDef(BaseModel):
    IamRoleArn: str
    DeliveryStreamArn: str

class SnsDestinationTypeDef(BaseModel):
    TopicArn: str

class CreateRegistrationAssociationRequestRequestTypeDef(BaseModel):
    RegistrationId: str
    ResourceId: str

class CreateRegistrationVersionRequestRequestTypeDef(BaseModel):
    RegistrationId: str

class RegistrationVersionStatusHistoryTypeDef(BaseModel):
    DraftTimestamp: datetime
    SubmittedTimestamp: Optional[datetime] = None
    ReviewingTimestamp: Optional[datetime] = None
    ApprovedTimestamp: Optional[datetime] = None
    DiscardedTimestamp: Optional[datetime] = None
    DeniedTimestamp: Optional[datetime] = None
    RevokedTimestamp: Optional[datetime] = None
    ArchivedTimestamp: Optional[datetime] = None

class DeleteConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class DeleteDefaultMessageTypeRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class DeleteDefaultSenderIdRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str

class DeleteEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteKeywordRequestRequestTypeDef(BaseModel):
    OriginationIdentity: str
    Keyword: str

class DeleteOptOutListRequestRequestTypeDef(BaseModel):
    OptOutListName: str

class DeleteOptedOutNumberRequestRequestTypeDef(BaseModel):
    OptOutListName: str
    OptedOutNumber: str

class DeletePoolRequestRequestTypeDef(BaseModel):
    PoolId: str

class DeleteProtectConfigurationRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str

class DeleteRegistrationAttachmentRequestRequestTypeDef(BaseModel):
    RegistrationAttachmentId: str

class DeleteRegistrationFieldValueRequestRequestTypeDef(BaseModel):
    RegistrationId: str
    FieldPath: str

class DeleteRegistrationRequestRequestTypeDef(BaseModel):
    RegistrationId: str

class DeleteVerifiedDestinationNumberRequestRequestTypeDef(BaseModel):
    VerifiedDestinationNumberId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccountAttributesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeAccountLimitsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class KeywordFilterTypeDef(BaseModel):
    Name: Literal["keyword-action"]
    Values: Sequence[str]

class KeywordInformationTypeDef(BaseModel):
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType

class DescribeOptOutListsRequestRequestTypeDef(BaseModel):
    OptOutListNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OptOutListInformationTypeDef(BaseModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime

class OptedOutFilterTypeDef(BaseModel):
    Name: Literal["end-user-opted-out"]
    Values: Sequence[str]

class OptedOutNumberInformationTypeDef(BaseModel):
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool

class PhoneNumberFilterTypeDef(BaseModel):
    Name: PhoneNumberFilterNameType
    Values: Sequence[str]

class PhoneNumberInformationTypeDef(BaseModel):
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

class PoolFilterTypeDef(BaseModel):
    Name: PoolFilterNameType
    Values: Sequence[str]

class PoolInformationTypeDef(BaseModel):
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

class ProtectConfigurationFilterTypeDef(BaseModel):
    Name: ProtectConfigurationFilterNameType
    Values: Sequence[str]

class ProtectConfigurationInformationTypeDef(BaseModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool

class RegistrationAttachmentFilterTypeDef(BaseModel):
    Name: Literal["attachment-status"]
    Values: Sequence[str]

class RegistrationAttachmentsInformationTypeDef(BaseModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    CreatedTimestamp: datetime
    AttachmentUploadErrorReason: Optional[Literal["INTERNAL_ERROR"]] = None

class DescribeRegistrationFieldDefinitionsRequestRequestTypeDef(BaseModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeRegistrationFieldValuesRequestRequestTypeDef(BaseModel):
    RegistrationId: str
    VersionNumber: Optional[int] = None
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RegistrationFieldValueInformationTypeDef(BaseModel):
    FieldPath: str
    SelectChoices: Optional[List[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None
    DeniedReason: Optional[str] = None

class DescribeRegistrationSectionDefinitionsRequestRequestTypeDef(BaseModel):
    RegistrationType: str
    SectionPaths: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RegistrationTypeFilterTypeDef(BaseModel):
    Name: RegistrationTypeFilterNameType
    Values: Sequence[str]

class RegistrationVersionFilterTypeDef(BaseModel):
    Name: Literal["registration-version-status"]
    Values: Sequence[str]

class RegistrationFilterTypeDef(BaseModel):
    Name: RegistrationFilterNameType
    Values: Sequence[str]

class RegistrationInformationTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    CreatedTimestamp: datetime
    ApprovedVersionNumber: Optional[int] = None
    LatestDeniedVersionNumber: Optional[int] = None
    AdditionalAttributes: Optional[Dict[str, str]] = None

class SenderIdAndCountryTypeDef(BaseModel):
    SenderId: str
    IsoCountryCode: str

class SenderIdFilterTypeDef(BaseModel):
    Name: SenderIdFilterNameType
    Values: Sequence[str]

class SenderIdInformationTypeDef(BaseModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: Optional[str] = None

class DescribeSpendLimitsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SpendLimitTypeDef(BaseModel):
    Name: SpendLimitNameType
    EnforcedLimit: int
    MaxLimit: int
    Overridden: bool

class VerifiedDestinationNumberFilterTypeDef(BaseModel):
    Name: Literal["status"]
    Values: Sequence[str]

class VerifiedDestinationNumberInformationTypeDef(BaseModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime

class DisassociateOriginationIdentityRequestRequestTypeDef(BaseModel):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: Optional[str] = None

class DisassociateProtectConfigurationRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str
    ConfigurationSetName: str

class DiscardRegistrationVersionRequestRequestTypeDef(BaseModel):
    RegistrationId: str

class GetProtectConfigurationCountryRuleSetRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType

class ProtectConfigurationCountryRuleSetInformationTypeDef(BaseModel):
    ProtectStatus: ProtectStatusType

class PoolOriginationIdentitiesFilterTypeDef(BaseModel):
    Name: PoolOriginationIdentitiesFilterNameType
    Values: Sequence[str]

class OriginationIdentityMetadataTypeDef(BaseModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    NumberCapabilities: List[NumberCapabilityType]
    PhoneNumber: Optional[str] = None

class RegistrationAssociationFilterTypeDef(BaseModel):
    Name: RegistrationAssociationFilterNameType
    Values: Sequence[str]

class RegistrationAssociationMetadataTypeDef(BaseModel):
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: Optional[str] = None
    PhoneNumber: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PutKeywordRequestRequestTypeDef(BaseModel):
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: Optional[KeywordActionType] = None

class PutOptedOutNumberRequestRequestTypeDef(BaseModel):
    OptOutListName: str
    OptedOutNumber: str

class PutRegistrationFieldValueRequestRequestTypeDef(BaseModel):
    RegistrationId: str
    FieldPath: str
    SelectChoices: Optional[Sequence[str]] = None
    TextValue: Optional[str] = None
    RegistrationAttachmentId: Optional[str] = None

class RegistrationDeniedReasonInformationTypeDef(BaseModel):
    Reason: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None

class SelectValidationTypeDef(BaseModel):
    MinChoices: int
    MaxChoices: int
    Options: List[str]

class TextValidationTypeDef(BaseModel):
    MinLength: int
    MaxLength: int
    Pattern: str

class SelectOptionDescriptionTypeDef(BaseModel):
    Option: str
    Title: Optional[str] = None
    Description: Optional[str] = None

class RegistrationSectionDisplayHintsTypeDef(BaseModel):
    Title: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None

class RegistrationTypeDisplayHintsTypeDef(BaseModel):
    Title: str
    ShortDescription: Optional[str] = None
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None

class SupportedAssociationTypeDef(BaseModel):
    ResourceType: str
    AssociationBehavior: RegistrationAssociationBehaviorType
    DisassociationBehavior: RegistrationDisassociationBehaviorType
    IsoCountryCode: Optional[str] = None

class ReleasePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class ReleaseSenderIdRequestRequestTypeDef(BaseModel):
    SenderId: str
    IsoCountryCode: str

class SendDestinationNumberVerificationCodeRequestRequestTypeDef(BaseModel):
    VerifiedDestinationNumberId: str
    VerificationChannel: VerificationChannelType
    LanguageCode: Optional[LanguageCodeType] = None
    OriginationIdentity: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    Context: Optional[Mapping[str, str]] = None
    DestinationCountryParameters: Optional[       Mapping[DestinationCountryParameterKeyType, str] = None

class SendMediaMessageRequestRequestTypeDef(BaseModel):
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

class SendTextMessageRequestRequestTypeDef(BaseModel):
    DestinationPhoneNumber: str
    OriginationIdentity: Optional[str] = None
    MessageBody: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    Keyword: Optional[str] = None
    ConfigurationSetName: Optional[str] = None
    MaxPrice: Optional[str] = None
    TimeToLive: Optional[int] = None
    Context: Optional[Mapping[str, str]] = None
    DestinationCountryParameters: Optional[       Mapping[DestinationCountryParameterKeyType, str] = None
    DryRun: Optional[bool] = None
    ProtectConfigurationId: Optional[str] = None

class SendVoiceMessageRequestRequestTypeDef(BaseModel):
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

class SetAccountDefaultProtectConfigurationRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str

class SetDefaultMessageTypeRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    MessageType: MessageTypeType

class SetDefaultSenderIdRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    SenderId: str

class SetMediaMessageSpendLimitOverrideRequestRequestTypeDef(BaseModel):
    MonthlyLimit: int

class SetTextMessageSpendLimitOverrideRequestRequestTypeDef(BaseModel):
    MonthlyLimit: int

class SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef(BaseModel):
    MonthlyLimit: int

class SubmitRegistrationVersionRequestRequestTypeDef(BaseModel):
    RegistrationId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdatePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class UpdatePoolRequestRequestTypeDef(BaseModel):
    PoolId: str
    TwoWayEnabled: Optional[bool] = None
    TwoWayChannelArn: Optional[str] = None
    TwoWayChannelRole: Optional[str] = None
    SelfManagedOptOutsEnabled: Optional[bool] = None
    OptOutListName: Optional[str] = None
    SharedRoutesEnabled: Optional[bool] = None
    DeletionProtectionEnabled: Optional[bool] = None

class UpdateProtectConfigurationRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str
    DeletionProtectionEnabled: Optional[bool] = None

class UpdateSenderIdRequestRequestTypeDef(BaseModel):
    SenderId: str
    IsoCountryCode: str
    DeletionProtectionEnabled: Optional[bool] = None

class VerifyDestinationNumberRequestRequestTypeDef(BaseModel):
    VerifiedDestinationNumberId: str
    VerificationCode: str

class AssociateOriginationIdentityResultTypeDef(BaseModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateProtectConfigurationResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistrationAssociationResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: str
    PhoneNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountDefaultProtectConfigurationResultTypeDef(BaseModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDefaultMessageTypeResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDefaultSenderIdResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeywordResultTypeDef(BaseModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMediaMessageSpendLimitOverrideResultTypeDef(BaseModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOptOutListResultTypeDef(BaseModel):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOptedOutNumberResultTypeDef(BaseModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePoolResultTypeDef(BaseModel):
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

class DeleteProtectConfigurationResultTypeDef(BaseModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistrationAttachmentResultTypeDef(BaseModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    AttachmentUploadErrorReason: Literal["INTERNAL_ERROR"]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistrationFieldValueResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistrationResultTypeDef(BaseModel):
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

class DeleteTextMessageSpendLimitOverrideResultTypeDef(BaseModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedDestinationNumberResultTypeDef(BaseModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVoiceMessageSpendLimitOverrideResultTypeDef(BaseModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResultTypeDef(BaseModel):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAccountLimitsResultTypeDef(BaseModel):
    AccountLimits: List[AccountLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateOriginationIdentityResultTypeDef(BaseModel):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateProtectConfigurationResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutKeywordResultTypeDef(BaseModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadataTypeDef

class PutOptedOutNumberResultTypeDef(BaseModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistrationFieldValueResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReleasePhoneNumberResultTypeDef(BaseModel):
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

class ReleaseSenderIdResultTypeDef(BaseModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendDestinationNumberVerificationCodeResultTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendMediaMessageResultTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendTextMessageResultTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendVoiceMessageResultTypeDef(BaseModel):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetAccountDefaultProtectConfigurationResultTypeDef(BaseModel):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultMessageTypeResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultSenderIdResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetMediaMessageSpendLimitOverrideResultTypeDef(BaseModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class SetTextMessageSpendLimitOverrideResultTypeDef(BaseModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class SetVoiceMessageSpendLimitOverrideResultTypeDef(BaseModel):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResultTypeDef(BaseModel):
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

class UpdatePoolResultTypeDef(BaseModel):
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

class UpdateProtectConfigurationResultTypeDef(BaseModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSenderIdResultTypeDef(BaseModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDestinationNumberResultTypeDef(BaseModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationSetsRequestRequestTypeDef(BaseModel):
    ConfigurationSetNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ConfigurationSetFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class CreateConfigurationSetRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateConfigurationSetResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOptOutListRequestRequestTypeDef(BaseModel):
    OptOutListName: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateOptOutListResultTypeDef(BaseModel):
    OptOutListArn: str
    OptOutListName: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePoolRequestRequestTypeDef(BaseModel):
    OriginationIdentity: str
    IsoCountryCode: str
    MessageType: MessageTypeType
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreatePoolResultTypeDef(BaseModel):
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

class CreateProtectConfigurationRequestRequestTypeDef(BaseModel):
    ClientToken: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateProtectConfigurationResultTypeDef(BaseModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistrationAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentBody: Optional[BlobTypeDef] = None
    AttachmentUrl: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateRegistrationAttachmentResultTypeDef(BaseModel):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistrationRequestRequestTypeDef(BaseModel):
    RegistrationType: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateRegistrationResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVerifiedDestinationNumberRequestRequestTypeDef(BaseModel):
    DestinationPhoneNumber: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateVerifiedDestinationNumberResultTypeDef(BaseModel):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RequestPhoneNumberRequestRequestTypeDef(BaseModel):
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

class RequestPhoneNumberResultTypeDef(BaseModel):
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

class RequestSenderIdRequestRequestTypeDef(BaseModel):
    SenderId: str
    IsoCountryCode: str
    MessageTypes: Optional[Sequence[MessageTypeType]] = None
    DeletionProtectionEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class RequestSenderIdResultTypeDef(BaseModel):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    MatchingEventTypes: Sequence[EventTypeType]
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None
    ClientToken: Optional[str] = None

class EventDestinationTypeDef(BaseModel):
    EventDestinationName: str
    Enabled: bool
    MatchingEventTypes: List[EventTypeType]
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None

class UpdateEventDestinationRequestRequestTypeDef(BaseModel):
    ConfigurationSetName: str
    EventDestinationName: str
    Enabled: Optional[bool] = None
    MatchingEventTypes: Optional[Sequence[EventTypeType]] = None
    CloudWatchLogsDestination: Optional[CloudWatchLogsDestinationTypeDef] = None
    KinesisFirehoseDestination: Optional[KinesisFirehoseDestinationTypeDef] = None
    SnsDestination: Optional[SnsDestinationTypeDef] = None

class CreateRegistrationVersionResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DiscardRegistrationVersionResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitRegistrationVersionResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesRequestDescribeAccountAttributesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAccountLimitsRequestDescribeAccountLimitsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigurationSetsRequestDescribeConfigurationSetsPaginateTypeDef(BaseModel):
    ConfigurationSetNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ConfigurationSetFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOptOutListsRequestDescribeOptOutListsPaginateTypeDef(BaseModel):
    OptOutListNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationFieldDefinitionsRequestDescribeRegistrationFieldDefinitionsPaginateTypeDef(BaseModel):
    RegistrationType: str
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationFieldValuesRequestDescribeRegistrationFieldValuesPaginateTypeDef(BaseModel):
    RegistrationId: str
    VersionNumber: Optional[int] = None
    SectionPath: Optional[str] = None
    FieldPaths: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationSectionDefinitionsRequestDescribeRegistrationSectionDefinitionsPaginateTypeDef(BaseModel):
    RegistrationType: str
    SectionPaths: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpendLimitsRequestDescribeSpendLimitsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeKeywordsRequestDescribeKeywordsPaginateTypeDef(BaseModel):
    OriginationIdentity: str
    Keywords: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[KeywordFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeKeywordsRequestRequestTypeDef(BaseModel):
    OriginationIdentity: str
    Keywords: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[KeywordFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeKeywordsResultTypeDef(BaseModel):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keywords: List[KeywordInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOptOutListsResultTypeDef(BaseModel):
    OptOutLists: List[OptOutListInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOptedOutNumbersRequestDescribeOptedOutNumbersPaginateTypeDef(BaseModel):
    OptOutListName: str
    OptedOutNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[OptedOutFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOptedOutNumbersRequestRequestTypeDef(BaseModel):
    OptOutListName: str
    OptedOutNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[OptedOutFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeOptedOutNumbersResultTypeDef(BaseModel):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumbers: List[OptedOutNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePhoneNumbersRequestDescribePhoneNumbersPaginateTypeDef(BaseModel):
    PhoneNumberIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PhoneNumberFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePhoneNumbersRequestRequestTypeDef(BaseModel):
    PhoneNumberIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PhoneNumberFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribePhoneNumbersResultTypeDef(BaseModel):
    PhoneNumbers: List[PhoneNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePoolsRequestDescribePoolsPaginateTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PoolFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePoolsRequestRequestTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[PoolFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribePoolsResultTypeDef(BaseModel):
    Pools: List[PoolInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeProtectConfigurationsRequestDescribeProtectConfigurationsPaginateTypeDef(BaseModel):
    ProtectConfigurationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ProtectConfigurationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeProtectConfigurationsRequestRequestTypeDef(BaseModel):
    ProtectConfigurationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[ProtectConfigurationFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeProtectConfigurationsResultTypeDef(BaseModel):
    ProtectConfigurations: List[ProtectConfigurationInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegistrationAttachmentsRequestDescribeRegistrationAttachmentsPaginateTypeDef(BaseModel):
    RegistrationAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationAttachmentFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationAttachmentsRequestRequestTypeDef(BaseModel):
    RegistrationAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationAttachmentFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeRegistrationAttachmentsResultTypeDef(BaseModel):
    RegistrationAttachments: List[RegistrationAttachmentsInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegistrationFieldValuesResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationFieldValues: List[RegistrationFieldValueInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegistrationTypeDefinitionsRequestDescribeRegistrationTypeDefinitionsPaginateTypeDef(BaseModel):
    RegistrationTypes: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationTypeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationTypeDefinitionsRequestRequestTypeDef(BaseModel):
    RegistrationTypes: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationTypeFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeRegistrationVersionsRequestDescribeRegistrationVersionsPaginateTypeDef(BaseModel):
    RegistrationId: str
    VersionNumbers: Optional[Sequence[int]] = None
    Filters: Optional[Sequence[RegistrationVersionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationVersionsRequestRequestTypeDef(BaseModel):
    RegistrationId: str
    VersionNumbers: Optional[Sequence[int]] = None
    Filters: Optional[Sequence[RegistrationVersionFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeRegistrationsRequestDescribeRegistrationsPaginateTypeDef(BaseModel):
    RegistrationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistrationsRequestRequestTypeDef(BaseModel):
    RegistrationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[RegistrationFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeRegistrationsResultTypeDef(BaseModel):
    Registrations: List[RegistrationInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSenderIdsRequestDescribeSenderIdsPaginateTypeDef(BaseModel):
    SenderIds: Optional[Sequence[SenderIdAndCountryTypeDef]] = None
    Filters: Optional[Sequence[SenderIdFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSenderIdsRequestRequestTypeDef(BaseModel):
    SenderIds: Optional[Sequence[SenderIdAndCountryTypeDef]] = None
    Filters: Optional[Sequence[SenderIdFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSenderIdsResultTypeDef(BaseModel):
    SenderIds: List[SenderIdInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpendLimitsResultTypeDef(BaseModel):
    SpendLimits: List[SpendLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVerifiedDestinationNumbersRequestDescribeVerifiedDestinationNumbersPaginateTypeDef(BaseModel):
    VerifiedDestinationNumberIds: Optional[Sequence[str]] = None
    DestinationPhoneNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VerifiedDestinationNumberFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedDestinationNumbersRequestRequestTypeDef(BaseModel):
    VerifiedDestinationNumberIds: Optional[Sequence[str]] = None
    DestinationPhoneNumbers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[VerifiedDestinationNumberFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVerifiedDestinationNumbersResultTypeDef(BaseModel):
    VerifiedDestinationNumbers: List[VerifiedDestinationNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetProtectConfigurationCountryRuleSetResultTypeDef(BaseModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef(BaseModel):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSetUpdates: Mapping[str, ProtectConfigurationCountryRuleSetInformationTypeDef]

class UpdateProtectConfigurationCountryRuleSetResultTypeDef(BaseModel):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoolOriginationIdentitiesRequestListPoolOriginationIdentitiesPaginateTypeDef(BaseModel):
    PoolId: str
    Filters: Optional[Sequence[PoolOriginationIdentitiesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoolOriginationIdentitiesRequestRequestTypeDef(BaseModel):
    PoolId: str
    Filters: Optional[Sequence[PoolOriginationIdentitiesFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPoolOriginationIdentitiesResultTypeDef(BaseModel):
    PoolArn: str
    PoolId: str
    OriginationIdentities: List[OriginationIdentityMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRegistrationAssociationsRequestListRegistrationAssociationsPaginateTypeDef(BaseModel):
    RegistrationId: str
    Filters: Optional[Sequence[RegistrationAssociationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistrationAssociationsRequestRequestTypeDef(BaseModel):
    RegistrationId: str
    Filters: Optional[Sequence[RegistrationAssociationFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRegistrationAssociationsResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationAssociations: List[RegistrationAssociationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegistrationVersionInformationTypeDef(BaseModel):
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    DeniedReasons: Optional[List[RegistrationDeniedReasonInformationTypeDef]] = None

class RegistrationFieldDisplayHintsTypeDef(BaseModel):
    Title: str
    ShortDescription: str
    LongDescription: Optional[str] = None
    DocumentationTitle: Optional[str] = None
    DocumentationLink: Optional[str] = None
    SelectOptionDescriptions: Optional[List[SelectOptionDescriptionTypeDef]] = None
    TextValidationDescription: Optional[str] = None
    ExampleTextValue: Optional[str] = None

class RegistrationSectionDefinitionTypeDef(BaseModel):
    SectionPath: str
    DisplayHints: RegistrationSectionDisplayHintsTypeDef

class RegistrationTypeDefinitionTypeDef(BaseModel):
    RegistrationType: str
    DisplayHints: RegistrationTypeDisplayHintsTypeDef
    SupportedAssociations: Optional[List[SupportedAssociationTypeDef]] = None

class ConfigurationSetInformationTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestinationTypeDef]
    CreatedTimestamp: datetime
    DefaultMessageType: Optional[MessageTypeType] = None
    DefaultSenderId: Optional[str] = None
    ProtectConfigurationId: Optional[str] = None

class CreateEventDestinationResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConfigurationSetResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestinationTypeDef]
    DefaultMessageType: MessageTypeType
    DefaultSenderId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventDestinationResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventDestinationResultTypeDef(BaseModel):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegistrationVersionsResultTypeDef(BaseModel):
    RegistrationArn: str
    RegistrationId: str
    RegistrationVersions: List[RegistrationVersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegistrationFieldDefinitionTypeDef(BaseModel):
    SectionPath: str
    FieldPath: str
    FieldType: FieldTypeType
    FieldRequirement: FieldRequirementType
    DisplayHints: RegistrationFieldDisplayHintsTypeDef
    SelectValidation: Optional[SelectValidationTypeDef] = None
    TextValidation: Optional[TextValidationTypeDef] = None

class DescribeRegistrationSectionDefinitionsResultTypeDef(BaseModel):
    RegistrationType: str
    RegistrationSectionDefinitions: List[RegistrationSectionDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegistrationTypeDefinitionsResultTypeDef(BaseModel):
    RegistrationTypeDefinitions: List[RegistrationTypeDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConfigurationSetsResultTypeDef(BaseModel):
    ConfigurationSets: List[ConfigurationSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegistrationFieldDefinitionsResultTypeDef(BaseModel):
    RegistrationType: str
    RegistrationFieldDefinitions: List[RegistrationFieldDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

