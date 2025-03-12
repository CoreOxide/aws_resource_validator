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
from aws_resource_validator.pydantic_models.pinpoint_constants import *

class ADMChannelRequestTypeDef(BaseValidatorModel):
    ClientId: str
    ClientSecret: str
    Enabled: Optional[bool] = None


class ADMChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class ADMMessageTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    ConsolidationKey: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    ExpiresAfter: Optional[str] = None
    IconReference: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    MD5: Optional[str] = None
    RawContent: Optional[str] = None
    SilentPush: Optional[bool] = None
    SmallImageIconUrl: Optional[str] = None
    Sound: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class APNSChannelRequestTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    HasTokenKey: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class APNSMessageTypeDef(BaseValidatorModel):
    APNSPushType: Optional[str] = None
    Action: Optional[ActionType] = None
    Badge: Optional[int] = None
    Body: Optional[str] = None
    Category: Optional[str] = None
    CollapseId: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    MediaUrl: Optional[str] = None
    PreferredAuthenticationMethod: Optional[str] = None
    Priority: Optional[str] = None
    RawContent: Optional[str] = None
    SilentPush: Optional[bool] = None
    Sound: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    ThreadId: Optional[str] = None
    TimeToLive: Optional[int] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class APNSPushNotificationTemplateTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    MediaUrl: Optional[str] = None
    RawContent: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class APNSSandboxChannelRequestTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSSandboxChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    HasTokenKey: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class APNSVoipChannelRequestTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSVoipChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    HasTokenKey: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class APNSVoipSandboxChannelRequestTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSVoipSandboxChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    HasTokenKey: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class ActivityResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    Id: str
    End: Optional[str] = None
    Result: Optional[str] = None
    ScheduledStart: Optional[str] = None
    Start: Optional[str] = None
    State: Optional[str] = None
    SuccessfulEndpointCount: Optional[int] = None
    TimezonesCompletedCount: Optional[int] = None
    TimezonesTotalCount: Optional[int] = None
    TotalEndpointCount: Optional[int] = None
    TreatmentId: Optional[str] = None
    ExecutionMetrics: Optional[Dict[str, str]] = None


class ContactCenterActivityTypeDef(BaseValidatorModel):
    NextActivity: Optional[str] = None


class HoldoutActivityTypeDef(BaseValidatorModel):
    Percentage: int
    NextActivity: Optional[str] = None


class AddressConfigurationTypeDef(BaseValidatorModel):
    BodyOverride: Optional[str] = None
    ChannelType: Optional[ChannelTypeType] = None
    Context: Optional[Mapping[str, str]] = None
    RawContent: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TitleOverride: Optional[str] = None


class AndroidPushNotificationTemplateTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    RawContent: Optional[str] = None
    SmallImageIconUrl: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class ApplicationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    tags: Optional[Dict[str, str]] = None
    CreationDate: Optional[str] = None


class JourneyTimeframeCapTypeDef(BaseValidatorModel):
    Cap: Optional[int] = None
    Days: Optional[int] = None


class CampaignHookTypeDef(BaseValidatorModel):
    LambdaFunctionName: Optional[str] = None
    Mode: Optional[ModeType] = None
    WebUrl: Optional[str] = None


class CampaignLimitsTypeDef(BaseValidatorModel):
    Daily: Optional[int] = None
    MaximumDuration: Optional[int] = None
    MessagesPerSecond: Optional[int] = None
    Total: Optional[int] = None
    Session: Optional[int] = None


class QuietTimeTypeDef(BaseValidatorModel):
    End: Optional[str] = None
    Start: Optional[str] = None


class AttributeDimensionOutputTypeDef(BaseValidatorModel):
    Values: List[str]
    AttributeType: Optional[AttributeTypeType] = None


class AttributeDimensionTypeDef(BaseValidatorModel):
    Values: Sequence[str]
    AttributeType: Optional[AttributeTypeType] = None


class AttributesResourceTypeDef(BaseValidatorModel):
    ApplicationId: str
    AttributeType: str
    Attributes: Optional[List[str]] = None


class BaiduChannelRequestTypeDef(BaseValidatorModel):
    ApiKey: str
    SecretKey: str
    Enabled: Optional[bool] = None


class BaiduChannelResponseTypeDef(BaseValidatorModel):
    Credential: str
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class BaiduMessageTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    IconReference: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    RawContent: Optional[str] = None
    SilentPush: Optional[bool] = None
    SmallImageIconUrl: Optional[str] = None
    Sound: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TimeToLive: Optional[int] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class CampaignCustomMessageTypeDef(BaseValidatorModel):
    Data: Optional[str] = None


class MessageHeaderTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class CampaignStateTypeDef(BaseValidatorModel):
    CampaignStatus: Optional[CampaignStatusType] = None


class CustomDeliveryConfigurationOutputTypeDef(BaseValidatorModel):
    DeliveryUri: str
    EndpointTypes: Optional[List[EndpointTypesElementType]] = None


class CampaignSmsMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None


class ChannelResponseTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class ClosedDaysRuleTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None


class WaitTimeTypeDef(BaseValidatorModel):
    WaitFor: Optional[str] = None
    WaitUntil: Optional[str] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    Name: str
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateTemplateMessageBodyTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None
    RequestID: Optional[str] = None


class ExportJobRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    S3UrlPrefix: str
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None


class ImportJobRequestTypeDef(BaseValidatorModel):
    Format: FormatType
    RoleArn: str
    S3Url: str
    DefineSegment: Optional[bool] = None
    ExternalId: Optional[str] = None
    RegisterEndpoints: Optional[bool] = None
    SegmentId: Optional[str] = None
    SegmentName: Optional[str] = None


class TemplateCreateMessageBodyTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None
    RequestID: Optional[str] = None


