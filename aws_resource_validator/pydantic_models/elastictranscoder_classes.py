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
from aws_resource_validator.pydantic_models.elastictranscoder_constants import *

class EncryptionTypeDef(BaseModel):
    Mode: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    InitializationVector: Optional[str] = None

class AudioCodecOptionsTypeDef(BaseModel):
    Profile: Optional[str] = None
    BitDepth: Optional[str] = None
    BitOrder: Optional[str] = None
    Signed: Optional[str] = None

class CancelJobRequestRequestTypeDef(BaseModel):
    Id: str

class TimeSpanTypeDef(BaseModel):
    StartTime: Optional[str] = None
    Duration: Optional[str] = None

class HlsContentProtectionTypeDef(BaseModel):
    Method: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    InitializationVector: Optional[str] = None
    LicenseAcquisitionUrl: Optional[str] = None
    KeyStoragePolicy: Optional[str] = None

class PlayReadyDrmTypeDef(BaseModel):
    Format: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    KeyId: Optional[str] = None
    InitializationVector: Optional[str] = None
    LicenseAcquisitionUrl: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class NotificationsTypeDef(BaseModel):
    Progressing: Optional[str] = None
    Completed: Optional[str] = None
    Warning: Optional[str] = None
    Error: Optional[str] = None

class WarningTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ThumbnailsTypeDef(BaseModel):
    Format: Optional[str] = None
    Interval: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None

class DeletePipelineRequestRequestTypeDef(BaseModel):
    Id: str

class DeletePresetRequestRequestTypeDef(BaseModel):
    Id: str

class DetectedPropertiesTypeDef(BaseModel):
    Width: Optional[int] = None
    Height: Optional[int] = None
    FrameRate: Optional[str] = None
    FileSize: Optional[int] = None
    DurationMillis: Optional[int] = None

