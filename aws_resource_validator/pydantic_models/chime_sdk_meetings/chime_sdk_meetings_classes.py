from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AttendeeCapabilities(BaseValidatorModel):
    Audio: MediaCapabilitiesType
    Video: MediaCapabilitiesType
    Content: MediaCapabilitiesType


class AttendeeFeatures(BaseValidatorModel):
    MaxCount: Optional[int] = None


class AttendeeIdItem(BaseValidatorModel):
    AttendeeId: str


class AudioFeatures(BaseValidatorModel):
    EchoReduction: Optional[MeetingFeatureStatusType] = None


class CreateAttendeeError(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ContentFeatures(BaseValidatorModel):
    MaxResolution: Optional[ContentResolutionType] = None


class NotificationsConfiguration(BaseValidatorModel):
    LambdaFunctionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SqsQueueArn: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'delete_attendee' function.
class DeleteAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str


# This class is the input for the 'delete_meeting' function.
class DeleteMeetingRequest(BaseValidatorModel):
    MeetingId: str


class EngineTranscribeMedicalSettings(BaseValidatorModel):
    LanguageCode: Literal['en-US']
    Specialty: TranscribeMedicalSpecialtyType
    Type: TranscribeMedicalTypeType
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeMedicalRegionType] = None
    ContentIdentificationType: Optional[Literal['PHI']] = None


class EngineTranscribeSettings(BaseValidatorModel):
    LanguageCode: Optional[TranscribeLanguageCodeType] = None
    VocabularyFilterMethod: Optional[TranscribeVocabularyFilterMethodType] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeRegionType] = None
    EnablePartialResultsStabilization: Optional[bool] = None
    PartialResultsStability: Optional[TranscribePartialResultsStabilityType] = None
    ContentIdentificationType: Optional[Literal['PII']] = None
    ContentRedactionType: Optional[Literal['PII']] = None
    PiiEntityTypes: Optional[str] = None
    LanguageModelName: Optional[str] = None
    IdentifyLanguage: Optional[bool] = None
    LanguageOptions: Optional[str] = None
    PreferredLanguage: Optional[TranscribeLanguageCodeType] = None
    VocabularyNames: Optional[str] = None
    VocabularyFilterNames: Optional[str] = None


# This class is the input for the 'get_attendee' function.
class GetAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str


# This class is the input for the 'get_meeting' function.
class GetMeetingRequest(BaseValidatorModel):
    MeetingId: str


# This class is the input for the 'list_attendees' function.
class ListAttendeesRequest(BaseValidatorModel):
    MeetingId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class MediaPlacement(BaseValidatorModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    ScreenDataUrl: Optional[str] = None
    ScreenViewingUrl: Optional[str] = None
    ScreenSharingUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None


class VideoFeatures(BaseValidatorModel):
    MaxResolution: Optional[VideoResolutionType] = None


# This class is the input for the 'stop_meeting_transcription' function.
class StopMeetingTranscriptionRequest(BaseValidatorModel):
    MeetingId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class Attendee(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None
    Capabilities: Optional[AttendeeCapabilities] = None


class CreateAttendeeRequestItem(BaseValidatorModel):
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilities] = None


# This class is the input for the 'create_attendee' function.
class CreateAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilities] = None


# This class is the input for the 'update_attendee_capabilities' function.
class UpdateAttendeeCapabilitiesRequest(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str
    Capabilities: AttendeeCapabilities


# This class is the input for the 'batch_update_attendee_capabilities_except' function.
class BatchUpdateAttendeeCapabilitiesExceptRequest(BaseValidatorModel):
    MeetingId: str
    ExcludedAttendeeIds: List[AttendeeIdItem]
    Capabilities: AttendeeCapabilities


# This class is the output for the 'stop_meeting_transcription' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class TranscriptionConfiguration(BaseValidatorModel):
    EngineTranscribeSettings: Optional[EngineTranscribeSettings] = None
    EngineTranscribeMedicalSettings: Optional[EngineTranscribeMedicalSettings] = None


class MeetingFeaturesConfiguration(BaseValidatorModel):
    Audio: Optional[AudioFeatures] = None
    Video: Optional[VideoFeatures] = None
    Content: Optional[ContentFeatures] = None
    Attendee: Optional[AttendeeFeatures] = None


# This class is the output for the 'batch_create_attendee' function.
class BatchCreateAttendeeResponse(BaseValidatorModel):
    Attendees: List[Attendee]
    Errors: List[CreateAttendeeError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_attendee' function.
class CreateAttendeeResponse(BaseValidatorModel):
    Attendee: Attendee
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_attendee' function.
class GetAttendeeResponse(BaseValidatorModel):
    Attendee: Attendee
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attendees' function.
class ListAttendeesResponse(BaseValidatorModel):
    Attendees: List[Attendee]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_attendee_capabilities' function.
class UpdateAttendeeCapabilitiesResponse(BaseValidatorModel):
    Attendee: Attendee
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_create_attendee' function.
class BatchCreateAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    Attendees: List[CreateAttendeeRequestItem]


# This class is the input for the 'start_meeting_transcription' function.
class StartMeetingTranscriptionRequest(BaseValidatorModel):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfiguration


# This class is the input for the 'create_meeting' function.
class CreateMeetingRequest(BaseValidatorModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    MeetingHostId: Optional[str] = None
    NotificationsConfiguration: Optional[NotificationsConfiguration] = None
    MeetingFeatures: Optional[MeetingFeaturesConfiguration] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_meeting_with_attendees' function.
class CreateMeetingWithAttendeesRequest(BaseValidatorModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    Attendees: List[CreateAttendeeRequestItem]
    MeetingHostId: Optional[str] = None
    MeetingFeatures: Optional[MeetingFeaturesConfiguration] = None
    NotificationsConfiguration: Optional[NotificationsConfiguration] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class Meeting(BaseValidatorModel):
    MeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    ExternalMeetingId: Optional[str] = None
    MediaRegion: Optional[str] = None
    MediaPlacement: Optional[MediaPlacement] = None
    MeetingFeatures: Optional[MeetingFeaturesConfiguration] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[List[str]] = None
    MeetingArn: Optional[str] = None


# This class is the output for the 'create_meeting' function.
class CreateMeetingResponse(BaseValidatorModel):
    Meeting: Meeting
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_meeting_with_attendees' function.
class CreateMeetingWithAttendeesResponse(BaseValidatorModel):
    Meeting: Meeting
    Attendees: List[Attendee]
    Errors: List[CreateAttendeeError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_meeting' function.
class GetMeetingResponse(BaseValidatorModel):
    Meeting: Meeting
    ResponseMetadata: ResponseMetadata