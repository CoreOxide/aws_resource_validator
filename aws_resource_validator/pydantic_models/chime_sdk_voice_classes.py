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
from aws_resource_validator.pydantic_models.chime_sdk_voice_constants import *

class AddressTypeDef(BaseValidatorModel):
    streetName: Optional[str] = None
    streetSuffix: Optional[str] = None
    postDirectional: Optional[str] = None
    preDirectional: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class PhoneNumberErrorTypeDef(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class BatchDeletePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberIds: Sequence[str]

class UpdatePhoneNumberRequestItemTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None

class CallDetailsTypeDef(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    TransactionId: Optional[str] = None
    IsCaller: Optional[bool] = None

class CandidateAddressTypeDef(BaseValidatorModel):
    streetInfo: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None

class CreatePhoneNumberOrderRequestRequestTypeDef(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]
    Name: Optional[str] = None

class GeoMatchParamsTypeDef(BaseValidatorModel):
    Country: str
    AreaCode: str

class CreateSipMediaApplicationCallRequestRequestTypeDef(BaseValidatorModel):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: Optional[Mapping[str, str]] = None
    ArgumentsMap: Optional[Mapping[str, str]] = None

class SipMediaApplicationCallTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None

class SipMediaApplicationEndpointTypeDef(BaseValidatorModel):
    LambdaArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class SipRuleTargetApplicationTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    Priority: Optional[int] = None
    AwsRegion: Optional[str] = None

class VoiceConnectorItemTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Priority: int

class VoiceConnectorTypeDef(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Name: Optional[str] = None
    OutboundHostName: Optional[str] = None
    RequireEncryption: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorArn: Optional[str] = None

class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKeyArn: str

class CreateVoiceProfileRequestRequestTypeDef(BaseValidatorModel):
    SpeakerSearchTaskId: str

class VoiceProfileTypeDef(BaseValidatorModel):
    VoiceProfileId: Optional[str] = None
    VoiceProfileArn: Optional[str] = None
    VoiceProfileDomainId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None

class CredentialTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class DNISEmergencyCallingConfigurationTypeDef(BaseValidatorModel):
    EmergencyPhoneNumber: str
    CallingCountry: str
    TestPhoneNumber: Optional[str] = None

class DeletePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class DeleteProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str

class DeleteSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class DeleteSipRuleRequestRequestTypeDef(BaseValidatorModel):
    SipRuleId: str

class DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str

class DeleteVoiceConnectorOriginationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorProxyRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Usernames: Sequence[str]

class DeleteVoiceConnectorTerminationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceProfileDomainRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileDomainId: str

class DeleteVoiceProfileRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileId: str

class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]

class DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]

class VoiceConnectorSettingsTypeDef(BaseValidatorModel):
    CdrBucket: Optional[str] = None

class GetPhoneNumberOrderRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberOrderId: str

class GetPhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class GetProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str

class GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class SipMediaApplicationAlexaSkillConfigurationOutputTypeDef(BaseValidatorModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: List[str]

class GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class SipMediaApplicationLoggingConfigurationTypeDef(BaseValidatorModel):
    EnableSipMediaApplicationMessageLogs: Optional[bool] = None

class GetSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class GetSipRuleRequestRequestTypeDef(BaseValidatorModel):
    SipRuleId: str

class GetSpeakerSearchTaskRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str

class GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str

class GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class LoggingConfigurationTypeDef(BaseValidatorModel):
    EnableSIPLogs: Optional[bool] = None
    EnableMediaMetricLogs: Optional[bool] = None

class GetVoiceConnectorOriginationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorProxyRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class ProxyTypeDef(BaseValidatorModel):
    DefaultSessionExpiryMinutes: Optional[int] = None
    Disabled: Optional[bool] = None
    FallBackPhoneNumber: Optional[str] = None
    PhoneNumberCountries: Optional[List[str]] = None

class GetVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorTerminationHealthRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class TerminationHealthTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Source: Optional[str] = None

class GetVoiceConnectorTerminationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class TerminationOutputTypeDef(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None

class GetVoiceProfileDomainRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileDomainId: str

class GetVoiceProfileRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileId: str

class GetVoiceToneAnalysisTaskRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str
    IsCaller: bool

class ListPhoneNumberOrdersRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumbersRequestRequestTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListProxySessionsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Status: Optional[ProxySessionStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSipMediaApplicationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSipRulesRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSupportedPhoneNumberCountriesRequestRequestTypeDef(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType

class PhoneNumberCountryTypeDef(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListVoiceConnectorGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class ListVoiceConnectorsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVoiceProfileDomainsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class VoiceProfileDomainSummaryTypeDef(BaseValidatorModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class ListVoiceProfilesRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileDomainId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class VoiceProfileSummaryTypeDef(BaseValidatorModel):
    VoiceProfileId: Optional[str] = None
    VoiceProfileArn: Optional[str] = None
    VoiceProfileDomainId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None

class MediaInsightsConfigurationTypeDef(BaseValidatorModel):
    Disabled: Optional[bool] = None
    ConfigurationArn: Optional[str] = None

class OrderedPhoneNumberTypeDef(BaseValidatorModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None

class OriginationRouteTypeDef(BaseValidatorModel):
    Host: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[OriginationRouteProtocolType] = None
    Priority: Optional[int] = None
    Weight: Optional[int] = None

class ParticipantTypeDef(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    ProxyPhoneNumber: Optional[str] = None

class PhoneNumberAssociationTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Name: Optional[PhoneNumberAssociationNameType] = None
    AssociatedTimestamp: Optional[datetime] = None

class PhoneNumberCapabilitiesTypeDef(BaseValidatorModel):
    InboundCall: Optional[bool] = None
    OutboundCall: Optional[bool] = None
    InboundSMS: Optional[bool] = None
    OutboundSMS: Optional[bool] = None
    InboundMMS: Optional[bool] = None
    OutboundMMS: Optional[bool] = None

class SipMediaApplicationAlexaSkillConfigurationTypeDef(BaseValidatorModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: Sequence[str]

class PutVoiceConnectorProxyRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: Sequence[str]
    FallBackPhoneNumber: Optional[str] = None
    Disabled: Optional[bool] = None

class TerminationTypeDef(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[Sequence[str]] = None
    CidrAllowedList: Optional[Sequence[str]] = None
    Disabled: Optional[bool] = None

class RestorePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class SearchAvailablePhoneNumbersRequestRequestTypeDef(BaseValidatorModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SpeakerSearchResultTypeDef(BaseValidatorModel):
    ConfidenceScore: Optional[float] = None
    VoiceProfileId: Optional[str] = None

class StartSpeakerSearchTaskRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    TransactionId: str
    VoiceProfileDomainId: str
    ClientRequestToken: Optional[str] = None
    CallLeg: Optional[CallLegTypeType] = None

class StartVoiceToneAnalysisTaskRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    TransactionId: str
    LanguageCode: Literal["en-US"]
    ClientRequestToken: Optional[str] = None

class StopSpeakerSearchTaskRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str

class StopVoiceToneAnalysisTaskRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str

class StreamingNotificationTargetTypeDef(BaseValidatorModel):
    NotificationTarget: Optional[NotificationTargetType] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdatePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None

class UpdatePhoneNumberSettingsRequestRequestTypeDef(BaseValidatorModel):
    CallingName: str

class UpdateProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: Sequence[CapabilityType]
    ExpiryMinutes: Optional[int] = None

class UpdateSipMediaApplicationCallRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Mapping[str, str]

class UpdateVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool

class UpdateVoiceProfileDomainRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileDomainId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateVoiceProfileRequestRequestTypeDef(BaseValidatorModel):
    VoiceProfileId: str
    SpeakerSearchTaskId: str

class ValidateE911AddressRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str

class AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberSettingsResponseTypeDef(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableVoiceConnectorRegionsResponseTypeDef(BaseValidatorModel):
    VoiceConnectorRegions: List[VoiceConnectorAwsRegionType]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorTerminationCredentialsResponseTypeDef(BaseValidatorModel):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchUpdatePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]

class VoiceToneAnalysisTaskTypeDef(BaseValidatorModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetailsTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class ValidateE911AddressResponseTypeDef(BaseValidatorModel):
    ValidationResult: int
    AddressExternalId: str
    Address: AddressTypeDef
    CandidateAddressList: List[CandidateAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: Sequence[str]
    Capabilities: Sequence[CapabilityType]
    Name: Optional[str] = None
    ExpiryMinutes: Optional[int] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParamsTypeDef] = None

class CreateSipMediaApplicationCallResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationCallResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SipMediaApplicationTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    AwsRegion: Optional[str] = None
    Name: Optional[str] = None
    Endpoints: Optional[List[SipMediaApplicationEndpointTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    SipMediaApplicationArn: Optional[str] = None

class UpdateSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    Name: Optional[str] = None
    Endpoints: Optional[Sequence[SipMediaApplicationEndpointTypeDef]] = None

class CreateSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    AwsRegion: str
    Name: str
    Endpoints: Sequence[SipMediaApplicationEndpointTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RequireEncryption: bool
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSipRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplicationTypeDef]] = None

class SipRuleTypeDef(BaseValidatorModel):
    SipRuleId: Optional[str] = None
    Name: Optional[str] = None
    Disabled: Optional[bool] = None
    TriggerType: Optional[SipRuleTriggerTypeType] = None
    TriggerValue: Optional[str] = None
    TargetApplications: Optional[List[SipRuleTargetApplicationTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class UpdateSipRuleRequestRequestTypeDef(BaseValidatorModel):
    SipRuleId: str
    Name: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplicationTypeDef]] = None

class CreateVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    VoiceConnectorItems: Optional[Sequence[VoiceConnectorItemTypeDef]] = None

class UpdateVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: Sequence[VoiceConnectorItemTypeDef]

class VoiceConnectorGroupTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: Optional[str] = None
    Name: Optional[str] = None
    VoiceConnectorItems: Optional[List[VoiceConnectorItemTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorGroupArn: Optional[str] = None

class CreateVoiceConnectorResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorsResponseTypeDef(BaseValidatorModel):
    VoiceConnectors: List[VoiceConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateVoiceConnectorResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceProfileDomainRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class VoiceProfileDomainTypeDef(BaseValidatorModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateVoiceProfileResponseTypeDef(BaseValidatorModel):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceProfileResponseTypeDef(BaseValidatorModel):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceProfileResponseTypeDef(BaseValidatorModel):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Credentials: Optional[Sequence[CredentialTypeDef]] = None

class EmergencyCallingConfigurationOutputTypeDef(BaseValidatorModel):
    DNIS: Optional[List[DNISEmergencyCallingConfigurationTypeDef]] = None

class EmergencyCallingConfigurationTypeDef(BaseValidatorModel):
    DNIS: Optional[Sequence[DNISEmergencyCallingConfigurationTypeDef]] = None

class GetGlobalSettingsResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalSettingsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnector: Optional[VoiceConnectorSettingsTypeDef] = None

class GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationAlexaSkillConfiguration: SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationAlexaSkillConfiguration: SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: Optional[       SipMediaApplicationLoggingConfigurationTypeDef     ] = None

class PutSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutVoiceConnectorLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorProxyResponseTypeDef(BaseValidatorModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorProxyResponseTypeDef(BaseValidatorModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationHealthResponseTypeDef(BaseValidatorModel):
    TerminationHealth: TerminationHealthTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationResponseTypeDef(BaseValidatorModel):
    Termination: TerminationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationResponseTypeDef(BaseValidatorModel):
    Termination: TerminationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSipRulesRequestListSipRulesPaginateTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSupportedPhoneNumberCountriesResponseTypeDef(BaseValidatorModel):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceProfileDomainsResponseTypeDef(BaseValidatorModel):
    VoiceProfileDomains: List[VoiceProfileDomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVoiceProfilesResponseTypeDef(BaseValidatorModel):
    VoiceProfiles: List[VoiceProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PhoneNumberOrderTypeDef(BaseValidatorModel):
    PhoneNumberOrderId: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberOrderStatusType] = None
    OrderType: Optional[PhoneNumberOrderTypeType] = None
    OrderedPhoneNumbers: Optional[List[OrderedPhoneNumberTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class OriginationOutputTypeDef(BaseValidatorModel):
    Routes: Optional[List[OriginationRouteTypeDef]] = None
    Disabled: Optional[bool] = None

class OriginationTypeDef(BaseValidatorModel):
    Routes: Optional[Sequence[OriginationRouteTypeDef]] = None
    Disabled: Optional[bool] = None

class ProxySessionTypeDef(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    ProxySessionId: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ProxySessionStatusType] = None
    ExpiryMinutes: Optional[int] = None
    Capabilities: Optional[List[CapabilityType]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    EndedTimestamp: Optional[datetime] = None
    Participants: Optional[List[ParticipantTypeDef]] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParamsTypeDef] = None

class PhoneNumberTypeDef(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    E164PhoneNumber: Optional[str] = None
    Country: Optional[str] = None
    Type: Optional[PhoneNumberTypeType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberStatusType] = None
    Capabilities: Optional[PhoneNumberCapabilitiesTypeDef] = None
    Associations: Optional[List[PhoneNumberAssociationTypeDef]] = None
    CallingName: Optional[str] = None
    CallingNameStatus: Optional[CallingNameStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    DeletionTimestamp: Optional[datetime] = None
    OrderId: Optional[str] = None
    Name: Optional[str] = None

class PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationAlexaSkillConfiguration: Optional[       SipMediaApplicationAlexaSkillConfigurationTypeDef     ] = None

class PutVoiceConnectorTerminationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Termination: TerminationTypeDef

class SpeakerSearchDetailsTypeDef(BaseValidatorModel):
    Results: Optional[List[SpeakerSearchResultTypeDef]] = None
    VoiceprintGenerationStatus: Optional[str] = None

class StreamingConfigurationOutputTypeDef(BaseValidatorModel):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: Optional[List[StreamingNotificationTargetTypeDef]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfigurationTypeDef] = None

class StreamingConfigurationTypeDef(BaseValidatorModel):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: Optional[Sequence[StreamingNotificationTargetTypeDef]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfigurationTypeDef] = None

class GetVoiceToneAnalysisTaskResponseTypeDef(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartVoiceToneAnalysisTaskResponseTypeDef(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationResponseTypeDef(BaseValidatorModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationResponseTypeDef(BaseValidatorModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsResponseTypeDef(BaseValidatorModel):
    SipMediaApplications: List[SipMediaApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSipMediaApplicationResponseTypeDef(BaseValidatorModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipRuleResponseTypeDef(BaseValidatorModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipRuleResponseTypeDef(BaseValidatorModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipRulesResponseTypeDef(BaseValidatorModel):
    SipRules: List[SipRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSipRuleResponseTypeDef(BaseValidatorModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorGroupsResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroups: List[VoiceConnectorGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceProfileDomainResponseTypeDef(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceProfileDomainResponseTypeDef(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceProfileDomainResponseTypeDef(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef

class CreatePhoneNumberOrderResponseTypeDef(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberOrderResponseTypeDef(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumberOrdersResponseTypeDef(BaseValidatorModel):
    PhoneNumberOrders: List[PhoneNumberOrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetVoiceConnectorOriginationResponseTypeDef(BaseValidatorModel):
    Origination: OriginationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationResponseTypeDef(BaseValidatorModel):
    Origination: OriginationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Origination: OriginationTypeDef

class CreateProxySessionResponseTypeDef(BaseValidatorModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProxySessionResponseTypeDef(BaseValidatorModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProxySessionsResponseTypeDef(BaseValidatorModel):
    ProxySessions: List[ProxySessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateProxySessionResponseTypeDef(BaseValidatorModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersResponseTypeDef(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RestorePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpeakerSearchTaskTypeDef(BaseValidatorModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetailsTypeDef] = None
    SpeakerSearchDetails: Optional[SpeakerSearchDetailsTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class GetVoiceConnectorStreamingConfigurationResponseTypeDef(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationResponseTypeDef(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationTypeDef

class GetSpeakerSearchTaskResponseTypeDef(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerSearchTaskResponseTypeDef(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