class TimingTypeDef(BaseModel):
    SubmitTimeMillis: Optional[int] = None
    StartTimeMillis: Optional[int] = None
    FinishTimeMillis: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListJobsByPipelineRequestRequestTypeDef(BaseModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class ListJobsByStatusRequestRequestTypeDef(BaseModel):
    Status: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class ListPipelinesRequestRequestTypeDef(BaseModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class ListPresetsRequestRequestTypeDef(BaseModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class PermissionExtraOutputTypeDef(BaseModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[List[str]] = None

class PermissionOutputTypeDef(BaseModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[List[str]] = None

class PermissionTypeDef(BaseModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[Sequence[str]] = None

class PresetWatermarkTypeDef(BaseModel):
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

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class ReadJobRequestRequestTypeDef(BaseModel):
    Id: str

class ReadPipelineRequestRequestTypeDef(BaseModel):
    Id: str

class ReadPresetRequestRequestTypeDef(BaseModel):
    Id: str

class TestRoleRequestRequestTypeDef(BaseModel):
    Role: str
    InputBucket: str
    OutputBucket: str
    Topics: Sequence[str]

class UpdatePipelineStatusRequestRequestTypeDef(BaseModel):
    Id: str
    Status: str

class ArtworkTypeDef(BaseModel):
    InputKey: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None
    AlbumArtFormat: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class CaptionFormatTypeDef(BaseModel):
    Format: Optional[str] = None
    Pattern: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class CaptionSourceTypeDef(BaseModel):
    Key: Optional[str] = None
    Language: Optional[str] = None
    TimeOffset: Optional[str] = None
    Label: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class JobWatermarkTypeDef(BaseModel):
    PresetWatermarkId: Optional[str] = None
    InputKey: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class AudioParametersTypeDef(BaseModel):
    Codec: Optional[str] = None
    SampleRate: Optional[str] = None
    BitRate: Optional[str] = None
    Channels: Optional[str] = None
    AudioPackingMode: Optional[str] = None
    CodecOptions: Optional[AudioCodecOptionsTypeDef] = None

class ClipTypeDef(BaseModel):
    TimeSpan: Optional[TimeSpanTypeDef] = None

class CreateJobPlaylistTypeDef(BaseModel):
    Name: Optional[str] = None
    Format: Optional[str] = None
    OutputKeys: Optional[Sequence[str]] = None
    HlsContentProtection: Optional[HlsContentProtectionTypeDef] = None
    PlayReadyDrm: Optional[PlayReadyDrmTypeDef] = None

class PlaylistTypeDef(BaseModel):
    Name: Optional[str] = None
    Format: Optional[str] = None
    OutputKeys: Optional[List[str]] = None
    HlsContentProtection: Optional[HlsContentProtectionTypeDef] = None
    PlayReadyDrm: Optional[PlayReadyDrmTypeDef] = None
    Status: Optional[str] = None
    StatusDetail: Optional[str] = None

class TestRoleResponseTypeDef(BaseModel):
    Success: str
    Messages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineNotificationsRequestRequestTypeDef(BaseModel):
    Id: str
    Notifications: NotificationsTypeDef

class ListJobsByPipelineRequestListJobsByPipelinePaginateTypeDef(BaseModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsByStatusRequestListJobsByStatusPaginateTypeDef(BaseModel):
    Status: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesRequestListPipelinesPaginateTypeDef(BaseModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPresetsRequestListPresetsPaginateTypeDef(BaseModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PipelineOutputConfigExtraOutputTypeDef(BaseModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[List[PermissionExtraOutputTypeDef]] = None

class PipelineOutputConfigOutputTypeDef(BaseModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[List[PermissionOutputTypeDef]] = None

class PipelineOutputConfigTypeDef(BaseModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[Sequence[PermissionTypeDef]] = None

class VideoParametersExtraOutputTypeDef(BaseModel):
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
    Watermarks: Optional[List[PresetWatermarkTypeDef]] = None

class VideoParametersOutputTypeDef(BaseModel):
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
    Watermarks: Optional[List[PresetWatermarkTypeDef]] = None

class VideoParametersTypeDef(BaseModel):
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
    Watermarks: Optional[Sequence[PresetWatermarkTypeDef]] = None

class ReadJobRequestJobCompleteWaitTypeDef(BaseModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class JobAlbumArtOutputTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[List[ArtworkTypeDef]] = None

class JobAlbumArtTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[Sequence[ArtworkTypeDef]] = None

class CaptionsOutputTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None
    CaptionFormats: Optional[List[CaptionFormatTypeDef]] = None

class CaptionsTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSourceTypeDef]] = None
    CaptionFormats: Optional[Sequence[CaptionFormatTypeDef]] = None

class InputCaptionsExtraOutputTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None

class InputCaptionsOutputTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None

class InputCaptionsTypeDef(BaseModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSourceTypeDef]] = None

class PipelineTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[str] = None
    InputBucket: Optional[str] = None
    OutputBucket: Optional[str] = None
    Role: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigOutputTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigOutputTypeDef] = None

class CreatePipelineRequestRequestTypeDef(BaseModel):
    Name: str
    InputBucket: str
    Role: str
    OutputBucket: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigTypeDef] = None

class UpdatePipelineRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    InputBucket: Optional[str] = None
    Role: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigTypeDef] = None

class PresetTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Container: Optional[str] = None
    Audio: Optional[AudioParametersTypeDef] = None
    Video: Optional[VideoParametersOutputTypeDef] = None
    Thumbnails: Optional[ThumbnailsTypeDef] = None
    Type: Optional[str] = None

class CreatePresetRequestRequestTypeDef(BaseModel):
    Name: str
    Container: str
    Description: Optional[str] = None
    Video: Optional[VideoParametersTypeDef] = None
    Audio: Optional[AudioParametersTypeDef] = None
    Thumbnails: Optional[ThumbnailsTypeDef] = None

class JobOutputTypeDef(BaseModel):
    Id: Optional[str] = None
    Key: Optional[str] = None
    ThumbnailPattern: Optional[str] = None
    ThumbnailEncryption: Optional[EncryptionTypeDef] = None
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
    Watermarks: Optional[List[JobWatermarkTypeDef]] = None
    AlbumArt: Optional[JobAlbumArtOutputTypeDef] = None
    Composition: Optional[List[ClipTypeDef]] = None
    Captions: Optional[CaptionsOutputTypeDef] = None
    Encryption: Optional[EncryptionTypeDef] = None
    AppliedColorSpaceConversion: Optional[str] = None

class CreateJobOutputTypeDef(BaseModel):
    Key: Optional[str] = None
    ThumbnailPattern: Optional[str] = None
    ThumbnailEncryption: Optional[EncryptionTypeDef] = None
    Rotate: Optional[str] = None
    PresetId: Optional[str] = None
    SegmentDuration: Optional[str] = None
    Watermarks: Optional[Sequence[JobWatermarkTypeDef]] = None
    AlbumArt: Optional[JobAlbumArtTypeDef] = None
    Composition: Optional[Sequence[ClipTypeDef]] = None
    Captions: Optional[CaptionsTypeDef] = None
    Encryption: Optional[EncryptionTypeDef] = None

class JobInputExtraOutputTypeDef(BaseModel):
    Key: Optional[str] = None
    FrameRate: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    Interlaced: Optional[str] = None
    Container: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    TimeSpan: Optional[TimeSpanTypeDef] = None
    InputCaptions: Optional[InputCaptionsExtraOutputTypeDef] = None
    DetectedProperties: Optional[DetectedPropertiesTypeDef] = None

class JobInputOutputTypeDef(BaseModel):
    Key: Optional[str] = None
    FrameRate: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    Interlaced: Optional[str] = None
    Container: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    TimeSpan: Optional[TimeSpanTypeDef] = None
    InputCaptions: Optional[InputCaptionsOutputTypeDef] = None
    DetectedProperties: Optional[DetectedPropertiesTypeDef] = None

class JobInputTypeDef(BaseModel):
    Key: Optional[str] = None
    FrameRate: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    Interlaced: Optional[str] = None
    Container: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None
    TimeSpan: Optional[TimeSpanTypeDef] = None
    InputCaptions: Optional[InputCaptionsTypeDef] = None
    DetectedProperties: Optional[DetectedPropertiesTypeDef] = None

class CreatePipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    Warnings: List[WarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPipelinesResponseTypeDef(BaseModel):
    Pipelines: List[PipelineTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadPipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    Warnings: List[WarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineNotificationsResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    Warnings: List[WarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineStatusResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresetResponseTypeDef(BaseModel):
    Preset: PresetTypeDef
    Warning: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPresetsResponseTypeDef(BaseModel):
    Presets: List[PresetTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadPresetResponseTypeDef(BaseModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    PipelineId: Optional[str] = None
    Input: Optional[JobInputOutputTypeDef] = None
    Inputs: Optional[List[JobInputOutputTypeDef]] = None
    Output: Optional[JobOutputTypeDef] = None
    Outputs: Optional[List[JobOutputTypeDef]] = None
    OutputKeyPrefix: Optional[str] = None
    Playlists: Optional[List[PlaylistTypeDef]] = None
    Status: Optional[str] = None
    UserMetadata: Optional[Dict[str, str]] = None
    Timing: Optional[TimingTypeDef] = None

class CreateJobResponseTypeDef(BaseModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsByPipelineResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsByStatusResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadJobResponseTypeDef(BaseModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestRequestTypeDef(BaseModel):
    PipelineId: str
    Input: Optional[JobInputTypeDef] = None
    Inputs: Optional[Sequence[JobInputUnionTypeDef]] = None
    Output: Optional[CreateJobOutputTypeDef] = None
    Outputs: Optional[Sequence[CreateJobOutputTypeDef]] = None
    OutputKeyPrefix: Optional[str] = None
    Playlists: Optional[Sequence[CreateJobPlaylistTypeDef]] = None
    UserMetadata: Optional[Mapping[str, str]] = None

