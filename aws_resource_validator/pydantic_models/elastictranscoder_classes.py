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


class CancelJobRequestTypeDef(BaseValidatorModel):
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


class DeletePipelineRequestTypeDef(BaseValidatorModel):
    Id: str


class DeletePresetRequestTypeDef(BaseValidatorModel):
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


class ListJobsByPipelineRequestTypeDef(BaseValidatorModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class ListJobsByStatusRequestTypeDef(BaseValidatorModel):
    Status: str
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class ListPipelinesRequestTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


class ListPresetsRequestTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PageToken: Optional[str] = None


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


class ReadJobRequestTypeDef(BaseValidatorModel):
    Id: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ReadPipelineRequestTypeDef(BaseValidatorModel):
    Id: str


class ReadPresetRequestTypeDef(BaseValidatorModel):
    Id: str


class TestRoleRequestTypeDef(BaseValidatorModel):
    Role: str
    InputBucket: str
    OutputBucket: str
    Topics: Sequence[str]


class UpdatePipelineStatusRequestTypeDef(BaseValidatorModel):
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


class NotificationsTypeDef(BaseValidatorModel):
    pass


class UpdatePipelineNotificationsRequestTypeDef(BaseValidatorModel):
    Id: str
    Notifications: NotificationsTypeDef


class ListJobsByPipelineRequestPaginateTypeDef(BaseValidatorModel):
    PipelineId: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsByStatusRequestPaginateTypeDef(BaseValidatorModel):
    Status: str
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPipelinesRequestPaginateTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPresetsRequestPaginateTypeDef(BaseValidatorModel):
    Ascending: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PipelineOutputConfigOutputTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[List[PermissionOutputTypeDef]] = None


class PipelineOutputConfigTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    StorageClass: Optional[str] = None
    Permissions: Optional[Sequence[PermissionTypeDef]] = None


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


class ReadJobRequestWaitTypeDef(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class JobAlbumArtOutputTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[List[ArtworkTypeDef]] = None


class JobAlbumArtTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    Artwork: Optional[Sequence[ArtworkTypeDef]] = None


class CaptionFormatTypeDef(BaseValidatorModel):
    pass


class CaptionsOutputTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[List[CaptionSourceTypeDef]] = None
    CaptionFormats: Optional[List[CaptionFormatTypeDef]] = None


class CaptionsTypeDef(BaseValidatorModel):
    MergePolicy: Optional[str] = None
    CaptionSources: Optional[Sequence[CaptionSourceTypeDef]] = None
    CaptionFormats: Optional[Sequence[CaptionFormatTypeDef]] = None


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


class PipelineOutputConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreatePipelineRequestTypeDef(BaseValidatorModel):
    Name: str
    InputBucket: str
    Role: str
    OutputBucket: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigUnionTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigUnionTypeDef] = None


class UpdatePipelineRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    InputBucket: Optional[str] = None
    Role: Optional[str] = None
    AwsKmsKeyArn: Optional[str] = None
    Notifications: Optional[NotificationsTypeDef] = None
    ContentConfig: Optional[PipelineOutputConfigUnionTypeDef] = None
    ThumbnailConfig: Optional[PipelineOutputConfigUnionTypeDef] = None


class PresetTypeDef(BaseValidatorModel):
    pass


class ListPresetsResponseTypeDef(BaseValidatorModel):
    Presets: List[PresetTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ReadPresetResponseTypeDef(BaseValidatorModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CaptionsUnionTypeDef(BaseValidatorModel):
    pass


class JobAlbumArtUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobOutputTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    ThumbnailPattern: Optional[str] = None
    ThumbnailEncryption: Optional[EncryptionTypeDef] = None
    Rotate: Optional[str] = None
    PresetId: Optional[str] = None
    SegmentDuration: Optional[str] = None
    Watermarks: Optional[Sequence[JobWatermarkTypeDef]] = None
    AlbumArt: Optional[JobAlbumArtUnionTypeDef] = None
    Composition: Optional[Sequence[ClipTypeDef]] = None
    Captions: Optional[CaptionsUnionTypeDef] = None
    Encryption: Optional[EncryptionTypeDef] = None


class JobInputOutputTypeDef(BaseValidatorModel):
    pass


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


class JobInputUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    PipelineId: str
    Input: Optional[JobInputUnionTypeDef] = None
    Inputs: Optional[Sequence[JobInputUnionTypeDef]] = None
    Output: Optional[CreateJobOutputTypeDef] = None
    Outputs: Optional[Sequence[CreateJobOutputTypeDef]] = None
    OutputKeyPrefix: Optional[str] = None
    Playlists: Optional[Sequence[CreateJobPlaylistTypeDef]] = None
    UserMetadata: Optional[Mapping[str, str]] = None


