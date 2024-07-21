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
from aws_resource_validator.pydantic_models.chime_sdk_voice_constants import *

class AddressTypeDef(BaseModel):
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

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class PhoneNumberErrorTypeDef(BaseModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class BatchDeletePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberIds: Sequence[str]

class UpdatePhoneNumberRequestItemTypeDef(BaseModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None

class CallDetailsTypeDef(BaseModel):
    VoiceConnectorId: Optional[str] = None
    TransactionId: Optional[str] = None
    IsCaller: Optional[bool] = None

class CandidateAddressTypeDef(BaseModel):
    streetInfo: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None

class CreatePhoneNumberOrderRequestRequestTypeDef(BaseModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]
    Name: Optional[str] = None

class GeoMatchParamsTypeDef(BaseModel):
    Country: str
    AreaCode: str

class CreateSipMediaApplicationCallRequestRequestTypeDef(BaseModel):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: Optional[Mapping[str, str]] = None
    ArgumentsMap: Optional[Mapping[str, str]] = None

class SipMediaApplicationCallTypeDef(BaseModel):
    TransactionId: Optional[str] = None

class SipMediaApplicationEndpointTypeDef(BaseModel):
    LambdaArn: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class SipRuleTargetApplicationTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    Priority: Optional[int] = None
    AwsRegion: Optional[str] = None

class VoiceConnectorItemTypeDef(BaseModel):
    VoiceConnectorId: str
    Priority: int

class VoiceConnectorTypeDef(BaseModel):
    VoiceConnectorId: Optional[str] = None
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Name: Optional[str] = None
    OutboundHostName: Optional[str] = None
    RequireEncryption: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorArn: Optional[str] = None

class ServerSideEncryptionConfigurationTypeDef(BaseModel):
    KmsKeyArn: str

class CreateVoiceProfileRequestRequestTypeDef(BaseModel):
    SpeakerSearchTaskId: str

class VoiceProfileTypeDef(BaseModel):
    VoiceProfileId: Optional[str] = None
    VoiceProfileArn: Optional[str] = None
    VoiceProfileDomainId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None

class CredentialTypeDef(BaseModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class DNISEmergencyCallingConfigurationTypeDef(BaseModel):
    EmergencyPhoneNumber: str
    CallingCountry: str
    TestPhoneNumber: Optional[str] = None

class DeletePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class DeleteProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ProxySessionId: str

class DeleteSipMediaApplicationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class DeleteSipRuleRequestRequestTypeDef(BaseModel):
    SipRuleId: str

class DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str

class DeleteVoiceConnectorOriginationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorProxyRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Usernames: Sequence[str]

class DeleteVoiceConnectorTerminationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceProfileDomainRequestRequestTypeDef(BaseModel):
    VoiceProfileDomainId: str

class DeleteVoiceProfileRequestRequestTypeDef(BaseModel):
    VoiceProfileId: str

class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]

class DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]

class VoiceConnectorSettingsTypeDef(BaseModel):
    CdrBucket: Optional[str] = None

class GetPhoneNumberOrderRequestRequestTypeDef(BaseModel):
    PhoneNumberOrderId: str

class GetPhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class GetProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ProxySessionId: str

class GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class SipMediaApplicationAlexaSkillConfigurationOutputTypeDef(BaseModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: List[str]

class GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class SipMediaApplicationLoggingConfigurationTypeDef(BaseModel):
    EnableSipMediaApplicationMessageLogs: Optional[bool] = None

class GetSipMediaApplicationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class GetSipRuleRequestRequestTypeDef(BaseModel):
    SipRuleId: str

class GetSpeakerSearchTaskRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str

class GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str

class GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class LoggingConfigurationTypeDef(BaseModel):
    EnableSIPLogs: Optional[bool] = None
    EnableMediaMetricLogs: Optional[bool] = None

class GetVoiceConnectorOriginationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorProxyRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class ProxyTypeDef(BaseModel):
    DefaultSessionExpiryMinutes: Optional[int] = None
    Disabled: Optional[bool] = None
    FallBackPhoneNumber: Optional[str] = None
    PhoneNumberCountries: Optional[List[str]] = None

class GetVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorTerminationHealthRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class TerminationHealthTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    Source: Optional[str] = None

class GetVoiceConnectorTerminationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class TerminationOutputTypeDef(BaseModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None

class GetVoiceProfileDomainRequestRequestTypeDef(BaseModel):
    VoiceProfileDomainId: str

class GetVoiceProfileRequestRequestTypeDef(BaseModel):
    VoiceProfileId: str

class GetVoiceToneAnalysisTaskRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str
    IsCaller: bool

class ListPhoneNumberOrdersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumbersRequestRequestTypeDef(BaseModel):
    Status: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListProxySessionsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Status: Optional[ProxySessionStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSipMediaApplicationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSipRulesRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSupportedPhoneNumberCountriesRequestRequestTypeDef(BaseModel):
    ProductType: PhoneNumberProductTypeType

class PhoneNumberCountryTypeDef(BaseModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListVoiceConnectorGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class ListVoiceConnectorsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVoiceProfileDomainsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class VoiceProfileDomainSummaryTypeDef(BaseModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class ListVoiceProfilesRequestRequestTypeDef(BaseModel):
    VoiceProfileDomainId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class VoiceProfileSummaryTypeDef(BaseModel):
    VoiceProfileId: Optional[str] = None
    VoiceProfileArn: Optional[str] = None
    VoiceProfileDomainId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None

class MediaInsightsConfigurationTypeDef(BaseModel):
    Disabled: Optional[bool] = None
    ConfigurationArn: Optional[str] = None

class OrderedPhoneNumberTypeDef(BaseModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None

class OriginationRouteTypeDef(BaseModel):
    Host: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[OriginationRouteProtocolType] = None
    Priority: Optional[int] = None
    Weight: Optional[int] = None

class ParticipantTypeDef(BaseModel):
    PhoneNumber: Optional[str] = None
    ProxyPhoneNumber: Optional[str] = None

class PhoneNumberAssociationTypeDef(BaseModel):
    Value: Optional[str] = None
    Name: Optional[PhoneNumberAssociationNameType] = None
    AssociatedTimestamp: Optional[datetime] = None

class PhoneNumberCapabilitiesTypeDef(BaseModel):
    InboundCall: Optional[bool] = None
    OutboundCall: Optional[bool] = None
    InboundSMS: Optional[bool] = None
    OutboundSMS: Optional[bool] = None
    InboundMMS: Optional[bool] = None
    OutboundMMS: Optional[bool] = None

class SipMediaApplicationAlexaSkillConfigurationTypeDef(BaseModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: Sequence[str]

class PutVoiceConnectorProxyRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: Sequence[str]
    FallBackPhoneNumber: Optional[str] = None
    Disabled: Optional[bool] = None

class TerminationTypeDef(BaseModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[Sequence[str]] = None
    CidrAllowedList: Optional[Sequence[str]] = None
    Disabled: Optional[bool] = None

class RestorePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class SearchAvailablePhoneNumbersRequestRequestTypeDef(BaseModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SpeakerSearchResultTypeDef(BaseModel):
    ConfidenceScore: Optional[float] = None
    VoiceProfileId: Optional[str] = None

class StartSpeakerSearchTaskRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    TransactionId: str
    VoiceProfileDomainId: str
    ClientRequestToken: Optional[str] = None
    CallLeg: Optional[CallLegTypeType] = None

class StartVoiceToneAnalysisTaskRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    TransactionId: str
    LanguageCode: Literal["en-US"]
    ClientRequestToken: Optional[str] = None

class StopSpeakerSearchTaskRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str

class StopVoiceToneAnalysisTaskRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str

class StreamingNotificationTargetTypeDef(BaseModel):
    NotificationTarget: Optional[NotificationTargetType] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdatePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None

class UpdatePhoneNumberSettingsRequestRequestTypeDef(BaseModel):
    CallingName: str

class UpdateProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: Sequence[CapabilityType]
    ExpiryMinutes: Optional[int] = None

class UpdateSipMediaApplicationCallRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Mapping[str, str]

class UpdateVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool

class UpdateVoiceProfileDomainRequestRequestTypeDef(BaseModel):
    VoiceProfileDomainId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateVoiceProfileRequestRequestTypeDef(BaseModel):
    VoiceProfileId: str
    SpeakerSearchTaskId: str

class ValidateE911AddressRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str

class AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberSettingsResponseTypeDef(BaseModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableVoiceConnectorRegionsResponseTypeDef(BaseModel):
    VoiceConnectorRegions: List[VoiceConnectorAwsRegionType]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorTerminationCredentialsResponseTypeDef(BaseModel):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(BaseModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchUpdatePhoneNumberRequestRequestTypeDef(BaseModel):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]

class VoiceToneAnalysisTaskTypeDef(BaseModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetailsTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class ValidateE911AddressResponseTypeDef(BaseModel):
    ValidationResult: int
    AddressExternalId: str
    Address: AddressTypeDef
    CandidateAddressList: List[CandidateAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: Sequence[str]
    Capabilities: Sequence[CapabilityType]
    Name: Optional[str] = None
    ExpiryMinutes: Optional[int] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParamsTypeDef] = None

class CreateSipMediaApplicationCallResponseTypeDef(BaseModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationCallResponseTypeDef(BaseModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SipMediaApplicationTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    AwsRegion: Optional[str] = None
    Name: Optional[str] = None
    Endpoints: Optional[List[SipMediaApplicationEndpointTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    SipMediaApplicationArn: Optional[str] = None

class UpdateSipMediaApplicationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    Name: Optional[str] = None
    Endpoints: Optional[Sequence[SipMediaApplicationEndpointTypeDef]] = None

class CreateSipMediaApplicationRequestRequestTypeDef(BaseModel):
    AwsRegion: str
    Name: str
    Endpoints: Sequence[SipMediaApplicationEndpointTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVoiceConnectorRequestRequestTypeDef(BaseModel):
    Name: str
    RequireEncryption: bool
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSipRuleRequestRequestTypeDef(BaseModel):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplicationTypeDef]] = None

class SipRuleTypeDef(BaseModel):
    SipRuleId: Optional[str] = None
    Name: Optional[str] = None
    Disabled: Optional[bool] = None
    TriggerType: Optional[SipRuleTriggerTypeType] = None
    TriggerValue: Optional[str] = None
    TargetApplications: Optional[List[SipRuleTargetApplicationTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class UpdateSipRuleRequestRequestTypeDef(BaseModel):
    SipRuleId: str
    Name: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplicationTypeDef]] = None

class CreateVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    Name: str
    VoiceConnectorItems: Optional[Sequence[VoiceConnectorItemTypeDef]] = None

class UpdateVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: Sequence[VoiceConnectorItemTypeDef]

class VoiceConnectorGroupTypeDef(BaseModel):
    VoiceConnectorGroupId: Optional[str] = None
    Name: Optional[str] = None
    VoiceConnectorItems: Optional[List[VoiceConnectorItemTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorGroupArn: Optional[str] = None

class CreateVoiceConnectorResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorsResponseTypeDef(BaseModel):
    VoiceConnectors: List[VoiceConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateVoiceConnectorResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceProfileDomainRequestRequestTypeDef(BaseModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class VoiceProfileDomainTypeDef(BaseModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateVoiceProfileResponseTypeDef(BaseModel):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceProfileResponseTypeDef(BaseModel):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceProfileResponseTypeDef(BaseModel):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Credentials: Optional[Sequence[CredentialTypeDef]] = None

class EmergencyCallingConfigurationOutputTypeDef(BaseModel):
    DNIS: Optional[List[DNISEmergencyCallingConfigurationTypeDef]] = None

class EmergencyCallingConfigurationTypeDef(BaseModel):
    DNIS: Optional[Sequence[DNISEmergencyCallingConfigurationTypeDef]] = None

class GetGlobalSettingsResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalSettingsRequestRequestTypeDef(BaseModel):
    VoiceConnector: Optional[VoiceConnectorSettingsTypeDef] = None

class GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef(BaseModel):
    SipMediaApplicationAlexaSkillConfiguration: SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef(BaseModel):
    SipMediaApplicationAlexaSkillConfiguration: SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: Optional[       SipMediaApplicationLoggingConfigurationTypeDef     ] = None

class PutSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutVoiceConnectorLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorProxyResponseTypeDef(BaseModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorProxyResponseTypeDef(BaseModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationHealthResponseTypeDef(BaseModel):
    TerminationHealth: TerminationHealthTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationResponseTypeDef(BaseModel):
    Termination: TerminationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationResponseTypeDef(BaseModel):
    Termination: TerminationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSipRulesRequestListSipRulesPaginateTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSupportedPhoneNumberCountriesResponseTypeDef(BaseModel):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceProfileDomainsResponseTypeDef(BaseModel):
    VoiceProfileDomains: List[VoiceProfileDomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVoiceProfilesResponseTypeDef(BaseModel):
    VoiceProfiles: List[VoiceProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PhoneNumberOrderTypeDef(BaseModel):
    PhoneNumberOrderId: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberOrderStatusType] = None
    OrderType: Optional[PhoneNumberOrderTypeType] = None
    OrderedPhoneNumbers: Optional[List[OrderedPhoneNumberTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class OriginationOutputTypeDef(BaseModel):
    Routes: Optional[List[OriginationRouteTypeDef]] = None
    Disabled: Optional[bool] = None

class OriginationTypeDef(BaseModel):
    Routes: Optional[Sequence[OriginationRouteTypeDef]] = None
    Disabled: Optional[bool] = None

class ProxySessionTypeDef(BaseModel):
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

class PhoneNumberTypeDef(BaseModel):
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

class PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    SipMediaApplicationAlexaSkillConfiguration: Optional[       SipMediaApplicationAlexaSkillConfigurationTypeDef     ] = None

class PutVoiceConnectorTerminationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Termination: TerminationTypeDef

class SpeakerSearchDetailsTypeDef(BaseModel):
    Results: Optional[List[SpeakerSearchResultTypeDef]] = None
    VoiceprintGenerationStatus: Optional[str] = None

class StreamingConfigurationOutputTypeDef(BaseModel):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: Optional[List[StreamingNotificationTargetTypeDef]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfigurationTypeDef] = None

class StreamingConfigurationTypeDef(BaseModel):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: Optional[Sequence[StreamingNotificationTargetTypeDef]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfigurationTypeDef] = None

class GetVoiceToneAnalysisTaskResponseTypeDef(BaseModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartVoiceToneAnalysisTaskResponseTypeDef(BaseModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationResponseTypeDef(BaseModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationResponseTypeDef(BaseModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsResponseTypeDef(BaseModel):
    SipMediaApplications: List[SipMediaApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSipMediaApplicationResponseTypeDef(BaseModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipRuleResponseTypeDef(BaseModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipRuleResponseTypeDef(BaseModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipRulesResponseTypeDef(BaseModel):
    SipRules: List[SipRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSipRuleResponseTypeDef(BaseModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceConnectorGroupResponseTypeDef(BaseModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorGroupResponseTypeDef(BaseModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorGroupsResponseTypeDef(BaseModel):
    VoiceConnectorGroups: List[VoiceConnectorGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateVoiceConnectorGroupResponseTypeDef(BaseModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceProfileDomainResponseTypeDef(BaseModel):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceProfileDomainResponseTypeDef(BaseModel):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceProfileDomainResponseTypeDef(BaseModel):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef

class CreatePhoneNumberOrderResponseTypeDef(BaseModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberOrderResponseTypeDef(BaseModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumberOrdersResponseTypeDef(BaseModel):
    PhoneNumberOrders: List[PhoneNumberOrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetVoiceConnectorOriginationResponseTypeDef(BaseModel):
    Origination: OriginationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationResponseTypeDef(BaseModel):
    Origination: OriginationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Origination: OriginationTypeDef

class CreateProxySessionResponseTypeDef(BaseModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProxySessionResponseTypeDef(BaseModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProxySessionsResponseTypeDef(BaseModel):
    ProxySessions: List[ProxySessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateProxySessionResponseTypeDef(BaseModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberResponseTypeDef(BaseModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersResponseTypeDef(BaseModel):
    PhoneNumbers: List[PhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RestorePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpeakerSearchTaskTypeDef(BaseModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetailsTypeDef] = None
    SpeakerSearchDetails: Optional[SpeakerSearchDetailsTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class GetVoiceConnectorStreamingConfigurationResponseTypeDef(BaseModel):
    StreamingConfiguration: StreamingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationResponseTypeDef(BaseModel):
    StreamingConfiguration: StreamingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationTypeDef

class GetSpeakerSearchTaskResponseTypeDef(BaseModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerSearchTaskResponseTypeDef(BaseModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

