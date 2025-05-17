from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Timestamp = Union[datetime, str]


class Fragment(BaseValidatorModel):
    FragmentNumber: Optional[str] = None
    FragmentSizeInBytes: Optional[int] = None
    ProducerTimestamp: Optional[datetime] = None
    ServerTimestamp: Optional[datetime] = None
    FragmentLengthInMilliseconds: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class Image(BaseValidatorModel):
    TimeStamp: Optional[datetime] = None
    Error: Optional[ImageErrorType] = None
    ImageContent: Optional[str] = None


# This class is the input for the 'get_media_for_fragment_list' function.
class GetMediaForFragmentListInput(BaseValidatorModel):
    Fragments: List[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class ClipTimestampRange(BaseValidatorModel):
    StartTimestamp: Timestamp
    EndTimestamp: Timestamp


class DASHTimestampRange(BaseValidatorModel):
    StartTimestamp: Optional[Timestamp] = None
    EndTimestamp: Optional[Timestamp] = None


# This class is the input for the 'get_images' function.
class GetImagesInput(BaseValidatorModel):
    ImageSelectorType: ImageSelectorTypeType
    StartTimestamp: Timestamp
    EndTimestamp: Timestamp
    Format: FormatType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    SamplingInterval: Optional[int] = None
    FormatConfig: Optional[Dict[Literal['JPEGQuality'], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class HLSTimestampRange(BaseValidatorModel):
    StartTimestamp: Optional[Timestamp] = None
    EndTimestamp: Optional[Timestamp] = None


class TimestampRange(BaseValidatorModel):
    StartTimestamp: Timestamp
    EndTimestamp: Timestamp


# This class is the output for the 'get_clip' function.
class GetClipOutput(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_dash_streaming_session_url' function.
class GetDASHStreamingSessionURLOutput(BaseValidatorModel):
    DASHStreamingSessionURL: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_hls_streaming_session_url' function.
class GetHLSStreamingSessionURLOutput(BaseValidatorModel):
    HLSStreamingSessionURL: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_media_for_fragment_list' function.
class GetMediaForFragmentListOutput(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_fragments' function.
class ListFragmentsOutput(BaseValidatorModel):
    Fragments: List[Fragment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetImagesInputPaginate(BaseValidatorModel):
    ImageSelectorType: ImageSelectorTypeType
    StartTimestamp: Timestamp
    EndTimestamp: Timestamp
    Format: FormatType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    SamplingInterval: Optional[int] = None
    FormatConfig: Optional[Dict[Literal['JPEGQuality'], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_images' function.
class GetImagesOutput(BaseValidatorModel):
    Images: List[Image]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClipFragmentSelector(BaseValidatorModel):
    FragmentSelectorType: ClipFragmentSelectorTypeType
    TimestampRange: ClipTimestampRange


class DASHFragmentSelector(BaseValidatorModel):
    FragmentSelectorType: Optional[DASHFragmentSelectorTypeType] = None
    TimestampRange: Optional[DASHTimestampRange] = None


class HLSFragmentSelector(BaseValidatorModel):
    FragmentSelectorType: Optional[HLSFragmentSelectorTypeType] = None
    TimestampRange: Optional[HLSTimestampRange] = None


class FragmentSelector(BaseValidatorModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRange


# This class is the input for the 'get_clip' function.
class GetClipInput(BaseValidatorModel):
    ClipFragmentSelector: ClipFragmentSelector
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'get_dash_streaming_session_url' function.
class GetDASHStreamingSessionURLInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PlaybackMode: Optional[DASHPlaybackModeType] = None
    DisplayFragmentTimestamp: Optional[DASHDisplayFragmentTimestampType] = None
    DisplayFragmentNumber: Optional[DASHDisplayFragmentNumberType] = None
    DASHFragmentSelector: Optional[DASHFragmentSelector] = None
    Expires: Optional[int] = None
    MaxManifestFragmentResults: Optional[int] = None


# This class is the input for the 'get_hls_streaming_session_url' function.
class GetHLSStreamingSessionURLInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PlaybackMode: Optional[HLSPlaybackModeType] = None
    HLSFragmentSelector: Optional[HLSFragmentSelector] = None
    ContainerFormat: Optional[ContainerFormatType] = None
    DiscontinuityMode: Optional[HLSDiscontinuityModeType] = None
    DisplayFragmentTimestamp: Optional[HLSDisplayFragmentTimestampType] = None
    Expires: Optional[int] = None
    MaxMediaPlaylistFragmentResults: Optional[int] = None


class ListFragmentsInputPaginate(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    FragmentSelector: Optional[FragmentSelector] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_fragments' function.
class ListFragmentsInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FragmentSelector: Optional[FragmentSelector] = None