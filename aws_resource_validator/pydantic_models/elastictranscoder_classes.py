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
from aws_resource_validator.pydantic_models.elastictranscoder_constants import *

class EncryptionTypeDef(BaseValidatorModel):
    Mode: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    InitializationVector: Optional[str] = None

class AudioCodecOptionsTypeDef(BaseValidatorModel):
    Profile: Optional[str] = None
    BitDepth: Optional[str] = None
    BitOrder: Optional[str] = None
    Signed: Optional[str] = None

class CancelJobRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class TimeSpanTypeDef(BaseValidatorModel):
    StartTime: Optional[str] = None
    Duration: Optional[str] = None

class HlsContentProtectionTypeDef(BaseValidatorModel):
    Method: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    InitializationVector: Optional[str] = None
    LicenseAcquisitionUrl: Optional[str] = None
    KeyStoragePolicy: Optional[str] = None

class PlayReadyDrmTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    Key: Optional[str] = None
    KeyMd5: Optional[str] = None
    KeyId: Optional[str] = None
    InitializationVector: Optional[str] = None
    LicenseAcquisitionUrl: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class NotificationsTypeDef(BaseValidatorModel):
    Progressing: Optional[str] = None
    Completed: Optional[str] = None
    Warning: Optional[str] = None
    Error: Optional[str] = None

class WarningTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ThumbnailsTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    Interval: Optional[str] = None
    Resolution: Optional[str] = None
    AspectRatio: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None

class DeletePipelineRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeletePresetRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DetectedPropertiesTypeDef(BaseValidatorModel):
    Width: Optional[int] = None
    Height: Optional[int] = None
    FrameRate: Optional[str] = None
    FileSize: Optional[int] = None
    DurationMillis: Optional[int] = None

class TimingTypeDef(BaseValidatorModel):
    SubmitTimeMillis: Optional[int] = None
    StartTimeMillis: Optional[int] = None
    FinishTimeMillis: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListJobsByPipelineRequestRequestTypeDef(BaseValidatorModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class ListJobsByStatusRequestRequestTypeDef(BaseValidatorModel):
    Status: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class ListPipelinesRequestRequestTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class ListPresetsRequestRequestTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None

class PermissionExtraOutputTypeDef(BaseValidatorModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[List[str]] = None

class PermissionOutputTypeDef(BaseValidatorModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[List[str]] = None

class PermissionTypeDef(BaseValidatorModel):
    GranteeType: Optional[str] = None
    Grantee: Optional[str] = None
    Access: Optional[Sequence[str]] = None

class PresetWatermarkTypeDef(BaseValidatorModel):
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

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class ReadJobRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class ReadPipelineRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class ReadPresetRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class TestRoleRequestRequestTypeDef(BaseValidatorModel):
    Role: str
    InputBucket: str
    OutputBucket: str
    Topics: Sequence[str]

class UpdatePipelineStatusRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Status: str

class ArtworkTypeDef(BaseValidatorModel):
    InputKey: Optional[str] = None
    MaxWidth: Optional[str] = None
    MaxHeight: Optional[str] = None
    SizingPolicy: Optional[str] = None
    PaddingPolicy: Optional[str] = None
    AlbumArtFormat: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class CaptionFormatTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    Pattern: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class CaptionSourceTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Language: Optional[str] = None
    TimeOffset: Optional[str] = None
    Label: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class JobWatermarkTypeDef(BaseValidatorModel):
    PresetWatermarkId: Optional[str] = None
    InputKey: Optional[str] = None
    Encryption: Optional[EncryptionTypeDef] = None

class AudioParametersTypeDef(BaseValidatorModel):
    Codec: Optional[str] = None
    SampleRate: Optional[str] = None
    BitRate: Optional[str] = None
    Channels: Optional[str] = None
    AudioPackingMode: Optional[str] = None
    CodecOptions: Optional[AudioCodecOptionsTypeDef] = None

class ClipTypeDef(BaseValidatorModel):
    TimeSpan: Optional[TimeSpanTypeDef] = None

class CreateJobPlaylistTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Format: Optional[str] = None
    OutputKeys: Optional[Sequence[str]] = None
    HlsContentProtection: Optional[HlsContentProtectionTypeDef] = None
    PlayReadyDrm: Optional[PlayReadyDrmTypeDef] = None

class PlaylistTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Format: Optional[str] = None
    OutputKeys: Optional[List[str]] = None
    HlsContentProtection: Optional[HlsContentProtectionTypeDef] = None
    PlayReadyDrm: Optional[PlayReadyDrmTypeDef] = None
    Status: Optional[str] = None
    StatusDetail: Optional[str] = None

class TestRoleResponseTypeDef(BaseValidatorModel):
    Success: str
    Messages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineNotificationsRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Notifications: NotificationsTypeDef

class ListJobsByPipelineRequestListJobsByPipelinePaginateTypeDef(BaseValidatorModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsByStatusRequestListJobsByStatusPaginateTypeDef(BaseValidatorModel):
    Status: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesRequestListPipelinesPaginateTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPresetsRequestListPresetsPaginateTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PipelineOutputConfigExtraOutputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[List[PermissionExtraOutputTypeDef]] = None

class PipelineOutputConfigOutputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[List[PermissionOutputTypeDef]] = None

class PipelineOutputConfigTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[Sequence[PermissionTypeDef]] = None

class VideoParametersExtraOutputTypeDef(BaseValidatorModel):
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

class VideoParametersOutputTypeDef(BaseValidatorModel):
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

class VideoParametersTypeDef(BaseValidatorModel):
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

class ReadJobRequestJobCompleteWaitTypeDef(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class JobAlbumArtOutputTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[List[ArtworkTypeDef]] = None

class JobAlbumArtTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[Sequence[ArtworkTypeDef]] = None

class CaptionsOutputTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None
    CaptionFormats: Optional[List[CaptionFormatTypeDef]] = None

class CaptionsTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSourceTypeDef]] = None
    CaptionFormats: Optional[Sequence[CaptionFormatTypeDef]] = None

class InputCaptionsExtraOutputTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None

class InputCaptionsOutputTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None

class InputCaptionsTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSourceTypeDef]] = None

class PipelineTypeDef(BaseValidatorModel):
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

class CreatePipelineRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    InputBucket: str
    Role: str
    OutputBucket: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigTypeDef] = None

class UpdatePipelineRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    InputBucket: Optional[str] = None
    Role: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigTypeDef] = None

class PresetTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Container: Optional[str] = None
    Audio: Optional[AudioParametersTypeDef] = None
    Video: Optional[VideoParametersOutputTypeDef] = None
    Thumbnails: Optional[ThumbnailsTypeDef] = None
    Type: Optional[str] = None

class CreatePresetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Container: str
    Description: Optional[str] = None
    Video: Optional[VideoParametersTypeDef] = None
    Audio: Optional[AudioParametersTypeDef] = None
    Thumbnails: Optional[ThumbnailsTypeDef] = None

class JobOutputTypeDef(BaseValidatorModel):
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

class CreateJobOutputTypeDef(BaseValidatorModel):
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

class JobInputExtraOutputTypeDef(BaseValidatorModel):
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

class JobInputOutputTypeDef(BaseValidatorModel):
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

class JobInputTypeDef(BaseValidatorModel):
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

class CreatePipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    Warnings: List[WarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPipelinesResponseTypeDef(BaseValidatorModel):
    Pipelines: List[PipelineTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadPipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    Warnings: List[WarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineNotificationsResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    Warnings: List[WarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineStatusResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresetResponseTypeDef(BaseValidatorModel):
    Preset: PresetTypeDef
    Warning: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPresetsResponseTypeDef(BaseValidatorModel):
    Presets: List[PresetTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadPresetResponseTypeDef(BaseValidatorModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobTypeDef(BaseValidatorModel):
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

class CreateJobResponseTypeDef(BaseValidatorModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsByPipelineResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsByStatusResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReadJobResponseTypeDef(BaseValidatorModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestRequestTypeDef(BaseValidatorModel):
    PipelineId: str
    Input: Optional[JobInputTypeDef] = None
    Inputs: Optional[Sequence[JobInputUnionTypeDef]] = None
    Output: Optional[CreateJobOutputTypeDef] = None
    Outputs: Optional[Sequence[CreateJobOutputTypeDef]] = None
    OutputKeyPrefix: Optional[str] = None
    Playlists: Optional[Sequence[CreateJobPlaylistTypeDef]] = None
    UserMetadata: Optional[Mapping[str, str]] = None

