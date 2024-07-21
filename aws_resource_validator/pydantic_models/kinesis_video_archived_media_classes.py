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
from aws_resource_validator.pydantic_models.kinesis_video_archived_media_constants import *

class FragmentTypeDef(BaseModel):
    FragmentNumber: Optional[str] = None
    FragmentSizeInBytes: Optional[int] = None
    ProducerTimestamp: Optional[datetime] = None
    ServerTimestamp: Optional[datetime] = None
    FragmentLengthInMilliseconds: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ImageTypeDef(BaseModel):
    TimeStamp: Optional[datetime] = None
    Error: Optional[ImageErrorType] = None
    ImageContent: Optional[str] = None

class GetMediaForFragmentListInputRequestTypeDef(BaseModel):
    Fragments: Sequence[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class ClipTimestampRangeTypeDef(BaseModel):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class DASHTimestampRangeTypeDef(BaseModel):
    StartTimestamp: Optional[TimestampTypeDef] = None
    EndTimestamp: Optional[TimestampTypeDef] = None

class GetImagesInputRequestTypeDef(BaseModel):
    ImageSelectorType: ImageSelectorTypeType
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef
    Format: FormatType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    SamplingInterval: Optional[int] = None
    FormatConfig: Optional[Mapping[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class HLSTimestampRangeTypeDef(BaseModel):
    StartTimestamp: Optional[TimestampTypeDef] = None
    EndTimestamp: Optional[TimestampTypeDef] = None

class TimestampRangeTypeDef(BaseModel):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class GetClipOutputTypeDef(BaseModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetDASHStreamingSessionURLOutputTypeDef(BaseModel):
    DASHStreamingSessionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHLSStreamingSessionURLOutputTypeDef(BaseModel):
    HLSStreamingSessionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaForFragmentListOutputTypeDef(BaseModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListFragmentsOutputTypeDef(BaseModel):
    Fragments: List[FragmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImagesInputGetImagesPaginateTypeDef(BaseModel):
    ImageSelectorType: ImageSelectorTypeType
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef
    Format: FormatType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    SamplingInterval: Optional[int] = None
    FormatConfig: Optional[Mapping[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetImagesOutputTypeDef(BaseModel):
    Images: List[ImageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClipFragmentSelectorTypeDef(BaseModel):
    FragmentSelectorType: ClipFragmentSelectorTypeType
    TimestampRange: ClipTimestampRangeTypeDef

class DASHFragmentSelectorTypeDef(BaseModel):
    FragmentSelectorType: Optional[DASHFragmentSelectorTypeType] = None
    TimestampRange: Optional[DASHTimestampRangeTypeDef] = None

class HLSFragmentSelectorTypeDef(BaseModel):
    FragmentSelectorType: Optional[HLSFragmentSelectorTypeType] = None
    TimestampRange: Optional[HLSTimestampRangeTypeDef] = None

class FragmentSelectorTypeDef(BaseModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeTypeDef

class GetClipInputRequestTypeDef(BaseModel):
    ClipFragmentSelector: ClipFragmentSelectorTypeDef
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class GetDASHStreamingSessionURLInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PlaybackMode: Optional[DASHPlaybackModeType] = None
    DisplayFragmentTimestamp: Optional[DASHDisplayFragmentTimestampType] = None
    DisplayFragmentNumber: Optional[DASHDisplayFragmentNumberType] = None
    DASHFragmentSelector: Optional[DASHFragmentSelectorTypeDef] = None
    Expires: Optional[int] = None
    MaxManifestFragmentResults: Optional[int] = None

class GetHLSStreamingSessionURLInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PlaybackMode: Optional[HLSPlaybackModeType] = None
    HLSFragmentSelector: Optional[HLSFragmentSelectorTypeDef] = None
    ContainerFormat: Optional[ContainerFormatType] = None
    DiscontinuityMode: Optional[HLSDiscontinuityModeType] = None
    DisplayFragmentTimestamp: Optional[HLSDisplayFragmentTimestampType] = None
    Expires: Optional[int] = None
    MaxMediaPlaylistFragmentResults: Optional[int] = None

class ListFragmentsInputListFragmentsPaginateTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    FragmentSelector: Optional[FragmentSelectorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFragmentsInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FragmentSelector: Optional[FragmentSelectorTypeDef] = None

