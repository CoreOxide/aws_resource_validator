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
from aws_resource_validator.pydantic_models.chime_sdk_voice_constants import *

class Address(BaseValidatorModel):
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


class AssociatePhoneNumbersWithVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None


class PhoneNumberError(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociatePhoneNumbersWithVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None


class BatchDeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberIds: Sequence[str]


class UpdatePhoneNumberRequestItem(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None


class CallDetails(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    TransactionId: Optional[str] = None
    IsCaller: Optional[bool] = None


class CandidateAddress(BaseValidatorModel):
    streetInfo: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None


class CreatePhoneNumberOrderRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]
    Name: Optional[str] = None


class GeoMatchParams(BaseValidatorModel):
    Country: str
    AreaCode: str


class CreateSipMediaApplicationCallRequest(BaseValidatorModel):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: Optional[Mapping[str, str]] = None
    ArgumentsMap: Optional[Mapping[str, str]] = None


class SipMediaApplicationCall(BaseValidatorModel):
    TransactionId: Optional[str] = None


class SipMediaApplicationEndpoint(BaseValidatorModel):
    LambdaArn: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class SipRuleTargetApplication(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    Priority: Optional[int] = None
    AwsRegion: Optional[str] = None


class VoiceConnectorItem(BaseValidatorModel):
    VoiceConnectorId: str
    Priority: int


class VoiceConnector(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Name: Optional[str] = None
    OutboundHostName: Optional[str] = None
    RequireEncryption: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorArn: Optional[str] = None
    IntegrationType: Optional[VoiceConnectorIntegrationTypeType] = None


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    KmsKeyArn: str


class CreateVoiceProfileRequest(BaseValidatorModel):
    SpeakerSearchTaskId: str


class VoiceProfile(BaseValidatorModel):
    VoiceProfileId: Optional[str] = None
    VoiceProfileArn: Optional[str] = None
    VoiceProfileDomainId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None


class Credential(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None


class DNISEmergencyCallingConfiguration(BaseValidatorModel):
    EmergencyPhoneNumber: str
    CallingCountry: str
    TestPhoneNumber: Optional[str] = None


class DeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class DeleteProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str


class DeleteSipMediaApplicationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


class DeleteSipRuleRequest(BaseValidatorModel):
    SipRuleId: str


class DeleteVoiceConnectorEmergencyCallingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceConnectorExternalSystemsConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str


class DeleteVoiceConnectorOriginationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceConnectorProxyRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceConnectorStreamingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceConnectorTerminationCredentialsRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Usernames: Sequence[str]


class DeleteVoiceConnectorTerminationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class DeleteVoiceProfileDomainRequest(BaseValidatorModel):
    VoiceProfileDomainId: str


class DeleteVoiceProfileRequest(BaseValidatorModel):
    VoiceProfileId: str


class DisassociatePhoneNumbersFromVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]


class DisassociatePhoneNumbersFromVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]


class ExternalSystemsConfiguration(BaseValidatorModel):
    SessionBorderControllerTypes: Optional[List[SessionBorderControllerTypeType]] = None
    ContactCenterSystemTypes: Optional[List[ContactCenterSystemTypeType]] = None


class VoiceConnectorSettings(BaseValidatorModel):
    CdrBucket: Optional[str] = None


class GetPhoneNumberOrderRequest(BaseValidatorModel):
    PhoneNumberOrderId: str


class GetPhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class GetProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str


class GetSipMediaApplicationAlexaSkillConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


class SipMediaApplicationAlexaSkillConfigurationOutput(BaseValidatorModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: List[str]


class GetSipMediaApplicationLoggingConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


class SipMediaApplicationLoggingConfiguration(BaseValidatorModel):
    EnableSipMediaApplicationMessageLogs: Optional[bool] = None


class GetSipMediaApplicationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


class GetSipRuleRequest(BaseValidatorModel):
    SipRuleId: str


class GetSpeakerSearchTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str


class GetVoiceConnectorEmergencyCallingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class GetVoiceConnectorExternalSystemsConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class GetVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str


class GetVoiceConnectorLoggingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class LoggingConfiguration(BaseValidatorModel):
    EnableSIPLogs: Optional[bool] = None
    EnableMediaMetricLogs: Optional[bool] = None


class GetVoiceConnectorOriginationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class GetVoiceConnectorProxyRequest(BaseValidatorModel):
    VoiceConnectorId: str


class Proxy(BaseValidatorModel):
    DefaultSessionExpiryMinutes: Optional[int] = None
    Disabled: Optional[bool] = None
    FallBackPhoneNumber: Optional[str] = None
    PhoneNumberCountries: Optional[List[str]] = None


class GetVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str


class GetVoiceConnectorStreamingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class GetVoiceConnectorTerminationHealthRequest(BaseValidatorModel):
    VoiceConnectorId: str


class TerminationHealth(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Source: Optional[str] = None


class GetVoiceConnectorTerminationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class TerminationOutput(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None


class GetVoiceProfileDomainRequest(BaseValidatorModel):
    VoiceProfileDomainId: str


class GetVoiceProfileRequest(BaseValidatorModel):
    VoiceProfileId: str


class GetVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str
    IsCaller: bool


class ListPhoneNumberOrdersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPhoneNumbersRequest(BaseValidatorModel):
    Status: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListProxySessionsRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Status: Optional[ProxySessionStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSipMediaApplicationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSipRulesRequest(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSupportedPhoneNumberCountriesRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType


class PhoneNumberCountry(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class ListVoiceConnectorGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListVoiceConnectorTerminationCredentialsRequest(BaseValidatorModel):
    VoiceConnectorId: str


class ListVoiceConnectorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListVoiceProfileDomainsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class VoiceProfileDomainSummary(BaseValidatorModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class ListVoiceProfilesRequest(BaseValidatorModel):
    VoiceProfileDomainId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class VoiceProfileSummary(BaseValidatorModel):
    VoiceProfileId: Optional[str] = None
    VoiceProfileArn: Optional[str] = None
    VoiceProfileDomainId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None


class MediaInsightsConfiguration(BaseValidatorModel):
    Disabled: Optional[bool] = None
    ConfigurationArn: Optional[str] = None


class OrderedPhoneNumber(BaseValidatorModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None


class Participant(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    ProxyPhoneNumber: Optional[str] = None


class PhoneNumberAssociation(BaseValidatorModel):
    Value: Optional[str] = None
    Name: Optional[PhoneNumberAssociationNameType] = None
    AssociatedTimestamp: Optional[datetime] = None


class PhoneNumberCapabilities(BaseValidatorModel):
    InboundCall: Optional[bool] = None
    OutboundCall: Optional[bool] = None
    InboundSMS: Optional[bool] = None
    OutboundSMS: Optional[bool] = None
    InboundMMS: Optional[bool] = None
    OutboundMMS: Optional[bool] = None


class PutVoiceConnectorExternalSystemsConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    SessionBorderControllerTypes: Optional[Sequence[SessionBorderControllerTypeType]] = None
    ContactCenterSystemTypes: Optional[Sequence[ContactCenterSystemTypeType]] = None


class PutVoiceConnectorProxyRequest(BaseValidatorModel):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: Sequence[str]
    FallBackPhoneNumber: Optional[str] = None
    Disabled: Optional[bool] = None


class RestorePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class SearchAvailablePhoneNumbersRequest(BaseValidatorModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SipMediaApplicationAlexaSkillConfiguration(BaseValidatorModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: Sequence[str]


class SpeakerSearchResult(BaseValidatorModel):
    ConfidenceScore: Optional[float] = None
    VoiceProfileId: Optional[str] = None


class StartSpeakerSearchTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    TransactionId: str
    VoiceProfileDomainId: str
    ClientRequestToken: Optional[str] = None
    CallLeg: Optional[CallLegTypeType] = None


class StartVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    TransactionId: str
    LanguageCode: Literal["en-US"]
    ClientRequestToken: Optional[str] = None


class StopSpeakerSearchTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str


class StopVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str


class StreamingNotificationTarget(BaseValidatorModel):
    NotificationTarget: Optional[NotificationTargetType] = None


class Termination(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[Sequence[str]] = None
    CidrAllowedList: Optional[Sequence[str]] = None
    Disabled: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None


class UpdatePhoneNumberSettingsRequest(BaseValidatorModel):
    CallingName: str


class UpdateProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: Sequence[CapabilityType]
    ExpiryMinutes: Optional[int] = None


class UpdateSipMediaApplicationCallRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Mapping[str, str]


class UpdateVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool


class UpdateVoiceProfileDomainRequest(BaseValidatorModel):
    VoiceProfileDomainId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateVoiceProfileRequest(BaseValidatorModel):
    VoiceProfileId: str
    SpeakerSearchTaskId: str


class ValidateE911AddressRequest(BaseValidatorModel):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str


class AssociatePhoneNumbersWithVoiceConnectorGroupResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class AssociatePhoneNumbersWithVoiceConnectorResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class BatchDeletePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class BatchUpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class DisassociatePhoneNumbersFromVoiceConnectorGroupResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class DisassociatePhoneNumbersFromVoiceConnectorResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetPhoneNumberSettingsResponse(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ListAvailableVoiceConnectorRegionsResponse(BaseValidatorModel):
    VoiceConnectorRegions: List[VoiceConnectorAwsRegionType]
    ResponseMetadata: ResponseMetadata


class ListVoiceConnectorTerminationCredentialsResponse(BaseValidatorModel):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadata


class SearchAvailablePhoneNumbersResponse(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchUpdatePhoneNumberRequest(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItem]


class VoiceToneAnalysisTask(BaseValidatorModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetails] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None


class ValidateE911AddressResponse(BaseValidatorModel):
    ValidationResult: int
    AddressExternalId: str
    Address: Address
    CandidateAddressList: List[CandidateAddress]
    ResponseMetadata: ResponseMetadata


class CreateProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: Sequence[str]
    Capabilities: Sequence[CapabilityType]
    Name: Optional[str] = None
    ExpiryMinutes: Optional[int] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParams] = None


class CreateSipMediaApplicationCallResponse(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCall
    ResponseMetadata: ResponseMetadata


class UpdateSipMediaApplicationCallResponse(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCall
    ResponseMetadata: ResponseMetadata


class SipMediaApplication(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    AwsRegion: Optional[str] = None
    Name: Optional[str] = None
    Endpoints: Optional[List[SipMediaApplicationEndpoint]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    SipMediaApplicationArn: Optional[str] = None


class UpdateSipMediaApplicationRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    Name: Optional[str] = None
    Endpoints: Optional[Sequence[SipMediaApplicationEndpoint]] = None


class CreateSipMediaApplicationRequest(BaseValidatorModel):
    AwsRegion: str
    Name: str
    Endpoints: Sequence[SipMediaApplicationEndpoint]
    Tags: Optional[Sequence[Tag]] = None


class CreateVoiceConnectorRequest(BaseValidatorModel):
    Name: str
    RequireEncryption: bool
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Tags: Optional[Sequence[Tag]] = None
    IntegrationType: Optional[VoiceConnectorIntegrationTypeType] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateSipRuleRequest(BaseValidatorModel):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplication]] = None


class SipRule(BaseValidatorModel):
    SipRuleId: Optional[str] = None
    Name: Optional[str] = None
    Disabled: Optional[bool] = None
    TriggerType: Optional[SipRuleTriggerTypeType] = None
    TriggerValue: Optional[str] = None
    TargetApplications: Optional[List[SipRuleTargetApplication]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class UpdateSipRuleRequest(BaseValidatorModel):
    SipRuleId: str
    Name: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplication]] = None


class CreateVoiceConnectorGroupRequest(BaseValidatorModel):
    Name: str
    VoiceConnectorItems: Optional[Sequence[VoiceConnectorItem]] = None


class UpdateVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: Sequence[VoiceConnectorItem]


class VoiceConnectorGroup(BaseValidatorModel):
    VoiceConnectorGroupId: Optional[str] = None
    Name: Optional[str] = None
    VoiceConnectorItems: Optional[List[VoiceConnectorItem]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorGroupArn: Optional[str] = None


class CreateVoiceConnectorResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnector
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnector
    ResponseMetadata: ResponseMetadata


class ListVoiceConnectorsResponse(BaseValidatorModel):
    VoiceConnectors: List[VoiceConnector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateVoiceConnectorResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnector
    ResponseMetadata: ResponseMetadata


class CreateVoiceProfileDomainRequest(BaseValidatorModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfiguration
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class VoiceProfileDomain(BaseValidatorModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class CreateVoiceProfileResponse(BaseValidatorModel):
    VoiceProfile: VoiceProfile
    ResponseMetadata: ResponseMetadata


class GetVoiceProfileResponse(BaseValidatorModel):
    VoiceProfile: VoiceProfile
    ResponseMetadata: ResponseMetadata


class UpdateVoiceProfileResponse(BaseValidatorModel):
    VoiceProfile: VoiceProfile
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorTerminationCredentialsRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Credentials: Optional[Sequence[Credential]] = None


class EmergencyCallingConfigurationOutput(BaseValidatorModel):
    DNIS: Optional[List[DNISEmergencyCallingConfiguration]] = None


class EmergencyCallingConfiguration(BaseValidatorModel):
    DNIS: Optional[Sequence[DNISEmergencyCallingConfiguration]] = None


class GetVoiceConnectorExternalSystemsConfigurationResponse(BaseValidatorModel):
    ExternalSystemsConfiguration: ExternalSystemsConfiguration
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorExternalSystemsConfigurationResponse(BaseValidatorModel):
    ExternalSystemsConfiguration: ExternalSystemsConfiguration
    ResponseMetadata: ResponseMetadata


class GetGlobalSettingsResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnectorSettings
    ResponseMetadata: ResponseMetadata


class UpdateGlobalSettingsRequest(BaseValidatorModel):
    VoiceConnector: Optional[VoiceConnectorSettings] = None


class GetSipMediaApplicationAlexaSkillConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationAlexaSkillConfiguration: ( SipMediaApplicationAlexaSkillConfigurationOutput )
    ResponseMetadata: ResponseMetadata


class PutSipMediaApplicationAlexaSkillConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationAlexaSkillConfiguration: ( SipMediaApplicationAlexaSkillConfigurationOutput )
    ResponseMetadata: ResponseMetadata


class GetSipMediaApplicationLoggingConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfiguration
    ResponseMetadata: ResponseMetadata


class PutSipMediaApplicationLoggingConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: Optional[ SipMediaApplicationLoggingConfiguration ] = None


class PutSipMediaApplicationLoggingConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfiguration
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfiguration
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorLoggingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfiguration


class PutVoiceConnectorLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfiguration
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorProxyResponse(BaseValidatorModel):
    Proxy: Proxy
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorProxyResponse(BaseValidatorModel):
    Proxy: Proxy
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorTerminationHealthResponse(BaseValidatorModel):
    TerminationHealth: TerminationHealth
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorTerminationResponse(BaseValidatorModel):
    Termination: TerminationOutput
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorTerminationResponse(BaseValidatorModel):
    Termination: TerminationOutput
    ResponseMetadata: ResponseMetadata


class ListSipMediaApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSipRulesRequestPaginate(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSupportedPhoneNumberCountriesResponse(BaseValidatorModel):
    PhoneNumberCountries: List[PhoneNumberCountry]
    ResponseMetadata: ResponseMetadata


class ListVoiceProfileDomainsResponse(BaseValidatorModel):
    VoiceProfileDomains: List[VoiceProfileDomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVoiceProfilesResponse(BaseValidatorModel):
    VoiceProfiles: List[VoiceProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PhoneNumberOrder(BaseValidatorModel):
    PhoneNumberOrderId: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberOrderStatusType] = None
    OrderType: Optional[PhoneNumberOrderTypeType] = None
    OrderedPhoneNumbers: Optional[List[OrderedPhoneNumber]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class OriginationRoute(BaseValidatorModel):
    pass


class OriginationOutput(BaseValidatorModel):
    Routes: Optional[List[OriginationRoute]] = None
    Disabled: Optional[bool] = None


class Origination(BaseValidatorModel):
    Routes: Optional[Sequence[OriginationRoute]] = None
    Disabled: Optional[bool] = None


class ProxySession(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    ProxySessionId: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ProxySessionStatusType] = None
    ExpiryMinutes: Optional[int] = None
    Capabilities: Optional[List[CapabilityType]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    EndedTimestamp: Optional[datetime] = None
    Participants: Optional[List[Participant]] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParams] = None


class SpeakerSearchDetails(BaseValidatorModel):
    Results: Optional[List[SpeakerSearchResult]] = None
    VoiceprintGenerationStatus: Optional[str] = None


class StreamingConfigurationOutput(BaseValidatorModel):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: Optional[List[StreamingNotificationTarget]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfiguration] = None


class StreamingConfiguration(BaseValidatorModel):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: Optional[Sequence[StreamingNotificationTarget]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfiguration] = None


class GetVoiceToneAnalysisTaskResponse(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTask
    ResponseMetadata: ResponseMetadata


class StartVoiceToneAnalysisTaskResponse(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTask
    ResponseMetadata: ResponseMetadata


class CreateSipMediaApplicationResponse(BaseValidatorModel):
    SipMediaApplication: SipMediaApplication
    ResponseMetadata: ResponseMetadata


class GetSipMediaApplicationResponse(BaseValidatorModel):
    SipMediaApplication: SipMediaApplication
    ResponseMetadata: ResponseMetadata


class ListSipMediaApplicationsResponse(BaseValidatorModel):
    SipMediaApplications: List[SipMediaApplication]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSipMediaApplicationResponse(BaseValidatorModel):
    SipMediaApplication: SipMediaApplication
    ResponseMetadata: ResponseMetadata


class CreateSipRuleResponse(BaseValidatorModel):
    SipRule: SipRule
    ResponseMetadata: ResponseMetadata


class GetSipRuleResponse(BaseValidatorModel):
    SipRule: SipRule
    ResponseMetadata: ResponseMetadata


class ListSipRulesResponse(BaseValidatorModel):
    SipRules: List[SipRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSipRuleResponse(BaseValidatorModel):
    SipRule: SipRule
    ResponseMetadata: ResponseMetadata


class CreateVoiceConnectorGroupResponse(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroup
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorGroupResponse(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroup
    ResponseMetadata: ResponseMetadata


class ListVoiceConnectorGroupsResponse(BaseValidatorModel):
    VoiceConnectorGroups: List[VoiceConnectorGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateVoiceConnectorGroupResponse(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroup
    ResponseMetadata: ResponseMetadata


class CreateVoiceProfileDomainResponse(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomain
    ResponseMetadata: ResponseMetadata


class GetVoiceProfileDomainResponse(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomain
    ResponseMetadata: ResponseMetadata


class UpdateVoiceProfileDomainResponse(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomain
    ResponseMetadata: ResponseMetadata


class GetVoiceConnectorEmergencyCallingConfigurationResponse(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorEmergencyCallingConfigurationResponse(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class CreatePhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


class GetPhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


class ListPhoneNumberOrdersResponse(BaseValidatorModel):
    PhoneNumberOrders: List[PhoneNumberOrder]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetVoiceConnectorOriginationResponse(BaseValidatorModel):
    Origination: OriginationOutput
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorOriginationResponse(BaseValidatorModel):
    Origination: OriginationOutput
    ResponseMetadata: ResponseMetadata


class CreateProxySessionResponse(BaseValidatorModel):
    ProxySession: ProxySession
    ResponseMetadata: ResponseMetadata


class GetProxySessionResponse(BaseValidatorModel):
    ProxySession: ProxySession
    ResponseMetadata: ResponseMetadata


class ListProxySessionsResponse(BaseValidatorModel):
    ProxySessions: List[ProxySession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateProxySessionResponse(BaseValidatorModel):
    ProxySession: ProxySession
    ResponseMetadata: ResponseMetadata


class PhoneNumber(BaseValidatorModel):
    pass


class GetPhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


class ListPhoneNumbersResponse(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RestorePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


class UpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


class SipMediaApplicationAlexaSkillConfigurationUnion(BaseValidatorModel):
    pass


class PutSipMediaApplicationAlexaSkillConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationAlexaSkillConfiguration: Optional[ SipMediaApplicationAlexaSkillConfigurationUnion ] = None


class SpeakerSearchTask(BaseValidatorModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetails] = None
    SpeakerSearchDetails: Optional[SpeakerSearchDetails] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None


class GetVoiceConnectorStreamingConfigurationResponse(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class PutVoiceConnectorStreamingConfigurationResponse(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class TerminationUnion(BaseValidatorModel):
    pass


class PutVoiceConnectorTerminationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Termination: TerminationUnion


class EmergencyCallingConfigurationUnion(BaseValidatorModel):
    pass


class PutVoiceConnectorEmergencyCallingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationUnion


class OriginationUnion(BaseValidatorModel):
    pass


class PutVoiceConnectorOriginationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Origination: OriginationUnion


class GetSpeakerSearchTaskResponse(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTask
    ResponseMetadata: ResponseMetadata


class StartSpeakerSearchTaskResponse(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTask
    ResponseMetadata: ResponseMetadata


class StreamingConfigurationUnion(BaseValidatorModel):
    pass


class PutVoiceConnectorStreamingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationUnion


