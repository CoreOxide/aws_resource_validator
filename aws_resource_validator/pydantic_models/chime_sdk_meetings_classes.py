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
from aws_resource_validator.pydantic_models.chime_sdk_meetings_constants import *

class AttendeeCapabilitiesTypeDef(BaseModel):
    Audio: MediaCapabilitiesType
    Video: MediaCapabilitiesType
    Content: MediaCapabilitiesType

class AttendeeFeaturesTypeDef(BaseModel):
    MaxCount: Optional[int] = None

class AttendeeIdItemTypeDef(BaseModel):
    AttendeeId: str

class AudioFeaturesTypeDef(BaseModel):
    EchoReduction: Optional[MeetingFeatureStatusType] = None

class CreateAttendeeErrorTypeDef(BaseModel):
    ExternalUserId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ContentFeaturesTypeDef(BaseModel):
    MaxResolution: Optional[ContentResolutionType] = None

class NotificationsConfigurationTypeDef(BaseModel):
    LambdaFunctionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SqsQueueArn: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str

class DeleteMeetingRequestRequestTypeDef(BaseModel):
    MeetingId: str

class EngineTranscribeMedicalSettingsTypeDef(BaseModel):
    LanguageCode: Literal["en-US"]
    Specialty: TranscribeMedicalSpecialtyType
    Type: TranscribeMedicalTypeType
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeMedicalRegionType] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None

class EngineTranscribeSettingsTypeDef(BaseModel):
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

class GetAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str

class GetMeetingRequestRequestTypeDef(BaseModel):
    MeetingId: str

class ListAttendeesRequestRequestTypeDef(BaseModel):
    MeetingId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class MediaPlacementTypeDef(BaseModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    ScreenDataUrl: Optional[str] = None
    ScreenViewingUrl: Optional[str] = None
    ScreenSharingUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None

class VideoFeaturesTypeDef(BaseModel):
    MaxResolution: Optional[VideoResolutionType] = None

class StopMeetingTranscriptionRequestRequestTypeDef(BaseModel):
    MeetingId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AttendeeTypeDef(BaseModel):
    ExternalUserId: Optional[str] = None
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None
    Capabilities: Optional[AttendeeCapabilitiesTypeDef] = None

class CreateAttendeeRequestItemTypeDef(BaseModel):
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilitiesTypeDef] = None

class CreateAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilitiesTypeDef] = None

class UpdateAttendeeCapabilitiesRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str
    Capabilities: AttendeeCapabilitiesTypeDef

class BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef(BaseModel):
    MeetingId: str
    ExcludedAttendeeIds: Sequence[AttendeeIdItemTypeDef]
    Capabilities: AttendeeCapabilitiesTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class TranscriptionConfigurationTypeDef(BaseModel):
    EngineTranscribeSettings: Optional[EngineTranscribeSettingsTypeDef] = None
    EngineTranscribeMedicalSettings: Optional[EngineTranscribeMedicalSettingsTypeDef] = None

class MeetingFeaturesConfigurationTypeDef(BaseModel):
    Audio: Optional[AudioFeaturesTypeDef] = None
    Video: Optional[VideoFeaturesTypeDef] = None
    Content: Optional[ContentFeaturesTypeDef] = None
    Attendee: Optional[AttendeeFeaturesTypeDef] = None

class BatchCreateAttendeeResponseTypeDef(BaseModel):
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttendeeResponseTypeDef(BaseModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttendeeResponseTypeDef(BaseModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttendeesResponseTypeDef(BaseModel):
    Attendees: List[AttendeeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAttendeeCapabilitiesResponseTypeDef(BaseModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]

class StartMeetingTranscriptionRequestRequestTypeDef(BaseModel):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfigurationTypeDef

class CreateMeetingRequestRequestTypeDef(BaseModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    MeetingHostId: Optional[str] = None
    NotificationsConfiguration: Optional[NotificationsConfigurationTypeDef] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMeetingWithAttendeesRequestRequestTypeDef(BaseModel):
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

class MeetingTypeDef(BaseModel):
    MeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    ExternalMeetingId: Optional[str] = None
    MediaRegion: Optional[str] = None
    MediaPlacement: Optional[MediaPlacementTypeDef] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[List[str]] = None
    MeetingArn: Optional[str] = None

class CreateMeetingResponseTypeDef(BaseModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingWithAttendeesResponseTypeDef(BaseModel):
    Meeting: MeetingTypeDef
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMeetingResponseTypeDef(BaseModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

