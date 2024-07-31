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
from aws_resource_validator.pydantic_models.pinpoint_constants import *

class ADMChannelRequestTypeDef(BaseModel):
    ClientId: str
    ClientSecret: str
    Enabled: Optional[bool] = None

class ADMChannelResponseTypeDef(BaseModel):
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

class ADMMessageTypeDef(BaseModel):
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

class APNSChannelRequestTypeDef(BaseModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None

class APNSChannelResponseTypeDef(BaseModel):
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

class APNSMessageTypeDef(BaseModel):
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

class APNSPushNotificationTemplateTypeDef(BaseModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    MediaUrl: Optional[str] = None
    RawContent: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None

class APNSSandboxChannelRequestTypeDef(BaseModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None

class APNSSandboxChannelResponseTypeDef(BaseModel):
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

class APNSVoipChannelRequestTypeDef(BaseModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None

class APNSVoipChannelResponseTypeDef(BaseModel):
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

class APNSVoipSandboxChannelRequestTypeDef(BaseModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None

class APNSVoipSandboxChannelResponseTypeDef(BaseModel):
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

class ActivityResponseTypeDef(BaseModel):
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

class ContactCenterActivityTypeDef(BaseModel):
    NextActivity: Optional[str] = None

class HoldoutActivityTypeDef(BaseModel):
    Percentage: int
    NextActivity: Optional[str] = None

class AddressConfigurationTypeDef(BaseModel):
    BodyOverride: Optional[str] = None
    ChannelType: Optional[ChannelTypeType] = None
    Context: Optional[Mapping[str, str]] = None
    RawContent: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TitleOverride: Optional[str] = None

class AndroidPushNotificationTemplateTypeDef(BaseModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    RawContent: Optional[str] = None
    SmallImageIconUrl: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None

class ApplicationResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    tags: Optional[Dict[str, str]] = None
    CreationDate: Optional[str] = None

class JourneyTimeframeCapTypeDef(BaseModel):
    Cap: Optional[int] = None
    Days: Optional[int] = None

class CampaignHookTypeDef(BaseModel):
    LambdaFunctionName: Optional[str] = None
    Mode: Optional[ModeType] = None
    WebUrl: Optional[str] = None

class CampaignLimitsTypeDef(BaseModel):
    Daily: Optional[int] = None
    MaximumDuration: Optional[int] = None
    MessagesPerSecond: Optional[int] = None
    Total: Optional[int] = None
    Session: Optional[int] = None

class QuietTimeTypeDef(BaseModel):
    End: Optional[str] = None
    Start: Optional[str] = None

class AttributeDimensionOutputTypeDef(BaseModel):
    Values: List[str]
    AttributeType: Optional[AttributeTypeType] = None

class AttributeDimensionTypeDef(BaseModel):
    Values: Sequence[str]
    AttributeType: Optional[AttributeTypeType] = None

class AttributesResourceTypeDef(BaseModel):
    ApplicationId: str
    AttributeType: str
    Attributes: Optional[List[str]] = None

class BaiduChannelRequestTypeDef(BaseModel):
    ApiKey: str
    SecretKey: str
    Enabled: Optional[bool] = None

class BaiduChannelResponseTypeDef(BaseModel):
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

class BaiduMessageTypeDef(BaseModel):
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

class CampaignCustomMessageTypeDef(BaseModel):
    Data: Optional[str] = None

class MessageHeaderTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class CampaignStateTypeDef(BaseModel):
    CampaignStatus: Optional[CampaignStatusType] = None

class CustomDeliveryConfigurationOutputTypeDef(BaseModel):
    DeliveryUri: str
    EndpointTypes: Optional[List[EndpointTypesElementType]] = None

class CampaignSmsMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None

class ChannelResponseTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None

class ClosedDaysRuleTypeDef(BaseModel):
    Name: Optional[str] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None

class WaitTimeTypeDef(BaseModel):
    WaitFor: Optional[str] = None
    WaitUntil: Optional[str] = None

class CreateApplicationRequestTypeDef(BaseModel):
    Name: str
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateTemplateMessageBodyTypeDef(BaseModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None
    RequestID: Optional[str] = None

class ExportJobRequestTypeDef(BaseModel):
    RoleArn: str
    S3UrlPrefix: str
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None

class ImportJobRequestTypeDef(BaseModel):
    Format: FormatType
    RoleArn: str
    S3Url: str
    DefineSegment: Optional[bool] = None
    ExternalId: Optional[str] = None
    RegisterEndpoints: Optional[bool] = None
    SegmentId: Optional[str] = None
    SegmentName: Optional[str] = None

class TemplateCreateMessageBodyTypeDef(BaseModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None
    RequestID: Optional[str] = None

class CreateRecommenderConfigurationTypeDef(BaseModel):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Mapping[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None

class RecommenderConfigurationResponseTypeDef(BaseModel):
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

class SMSTemplateRequestTypeDef(BaseModel):
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None

class VoiceTemplateRequestTypeDef(BaseModel):
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    LanguageCode: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None
    VoiceId: Optional[str] = None

class CustomDeliveryConfigurationTypeDef(BaseModel):
    DeliveryUri: str
    EndpointTypes: Optional[Sequence[EndpointTypesElementType]] = None

class JourneyCustomMessageTypeDef(BaseModel):
    Data: Optional[str] = None

class DefaultButtonConfigurationTypeDef(BaseModel):
    ButtonAction: ButtonActionType
    Text: str
    BackgroundColor: Optional[str] = None
    BorderRadius: Optional[int] = None
    Link: Optional[str] = None
    TextColor: Optional[str] = None

class DefaultMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None

class DefaultPushNotificationMessageTypeDef(BaseModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    SilentPush: Optional[bool] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    Title: Optional[str] = None
    Url: Optional[str] = None

class DefaultPushNotificationTemplateTypeDef(BaseModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None

class DeleteAdmChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteApnsChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteApnsSandboxChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteApnsVoipChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteApnsVoipSandboxChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteAppRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteBaiduChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteCampaignRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str

class DeleteEmailChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class EmailChannelResponseTypeDef(BaseModel):
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

class DeleteEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class MessageBodyTypeDef(BaseModel):
    Message: Optional[str] = None
    RequestID: Optional[str] = None

class DeleteEndpointRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EndpointId: str

class DeleteEventStreamRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class EventStreamTypeDef(BaseModel):
    ApplicationId: str
    DestinationStreamArn: str
    RoleArn: str
    ExternalId: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    LastUpdatedBy: Optional[str] = None

class DeleteGcmChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GCMChannelResponseTypeDef(BaseModel):
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

class DeleteInAppTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class DeleteJourneyRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str

class DeletePushTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class DeleteRecommenderConfigurationRequestRequestTypeDef(BaseModel):
    RecommenderId: str

class DeleteSegmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str

class DeleteSmsChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class SMSChannelResponseTypeDef(BaseModel):
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

class DeleteSmsTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class DeleteUserEndpointsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    UserId: str

class DeleteVoiceChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class VoiceChannelResponseTypeDef(BaseModel):
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

class DeleteVoiceTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class GCMMessageTypeDef(BaseModel):
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

class SMSMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    Keyword: Optional[str] = None
    MediaUrl: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None

class VoiceMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    LanguageCode: Optional[str] = None
    OriginationNumber: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    VoiceId: Optional[str] = None

class EmailChannelRequestTypeDef(BaseModel):
    FromAddress: str
    Identity: str
    ConfigurationSet: Optional[str] = None
    Enabled: Optional[bool] = None
    RoleArn: Optional[str] = None
    OrchestrationSendingRoleArn: Optional[str] = None

class JourneyEmailMessageTypeDef(BaseModel):
    FromAddress: Optional[str] = None

class EndpointDemographicTypeDef(BaseModel):
    AppVersion: Optional[str] = None
    Locale: Optional[str] = None
    Make: Optional[str] = None
    Model: Optional[str] = None
    ModelVersion: Optional[str] = None
    Platform: Optional[str] = None
    PlatformVersion: Optional[str] = None
    Timezone: Optional[str] = None

class EndpointLocationTypeDef(BaseModel):
    City: Optional[str] = None
    Country: Optional[str] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    PostalCode: Optional[str] = None
    Region: Optional[str] = None

class EndpointUserTypeDef(BaseModel):
    UserAttributes: Optional[Mapping[str, Sequence[str]]] = None
    UserId: Optional[str] = None

class EndpointItemResponseTypeDef(BaseModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None

class EndpointMessageResultTypeDef(BaseModel):
    DeliveryStatus: DeliveryStatusType
    StatusCode: int
    Address: Optional[str] = None
    MessageId: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdatedToken: Optional[str] = None

class EndpointUserOutputTypeDef(BaseModel):
    UserAttributes: Optional[Dict[str, List[str]]] = None
    UserId: Optional[str] = None

class EndpointSendConfigurationTypeDef(BaseModel):
    BodyOverride: Optional[str] = None
    Context: Optional[Mapping[str, str]] = None
    RawContent: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TitleOverride: Optional[str] = None

class MetricDimensionTypeDef(BaseModel):
    ComparisonOperator: str
    Value: float

class SetDimensionOutputTypeDef(BaseModel):
    Values: List[str]
    DimensionType: Optional[DimensionTypeType] = None

class SetDimensionTypeDef(BaseModel):
    Values: Sequence[str]
    DimensionType: Optional[DimensionTypeType] = None

class EventItemResponseTypeDef(BaseModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None

class SessionTypeDef(BaseModel):
    Id: str
    StartTimestamp: str
    Duration: Optional[int] = None
    StopTimestamp: Optional[str] = None

class ExportJobResourceTypeDef(BaseModel):
    RoleArn: str
    S3UrlPrefix: str
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None

class GCMChannelRequestTypeDef(BaseModel):
    ApiKey: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    ServiceJson: Optional[str] = None

class GPSCoordinatesTypeDef(BaseModel):
    Latitude: float
    Longitude: float

class GetAdmChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApnsChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApnsSandboxChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApnsVoipChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApnsVoipSandboxChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetAppRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetApplicationSettingsRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetAppsRequestRequestTypeDef(BaseModel):
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetBaiduChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetCampaignActivitiesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetCampaignRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str

class GetCampaignVersionRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str
    Version: str

class GetCampaignVersionsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetCampaignsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetChannelsRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetEmailChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetEmailTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class GetEndpointRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EndpointId: str

class GetEventStreamRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetExportJobRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JobId: str

class GetExportJobsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetGcmChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetImportJobRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JobId: str

class GetImportJobsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetInAppMessagesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EndpointId: str

class GetInAppTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class GetJourneyExecutionActivityMetricsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None

class JourneyExecutionActivityMetricsResponseTypeDef(BaseModel):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]

class GetJourneyExecutionMetricsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None

class JourneyExecutionMetricsResponseTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]

class GetJourneyRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str

class GetJourneyRunExecutionActivityMetricsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    RunId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None

class JourneyRunExecutionActivityMetricsResponseTypeDef(BaseModel):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]
    RunId: str

class GetJourneyRunExecutionMetricsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    RunId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None

class JourneyRunExecutionMetricsResponseTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]
    RunId: str

class GetJourneyRunsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetPushTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class GetRecommenderConfigurationRequestRequestTypeDef(BaseModel):
    RecommenderId: str

class GetRecommenderConfigurationsRequestRequestTypeDef(BaseModel):
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetSegmentExportJobsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetSegmentImportJobsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetSegmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str

class GetSegmentVersionRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str
    Version: str

class GetSegmentVersionsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetSegmentsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class GetSmsChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetSmsTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class SMSTemplateResponseTypeDef(BaseModel):
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

class GetUserEndpointsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    UserId: str

class GetVoiceChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetVoiceTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    Version: Optional[str] = None

class VoiceTemplateResponseTypeDef(BaseModel):
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

class ImportJobResourceTypeDef(BaseModel):
    Format: FormatType
    RoleArn: str
    S3Url: str
    DefineSegment: Optional[bool] = None
    ExternalId: Optional[str] = None
    RegisterEndpoints: Optional[bool] = None
    SegmentId: Optional[str] = None
    SegmentName: Optional[str] = None

class InAppMessageBodyConfigTypeDef(BaseModel):
    Alignment: AlignmentType
    Body: str
    TextColor: str

class OverrideButtonConfigurationTypeDef(BaseModel):
    ButtonAction: ButtonActionType
    Link: Optional[str] = None

class InAppMessageHeaderConfigTypeDef(BaseModel):
    Alignment: AlignmentType
    Header: str
    TextColor: str

class JourneyChannelSettingsTypeDef(BaseModel):
    ConnectCampaignArn: Optional[str] = None
    ConnectCampaignExecutionRoleArn: Optional[str] = None

class JourneyPushMessageTypeDef(BaseModel):
    TimeToLive: Optional[str] = None

class JourneyScheduleOutputTypeDef(BaseModel):
    EndTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    Timezone: Optional[str] = None

class JourneyRunResponseTypeDef(BaseModel):
    CreationTime: str
    LastUpdateTime: str
    RunId: str
    Status: JourneyRunStatusType

class JourneySMSMessageTypeDef(BaseModel):
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None

class JourneyStateRequestTypeDef(BaseModel):
    State: Optional[StateType] = None

class ListJourneysRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagsModelOutputTypeDef(BaseModel):
    tags: Dict[str, str]

class ListTemplateVersionsRequestRequestTypeDef(BaseModel):
    TemplateName: str
    TemplateType: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    Prefix: Optional[str] = None
    TemplateType: Optional[str] = None

class MessageTypeDef(BaseModel):
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

class MessageResultTypeDef(BaseModel):
    DeliveryStatus: DeliveryStatusType
    StatusCode: int
    MessageId: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdatedToken: Optional[str] = None

class NumberValidateRequestTypeDef(BaseModel):
    IsoCountryCode: Optional[str] = None
    PhoneNumber: Optional[str] = None

class NumberValidateResponseTypeDef(BaseModel):
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

class OpenHoursRuleTypeDef(BaseModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None

class WriteEventStreamTypeDef(BaseModel):
    DestinationStreamArn: str
    RoleArn: str

class RandomSplitEntryTypeDef(BaseModel):
    NextActivity: Optional[str] = None
    Percentage: Optional[int] = None

class RecencyDimensionTypeDef(BaseModel):
    Duration: DurationType
    RecencyType: RecencyTypeType

class UpdateAttributesRequestTypeDef(BaseModel):
    Blacklist: Optional[Sequence[str]] = None

class ResultRowValueTypeDef(BaseModel):
    Key: str
    Type: str
    Value: str

class SMSChannelRequestTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    SenderId: Optional[str] = None
    ShortCode: Optional[str] = None

class SegmentConditionTypeDef(BaseModel):
    SegmentId: str

class SegmentReferenceTypeDef(BaseModel):
    Id: str
    Version: Optional[int] = None

class SegmentImportResourceTypeDef(BaseModel):
    ExternalId: str
    Format: FormatType
    RoleArn: str
    S3Url: str
    Size: int
    ChannelCounts: Optional[Dict[str, int]] = None

class SendOTPMessageRequestParametersTypeDef(BaseModel):
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

class SimpleEmailPartTypeDef(BaseModel):
    Charset: Optional[str] = None
    Data: Optional[str] = None

class TagsModelTypeDef(BaseModel):
    tags: Mapping[str, str]

class TemplateActiveVersionRequestTypeDef(BaseModel):
    Version: Optional[str] = None

class TemplateTypeDef(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class TemplateResponseTypeDef(BaseModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None

class TemplateVersionResponseTypeDef(BaseModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: str
    DefaultSubstitutions: Optional[str] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateRecommenderConfigurationTypeDef(BaseModel):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Mapping[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None

class VoiceChannelRequestTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class VerificationResponseTypeDef(BaseModel):
    Valid: Optional[bool] = None

class VerifyOTPMessageRequestParametersTypeDef(BaseModel):
    DestinationIdentity: str
    Otp: str
    ReferenceId: str

class UpdateAdmChannelRequestRequestTypeDef(BaseModel):
    ADMChannelRequest: ADMChannelRequestTypeDef
    ApplicationId: str

class UpdateApnsChannelRequestRequestTypeDef(BaseModel):
    APNSChannelRequest: APNSChannelRequestTypeDef
    ApplicationId: str

class UpdateApnsSandboxChannelRequestRequestTypeDef(BaseModel):
    APNSSandboxChannelRequest: APNSSandboxChannelRequestTypeDef
    ApplicationId: str

class UpdateApnsVoipChannelRequestRequestTypeDef(BaseModel):
    APNSVoipChannelRequest: APNSVoipChannelRequestTypeDef
    ApplicationId: str

class UpdateApnsVoipSandboxChannelRequestRequestTypeDef(BaseModel):
    APNSVoipSandboxChannelRequest: APNSVoipSandboxChannelRequestTypeDef
    ApplicationId: str

class ActivitiesResponseTypeDef(BaseModel):
    Item: List[ActivityResponseTypeDef]
    NextToken: Optional[str] = None

class ApplicationsResponseTypeDef(BaseModel):
    Item: Optional[List[ApplicationResponseTypeDef]] = None
    NextToken: Optional[str] = None

class ApplicationSettingsJourneyLimitsTypeDef(BaseModel):
    DailyCap: Optional[int] = None
    TimeframeCap: Optional[JourneyTimeframeCapTypeDef] = None
    TotalCap: Optional[int] = None

class JourneyLimitsTypeDef(BaseModel):
    DailyCap: Optional[int] = None
    EndpointReentryCap: Optional[int] = None
    MessagesPerSecond: Optional[int] = None
    EndpointReentryInterval: Optional[str] = None
    TimeframeCap: Optional[JourneyTimeframeCapTypeDef] = None
    TotalCap: Optional[int] = None

class UpdateBaiduChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    BaiduChannelRequest: BaiduChannelRequestTypeDef

class RawEmailTypeDef(BaseModel):
    Data: Optional[BlobTypeDef] = None

class CampaignEmailMessageOutputTypeDef(BaseModel):
    Body: Optional[str] = None
    FromAddress: Optional[str] = None
    Headers: Optional[List[MessageHeaderTypeDef]] = None
    HtmlBody: Optional[str] = None
    Title: Optional[str] = None

class CampaignEmailMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    FromAddress: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None
    HtmlBody: Optional[str] = None
    Title: Optional[str] = None

class EmailTemplateRequestTypeDef(BaseModel):
    DefaultSubstitutions: Optional[str] = None
    HtmlPart: Optional[str] = None
    RecommenderId: Optional[str] = None
    Subject: Optional[str] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None
    TextPart: Optional[str] = None

class EmailTemplateResponseTypeDef(BaseModel):
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

class ChannelsResponseTypeDef(BaseModel):
    Channels: Dict[str, ChannelResponseTypeDef]

class ClosedDaysOutputTypeDef(BaseModel):
    EMAIL: Optional[List[ClosedDaysRuleTypeDef]] = None
    SMS: Optional[List[ClosedDaysRuleTypeDef]] = None
    PUSH: Optional[List[ClosedDaysRuleTypeDef]] = None
    VOICE: Optional[List[ClosedDaysRuleTypeDef]] = None
    CUSTOM: Optional[List[ClosedDaysRuleTypeDef]] = None

class ClosedDaysTypeDef(BaseModel):
    EMAIL: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    SMS: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    PUSH: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    VOICE: Optional[Sequence[ClosedDaysRuleTypeDef]] = None
    CUSTOM: Optional[Sequence[ClosedDaysRuleTypeDef]] = None

class WaitActivityTypeDef(BaseModel):
    NextActivity: Optional[str] = None
    WaitTime: Optional[WaitTimeTypeDef] = None

class CreateAppRequestRequestTypeDef(BaseModel):
    CreateApplicationRequest: CreateApplicationRequestTypeDef

class CreateAppResponseTypeDef(BaseModel):
    ApplicationResponse: ApplicationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAdmChannelResponseTypeDef(BaseModel):
    ADMChannelResponse: ADMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApnsChannelResponseTypeDef(BaseModel):
    APNSChannelResponse: APNSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApnsSandboxChannelResponseTypeDef(BaseModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApnsVoipChannelResponseTypeDef(BaseModel):
    APNSVoipChannelResponse: APNSVoipChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApnsVoipSandboxChannelResponseTypeDef(BaseModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppResponseTypeDef(BaseModel):
    ApplicationResponse: ApplicationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBaiduChannelResponseTypeDef(BaseModel):
    BaiduChannelResponse: BaiduChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdmChannelResponseTypeDef(BaseModel):
    ADMChannelResponse: ADMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApnsChannelResponseTypeDef(BaseModel):
    APNSChannelResponse: APNSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApnsSandboxChannelResponseTypeDef(BaseModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApnsVoipChannelResponseTypeDef(BaseModel):
    APNSVoipChannelResponse: APNSVoipChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApnsVoipSandboxChannelResponseTypeDef(BaseModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppResponseTypeDef(BaseModel):
    ApplicationResponse: ApplicationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaiduChannelResponseTypeDef(BaseModel):
    BaiduChannelResponse: BaiduChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveAttributesResponseTypeDef(BaseModel):
    AttributesResource: AttributesResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAdmChannelResponseTypeDef(BaseModel):
    ADMChannelResponse: ADMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApnsChannelResponseTypeDef(BaseModel):
    APNSChannelResponse: APNSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApnsSandboxChannelResponseTypeDef(BaseModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApnsVoipChannelResponseTypeDef(BaseModel):
    APNSVoipChannelResponse: APNSVoipChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApnsVoipSandboxChannelResponseTypeDef(BaseModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBaiduChannelResponseTypeDef(BaseModel):
    BaiduChannelResponse: BaiduChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEmailTemplateResponseTypeDef(BaseModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePushTemplateResponseTypeDef(BaseModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSmsTemplateResponseTypeDef(BaseModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceTemplateResponseTypeDef(BaseModel):
    CreateTemplateMessageBody: CreateTemplateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExportJobRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ExportJobRequest: ExportJobRequestTypeDef

class CreateImportJobRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ImportJobRequest: ImportJobRequestTypeDef

class CreateInAppTemplateResponseTypeDef(BaseModel):
    TemplateCreateMessageBody: TemplateCreateMessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecommenderConfigurationRequestRequestTypeDef(BaseModel):
    CreateRecommenderConfiguration: CreateRecommenderConfigurationTypeDef

class CreateRecommenderConfigurationResponseTypeDef(BaseModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRecommenderConfigurationResponseTypeDef(BaseModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommenderConfigurationResponseTypeDef(BaseModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommenderConfigurationsResponseTypeDef(BaseModel):
    Item: List[RecommenderConfigurationResponseTypeDef]
    NextToken: Optional[str] = None

class UpdateRecommenderConfigurationResponseTypeDef(BaseModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSmsTemplateRequestRequestTypeDef(BaseModel):
    SMSTemplateRequest: SMSTemplateRequestTypeDef
    TemplateName: str

class UpdateSmsTemplateRequestRequestTypeDef(BaseModel):
    SMSTemplateRequest: SMSTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None

class CreateVoiceTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    VoiceTemplateRequest: VoiceTemplateRequestTypeDef

class UpdateVoiceTemplateRequestRequestTypeDef(BaseModel):
    TemplateName: str
    VoiceTemplateRequest: VoiceTemplateRequestTypeDef
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None

class CustomMessageActivityOutputTypeDef(BaseModel):
    DeliveryUri: Optional[str] = None
    EndpointTypes: Optional[List[EndpointTypesElementType]] = None
    MessageConfig: Optional[JourneyCustomMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None

class CustomMessageActivityTypeDef(BaseModel):
    DeliveryUri: Optional[str] = None
    EndpointTypes: Optional[Sequence[EndpointTypesElementType]] = None
    MessageConfig: Optional[JourneyCustomMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None

class PushNotificationTemplateRequestTypeDef(BaseModel):
    ADM: Optional[AndroidPushNotificationTemplateTypeDef] = None
    APNS: Optional[APNSPushNotificationTemplateTypeDef] = None
    Baidu: Optional[AndroidPushNotificationTemplateTypeDef] = None
    Default: Optional[DefaultPushNotificationTemplateTypeDef] = None
    DefaultSubstitutions: Optional[str] = None
    GCM: Optional[AndroidPushNotificationTemplateTypeDef] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None

class PushNotificationTemplateResponseTypeDef(BaseModel):
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

class DeleteEmailChannelResponseTypeDef(BaseModel):
    EmailChannelResponse: EmailChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEmailChannelResponseTypeDef(BaseModel):
    EmailChannelResponse: EmailChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEmailChannelResponseTypeDef(BaseModel):
    EmailChannelResponse: EmailChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEmailTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInAppTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePushTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSmsTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVoiceTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEmailTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointsBatchResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInAppTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePushTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSmsTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateActiveVersionResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceTemplateResponseTypeDef(BaseModel):
    MessageBody: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventStreamResponseTypeDef(BaseModel):
    EventStream: EventStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventStreamResponseTypeDef(BaseModel):
    EventStream: EventStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventStreamResponseTypeDef(BaseModel):
    EventStream: EventStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGcmChannelResponseTypeDef(BaseModel):
    GCMChannelResponse: GCMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGcmChannelResponseTypeDef(BaseModel):
    GCMChannelResponse: GCMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGcmChannelResponseTypeDef(BaseModel):
    GCMChannelResponse: GCMChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSmsChannelResponseTypeDef(BaseModel):
    SMSChannelResponse: SMSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSmsChannelResponseTypeDef(BaseModel):
    SMSChannelResponse: SMSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSmsChannelResponseTypeDef(BaseModel):
    SMSChannelResponse: SMSChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVoiceChannelResponseTypeDef(BaseModel):
    VoiceChannelResponse: VoiceChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceChannelResponseTypeDef(BaseModel):
    VoiceChannelResponse: VoiceChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceChannelResponseTypeDef(BaseModel):
    VoiceChannelResponse: VoiceChannelResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEmailChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EmailChannelRequest: EmailChannelRequestTypeDef

class EmailMessageActivityTypeDef(BaseModel):
    MessageConfig: Optional[JourneyEmailMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None

class EndpointBatchItemTypeDef(BaseModel):
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
    User: Optional[EndpointUserTypeDef] = None

class EndpointRequestTypeDef(BaseModel):
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
    User: Optional[EndpointUserTypeDef] = None

class PublicEndpointTypeDef(BaseModel):
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
    User: Optional[EndpointUserTypeDef] = None

class SendUsersMessageResponseTypeDef(BaseModel):
    ApplicationId: str
    RequestId: Optional[str] = None
    Result: Optional[Dict[str, Dict[str, EndpointMessageResultTypeDef]]] = None

class EndpointResponseTypeDef(BaseModel):
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

class EventDimensionsOutputTypeDef(BaseModel):
    Attributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None
    EventType: Optional[SetDimensionOutputTypeDef] = None
    Metrics: Optional[Dict[str, MetricDimensionTypeDef]] = None

class SegmentDemographicsOutputTypeDef(BaseModel):
    AppVersion: Optional[SetDimensionOutputTypeDef] = None
    Channel: Optional[SetDimensionOutputTypeDef] = None
    DeviceType: Optional[SetDimensionOutputTypeDef] = None
    Make: Optional[SetDimensionOutputTypeDef] = None
    Model: Optional[SetDimensionOutputTypeDef] = None
    Platform: Optional[SetDimensionOutputTypeDef] = None

class EventDimensionsTypeDef(BaseModel):
    Attributes: Optional[Mapping[str, AttributeDimensionTypeDef]] = None
    EventType: Optional[SetDimensionTypeDef] = None
    Metrics: Optional[Mapping[str, MetricDimensionTypeDef]] = None

class SegmentDemographicsTypeDef(BaseModel):
    AppVersion: Optional[SetDimensionTypeDef] = None
    Channel: Optional[SetDimensionTypeDef] = None
    DeviceType: Optional[SetDimensionTypeDef] = None
    Make: Optional[SetDimensionTypeDef] = None
    Model: Optional[SetDimensionTypeDef] = None
    Platform: Optional[SetDimensionTypeDef] = None

class ItemResponseTypeDef(BaseModel):
    EndpointItemResponse: Optional[EndpointItemResponseTypeDef] = None
    EventsItemResponse: Optional[Dict[str, EventItemResponseTypeDef]] = None

class EventTypeDef(BaseModel):
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

class ExportJobResponseTypeDef(BaseModel):
    ApplicationId: str
    CreationDate: str
    Definition: ExportJobResourceTypeDef
    Id: str
    JobStatus: JobStatusType
    Type: str
    CompletedPieces: Optional[int] = None
    CompletionDate: Optional[str] = None
    FailedPieces: Optional[int] = None
    Failures: Optional[List[str]] = None
    TotalFailures: Optional[int] = None
    TotalPieces: Optional[int] = None
    TotalProcessed: Optional[int] = None

class UpdateGcmChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    GCMChannelRequest: GCMChannelRequestTypeDef

class GPSPointDimensionTypeDef(BaseModel):
    Coordinates: GPSCoordinatesTypeDef
    RangeInKilometers: Optional[float] = None

class GetApplicationDateRangeKpiRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    KpiName: str
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None

class GetCampaignDateRangeKpiRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str
    KpiName: str
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None

class GetJourneyDateRangeKpiRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    KpiName: str
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None

class JourneyScheduleTypeDef(BaseModel):
    EndTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Timezone: Optional[str] = None

class GetJourneyExecutionActivityMetricsResponseTypeDef(BaseModel):
    JourneyExecutionActivityMetricsResponse: JourneyExecutionActivityMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJourneyExecutionMetricsResponseTypeDef(BaseModel):
    JourneyExecutionMetricsResponse: JourneyExecutionMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJourneyRunExecutionActivityMetricsResponseTypeDef(BaseModel):
    JourneyRunExecutionActivityMetricsResponse: JourneyRunExecutionActivityMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJourneyRunExecutionMetricsResponseTypeDef(BaseModel):
    JourneyRunExecutionMetricsResponse: JourneyRunExecutionMetricsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSmsTemplateResponseTypeDef(BaseModel):
    SMSTemplateResponse: SMSTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceTemplateResponseTypeDef(BaseModel):
    VoiceTemplateResponse: VoiceTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportJobResponseTypeDef(BaseModel):
    ApplicationId: str
    CreationDate: str
    Definition: ImportJobResourceTypeDef
    Id: str
    JobStatus: JobStatusType
    Type: str
    CompletedPieces: Optional[int] = None
    CompletionDate: Optional[str] = None
    FailedPieces: Optional[int] = None
    Failures: Optional[List[str]] = None
    TotalFailures: Optional[int] = None
    TotalPieces: Optional[int] = None
    TotalProcessed: Optional[int] = None

class InAppMessageButtonTypeDef(BaseModel):
    Android: Optional[OverrideButtonConfigurationTypeDef] = None
    DefaultConfig: Optional[DefaultButtonConfigurationTypeDef] = None
    IOS: Optional[OverrideButtonConfigurationTypeDef] = None
    Web: Optional[OverrideButtonConfigurationTypeDef] = None

class PushMessageActivityTypeDef(BaseModel):
    MessageConfig: Optional[JourneyPushMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None

class JourneyRunsResponseTypeDef(BaseModel):
    Item: List[JourneyRunResponseTypeDef]
    NextToken: Optional[str] = None

class SMSMessageActivityTypeDef(BaseModel):
    MessageConfig: Optional[JourneySMSMessageTypeDef] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None

class UpdateJourneyStateRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    JourneyStateRequest: JourneyStateRequestTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    TagsModel: TagsModelOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MessageResponseTypeDef(BaseModel):
    ApplicationId: str
    EndpointResult: Optional[Dict[str, EndpointMessageResultTypeDef]] = None
    RequestId: Optional[str] = None
    Result: Optional[Dict[str, MessageResultTypeDef]] = None

class PhoneNumberValidateRequestRequestTypeDef(BaseModel):
    NumberValidateRequest: NumberValidateRequestTypeDef

class PhoneNumberValidateResponseTypeDef(BaseModel):
    NumberValidateResponse: NumberValidateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OpenHoursOutputTypeDef(BaseModel):
    EMAIL: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    SMS: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    PUSH: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    VOICE: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None
    CUSTOM: Optional[Dict[DayOfWeekType, List[OpenHoursRuleTypeDef]]] = None

class OpenHoursTypeDef(BaseModel):
    EMAIL: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    SMS: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    PUSH: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    VOICE: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None
    CUSTOM: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRuleTypeDef]]] = None

class PutEventStreamRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    WriteEventStream: WriteEventStreamTypeDef

class RandomSplitActivityOutputTypeDef(BaseModel):
    Branches: Optional[List[RandomSplitEntryTypeDef]] = None

class RandomSplitActivityTypeDef(BaseModel):
    Branches: Optional[Sequence[RandomSplitEntryTypeDef]] = None

class SegmentBehaviorsTypeDef(BaseModel):
    Recency: Optional[RecencyDimensionTypeDef] = None

class RemoveAttributesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    AttributeType: str
    UpdateAttributesRequest: UpdateAttributesRequestTypeDef

class ResultRowTypeDef(BaseModel):
    GroupedBys: List[ResultRowValueTypeDef]
    Values: List[ResultRowValueTypeDef]

class UpdateSmsChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SMSChannelRequest: SMSChannelRequestTypeDef

class SendOTPMessageRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SendOTPMessageRequestParameters: SendOTPMessageRequestParametersTypeDef

class SimpleEmailTypeDef(BaseModel):
    HtmlPart: Optional[SimpleEmailPartTypeDef] = None
    Subject: Optional[SimpleEmailPartTypeDef] = None
    TextPart: Optional[SimpleEmailPartTypeDef] = None
    Headers: Optional[Sequence[MessageHeaderTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagsModel: TagsModelTypeDef

class UpdateTemplateActiveVersionRequestRequestTypeDef(BaseModel):
    TemplateActiveVersionRequest: TemplateActiveVersionRequestTypeDef
    TemplateName: str
    TemplateType: str

class TemplateConfigurationTypeDef(BaseModel):
    EmailTemplate: Optional[TemplateTypeDef] = None
    PushTemplate: Optional[TemplateTypeDef] = None
    SMSTemplate: Optional[TemplateTypeDef] = None
    VoiceTemplate: Optional[TemplateTypeDef] = None
    InAppTemplate: Optional[TemplateTypeDef] = None

class TemplatesResponseTypeDef(BaseModel):
    Item: List[TemplateResponseTypeDef]
    NextToken: Optional[str] = None

class TemplateVersionsResponseTypeDef(BaseModel):
    Item: List[TemplateVersionResponseTypeDef]
    Message: Optional[str] = None
    NextToken: Optional[str] = None
    RequestID: Optional[str] = None

class UpdateRecommenderConfigurationRequestRequestTypeDef(BaseModel):
    RecommenderId: str
    UpdateRecommenderConfiguration: UpdateRecommenderConfigurationTypeDef

class UpdateVoiceChannelRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    VoiceChannelRequest: VoiceChannelRequestTypeDef

class VerifyOTPMessageResponseTypeDef(BaseModel):
    VerificationResponse: VerificationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyOTPMessageRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    VerifyOTPMessageRequestParameters: VerifyOTPMessageRequestParametersTypeDef

class GetCampaignActivitiesResponseTypeDef(BaseModel):
    ActivitiesResponse: ActivitiesResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppsResponseTypeDef(BaseModel):
    ApplicationsResponse: ApplicationsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationSettingsResourceTypeDef(BaseModel):
    ApplicationId: str
    CampaignHook: Optional[CampaignHookTypeDef] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    JourneyLimits: Optional[ApplicationSettingsJourneyLimitsTypeDef] = None

class WriteApplicationSettingsRequestTypeDef(BaseModel):
    CampaignHook: Optional[CampaignHookTypeDef] = None
    CloudWatchMetricsEnabled: Optional[bool] = None
    EventTaggingEnabled: Optional[bool] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    JourneyLimits: Optional[ApplicationSettingsJourneyLimitsTypeDef] = None

class CreateEmailTemplateRequestRequestTypeDef(BaseModel):
    EmailTemplateRequest: EmailTemplateRequestTypeDef
    TemplateName: str

class UpdateEmailTemplateRequestRequestTypeDef(BaseModel):
    EmailTemplateRequest: EmailTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None

class GetEmailTemplateResponseTypeDef(BaseModel):
    EmailTemplateResponse: EmailTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelsResponseTypeDef(BaseModel):
    ChannelsResponse: ChannelsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommenderConfigurationsResponseTypeDef(BaseModel):
    ListRecommenderConfigurationsResponse: ListRecommenderConfigurationsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePushTemplateRequestRequestTypeDef(BaseModel):
    PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef
    TemplateName: str

class UpdatePushTemplateRequestRequestTypeDef(BaseModel):
    PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None

class GetPushTemplateResponseTypeDef(BaseModel):
    PushNotificationTemplateResponse: PushNotificationTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointBatchRequestTypeDef(BaseModel):
    Item: Sequence[EndpointBatchItemTypeDef]

class UpdateEndpointRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EndpointId: str
    EndpointRequest: EndpointRequestTypeDef

class SendUsersMessagesResponseTypeDef(BaseModel):
    SendUsersMessageResponse: SendUsersMessageResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEndpointResponseTypeDef(BaseModel):
    EndpointResponse: EndpointResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointsResponseTypeDef(BaseModel):
    Item: List[EndpointResponseTypeDef]

class GetEndpointResponseTypeDef(BaseModel):
    EndpointResponse: EndpointResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CampaignEventFilterOutputTypeDef(BaseModel):
    Dimensions: EventDimensionsOutputTypeDef
    FilterType: FilterTypeType

class EventConditionOutputTypeDef(BaseModel):
    Dimensions: Optional[EventDimensionsOutputTypeDef] = None
    MessageActivity: Optional[str] = None

class EventFilterOutputTypeDef(BaseModel):
    Dimensions: EventDimensionsOutputTypeDef
    FilterType: FilterTypeType

class CampaignEventFilterTypeDef(BaseModel):
    Dimensions: EventDimensionsTypeDef
    FilterType: FilterTypeType

class EventConditionTypeDef(BaseModel):
    Dimensions: Optional[EventDimensionsTypeDef] = None
    MessageActivity: Optional[str] = None

class EventFilterTypeDef(BaseModel):
    Dimensions: EventDimensionsTypeDef
    FilterType: FilterTypeType

class EventsResponseTypeDef(BaseModel):
    Results: Optional[Dict[str, ItemResponseTypeDef]] = None

class EventsBatchTypeDef(BaseModel):
    Endpoint: PublicEndpointTypeDef
    Events: Mapping[str, EventTypeDef]

class CreateExportJobResponseTypeDef(BaseModel):
    ExportJobResponse: ExportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportJobsResponseTypeDef(BaseModel):
    Item: List[ExportJobResponseTypeDef]
    NextToken: Optional[str] = None

class GetExportJobResponseTypeDef(BaseModel):
    ExportJobResponse: ExportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SegmentLocationOutputTypeDef(BaseModel):
    Country: Optional[SetDimensionOutputTypeDef] = None
    GPSPoint: Optional[GPSPointDimensionTypeDef] = None

class SegmentLocationTypeDef(BaseModel):
    Country: Optional[SetDimensionTypeDef] = None
    GPSPoint: Optional[GPSPointDimensionTypeDef] = None

class CreateImportJobResponseTypeDef(BaseModel):
    ImportJobResponse: ImportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportJobResponseTypeDef(BaseModel):
    ImportJobResponse: ImportJobResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportJobsResponseTypeDef(BaseModel):
    Item: List[ImportJobResponseTypeDef]
    NextToken: Optional[str] = None

class InAppMessageContentTypeDef(BaseModel):
    BackgroundColor: Optional[str] = None
    BodyConfig: Optional[InAppMessageBodyConfigTypeDef] = None
    HeaderConfig: Optional[InAppMessageHeaderConfigTypeDef] = None
    ImageUrl: Optional[str] = None
    PrimaryBtn: Optional[InAppMessageButtonTypeDef] = None
    SecondaryBtn: Optional[InAppMessageButtonTypeDef] = None

class GetJourneyRunsResponseTypeDef(BaseModel):
    JourneyRunsResponse: JourneyRunsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessagesResponseTypeDef(BaseModel):
    MessageResponse: MessageResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendOTPMessageResponseTypeDef(BaseModel):
    MessageResponse: MessageResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BaseKpiResultTypeDef(BaseModel):
    Rows: List[ResultRowTypeDef]

class EmailMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    FeedbackForwardingAddress: Optional[str] = None
    FromAddress: Optional[str] = None
    RawEmail: Optional[RawEmailTypeDef] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    SimpleEmail: Optional[SimpleEmailTypeDef] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None

class ListTemplatesResponseTypeDef(BaseModel):
    TemplatesResponse: TemplatesResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateVersionsResponseTypeDef(BaseModel):
    TemplateVersionsResponse: TemplateVersionsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationSettingsResponseTypeDef(BaseModel):
    ApplicationSettingsResource: ApplicationSettingsResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationSettingsResponseTypeDef(BaseModel):
    ApplicationSettingsResource: ApplicationSettingsResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationSettingsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    WriteApplicationSettingsRequest: WriteApplicationSettingsRequestTypeDef

class UpdateEndpointsBatchRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EndpointBatchRequest: EndpointBatchRequestTypeDef

class DeleteUserEndpointsResponseTypeDef(BaseModel):
    EndpointsResponse: EndpointsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserEndpointsResponseTypeDef(BaseModel):
    EndpointsResponse: EndpointsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InAppCampaignScheduleTypeDef(BaseModel):
    EndDate: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterOutputTypeDef] = None
    QuietTime: Optional[QuietTimeTypeDef] = None

class ScheduleOutputTypeDef(BaseModel):
    StartTime: str
    EndTime: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterOutputTypeDef] = None
    Frequency: Optional[FrequencyType] = None
    IsLocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    Timezone: Optional[str] = None

class EventStartConditionOutputTypeDef(BaseModel):
    EventFilter: Optional[EventFilterOutputTypeDef] = None
    SegmentId: Optional[str] = None

class ScheduleTypeDef(BaseModel):
    StartTime: str
    EndTime: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterTypeDef] = None
    Frequency: Optional[FrequencyType] = None
    IsLocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    Timezone: Optional[str] = None

class EventStartConditionTypeDef(BaseModel):
    EventFilter: Optional[EventFilterTypeDef] = None
    SegmentId: Optional[str] = None

class PutEventsResponseTypeDef(BaseModel):
    EventsResponse: EventsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventsRequestTypeDef(BaseModel):
    BatchItem: Mapping[str, EventsBatchTypeDef]

class GetExportJobsResponseTypeDef(BaseModel):
    ExportJobsResponse: ExportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentExportJobsResponseTypeDef(BaseModel):
    ExportJobsResponse: ExportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SegmentDimensionsOutputTypeDef(BaseModel):
    Attributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None
    Behavior: Optional[SegmentBehaviorsTypeDef] = None
    Demographic: Optional[SegmentDemographicsOutputTypeDef] = None
    Location: Optional[SegmentLocationOutputTypeDef] = None
    Metrics: Optional[Dict[str, MetricDimensionTypeDef]] = None
    UserAttributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None

class SegmentDimensionsTypeDef(BaseModel):
    Attributes: Optional[Mapping[str, AttributeDimensionTypeDef]] = None
    Behavior: Optional[SegmentBehaviorsTypeDef] = None
    Demographic: Optional[SegmentDemographicsTypeDef] = None
    Location: Optional[SegmentLocationTypeDef] = None
    Metrics: Optional[Mapping[str, MetricDimensionTypeDef]] = None
    UserAttributes: Optional[Mapping[str, AttributeDimensionTypeDef]] = None

class GetImportJobsResponseTypeDef(BaseModel):
    ImportJobsResponse: ImportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentImportJobsResponseTypeDef(BaseModel):
    ImportJobsResponse: ImportJobsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CampaignInAppMessageOutputTypeDef(BaseModel):
    Body: Optional[str] = None
    Content: Optional[List[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None

class CampaignInAppMessageTypeDef(BaseModel):
    Body: Optional[str] = None
    Content: Optional[Sequence[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Mapping[str, str]] = None
    Layout: Optional[LayoutType] = None

class InAppMessageTypeDef(BaseModel):
    Content: Optional[List[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None

class InAppTemplateRequestTypeDef(BaseModel):
    Content: Optional[Sequence[InAppMessageContentTypeDef]] = None
    CustomConfig: Optional[Mapping[str, str]] = None
    Layout: Optional[LayoutType] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None

class InAppTemplateResponseTypeDef(BaseModel):
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

class ApplicationDateRangeKpiResponseTypeDef(BaseModel):
    ApplicationId: str
    EndTime: datetime
    KpiName: str
    KpiResult: BaseKpiResultTypeDef
    StartTime: datetime
    NextToken: Optional[str] = None

class CampaignDateRangeKpiResponseTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str
    EndTime: datetime
    KpiName: str
    KpiResult: BaseKpiResultTypeDef
    StartTime: datetime
    NextToken: Optional[str] = None

class JourneyDateRangeKpiResponseTypeDef(BaseModel):
    ApplicationId: str
    EndTime: datetime
    JourneyId: str
    KpiName: str
    KpiResult: BaseKpiResultTypeDef
    StartTime: datetime
    NextToken: Optional[str] = None

class DirectMessageConfigurationTypeDef(BaseModel):
    ADMMessage: Optional[ADMMessageTypeDef] = None
    APNSMessage: Optional[APNSMessageTypeDef] = None
    BaiduMessage: Optional[BaiduMessageTypeDef] = None
    DefaultMessage: Optional[DefaultMessageTypeDef] = None
    DefaultPushNotificationMessage: Optional[DefaultPushNotificationMessageTypeDef] = None
    EmailMessage: Optional[EmailMessageTypeDef] = None
    GCMMessage: Optional[GCMMessageTypeDef] = None
    SMSMessage: Optional[SMSMessageTypeDef] = None
    VoiceMessage: Optional[VoiceMessageTypeDef] = None

class StartConditionOutputTypeDef(BaseModel):
    Description: Optional[str] = None
    EventStartCondition: Optional[EventStartConditionOutputTypeDef] = None
    SegmentStartCondition: Optional[SegmentConditionTypeDef] = None

class StartConditionTypeDef(BaseModel):
    Description: Optional[str] = None
    EventStartCondition: Optional[EventStartConditionTypeDef] = None
    SegmentStartCondition: Optional[SegmentConditionTypeDef] = None

class PutEventsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EventsRequest: EventsRequestTypeDef

class SegmentGroupOutputTypeDef(BaseModel):
    Dimensions: Optional[List[SegmentDimensionsOutputTypeDef]] = None
    SourceSegments: Optional[List[SegmentReferenceTypeDef]] = None
    SourceType: Optional[SourceTypeType] = None
    Type: Optional[TypeType] = None

class SimpleConditionOutputTypeDef(BaseModel):
    EventCondition: Optional[EventConditionOutputTypeDef] = None
    SegmentCondition: Optional[SegmentConditionTypeDef] = None
    SegmentDimensions: Optional[SegmentDimensionsOutputTypeDef] = None

class SegmentGroupTypeDef(BaseModel):
    Dimensions: Optional[Sequence[SegmentDimensionsTypeDef]] = None
    SourceSegments: Optional[Sequence[SegmentReferenceTypeDef]] = None
    SourceType: Optional[SourceTypeType] = None
    Type: Optional[TypeType] = None

class SimpleConditionTypeDef(BaseModel):
    EventCondition: Optional[EventConditionTypeDef] = None
    SegmentCondition: Optional[SegmentConditionTypeDef] = None
    SegmentDimensions: Optional[SegmentDimensionsTypeDef] = None

class MessageConfigurationOutputTypeDef(BaseModel):
    ADMMessage: Optional[MessageTypeDef] = None
    APNSMessage: Optional[MessageTypeDef] = None
    BaiduMessage: Optional[MessageTypeDef] = None
    CustomMessage: Optional[CampaignCustomMessageTypeDef] = None
    DefaultMessage: Optional[MessageTypeDef] = None
    EmailMessage: Optional[CampaignEmailMessageOutputTypeDef] = None
    GCMMessage: Optional[MessageTypeDef] = None
    SMSMessage: Optional[CampaignSmsMessageTypeDef] = None
    InAppMessage: Optional[CampaignInAppMessageOutputTypeDef] = None

class MessageConfigurationTypeDef(BaseModel):
    ADMMessage: Optional[MessageTypeDef] = None
    APNSMessage: Optional[MessageTypeDef] = None
    BaiduMessage: Optional[MessageTypeDef] = None
    CustomMessage: Optional[CampaignCustomMessageTypeDef] = None
    DefaultMessage: Optional[MessageTypeDef] = None
    EmailMessage: Optional[CampaignEmailMessageTypeDef] = None
    GCMMessage: Optional[MessageTypeDef] = None
    SMSMessage: Optional[CampaignSmsMessageTypeDef] = None
    InAppMessage: Optional[CampaignInAppMessageTypeDef] = None

class InAppMessageCampaignTypeDef(BaseModel):
    CampaignId: Optional[str] = None
    DailyCap: Optional[int] = None
    InAppMessage: Optional[InAppMessageTypeDef] = None
    Priority: Optional[int] = None
    Schedule: Optional[InAppCampaignScheduleTypeDef] = None
    SessionCap: Optional[int] = None
    TotalCap: Optional[int] = None
    TreatmentId: Optional[str] = None

class CreateInAppTemplateRequestRequestTypeDef(BaseModel):
    InAppTemplateRequest: InAppTemplateRequestTypeDef
    TemplateName: str

class UpdateInAppTemplateRequestRequestTypeDef(BaseModel):
    InAppTemplateRequest: InAppTemplateRequestTypeDef
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None

class GetInAppTemplateResponseTypeDef(BaseModel):
    InAppTemplateResponse: InAppTemplateResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationDateRangeKpiResponseTypeDef(BaseModel):
    ApplicationDateRangeKpiResponse: ApplicationDateRangeKpiResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignDateRangeKpiResponseTypeDef(BaseModel):
    CampaignDateRangeKpiResponse: CampaignDateRangeKpiResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJourneyDateRangeKpiResponseTypeDef(BaseModel):
    JourneyDateRangeKpiResponse: JourneyDateRangeKpiResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MessageRequestTypeDef(BaseModel):
    MessageConfiguration: DirectMessageConfigurationTypeDef
    Addresses: Optional[Mapping[str, AddressConfigurationTypeDef]] = None
    Context: Optional[Mapping[str, str]] = None
    Endpoints: Optional[Mapping[str, EndpointSendConfigurationTypeDef]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TraceId: Optional[str] = None

class SendUsersMessageRequestTypeDef(BaseModel):
    MessageConfiguration: DirectMessageConfigurationTypeDef
    Users: Mapping[str, EndpointSendConfigurationTypeDef]
    Context: Optional[Mapping[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TraceId: Optional[str] = None

class SegmentGroupListOutputTypeDef(BaseModel):
    Groups: Optional[List[SegmentGroupOutputTypeDef]] = None
    Include: Optional[IncludeType] = None

class ConditionOutputTypeDef(BaseModel):
    Conditions: Optional[List[SimpleConditionOutputTypeDef]] = None
    Operator: Optional[OperatorType] = None

class MultiConditionalBranchOutputTypeDef(BaseModel):
    Condition: Optional[SimpleConditionOutputTypeDef] = None
    NextActivity: Optional[str] = None

class SegmentGroupListTypeDef(BaseModel):
    Groups: Optional[Sequence[SegmentGroupTypeDef]] = None
    Include: Optional[IncludeType] = None

class ConditionTypeDef(BaseModel):
    Conditions: Optional[Sequence[SimpleConditionTypeDef]] = None
    Operator: Optional[OperatorType] = None

class MultiConditionalBranchTypeDef(BaseModel):
    Condition: Optional[SimpleConditionTypeDef] = None
    NextActivity: Optional[str] = None

class TreatmentResourceTypeDef(BaseModel):
    Id: str
    SizePercent: int
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationOutputTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationOutputTypeDef] = None
    Schedule: Optional[ScheduleOutputTypeDef] = None
    State: Optional[CampaignStateTypeDef] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None

class WriteTreatmentResourceTypeDef(BaseModel):
    SizePercent: int
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationTypeDef] = None
    Schedule: Optional[ScheduleTypeDef] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None

class InAppMessagesResponseTypeDef(BaseModel):
    InAppMessageCampaigns: Optional[List[InAppMessageCampaignTypeDef]] = None

class SendMessagesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    MessageRequest: MessageRequestTypeDef

class SendUsersMessagesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SendUsersMessageRequest: SendUsersMessageRequestTypeDef

class SegmentResponseTypeDef(BaseModel):
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

class ConditionalSplitActivityOutputTypeDef(BaseModel):
    Condition: Optional[ConditionOutputTypeDef] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None
    FalseActivity: Optional[str] = None
    TrueActivity: Optional[str] = None

class MultiConditionalSplitActivityOutputTypeDef(BaseModel):
    Branches: Optional[List[MultiConditionalBranchOutputTypeDef]] = None
    DefaultActivity: Optional[str] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None

class WriteSegmentRequestTypeDef(BaseModel):
    Dimensions: Optional[SegmentDimensionsTypeDef] = None
    Name: Optional[str] = None
    SegmentGroups: Optional[SegmentGroupListTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ConditionalSplitActivityTypeDef(BaseModel):
    Condition: Optional[ConditionTypeDef] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None
    FalseActivity: Optional[str] = None
    TrueActivity: Optional[str] = None

class MultiConditionalSplitActivityTypeDef(BaseModel):
    Branches: Optional[Sequence[MultiConditionalBranchTypeDef]] = None
    DefaultActivity: Optional[str] = None
    EvaluationWaitTime: Optional[WaitTimeTypeDef] = None

class CampaignResponseTypeDef(BaseModel):
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

class WriteCampaignRequestTypeDef(BaseModel):
    AdditionalTreatments: Optional[Sequence[WriteTreatmentResourceTypeDef]] = None
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationTypeDef] = None
    Description: Optional[str] = None
    HoldoutPercent: Optional[int] = None
    Hook: Optional[CampaignHookTypeDef] = None
    IsPaused: Optional[bool] = None
    Limits: Optional[CampaignLimitsTypeDef] = None
    MessageConfiguration: Optional[MessageConfigurationTypeDef] = None
    Name: Optional[str] = None
    Schedule: Optional[ScheduleTypeDef] = None
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None
    Priority: Optional[int] = None

class GetInAppMessagesResponseTypeDef(BaseModel):
    InAppMessagesResponse: InAppMessagesResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSegmentResponseTypeDef(BaseModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSegmentResponseTypeDef(BaseModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentResponseTypeDef(BaseModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentVersionResponseTypeDef(BaseModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SegmentsResponseTypeDef(BaseModel):
    Item: List[SegmentResponseTypeDef]
    NextToken: Optional[str] = None

class UpdateSegmentResponseTypeDef(BaseModel):
    SegmentResponse: SegmentResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActivityOutputTypeDef(BaseModel):
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

class CreateSegmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    WriteSegmentRequest: WriteSegmentRequestTypeDef

class UpdateSegmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    SegmentId: str
    WriteSegmentRequest: WriteSegmentRequestTypeDef

class ActivityTypeDef(BaseModel):
    CUSTOM: Optional[CustomMessageActivityTypeDef] = None
    ConditionalSplit: Optional[ConditionalSplitActivityTypeDef] = None
    Description: Optional[str] = None
    EMAIL: Optional[EmailMessageActivityTypeDef] = None
    Holdout: Optional[HoldoutActivityTypeDef] = None
    MultiCondition: Optional[MultiConditionalSplitActivityTypeDef] = None
    PUSH: Optional[PushMessageActivityTypeDef] = None
    RandomSplit: Optional[RandomSplitActivityTypeDef] = None
    SMS: Optional[SMSMessageActivityTypeDef] = None
    Wait: Optional[WaitActivityTypeDef] = None
    ContactCenter: Optional[ContactCenterActivityTypeDef] = None

class CampaignsResponseTypeDef(BaseModel):
    Item: List[CampaignResponseTypeDef]
    NextToken: Optional[str] = None

class CreateCampaignResponseTypeDef(BaseModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCampaignResponseTypeDef(BaseModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignResponseTypeDef(BaseModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignVersionResponseTypeDef(BaseModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCampaignResponseTypeDef(BaseModel):
    CampaignResponse: CampaignResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCampaignRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    WriteCampaignRequest: WriteCampaignRequestTypeDef

class UpdateCampaignRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    CampaignId: str
    WriteCampaignRequest: WriteCampaignRequestTypeDef

class GetSegmentVersionsResponseTypeDef(BaseModel):
    SegmentsResponse: SegmentsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentsResponseTypeDef(BaseModel):
    SegmentsResponse: SegmentsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JourneyResponseTypeDef(BaseModel):
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

class WriteJourneyRequestTypeDef(BaseModel):
    Name: str
    Activities: Optional[Mapping[str, ActivityTypeDef]] = None
    CreationDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[JourneyLimitsTypeDef] = None
    LocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTimeTypeDef] = None
    RefreshFrequency: Optional[str] = None
    Schedule: Optional[JourneyScheduleTypeDef] = None
    StartActivity: Optional[str] = None
    StartCondition: Optional[StartConditionTypeDef] = None
    State: Optional[StateType] = None
    WaitForQuietTime: Optional[bool] = None
    RefreshOnSegmentUpdate: Optional[bool] = None
    JourneyChannelSettings: Optional[JourneyChannelSettingsTypeDef] = None
    SendingSchedule: Optional[bool] = None
    OpenHours: Optional[OpenHoursTypeDef] = None
    ClosedDays: Optional[ClosedDaysTypeDef] = None
    TimezoneEstimationMethods: Optional[Sequence[TimezoneEstimationMethodsElementType]] = None

class GetCampaignVersionsResponseTypeDef(BaseModel):
    CampaignsResponse: CampaignsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignsResponseTypeDef(BaseModel):
    CampaignsResponse: CampaignsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJourneyResponseTypeDef(BaseModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJourneyResponseTypeDef(BaseModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJourneyResponseTypeDef(BaseModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JourneysResponseTypeDef(BaseModel):
    Item: List[JourneyResponseTypeDef]
    NextToken: Optional[str] = None

class UpdateJourneyResponseTypeDef(BaseModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJourneyStateResponseTypeDef(BaseModel):
    JourneyResponse: JourneyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJourneyRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    WriteJourneyRequest: WriteJourneyRequestTypeDef

class UpdateJourneyRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    JourneyId: str
    WriteJourneyRequest: WriteJourneyRequestTypeDef

class ListJourneysResponseTypeDef(BaseModel):
    JourneysResponse: JourneysResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

