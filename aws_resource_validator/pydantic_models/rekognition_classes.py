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
from aws_resource_validator.pydantic_models.rekognition_constants import *

class AgeRangeTypeDef(BaseValidatorModel):
    Low: Optional[int] = None
    High: Optional[int] = None


class AssociateFacesRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    UserId: str
    FaceIds: Sequence[str]
    UserMatchThreshold: Optional[float] = None
    ClientRequestToken: Optional[str] = None


class AssociatedFaceTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnsuccessfulFaceAssociationTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Confidence: Optional[float] = None
    Reasons: Optional[List[UnsuccessfulFaceAssociationReasonType]] = None


class AudioMetadataTypeDef(BaseValidatorModel):
    Codec: Optional[str] = None
    DurationMillis: Optional[int] = None
    SampleRate: Optional[int] = None
    NumberOfChannels: Optional[int] = None


class BoundingBoxTypeDef(BaseValidatorModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None


class S3ObjectTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None


class BeardTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class BlackFrameTypeDef(BaseValidatorModel):
    MaxPixelThreshold: Optional[float] = None
    MinCoveragePercentage: Optional[float] = None


class ImageQualityTypeDef(BaseValidatorModel):
    Brightness: Optional[float] = None
    Sharpness: Optional[float] = None


class PoseTypeDef(BaseValidatorModel):
    Roll: Optional[float] = None
    Yaw: Optional[float] = None
    Pitch: Optional[float] = None


class SmileTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class ConnectedHomeSettingsForUpdateTypeDef(BaseValidatorModel):
    Labels: Optional[Sequence[str]] = None
    MinConfidence: Optional[float] = None


class ConnectedHomeSettingsOutputTypeDef(BaseValidatorModel):
    Labels: List[str]
    MinConfidence: Optional[float] = None


class ConnectedHomeSettingsTypeDef(BaseValidatorModel):
    Labels: Sequence[str]
    MinConfidence: Optional[float] = None


class ContentTypeTypeDef(BaseValidatorModel):
    Confidence: Optional[float] = None
    Name: Optional[str] = None


class ModerationLabelTypeDef(BaseValidatorModel):
    Confidence: Optional[float] = None
    Name: Optional[str] = None
    ParentName: Optional[str] = None
    TaxonomyLevel: Optional[int] = None


class OutputConfigTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3KeyPrefix: Optional[str] = None


class CoversBodyPartTypeDef(BaseValidatorModel):
    Confidence: Optional[float] = None
    Value: Optional[bool] = None


class CreateCollectionRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    Tags: Optional[Mapping[str, str]] = None


class LivenessOutputConfigTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3KeyPrefix: Optional[str] = None


class CreateProjectRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    Feature: Optional[CustomizationFeatureType] = None
    AutoUpdate: Optional[ProjectAutoUpdateType] = None
    Tags: Optional[Mapping[str, str]] = None


class StreamProcessorDataSharingPreferenceTypeDef(BaseValidatorModel):
    OptIn: bool


class StreamProcessorNotificationChannelTypeDef(BaseValidatorModel):
    SNSTopicArn: str


class CreateUserRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    UserId: str
    ClientRequestToken: Optional[str] = None


class CustomizationFeatureContentModerationConfigTypeDef(BaseValidatorModel):
    ConfidenceThreshold: Optional[float] = None


class DatasetStatsTypeDef(BaseValidatorModel):
    LabeledEntries: Optional[int] = None
    TotalEntries: Optional[int] = None
    TotalLabels: Optional[int] = None
    ErrorEntries: Optional[int] = None


class DatasetLabelStatsTypeDef(BaseValidatorModel):
    EntryCount: Optional[int] = None
    BoundingBoxCount: Optional[int] = None


class DatasetMetadataTypeDef(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    DatasetType: Optional[DatasetTypeType] = None
    DatasetArn: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    StatusMessageCode: Optional[DatasetStatusMessageCodeType] = None


class DeleteCollectionRequestTypeDef(BaseValidatorModel):
    CollectionId: str


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    DatasetArn: str


class DeleteFacesRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    FaceIds: Sequence[str]


class UnsuccessfulFaceDeletionTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Reasons: Optional[List[UnsuccessfulFaceDeletionReasonType]] = None


class DeleteProjectPolicyRequestTypeDef(BaseValidatorModel):
    ProjectArn: str
    PolicyName: str
    PolicyRevisionId: Optional[str] = None


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    ProjectArn: str


class DeleteProjectVersionRequestTypeDef(BaseValidatorModel):
    ProjectVersionArn: str


class DeleteStreamProcessorRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    UserId: str
    ClientRequestToken: Optional[str] = None


class DescribeCollectionRequestTypeDef(BaseValidatorModel):
    CollectionId: str


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    DatasetArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeProjectVersionsRequestTypeDef(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeProjectsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProjectNames: Optional[Sequence[str]] = None
    Features: Optional[Sequence[CustomizationFeatureType]] = None


class DescribeStreamProcessorRequestTypeDef(BaseValidatorModel):
    Name: str


class DetectLabelsImageQualityTypeDef(BaseValidatorModel):
    Brightness: Optional[float] = None
    Sharpness: Optional[float] = None
    Contrast: Optional[float] = None


class DominantColorTypeDef(BaseValidatorModel):
    Red: Optional[int] = None
    Blue: Optional[int] = None
    Green: Optional[int] = None
    HexCode: Optional[str] = None
    CSSColor: Optional[str] = None
    SimplifiedColor: Optional[str] = None
    PixelPercent: Optional[float] = None


class DetectLabelsImagePropertiesSettingsTypeDef(BaseValidatorModel):
    MaxDominantColors: Optional[int] = None


class GeneralLabelsSettingsTypeDef(BaseValidatorModel):
    LabelInclusionFilters: Optional[Sequence[str]] = None
    LabelExclusionFilters: Optional[Sequence[str]] = None
    LabelCategoryInclusionFilters: Optional[Sequence[str]] = None
    LabelCategoryExclusionFilters: Optional[Sequence[str]] = None


class HumanLoopActivationOutputTypeDef(BaseValidatorModel):
    HumanLoopArn: Optional[str] = None
    HumanLoopActivationReasons: Optional[List[str]] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[str] = None


class ProtectiveEquipmentSummarizationAttributesTypeDef(BaseValidatorModel):
    MinConfidence: float
    RequiredEquipmentTypes: Sequence[ProtectiveEquipmentTypeType]


class ProtectiveEquipmentSummaryTypeDef(BaseValidatorModel):
    PersonsWithRequiredEquipment: Optional[List[int]] = None
    PersonsWithoutRequiredEquipment: Optional[List[int]] = None
    PersonsIndeterminate: Optional[List[int]] = None


class DetectionFilterTypeDef(BaseValidatorModel):
    MinConfidence: Optional[float] = None
    MinBoundingBoxHeight: Optional[float] = None
    MinBoundingBoxWidth: Optional[float] = None


class DisassociateFacesRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    UserId: str
    FaceIds: Sequence[str]
    ClientRequestToken: Optional[str] = None


class DisassociatedFaceTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None


class UnsuccessfulFaceDisassociationTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Reasons: Optional[List[UnsuccessfulFaceDisassociationReasonType]] = None


class DistributeDatasetTypeDef(BaseValidatorModel):
    Arn: str


class EyeDirectionTypeDef(BaseValidatorModel):
    Yaw: Optional[float] = None
    Pitch: Optional[float] = None
    Confidence: Optional[float] = None


class EyeOpenTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class EyeglassesTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class FaceOccludedTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class GenderTypeDef(BaseValidatorModel):
    Value: Optional[GenderTypeType] = None
    Confidence: Optional[float] = None


class MouthOpenTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class MustacheTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class SunglassesTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class FaceSearchSettingsTypeDef(BaseValidatorModel):
    CollectionId: Optional[str] = None
    FaceMatchThreshold: Optional[float] = None


class PointTypeDef(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None


class GetCelebrityInfoRequestTypeDef(BaseValidatorModel):
    Id: str


class GetCelebrityRecognitionRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[CelebrityRecognitionSortByType] = None


class VideoMetadataTypeDef(BaseValidatorModel):
    Codec: Optional[str] = None
    DurationMillis: Optional[int] = None
    Format: Optional[str] = None
    FrameRate: Optional[float] = None
    FrameHeight: Optional[int] = None
    FrameWidth: Optional[int] = None
    ColorRange: Optional[VideoColorRangeType] = None


class GetContentModerationRequestMetadataTypeDef(BaseValidatorModel):
    SortBy: Optional[ContentModerationSortByType] = None
    AggregateBy: Optional[ContentModerationAggregateByType] = None


class GetContentModerationRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ContentModerationSortByType] = None
    AggregateBy: Optional[ContentModerationAggregateByType] = None


class GetFaceDetectionRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetFaceLivenessSessionResultsRequestTypeDef(BaseValidatorModel):
    SessionId: str


class GetFaceSearchRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[FaceSearchSortByType] = None


class GetLabelDetectionRequestMetadataTypeDef(BaseValidatorModel):
    SortBy: Optional[LabelDetectionSortByType] = None
    AggregateBy: Optional[LabelDetectionAggregateByType] = None


class GetLabelDetectionRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[LabelDetectionSortByType] = None
    AggregateBy: Optional[LabelDetectionAggregateByType] = None


class GetMediaAnalysisJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class MediaAnalysisJobFailureDetailsTypeDef(BaseValidatorModel):
    Code: Optional[MediaAnalysisJobFailureCodeType] = None
    Message: Optional[str] = None


class MediaAnalysisOutputConfigTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3KeyPrefix: Optional[str] = None


class GetPersonTrackingRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[PersonTrackingSortByType] = None


class GetSegmentDetectionRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetTextDetectionRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class HumanLoopDataAttributesTypeDef(BaseValidatorModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None


class KinesisDataStreamTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class KinesisVideoStreamStartSelectorTypeDef(BaseValidatorModel):
    ProducerTimestamp: Optional[int] = None
    FragmentNumber: Optional[str] = None


class KinesisVideoStreamTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class LabelAliasTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class LabelCategoryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class ParentTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class ListCollectionsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatasetEntriesRequestTypeDef(BaseValidatorModel):
    DatasetArn: str
    ContainsLabels: Optional[Sequence[str]] = None
    Labeled: Optional[bool] = None
    SourceRefContains: Optional[str] = None
    HasErrors: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatasetLabelsRequestTypeDef(BaseValidatorModel):
    DatasetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFacesRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    UserId: Optional[str] = None
    FaceIds: Optional[Sequence[str]] = None


class ListMediaAnalysisJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProjectPoliciesRequestTypeDef(BaseValidatorModel):
    ProjectArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProjectPolicyTypeDef(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    PolicyDocument: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class ListStreamProcessorsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StreamProcessorTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[StreamProcessorStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListUsersRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UserTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    UserStatus: Optional[UserStatusType] = None


class MatchedUserTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    UserStatus: Optional[UserStatusType] = None


class MediaAnalysisDetectModerationLabelsConfigTypeDef(BaseValidatorModel):
    MinConfidence: Optional[float] = None
    ProjectVersion: Optional[str] = None


class MediaAnalysisModelVersionsTypeDef(BaseValidatorModel):
    Moderation: Optional[str] = None


class NotificationChannelTypeDef(BaseValidatorModel):
    SNSTopicArn: str
    RoleArn: str


class PutProjectPolicyRequestTypeDef(BaseValidatorModel):
    ProjectArn: str
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None


class S3DestinationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    KeyPrefix: Optional[str] = None


class SearchFacesRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    FaceId: str
    MaxFaces: Optional[int] = None
    FaceMatchThreshold: Optional[float] = None


class SearchUsersRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    UserId: Optional[str] = None
    FaceId: Optional[str] = None
    UserMatchThreshold: Optional[float] = None
    MaxUsers: Optional[int] = None


class SearchedFaceTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None


class SearchedUserTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None


class ShotSegmentTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Confidence: Optional[float] = None


class StartProjectVersionRequestTypeDef(BaseValidatorModel):
    ProjectVersionArn: str
    MinInferenceUnits: int
    MaxInferenceUnits: Optional[int] = None


class StartShotDetectionFilterTypeDef(BaseValidatorModel):
    MinSegmentConfidence: Optional[float] = None


class StreamProcessingStopSelectorTypeDef(BaseValidatorModel):
    MaxDurationInSeconds: Optional[int] = None


class StopProjectVersionRequestTypeDef(BaseValidatorModel):
    ProjectVersionArn: str


class StopStreamProcessorRequestTypeDef(BaseValidatorModel):
    Name: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class CopyProjectVersionResponseTypeDef(BaseValidatorModel):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCollectionResponseTypeDef(BaseValidatorModel):
    StatusCode: int
    CollectionArn: str
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFaceLivenessSessionResponseTypeDef(BaseValidatorModel):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProjectResponseTypeDef(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProjectVersionResponseTypeDef(BaseValidatorModel):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamProcessorResponseTypeDef(BaseValidatorModel):
    StreamProcessorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCollectionResponseTypeDef(BaseValidatorModel):
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProjectResponseTypeDef(BaseValidatorModel):
    Status: ProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProjectVersionResponseTypeDef(BaseValidatorModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCollectionResponseTypeDef(BaseValidatorModel):
    FaceCount: int
    FaceModelVersion: str
    CollectionARN: str
    CreationTimestamp: datetime
    UserCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListCollectionsResponseTypeDef(BaseValidatorModel):
    CollectionIds: List[str]
    FaceModelVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDatasetEntriesResponseTypeDef(BaseValidatorModel):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutProjectPolicyResponseTypeDef(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartCelebrityRecognitionResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartContentModerationResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartFaceDetectionResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartFaceSearchResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartLabelDetectionResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMediaAnalysisJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartPersonTrackingResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartProjectVersionResponseTypeDef(BaseValidatorModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartSegmentDetectionResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartStreamProcessorResponseTypeDef(BaseValidatorModel):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartTextDetectionResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopProjectVersionResponseTypeDef(BaseValidatorModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateFacesResponseTypeDef(BaseValidatorModel):
    AssociatedFaces: List[AssociatedFaceTypeDef]
    UnsuccessfulFaceAssociations: List[UnsuccessfulFaceAssociationTypeDef]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ComparedSourceImageFaceTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None


class FaceTypeDef(BaseValidatorModel):
    FaceId: Optional[str] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    ImageId: Optional[str] = None
    ExternalImageId: Optional[str] = None
    Confidence: Optional[float] = None
    IndexFacesModelVersion: Optional[str] = None
    UserId: Optional[str] = None


class AuditImageTypeDef(BaseValidatorModel):
    Bytes: Optional[bytes] = None
    S3Object: Optional[S3ObjectTypeDef] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None


class GroundTruthManifestTypeDef(BaseValidatorModel):
    S3Object: Optional[S3ObjectTypeDef] = None


class MediaAnalysisInputTypeDef(BaseValidatorModel):
    S3Object: S3ObjectTypeDef


class MediaAnalysisManifestSummaryTypeDef(BaseValidatorModel):
    S3Object: Optional[S3ObjectTypeDef] = None


class SummaryTypeDef(BaseValidatorModel):
    S3Object: Optional[S3ObjectTypeDef] = None


class VideoTypeDef(BaseValidatorModel):
    S3Object: Optional[S3ObjectTypeDef] = None


class StartTechnicalCueDetectionFilterTypeDef(BaseValidatorModel):
    MinSegmentConfidence: Optional[float] = None
    BlackFrame: Optional[BlackFrameTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class DatasetChangesTypeDef(BaseValidatorModel):
    GroundTruth: BlobTypeDef


class ImageTypeDef(BaseValidatorModel):
    Bytes: Optional[BlobTypeDef] = None
    S3Object: Optional[S3ObjectTypeDef] = None


class KnownGenderTypeDef(BaseValidatorModel):
    pass


class GetCelebrityInfoResponseTypeDef(BaseValidatorModel):
    Urls: List[str]
    Name: str
    KnownGender: KnownGenderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmotionTypeDef(BaseValidatorModel):
    pass


class LandmarkTypeDef(BaseValidatorModel):
    pass


class ComparedFaceTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    Landmarks: Optional[List[LandmarkTypeDef]] = None
    Pose: Optional[PoseTypeDef] = None
    Quality: Optional[ImageQualityTypeDef] = None
    Emotions: Optional[List[EmotionTypeDef]] = None
    Smile: Optional[SmileTypeDef] = None


class StreamProcessorSettingsForUpdateTypeDef(BaseValidatorModel):
    ConnectedHomeForUpdate: Optional[ConnectedHomeSettingsForUpdateTypeDef] = None


class ContentModerationDetectionTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    ModerationLabel: Optional[ModerationLabelTypeDef] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None
    ContentTypes: Optional[List[ContentTypeTypeDef]] = None


class CopyProjectVersionRequestTypeDef(BaseValidatorModel):
    SourceProjectArn: str
    SourceProjectVersionArn: str
    DestinationProjectArn: str
    VersionName: str
    OutputConfig: OutputConfigTypeDef
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None


class CreateFaceLivenessSessionRequestSettingsTypeDef(BaseValidatorModel):
    OutputConfig: Optional[LivenessOutputConfigTypeDef] = None
    AuditImagesLimit: Optional[int] = None


class CustomizationFeatureConfigTypeDef(BaseValidatorModel):
    ContentModeration: Optional[CustomizationFeatureContentModerationConfigTypeDef] = None


class DatasetDescriptionTypeDef(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    StatusMessageCode: Optional[DatasetStatusMessageCodeType] = None
    DatasetStats: Optional[DatasetStatsTypeDef] = None


class DatasetLabelDescriptionTypeDef(BaseValidatorModel):
    LabelName: Optional[str] = None
    LabelStats: Optional[DatasetLabelStatsTypeDef] = None


class ProjectDescriptionTypeDef(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Status: Optional[ProjectStatusType] = None
    Datasets: Optional[List[DatasetMetadataTypeDef]] = None
    Feature: Optional[CustomizationFeatureType] = None
    AutoUpdate: Optional[ProjectAutoUpdateType] = None


class DeleteFacesResponseTypeDef(BaseValidatorModel):
    DeletedFaces: List[str]
    UnsuccessfulFaceDeletions: List[UnsuccessfulFaceDeletionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProjectVersionsRequestPaginateTypeDef(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeProjectsRequestPaginateTypeDef(BaseValidatorModel):
    ProjectNames: Optional[Sequence[str]] = None
    Features: Optional[Sequence[CustomizationFeatureType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollectionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetEntriesRequestPaginateTypeDef(BaseValidatorModel):
    DatasetArn: str
    ContainsLabels: Optional[Sequence[str]] = None
    Labeled: Optional[bool] = None
    SourceRefContains: Optional[str] = None
    HasErrors: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetLabelsRequestPaginateTypeDef(BaseValidatorModel):
    DatasetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFacesRequestPaginateTypeDef(BaseValidatorModel):
    CollectionId: str
    UserId: Optional[str] = None
    FaceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    ProjectArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamProcessorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeProjectVersionsRequestWaitExtraTypeDef(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeProjectVersionsRequestWaitTypeDef(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DetectLabelsImageBackgroundTypeDef(BaseValidatorModel):
    Quality: Optional[DetectLabelsImageQualityTypeDef] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None


class DetectLabelsImageForegroundTypeDef(BaseValidatorModel):
    Quality: Optional[DetectLabelsImageQualityTypeDef] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None


class InstanceTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None


class DetectLabelsSettingsTypeDef(BaseValidatorModel):
    GeneralLabels: Optional[GeneralLabelsSettingsTypeDef] = None
    ImageProperties: Optional[DetectLabelsImagePropertiesSettingsTypeDef] = None


class LabelDetectionSettingsTypeDef(BaseValidatorModel):
    GeneralLabels: Optional[GeneralLabelsSettingsTypeDef] = None


class DetectModerationLabelsResponseTypeDef(BaseValidatorModel):
    ModerationLabels: List[ModerationLabelTypeDef]
    ModerationModelVersion: str
    HumanLoopActivationOutput: HumanLoopActivationOutputTypeDef
    ProjectVersion: str
    ContentTypes: List[ContentTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateFacesResponseTypeDef(BaseValidatorModel):
    DisassociatedFaces: List[DisassociatedFaceTypeDef]
    UnsuccessfulFaceDisassociations: List[UnsuccessfulFaceDisassociationTypeDef]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DistributeDatasetEntriesRequestTypeDef(BaseValidatorModel):
    Datasets: Sequence[DistributeDatasetTypeDef]


class FaceDetailTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    AgeRange: Optional[AgeRangeTypeDef] = None
    Smile: Optional[SmileTypeDef] = None
    Eyeglasses: Optional[EyeglassesTypeDef] = None
    Sunglasses: Optional[SunglassesTypeDef] = None
    Gender: Optional[GenderTypeDef] = None
    Beard: Optional[BeardTypeDef] = None
    Mustache: Optional[MustacheTypeDef] = None
    EyesOpen: Optional[EyeOpenTypeDef] = None
    MouthOpen: Optional[MouthOpenTypeDef] = None
    Emotions: Optional[List[EmotionTypeDef]] = None
    Landmarks: Optional[List[LandmarkTypeDef]] = None
    Pose: Optional[PoseTypeDef] = None
    Quality: Optional[ImageQualityTypeDef] = None
    Confidence: Optional[float] = None
    FaceOccluded: Optional[FaceOccludedTypeDef] = None
    EyeDirection: Optional[EyeDirectionTypeDef] = None


class StreamProcessorSettingsOutputTypeDef(BaseValidatorModel):
    FaceSearch: Optional[FaceSearchSettingsTypeDef] = None
    ConnectedHome: Optional[ConnectedHomeSettingsOutputTypeDef] = None


class StreamProcessorSettingsTypeDef(BaseValidatorModel):
    FaceSearch: Optional[FaceSearchSettingsTypeDef] = None
    ConnectedHome: Optional[ConnectedHomeSettingsTypeDef] = None


class GeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None


class RegionOfInterestOutputTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None


class RegionOfInterestTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[Sequence[PointTypeDef]] = None


class HumanLoopConfigTypeDef(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None


class StreamProcessingStartSelectorTypeDef(BaseValidatorModel):
    KVSStreamStartSelector: Optional[KinesisVideoStreamStartSelectorTypeDef] = None


class StreamProcessorInputTypeDef(BaseValidatorModel):
    KinesisVideoStream: Optional[KinesisVideoStreamTypeDef] = None


class ListProjectPoliciesResponseTypeDef(BaseValidatorModel):
    ProjectPolicies: List[ProjectPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListStreamProcessorsResponseTypeDef(BaseValidatorModel):
    StreamProcessors: List[StreamProcessorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UserMatchTypeDef(BaseValidatorModel):
    Similarity: Optional[float] = None
    User: Optional[MatchedUserTypeDef] = None


class MediaAnalysisOperationsConfigTypeDef(BaseValidatorModel):
    DetectModerationLabels: Optional[MediaAnalysisDetectModerationLabelsConfigTypeDef] = None


class MediaAnalysisResultsTypeDef(BaseValidatorModel):
    S3Object: Optional[S3ObjectTypeDef] = None
    ModelVersions: Optional[MediaAnalysisModelVersionsTypeDef] = None


class StreamProcessorOutputTypeDef(BaseValidatorModel):
    KinesisDataStream: Optional[KinesisDataStreamTypeDef] = None
    S3Destination: Optional[S3DestinationTypeDef] = None


class FaceMatchTypeDef(BaseValidatorModel):
    Similarity: Optional[float] = None
    Face: Optional[FaceTypeDef] = None


class ListFacesResponseTypeDef(BaseValidatorModel):
    Faces: List[FaceTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetFaceLivenessSessionResultsResponseTypeDef(BaseValidatorModel):
    SessionId: str
    Status: LivenessSessionStatusType
    Confidence: float
    ReferenceImage: AuditImageTypeDef
    AuditImages: List[AuditImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssetTypeDef(BaseValidatorModel):
    GroundTruthManifest: Optional[GroundTruthManifestTypeDef] = None


class DatasetSourceTypeDef(BaseValidatorModel):
    GroundTruthManifest: Optional[GroundTruthManifestTypeDef] = None
    DatasetArn: Optional[str] = None


class EvaluationResultTypeDef(BaseValidatorModel):
    F1Score: Optional[float] = None
    Summary: Optional[SummaryTypeDef] = None


class StartCelebrityRecognitionRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None


class StartContentModerationRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    MinConfidence: Optional[float] = None
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None


class StartFaceDetectionRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    FaceAttributes: Optional[FaceAttributesType] = None
    JobTag: Optional[str] = None


class StartFaceSearchRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    CollectionId: str
    ClientRequestToken: Optional[str] = None
    FaceMatchThreshold: Optional[float] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None


class StartPersonTrackingRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None


class StartSegmentDetectionFiltersTypeDef(BaseValidatorModel):
    TechnicalCueFilter: Optional[StartTechnicalCueDetectionFilterTypeDef] = None
    ShotFilter: Optional[StartShotDetectionFilterTypeDef] = None


class UpdateDatasetEntriesRequestTypeDef(BaseValidatorModel):
    DatasetArn: str
    Changes: DatasetChangesTypeDef


class CompareFacesRequestTypeDef(BaseValidatorModel):
    SourceImage: ImageTypeDef
    TargetImage: ImageTypeDef
    SimilarityThreshold: Optional[float] = None
    QualityFilter: Optional[QualityFilterType] = None


class DetectCustomLabelsRequestTypeDef(BaseValidatorModel):
    ProjectVersionArn: str
    Image: ImageTypeDef
    MaxResults: Optional[int] = None
    MinConfidence: Optional[float] = None


class DetectFacesRequestTypeDef(BaseValidatorModel):
    Image: ImageTypeDef
    Attributes: Optional[Sequence[AttributeType]] = None


class DetectProtectiveEquipmentRequestTypeDef(BaseValidatorModel):
    Image: ImageTypeDef
    SummarizationAttributes: Optional[ProtectiveEquipmentSummarizationAttributesTypeDef] = None


class IndexFacesRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    Image: ImageTypeDef
    ExternalImageId: Optional[str] = None
    DetectionAttributes: Optional[Sequence[AttributeType]] = None
    MaxFaces: Optional[int] = None
    QualityFilter: Optional[QualityFilterType] = None


class RecognizeCelebritiesRequestTypeDef(BaseValidatorModel):
    Image: ImageTypeDef


class SearchFacesByImageRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    Image: ImageTypeDef
    MaxFaces: Optional[int] = None
    FaceMatchThreshold: Optional[float] = None
    QualityFilter: Optional[QualityFilterType] = None


class SearchUsersByImageRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    Image: ImageTypeDef
    UserMatchThreshold: Optional[float] = None
    MaxUsers: Optional[int] = None
    QualityFilter: Optional[QualityFilterType] = None


class CelebrityTypeDef(BaseValidatorModel):
    Urls: Optional[List[str]] = None
    Name: Optional[str] = None
    Id: Optional[str] = None
    Face: Optional[ComparedFaceTypeDef] = None
    MatchConfidence: Optional[float] = None
    KnownGender: Optional[KnownGenderTypeDef] = None


class CompareFacesMatchTypeDef(BaseValidatorModel):
    Similarity: Optional[float] = None
    Face: Optional[ComparedFaceTypeDef] = None


class GetContentModerationResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    ModerationLabels: List[ContentModerationDetectionTypeDef]
    ModerationModelVersion: str
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    GetRequestMetadata: GetContentModerationRequestMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EquipmentDetectionTypeDef(BaseValidatorModel):
    pass


class ProtectiveEquipmentBodyPartTypeDef(BaseValidatorModel):
    Name: Optional[BodyPartType] = None
    Confidence: Optional[float] = None
    EquipmentDetections: Optional[List[EquipmentDetectionTypeDef]] = None


class CreateFaceLivenessSessionRequestTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    Settings: Optional[CreateFaceLivenessSessionRequestSettingsTypeDef] = None
    ClientRequestToken: Optional[str] = None


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    DatasetDescription: DatasetDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDatasetLabelsResponseTypeDef(BaseValidatorModel):
    DatasetLabelDescriptions: List[DatasetLabelDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeProjectsResponseTypeDef(BaseValidatorModel):
    ProjectDescriptions: List[ProjectDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DetectLabelsImagePropertiesTypeDef(BaseValidatorModel):
    Quality: Optional[DetectLabelsImageQualityTypeDef] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None
    Foreground: Optional[DetectLabelsImageForegroundTypeDef] = None
    Background: Optional[DetectLabelsImageBackgroundTypeDef] = None


class LabelTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Confidence: Optional[float] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    Parents: Optional[List[ParentTypeDef]] = None
    Aliases: Optional[List[LabelAliasTypeDef]] = None
    Categories: Optional[List[LabelCategoryTypeDef]] = None


class DetectLabelsRequestTypeDef(BaseValidatorModel):
    Image: ImageTypeDef
    MaxLabels: Optional[int] = None
    MinConfidence: Optional[float] = None
    Features: Optional[Sequence[DetectLabelsFeatureNameType]] = None
    Settings: Optional[DetectLabelsSettingsTypeDef] = None


class StartLabelDetectionRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    MinConfidence: Optional[float] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None
    Features: Optional[Sequence[Literal["GENERAL_LABELS"]]] = None
    Settings: Optional[LabelDetectionSettingsTypeDef] = None


class CelebrityDetailTypeDef(BaseValidatorModel):
    Urls: Optional[List[str]] = None
    Name: Optional[str] = None
    Id: Optional[str] = None
    Confidence: Optional[float] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Face: Optional[FaceDetailTypeDef] = None
    KnownGender: Optional[KnownGenderTypeDef] = None


class DetectFacesResponseTypeDef(BaseValidatorModel):
    FaceDetails: List[FaceDetailTypeDef]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef


class FaceDetectionTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Face: Optional[FaceDetailTypeDef] = None


class FaceRecordTypeDef(BaseValidatorModel):
    Face: Optional[FaceTypeDef] = None
    FaceDetail: Optional[FaceDetailTypeDef] = None


class PersonDetailTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Face: Optional[FaceDetailTypeDef] = None


class SearchedFaceDetailsTypeDef(BaseValidatorModel):
    FaceDetail: Optional[FaceDetailTypeDef] = None


class UnindexedFaceTypeDef(BaseValidatorModel):
    Reasons: Optional[List[ReasonType]] = None
    FaceDetail: Optional[FaceDetailTypeDef] = None


class UnsearchedFaceTypeDef(BaseValidatorModel):
    FaceDetails: Optional[FaceDetailTypeDef] = None
    Reasons: Optional[List[UnsearchedFaceReasonType]] = None


class CustomLabelTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Confidence: Optional[float] = None
    Geometry: Optional[GeometryTypeDef] = None


class DetectModerationLabelsRequestTypeDef(BaseValidatorModel):
    Image: ImageTypeDef
    MinConfidence: Optional[float] = None
    HumanLoopConfig: Optional[HumanLoopConfigTypeDef] = None
    ProjectVersion: Optional[str] = None


class StartStreamProcessorRequestTypeDef(BaseValidatorModel):
    Name: str
    StartSelector: Optional[StreamProcessingStartSelectorTypeDef] = None
    StopSelector: Optional[StreamProcessingStopSelectorTypeDef] = None


class SearchUsersResponseTypeDef(BaseValidatorModel):
    UserMatches: List[UserMatchTypeDef]
    FaceModelVersion: str
    SearchedFace: SearchedFaceTypeDef
    SearchedUser: SearchedUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartMediaAnalysisJobRequestTypeDef(BaseValidatorModel):
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    ClientRequestToken: Optional[str] = None
    JobName: Optional[str] = None
    KmsKeyId: Optional[str] = None


class GetMediaAnalysisJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobName: str
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Status: MediaAnalysisJobStatusType
    FailureDetails: MediaAnalysisJobFailureDetailsTypeDef
    CreationTimestamp: datetime
    CompletionTimestamp: datetime
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    KmsKeyId: str
    Results: MediaAnalysisResultsTypeDef
    ManifestSummary: MediaAnalysisManifestSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MediaAnalysisJobDescriptionTypeDef(BaseValidatorModel):
    JobId: str
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Status: MediaAnalysisJobStatusType
    CreationTimestamp: datetime
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    JobName: Optional[str] = None
    FailureDetails: Optional[MediaAnalysisJobFailureDetailsTypeDef] = None
    CompletionTimestamp: Optional[datetime] = None
    KmsKeyId: Optional[str] = None
    Results: Optional[MediaAnalysisResultsTypeDef] = None
    ManifestSummary: Optional[MediaAnalysisManifestSummaryTypeDef] = None


class DescribeStreamProcessorResponseTypeDef(BaseValidatorModel):
    Name: str
    StreamProcessorArn: str
    Status: StreamProcessorStatusType
    StatusMessage: str
    CreationTimestamp: datetime
    LastUpdateTimestamp: datetime
    Input: StreamProcessorInputTypeDef
    Output: StreamProcessorOutputTypeDef
    RoleArn: str
    Settings: StreamProcessorSettingsOutputTypeDef
    NotificationChannel: StreamProcessorNotificationChannelTypeDef
    KmsKeyId: str
    RegionsOfInterest: List[RegionOfInterestOutputTypeDef]
    DataSharingPreference: StreamProcessorDataSharingPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SegmentTypeInfoTypeDef(BaseValidatorModel):
    pass


class SegmentDetectionTypeDef(BaseValidatorModel):
    pass


class GetSegmentDetectionResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: List[VideoMetadataTypeDef]
    AudioMetadata: List[AudioMetadataTypeDef]
    Segments: List[SegmentDetectionTypeDef]
    SelectedSegmentTypes: List[SegmentTypeInfoTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchFacesByImageResponseTypeDef(BaseValidatorModel):
    SearchedFaceBoundingBox: BoundingBoxTypeDef
    SearchedFaceConfidence: float
    FaceMatches: List[FaceMatchTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchFacesResponseTypeDef(BaseValidatorModel):
    SearchedFaceId: str
    FaceMatches: List[FaceMatchTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestingDataOutputTypeDef(BaseValidatorModel):
    Assets: Optional[List[AssetTypeDef]] = None
    AutoCreate: Optional[bool] = None


class TestingDataTypeDef(BaseValidatorModel):
    Assets: Optional[Sequence[AssetTypeDef]] = None
    AutoCreate: Optional[bool] = None


class TrainingDataOutputTypeDef(BaseValidatorModel):
    Assets: Optional[List[AssetTypeDef]] = None


class TrainingDataTypeDef(BaseValidatorModel):
    Assets: Optional[Sequence[AssetTypeDef]] = None


class ValidationDataTypeDef(BaseValidatorModel):
    Assets: Optional[List[AssetTypeDef]] = None


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    DatasetType: DatasetTypeType
    ProjectArn: str
    DatasetSource: Optional[DatasetSourceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class StartSegmentDetectionRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    SegmentTypes: Sequence[SegmentTypeType]
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None
    Filters: Optional[StartSegmentDetectionFiltersTypeDef] = None


class RecognizeCelebritiesResponseTypeDef(BaseValidatorModel):
    CelebrityFaces: List[CelebrityTypeDef]
    UnrecognizedFaces: List[ComparedFaceTypeDef]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef


class CompareFacesResponseTypeDef(BaseValidatorModel):
    SourceImageFace: ComparedSourceImageFaceTypeDef
    FaceMatches: List[CompareFacesMatchTypeDef]
    UnmatchedFaces: List[ComparedFaceTypeDef]
    SourceImageOrientationCorrection: OrientationCorrectionType
    TargetImageOrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef


class ProtectiveEquipmentPersonTypeDef(BaseValidatorModel):
    BodyParts: Optional[List[ProtectiveEquipmentBodyPartTypeDef]] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    Id: Optional[int] = None


class DetectLabelsResponseTypeDef(BaseValidatorModel):
    Labels: List[LabelTypeDef]
    OrientationCorrection: OrientationCorrectionType
    LabelModelVersion: str
    ImageProperties: DetectLabelsImagePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LabelDetectionTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Label: Optional[LabelTypeDef] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None


class CelebrityRecognitionTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Celebrity: Optional[CelebrityDetailTypeDef] = None


class GetFaceDetectionResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Faces: List[FaceDetectionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PersonDetectionTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Person: Optional[PersonDetailTypeDef] = None


class PersonMatchTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Person: Optional[PersonDetailTypeDef] = None
    FaceMatches: Optional[List[FaceMatchTypeDef]] = None


class IndexFacesResponseTypeDef(BaseValidatorModel):
    FaceRecords: List[FaceRecordTypeDef]
    OrientationCorrection: OrientationCorrectionType
    FaceModelVersion: str
    UnindexedFaces: List[UnindexedFaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchUsersByImageResponseTypeDef(BaseValidatorModel):
    UserMatches: List[UserMatchTypeDef]
    FaceModelVersion: str
    SearchedFace: SearchedFaceDetailsTypeDef
    UnsearchedFaces: List[UnsearchedFaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetectCustomLabelsResponseTypeDef(BaseValidatorModel):
    CustomLabels: List[CustomLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TextDetectionTypeDef(BaseValidatorModel):
    pass


class DetectTextResponseTypeDef(BaseValidatorModel):
    TextDetections: List[TextDetectionTypeDef]
    TextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class TextDetectionResultTypeDef(BaseValidatorModel):
    Timestamp: Optional[int] = None
    TextDetection: Optional[TextDetectionTypeDef] = None


class StreamProcessorSettingsUnionTypeDef(BaseValidatorModel):
    pass


class RegionOfInterestUnionTypeDef(BaseValidatorModel):
    pass


class CreateStreamProcessorRequestTypeDef(BaseValidatorModel):
    Input: StreamProcessorInputTypeDef
    Output: StreamProcessorOutputTypeDef
    Name: str
    Settings: StreamProcessorSettingsUnionTypeDef
    RoleArn: str
    Tags: Optional[Mapping[str, str]] = None
    NotificationChannel: Optional[StreamProcessorNotificationChannelTypeDef] = None
    KmsKeyId: Optional[str] = None
    RegionsOfInterest: Optional[Sequence[RegionOfInterestUnionTypeDef]] = None
    DataSharingPreference: Optional[StreamProcessorDataSharingPreferenceTypeDef] = None


class DetectTextFiltersTypeDef(BaseValidatorModel):
    WordFilter: Optional[DetectionFilterTypeDef] = None
    RegionsOfInterest: Optional[Sequence[RegionOfInterestUnionTypeDef]] = None


class StartTextDetectionFiltersTypeDef(BaseValidatorModel):
    WordFilter: Optional[DetectionFilterTypeDef] = None
    RegionsOfInterest: Optional[Sequence[RegionOfInterestUnionTypeDef]] = None


class UpdateStreamProcessorRequestTypeDef(BaseValidatorModel):
    Name: str
    SettingsForUpdate: Optional[StreamProcessorSettingsForUpdateTypeDef] = None
    RegionsOfInterestForUpdate: Optional[Sequence[RegionOfInterestUnionTypeDef]] = None
    DataSharingPreferenceForUpdate: Optional[StreamProcessorDataSharingPreferenceTypeDef] = None
    ParametersToDelete: Optional[Sequence[StreamProcessorParameterToDeleteType]] = None


class ListMediaAnalysisJobsResponseTypeDef(BaseValidatorModel):
    MediaAnalysisJobs: List[MediaAnalysisJobDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TestingDataResultTypeDef(BaseValidatorModel):
    Input: Optional[TestingDataOutputTypeDef] = None
    Output: Optional[TestingDataOutputTypeDef] = None
    Validation: Optional[ValidationDataTypeDef] = None


class TrainingDataResultTypeDef(BaseValidatorModel):
    Input: Optional[TrainingDataOutputTypeDef] = None
    Output: Optional[TrainingDataOutputTypeDef] = None
    Validation: Optional[ValidationDataTypeDef] = None


class DetectProtectiveEquipmentResponseTypeDef(BaseValidatorModel):
    ProtectiveEquipmentModelVersion: str
    Persons: List[ProtectiveEquipmentPersonTypeDef]
    Summary: ProtectiveEquipmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLabelDetectionResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Labels: List[LabelDetectionTypeDef]
    LabelModelVersion: str
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    GetRequestMetadata: GetLabelDetectionRequestMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetCelebrityRecognitionResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Celebrities: List[CelebrityRecognitionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetPersonTrackingResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Persons: List[PersonDetectionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetFaceSearchResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Persons: List[PersonMatchTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTextDetectionResponseTypeDef(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    TextDetections: List[TextDetectionResultTypeDef]
    TextModelVersion: str
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DetectTextRequestTypeDef(BaseValidatorModel):
    Image: ImageTypeDef
    Filters: Optional[DetectTextFiltersTypeDef] = None


class StartTextDetectionRequestTypeDef(BaseValidatorModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None
    Filters: Optional[StartTextDetectionFiltersTypeDef] = None


class TrainingDataUnionTypeDef(BaseValidatorModel):
    pass


class TestingDataUnionTypeDef(BaseValidatorModel):
    pass


class CreateProjectVersionRequestTypeDef(BaseValidatorModel):
    ProjectArn: str
    VersionName: str
    OutputConfig: OutputConfigTypeDef
    TrainingData: Optional[TrainingDataUnionTypeDef] = None
    TestingData: Optional[TestingDataUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None
    VersionDescription: Optional[str] = None
    FeatureConfig: Optional[CustomizationFeatureConfigTypeDef] = None


class ProjectVersionDescriptionTypeDef(BaseValidatorModel):
    ProjectVersionArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    MinInferenceUnits: Optional[int] = None
    Status: Optional[ProjectVersionStatusType] = None
    StatusMessage: Optional[str] = None
    BillableTrainingTimeInSeconds: Optional[int] = None
    TrainingEndTimestamp: Optional[datetime] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    TrainingDataResult: Optional[TrainingDataResultTypeDef] = None
    TestingDataResult: Optional[TestingDataResultTypeDef] = None
    EvaluationResult: Optional[EvaluationResultTypeDef] = None
    ManifestSummary: Optional[GroundTruthManifestTypeDef] = None
    KmsKeyId: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None
    SourceProjectVersionArn: Optional[str] = None
    VersionDescription: Optional[str] = None
    Feature: Optional[CustomizationFeatureType] = None
    BaseModelVersion: Optional[str] = None
    FeatureConfig: Optional[CustomizationFeatureConfigTypeDef] = None


class DescribeProjectVersionsResponseTypeDef(BaseValidatorModel):
    ProjectVersionDescriptions: List[ProjectVersionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