class CreateRecommenderConfigurationTypeDef(BaseValidatorModel):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Mapping[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None


class RecommenderConfigurationResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    Id: str
    LastModifiedDate: str
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Dict[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None


class SMSTemplateRequestTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None


class VoiceTemplateRequestTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    LanguageCode: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None
    VoiceId: Optional[str] = None


class CustomDeliveryConfigurationTypeDef(BaseValidatorModel):
    DeliveryUri: str
    EndpointTypes: Optional[Sequence[EndpointTypesElementType]] = None


class JourneyCustomMessageTypeDef(BaseValidatorModel):
    Data: Optional[str] = None


class DefaultMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None


class DefaultPushNotificationMessageTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    SilentPush: Optional[bool] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class DefaultPushNotificationTemplateTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class DeleteAdmChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsSandboxChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsVoipChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsVoipSandboxChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteAppRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteBaiduChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteCampaignRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str


class DeleteEmailChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class EmailChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    ConfigurationSet: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    FromAddress: Optional[str] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    Identity: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    MessagesPerSecond: Optional[int] = None
    RoleArn: Optional[str] = None
    OrchestrationSendingRoleArn: Optional[str] = None
    Version: Optional[int] = None


class DeleteEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class MessageBodyTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    RequestID: Optional[str] = None


class DeleteEndpointRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str


class DeleteEventStreamRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class EventStreamTypeDef(BaseValidatorModel):
    ApplicationId: str
    DestinationStreamArn: str
    RoleArn: str
    ExternalId: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    LastUpdatedBy: Optional[str] = None


class DeleteGcmChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GCMChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Credential: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    HasFcmServiceCredentials: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class DeleteInAppTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class DeleteJourneyRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str


class DeletePushTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class DeleteRecommenderConfigurationRequestTypeDef(BaseValidatorModel):
    RecommenderId: str


class DeleteSegmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str


class DeleteSmsChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class SMSChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    PromotionalMessagesPerSecond: Optional[int] = None
    SenderId: Optional[str] = None
    ShortCode: Optional[str] = None
    TransactionalMessagesPerSecond: Optional[int] = None
    Version: Optional[int] = None


class DeleteSmsTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class DeleteUserEndpointsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    UserId: str


class DeleteVoiceChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class VoiceChannelResponseTypeDef(BaseValidatorModel):
    Platform: str
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class DeleteVoiceTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GCMMessageTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    CollapseKey: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    IconReference: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    PreferredAuthenticationMethod: Optional[str] = None
    Priority: Optional[str] = None
    RawContent: Optional[str] = None
    RestrictedPackageName: Optional[str] = None
    SilentPush: Optional[bool] = None
    SmallImageIconUrl: Optional[str] = None
    Sound: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TimeToLive: Optional[int] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class SMSMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    Keyword: Optional[str] = None
    MediaUrl: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None


class VoiceMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    LanguageCode: Optional[str] = None
    OriginationNumber: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    VoiceId: Optional[str] = None


class EmailChannelRequestTypeDef(BaseValidatorModel):
    FromAddress: str
    Identity: str
    ConfigurationSet: Optional[str] = None
    Enabled: Optional[bool] = None
    RoleArn: Optional[str] = None
    OrchestrationSendingRoleArn: Optional[str] = None


class JourneyEmailMessageTypeDef(BaseValidatorModel):
    FromAddress: Optional[str] = None


class EndpointDemographicTypeDef(BaseValidatorModel):
    AppVersion: Optional[str] = None
    Locale: Optional[str] = None
    Make: Optional[str] = None
    Model: Optional[str] = None
    ModelVersion: Optional[str] = None
    Platform: Optional[str] = None
    PlatformVersion: Optional[str] = None
    Timezone: Optional[str] = None


class EndpointLocationTypeDef(BaseValidatorModel):
    City: Optional[str] = None
    Country: Optional[str] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    PostalCode: Optional[str] = None
    Region: Optional[str] = None


class EndpointItemResponseTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None


class EndpointMessageResultTypeDef(BaseValidatorModel):
    DeliveryStatus: DeliveryStatusType
    StatusCode: int
    Address: Optional[str] = None
    MessageId: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdatedToken: Optional[str] = None


class EndpointUserOutputTypeDef(BaseValidatorModel):
    UserAttributes: Optional[Dict[str, List[str]]] = None
    UserId: Optional[str] = None


class EndpointSendConfigurationTypeDef(BaseValidatorModel):
    BodyOverride: Optional[str] = None
    Context: Optional[Mapping[str, str]] = None
    RawContent: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TitleOverride: Optional[str] = None


class EndpointUserTypeDef(BaseValidatorModel):
    UserAttributes: Optional[Mapping[str, Sequence[str]]] = None
    UserId: Optional[str] = None


class MetricDimensionTypeDef(BaseValidatorModel):
    ComparisonOperator: str
    Value: float


class SetDimensionOutputTypeDef(BaseValidatorModel):
    Values: List[str]
    DimensionType: Optional[DimensionTypeType] = None


class EventItemResponseTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None


class SessionTypeDef(BaseValidatorModel):
    Id: str
    StartTimestamp: str
    Duration: Optional[int] = None
    StopTimestamp: Optional[str] = None


class ExportJobResourceTypeDef(BaseValidatorModel):
    RoleArn: str
    S3UrlPrefix: str
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None


class GCMChannelRequestTypeDef(BaseValidatorModel):
    ApiKey: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    ServiceJson: Optional[str] = None


class GPSCoordinatesTypeDef(BaseValidatorModel):
    Latitude: float
    Longitude: float


class GetAdmChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetApnsChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetApnsSandboxChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetApnsVoipChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetApnsVoipSandboxChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetAppRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetApplicationSettingsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetAppsRequestTypeDef(BaseValidatorModel):
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetBaiduChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetCampaignActivitiesRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetCampaignRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str


class GetCampaignVersionRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    Version: str


class GetCampaignVersionsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetCampaignsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetChannelsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetEmailChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetEmailTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GetEndpointRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str


class GetEventStreamRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetExportJobRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JobId: str


class GetExportJobsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetGcmChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetImportJobRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JobId: str


class GetImportJobsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetInAppMessagesRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str


class GetInAppTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GetJourneyExecutionActivityMetricsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyExecutionActivityMetricsResponseTypeDef(BaseValidatorModel):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]


class GetJourneyExecutionMetricsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyExecutionMetricsResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]


class GetJourneyRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str


class GetJourneyRunExecutionActivityMetricsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    RunId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyRunExecutionActivityMetricsResponseTypeDef(BaseValidatorModel):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]
    RunId: str


class GetJourneyRunExecutionMetricsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    RunId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyRunExecutionMetricsResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]
    RunId: str


class GetJourneyRunsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetPushTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GetRecommenderConfigurationRequestTypeDef(BaseValidatorModel):
    RecommenderId: str


class GetRecommenderConfigurationsRequestTypeDef(BaseValidatorModel):
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentExportJobsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentImportJobsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str


class GetSegmentVersionRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    Version: str


class GetSegmentVersionsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSmsChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetSmsTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class SMSTemplateResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class GetUserEndpointsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    UserId: str


class GetVoiceChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetVoiceTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class VoiceTemplateResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    LanguageCode: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None
    VoiceId: Optional[str] = None


class ImportJobResourceTypeDef(BaseValidatorModel):
    Format: FormatType
    RoleArn: str
    S3Url: str
    DefineSegment: Optional[bool] = None
    ExternalId: Optional[str] = None
    RegisterEndpoints: Optional[bool] = None
    SegmentId: Optional[str] = None
    SegmentName: Optional[str] = None


class InAppMessageBodyConfigTypeDef(BaseValidatorModel):
    Alignment: AlignmentType
    Body: str
    TextColor: str


class OverrideButtonConfigurationTypeDef(BaseValidatorModel):
    ButtonAction: ButtonActionType
    Link: Optional[str] = None


class InAppMessageHeaderConfigTypeDef(BaseValidatorModel):
    Alignment: AlignmentType
    Header: str
    TextColor: str


class JourneyChannelSettingsTypeDef(BaseValidatorModel):
    ConnectCampaignArn: Optional[str] = None
    ConnectCampaignExecutionRoleArn: Optional[str] = None


class JourneyPushMessageTypeDef(BaseValidatorModel):
    TimeToLive: Optional[str] = None


class JourneyScheduleOutputTypeDef(BaseValidatorModel):
    EndTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    Timezone: Optional[str] = None


class JourneyRunResponseTypeDef(BaseValidatorModel):
    CreationTime: str
    LastUpdateTime: str
    RunId: str
    Status: JourneyRunStatusType


class JourneySMSMessageTypeDef(BaseValidatorModel):
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None


class JourneyStateRequestTypeDef(BaseValidatorModel):
    State: Optional[StateType] = None


class ListJourneysRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagsModelOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]


class ListTemplateVersionsRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    TemplateType: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class ListTemplatesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    Prefix: Optional[str] = None
    TemplateType: Optional[str] = None


