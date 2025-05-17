from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.chime_sdk_voice.chime_sdk_voice_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'associate_phone_numbers_with_voice_connector_group' function.
class AssociatePhoneNumbersWithVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: List[str]
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


# This class is the input for the 'associate_phone_numbers_with_voice_connector' function.
class AssociatePhoneNumbersWithVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: List[str]
    ForceAssociate: Optional[bool] = None


# This class is the input for the 'batch_delete_phone_number' function.
class BatchDeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberIds: List[str]


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


# This class is the input for the 'create_phone_number_order' function.
class CreatePhoneNumberOrderRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: List[str]
    Name: Optional[str] = None


class GeoMatchParams(BaseValidatorModel):
    Country: str
    AreaCode: str


# This class is the input for the 'create_sip_media_application_call' function.
class CreateSipMediaApplicationCallRequest(BaseValidatorModel):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: Optional[Dict[str, str]] = None
    ArgumentsMap: Optional[Dict[str, str]] = None


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


# This class is the input for the 'create_voice_profile' function.
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


# This class is the input for the 'delete_phone_number' function.
class DeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'delete_proxy_session' function.
class DeleteProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str


# This class is the input for the 'delete_sip_media_application' function.
class DeleteSipMediaApplicationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


# This class is the input for the 'delete_sip_rule' function.
class DeleteSipRuleRequest(BaseValidatorModel):
    SipRuleId: str


# This class is the input for the 'delete_voice_connector_emergency_calling_configuration' function.
class DeleteVoiceConnectorEmergencyCallingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_connector_external_systems_configuration' function.
class DeleteVoiceConnectorExternalSystemsConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_connector_group' function.
class DeleteVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str


# This class is the input for the 'delete_voice_connector_origination' function.
class DeleteVoiceConnectorOriginationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_connector_proxy' function.
class DeleteVoiceConnectorProxyRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_connector' function.
class DeleteVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_connector_streaming_configuration' function.
class DeleteVoiceConnectorStreamingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_connector_termination_credentials' function.
class DeleteVoiceConnectorTerminationCredentialsRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Usernames: List[str]


# This class is the input for the 'delete_voice_connector_termination' function.
class DeleteVoiceConnectorTerminationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'delete_voice_profile_domain' function.
class DeleteVoiceProfileDomainRequest(BaseValidatorModel):
    VoiceProfileDomainId: str


# This class is the input for the 'delete_voice_profile' function.
class DeleteVoiceProfileRequest(BaseValidatorModel):
    VoiceProfileId: str


# This class is the input for the 'disassociate_phone_numbers_from_voice_connector_group' function.
class DisassociatePhoneNumbersFromVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: List[str]


# This class is the input for the 'disassociate_phone_numbers_from_voice_connector' function.
class DisassociatePhoneNumbersFromVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: List[str]


class ExternalSystemsConfiguration(BaseValidatorModel):
    SessionBorderControllerTypes: Optional[List[SessionBorderControllerTypeType]] = None
    ContactCenterSystemTypes: Optional[List[ContactCenterSystemTypeType]] = None


class VoiceConnectorSettings(BaseValidatorModel):
    CdrBucket: Optional[str] = None


# This class is the input for the 'get_phone_number_order' function.
class GetPhoneNumberOrderRequest(BaseValidatorModel):
    PhoneNumberOrderId: str


# This class is the input for the 'get_phone_number' function.
class GetPhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'get_proxy_session' function.
class GetProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str


# This class is the input for the 'get_sip_media_application_alexa_skill_configuration' function.
class GetSipMediaApplicationAlexaSkillConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


class SipMediaApplicationAlexaSkillConfigurationOutput(BaseValidatorModel):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: List[str]


# This class is the input for the 'get_sip_media_application_logging_configuration' function.
class GetSipMediaApplicationLoggingConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


class SipMediaApplicationLoggingConfiguration(BaseValidatorModel):
    EnableSipMediaApplicationMessageLogs: Optional[bool] = None


# This class is the input for the 'get_sip_media_application' function.
class GetSipMediaApplicationRequest(BaseValidatorModel):
    SipMediaApplicationId: str


# This class is the input for the 'get_sip_rule' function.
class GetSipRuleRequest(BaseValidatorModel):
    SipRuleId: str


