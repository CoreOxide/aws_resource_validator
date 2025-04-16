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
from aws_resource_validator.pydantic_models.elastictranscoder_constants import *

class Encryption(BaseValidatorModel):
    Mode: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    InitializationVector: Optional[str] = None


class AudioCodecOptions(BaseValidatorModel):
    Profile: Optional[str] = None
    BitDepth: Optional[str] = None
    BitOrder: Optional[str] = None
    Signed: Optional[str] = None


class CancelJobRequest(BaseValidatorModel):
    Id: str


class TimeSpan(BaseValidatorModel):
    StartTime: Optional[str] = None
    Duration: Optional[str] = None


class HlsContentProtection(BaseValidatorModel):
    Method: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    InitializationVector: Optional[str] = None
    LicenseAcquisitionUrl: Optional[str] = None
    KeyStoragePolicy: Optional[str] = None


class PlayReadyDrm(BaseValidatorModel):
    Format: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    KeyId: Optional[str] = None
    InitializationVector: Optional[str] = None
    LicenseAcquisitionUrl: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Warning(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class Thumbnails(BaseValidatorModel):
    Format: Optional[str] = None
    Interval: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None


class DeletePipelineRequest(BaseValidatorModel):
    Id: str


class DeletePresetRequest(BaseValidatorModel):
    Id: str


class DetectedProperties(BaseValidatorModel):
    Width: Optional[int] = None
    Height: Optional[int] = None
    FrameRate: Optional[str] = None
    FileSize: Optional[int] = None
    DurationMillis: Optional[int] = None


class Timing(BaseValidatorModel):
    SubmitTimeMillis: Optional[int] = None
    StartTimeMillis: Optional[int] = None
    FinishTimeMillis: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListJobsByPipelineRequest(BaseValidatorModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class ListJobsByStatusRequest(BaseValidatorModel):
    Status: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class ListPipelinesRequest(BaseValidatorModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class ListPresetsRequest(BaseValidatorModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class PermissionOutput(BaseValidatorModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[List[str]] = None


class Permission(BaseValidatorModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[Sequence[str]] = None


class PresetWatermark(BaseValidatorModel):
    Id: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    HorizontalAlign: Optional[str] = None
    HorizontalOffset: Optional[str] = None
    VerticalAlign: Optional[str] = None
    VerticalOffset: Optional[str] = None
    Opacity: Optional[str] = None
    Target: Optional[str] = None


class ReadJobRequest(BaseValidatorModel):
    Id: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ReadPipelineRequest(BaseValidatorModel):
    Id: str


class ReadPresetRequest(BaseValidatorModel):
    Id: str


class TestRoleRequest(BaseValidatorModel):
    Role: str
    InputBucket: str
    OutputBucket: str
    Topics: Sequence[str]


class UpdatePipelineStatusRequest(BaseValidatorModel):
    Id: str
    Status: str


class Artwork(BaseValidatorModel):
    InputKey: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None
    AlbumArtFormat: Optional[str] = None
    Encryption: Optional[Encryption] = None


class CaptionSource(BaseValidatorModel):
    Key: Optional[str] = None
    Language: Optional[str] = None
    TimeOffset: Optional[str] = None
    Label: Optional[str] = None
    Encryption: Optional[Encryption] = None


class JobWatermark(BaseValidatorModel):
    PresetWatermarkId: Optional[str] = None
    InputKey: Optional[str] = None
    Encryption: Optional[Encryption] = None


class AudioParameters(BaseValidatorModel):
    Codec: Optional[str] = None
    SampleRate: Optional[str] = None
    BitRate: Optional[str] = None
    Channels: Optional[str] = None
    AudioPackingMode: Optional[str] = None
    CodecOptions: Optional[AudioCodecOptions] = None


class Clip(BaseValidatorModel):
    TimeSpan: Optional[TimeSpan] = None


class CreateJobPlaylist(BaseValidatorModel):
    Name: Optional[str] = None
    Format: Optional[str] = None
    OutputKeys: Optional[Sequence[str]] = None
    HlsContentProtection: Optional[HlsContentProtection] = None
    PlayReadyDrm: Optional[PlayReadyDrm] = None


class Playlist(BaseValidatorModel):
    Name: Optional[str] = None
    Format: Optional[str] = None
    OutputKeys: Optional[List[str]] = None
    HlsContentProtection: Optional[HlsContentProtection] = None
    PlayReadyDrm: Optional[PlayReadyDrm] = None
    Status: Optional[str] = None
    StatusDetail: Optional[str] = None


class TestRoleResponse(BaseValidatorModel):
    Success: str
    Messages: List[str]
    ResponseMetadata: ResponseMetadata


class Notifications(BaseValidatorModel):
    pass


class UpdatePipelineNotificationsRequest(BaseValidatorModel):
    Id: str
    Notifications: Notifications


class ListJobsByPipelineRequestPaginate(BaseValidatorModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsByStatusRequestPaginate(BaseValidatorModel):
    Status: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelinesRequestPaginate(BaseValidatorModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPresetsRequestPaginate(BaseValidatorModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class PipelineOutputConfigOutput(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[List[PermissionOutput]] = None


class PipelineOutputConfig(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[Sequence[Permission]] = None


class VideoParametersOutput(BaseValidatorModel):
    Codec: Optional[str] = None
    CodecOptions: Optional[Dict[str, str]] = None
    KeyframesMaxDist: Optional[str] = None
    FixedGOP: Optional[str] = None
    BitRate: Optional[str] = None
    FrameRate: Optional[str] = None
    MaxFrameRate: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    DisplayAspectRatio: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None
    Watermarks: Optional[List[PresetWatermark]] = None


class VideoParameters(BaseValidatorModel):
    Codec: Optional[str] = None
    CodecOptions: Optional[Mapping[str, str]] = None
    KeyframesMaxDist: Optional[str] = None
    FixedGOP: Optional[str] = None
    BitRate: Optional[str] = None
    FrameRate: Optional[str] = None
    MaxFrameRate: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    DisplayAspectRatio: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None
    Watermarks: Optional[Sequence[PresetWatermark]] = None


class ReadJobRequestWait(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfig] = None


class JobAlbumArtOutput(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[List[Artwork]] = None


class JobAlbumArt(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[Sequence[Artwork]] = None


class CaptionFormat(BaseValidatorModel):
    pass


class CaptionsOutput(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSource]] = None
    CaptionFormats: Optional[List[CaptionFormat]] = None


class Captions(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSource]] = None
    CaptionFormats: Optional[Sequence[CaptionFormat]] = None


class InputCaptionsOutput(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSource]] = None


class InputCaptions(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSource]] = None


class Pipeline(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[str] = None
    InputBucket: Optional[str] = None
    OutputBucket: Optional[str] = None
    Role: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[Notifications] = None
    ContentConfig: Optional[PipelineOutputConfigOutput] = None
    ThumbnailConfig: Optional[PipelineOutputConfigOutput] = None


class JobOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Key: Optional[str] = None
    ThumbnailPattern: Optional[str] = None
    ThumbnailEncryption: Optional[Encryption] = None
    Rotate: Optional[str] = None
    PresetId: Optional[str] = None
    SegmentDuration: Optional[str] = None
    Status: Optional[str] = None
    StatusDetail: Optional[str] = None
    Duration: Optional[int] = None
    Width: Optional[int] = None
    Height: Optional[int] = None
    FrameRate: Optional[str] = None
    FileSize: Optional[int] = None
    DurationMillis: Optional[int] = None
    Watermarks: Optional[List[JobWatermark]] = None
    AlbumArt: Optional[JobAlbumArtOutput] = None
    Composition: Optional[List[Clip]] = None
    Captions: Optional[CaptionsOutput] = None
    Encryption: Optional[Encryption] = None
    AppliedColorSpaceConversion: Optional[str] = None


class CreatePipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    Warnings: List[Warning]
    ResponseMetadata: ResponseMetadata


class ListPipelinesResponse(BaseValidatorModel):
    Pipelines: List[Pipeline]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ReadPipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    Warnings: List[Warning]
    ResponseMetadata: ResponseMetadata


class UpdatePipelineNotificationsResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class UpdatePipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    Warnings: List[Warning]
    ResponseMetadata: ResponseMetadata


class UpdatePipelineStatusResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class PipelineOutputConfigUnion(BaseValidatorModel):
    pass


class CreatePipelineRequest(BaseValidatorModel):
    Name: str
    InputBucket: str
    Role: str
    OutputBucket: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[Notifications] = None
    ContentConfig: Optional[PipelineOutputConfigUnion] = None
    ThumbnailConfig: Optional[PipelineOutputConfigUnion] = None


class UpdatePipelineRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    InputBucket: Optional[str] = None
    Role: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[Notifications] = None
    ContentConfig: Optional[PipelineOutputConfigUnion] = None
    ThumbnailConfig: Optional[PipelineOutputConfigUnion] = None


class Preset(BaseValidatorModel):
    pass


class ListPresetsResponse(BaseValidatorModel):
    Presets: List[Preset]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ReadPresetResponse(BaseValidatorModel):
    Preset: Preset
    ResponseMetadata: ResponseMetadata


class CaptionsUnion(BaseValidatorModel):
    pass


class JobAlbumArtUnion(BaseValidatorModel):
    pass


class CreateJobOutput(BaseValidatorModel):
    Key: Optional[str] = None
    ThumbnailPattern: Optional[str] = None
    ThumbnailEncryption: Optional[Encryption] = None
    Rotate: Optional[str] = None
    PresetId: Optional[str] = None
    SegmentDuration: Optional[str] = None
    Watermarks: Optional[Sequence[JobWatermark]] = None
    AlbumArt: Optional[JobAlbumArtUnion] = None
    Composition: Optional[Sequence[Clip]] = None
    Captions: Optional[CaptionsUnion] = None
    Encryption: Optional[Encryption] = None


class JobInputOutput(BaseValidatorModel):
    pass


class Job(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    PipelineId: Optional[str] = None
    Input: Optional[JobInputOutput] = None
    Inputs: Optional[List[JobInputOutput]] = None
    Output: Optional[JobOutput] = None
    Outputs: Optional[List[JobOutput]] = None
    OutputKeyPrefix: Optional[str] = None
    Playlists: Optional[List[Playlist]] = None
    Status: Optional[str] = None
    UserMetadata: Optional[Dict[str, str]] = None
    Timing: Optional[Timing] = None


class CreateJobResponse(BaseValidatorModel):
    Job: Job
    ResponseMetadata: ResponseMetadata


class ListJobsByPipelineResponse(BaseValidatorModel):
    Jobs: List[Job]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListJobsByStatusResponse(BaseValidatorModel):
    Jobs: List[Job]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ReadJobResponse(BaseValidatorModel):
    Job: Job
    ResponseMetadata: ResponseMetadata


class JobInputUnion(BaseValidatorModel):
    pass


class CreateJobRequest(BaseValidatorModel):
    PipelineId: str
    Input: Optional[JobInputUnion] = None
    Inputs: Optional[Sequence[JobInputUnion]] = None
    Output: Optional[CreateJobOutput] = None
    Outputs: Optional[Sequence[CreateJobOutput]] = None
    OutputKeyPrefix: Optional[str] = None
    Playlists: Optional[Sequence[CreateJobPlaylist]] = None
    UserMetadata: Optional[Mapping[str, str]] = None


