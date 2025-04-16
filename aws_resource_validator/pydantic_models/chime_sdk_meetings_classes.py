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
from aws_resource_validator.pydantic_models.chime_sdk_meetings_constants import *

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


class DeleteAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str


class DeleteMeetingRequest(BaseValidatorModel):
    MeetingId: str


class EngineTranscribeSettings(BaseValidatorModel):
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


class GetAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str


class GetMeetingRequest(BaseValidatorModel):
    MeetingId: str


class ListAttendeesRequest(BaseValidatorModel):
    MeetingId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class StopMeetingTranscriptionRequest(BaseValidatorModel):
    MeetingId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class Attendee(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None
    Capabilities: Optional[AttendeeCapabilities] = None


class CreateAttendeeRequestItem(BaseValidatorModel):
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilities] = None


class CreateAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    ExternalUserId: str
    Capabilities: Optional[AttendeeCapabilities] = None


class UpdateAttendeeCapabilitiesRequest(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str
    Capabilities: AttendeeCapabilities


class BatchUpdateAttendeeCapabilitiesExceptRequest(BaseValidatorModel):
    MeetingId: str
    ExcludedAttendeeIds: Sequence[AttendeeIdItem]
    Capabilities: AttendeeCapabilities


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class EngineTranscribeMedicalSettings(BaseValidatorModel):
    pass


class TranscriptionConfiguration(BaseValidatorModel):
    EngineTranscribeSettings: Optional[EngineTranscribeSettings] = None
    EngineTranscribeMedicalSettings: Optional[EngineTranscribeMedicalSettings] = None


class MeetingFeaturesConfiguration(BaseValidatorModel):
    Audio: Optional[AudioFeatures] = None
    Video: Optional[VideoFeatures] = None
    Content: Optional[ContentFeatures] = None
    Attendee: Optional[AttendeeFeatures] = None


class BatchCreateAttendeeResponse(BaseValidatorModel):
    Attendees: List[Attendee]
    Errors: List[CreateAttendeeError]
    ResponseMetadata: ResponseMetadata


class CreateAttendeeResponse(BaseValidatorModel):
    Attendee: Attendee
    ResponseMetadata: ResponseMetadata


class GetAttendeeResponse(BaseValidatorModel):
    Attendee: Attendee
    ResponseMetadata: ResponseMetadata


class ListAttendeesResponse(BaseValidatorModel):
    Attendees: List[Attendee]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateAttendeeCapabilitiesResponse(BaseValidatorModel):
    Attendee: Attendee
    ResponseMetadata: ResponseMetadata


class BatchCreateAttendeeRequest(BaseValidatorModel):
    MeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItem]


class StartMeetingTranscriptionRequest(BaseValidatorModel):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfiguration


class CreateMeetingRequest(BaseValidatorModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    MeetingHostId: Optional[str] = None
    NotificationsConfiguration: Optional[NotificationsConfiguration] = None
    MeetingFeatures: Optional[MeetingFeaturesConfiguration] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateMeetingWithAttendeesRequest(BaseValidatorModel):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItem]
    MeetingHostId: Optional[str] = None
    MeetingFeatures: Optional[MeetingFeaturesConfiguration] = None
    NotificationsConfiguration: Optional[NotificationsConfiguration] = None
    PrimaryMeetingId: Optional[str] = None
    TenantIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


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


class CreateMeetingResponse(BaseValidatorModel):
    Meeting: Meeting
    ResponseMetadata: ResponseMetadata


class CreateMeetingWithAttendeesResponse(BaseValidatorModel):
    Meeting: Meeting
    Attendees: List[Attendee]
    Errors: List[CreateAttendeeError]
    ResponseMetadata: ResponseMetadata


class GetMeetingResponse(BaseValidatorModel):
    Meeting: Meeting
    ResponseMetadata: ResponseMetadata