# This class is the input for the 'get_speaker_search_task' function.
class GetSpeakerSearchTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str


# This class is the input for the 'get_voice_connector_emergency_calling_configuration' function.
class GetVoiceConnectorEmergencyCallingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'get_voice_connector_external_systems_configuration' function.
class GetVoiceConnectorExternalSystemsConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'get_voice_connector_group' function.
class GetVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str


# This class is the input for the 'get_voice_connector_logging_configuration' function.
class GetVoiceConnectorLoggingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class LoggingConfiguration(BaseValidatorModel):
    EnableSIPLogs: Optional[bool] = None
    EnableMediaMetricLogs: Optional[bool] = None


# This class is the input for the 'get_voice_connector_origination' function.
class GetVoiceConnectorOriginationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'get_voice_connector_proxy' function.
class GetVoiceConnectorProxyRequest(BaseValidatorModel):
    VoiceConnectorId: str


class Proxy(BaseValidatorModel):
    DefaultSessionExpiryMinutes: Optional[int] = None
    Disabled: Optional[bool] = None
    FallBackPhoneNumber: Optional[str] = None
    PhoneNumberCountries: Optional[List[str]] = None


# This class is the input for the 'get_voice_connector' function.
class GetVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'get_voice_connector_streaming_configuration' function.
class GetVoiceConnectorStreamingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'get_voice_connector_termination_health' function.
class GetVoiceConnectorTerminationHealthRequest(BaseValidatorModel):
    VoiceConnectorId: str


