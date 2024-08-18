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
from aws_resource_validator.pydantic_models.chime_sdk_meetings_constants import *

class AttendeeCapabilitiesTypeDef(BaseValidatorModel):
    Audio: MediaCapabilitiesType
    Video: MediaCapabilitiesType
    Content: MediaCapabilitiesType

class AttendeeFeaturesTypeDef(BaseValidatorModel):
    MaxCount: Optional[int] = None

class AttendeeIdItemTypeDef(BaseValidatorModel):
    AttendeeId: str

class AudioFeaturesTypeDef(BaseValidatorModel):
    EchoReduction: Optional[MeetingFeatureStatusType] = None

class CreateAttendeeErrorTypeDef(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ContentFeaturesTypeDef(BaseValidatorModel):
    MaxResolution: Optional[ContentResolutionType] = None

class NotificationsConfigurationTypeDef(BaseValidatorModel):
    LambdaFunctionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SqsQueueArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class DeleteAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str

class DeleteMeetingRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class EngineTranscribeMedicalSettingsTypeDef(BaseValidatorModel):
    LanguageCode: Literal["en-US"]
    Specialty: TranscribeMedicalSpecialtyType
    Type: TranscribeMedicalTypeType
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeMedicalRegionType] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None

class EngineTranscribeSettingsTypeDef(BaseValidatorModel):
    LanguageCode: Optional[TranscribeLanguageCodeType] = None
    VocabularyFilterMethod: Optional[TranscribeVocabularyFilterMethodType] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeRegionType] = None
    EnablePartialResultsStabilization: Optional[bool] = None
    PartialResultsStability: Optional[TranscribePartialResultsStabilityType] = None
    ContentIdentificationType: Optional[Literal["PII"]] = None
    ContentRedactionType: Optional[Literal["PII"]] = None
    PiiEntityTypes: Optional[str] = None
    LanguageModelName: Optional[str] = None
    IdentifyLanguage: Optional[bool] = None
    LanguageOptions: Optional[str] = None
    PreferredLanguage: Optional[TranscribeLanguageCodeType] = None
    VocabularyNames: Optional[str] = None
    VocabularyFilterNames: Optional[str] = None

class GetAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str

class GetMeetingRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class ListAttendeesRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class MediaPlacementTypeDef(BaseValidatorModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    ScreenDataUrl: Optional[str] = None
    ScreenViewingUrl: Optional[str] = None
    ScreenSharingUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None

class VideoFeaturesTypeDef(BaseValidatorModel):
    MaxResolution: Optional[VideoResolutionType] = None

class StopMeetingTranscriptionRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AttendeeTypeDef(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None
    Capabilities: Optional[AttendeeCapabilitiesTypeDef] = None

class CreateAttendeeRequestItemTypeDef(BaseValidatorModel):
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilitiesTypeDef] = None

class CreateAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilitiesTypeDef] = None

class UpdateAttendeeCapabilitiesRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str
    Capabilities: AttendeeCapabilitiesTypeDef

class BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    ExcludedAttendeeIds: Sequence[AttendeeIdItemTypeDef]
    Capabilities: AttendeeCapabilitiesTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class TranscriptionConfigurationTypeDef(BaseValidatorModel):
    EngineTranscribeSettings: Optional[EngineTranscribeSettingsTypeDef] = None
    EngineTranscribeMedicalSettings: Optional[EngineTranscribeMedicalSettingsTypeDef] = None

class MeetingFeaturesConfigurationTypeDef(BaseValidatorModel):
    Audio: Optional[AudioFeaturesTypeDef] = None
    Video: Optional[VideoFeaturesTypeDef] = None
    Content: Optional[ContentFeaturesTypeDef] = None
    Attendee: Optional[AttendeeFeaturesTypeDef] = None

class BatchCreateAttendeeResponseTypeDef(BaseValidatorModel):
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttendeeResponseTypeDef(BaseValidatorModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttendeeResponseTypeDef(BaseValidatorModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttendeesResponseTypeDef(BaseValidatorModel):
    Attendees: List[AttendeeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAttendeeCapabilitiesResponseTypeDef(BaseValidatorModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]

class StartMeetingTranscriptionRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfigurationTypeDef

class CreateMeetingRequestRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    MeetingHostId: Optional[str] = None
    NotificationsConfiguration: Optional[NotificationsConfigurationTypeDef] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMeetingWithAttendeesRequestRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]
    MeetingHostId: Optional[str] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    NotificationsConfiguration: Optional[NotificationsConfigurationTypeDef] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MeetingTypeDef(BaseValidatorModel):
    MeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    ExternalMeetingId: Optional[str] = None
    MediaRegion: Optional[str] = None
    MediaPlacement: Optional[MediaPlacementTypeDef] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[List[str]] = None
    MeetingArn: Optional[str] = None

class CreateMeetingResponseTypeDef(BaseValidatorModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingWithAttendeesResponseTypeDef(BaseValidatorModel):
    Meeting: MeetingTypeDef
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMeetingResponseTypeDef(BaseValidatorModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

