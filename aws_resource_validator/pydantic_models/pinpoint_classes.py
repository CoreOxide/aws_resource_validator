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

class ADMChannelRequest(BaseValidatorModel):
    ClientId: str
    ClientSecret: str
    Enabled: Optional[bool] = None


class ADMChannelResponse(BaseValidatorModel):
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


class ADMMessage(BaseValidatorModel):
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


class APNSChannelRequest(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSChannelResponse(BaseValidatorModel):
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


class APNSMessage(BaseValidatorModel):
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


class APNSPushNotificationTemplate(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    MediaUrl: Optional[str] = None
    RawContent: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class APNSSandboxChannelRequest(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSSandboxChannelResponse(BaseValidatorModel):
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


class APNSVoipChannelRequest(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSVoipChannelResponse(BaseValidatorModel):
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


class APNSVoipSandboxChannelRequest(BaseValidatorModel):
    BundleId: Optional[str] = None
    Certificate: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    PrivateKey: Optional[str] = None
    TeamId: Optional[str] = None
    TokenKey: Optional[str] = None
    TokenKeyId: Optional[str] = None


class APNSVoipSandboxChannelResponse(BaseValidatorModel):
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


class ActivityResponse(BaseValidatorModel):
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


class ContactCenterActivity(BaseValidatorModel):
    NextActivity: Optional[str] = None


class HoldoutActivity(BaseValidatorModel):
    Percentage: int
    NextActivity: Optional[str] = None


class AddressConfiguration(BaseValidatorModel):
    BodyOverride: Optional[str] = None
    ChannelType: Optional[ChannelTypeType] = None
    Context: Optional[Mapping[str, str]] = None
    RawContent: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TitleOverride: Optional[str] = None


class AndroidPushNotificationTemplate(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    ImageIconUrl: Optional[str] = None
    ImageUrl: Optional[str] = None
    RawContent: Optional[str] = None
    SmallImageIconUrl: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class ApplicationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    tags: Optional[Dict[str, str]] = None
    CreationDate: Optional[str] = None


class JourneyTimeframeCap(BaseValidatorModel):
    Cap: Optional[int] = None
    Days: Optional[int] = None


class CampaignHook(BaseValidatorModel):
    LambdaFunctionName: Optional[str] = None
    Mode: Optional[ModeType] = None
    WebUrl: Optional[str] = None


class CampaignLimits(BaseValidatorModel):
    Daily: Optional[int] = None
    MaximumDuration: Optional[int] = None
    MessagesPerSecond: Optional[int] = None
    Total: Optional[int] = None
    Session: Optional[int] = None


class QuietTime(BaseValidatorModel):
    End: Optional[str] = None
    Start: Optional[str] = None


class AttributeDimensionOutput(BaseValidatorModel):
    Values: List[str]
    AttributeType: Optional[AttributeTypeType] = None


class AttributeDimension(BaseValidatorModel):
    Values: Sequence[str]
    AttributeType: Optional[AttributeTypeType] = None


class AttributesResource(BaseValidatorModel):
    ApplicationId: str
    AttributeType: str
    Attributes: Optional[List[str]] = None


class BaiduChannelRequest(BaseValidatorModel):
    ApiKey: str
    SecretKey: str
    Enabled: Optional[bool] = None


class BaiduChannelResponse(BaseValidatorModel):
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


class BaiduMessage(BaseValidatorModel):
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


class CampaignCustomMessage(BaseValidatorModel):
    Data: Optional[str] = None


class MessageHeader(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class CampaignState(BaseValidatorModel):
    CampaignStatus: Optional[CampaignStatusType] = None


class CustomDeliveryConfigurationOutput(BaseValidatorModel):
    DeliveryUri: str
    EndpointTypes: Optional[List[EndpointTypesElementType]] = None


class CampaignSmsMessage(BaseValidatorModel):
    Body: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None


class ChannelResponse(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    CreationDate: Optional[str] = None
    Enabled: Optional[bool] = None
    HasCredential: Optional[bool] = None
    Id: Optional[str] = None
    IsArchived: Optional[bool] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Version: Optional[int] = None


class ClosedDaysRule(BaseValidatorModel):
    Name: Optional[str] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None


class WaitTime(BaseValidatorModel):
    WaitFor: Optional[str] = None
    WaitUntil: Optional[str] = None


class CreateApplicationRequest(BaseValidatorModel):
    Name: str
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateTemplateMessageBody(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None
    RequestID: Optional[str] = None


class ExportJobRequest(BaseValidatorModel):
    RoleArn: str
    S3UrlPrefix: str
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None


class ImportJobRequest(BaseValidatorModel):
    Format: FormatType
    RoleArn: str
    S3Url: str
    DefineSegment: Optional[bool] = None
    ExternalId: Optional[str] = None
    RegisterEndpoints: Optional[bool] = None
    SegmentId: Optional[str] = None
    SegmentName: Optional[str] = None


class TemplateCreateMessageBody(BaseValidatorModel):
    Arn: Optional[str] = None
    Message: Optional[str] = None
    RequestID: Optional[str] = None


class CreateRecommenderConfiguration(BaseValidatorModel):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Mapping[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None


class RecommenderConfigurationResponse(BaseValidatorModel):
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


class SMSTemplateRequest(BaseValidatorModel):
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None


class VoiceTemplateRequest(BaseValidatorModel):
    Body: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    LanguageCode: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None
    VoiceId: Optional[str] = None


class CustomDeliveryConfiguration(BaseValidatorModel):
    DeliveryUri: str
    EndpointTypes: Optional[Sequence[EndpointTypesElementType]] = None


class JourneyCustomMessage(BaseValidatorModel):
    Data: Optional[str] = None


class DefaultMessage(BaseValidatorModel):
    Body: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None


class DefaultPushNotificationMessage(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Data: Optional[Mapping[str, str]] = None
    SilentPush: Optional[bool] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class DefaultPushNotificationTemplate(BaseValidatorModel):
    Action: Optional[ActionType] = None
    Body: Optional[str] = None
    Sound: Optional[str] = None
    Title: Optional[str] = None
    Url: Optional[str] = None


class DeleteAdmChannelRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsChannelRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsSandboxChannelRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsVoipChannelRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteApnsVoipSandboxChannelRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteAppRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteBaiduChannelRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteCampaignRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str


class DeleteEmailChannelRequest(BaseValidatorModel):
    ApplicationId: str


class EmailChannelResponse(BaseValidatorModel):
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


class DeleteEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class MessageBody(BaseValidatorModel):
    Message: Optional[str] = None
    RequestID: Optional[str] = None


class DeleteEndpointRequest(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str


class DeleteEventStreamRequest(BaseValidatorModel):
    ApplicationId: str


class EventStream(BaseValidatorModel):
    ApplicationId: str
    DestinationStreamArn: str
    RoleArn: str
    ExternalId: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    LastUpdatedBy: Optional[str] = None


class DeleteGcmChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GCMChannelResponse(BaseValidatorModel):
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


class DeleteInAppTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class DeleteJourneyRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str


class DeletePushTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class DeleteRecommenderConfigurationRequest(BaseValidatorModel):
    RecommenderId: str


class DeleteSegmentRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str


class DeleteSmsChannelRequest(BaseValidatorModel):
    ApplicationId: str


class SMSChannelResponse(BaseValidatorModel):
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


class DeleteSmsTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class DeleteUserEndpointsRequest(BaseValidatorModel):
    ApplicationId: str
    UserId: str


class DeleteVoiceChannelRequest(BaseValidatorModel):
    ApplicationId: str


class VoiceChannelResponse(BaseValidatorModel):
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


class DeleteVoiceTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GCMMessage(BaseValidatorModel):
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


class SMSMessage(BaseValidatorModel):
    Body: Optional[str] = None
    Keyword: Optional[str] = None
    MediaUrl: Optional[str] = None
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None


class VoiceMessage(BaseValidatorModel):
    Body: Optional[str] = None
    LanguageCode: Optional[str] = None
    OriginationNumber: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    VoiceId: Optional[str] = None


class EmailChannelRequest(BaseValidatorModel):
    FromAddress: str
    Identity: str
    ConfigurationSet: Optional[str] = None
    Enabled: Optional[bool] = None
    RoleArn: Optional[str] = None
    OrchestrationSendingRoleArn: Optional[str] = None


class JourneyEmailMessage(BaseValidatorModel):
    FromAddress: Optional[str] = None


class EndpointDemographic(BaseValidatorModel):
    AppVersion: Optional[str] = None
    Locale: Optional[str] = None
    Make: Optional[str] = None
    Model: Optional[str] = None
    ModelVersion: Optional[str] = None
    Platform: Optional[str] = None
    PlatformVersion: Optional[str] = None
    Timezone: Optional[str] = None


class EndpointLocation(BaseValidatorModel):
    City: Optional[str] = None
    Country: Optional[str] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    PostalCode: Optional[str] = None
    Region: Optional[str] = None


class EndpointItemResponse(BaseValidatorModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None


class EndpointMessageResult(BaseValidatorModel):
    DeliveryStatus: DeliveryStatusType
    StatusCode: int
    Address: Optional[str] = None
    MessageId: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdatedToken: Optional[str] = None


class EndpointUserOutput(BaseValidatorModel):
    UserAttributes: Optional[Dict[str, List[str]]] = None
    UserId: Optional[str] = None


class EndpointSendConfiguration(BaseValidatorModel):
    BodyOverride: Optional[str] = None
    Context: Optional[Mapping[str, str]] = None
    RawContent: Optional[str] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None
    TitleOverride: Optional[str] = None


class EndpointUser(BaseValidatorModel):
    UserAttributes: Optional[Mapping[str, Sequence[str]]] = None
    UserId: Optional[str] = None


class MetricDimension(BaseValidatorModel):
    ComparisonOperator: str
    Value: float


class SetDimensionOutput(BaseValidatorModel):
    Values: List[str]
    DimensionType: Optional[DimensionTypeType] = None


class EventItemResponse(BaseValidatorModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None


class Session(BaseValidatorModel):
    Id: str
    StartTimestamp: str
    Duration: Optional[int] = None
    StopTimestamp: Optional[str] = None


class ExportJobResource(BaseValidatorModel):
    RoleArn: str
    S3UrlPrefix: str
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None


class GCMChannelRequest(BaseValidatorModel):
    ApiKey: Optional[str] = None
    DefaultAuthenticationMethod: Optional[str] = None
    Enabled: Optional[bool] = None
    ServiceJson: Optional[str] = None


class GPSCoordinates(BaseValidatorModel):
    Latitude: float
    Longitude: float


class GetAdmChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetApnsChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetApnsSandboxChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetApnsVoipChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetApnsVoipSandboxChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetAppRequest(BaseValidatorModel):
    ApplicationId: str


class GetApplicationSettingsRequest(BaseValidatorModel):
    ApplicationId: str


class GetAppsRequest(BaseValidatorModel):
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetBaiduChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetCampaignActivitiesRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetCampaignRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str


class GetCampaignVersionRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    Version: str


class GetCampaignVersionsRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetCampaignsRequest(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetChannelsRequest(BaseValidatorModel):
    ApplicationId: str


class GetEmailChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetEmailTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GetEndpointRequest(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str


class GetEventStreamRequest(BaseValidatorModel):
    ApplicationId: str


class GetExportJobRequest(BaseValidatorModel):
    ApplicationId: str
    JobId: str


class GetExportJobsRequest(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetGcmChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetImportJobRequest(BaseValidatorModel):
    ApplicationId: str
    JobId: str


class GetImportJobsRequest(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetInAppMessagesRequest(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str


class GetInAppTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GetJourneyExecutionActivityMetricsRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyExecutionActivityMetricsResponse(BaseValidatorModel):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]


class GetJourneyExecutionMetricsRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyExecutionMetricsResponse(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]


class GetJourneyRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str


class GetJourneyRunExecutionActivityMetricsRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    RunId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyRunExecutionActivityMetricsResponse(BaseValidatorModel):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]
    RunId: str


class GetJourneyRunExecutionMetricsRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    RunId: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class JourneyRunExecutionMetricsResponse(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]
    RunId: str


class GetJourneyRunsRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetPushTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class GetRecommenderConfigurationRequest(BaseValidatorModel):
    RecommenderId: str


class GetRecommenderConfigurationsRequest(BaseValidatorModel):
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentExportJobsRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentImportJobsRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str


class GetSegmentVersionRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    Version: str


class GetSegmentVersionsRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSegmentsRequest(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class GetSmsChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetSmsTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class SMSTemplateResponse(BaseValidatorModel):
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


class GetUserEndpointsRequest(BaseValidatorModel):
    ApplicationId: str
    UserId: str


class GetVoiceChannelRequest(BaseValidatorModel):
    ApplicationId: str


class GetVoiceTemplateRequest(BaseValidatorModel):
    TemplateName: str
    Version: Optional[str] = None


class VoiceTemplateResponse(BaseValidatorModel):
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


class ImportJobResource(BaseValidatorModel):
    Format: FormatType
    RoleArn: str
    S3Url: str
    DefineSegment: Optional[bool] = None
    ExternalId: Optional[str] = None
    RegisterEndpoints: Optional[bool] = None
    SegmentId: Optional[str] = None
    SegmentName: Optional[str] = None


class InAppMessageBodyConfig(BaseValidatorModel):
    Alignment: AlignmentType
    Body: str
    TextColor: str


class OverrideButtonConfiguration(BaseValidatorModel):
    ButtonAction: ButtonActionType
    Link: Optional[str] = None


class InAppMessageHeaderConfig(BaseValidatorModel):
    Alignment: AlignmentType
    Header: str
    TextColor: str


class JourneyChannelSettings(BaseValidatorModel):
    ConnectCampaignArn: Optional[str] = None
    ConnectCampaignExecutionRoleArn: Optional[str] = None


class JourneyPushMessage(BaseValidatorModel):
    TimeToLive: Optional[str] = None


class JourneyScheduleOutput(BaseValidatorModel):
    EndTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    Timezone: Optional[str] = None


class JourneyRunResponse(BaseValidatorModel):
    CreationTime: str
    LastUpdateTime: str
    RunId: str
    Status: JourneyRunStatusType


class JourneySMSMessage(BaseValidatorModel):
    MessageType: Optional[MessageTypeType] = None
    OriginationNumber: Optional[str] = None
    SenderId: Optional[str] = None
    EntityId: Optional[str] = None
    TemplateId: Optional[str] = None


class JourneyStateRequest(BaseValidatorModel):
    State: Optional[StateType] = None


class ListJourneysRequest(BaseValidatorModel):
    ApplicationId: str
    PageSize: Optional[str] = None
    Token: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagsModelOutput(BaseValidatorModel):
    tags: Dict[str, str]


class ListTemplateVersionsRequest(BaseValidatorModel):
    TemplateName: str
    TemplateType: str
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None


class ListTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    Prefix: Optional[str] = None
    TemplateType: Optional[str] = None


class Message(BaseValidatorModel):
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


class MessageResult(BaseValidatorModel):
    DeliveryStatus: DeliveryStatusType
    StatusCode: int
    MessageId: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdatedToken: Optional[str] = None


class NumberValidateRequest(BaseValidatorModel):
    IsoCountryCode: Optional[str] = None
    PhoneNumber: Optional[str] = None


class NumberValidateResponse(BaseValidatorModel):
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


class OpenHoursRule(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None


class WriteEventStream(BaseValidatorModel):
    DestinationStreamArn: str
    RoleArn: str


class RandomSplitEntry(BaseValidatorModel):
    NextActivity: Optional[str] = None
    Percentage: Optional[int] = None


class RecencyDimension(BaseValidatorModel):
    Duration: DurationType
    RecencyType: RecencyTypeType


class UpdateAttributesRequest(BaseValidatorModel):
    Blacklist: Optional[Sequence[str]] = None


class SMSChannelRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SenderId: Optional[str] = None
    ShortCode: Optional[str] = None


class SegmentCondition(BaseValidatorModel):
    SegmentId: str


class SegmentReference(BaseValidatorModel):
    Id: str
    Version: Optional[int] = None


class SegmentImportResource(BaseValidatorModel):
    ExternalId: str
    Format: FormatType
    RoleArn: str
    S3Url: str
    Size: int
    ChannelCounts: Optional[Dict[str, int]] = None


class SendOTPMessageRequestParameters(BaseValidatorModel):
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


class SetDimension(BaseValidatorModel):
    Values: Sequence[str]
    DimensionType: Optional[DimensionTypeType] = None


class SimpleEmailPart(BaseValidatorModel):
    Charset: Optional[str] = None
    Data: Optional[str] = None


class TagsModel(BaseValidatorModel):
    tags: Mapping[str, str]


class TemplateActiveVersionRequest(BaseValidatorModel):
    Version: Optional[str] = None


class Template(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class TemplateResponse(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class TemplateVersionResponse(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: str
    DefaultSubstitutions: Optional[str] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateRecommenderConfiguration(BaseValidatorModel):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str
    Attributes: Optional[Mapping[str, str]] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    RecommendationProviderIdType: Optional[str] = None
    RecommendationTransformerUri: Optional[str] = None
    RecommendationsDisplayName: Optional[str] = None
    RecommendationsPerMessage: Optional[int] = None


class VoiceChannelRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None


class VerificationResponse(BaseValidatorModel):
    Valid: Optional[bool] = None


class VerifyOTPMessageRequestParameters(BaseValidatorModel):
    DestinationIdentity: str
    Otp: str
    ReferenceId: str


class UpdateAdmChannelRequest(BaseValidatorModel):
    ADMChannelRequest: ADMChannelRequest
    ApplicationId: str


class UpdateApnsChannelRequest(BaseValidatorModel):
    APNSChannelRequest: APNSChannelRequest
    ApplicationId: str


class UpdateApnsSandboxChannelRequest(BaseValidatorModel):
    APNSSandboxChannelRequest: APNSSandboxChannelRequest
    ApplicationId: str


class UpdateApnsVoipChannelRequest(BaseValidatorModel):
    APNSVoipChannelRequest: APNSVoipChannelRequest
    ApplicationId: str


class UpdateApnsVoipSandboxChannelRequest(BaseValidatorModel):
    APNSVoipSandboxChannelRequest: APNSVoipSandboxChannelRequest
    ApplicationId: str


class ActivitiesResponse(BaseValidatorModel):
    Item: List[ActivityResponse]
    NextToken: Optional[str] = None


class ApplicationsResponse(BaseValidatorModel):
    Item: Optional[List[ApplicationResponse]] = None
    NextToken: Optional[str] = None


class ApplicationSettingsJourneyLimits(BaseValidatorModel):
    DailyCap: Optional[int] = None
    TimeframeCap: Optional[JourneyTimeframeCap] = None
    TotalCap: Optional[int] = None


class JourneyLimits(BaseValidatorModel):
    DailyCap: Optional[int] = None
    EndpointReentryCap: Optional[int] = None
    MessagesPerSecond: Optional[int] = None
    EndpointReentryInterval: Optional[str] = None
    TimeframeCap: Optional[JourneyTimeframeCap] = None
    TotalCap: Optional[int] = None


class UpdateBaiduChannelRequest(BaseValidatorModel):
    ApplicationId: str
    BaiduChannelRequest: BaiduChannelRequest


class Blob(BaseValidatorModel):
    pass


class RawEmail(BaseValidatorModel):
    Data: Optional[Blob] = None


class CampaignEmailMessageOutput(BaseValidatorModel):
    Body: Optional[str] = None
    FromAddress: Optional[str] = None
    Headers: Optional[List[MessageHeader]] = None
    HtmlBody: Optional[str] = None
    Title: Optional[str] = None


class CampaignEmailMessage(BaseValidatorModel):
    Body: Optional[str] = None
    FromAddress: Optional[str] = None
    Headers: Optional[Sequence[MessageHeader]] = None
    HtmlBody: Optional[str] = None
    Title: Optional[str] = None


class EmailTemplateRequest(BaseValidatorModel):
    DefaultSubstitutions: Optional[str] = None
    HtmlPart: Optional[str] = None
    RecommenderId: Optional[str] = None
    Subject: Optional[str] = None
    Headers: Optional[Sequence[MessageHeader]] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None
    TextPart: Optional[str] = None


class EmailTemplateResponse(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    DefaultSubstitutions: Optional[str] = None
    HtmlPart: Optional[str] = None
    RecommenderId: Optional[str] = None
    Subject: Optional[str] = None
    Headers: Optional[List[MessageHeader]] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    TextPart: Optional[str] = None
    Version: Optional[str] = None


class ChannelsResponse(BaseValidatorModel):
    Channels: Dict[str, ChannelResponse]


class ClosedDaysOutput(BaseValidatorModel):
    EMAIL: Optional[List[ClosedDaysRule]] = None
    SMS: Optional[List[ClosedDaysRule]] = None
    PUSH: Optional[List[ClosedDaysRule]] = None
    VOICE: Optional[List[ClosedDaysRule]] = None
    CUSTOM: Optional[List[ClosedDaysRule]] = None


class ClosedDays(BaseValidatorModel):
    EMAIL: Optional[Sequence[ClosedDaysRule]] = None
    SMS: Optional[Sequence[ClosedDaysRule]] = None
    PUSH: Optional[Sequence[ClosedDaysRule]] = None
    VOICE: Optional[Sequence[ClosedDaysRule]] = None
    CUSTOM: Optional[Sequence[ClosedDaysRule]] = None


class WaitActivity(BaseValidatorModel):
    NextActivity: Optional[str] = None
    WaitTime: Optional[WaitTime] = None


class CreateAppRequest(BaseValidatorModel):
    CreateApplicationRequest: CreateApplicationRequest


class CreateAppResponse(BaseValidatorModel):
    ApplicationResponse: ApplicationResponse
    ResponseMetadata: ResponseMetadata


class DeleteAdmChannelResponse(BaseValidatorModel):
    ADMChannelResponse: ADMChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteApnsChannelResponse(BaseValidatorModel):
    APNSChannelResponse: APNSChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteApnsSandboxChannelResponse(BaseValidatorModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteApnsVoipChannelResponse(BaseValidatorModel):
    APNSVoipChannelResponse: APNSVoipChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteApnsVoipSandboxChannelResponse(BaseValidatorModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteAppResponse(BaseValidatorModel):
    ApplicationResponse: ApplicationResponse
    ResponseMetadata: ResponseMetadata


class DeleteBaiduChannelResponse(BaseValidatorModel):
    BaiduChannelResponse: BaiduChannelResponse
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAdmChannelResponse(BaseValidatorModel):
    ADMChannelResponse: ADMChannelResponse
    ResponseMetadata: ResponseMetadata


class GetApnsChannelResponse(BaseValidatorModel):
    APNSChannelResponse: APNSChannelResponse
    ResponseMetadata: ResponseMetadata


class GetApnsSandboxChannelResponse(BaseValidatorModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponse
    ResponseMetadata: ResponseMetadata


class GetApnsVoipChannelResponse(BaseValidatorModel):
    APNSVoipChannelResponse: APNSVoipChannelResponse
    ResponseMetadata: ResponseMetadata


class GetApnsVoipSandboxChannelResponse(BaseValidatorModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponse
    ResponseMetadata: ResponseMetadata


class GetAppResponse(BaseValidatorModel):
    ApplicationResponse: ApplicationResponse
    ResponseMetadata: ResponseMetadata


class GetBaiduChannelResponse(BaseValidatorModel):
    BaiduChannelResponse: BaiduChannelResponse
    ResponseMetadata: ResponseMetadata


class RemoveAttributesResponse(BaseValidatorModel):
    AttributesResource: AttributesResource
    ResponseMetadata: ResponseMetadata


class UpdateAdmChannelResponse(BaseValidatorModel):
    ADMChannelResponse: ADMChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateApnsChannelResponse(BaseValidatorModel):
    APNSChannelResponse: APNSChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateApnsSandboxChannelResponse(BaseValidatorModel):
    APNSSandboxChannelResponse: APNSSandboxChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateApnsVoipChannelResponse(BaseValidatorModel):
    APNSVoipChannelResponse: APNSVoipChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateApnsVoipSandboxChannelResponse(BaseValidatorModel):
    APNSVoipSandboxChannelResponse: APNSVoipSandboxChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateBaiduChannelResponse(BaseValidatorModel):
    BaiduChannelResponse: BaiduChannelResponse
    ResponseMetadata: ResponseMetadata


class CreateEmailTemplateResponse(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBody
    ResponseMetadata: ResponseMetadata


class CreatePushTemplateResponse(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBody
    ResponseMetadata: ResponseMetadata


class CreateSmsTemplateResponse(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBody
    ResponseMetadata: ResponseMetadata


class CreateVoiceTemplateResponse(BaseValidatorModel):
    CreateTemplateMessageBody: CreateTemplateMessageBody
    ResponseMetadata: ResponseMetadata


class CreateExportJobRequest(BaseValidatorModel):
    ApplicationId: str
    ExportJobRequest: ExportJobRequest


class CreateImportJobRequest(BaseValidatorModel):
    ApplicationId: str
    ImportJobRequest: ImportJobRequest


class CreateInAppTemplateResponse(BaseValidatorModel):
    TemplateCreateMessageBody: TemplateCreateMessageBody
    ResponseMetadata: ResponseMetadata


class CreateRecommenderConfigurationRequest(BaseValidatorModel):
    CreateRecommenderConfiguration: CreateRecommenderConfiguration


class CreateRecommenderConfigurationResponse(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponse
    ResponseMetadata: ResponseMetadata


class DeleteRecommenderConfigurationResponse(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponse
    ResponseMetadata: ResponseMetadata


class GetRecommenderConfigurationResponse(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponse
    ResponseMetadata: ResponseMetadata


class ListRecommenderConfigurationsResponse(BaseValidatorModel):
    Item: List[RecommenderConfigurationResponse]
    NextToken: Optional[str] = None


class UpdateRecommenderConfigurationResponse(BaseValidatorModel):
    RecommenderConfigurationResponse: RecommenderConfigurationResponse
    ResponseMetadata: ResponseMetadata


class CreateSmsTemplateRequest(BaseValidatorModel):
    SMSTemplateRequest: SMSTemplateRequest
    TemplateName: str


class UpdateSmsTemplateRequest(BaseValidatorModel):
    SMSTemplateRequest: SMSTemplateRequest
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class CreateVoiceTemplateRequest(BaseValidatorModel):
    TemplateName: str
    VoiceTemplateRequest: VoiceTemplateRequest


class UpdateVoiceTemplateRequest(BaseValidatorModel):
    TemplateName: str
    VoiceTemplateRequest: VoiceTemplateRequest
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class CustomMessageActivityOutput(BaseValidatorModel):
    DeliveryUri: Optional[str] = None
    EndpointTypes: Optional[List[EndpointTypesElementType]] = None
    MessageConfig: Optional[JourneyCustomMessage] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class CustomMessageActivity(BaseValidatorModel):
    DeliveryUri: Optional[str] = None
    EndpointTypes: Optional[Sequence[EndpointTypesElementType]] = None
    MessageConfig: Optional[JourneyCustomMessage] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class PushNotificationTemplateRequest(BaseValidatorModel):
    ADM: Optional[AndroidPushNotificationTemplate] = None
    APNS: Optional[APNSPushNotificationTemplate] = None
    Baidu: Optional[AndroidPushNotificationTemplate] = None
    Default: Optional[DefaultPushNotificationTemplate] = None
    DefaultSubstitutions: Optional[str] = None
    GCM: Optional[AndroidPushNotificationTemplate] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None


class PushNotificationTemplateResponse(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    ADM: Optional[AndroidPushNotificationTemplate] = None
    APNS: Optional[APNSPushNotificationTemplate] = None
    Arn: Optional[str] = None
    Baidu: Optional[AndroidPushNotificationTemplate] = None
    Default: Optional[DefaultPushNotificationTemplate] = None
    DefaultSubstitutions: Optional[str] = None
    GCM: Optional[AndroidPushNotificationTemplate] = None
    RecommenderId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class DeleteEmailChannelResponse(BaseValidatorModel):
    EmailChannelResponse: EmailChannelResponse
    ResponseMetadata: ResponseMetadata


class GetEmailChannelResponse(BaseValidatorModel):
    EmailChannelResponse: EmailChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateEmailChannelResponse(BaseValidatorModel):
    EmailChannelResponse: EmailChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteEmailTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class DeleteInAppTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class DeletePushTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class DeleteSmsTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class DeleteVoiceTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateEmailTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateEndpointResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateEndpointsBatchResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateInAppTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdatePushTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateSmsTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateTemplateActiveVersionResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class UpdateVoiceTemplateResponse(BaseValidatorModel):
    MessageBody: MessageBody
    ResponseMetadata: ResponseMetadata


class DeleteEventStreamResponse(BaseValidatorModel):
    EventStream: EventStream
    ResponseMetadata: ResponseMetadata


class GetEventStreamResponse(BaseValidatorModel):
    EventStream: EventStream
    ResponseMetadata: ResponseMetadata


class PutEventStreamResponse(BaseValidatorModel):
    EventStream: EventStream
    ResponseMetadata: ResponseMetadata


class DeleteGcmChannelResponse(BaseValidatorModel):
    GCMChannelResponse: GCMChannelResponse
    ResponseMetadata: ResponseMetadata


class GetGcmChannelResponse(BaseValidatorModel):
    GCMChannelResponse: GCMChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateGcmChannelResponse(BaseValidatorModel):
    GCMChannelResponse: GCMChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteSmsChannelResponse(BaseValidatorModel):
    SMSChannelResponse: SMSChannelResponse
    ResponseMetadata: ResponseMetadata


class GetSmsChannelResponse(BaseValidatorModel):
    SMSChannelResponse: SMSChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateSmsChannelResponse(BaseValidatorModel):
    SMSChannelResponse: SMSChannelResponse
    ResponseMetadata: ResponseMetadata


class DeleteVoiceChannelResponse(BaseValidatorModel):
    VoiceChannelResponse: VoiceChannelResponse
    ResponseMetadata: ResponseMetadata


class GetVoiceChannelResponse(BaseValidatorModel):
    VoiceChannelResponse: VoiceChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateVoiceChannelResponse(BaseValidatorModel):
    VoiceChannelResponse: VoiceChannelResponse
    ResponseMetadata: ResponseMetadata


class UpdateEmailChannelRequest(BaseValidatorModel):
    ApplicationId: str
    EmailChannelRequest: EmailChannelRequest


class EmailMessageActivity(BaseValidatorModel):
    MessageConfig: Optional[JourneyEmailMessage] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class SendUsersMessageResponse(BaseValidatorModel):
    ApplicationId: str
    RequestId: Optional[str] = None
    Result: Optional[Dict[str, Dict[str, EndpointMessageResult]]] = None


class EndpointResponse(BaseValidatorModel):
    Address: Optional[str] = None
    ApplicationId: Optional[str] = None
    Attributes: Optional[Dict[str, List[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    CohortId: Optional[str] = None
    CreationDate: Optional[str] = None
    Demographic: Optional[EndpointDemographic] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Id: Optional[str] = None
    Location: Optional[EndpointLocation] = None
    Metrics: Optional[Dict[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserOutput] = None


class EventDimensionsOutput(BaseValidatorModel):
    Attributes: Optional[Dict[str, AttributeDimensionOutput]] = None
    EventType: Optional[SetDimensionOutput] = None
    Metrics: Optional[Dict[str, MetricDimension]] = None


class SegmentDemographicsOutput(BaseValidatorModel):
    AppVersion: Optional[SetDimensionOutput] = None
    Channel: Optional[SetDimensionOutput] = None
    DeviceType: Optional[SetDimensionOutput] = None
    Make: Optional[SetDimensionOutput] = None
    Model: Optional[SetDimensionOutput] = None
    Platform: Optional[SetDimensionOutput] = None


class ItemResponse(BaseValidatorModel):
    EndpointItemResponse: Optional[EndpointItemResponse] = None
    EventsItemResponse: Optional[Dict[str, EventItemResponse]] = None


class Event(BaseValidatorModel):
    EventType: str
    Timestamp: str
    AppPackageName: Optional[str] = None
    AppTitle: Optional[str] = None
    AppVersionCode: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    ClientSdkVersion: Optional[str] = None
    Metrics: Optional[Mapping[str, float]] = None
    SdkName: Optional[str] = None
    Session: Optional[Session] = None


class UpdateGcmChannelRequest(BaseValidatorModel):
    ApplicationId: str
    GCMChannelRequest: GCMChannelRequest


class GPSPointDimension(BaseValidatorModel):
    Coordinates: GPSCoordinates
    RangeInKilometers: Optional[float] = None


class Timestamp(BaseValidatorModel):
    pass


class GetApplicationDateRangeKpiRequest(BaseValidatorModel):
    ApplicationId: str
    KpiName: str
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[Timestamp] = None


class GetCampaignDateRangeKpiRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    KpiName: str
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[Timestamp] = None


class GetJourneyDateRangeKpiRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    KpiName: str
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    PageSize: Optional[str] = None
    StartTime: Optional[Timestamp] = None


class JourneySchedule(BaseValidatorModel):
    EndTime: Optional[Timestamp] = None
    StartTime: Optional[Timestamp] = None
    Timezone: Optional[str] = None


class GetJourneyExecutionActivityMetricsResponse(BaseValidatorModel):
    JourneyExecutionActivityMetricsResponse: JourneyExecutionActivityMetricsResponse
    ResponseMetadata: ResponseMetadata


class GetJourneyExecutionMetricsResponse(BaseValidatorModel):
    JourneyExecutionMetricsResponse: JourneyExecutionMetricsResponse
    ResponseMetadata: ResponseMetadata


class GetJourneyRunExecutionActivityMetricsResponse(BaseValidatorModel):
    JourneyRunExecutionActivityMetricsResponse: JourneyRunExecutionActivityMetricsResponse
    ResponseMetadata: ResponseMetadata


class GetJourneyRunExecutionMetricsResponse(BaseValidatorModel):
    JourneyRunExecutionMetricsResponse: JourneyRunExecutionMetricsResponse
    ResponseMetadata: ResponseMetadata


class GetSmsTemplateResponse(BaseValidatorModel):
    SMSTemplateResponse: SMSTemplateResponse
    ResponseMetadata: ResponseMetadata


class GetVoiceTemplateResponse(BaseValidatorModel):
    VoiceTemplateResponse: VoiceTemplateResponse
    ResponseMetadata: ResponseMetadata


class DefaultButtonConfiguration(BaseValidatorModel):
    pass


class InAppMessageButton(BaseValidatorModel):
    Android: Optional[OverrideButtonConfiguration] = None
    DefaultConfig: Optional[DefaultButtonConfiguration] = None
    IOS: Optional[OverrideButtonConfiguration] = None
    Web: Optional[OverrideButtonConfiguration] = None


class PushMessageActivity(BaseValidatorModel):
    MessageConfig: Optional[JourneyPushMessage] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class JourneyRunsResponse(BaseValidatorModel):
    Item: List[JourneyRunResponse]
    NextToken: Optional[str] = None


class SMSMessageActivity(BaseValidatorModel):
    MessageConfig: Optional[JourneySMSMessage] = None
    NextActivity: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateVersion: Optional[str] = None


class UpdateJourneyStateRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    JourneyStateRequest: JourneyStateRequest


class ListTagsForResourceResponse(BaseValidatorModel):
    TagsModel: TagsModelOutput
    ResponseMetadata: ResponseMetadata


class MessageResponse(BaseValidatorModel):
    ApplicationId: str
    EndpointResult: Optional[Dict[str, EndpointMessageResult]] = None
    RequestId: Optional[str] = None
    Result: Optional[Dict[str, MessageResult]] = None


class PhoneNumberValidateRequest(BaseValidatorModel):
    NumberValidateRequest: NumberValidateRequest


class PhoneNumberValidateResponse(BaseValidatorModel):
    NumberValidateResponse: NumberValidateResponse
    ResponseMetadata: ResponseMetadata


class OpenHoursOutput(BaseValidatorModel):
    EMAIL: Optional[Dict[DayOfWeekType, List[OpenHoursRule]]] = None
    SMS: Optional[Dict[DayOfWeekType, List[OpenHoursRule]]] = None
    PUSH: Optional[Dict[DayOfWeekType, List[OpenHoursRule]]] = None
    VOICE: Optional[Dict[DayOfWeekType, List[OpenHoursRule]]] = None
    CUSTOM: Optional[Dict[DayOfWeekType, List[OpenHoursRule]]] = None


class OpenHours(BaseValidatorModel):
    EMAIL: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRule]]] = None
    SMS: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRule]]] = None
    PUSH: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRule]]] = None
    VOICE: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRule]]] = None
    CUSTOM: Optional[Mapping[DayOfWeekType, Sequence[OpenHoursRule]]] = None


class PutEventStreamRequest(BaseValidatorModel):
    ApplicationId: str
    WriteEventStream: WriteEventStream


class RandomSplitActivityOutput(BaseValidatorModel):
    Branches: Optional[List[RandomSplitEntry]] = None


class RandomSplitActivity(BaseValidatorModel):
    Branches: Optional[Sequence[RandomSplitEntry]] = None


class SegmentBehaviors(BaseValidatorModel):
    Recency: Optional[RecencyDimension] = None


class RemoveAttributesRequest(BaseValidatorModel):
    ApplicationId: str
    AttributeType: str
    UpdateAttributesRequest: UpdateAttributesRequest


class ResultRowValue(BaseValidatorModel):
    pass


class ResultRow(BaseValidatorModel):
    GroupedBys: List[ResultRowValue]
    Values: List[ResultRowValue]


class UpdateSmsChannelRequest(BaseValidatorModel):
    ApplicationId: str
    SMSChannelRequest: SMSChannelRequest


class SendOTPMessageRequest(BaseValidatorModel):
    ApplicationId: str
    SendOTPMessageRequestParameters: SendOTPMessageRequestParameters


class SimpleEmail(BaseValidatorModel):
    HtmlPart: Optional[SimpleEmailPart] = None
    Subject: Optional[SimpleEmailPart] = None
    TextPart: Optional[SimpleEmailPart] = None
    Headers: Optional[Sequence[MessageHeader]] = None


class UpdateTemplateActiveVersionRequest(BaseValidatorModel):
    TemplateActiveVersionRequest: TemplateActiveVersionRequest
    TemplateName: str
    TemplateType: str


class TemplateConfiguration(BaseValidatorModel):
    EmailTemplate: Optional[Template] = None
    PushTemplate: Optional[Template] = None
    SMSTemplate: Optional[Template] = None
    VoiceTemplate: Optional[Template] = None
    InAppTemplate: Optional[Template] = None


class TemplatesResponse(BaseValidatorModel):
    Item: List[TemplateResponse]
    NextToken: Optional[str] = None


class TemplateVersionsResponse(BaseValidatorModel):
    Item: List[TemplateVersionResponse]
    Message: Optional[str] = None
    NextToken: Optional[str] = None
    RequestID: Optional[str] = None


class UpdateRecommenderConfigurationRequest(BaseValidatorModel):
    RecommenderId: str
    UpdateRecommenderConfiguration: UpdateRecommenderConfiguration


class UpdateVoiceChannelRequest(BaseValidatorModel):
    ApplicationId: str
    VoiceChannelRequest: VoiceChannelRequest


class VerifyOTPMessageResponse(BaseValidatorModel):
    VerificationResponse: VerificationResponse
    ResponseMetadata: ResponseMetadata


class VerifyOTPMessageRequest(BaseValidatorModel):
    ApplicationId: str
    VerifyOTPMessageRequestParameters: VerifyOTPMessageRequestParameters


class GetCampaignActivitiesResponse(BaseValidatorModel):
    ActivitiesResponse: ActivitiesResponse
    ResponseMetadata: ResponseMetadata


class GetAppsResponse(BaseValidatorModel):
    ApplicationsResponse: ApplicationsResponse
    ResponseMetadata: ResponseMetadata


class ApplicationSettingsResource(BaseValidatorModel):
    ApplicationId: str
    CampaignHook: Optional[CampaignHook] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[CampaignLimits] = None
    QuietTime: Optional[QuietTime] = None
    JourneyLimits: Optional[ApplicationSettingsJourneyLimits] = None


class WriteApplicationSettingsRequest(BaseValidatorModel):
    CampaignHook: Optional[CampaignHook] = None
    CloudWatchMetricsEnabled: Optional[bool] = None
    EventTaggingEnabled: Optional[bool] = None
    Limits: Optional[CampaignLimits] = None
    QuietTime: Optional[QuietTime] = None
    JourneyLimits: Optional[ApplicationSettingsJourneyLimits] = None


class CreateEmailTemplateRequest(BaseValidatorModel):
    EmailTemplateRequest: EmailTemplateRequest
    TemplateName: str


class UpdateEmailTemplateRequest(BaseValidatorModel):
    EmailTemplateRequest: EmailTemplateRequest
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class GetEmailTemplateResponse(BaseValidatorModel):
    EmailTemplateResponse: EmailTemplateResponse
    ResponseMetadata: ResponseMetadata


class GetChannelsResponse(BaseValidatorModel):
    ChannelsResponse: ChannelsResponse
    ResponseMetadata: ResponseMetadata


class GetRecommenderConfigurationsResponse(BaseValidatorModel):
    ListRecommenderConfigurationsResponse: ListRecommenderConfigurationsResponse
    ResponseMetadata: ResponseMetadata


class CreatePushTemplateRequest(BaseValidatorModel):
    PushNotificationTemplateRequest: PushNotificationTemplateRequest
    TemplateName: str


class UpdatePushTemplateRequest(BaseValidatorModel):
    PushNotificationTemplateRequest: PushNotificationTemplateRequest
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class GetPushTemplateResponse(BaseValidatorModel):
    PushNotificationTemplateResponse: PushNotificationTemplateResponse
    ResponseMetadata: ResponseMetadata


class SendUsersMessagesResponse(BaseValidatorModel):
    SendUsersMessageResponse: SendUsersMessageResponse
    ResponseMetadata: ResponseMetadata


class DeleteEndpointResponse(BaseValidatorModel):
    EndpointResponse: EndpointResponse
    ResponseMetadata: ResponseMetadata


class EndpointsResponse(BaseValidatorModel):
    Item: List[EndpointResponse]


class GetEndpointResponse(BaseValidatorModel):
    EndpointResponse: EndpointResponse
    ResponseMetadata: ResponseMetadata


class EndpointUserUnion(BaseValidatorModel):
    pass


class EndpointBatchItem(BaseValidatorModel):
    Address: Optional[str] = None
    Attributes: Optional[Mapping[str, Sequence[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    Demographic: Optional[EndpointDemographic] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Id: Optional[str] = None
    Location: Optional[EndpointLocation] = None
    Metrics: Optional[Mapping[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserUnion] = None


class EndpointRequest(BaseValidatorModel):
    Address: Optional[str] = None
    Attributes: Optional[Mapping[str, Sequence[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    Demographic: Optional[EndpointDemographic] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Location: Optional[EndpointLocation] = None
    Metrics: Optional[Mapping[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserUnion] = None


class PublicEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Attributes: Optional[Mapping[str, Sequence[str]]] = None
    ChannelType: Optional[ChannelTypeType] = None
    Demographic: Optional[EndpointDemographic] = None
    EffectiveDate: Optional[str] = None
    EndpointStatus: Optional[str] = None
    Location: Optional[EndpointLocation] = None
    Metrics: Optional[Mapping[str, float]] = None
    OptOut: Optional[str] = None
    RequestId: Optional[str] = None
    User: Optional[EndpointUserUnion] = None


class CampaignEventFilterOutput(BaseValidatorModel):
    Dimensions: EventDimensionsOutput
    FilterType: FilterTypeType


class EventConditionOutput(BaseValidatorModel):
    Dimensions: Optional[EventDimensionsOutput] = None
    MessageActivity: Optional[str] = None


class EventFilterOutput(BaseValidatorModel):
    Dimensions: EventDimensionsOutput
    FilterType: FilterTypeType


class EventsResponse(BaseValidatorModel):
    Results: Optional[Dict[str, ItemResponse]] = None


class ExportJobResponse(BaseValidatorModel):
    pass


class CreateExportJobResponse(BaseValidatorModel):
    ExportJobResponse: ExportJobResponse
    ResponseMetadata: ResponseMetadata


class ExportJobsResponse(BaseValidatorModel):
    Item: List[ExportJobResponse]
    NextToken: Optional[str] = None


class GetExportJobResponse(BaseValidatorModel):
    ExportJobResponse: ExportJobResponse
    ResponseMetadata: ResponseMetadata


class SegmentLocationOutput(BaseValidatorModel):
    Country: Optional[SetDimensionOutput] = None
    GPSPoint: Optional[GPSPointDimension] = None


class ImportJobResponse(BaseValidatorModel):
    pass


class CreateImportJobResponse(BaseValidatorModel):
    ImportJobResponse: ImportJobResponse
    ResponseMetadata: ResponseMetadata


class GetImportJobResponse(BaseValidatorModel):
    ImportJobResponse: ImportJobResponse
    ResponseMetadata: ResponseMetadata


class ImportJobsResponse(BaseValidatorModel):
    Item: List[ImportJobResponse]
    NextToken: Optional[str] = None


class InAppMessageContent(BaseValidatorModel):
    BackgroundColor: Optional[str] = None
    BodyConfig: Optional[InAppMessageBodyConfig] = None
    HeaderConfig: Optional[InAppMessageHeaderConfig] = None
    ImageUrl: Optional[str] = None
    PrimaryBtn: Optional[InAppMessageButton] = None
    SecondaryBtn: Optional[InAppMessageButton] = None


class GetJourneyRunsResponse(BaseValidatorModel):
    JourneyRunsResponse: JourneyRunsResponse
    ResponseMetadata: ResponseMetadata


class SendMessagesResponse(BaseValidatorModel):
    MessageResponse: MessageResponse
    ResponseMetadata: ResponseMetadata


class SendOTPMessageResponse(BaseValidatorModel):
    MessageResponse: MessageResponse
    ResponseMetadata: ResponseMetadata


class BaseKpiResult(BaseValidatorModel):
    Rows: List[ResultRow]


class AttributeDimensionUnion(BaseValidatorModel):
    pass


class SetDimensionUnion(BaseValidatorModel):
    pass


class EventDimensions(BaseValidatorModel):
    Attributes: Optional[Mapping[str, AttributeDimensionUnion]] = None
    EventType: Optional[SetDimensionUnion] = None
    Metrics: Optional[Mapping[str, MetricDimension]] = None


class SegmentDemographics(BaseValidatorModel):
    AppVersion: Optional[SetDimensionUnion] = None
    Channel: Optional[SetDimensionUnion] = None
    DeviceType: Optional[SetDimensionUnion] = None
    Make: Optional[SetDimensionUnion] = None
    Model: Optional[SetDimensionUnion] = None
    Platform: Optional[SetDimensionUnion] = None


class SegmentLocation(BaseValidatorModel):
    Country: Optional[SetDimensionUnion] = None
    GPSPoint: Optional[GPSPointDimension] = None


class EmailMessage(BaseValidatorModel):
    Body: Optional[str] = None
    FeedbackForwardingAddress: Optional[str] = None
    FromAddress: Optional[str] = None
    RawEmail: Optional[RawEmail] = None
    ReplyToAddresses: Optional[Sequence[str]] = None
    SimpleEmail: Optional[SimpleEmail] = None
    Substitutions: Optional[Mapping[str, Sequence[str]]] = None


class TagsModelUnion(BaseValidatorModel):
    pass


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagsModel: TagsModelUnion


class ListTemplatesResponse(BaseValidatorModel):
    TemplatesResponse: TemplatesResponse
    ResponseMetadata: ResponseMetadata


class ListTemplateVersionsResponse(BaseValidatorModel):
    TemplateVersionsResponse: TemplateVersionsResponse
    ResponseMetadata: ResponseMetadata


class GetApplicationSettingsResponse(BaseValidatorModel):
    ApplicationSettingsResource: ApplicationSettingsResource
    ResponseMetadata: ResponseMetadata


class UpdateApplicationSettingsResponse(BaseValidatorModel):
    ApplicationSettingsResource: ApplicationSettingsResource
    ResponseMetadata: ResponseMetadata


class UpdateApplicationSettingsRequest(BaseValidatorModel):
    ApplicationId: str
    WriteApplicationSettingsRequest: WriteApplicationSettingsRequest


class DeleteUserEndpointsResponse(BaseValidatorModel):
    EndpointsResponse: EndpointsResponse
    ResponseMetadata: ResponseMetadata


class GetUserEndpointsResponse(BaseValidatorModel):
    EndpointsResponse: EndpointsResponse
    ResponseMetadata: ResponseMetadata


class EndpointBatchRequest(BaseValidatorModel):
    Item: Sequence[EndpointBatchItem]


class UpdateEndpointRequest(BaseValidatorModel):
    ApplicationId: str
    EndpointId: str
    EndpointRequest: EndpointRequest


class EventsBatch(BaseValidatorModel):
    Endpoint: PublicEndpoint
    Events: Mapping[str, Event]


class InAppCampaignSchedule(BaseValidatorModel):
    EndDate: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterOutput] = None
    QuietTime: Optional[QuietTime] = None


class ScheduleOutput(BaseValidatorModel):
    StartTime: str
    EndTime: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterOutput] = None
    Frequency: Optional[FrequencyType] = None
    IsLocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTime] = None
    Timezone: Optional[str] = None


class EventStartConditionOutput(BaseValidatorModel):
    EventFilter: Optional[EventFilterOutput] = None
    SegmentId: Optional[str] = None


class PutEventsResponse(BaseValidatorModel):
    EventsResponse: EventsResponse
    ResponseMetadata: ResponseMetadata


class GetExportJobsResponse(BaseValidatorModel):
    ExportJobsResponse: ExportJobsResponse
    ResponseMetadata: ResponseMetadata


class GetSegmentExportJobsResponse(BaseValidatorModel):
    ExportJobsResponse: ExportJobsResponse
    ResponseMetadata: ResponseMetadata


class SegmentDimensionsOutput(BaseValidatorModel):
    Attributes: Optional[Dict[str, AttributeDimensionOutput]] = None
    Behavior: Optional[SegmentBehaviors] = None
    Demographic: Optional[SegmentDemographicsOutput] = None
    Location: Optional[SegmentLocationOutput] = None
    Metrics: Optional[Dict[str, MetricDimension]] = None
    UserAttributes: Optional[Dict[str, AttributeDimensionOutput]] = None


class GetImportJobsResponse(BaseValidatorModel):
    ImportJobsResponse: ImportJobsResponse
    ResponseMetadata: ResponseMetadata


class GetSegmentImportJobsResponse(BaseValidatorModel):
    ImportJobsResponse: ImportJobsResponse
    ResponseMetadata: ResponseMetadata


class CampaignInAppMessageOutput(BaseValidatorModel):
    Body: Optional[str] = None
    Content: Optional[List[InAppMessageContent]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None


class CampaignInAppMessage(BaseValidatorModel):
    Body: Optional[str] = None
    Content: Optional[Sequence[InAppMessageContent]] = None
    CustomConfig: Optional[Mapping[str, str]] = None
    Layout: Optional[LayoutType] = None


class InAppMessage(BaseValidatorModel):
    Content: Optional[List[InAppMessageContent]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None


class InAppTemplateRequest(BaseValidatorModel):
    Content: Optional[Sequence[InAppMessageContent]] = None
    CustomConfig: Optional[Mapping[str, str]] = None
    Layout: Optional[LayoutType] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateDescription: Optional[str] = None


class InAppTemplateResponse(BaseValidatorModel):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateTypeType
    Arn: Optional[str] = None
    Content: Optional[List[InAppMessageContent]] = None
    CustomConfig: Optional[Dict[str, str]] = None
    Layout: Optional[LayoutType] = None
    tags: Optional[Dict[str, str]] = None
    TemplateDescription: Optional[str] = None
    Version: Optional[str] = None


class ApplicationDateRangeKpiResponse(BaseValidatorModel):
    ApplicationId: str
    EndTime: datetime
    KpiName: str
    KpiResult: BaseKpiResult
    StartTime: datetime
    NextToken: Optional[str] = None


class CampaignDateRangeKpiResponse(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    EndTime: datetime
    KpiName: str
    KpiResult: BaseKpiResult
    StartTime: datetime
    NextToken: Optional[str] = None


class JourneyDateRangeKpiResponse(BaseValidatorModel):
    ApplicationId: str
    EndTime: datetime
    JourneyId: str
    KpiName: str
    KpiResult: BaseKpiResult
    StartTime: datetime
    NextToken: Optional[str] = None


class DirectMessageConfiguration(BaseValidatorModel):
    ADMMessage: Optional[ADMMessage] = None
    APNSMessage: Optional[APNSMessage] = None
    BaiduMessage: Optional[BaiduMessage] = None
    DefaultMessage: Optional[DefaultMessage] = None
    DefaultPushNotificationMessage: Optional[DefaultPushNotificationMessage] = None
    EmailMessage: Optional[EmailMessage] = None
    GCMMessage: Optional[GCMMessage] = None
    SMSMessage: Optional[SMSMessage] = None
    VoiceMessage: Optional[VoiceMessage] = None


class UpdateEndpointsBatchRequest(BaseValidatorModel):
    ApplicationId: str
    EndpointBatchRequest: EndpointBatchRequest


class EventsRequest(BaseValidatorModel):
    BatchItem: Mapping[str, EventsBatch]


class StartConditionOutput(BaseValidatorModel):
    Description: Optional[str] = None
    EventStartCondition: Optional[EventStartConditionOutput] = None
    SegmentStartCondition: Optional[SegmentCondition] = None


class SimpleConditionOutput(BaseValidatorModel):
    EventCondition: Optional[EventConditionOutput] = None
    SegmentCondition: Optional[SegmentCondition] = None
    SegmentDimensions: Optional[SegmentDimensionsOutput] = None


class MessageConfigurationOutput(BaseValidatorModel):
    ADMMessage: Optional[Message] = None
    APNSMessage: Optional[Message] = None
    BaiduMessage: Optional[Message] = None
    CustomMessage: Optional[CampaignCustomMessage] = None
    DefaultMessage: Optional[Message] = None
    EmailMessage: Optional[CampaignEmailMessageOutput] = None
    GCMMessage: Optional[Message] = None
    SMSMessage: Optional[CampaignSmsMessage] = None
    InAppMessage: Optional[CampaignInAppMessageOutput] = None


class InAppMessageCampaign(BaseValidatorModel):
    CampaignId: Optional[str] = None
    DailyCap: Optional[int] = None
    InAppMessage: Optional[InAppMessage] = None
    Priority: Optional[int] = None
    Schedule: Optional[InAppCampaignSchedule] = None
    SessionCap: Optional[int] = None
    TotalCap: Optional[int] = None
    TreatmentId: Optional[str] = None


class CreateInAppTemplateRequest(BaseValidatorModel):
    InAppTemplateRequest: InAppTemplateRequest
    TemplateName: str


class UpdateInAppTemplateRequest(BaseValidatorModel):
    InAppTemplateRequest: InAppTemplateRequest
    TemplateName: str
    CreateNewVersion: Optional[bool] = None
    Version: Optional[str] = None


class GetInAppTemplateResponse(BaseValidatorModel):
    InAppTemplateResponse: InAppTemplateResponse
    ResponseMetadata: ResponseMetadata


class GetApplicationDateRangeKpiResponse(BaseValidatorModel):
    ApplicationDateRangeKpiResponse: ApplicationDateRangeKpiResponse
    ResponseMetadata: ResponseMetadata


class GetCampaignDateRangeKpiResponse(BaseValidatorModel):
    CampaignDateRangeKpiResponse: CampaignDateRangeKpiResponse
    ResponseMetadata: ResponseMetadata


class GetJourneyDateRangeKpiResponse(BaseValidatorModel):
    JourneyDateRangeKpiResponse: JourneyDateRangeKpiResponse
    ResponseMetadata: ResponseMetadata


class EventDimensionsUnion(BaseValidatorModel):
    pass


class CampaignEventFilter(BaseValidatorModel):
    Dimensions: EventDimensionsUnion
    FilterType: FilterTypeType


class EventCondition(BaseValidatorModel):
    Dimensions: Optional[EventDimensionsUnion] = None
    MessageActivity: Optional[str] = None


class EventFilter(BaseValidatorModel):
    Dimensions: EventDimensionsUnion
    FilterType: FilterTypeType


class SegmentLocationUnion(BaseValidatorModel):
    pass


class SegmentDemographicsUnion(BaseValidatorModel):
    pass


class SegmentDimensions(BaseValidatorModel):
    Attributes: Optional[Mapping[str, AttributeDimensionUnion]] = None
    Behavior: Optional[SegmentBehaviors] = None
    Demographic: Optional[SegmentDemographicsUnion] = None
    Location: Optional[SegmentLocationUnion] = None
    Metrics: Optional[Mapping[str, MetricDimension]] = None
    UserAttributes: Optional[Mapping[str, AttributeDimensionUnion]] = None


class MessageRequest(BaseValidatorModel):
    MessageConfiguration: DirectMessageConfiguration
    Addresses: Optional[Mapping[str, AddressConfiguration]] = None
    Context: Optional[Mapping[str, str]] = None
    Endpoints: Optional[Mapping[str, EndpointSendConfiguration]] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None
    TraceId: Optional[str] = None


class SendUsersMessageRequest(BaseValidatorModel):
    MessageConfiguration: DirectMessageConfiguration
    Users: Mapping[str, EndpointSendConfiguration]
    Context: Optional[Mapping[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None
    TraceId: Optional[str] = None


class PutEventsRequest(BaseValidatorModel):
    ApplicationId: str
    EventsRequest: EventsRequest


class SegmentGroupOutput(BaseValidatorModel):
    pass


class SegmentGroupListOutput(BaseValidatorModel):
    Groups: Optional[List[SegmentGroupOutput]] = None
    Include: Optional[IncludeType] = None


class ConditionOutput(BaseValidatorModel):
    Conditions: Optional[List[SimpleConditionOutput]] = None
    Operator: Optional[OperatorType] = None


class MultiConditionalBranchOutput(BaseValidatorModel):
    Condition: Optional[SimpleConditionOutput] = None
    NextActivity: Optional[str] = None


class TreatmentResource(BaseValidatorModel):
    Id: str
    SizePercent: int
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationOutput] = None
    MessageConfiguration: Optional[MessageConfigurationOutput] = None
    Schedule: Optional[ScheduleOutput] = None
    State: Optional[CampaignState] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None


class CampaignInAppMessageUnion(BaseValidatorModel):
    pass


class CampaignEmailMessageUnion(BaseValidatorModel):
    pass


class MessageConfiguration(BaseValidatorModel):
    ADMMessage: Optional[Message] = None
    APNSMessage: Optional[Message] = None
    BaiduMessage: Optional[Message] = None
    CustomMessage: Optional[CampaignCustomMessage] = None
    DefaultMessage: Optional[Message] = None
    EmailMessage: Optional[CampaignEmailMessageUnion] = None
    GCMMessage: Optional[Message] = None
    SMSMessage: Optional[CampaignSmsMessage] = None
    InAppMessage: Optional[CampaignInAppMessageUnion] = None


class InAppMessagesResponse(BaseValidatorModel):
    InAppMessageCampaigns: Optional[List[InAppMessageCampaign]] = None


class SendMessagesRequest(BaseValidatorModel):
    ApplicationId: str
    MessageRequest: MessageRequest


class SendUsersMessagesRequest(BaseValidatorModel):
    ApplicationId: str
    SendUsersMessageRequest: SendUsersMessageRequest


class SegmentResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreationDate: str
    Id: str
    SegmentType: SegmentTypeType
    Dimensions: Optional[SegmentDimensionsOutput] = None
    ImportDefinition: Optional[SegmentImportResource] = None
    LastModifiedDate: Optional[str] = None
    Name: Optional[str] = None
    SegmentGroups: Optional[SegmentGroupListOutput] = None
    tags: Optional[Dict[str, str]] = None
    Version: Optional[int] = None


class ConditionalSplitActivityOutput(BaseValidatorModel):
    Condition: Optional[ConditionOutput] = None
    EvaluationWaitTime: Optional[WaitTime] = None
    FalseActivity: Optional[str] = None
    TrueActivity: Optional[str] = None


class MultiConditionalSplitActivityOutput(BaseValidatorModel):
    Branches: Optional[List[MultiConditionalBranchOutput]] = None
    DefaultActivity: Optional[str] = None
    EvaluationWaitTime: Optional[WaitTime] = None


class CampaignResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreationDate: str
    Id: str
    LastModifiedDate: str
    SegmentId: str
    SegmentVersion: int
    AdditionalTreatments: Optional[List[TreatmentResource]] = None
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationOutput] = None
    DefaultState: Optional[CampaignState] = None
    Description: Optional[str] = None
    HoldoutPercent: Optional[int] = None
    Hook: Optional[CampaignHook] = None
    IsPaused: Optional[bool] = None
    Limits: Optional[CampaignLimits] = None
    MessageConfiguration: Optional[MessageConfigurationOutput] = None
    Name: Optional[str] = None
    Schedule: Optional[ScheduleOutput] = None
    State: Optional[CampaignState] = None
    tags: Optional[Dict[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None
    Version: Optional[int] = None
    Priority: Optional[int] = None


class GetInAppMessagesResponse(BaseValidatorModel):
    InAppMessagesResponse: InAppMessagesResponse
    ResponseMetadata: ResponseMetadata


class CampaignEventFilterUnion(BaseValidatorModel):
    pass


class Schedule(BaseValidatorModel):
    StartTime: str
    EndTime: Optional[str] = None
    EventFilter: Optional[CampaignEventFilterUnion] = None
    Frequency: Optional[FrequencyType] = None
    IsLocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTime] = None
    Timezone: Optional[str] = None


class EventFilterUnion(BaseValidatorModel):
    pass


class EventStartCondition(BaseValidatorModel):
    EventFilter: Optional[EventFilterUnion] = None
    SegmentId: Optional[str] = None


class SegmentDimensionsUnion(BaseValidatorModel):
    pass


class EventConditionUnion(BaseValidatorModel):
    pass


class SimpleCondition(BaseValidatorModel):
    EventCondition: Optional[EventConditionUnion] = None
    SegmentCondition: Optional[SegmentCondition] = None
    SegmentDimensions: Optional[SegmentDimensionsUnion] = None


class CreateSegmentResponse(BaseValidatorModel):
    SegmentResponse: SegmentResponse
    ResponseMetadata: ResponseMetadata


class DeleteSegmentResponse(BaseValidatorModel):
    SegmentResponse: SegmentResponse
    ResponseMetadata: ResponseMetadata


class GetSegmentResponse(BaseValidatorModel):
    SegmentResponse: SegmentResponse
    ResponseMetadata: ResponseMetadata


class GetSegmentVersionResponse(BaseValidatorModel):
    SegmentResponse: SegmentResponse
    ResponseMetadata: ResponseMetadata


class SegmentsResponse(BaseValidatorModel):
    Item: List[SegmentResponse]
    NextToken: Optional[str] = None


class UpdateSegmentResponse(BaseValidatorModel):
    SegmentResponse: SegmentResponse
    ResponseMetadata: ResponseMetadata


class ActivityOutput(BaseValidatorModel):
    CUSTOM: Optional[CustomMessageActivityOutput] = None
    ConditionalSplit: Optional[ConditionalSplitActivityOutput] = None
    Description: Optional[str] = None
    EMAIL: Optional[EmailMessageActivity] = None
    Holdout: Optional[HoldoutActivity] = None
    MultiCondition: Optional[MultiConditionalSplitActivityOutput] = None
    PUSH: Optional[PushMessageActivity] = None
    RandomSplit: Optional[RandomSplitActivityOutput] = None
    SMS: Optional[SMSMessageActivity] = None
    Wait: Optional[WaitActivity] = None
    ContactCenter: Optional[ContactCenterActivity] = None


class CampaignsResponse(BaseValidatorModel):
    Item: List[CampaignResponse]
    NextToken: Optional[str] = None


class CreateCampaignResponse(BaseValidatorModel):
    CampaignResponse: CampaignResponse
    ResponseMetadata: ResponseMetadata


class DeleteCampaignResponse(BaseValidatorModel):
    CampaignResponse: CampaignResponse
    ResponseMetadata: ResponseMetadata


class GetCampaignResponse(BaseValidatorModel):
    CampaignResponse: CampaignResponse
    ResponseMetadata: ResponseMetadata


class GetCampaignVersionResponse(BaseValidatorModel):
    CampaignResponse: CampaignResponse
    ResponseMetadata: ResponseMetadata


class UpdateCampaignResponse(BaseValidatorModel):
    CampaignResponse: CampaignResponse
    ResponseMetadata: ResponseMetadata


class GetSegmentVersionsResponse(BaseValidatorModel):
    SegmentsResponse: SegmentsResponse
    ResponseMetadata: ResponseMetadata


class GetSegmentsResponse(BaseValidatorModel):
    SegmentsResponse: SegmentsResponse
    ResponseMetadata: ResponseMetadata


class JourneyResponse(BaseValidatorModel):
    ApplicationId: str
    Id: str
    Name: str
    Activities: Optional[Dict[str, ActivityOutput]] = None
    CreationDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[JourneyLimits] = None
    LocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTime] = None
    RefreshFrequency: Optional[str] = None
    Schedule: Optional[JourneyScheduleOutput] = None
    StartActivity: Optional[str] = None
    StartCondition: Optional[StartConditionOutput] = None
    State: Optional[StateType] = None
    tags: Optional[Dict[str, str]] = None
    WaitForQuietTime: Optional[bool] = None
    RefreshOnSegmentUpdate: Optional[bool] = None
    JourneyChannelSettings: Optional[JourneyChannelSettings] = None
    SendingSchedule: Optional[bool] = None
    OpenHours: Optional[OpenHoursOutput] = None
    ClosedDays: Optional[ClosedDaysOutput] = None
    TimezoneEstimationMethods: Optional[List[TimezoneEstimationMethodsElementType]] = None


class GetCampaignVersionsResponse(BaseValidatorModel):
    CampaignsResponse: CampaignsResponse
    ResponseMetadata: ResponseMetadata


class GetCampaignsResponse(BaseValidatorModel):
    CampaignsResponse: CampaignsResponse
    ResponseMetadata: ResponseMetadata


class ScheduleUnion(BaseValidatorModel):
    pass


class MessageConfigurationUnion(BaseValidatorModel):
    pass


class CustomDeliveryConfigurationUnion(BaseValidatorModel):
    pass


class WriteTreatmentResource(BaseValidatorModel):
    SizePercent: int
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationUnion] = None
    MessageConfiguration: Optional[MessageConfigurationUnion] = None
    Schedule: Optional[ScheduleUnion] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None


class EventStartConditionUnion(BaseValidatorModel):
    pass


class StartCondition(BaseValidatorModel):
    Description: Optional[str] = None
    EventStartCondition: Optional[EventStartConditionUnion] = None
    SegmentStartCondition: Optional[SegmentCondition] = None


class SegmentGroupUnion(BaseValidatorModel):
    pass


class SegmentGroupList(BaseValidatorModel):
    Groups: Optional[Sequence[SegmentGroupUnion]] = None
    Include: Optional[IncludeType] = None


class SimpleConditionUnion(BaseValidatorModel):
    pass


class Condition(BaseValidatorModel):
    Conditions: Optional[Sequence[SimpleConditionUnion]] = None
    Operator: Optional[OperatorType] = None


class MultiConditionalBranch(BaseValidatorModel):
    Condition: Optional[SimpleConditionUnion] = None
    NextActivity: Optional[str] = None


class CreateJourneyResponse(BaseValidatorModel):
    JourneyResponse: JourneyResponse
    ResponseMetadata: ResponseMetadata


class DeleteJourneyResponse(BaseValidatorModel):
    JourneyResponse: JourneyResponse
    ResponseMetadata: ResponseMetadata


class GetJourneyResponse(BaseValidatorModel):
    JourneyResponse: JourneyResponse
    ResponseMetadata: ResponseMetadata


class JourneysResponse(BaseValidatorModel):
    Item: List[JourneyResponse]
    NextToken: Optional[str] = None


class UpdateJourneyResponse(BaseValidatorModel):
    JourneyResponse: JourneyResponse
    ResponseMetadata: ResponseMetadata


class UpdateJourneyStateResponse(BaseValidatorModel):
    JourneyResponse: JourneyResponse
    ResponseMetadata: ResponseMetadata


class WriteCampaignRequest(BaseValidatorModel):
    AdditionalTreatments: Optional[Sequence[WriteTreatmentResource]] = None
    CustomDeliveryConfiguration: Optional[CustomDeliveryConfigurationUnion] = None
    Description: Optional[str] = None
    HoldoutPercent: Optional[int] = None
    Hook: Optional[CampaignHook] = None
    IsPaused: Optional[bool] = None
    Limits: Optional[CampaignLimits] = None
    MessageConfiguration: Optional[MessageConfigurationUnion] = None
    Name: Optional[str] = None
    Schedule: Optional[ScheduleUnion] = None
    SegmentId: Optional[str] = None
    SegmentVersion: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None
    TreatmentDescription: Optional[str] = None
    TreatmentName: Optional[str] = None
    Priority: Optional[int] = None


class ListJourneysResponse(BaseValidatorModel):
    JourneysResponse: JourneysResponse
    ResponseMetadata: ResponseMetadata


class CreateCampaignRequest(BaseValidatorModel):
    ApplicationId: str
    WriteCampaignRequest: WriteCampaignRequest


class UpdateCampaignRequest(BaseValidatorModel):
    ApplicationId: str
    CampaignId: str
    WriteCampaignRequest: WriteCampaignRequest


class SegmentGroupListUnion(BaseValidatorModel):
    pass


class WriteSegmentRequest(BaseValidatorModel):
    Dimensions: Optional[SegmentDimensionsUnion] = None
    Name: Optional[str] = None
    SegmentGroups: Optional[SegmentGroupListUnion] = None
    tags: Optional[Mapping[str, str]] = None


class ConditionUnion(BaseValidatorModel):
    pass


class ConditionalSplitActivity(BaseValidatorModel):
    Condition: Optional[ConditionUnion] = None
    EvaluationWaitTime: Optional[WaitTime] = None
    FalseActivity: Optional[str] = None
    TrueActivity: Optional[str] = None


class MultiConditionalBranchUnion(BaseValidatorModel):
    pass


class MultiConditionalSplitActivity(BaseValidatorModel):
    Branches: Optional[Sequence[MultiConditionalBranchUnion]] = None
    DefaultActivity: Optional[str] = None
    EvaluationWaitTime: Optional[WaitTime] = None


class CreateSegmentRequest(BaseValidatorModel):
    ApplicationId: str
    WriteSegmentRequest: WriteSegmentRequest


class UpdateSegmentRequest(BaseValidatorModel):
    ApplicationId: str
    SegmentId: str
    WriteSegmentRequest: WriteSegmentRequest


class CustomMessageActivityUnion(BaseValidatorModel):
    pass


class MultiConditionalSplitActivityUnion(BaseValidatorModel):
    pass


class RandomSplitActivityUnion(BaseValidatorModel):
    pass


class ConditionalSplitActivityUnion(BaseValidatorModel):
    pass


class Activity(BaseValidatorModel):
    CUSTOM: Optional[CustomMessageActivityUnion] = None
    ConditionalSplit: Optional[ConditionalSplitActivityUnion] = None
    Description: Optional[str] = None
    EMAIL: Optional[EmailMessageActivity] = None
    Holdout: Optional[HoldoutActivity] = None
    MultiCondition: Optional[MultiConditionalSplitActivityUnion] = None
    PUSH: Optional[PushMessageActivity] = None
    RandomSplit: Optional[RandomSplitActivityUnion] = None
    SMS: Optional[SMSMessageActivity] = None
    Wait: Optional[WaitActivity] = None
    ContactCenter: Optional[ContactCenterActivity] = None


class ActivityUnion(BaseValidatorModel):
    pass


class StartConditionUnion(BaseValidatorModel):
    pass


class OpenHoursUnion(BaseValidatorModel):
    pass


class JourneyScheduleUnion(BaseValidatorModel):
    pass


class ClosedDaysUnion(BaseValidatorModel):
    pass


class WriteJourneyRequest(BaseValidatorModel):
    Name: str
    Activities: Optional[Mapping[str, ActivityUnion]] = None
    CreationDate: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Limits: Optional[JourneyLimits] = None
    LocalTime: Optional[bool] = None
    QuietTime: Optional[QuietTime] = None
    RefreshFrequency: Optional[str] = None
    Schedule: Optional[JourneyScheduleUnion] = None
    StartActivity: Optional[str] = None
    StartCondition: Optional[StartConditionUnion] = None
    State: Optional[StateType] = None
    WaitForQuietTime: Optional[bool] = None
    RefreshOnSegmentUpdate: Optional[bool] = None
    JourneyChannelSettings: Optional[JourneyChannelSettings] = None
    SendingSchedule: Optional[bool] = None
    OpenHours: Optional[OpenHoursUnion] = None
    ClosedDays: Optional[ClosedDaysUnion] = None
    TimezoneEstimationMethods: Optional[Sequence[TimezoneEstimationMethodsElementType]] = None


class CreateJourneyRequest(BaseValidatorModel):
    ApplicationId: str
    WriteJourneyRequest: WriteJourneyRequest


class UpdateJourneyRequest(BaseValidatorModel):
    ApplicationId: str
    JourneyId: str
    WriteJourneyRequest: WriteJourneyRequest