class MessageTypeDef(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageSmallIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    JsonBody: Optional[str] = None
    MediaUrl: Optional[str] = None
    RawContent: Optional[str] = None
    SilentPush: Optional[bool] = None
    TimeToLive: Optional[int] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class MessageResultTypeDef(BaseValidatorModel):
    DeliveryStatus: DeliveryStatusType
    StatusCode: int
    MessageId: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdatedToken: Optional[str] = None


class NumberValidateRequestTypeDef(BaseValidatorModel):
    IsoCountryCode: Optional[str] = None
    PhoneNumber: Optional[str] = None


class NumberValidateResponseTypeDef(BaseValidatorModel):
    Carrier: Optional[str] = None
    City: Optional[str] = None
    CleansedPhoneNumberE164: Optional[str] = None
    CleansedPhoneNumberNational: Optional[str] = None
    Country: Optional[str] = None
    CountryCodeIso2: Optional[str] = None
    CountryCodeNumeric: Optional[str] = None
    County: Optional[str] = None
    OriginalCountryCodeIso2: Optional[str] = None
    OriginalPhoneNumber: Optional[str] = None
    PhoneType: Optional[str] = None
    PhoneTypeCode: Optional[int] = None
    Timezone: Optional[str] = None
    ZipCode: Optional[str] = None


class OpenHoursRuleTypeDef(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None


class WriteEventStreamTypeDef(BaseValidatorModel):
    DestinationStreamArn: str
    RoleArn: str


class RandomSplitEntryTypeDef(BaseValidatorModel):
    NextActivity: Optional[str] = None
    Percentage: Optional[int] = None


class RecencyDimensionTypeDef(BaseValidatorModel):
    Duration: DurationType
    RecencyType: RecencyTypeType


class UpdateAttributesRequestTypeDef(BaseValidatorModel):
    Blacklist: Optional[Sequence[str]] = None


class SMSChannelRequestTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SenderId: Optional[str] = None
    ShortCode: Optional[str] = None


class SegmentConditionTypeDef(BaseValidatorModel):
    SegmentId: str


class SegmentReferenceTypeDef(BaseValidatorModel):
    Id: str
    Version: Optional[int] = None


class SegmentImportResourceTypeDef(BaseValidatorModel):
    ExternalId: str
    Format: FormatType
    RoleArn: str
    S3Url: str
    Size: int
    ChannelCounts: Optional[Dict[str, int]] = None


class SendOTPMessageRequestParametersTypeDef(BaseValidatorModel):
    BrandName: str
    Channel: str
    DestinationIdentity: str
    OriginationIdentity: str
    ReferenceId: str
    AllowedAttempts: Optional[int] = None
    CodeLength: Optional[int] = None
    EntityId: Optional[str] = None
    Language: Optional[str] = None
    TemplateId: Optional[str] = None
    ValidityPeriod: Optional[int] = None


class SetDimensionTypeDef(BaseValidatorModel):
    Values: Sequence[str]
    DimensionType: Optional[DimensionTypeType] = None


class SimpleEmailPartTypeDef(BaseValidatorModel):
    Charset: Optional[str] = None
    Data: Optional[str] = None


class TagsModelTypeDef(BaseValidatorModel):
    tags: Mapping[str, str]


class TemplateActiveVersionRequestTypeDef(BaseValidatorModel):
    Version: Optional[str] = None


class TemplateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class TemplateResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class TemplateVersionResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: str
    DefaultSubstitutions: Optional[str] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateRecommenderConfigurationTypeDef(BaseValidatorModel):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Mapping[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None


class VoiceChannelRequestTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None


class VerificationResponseTypeDef(BaseValidatorModel):
    Valid: Optional[bool] = None


class VerifyOTPMessageRequestParametersTypeDef(BaseValidatorModel):
    DestinationIdentity: str
    Otp: str
    ReferenceId: str


class UpdateAdmChannelRequestTypeDef(BaseValidatorModel):
    ADMChannelRequest: ADMChannelRequestTypeDef
    ApplicationId: str


class UpdateApnsChannelRequestTypeDef(BaseValidatorModel):
    APNSChannelRequest: APNSChannelRequestTypeDef
    ApplicationId: str


class UpdateApnsSandboxChannelRequestTypeDef(BaseValidatorModel):
    APNSSandboxChannelRequest: APNSSandboxChannelRequestTypeDef
    ApplicationId: str


class UpdateApnsVoipChannelRequestTypeDef(BaseValidatorModel):
    APNSVoipChannelRequest: APNSVoipChannelRequestTypeDef
    ApplicationId: str


class UpdateApnsVoipSandboxChannelRequestTypeDef(BaseValidatorModel):
    APNSVoipSandboxChannelRequest: APNSVoipSandboxChannelRequestTypeDef
    ApplicationId: str


class ActivitiesResponseTypeDef(BaseValidatorModel):
    Item: List[ActivityResponseTypeDef]
    NextToken: Optional[str] = None


class ApplicationsResponseTypeDef(BaseValidatorModel):
    Item: Optional[List[ApplicationResponseTypeDef]] = None
    NextToken: Optional[str] = None


class ApplicationSettingsJourneyLimitsTypeDef(BaseValidatorModel):
    DailyCap: Optional[int] = None
    TimeframeCap: Optional[JourneyTimeframeCapTypeDef] = None
    TotalCap: Optional[int] = None


class JourneyLimitsTypeDef(BaseValidatorModel):
    DailyCap: Optional[int] = None
    EndpointReentryCap: Optional[int] = None
    MessagesPerSecond: Optional[int] = None
    EndpointReentryInterval: Optional[str] = None
    TimeframeCap: Optional[JourneyTimeframeCapTypeDef] = None
    TotalCap: Optional[int] = None


class UpdateBaiduChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    BaiduChannelRequest: BaiduChannelRequestTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class RawEmailTypeDef(BaseValidatorModel):
    Data: Optional[BlobTypeDef] = None


class CampaignEmailMessageOutputTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    FromAddress: Optional[str] = None
    Headers: Optional[List[MessageHeaderTypeDef]] = None
    HtmlBody: Optional[str] = None
    Title: Optional[str] = None


class CampaignEmailMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    FromAddress: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None
    HtmlBody: Optional[str] = None
    Title: Optional[str] = None


class EmailTemplateRequestTypeDef(BaseValidatorModel):
    DefaultSubstitutions: Optional[str] = None
    HtmlPart: Optional[str] = None
    RecommenderId: Optional[str] = None
    Subject: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None
    TextPart: Optional[str] = None


class EmailTemplateResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    HtmlPart: Optional[str] = None
    RecommenderId: Optional[str] = None
    Subject: Optional[str] = None
    Headers: Optional[List[MessageHeaderTypeDef]] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    TextPart: Optional[str] = None
    Version: Optional[str] = None


class ChannelsResponseTypeDef(BaseValidatorModel):
    Channels: Dict[str, ChannelResponseTypeDef]


class ClosedDaysOutputTypeDef(BaseValidatorModel):
    EMAIL: Optional[List[ClosedDaysRuleTypeDef]] = None
    SMS: Optional[List[ClosedDaysRuleTypeDef]] = None
    PUSH: Optional[List[ClosedDaysRuleTypeDef]] = None
    VOICE: Optional[List[ClosedDaysRuleTypeDef]] = None
    CUSTOM: Optional[List[ClosedDaysRuleTypeDef]] = None


class ClosedDaysTypeDef(BaseValidatorModel):
    EMAIL: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    SMS: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    PUSH: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    VOICE: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    CUSTOM: Optional[Sequence[ClosedDaysRuleTypeDef]] = None


class WaitActivityTypeDef(BaseValidatorModel):
    NextActivity: Optional[str] = None
    WaitTime: Optional[WaitTimeTypeDef] = None


class CreateAppRequestTypeDef(BaseValidatorModel):
    CreateApplicationRequest: CreateApplicationRequestTypeDef


class CreateAppResponseTypeDef(BaseValidatorModel):
    ApplicationResponse: ApplicationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAdmChannelResponseTypeDef(BaseValidatorModel):
    ADMChannelResponse: ADMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteApnsChannelResponseTypeDef(BaseValidatorModel):
    APNSChannelResponse: APNSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteApnsSandboxChannelResponseTypeDef(BaseValidatorModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteApnsVoipChannelResponseTypeDef(BaseValidatorModel):
    APNSVoipChannelResponse: APNSVoipChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteApnsVoipSandboxChannelResponseTypeDef(BaseValidatorModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAppResponseTypeDef(BaseValidatorModel):
    ApplicationResponse: ApplicationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBaiduChannelResponseTypeDef(BaseValidatorModel):
    BaiduChannelResponse: BaiduChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAdmChannelResponseTypeDef(BaseValidatorModel):
    ADMChannelResponse: ADMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApnsChannelResponseTypeDef(BaseValidatorModel):
    APNSChannelResponse: APNSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApnsSandboxChannelResponseTypeDef(BaseValidatorModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApnsVoipChannelResponseTypeDef(BaseValidatorModel):
    APNSVoipChannelResponse: APNSVoipChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApnsVoipSandboxChannelResponseTypeDef(BaseValidatorModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppResponseTypeDef(BaseValidatorModel):
    ApplicationResponse: ApplicationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBaiduChannelResponseTypeDef(BaseValidatorModel):
    BaiduChannelResponse: BaiduChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveAttributesResponseTypeDef(BaseValidatorModel):
    AttributesResource: AttributesResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAdmChannelResponseTypeDef(BaseValidatorModel):
    ADMChannelResponse: ADMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApnsChannelResponseTypeDef(BaseValidatorModel):
    APNSChannelResponse: APNSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApnsSandboxChannelResponseTypeDef(BaseValidatorModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApnsVoipChannelResponseTypeDef(BaseValidatorModel):
    APNSVoipChannelResponse: APNSVoipChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApnsVoipSandboxChannelResponseTypeDef(BaseValidatorModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBaiduChannelResponseTypeDef(BaseValidatorModel):
    BaiduChannelResponse: BaiduChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEmailTemplateResponseTypeDef(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePushTemplateResponseTypeDef(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSmsTemplateResponseTypeDef(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVoiceTemplateResponseTypeDef(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateExportJobRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ExportJobRequest: ExportJobRequestTypeDef


class CreateImportJobRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ImportJobRequest: ImportJobRequestTypeDef


class CreateInAppTemplateResponseTypeDef(BaseValidatorModel):
    TemplateCreateMessageBody: TemplateCreateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRecommenderConfigurationRequestTypeDef(BaseValidatorModel):
    CreateRecommenderConfiguration: CreateRecommenderConfigurationTypeDef


class CreateRecommenderConfigurationResponseTypeDef(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRecommenderConfigurationResponseTypeDef(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRecommenderConfigurationResponseTypeDef(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecommenderConfigurationsResponseTypeDef(BaseValidatorModel):
    Item: List[RecommenderConfigurationResponseTypeDef]
    NextToken: Optional[str] = None


class UpdateRecommenderConfigurationResponseTypeDef(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSmsTemplateRequestTypeDef(BaseValidatorModel):
    SMSTemplateRequest: SMSTemplateRequestTypeDef
    TemplateName: str


class UpdateSmsTemplateRequestTypeDef(BaseValidatorModel):
    SMSTemplateRequest: SMSTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class CreateVoiceTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    VoiceTemplateRequest: VoiceTemplateRequestTypeDef


class UpdateVoiceTemplateRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    VoiceTemplateRequest: VoiceTemplateRequestTypeDef
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class CustomMessageActivityOutputTypeDef(BaseValidatorModel):
    DeliveryUri: Optional[str] = None
    EndpointTypes: Optional[List[EndpointTypesElementType]] = None
    MessageConfig: Optional[JourneyCustomMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class CustomMessageActivityTypeDef(BaseValidatorModel):
    DeliveryUri: Optional[str] = None
    EndpointTypes: Optional[Sequence[EndpointTypesElementType]] = None
    MessageConfig: Optional[JourneyCustomMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class PushNotificationTemplateRequestTypeDef(BaseValidatorModel):
    ADM: Optional[AndroidPushNotificationTemplateTypeDef] = None
    APNS: Optional[APNSPushNotificationTemplateTypeDef] = None
    Baidu: Optional[AndroidPushNotificationTemplateTypeDef] = None
    Default: Optional[DefaultPushNotificationTemplateTypeDef] = None
    DefaultSubstitutions: Optional[str] = None
    GCM: Optional[AndroidPushNotificationTemplateTypeDef] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None


class PushNotificationTemplateResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    ADM: Optional[AndroidPushNotificationTemplateTypeDef] = None
    APNS: Optional[APNSPushNotificationTemplateTypeDef] = None
    Arn: Optional[str] = None
    Baidu: Optional[AndroidPushNotificationTemplateTypeDef] = None
    Default: Optional[DefaultPushNotificationTemplateTypeDef] = None
    DefaultSubstitutions: Optional[str] = None
    GCM: Optional[AndroidPushNotificationTemplateTypeDef] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class DeleteEmailChannelResponseTypeDef(BaseValidatorModel):
    EmailChannelResponse: EmailChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetEmailChannelResponseTypeDef(BaseValidatorModel):
    EmailChannelResponse: EmailChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEmailChannelResponseTypeDef(BaseValidatorModel):
    EmailChannelResponse: EmailChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEmailTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInAppTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePushTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSmsTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVoiceTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEmailTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEndpointResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEndpointsBatchResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateInAppTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePushTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSmsTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTemplateActiveVersionResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVoiceTemplateResponseTypeDef(BaseValidatorModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEventStreamResponseTypeDef(BaseValidatorModel):
    EventStream: EventStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventStreamResponseTypeDef(BaseValidatorModel):
    EventStream: EventStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutEventStreamResponseTypeDef(BaseValidatorModel):
    EventStream: EventStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteGcmChannelResponseTypeDef(BaseValidatorModel):
    GCMChannelResponse: GCMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetGcmChannelResponseTypeDef(BaseValidatorModel):
    GCMChannelResponse: GCMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGcmChannelResponseTypeDef(BaseValidatorModel):
    GCMChannelResponse: GCMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSmsChannelResponseTypeDef(BaseValidatorModel):
    SMSChannelResponse: SMSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSmsChannelResponseTypeDef(BaseValidatorModel):
    SMSChannelResponse: SMSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSmsChannelResponseTypeDef(BaseValidatorModel):
    SMSChannelResponse: SMSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVoiceChannelResponseTypeDef(BaseValidatorModel):
    VoiceChannelResponse: VoiceChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetVoiceChannelResponseTypeDef(BaseValidatorModel):
    VoiceChannelResponse: VoiceChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVoiceChannelResponseTypeDef(BaseValidatorModel):
    VoiceChannelResponse: VoiceChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEmailChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EmailChannelRequest: EmailChannelRequestTypeDef


class EmailMessageActivityTypeDef(BaseValidatorModel):
    MessageConfig: Optional[JourneyEmailMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class SendUsersMessageResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    RequestId: Optional[str] = None
    Result: Optional[Dict[str, Dict[str, EndpointMessageResultTypeDef]]] = None


class EndpointResponseTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    ApplicationId: Optional[str] = None
    Attributes: Optional[Dict[str, List[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    CohortId: Optional[str] = None
    CreationDate: Optional[str] = None
    Demographic: Optional[EndpointDemographicTypeDef] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Id: Optional[str] = None
    Location: Optional[EndpointLocationTypeDef] = None
    Metrics: Optional[Dict[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserOutputTypeDef] = None


class EventDimensionsOutputTypeDef(BaseValidatorModel):
    Attributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None
    EventType: Optional[SetDimensionOutputTypeDef] = None
    Metrics: Optional[Dict[str, MetricDimensionTypeDef]] = None


class SegmentDemographicsOutputTypeDef(BaseValidatorModel):
    AppVersion: Optional[SetDimensionOutputTypeDef] = None
    Channel: Optional[SetDimensionOutputTypeDef] = None
    DeviceType: Optional[SetDimensionOutputTypeDef] = None
    Make: Optional[SetDimensionOutputTypeDef] = None
    Model: Optional[SetDimensionOutputTypeDef] = None
    Platform: Optional[SetDimensionOutputTypeDef] = None


class ItemResponseTypeDef(BaseValidatorModel):
    EndpointItemResponse: Optional[EndpointItemResponseTypeDef] = None
    EventsItemResponse: Optional[Dict[str, EventItemResponseTypeDef]] = None


class EventTypeDef(BaseValidatorModel):
    EventType: str
    Timestamp: str
    AppPackageName: Optional[str] = None
    AppTitle: Optional[str] = None
    AppVersionCode: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    ClientSdkVersion: Optional[str] = None
    Metrics: Optional[Mapping[str, float]] = None
    SdkName: Optional[str] = None
    Session: Optional[SessionTypeDef] = None


class UpdateGcmChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    GCMChannelRequest: GCMChannelRequestTypeDef


class GPSPointDimensionTypeDef(BaseValidatorModel):
    Coordinates: GPSCoordinatesTypeDef
    RangeInKilometers: Optional[float] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetApplicationDateRangeKpiRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    KpiName: str
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None


class GetCampaignDateRangeKpiRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    KpiName: str
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None


class GetJourneyDateRangeKpiRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    KpiName: str
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None


class JourneyScheduleTypeDef(BaseValidatorModel):
    EndTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Timezone: Optional[str] = None


class GetJourneyExecutionActivityMetricsResponseTypeDef(BaseValidatorModel):
    JourneyExecutionActivityMetricsResponse: JourneyExecutionActivityMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJourneyExecutionMetricsResponseTypeDef(BaseValidatorModel):
    JourneyExecutionMetricsResponse: JourneyExecutionMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJourneyRunExecutionActivityMetricsResponseTypeDef(BaseValidatorModel):
    JourneyRunExecutionActivityMetricsResponse: JourneyRunExecutionActivityMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJourneyRunExecutionMetricsResponseTypeDef(BaseValidatorModel):
    JourneyRunExecutionMetricsResponse: JourneyRunExecutionMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSmsTemplateResponseTypeDef(BaseValidatorModel):
    SMSTemplateResponse: SMSTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetVoiceTemplateResponseTypeDef(BaseValidatorModel):
    VoiceTemplateResponse: VoiceTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DefaultButtonConfigurationTypeDef(BaseValidatorModel):
    pass


class InAppMessageButtonTypeDef(BaseValidatorModel):
    Android: Optional[OverrideButtonConfigurationTypeDef] = None
    DefaultConfig: Optional[DefaultButtonConfigurationTypeDef] = None
    IOS: Optional[OverrideButtonConfigurationTypeDef] = None
    Web: Optional[OverrideButtonConfigurationTypeDef] = None


class PushMessageActivityTypeDef(BaseValidatorModel):
    MessageConfig: Optional[JourneyPushMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class JourneyRunsResponseTypeDef(BaseValidatorModel):
    Item: List[JourneyRunResponseTypeDef]
    NextToken: Optional[str] = None


class SMSMessageActivityTypeDef(BaseValidatorModel):
    MessageConfig: Optional[JourneySMSMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class UpdateJourneyStateRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    JourneyStateRequest: JourneyStateRequestTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    TagsModel: TagsModelOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MessageResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndpointResult: Optional[Dict[str, EndpointMessageResultTypeDef]] = None
    RequestId: Optional[str] = None
    Result: Optional[Dict[str, MessageResultTypeDef]] = None


class PhoneNumberValidateRequestTypeDef(BaseValidatorModel):
    NumberValidateRequest: NumberValidateRequestTypeDef


class PhoneNumberValidateResponseTypeDef(BaseValidatorModel):
    NumberValidateResponse: NumberValidateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OpenHoursOutputTypeDef(BaseValidatorModel):
    EMAIL: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    SMS: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    PUSH: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    VOICE: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    CUSTOM: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None


class OpenHoursTypeDef(BaseValidatorModel):
    EMAIL: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    SMS: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    PUSH: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    VOICE: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    CUSTOM: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None


class PutEventStreamRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    WriteEventStream: WriteEventStreamTypeDef


class RandomSplitActivityOutputTypeDef(BaseValidatorModel):
    Branches: Optional[List[RandomSplitEntryTypeDef]] = None


class RandomSplitActivityTypeDef(BaseValidatorModel):
    Branches: Optional[Sequence[RandomSplitEntryTypeDef]] = None


class SegmentBehaviorsTypeDef(BaseValidatorModel):
    Recency: Optional[RecencyDimensionTypeDef] = None


class RemoveAttributesRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    AttributeType: str
    UpdateAttributesRequest: UpdateAttributesRequestTypeDef


class ResultRowValueTypeDef(BaseValidatorModel):
    pass


class ResultRowTypeDef(BaseValidatorModel):
    GroupedBys: List[ResultRowValueTypeDef]
    Values: List[ResultRowValueTypeDef]


class UpdateSmsChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SMSChannelRequest: SMSChannelRequestTypeDef


class SendOTPMessageRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SendOTPMessageRequestParameters: SendOTPMessageRequestParametersTypeDef


class SimpleEmailTypeDef(BaseValidatorModel):
    HtmlPart: Optional[SimpleEmailPartTypeDef] = None
    Subject: Optional[SimpleEmailPartTypeDef] = None
    TextPart: Optional[SimpleEmailPartTypeDef] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None


class UpdateTemplateActiveVersionRequestTypeDef(BaseValidatorModel):
    TemplateActiveVersionRequest: TemplateActiveVersionRequestTypeDef
    TemplateName: str
    TemplateType: str


class TemplateConfigurationTypeDef(BaseValidatorModel):
    EmailTemplate: Optional[TemplateTypeDef] = None
    PushTemplate: Optional[TemplateTypeDef] = None
    SMSTemplate: Optional[TemplateTypeDef] = None
    VoiceTemplate: Optional[TemplateTypeDef] = None
    InAppTemplate: Optional[TemplateTypeDef] = None


class TemplatesResponseTypeDef(BaseValidatorModel):
    Item: List[TemplateResponseTypeDef]
    NextToken: Optional[str] = None


class TemplateVersionsResponseTypeDef(BaseValidatorModel):
    Item: List[TemplateVersionResponseTypeDef]
    Message: Optional[str] = None
    NextToken: Optional[str] = None
    RequestID: Optional[str] = None


class UpdateRecommenderConfigurationRequestTypeDef(BaseValidatorModel):
    RecommenderId: str
    UpdateRecommenderConfiguration: UpdateRecommenderConfigurationTypeDef


class UpdateVoiceChannelRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    VoiceChannelRequest: VoiceChannelRequestTypeDef


class VerifyOTPMessageResponseTypeDef(BaseValidatorModel):
    VerificationResponse: VerificationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class VerifyOTPMessageRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    VerifyOTPMessageRequestParameters: VerifyOTPMessageRequestParametersTypeDef


class GetCampaignActivitiesResponseTypeDef(BaseValidatorModel):
    ActivitiesResponse: ActivitiesResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppsResponseTypeDef(BaseValidatorModel):
    ApplicationsResponse: ApplicationsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApplicationSettingsResourceTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignHook: Optional[CampaignHookTypeDef] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    JourneyLimits: Optional[ApplicationSettingsJourneyLimitsTypeDef] = None


class WriteApplicationSettingsRequestTypeDef(BaseValidatorModel):
    CampaignHook: Optional[CampaignHookTypeDef] = None
    CloudWatchMetricsEnabled: Optional[bool] = None
    EventTaggingEnabled: Optional[bool] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    JourneyLimits: Optional[ApplicationSettingsJourneyLimitsTypeDef] = None


class CreateEmailTemplateRequestTypeDef(BaseValidatorModel):
    EmailTemplateRequest: EmailTemplateRequestTypeDef
    TemplateName: str


class UpdateEmailTemplateRequestTypeDef(BaseValidatorModel):
    EmailTemplateRequest: EmailTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class GetEmailTemplateResponseTypeDef(BaseValidatorModel):
    EmailTemplateResponse: EmailTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetChannelsResponseTypeDef(BaseValidatorModel):
    ChannelsResponse: ChannelsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRecommenderConfigurationsResponseTypeDef(BaseValidatorModel):
    ListRecommenderConfigurationsResponse: ListRecommenderConfigurationsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePushTemplateRequestTypeDef(BaseValidatorModel):
    PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef
    TemplateName: str


class UpdatePushTemplateRequestTypeDef(BaseValidatorModel):
    PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class GetPushTemplateResponseTypeDef(BaseValidatorModel):
    PushNotificationTemplateResponse: PushNotificationTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SendUsersMessagesResponseTypeDef(BaseValidatorModel):
    SendUsersMessageResponse: SendUsersMessageResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEndpointResponseTypeDef(BaseValidatorModel):
    EndpointResponse: EndpointResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointsResponseTypeDef(BaseValidatorModel):
    Item: List[EndpointResponseTypeDef]


class GetEndpointResponseTypeDef(BaseValidatorModel):
    EndpointResponse: EndpointResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointUserUnionTypeDef(BaseValidatorModel):
    pass


class EndpointBatchItemTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Attributes: Optional[Mapping[str, Sequence[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    Demographic: Optional[EndpointDemographicTypeDef] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Id: Optional[str] = None
    Location: Optional[EndpointLocationTypeDef] = None
    Metrics: Optional[Mapping[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserUnionTypeDef] = None


class EndpointRequestTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Attributes: Optional[Mapping[str, Sequence[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    Demographic: Optional[EndpointDemographicTypeDef] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Location: Optional[EndpointLocationTypeDef] = None
    Metrics: Optional[Mapping[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserUnionTypeDef] = None


class PublicEndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Attributes: Optional[Mapping[str, Sequence[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    Demographic: Optional[EndpointDemographicTypeDef] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Location: Optional[EndpointLocationTypeDef] = None
    Metrics: Optional[Mapping[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserUnionTypeDef] = None


class CampaignEventFilterOutputTypeDef(BaseValidatorModel):
    Dimensions: EventDimensionsOutputTypeDef
    FilterType: FilterTypeType


class EventConditionOutputTypeDef(BaseValidatorModel):
    Dimensions: Optional[EventDimensionsOutputTypeDef] = None
    MessageActivity: Optional[str] = None


class EventFilterOutputTypeDef(BaseValidatorModel):
    Dimensions: EventDimensionsOutputTypeDef
    FilterType: FilterTypeType


class EventsResponseTypeDef(BaseValidatorModel):
    Results: Optional[Dict[str, ItemResponseTypeDef]] = None


class ExportJobResponseTypeDef(BaseValidatorModel):
    pass


class CreateExportJobResponseTypeDef(BaseValidatorModel):
    ExportJobResponse: ExportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportJobsResponseTypeDef(BaseValidatorModel):
    Item: List[ExportJobResponseTypeDef]
    NextToken: Optional[str] = None


class GetExportJobResponseTypeDef(BaseValidatorModel):
    ExportJobResponse: ExportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SegmentLocationOutputTypeDef(BaseValidatorModel):
    Country: Optional[SetDimensionOutputTypeDef] = None
    GPSPoint: Optional[GPSPointDimensionTypeDef] = None


class ImportJobResponseTypeDef(BaseValidatorModel):
    pass


class CreateImportJobResponseTypeDef(BaseValidatorModel):
    ImportJobResponse: ImportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetImportJobResponseTypeDef(BaseValidatorModel):
    ImportJobResponse: ImportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImportJobsResponseTypeDef(BaseValidatorModel):
    Item: List[ImportJobResponseTypeDef]
    NextToken: Optional[str] = None


class InAppMessageContentTypeDef(BaseValidatorModel):
    BackgroundColor: Optional[str] = None
    BodyConfig: Optional[InAppMessageBodyConfigTypeDef] = None
    HeaderConfig: Optional[InAppMessageHeaderConfigTypeDef] = None
    ImageUrl: Optional[str] = None
    PrimaryBtn: Optional[InAppMessageButtonTypeDef] = None
    SecondaryBtn: Optional[InAppMessageButtonTypeDef] = None


class GetJourneyRunsResponseTypeDef(BaseValidatorModel):
    JourneyRunsResponse: JourneyRunsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SendMessagesResponseTypeDef(BaseValidatorModel):
    MessageResponse: MessageResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SendOTPMessageResponseTypeDef(BaseValidatorModel):
    MessageResponse: MessageResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BaseKpiResultTypeDef(BaseValidatorModel):
    Rows: List[ResultRowTypeDef]


class AttributeDimensionUnionTypeDef(BaseValidatorModel):
    pass


class SetDimensionUnionTypeDef(BaseValidatorModel):
    pass


class EventDimensionsTypeDef(BaseValidatorModel):
    Attributes: Optional[Mapping[str, AttributeDimensionUnionTypeDef]] = None
    EventType: Optional[SetDimensionUnionTypeDef] = None
    Metrics: Optional[Mapping[str, MetricDimensionTypeDef]] = None


class SegmentDemographicsTypeDef(BaseValidatorModel):
    AppVersion: Optional[SetDimensionUnionTypeDef] = None
    Channel: Optional[SetDimensionUnionTypeDef] = None
    DeviceType: Optional[SetDimensionUnionTypeDef] = None
    Make: Optional[SetDimensionUnionTypeDef] = None
    Model: Optional[SetDimensionUnionTypeDef] = None
    Platform: Optional[SetDimensionUnionTypeDef] = None


class SegmentLocationTypeDef(BaseValidatorModel):
    Country: Optional[SetDimensionUnionTypeDef] = None
    GPSPoint: Optional[GPSPointDimensionTypeDef] = None


class EmailMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    FeedbackForwardingAddress: Optional[str] = None
    FromAddress: Optional[str] = None
    RawEmail: Optional[RawEmailTypeDef] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    SimpleEmail: Optional[SimpleEmailTypeDef] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None


class TagsModelUnionTypeDef(BaseValidatorModel):
    pass


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagsModel: TagsModelUnionTypeDef


class ListTemplatesResponseTypeDef(BaseValidatorModel):
    TemplatesResponse: TemplatesResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTemplateVersionsResponseTypeDef(BaseValidatorModel):
    TemplateVersionsResponse: TemplateVersionsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationSettingsResponseTypeDef(BaseValidatorModel):
    ApplicationSettingsResource: ApplicationSettingsResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApplicationSettingsResponseTypeDef(BaseValidatorModel):
    ApplicationSettingsResource: ApplicationSettingsResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApplicationSettingsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    WriteApplicationSettingsRequest: WriteApplicationSettingsRequestTypeDef


class DeleteUserEndpointsResponseTypeDef(BaseValidatorModel):
    EndpointsResponse: EndpointsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserEndpointsResponseTypeDef(BaseValidatorModel):
    EndpointsResponse: EndpointsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointBatchRequestTypeDef(BaseValidatorModel):
    Item: Sequence[EndpointBatchItemTypeDef]


class UpdateEndpointRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str
    EndpointRequest: EndpointRequestTypeDef


class EventsBatchTypeDef(BaseValidatorModel):
    Endpoint: PublicEndpointTypeDef
    Events: Mapping[str, EventTypeDef]


class InAppCampaignScheduleTypeDef(BaseValidatorModel):
    EndDate: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterOutputTypeDef] = None
    QuietTime: Optional[QuietTimeTypeDef] = None


class ScheduleOutputTypeDef(BaseValidatorModel):
    StartTime: str
    EndTime: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterOutputTypeDef] = None
    Frequency: Optional[FrequencyType] = None
    IsLocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    Timezone: Optional[str] = None


class EventStartConditionOutputTypeDef(BaseValidatorModel):
    EventFilter: Optional[EventFilterOutputTypeDef] = None
    SegmentId: Optional[str] = None


class PutEventsResponseTypeDef(BaseValidatorModel):
    EventsResponse: EventsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetExportJobsResponseTypeDef(BaseValidatorModel):
    ExportJobsResponse: ExportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentExportJobsResponseTypeDef(BaseValidatorModel):
    ExportJobsResponse: ExportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SegmentDimensionsOutputTypeDef(BaseValidatorModel):
    Attributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None
    Behavior: Optional[SegmentBehaviorsTypeDef] = None
    Demographic: Optional[SegmentDemographicsOutputTypeDef] = None
    Location: Optional[SegmentLocationOutputTypeDef] = None
    Metrics: Optional[Dict[str, MetricDimensionTypeDef]] = None
    UserAttributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None


class GetImportJobsResponseTypeDef(BaseValidatorModel):
    ImportJobsResponse: ImportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentImportJobsResponseTypeDef(BaseValidatorModel):
    ImportJobsResponse: ImportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CampaignInAppMessageOutputTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    Content: Optional[List[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None


class CampaignInAppMessageTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    Content: Optional[Sequence[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Mapping[str, str]] = None
    Layout: Optional[LayoutType] = None


class InAppMessageTypeDef(BaseValidatorModel):
    Content: Optional[List[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None


class InAppTemplateRequestTypeDef(BaseValidatorModel):
    Content: Optional[Sequence[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Mapping[str, str]] = None
    Layout: Optional[LayoutType] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None


class InAppTemplateResponseTypeDef(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    Content: Optional[List[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class ApplicationDateRangeKpiResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndTime: datetime
    KpiName: str
    KpiResult: BaseKpiResultTypeDef
    StartTime: datetime
    NextToken: Optional[str] = None


class CampaignDateRangeKpiResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    EndTime: datetime
    KpiName: str
    KpiResult: BaseKpiResultTypeDef
    StartTime: datetime
    NextToken: Optional[str] = None


class JourneyDateRangeKpiResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndTime: datetime
    JourneyId: str
    KpiName: str
    KpiResult: BaseKpiResultTypeDef
    StartTime: datetime
    NextToken: Optional[str] = None


class DirectMessageConfigurationTypeDef(BaseValidatorModel):
    ADMMessage: Optional[ADMMessageTypeDef] = None
    APNSMessage: Optional[APNSMessageTypeDef] = None
    BaiduMessage: Optional[BaiduMessageTypeDef] = None
    DefaultMessage: Optional[DefaultMessageTypeDef] = None
    DefaultPushNotificationMessage: Optional[DefaultPushNotificationMessageTypeDef] = None
    EmailMessage: Optional[EmailMessageTypeDef] = None
    GCMMessage: Optional[GCMMessageTypeDef] = None
    SMSMessage: Optional[SMSMessageTypeDef] = None
    VoiceMessage: Optional[VoiceMessageTypeDef] = None


class UpdateEndpointsBatchRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EndpointBatchRequest: EndpointBatchRequestTypeDef


class EventsRequestTypeDef(BaseValidatorModel):
    BatchItem: Mapping[str, EventsBatchTypeDef]


class StartConditionOutputTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    EventStartCondition: Optional[EventStartConditionOutputTypeDef] = None
    SegmentStartCondition: Optional[SegmentConditionTypeDef] = None


class SimpleConditionOutputTypeDef(BaseValidatorModel):
    EventCondition: Optional[EventConditionOutputTypeDef] = None
    SegmentCondition: Optional[SegmentConditionTypeDef] = None
    SegmentDimensions: Optional[SegmentDimensionsOutputTypeDef] = None


class MessageConfigurationOutputTypeDef(BaseValidatorModel):
    ADMMessage: Optional[MessageTypeDef] = None
    APNSMessage: Optional[MessageTypeDef] = None
    BaiduMessage: Optional[MessageTypeDef] = None
    CustomMessage: Optional[CampaignCustomMessageTypeDef] = None
    DefaultMessage: Optional[MessageTypeDef] = None
    EmailMessage: Optional[CampaignEmailMessageOutputTypeDef] = None
    GCMMessage: Optional[MessageTypeDef] = None
    SMSMessage: Optional[CampaignSmsMessageTypeDef] = None
    InAppMessage: Optional[CampaignInAppMessageOutputTypeDef] = None


class InAppMessageCampaignTypeDef(BaseValidatorModel):
    CampaignId: Optional[str] = None
    DailyCap: Optional[int] = None
    InAppMessage: Optional[InAppMessageTypeDef] = None
    Priority: Optional[int] = None
    Schedule: Optional[InAppCampaignScheduleTypeDef] = None
    SessionCap: Optional[int] = None
    TotalCap: Optional[int] = None
    TreatmentId: Optional[str] = None


class CreateInAppTemplateRequestTypeDef(BaseValidatorModel):
    InAppTemplateRequest: InAppTemplateRequestTypeDef
    TemplateName: str


class UpdateInAppTemplateRequestTypeDef(BaseValidatorModel):
    InAppTemplateRequest: InAppTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class GetInAppTemplateResponseTypeDef(BaseValidatorModel):
    InAppTemplateResponse: InAppTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationDateRangeKpiResponseTypeDef(BaseValidatorModel):
    ApplicationDateRangeKpiResponse: ApplicationDateRangeKpiResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCampaignDateRangeKpiResponseTypeDef(BaseValidatorModel):
    CampaignDateRangeKpiResponse: CampaignDateRangeKpiResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJourneyDateRangeKpiResponseTypeDef(BaseValidatorModel):
    JourneyDateRangeKpiResponse: JourneyDateRangeKpiResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EventDimensionsUnionTypeDef(BaseValidatorModel):
    pass


class CampaignEventFilterTypeDef(BaseValidatorModel):
    Dimensions: EventDimensionsUnionTypeDef
    FilterType: FilterTypeType


class EventConditionTypeDef(BaseValidatorModel):
    Dimensions: Optional[EventDimensionsUnionTypeDef] = None
    MessageActivity: Optional[str] = None


class EventFilterTypeDef(BaseValidatorModel):
    Dimensions: EventDimensionsUnionTypeDef
    FilterType: FilterTypeType


class SegmentLocationUnionTypeDef(BaseValidatorModel):
    pass


class SegmentDemographicsUnionTypeDef(BaseValidatorModel):
    pass


class SegmentDimensionsTypeDef(BaseValidatorModel):
    Attributes: Optional[Mapping[str, AttributeDimensionUnionTypeDef]] = None
    Behavior: Optional[SegmentBehaviorsTypeDef] = None
    Demographic: Optional[SegmentDemographicsUnionTypeDef] = None
    Location: Optional[SegmentLocationUnionTypeDef] = None
    Metrics: Optional[Mapping[str, MetricDimensionTypeDef]] = None
    UserAttributes: Optional[Mapping[str, AttributeDimensionUnionTypeDef]] = None


class MessageRequestTypeDef(BaseValidatorModel):
    MessageConfiguration: DirectMessageConfigurationTypeDef
    Addresses: Optional[Mapping[str, AddressConfigurationTypeDef]] = None
    Context: Optional[Mapping[str, str]] = None
    Endpoints: Optional[Mapping[str, EndpointSendConfigurationTypeDef]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TraceId: Optional[str] = None


class SendUsersMessageRequestTypeDef(BaseValidatorModel):
    MessageConfiguration: DirectMessageConfigurationTypeDef
    Users: Mapping[str, EndpointSendConfigurationTypeDef]
    Context: Optional[Mapping[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TraceId: Optional[str] = None


class PutEventsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EventsRequest: EventsRequestTypeDef


class SegmentGroupOutputTypeDef(BaseValidatorModel):
    pass


class SegmentGroupListOutputTypeDef(BaseValidatorModel):
    Groups: Optional[List[SegmentGroupOutputTypeDef]] = None
    Include: Optional[IncludeType] = None


class ConditionOutputTypeDef(BaseValidatorModel):
    Conditions: Optional[List[SimpleConditionOutputTypeDef]] = None
    Operator: Optional[OperatorType] = None


class MultiConditionalBranchOutputTypeDef(BaseValidatorModel):
    Condition: Optional[SimpleConditionOutputTypeDef] = None
    NextActivity: Optional[str] = None


class TreatmentResourceTypeDef(BaseValidatorModel):
    Id: str
    SizePercent: int
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationOutputTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationOutputTypeDef] = None
    Schedule: Optional[ScheduleOutputTypeDef] = None
    State: Optional[CampaignStateTypeDef] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None


class CampaignInAppMessageUnionTypeDef(BaseValidatorModel):
    pass


class CampaignEmailMessageUnionTypeDef(BaseValidatorModel):
    pass


class MessageConfigurationTypeDef(BaseValidatorModel):
    ADMMessage: Optional[MessageTypeDef] = None
    APNSMessage: Optional[MessageTypeDef] = None
    BaiduMessage: Optional[MessageTypeDef] = None
    CustomMessage: Optional[CampaignCustomMessageTypeDef] = None
    DefaultMessage: Optional[MessageTypeDef] = None
    EmailMessage: Optional[CampaignEmailMessageUnionTypeDef] = None
    GCMMessage: Optional[MessageTypeDef] = None
    SMSMessage: Optional[CampaignSmsMessageTypeDef] = None
    InAppMessage: Optional[CampaignInAppMessageUnionTypeDef] = None


class InAppMessagesResponseTypeDef(BaseValidatorModel):
    InAppMessageCampaigns: Optional[List[InAppMessageCampaignTypeDef]] = None


class SendMessagesRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MessageRequest: MessageRequestTypeDef


class SendUsersMessagesRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SendUsersMessageRequest: SendUsersMessageRequestTypeDef


class SegmentResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreationDate: str
    Id: str
    SegmentType: SegmentTypeType
    Dimensions: Optional[SegmentDimensionsOutputTypeDef] = None
    ImportDefinition: Optional[SegmentImportResourceTypeDef] = None
    LastModifiedDate: Optional[str] = None
    Name: Optional[str] = None
    SegmentGroups: Optional[SegmentGroupListOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    Version: Optional[int] = None


class ConditionalSplitActivityOutputTypeDef(BaseValidatorModel):
    Condition: Optional[ConditionOutputTypeDef] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None
    FalseActivity: Optional[str] = None
    TrueActivity: Optional[str] = None


class MultiConditionalSplitActivityOutputTypeDef(BaseValidatorModel):
    Branches: Optional[List[MultiConditionalBranchOutputTypeDef]] = None
    DefaultActivity: Optional[str] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None


class CampaignResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreationDate: str
    Id: str
    LastModifiedDate: str
    SegmentId: str
    SegmentVersion: int
    AdditionalTreatments: Optional[List[TreatmentResourceTypeDef]] = None
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationOutputTypeDef] = None
    DefaultState: Optional[CampaignStateTypeDef] = None
    Description: Optional[str] = None
    HoldoutPercent: Optional[int] = None
    Hook: Optional[CampaignHookTypeDef] = None
    IsPaused: Optional[bool] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationOutputTypeDef] = None
    Name: Optional[str] = None
    Schedule: Optional[ScheduleOutputTypeDef] = None
    State: Optional[CampaignStateTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None
    Version: Optional[int] = None
    Priority: Optional[int] = None


class GetInAppMessagesResponseTypeDef(BaseValidatorModel):
    InAppMessagesResponse: InAppMessagesResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CampaignEventFilterUnionTypeDef(BaseValidatorModel):
    pass


class ScheduleTypeDef(BaseValidatorModel):
    StartTime: str
    EndTime: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterUnionTypeDef] = None
    Frequency: Optional[FrequencyType] = None
    IsLocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    Timezone: Optional[str] = None


class EventFilterUnionTypeDef(BaseValidatorModel):
    pass


class EventStartConditionTypeDef(BaseValidatorModel):
    EventFilter: Optional[EventFilterUnionTypeDef] = None
    SegmentId: Optional[str] = None


class SegmentDimensionsUnionTypeDef(BaseValidatorModel):
    pass


class EventConditionUnionTypeDef(BaseValidatorModel):
    pass


class SimpleConditionTypeDef(BaseValidatorModel):
    EventCondition: Optional[EventConditionUnionTypeDef] = None
    SegmentCondition: Optional[SegmentConditionTypeDef] = None
    SegmentDimensions: Optional[SegmentDimensionsUnionTypeDef] = None


class CreateSegmentResponseTypeDef(BaseValidatorModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSegmentResponseTypeDef(BaseValidatorModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentResponseTypeDef(BaseValidatorModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentVersionResponseTypeDef(BaseValidatorModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SegmentsResponseTypeDef(BaseValidatorModel):
    Item: List[SegmentResponseTypeDef]
    NextToken: Optional[str] = None


class UpdateSegmentResponseTypeDef(BaseValidatorModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ActivityOutputTypeDef(BaseValidatorModel):
    CUSTOM: Optional[CustomMessageActivityOutputTypeDef] = None
    ConditionalSplit: Optional[ConditionalSplitActivityOutputTypeDef] = None
    Description: Optional[str] = None
    EMAIL: Optional[EmailMessageActivityTypeDef] = None
    Holdout: Optional[HoldoutActivityTypeDef] = None
    MultiCondition: Optional[MultiConditionalSplitActivityOutputTypeDef] = None
    PUSH: Optional[PushMessageActivityTypeDef] = None
    RandomSplit: Optional[RandomSplitActivityOutputTypeDef] = None
    SMS: Optional[SMSMessageActivityTypeDef] = None
    Wait: Optional[WaitActivityTypeDef] = None
    ContactCenter: Optional[ContactCenterActivityTypeDef] = None


class CampaignsResponseTypeDef(BaseValidatorModel):
    Item: List[CampaignResponseTypeDef]
    NextToken: Optional[str] = None


class CreateCampaignResponseTypeDef(BaseValidatorModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCampaignResponseTypeDef(BaseValidatorModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCampaignResponseTypeDef(BaseValidatorModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCampaignVersionResponseTypeDef(BaseValidatorModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCampaignResponseTypeDef(BaseValidatorModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentVersionsResponseTypeDef(BaseValidatorModel):
    SegmentsResponse: SegmentsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentsResponseTypeDef(BaseValidatorModel):
    SegmentsResponse: SegmentsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JourneyResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Id: str
    Name: str
    Activities: Optional[Dict[str, ActivityOutputTypeDef]] = None
    CreationDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[JourneyLimitsTypeDef] = None
    LocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    RefreshFrequency: Optional[str] = None
    Schedule: Optional[JourneyScheduleOutputTypeDef] = None
    StartActivity: Optional[str] = None
    StartCondition: Optional[StartConditionOutputTypeDef] = None
    State: Optional[StateType] = None
    tags: Optional[Dict[str, str]] = None
    WaitForQuietTime: Optional[bool] = None
    RefreshOnSegmentUpdate: Optional[bool] = None
    JourneyChannelSettings: Optional[JourneyChannelSettingsTypeDef] = None
    SendingSchedule: Optional[bool] = None
    OpenHours: Optional[OpenHoursOutputTypeDef] = None
    ClosedDays: Optional[ClosedDaysOutputTypeDef] = None
    TimezoneEstimationMethods: Optional[List[TimezoneEstimationMethodsElementType]] = None


class GetCampaignVersionsResponseTypeDef(BaseValidatorModel):
    CampaignsResponse: CampaignsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCampaignsResponseTypeDef(BaseValidatorModel):
    CampaignsResponse: CampaignsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ScheduleUnionTypeDef(BaseValidatorModel):
    pass


class MessageConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CustomDeliveryConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class WriteTreatmentResourceTypeDef(BaseValidatorModel):
    SizePercent: int
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationUnionTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationUnionTypeDef] = None
    Schedule: Optional[ScheduleUnionTypeDef] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None


class EventStartConditionUnionTypeDef(BaseValidatorModel):
    pass


class StartConditionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    EventStartCondition: Optional[EventStartConditionUnionTypeDef] = None
    SegmentStartCondition: Optional[SegmentConditionTypeDef] = None


class SegmentGroupUnionTypeDef(BaseValidatorModel):
    pass


class SegmentGroupListTypeDef(BaseValidatorModel):
    Groups: Optional[Sequence[SegmentGroupUnionTypeDef]] = None
    Include: Optional[IncludeType] = None


class SimpleConditionUnionTypeDef(BaseValidatorModel):
    pass


class ConditionTypeDef(BaseValidatorModel):
    Conditions: Optional[Sequence[SimpleConditionUnionTypeDef]] = None
    Operator: Optional[OperatorType] = None


class MultiConditionalBranchTypeDef(BaseValidatorModel):
    Condition: Optional[SimpleConditionUnionTypeDef] = None
    NextActivity: Optional[str] = None


class CreateJourneyResponseTypeDef(BaseValidatorModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteJourneyResponseTypeDef(BaseValidatorModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJourneyResponseTypeDef(BaseValidatorModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JourneysResponseTypeDef(BaseValidatorModel):
    Item: List[JourneyResponseTypeDef]
    NextToken: Optional[str] = None


class UpdateJourneyResponseTypeDef(BaseValidatorModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJourneyStateResponseTypeDef(BaseValidatorModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WriteCampaignRequestTypeDef(BaseValidatorModel):
    AdditionalTreatments: Optional[Sequence[WriteTreatmentResourceTypeDef]] = None
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationUnionTypeDef] = None
    Description: Optional[str] = None
    HoldoutPercent: Optional[int] = None
    Hook: Optional[CampaignHookTypeDef] = None
    IsPaused: Optional[bool] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationUnionTypeDef] = None
    Name: Optional[str] = None
    Schedule: Optional[ScheduleUnionTypeDef] = None
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None
    Priority: Optional[int] = None


class ListJourneysResponseTypeDef(BaseValidatorModel):
    JourneysResponse: JourneysResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCampaignRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    WriteCampaignRequest: WriteCampaignRequestTypeDef


class UpdateCampaignRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    WriteCampaignRequest: WriteCampaignRequestTypeDef


class SegmentGroupListUnionTypeDef(BaseValidatorModel):
    pass


class WriteSegmentRequestTypeDef(BaseValidatorModel):
    Dimensions: Optional[SegmentDimensionsUnionTypeDef] = None
    Name: Optional[str] = None
    SegmentGroups: Optional[SegmentGroupListUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class ConditionUnionTypeDef(BaseValidatorModel):
    pass


class ConditionalSplitActivityTypeDef(BaseValidatorModel):
    Condition: Optional[ConditionUnionTypeDef] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None
    FalseActivity: Optional[str] = None
    TrueActivity: Optional[str] = None


class MultiConditionalBranchUnionTypeDef(BaseValidatorModel):
    pass


class MultiConditionalSplitActivityTypeDef(BaseValidatorModel):
    Branches: Optional[Sequence[MultiConditionalBranchUnionTypeDef]] = None
    DefaultActivity: Optional[str] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None


class CreateSegmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    WriteSegmentRequest: WriteSegmentRequestTypeDef


class UpdateSegmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    WriteSegmentRequest: WriteSegmentRequestTypeDef


class CustomMessageActivityUnionTypeDef(BaseValidatorModel):
    pass


class MultiConditionalSplitActivityUnionTypeDef(BaseValidatorModel):
    pass


class RandomSplitActivityUnionTypeDef(BaseValidatorModel):
    pass


class ConditionalSplitActivityUnionTypeDef(BaseValidatorModel):
    pass


class ActivityTypeDef(BaseValidatorModel):
    CUSTOM: Optional[CustomMessageActivityUnionTypeDef] = None
    ConditionalSplit: Optional[ConditionalSplitActivityUnionTypeDef] = None
    Description: Optional[str] = None
    EMAIL: Optional[EmailMessageActivityTypeDef] = None
    Holdout: Optional[HoldoutActivityTypeDef] = None
    MultiCondition: Optional[MultiConditionalSplitActivityUnionTypeDef] = None
    PUSH: Optional[PushMessageActivityTypeDef] = None
    RandomSplit: Optional[RandomSplitActivityUnionTypeDef] = None
    SMS: Optional[SMSMessageActivityTypeDef] = None
    Wait: Optional[WaitActivityTypeDef] = None
    ContactCenter: Optional[ContactCenterActivityTypeDef] = None


class ActivityUnionTypeDef(BaseValidatorModel):
    pass


class StartConditionUnionTypeDef(BaseValidatorModel):
    pass


class OpenHoursUnionTypeDef(BaseValidatorModel):
    pass


class JourneyScheduleUnionTypeDef(BaseValidatorModel):
    pass


class ClosedDaysUnionTypeDef(BaseValidatorModel):
    pass


class WriteJourneyRequestTypeDef(BaseValidatorModel):
    Name: str
    Activities: Optional[Mapping[str, ActivityUnionTypeDef]] = None
    CreationDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[JourneyLimitsTypeDef] = None
    LocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    RefreshFrequency: Optional[str] = None
    Schedule: Optional[JourneyScheduleUnionTypeDef] = None
    StartActivity: Optional[str] = None
    StartCondition: Optional[StartConditionUnionTypeDef] = None
    State: Optional[StateType] = None
    WaitForQuietTime: Optional[bool] = None
    RefreshOnSegmentUpdate: Optional[bool] = None
    JourneyChannelSettings: Optional[JourneyChannelSettingsTypeDef] = None
    SendingSchedule: Optional[bool] = None
    OpenHours: Optional[OpenHoursUnionTypeDef] = None
    ClosedDays: Optional[ClosedDaysUnionTypeDef] = None
    TimezoneEstimationMethods: Optional[Sequence[TimezoneEstimationMethodsElementType]] = None


class CreateJourneyRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    WriteJourneyRequest: WriteJourneyRequestTypeDef


class UpdateJourneyRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    WriteJourneyRequest: WriteJourneyRequestTypeDef


