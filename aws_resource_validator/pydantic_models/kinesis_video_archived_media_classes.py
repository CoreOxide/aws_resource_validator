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
from aws_resource_validator.pydantic_models.kinesis_video_archived_media_constants import *

class FragmentTypeDef(BaseValidatorModel):
    FragmentNumber: Optional[str] = None
    FragmentSizeInBytes: Optional[int] = None
    ProducerTimestamp: Optional[datetime] = None
    ServerTimestamp: Optional[datetime] = None
    FragmentLengthInMilliseconds: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ImageTypeDef(BaseValidatorModel):
    TimeStamp: Optional[datetime] = None
    Error: Optional[ImageErrorType] = None
    ImageContent: Optional[str] = None

class GetMediaForFragmentListInputRequestTypeDef(BaseValidatorModel):
    Fragments: Sequence[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class ClipTimestampRangeTypeDef(BaseValidatorModel):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class DASHTimestampRangeTypeDef(BaseValidatorModel):
    StartTimestamp: Optional[TimestampTypeDef] = None
    EndTimestamp: Optional[TimestampTypeDef] = None

class GetImagesInputRequestTypeDef(BaseValidatorModel):
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

class HLSTimestampRangeTypeDef(BaseValidatorModel):
    StartTimestamp: Optional[TimestampTypeDef] = None
    EndTimestamp: Optional[TimestampTypeDef] = None

class TimestampRangeTypeDef(BaseValidatorModel):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class GetClipOutputTypeDef(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetDASHStreamingSessionURLOutputTypeDef(BaseValidatorModel):
    DASHStreamingSessionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHLSStreamingSessionURLOutputTypeDef(BaseValidatorModel):
    HLSStreamingSessionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaForFragmentListOutputTypeDef(BaseValidatorModel):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListFragmentsOutputTypeDef(BaseValidatorModel):
    Fragments: List[FragmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImagesInputGetImagesPaginateTypeDef(BaseValidatorModel):
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

class GetImagesOutputTypeDef(BaseValidatorModel):
    Images: List[ImageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClipFragmentSelectorTypeDef(BaseValidatorModel):
    FragmentSelectorType: ClipFragmentSelectorTypeType
    TimestampRange: ClipTimestampRangeTypeDef

class DASHFragmentSelectorTypeDef(BaseValidatorModel):
    FragmentSelectorType: Optional[DASHFragmentSelectorTypeType] = None
    TimestampRange: Optional[DASHTimestampRangeTypeDef] = None

class HLSFragmentSelectorTypeDef(BaseValidatorModel):
    FragmentSelectorType: Optional[HLSFragmentSelectorTypeType] = None
    TimestampRange: Optional[HLSTimestampRangeTypeDef] = None

class FragmentSelectorTypeDef(BaseValidatorModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeTypeDef

class GetClipInputRequestTypeDef(BaseValidatorModel):
    ClipFragmentSelector: ClipFragmentSelectorTypeDef
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class GetDASHStreamingSessionURLInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PlaybackMode: Optional[DASHPlaybackModeType] = None
    DisplayFragmentTimestamp: Optional[DASHDisplayFragmentTimestampType] = None
    DisplayFragmentNumber: Optional[DASHDisplayFragmentNumberType] = None
    DASHFragmentSelector: Optional[DASHFragmentSelectorTypeDef] = None
    Expires: Optional[int] = None
    MaxManifestFragmentResults: Optional[int] = None

class GetHLSStreamingSessionURLInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PlaybackMode: Optional[HLSPlaybackModeType] = None
    HLSFragmentSelector: Optional[HLSFragmentSelectorTypeDef] = None
    ContainerFormat: Optional[ContainerFormatType] = None
    DiscontinuityMode: Optional[HLSDiscontinuityModeType] = None
    DisplayFragmentTimestamp: Optional[HLSDisplayFragmentTimestampType] = None
    Expires: Optional[int] = None
    MaxMediaPlaylistFragmentResults: Optional[int] = None

class ListFragmentsInputListFragmentsPaginateTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    FragmentSelector: Optional[FragmentSelectorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFragmentsInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FragmentSelector: Optional[FragmentSelectorTypeDef] = None