class TerminationHealth(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Source: Optional[str] = None


# This class is the input for the 'get_voice_connector_termination' function.
class GetVoiceConnectorTerminationRequest(BaseValidatorModel):
    VoiceConnectorId: str


class TerminationOutput(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None


# This class is the input for the 'get_voice_profile_domain' function.
class GetVoiceProfileDomainRequest(BaseValidatorModel):
    VoiceProfileDomainId: str


# This class is the input for the 'get_voice_profile' function.
class GetVoiceProfileRequest(BaseValidatorModel):
    VoiceProfileId: str


# This class is the input for the 'get_voice_tone_analysis_task' function.
class GetVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str
    IsCaller: bool


# This class is the input for the 'list_phone_number_orders' function.
class ListPhoneNumberOrdersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_phone_numbers' function.
class ListPhoneNumbersRequest(BaseValidatorModel):
    Status: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_proxy_sessions' function.
class ListProxySessionsRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Status: Optional[ProxySessionStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_sip_media_applications' function.
class ListSipMediaApplicationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_sip_rules' function.
class ListSipRulesRequest(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_supported_phone_number_countries' function.
class ListSupportedPhoneNumberCountriesRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType


class PhoneNumberCountry(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'list_voice_connector_groups' function.
class ListVoiceConnectorGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_voice_connector_termination_credentials' function.
class ListVoiceConnectorTerminationCredentialsRequest(BaseValidatorModel):
    VoiceConnectorId: str


# This class is the input for the 'list_voice_connectors' function.
class ListVoiceConnectorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_voice_profile_domains' function.
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


# This class is the input for the 'list_voice_profiles' function.
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


class OriginationRoute(BaseValidatorModel):
    Host: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[OriginationRouteProtocolType] = None
    Priority: Optional[int] = None
    Weight: Optional[int] = None


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


# This class is the input for the 'put_voice_connector_external_systems_configuration' function.
class PutVoiceConnectorExternalSystemsConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    SessionBorderControllerTypes: Optional[List[SessionBorderControllerTypeType]] = None
    ContactCenterSystemTypes: Optional[List[ContactCenterSystemTypeType]] = None


# This class is the input for the 'put_voice_connector_proxy' function.
class PutVoiceConnectorProxyRequest(BaseValidatorModel):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: List[str]
    FallBackPhoneNumber: Optional[str] = None
    Disabled: Optional[bool] = None


# This class is the input for the 'restore_phone_number' function.
class RestorePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'search_available_phone_numbers' function.
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
    AlexaSkillIds: List[str]


class SpeakerSearchResult(BaseValidatorModel):
    ConfidenceScore: Optional[float] = None
    VoiceProfileId: Optional[str] = None


# This class is the input for the 'start_speaker_search_task' function.
class StartSpeakerSearchTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    TransactionId: str
    VoiceProfileDomainId: str
    ClientRequestToken: Optional[str] = None
    CallLeg: Optional[CallLegTypeType] = None


# This class is the input for the 'start_voice_tone_analysis_task' function.
class StartVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    TransactionId: str
    LanguageCode: Literal['en-US']
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'stop_speaker_search_task' function.
class StopSpeakerSearchTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str


# This class is the input for the 'stop_voice_tone_analysis_task' function.
class StopVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str


class StreamingNotificationTarget(BaseValidatorModel):
    NotificationTarget: Optional[NotificationTargetType] = None


class Termination(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_phone_number' function.
class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'update_phone_number_settings' function.
class UpdatePhoneNumberSettingsRequest(BaseValidatorModel):
    CallingName: str


# This class is the input for the 'update_proxy_session' function.
class UpdateProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: List[CapabilityType]
    ExpiryMinutes: Optional[int] = None


# This class is the input for the 'update_sip_media_application_call' function.
class UpdateSipMediaApplicationCallRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Dict[str, str]


# This class is the input for the 'update_voice_connector' function.
class UpdateVoiceConnectorRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool


# This class is the input for the 'update_voice_profile_domain' function.
class UpdateVoiceProfileDomainRequest(BaseValidatorModel):
    VoiceProfileDomainId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_voice_profile' function.
class UpdateVoiceProfileRequest(BaseValidatorModel):
    VoiceProfileId: str
    SpeakerSearchTaskId: str


# This class is the input for the 'validate_e911_address' function.
class ValidateE911AddressRequest(BaseValidatorModel):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str


# This class is the output for the 'associate_phone_numbers_with_voice_connector_group' function.
class AssociatePhoneNumbersWithVoiceConnectorGroupResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_phone_numbers_with_voice_connector' function.
class AssociatePhoneNumbersWithVoiceConnectorResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_phone_number' function.
class BatchDeletePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_phone_number' function.
class BatchUpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_phone_numbers_from_voice_connector_group' function.
class DisassociatePhoneNumbersFromVoiceConnectorGroupResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_phone_numbers_from_voice_connector' function.
class DisassociatePhoneNumbersFromVoiceConnectorResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_phone_number_settings' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetPhoneNumberSettingsResponse(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class ListAvailableVoiceConnectorRegionsResponse(BaseValidatorModel):
    VoiceConnectorRegions: List[VoiceConnectorAwsRegionType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_voice_connector_termination_credentials' function.
class ListVoiceConnectorTerminationCredentialsResponse(BaseValidatorModel):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_available_phone_numbers' function.
class SearchAvailablePhoneNumbersResponse(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'batch_update_phone_number' function.
class BatchUpdatePhoneNumberRequest(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItem]


class VoiceToneAnalysisTask(BaseValidatorModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetails] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None


# This class is the output for the 'validate_e911_address' function.
class ValidateE911AddressResponse(BaseValidatorModel):
    ValidationResult: int
    AddressExternalId: str
    Address: Address
    CandidateAddressList: List[CandidateAddress]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_proxy_session' function.
class CreateProxySessionRequest(BaseValidatorModel):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: List[str]
    Capabilities: List[CapabilityType]
    Name: Optional[str] = None
    ExpiryMinutes: Optional[int] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParams] = None


# This class is the output for the 'create_sip_media_application_call' function.
class CreateSipMediaApplicationCallResponse(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCall
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_sip_media_application_call' function.
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


# This class is the input for the 'update_sip_media_application' function.
class UpdateSipMediaApplicationRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    Name: Optional[str] = None
    Endpoints: Optional[List[SipMediaApplicationEndpoint]] = None


# This class is the input for the 'create_sip_media_application' function.
class CreateSipMediaApplicationRequest(BaseValidatorModel):
    AwsRegion: str
    Name: str
    Endpoints: List[SipMediaApplicationEndpoint]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_voice_connector' function.
class CreateVoiceConnectorRequest(BaseValidatorModel):
    Name: str
    RequireEncryption: bool
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Tags: Optional[List[Tag]] = None
    IntegrationType: Optional[VoiceConnectorIntegrationTypeType] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the input for the 'create_sip_rule' function.
class CreateSipRuleRequest(BaseValidatorModel):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[List[SipRuleTargetApplication]] = None


class SipRule(BaseValidatorModel):
    SipRuleId: Optional[str] = None
    Name: Optional[str] = None
    Disabled: Optional[bool] = None
    TriggerType: Optional[SipRuleTriggerTypeType] = None
    TriggerValue: Optional[str] = None
    TargetApplications: Optional[List[SipRuleTargetApplication]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


# This class is the input for the 'update_sip_rule' function.
class UpdateSipRuleRequest(BaseValidatorModel):
    SipRuleId: str
    Name: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[List[SipRuleTargetApplication]] = None


# This class is the input for the 'create_voice_connector_group' function.
class CreateVoiceConnectorGroupRequest(BaseValidatorModel):
    Name: str
    VoiceConnectorItems: Optional[List[VoiceConnectorItem]] = None


# This class is the input for the 'update_voice_connector_group' function.
class UpdateVoiceConnectorGroupRequest(BaseValidatorModel):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: List[VoiceConnectorItem]


class VoiceConnectorGroup(BaseValidatorModel):
    VoiceConnectorGroupId: Optional[str] = None
    Name: Optional[str] = None
    VoiceConnectorItems: Optional[List[VoiceConnectorItem]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorGroupArn: Optional[str] = None


# This class is the output for the 'create_voice_connector' function.
class CreateVoiceConnectorResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnector
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector' function.
class GetVoiceConnectorResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnector
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_voice_connectors' function.
class ListVoiceConnectorsResponse(BaseValidatorModel):
    VoiceConnectors: List[VoiceConnector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_voice_connector' function.
class UpdateVoiceConnectorResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnector
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_voice_profile_domain' function.
class CreateVoiceProfileDomainRequest(BaseValidatorModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfiguration
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class VoiceProfileDomain(BaseValidatorModel):
    VoiceProfileDomainId: Optional[str] = None
    VoiceProfileDomainArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


# This class is the output for the 'create_voice_profile' function.
class CreateVoiceProfileResponse(BaseValidatorModel):
    VoiceProfile: VoiceProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_profile' function.
class GetVoiceProfileResponse(BaseValidatorModel):
    VoiceProfile: VoiceProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_voice_profile' function.
class UpdateVoiceProfileResponse(BaseValidatorModel):
    VoiceProfile: VoiceProfile
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_voice_connector_termination_credentials' function.
class PutVoiceConnectorTerminationCredentialsRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Credentials: Optional[List[Credential]] = None


class EmergencyCallingConfigurationOutput(BaseValidatorModel):
    DNIS: Optional[List[DNISEmergencyCallingConfiguration]] = None


class EmergencyCallingConfiguration(BaseValidatorModel):
    DNIS: Optional[List[DNISEmergencyCallingConfiguration]] = None


# This class is the output for the 'get_voice_connector_external_systems_configuration' function.
class GetVoiceConnectorExternalSystemsConfigurationResponse(BaseValidatorModel):
    ExternalSystemsConfiguration: ExternalSystemsConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_voice_connector_external_systems_configuration' function.
class PutVoiceConnectorExternalSystemsConfigurationResponse(BaseValidatorModel):
    ExternalSystemsConfiguration: ExternalSystemsConfiguration
    ResponseMetadata: ResponseMetadata


class GetGlobalSettingsResponse(BaseValidatorModel):
    VoiceConnector: VoiceConnectorSettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_global_settings' function.
class UpdateGlobalSettingsRequest(BaseValidatorModel):
    VoiceConnector: Optional[VoiceConnectorSettings] = None


# This class is the output for the 'get_sip_media_application_alexa_skill_configuration' function.
class GetSipMediaApplicationAlexaSkillConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationAlexaSkillConfiguration: SipMediaApplicationAlexaSkillConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_sip_media_application_alexa_skill_configuration' function.
class PutSipMediaApplicationAlexaSkillConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationAlexaSkillConfiguration: SipMediaApplicationAlexaSkillConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sip_media_application_logging_configuration' function.
class GetSipMediaApplicationLoggingConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_sip_media_application_logging_configuration' function.
class PutSipMediaApplicationLoggingConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: Optional[SipMediaApplicationLoggingConfiguration] = None


# This class is the output for the 'put_sip_media_application_logging_configuration' function.
class PutSipMediaApplicationLoggingConfigurationResponse(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector_logging_configuration' function.
class GetVoiceConnectorLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_voice_connector_logging_configuration' function.
class PutVoiceConnectorLoggingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfiguration


# This class is the output for the 'put_voice_connector_logging_configuration' function.
class PutVoiceConnectorLoggingConfigurationResponse(BaseValidatorModel):
    LoggingConfiguration: LoggingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector_proxy' function.
class GetVoiceConnectorProxyResponse(BaseValidatorModel):
    Proxy: Proxy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_voice_connector_proxy' function.
class PutVoiceConnectorProxyResponse(BaseValidatorModel):
    Proxy: Proxy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector_termination_health' function.
class GetVoiceConnectorTerminationHealthResponse(BaseValidatorModel):
    TerminationHealth: TerminationHealth
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector_termination' function.
class GetVoiceConnectorTerminationResponse(BaseValidatorModel):
    Termination: TerminationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_voice_connector_termination' function.
class PutVoiceConnectorTerminationResponse(BaseValidatorModel):
    Termination: TerminationOutput
    ResponseMetadata: ResponseMetadata


class ListSipMediaApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSipRulesRequestPaginate(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_supported_phone_number_countries' function.
class ListSupportedPhoneNumberCountriesResponse(BaseValidatorModel):
    PhoneNumberCountries: List[PhoneNumberCountry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_voice_profile_domains' function.
class ListVoiceProfileDomainsResponse(BaseValidatorModel):
    VoiceProfileDomains: List[VoiceProfileDomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_voice_profiles' function.
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


class OriginationOutput(BaseValidatorModel):
    Routes: Optional[List[OriginationRoute]] = None
    Disabled: Optional[bool] = None


class Origination(BaseValidatorModel):
    Routes: Optional[List[OriginationRoute]] = None
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


class PhoneNumber(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    E164PhoneNumber: Optional[str] = None
    Country: Optional[str] = None
    Type: Optional[PhoneNumberTypeType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberStatusType] = None
    Capabilities: Optional[PhoneNumberCapabilities] = None
    Associations: Optional[List[PhoneNumberAssociation]] = None
    CallingName: Optional[str] = None
    CallingNameStatus: Optional[CallingNameStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    DeletionTimestamp: Optional[datetime] = None
    OrderId: Optional[str] = None
    Name: Optional[str] = None

SipMediaApplicationAlexaSkillConfigurationUnion = Union[SipMediaApplicationAlexaSkillConfiguration, SipMediaApplicationAlexaSkillConfigurationOutput]


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
    StreamingNotificationTargets: Optional[List[StreamingNotificationTarget]] = None
    MediaInsightsConfiguration: Optional[MediaInsightsConfiguration] = None

TerminationUnion = Union[Termination, TerminationOutput]


# This class is the output for the 'get_voice_tone_analysis_task' function.
class GetVoiceToneAnalysisTaskResponse(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_voice_tone_analysis_task' function.
class StartVoiceToneAnalysisTaskResponse(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_sip_media_application' function.
class CreateSipMediaApplicationResponse(BaseValidatorModel):
    SipMediaApplication: SipMediaApplication
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sip_media_application' function.
class GetSipMediaApplicationResponse(BaseValidatorModel):
    SipMediaApplication: SipMediaApplication
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_sip_media_applications' function.
class ListSipMediaApplicationsResponse(BaseValidatorModel):
    SipMediaApplications: List[SipMediaApplication]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_sip_media_application' function.
class UpdateSipMediaApplicationResponse(BaseValidatorModel):
    SipMediaApplication: SipMediaApplication
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_sip_rule' function.
class CreateSipRuleResponse(BaseValidatorModel):
    SipRule: SipRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sip_rule' function.
class GetSipRuleResponse(BaseValidatorModel):
    SipRule: SipRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_sip_rules' function.
class ListSipRulesResponse(BaseValidatorModel):
    SipRules: List[SipRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_sip_rule' function.
class UpdateSipRuleResponse(BaseValidatorModel):
    SipRule: SipRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_voice_connector_group' function.
class CreateVoiceConnectorGroupResponse(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector_group' function.
class GetVoiceConnectorGroupResponse(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_voice_connector_groups' function.
class ListVoiceConnectorGroupsResponse(BaseValidatorModel):
    VoiceConnectorGroups: List[VoiceConnectorGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_voice_connector_group' function.
class UpdateVoiceConnectorGroupResponse(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_voice_profile_domain' function.
class CreateVoiceProfileDomainResponse(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_profile_domain' function.
class GetVoiceProfileDomainResponse(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_voice_profile_domain' function.
class UpdateVoiceProfileDomainResponse(BaseValidatorModel):
    VoiceProfileDomain: VoiceProfileDomain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_voice_connector_emergency_calling_configuration' function.
class GetVoiceConnectorEmergencyCallingConfigurationResponse(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_voice_connector_emergency_calling_configuration' function.
class PutVoiceConnectorEmergencyCallingConfigurationResponse(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutput
    ResponseMetadata: ResponseMetadata

EmergencyCallingConfigurationUnion = Union[EmergencyCallingConfiguration, EmergencyCallingConfigurationOutput]


# This class is the output for the 'create_phone_number_order' function.
class CreatePhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_phone_number_order' function.
class GetPhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_phone_number_orders' function.
class ListPhoneNumberOrdersResponse(BaseValidatorModel):
    PhoneNumberOrders: List[PhoneNumberOrder]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_voice_connector_origination' function.
class GetVoiceConnectorOriginationResponse(BaseValidatorModel):
    Origination: OriginationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_voice_connector_origination' function.
class PutVoiceConnectorOriginationResponse(BaseValidatorModel):
    Origination: OriginationOutput
    ResponseMetadata: ResponseMetadata

OriginationUnion = Union[Origination, OriginationOutput]


# This class is the output for the 'create_proxy_session' function.
class CreateProxySessionResponse(BaseValidatorModel):
    ProxySession: ProxySession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_proxy_session' function.
class GetProxySessionResponse(BaseValidatorModel):
    ProxySession: ProxySession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_proxy_sessions' function.
class ListProxySessionsResponse(BaseValidatorModel):
    ProxySessions: List[ProxySession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_proxy_session' function.
class UpdateProxySessionResponse(BaseValidatorModel):
    ProxySession: ProxySession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_phone_number' function.
class GetPhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_phone_numbers' function.
class ListPhoneNumbersResponse(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'restore_phone_number' function.
class RestorePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_phone_number' function.
class UpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_sip_media_application_alexa_skill_configuration' function.
class PutSipMediaApplicationAlexaSkillConfigurationRequest(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationAlexaSkillConfiguration: Optional[SipMediaApplicationAlexaSkillConfigurationUnion] = None


class SpeakerSearchTask(BaseValidatorModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[str] = None
    CallDetails: Optional[CallDetails] = None
    SpeakerSearchDetails: Optional[SpeakerSearchDetails] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    StartedTimestamp: Optional[datetime] = None
    StatusMessage: Optional[str] = None


# This class is the output for the 'get_voice_connector_streaming_configuration' function.
class GetVoiceConnectorStreamingConfigurationResponse(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_voice_connector_streaming_configuration' function.
class PutVoiceConnectorStreamingConfigurationResponse(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationOutput
    ResponseMetadata: ResponseMetadata

StreamingConfigurationUnion = Union[StreamingConfiguration, StreamingConfigurationOutput]


# This class is the input for the 'put_voice_connector_termination' function.
class PutVoiceConnectorTerminationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Termination: TerminationUnion


# This class is the input for the 'put_voice_connector_emergency_calling_configuration' function.
class PutVoiceConnectorEmergencyCallingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationUnion


# This class is the input for the 'put_voice_connector_origination' function.
class PutVoiceConnectorOriginationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    Origination: OriginationUnion


# This class is the output for the 'get_speaker_search_task' function.
class GetSpeakerSearchTaskResponse(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_speaker_search_task' function.
class StartSpeakerSearchTaskResponse(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTask
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_voice_connector_streaming_configuration' function.
class PutVoiceConnectorStreamingConfigurationRequest(BaseValidatorModel):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationUnion