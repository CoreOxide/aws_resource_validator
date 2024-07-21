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
from aws_resource_validator.pydantic_models.rekognition_constants import *

class AgeRangeTypeDef(BaseModel):
    Low: Optional[int] = None
    High: Optional[int] = None

class AssociateFacesRequestRequestTypeDef(BaseModel):
    CollectionId: str
    UserId: str
    FaceIds: Sequence[str]
    UserMatchThreshold: Optional[float] = None
    ClientRequestToken: Optional[str] = None

class AssociatedFaceTypeDef(BaseModel):
    FaceId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnsuccessfulFaceAssociationTypeDef(BaseModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Confidence: Optional[float] = None
    Reasons: Optional[List[UnsuccessfulFaceAssociationReasonType]] = None

class AudioMetadataTypeDef(BaseModel):
    Codec: Optional[str] = None
    DurationMillis: Optional[int] = None
    SampleRate: Optional[int] = None
    NumberOfChannels: Optional[int] = None

class BoundingBoxTypeDef(BaseModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None

class S3ObjectTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None

class BeardTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class BlackFrameTypeDef(BaseModel):
    MaxPixelThreshold: Optional[float] = None
    MinCoveragePercentage: Optional[float] = None

class KnownGenderTypeDef(BaseModel):
    Type: Optional[KnownGenderTypeType] = None

class EmotionTypeDef(BaseModel):
    Type: Optional[EmotionNameType] = None
    Confidence: Optional[float] = None

class ImageQualityTypeDef(BaseModel):
    Brightness: Optional[float] = None
    Sharpness: Optional[float] = None

class LandmarkTypeDef(BaseModel):
    Type: Optional[LandmarkTypeType] = None
    X: Optional[float] = None
    Y: Optional[float] = None

class PoseTypeDef(BaseModel):
    Roll: Optional[float] = None
    Yaw: Optional[float] = None
    Pitch: Optional[float] = None

class SmileTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class ConnectedHomeSettingsForUpdateTypeDef(BaseModel):
    Labels: Optional[Sequence[str]] = None
    MinConfidence: Optional[float] = None

class ConnectedHomeSettingsOutputTypeDef(BaseModel):
    Labels: List[str]
    MinConfidence: Optional[float] = None

class ConnectedHomeSettingsTypeDef(BaseModel):
    Labels: Sequence[str]
    MinConfidence: Optional[float] = None

class ContentTypeTypeDef(BaseModel):
    Confidence: Optional[float] = None
    Name: Optional[str] = None

class ModerationLabelTypeDef(BaseModel):
    Confidence: Optional[float] = None
    Name: Optional[str] = None
    ParentName: Optional[str] = None
    TaxonomyLevel: Optional[int] = None

class OutputConfigTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3KeyPrefix: Optional[str] = None

class CoversBodyPartTypeDef(BaseModel):
    Confidence: Optional[float] = None
    Value: Optional[bool] = None

class CreateCollectionRequestRequestTypeDef(BaseModel):
    CollectionId: str
    Tags: Optional[Mapping[str, str]] = None

class LivenessOutputConfigTypeDef(BaseModel):
    S3Bucket: str
    S3KeyPrefix: Optional[str] = None

class CreateProjectRequestRequestTypeDef(BaseModel):
    ProjectName: str
    Feature: Optional[CustomizationFeatureType] = None
    AutoUpdate: Optional[ProjectAutoUpdateType] = None
    Tags: Optional[Mapping[str, str]] = None

class StreamProcessorDataSharingPreferenceTypeDef(BaseModel):
    OptIn: bool

class StreamProcessorNotificationChannelTypeDef(BaseModel):
    SNSTopicArn: str

class CreateUserRequestRequestTypeDef(BaseModel):
    CollectionId: str
    UserId: str
    ClientRequestToken: Optional[str] = None

class CustomizationFeatureContentModerationConfigTypeDef(BaseModel):
    ConfidenceThreshold: Optional[float] = None

class DatasetStatsTypeDef(BaseModel):
    LabeledEntries: Optional[int] = None
    TotalEntries: Optional[int] = None
    TotalLabels: Optional[int] = None
    ErrorEntries: Optional[int] = None

class DatasetLabelStatsTypeDef(BaseModel):
    EntryCount: Optional[int] = None
    BoundingBoxCount: Optional[int] = None

class DatasetMetadataTypeDef(BaseModel):
    CreationTimestamp: Optional[datetime] = None
    DatasetType: Optional[DatasetTypeType] = None
    DatasetArn: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    StatusMessageCode: Optional[DatasetStatusMessageCodeType] = None

class DeleteCollectionRequestRequestTypeDef(BaseModel):
    CollectionId: str

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    DatasetArn: str

class DeleteFacesRequestRequestTypeDef(BaseModel):
    CollectionId: str
    FaceIds: Sequence[str]

class UnsuccessfulFaceDeletionTypeDef(BaseModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Reasons: Optional[List[UnsuccessfulFaceDeletionReasonType]] = None

class DeleteProjectPolicyRequestRequestTypeDef(BaseModel):
    ProjectArn: str
    PolicyName: str
    PolicyRevisionId: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseModel):
    ProjectArn: str

class DeleteProjectVersionRequestRequestTypeDef(BaseModel):
    ProjectVersionArn: str

class DeleteStreamProcessorRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    CollectionId: str
    UserId: str
    ClientRequestToken: Optional[str] = None

class DescribeCollectionRequestRequestTypeDef(BaseModel):
    CollectionId: str

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    DatasetArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeProjectVersionsRequestRequestTypeDef(BaseModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeProjectsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProjectNames: Optional[Sequence[str]] = None
    Features: Optional[Sequence[CustomizationFeatureType]] = None

class DescribeStreamProcessorRequestRequestTypeDef(BaseModel):
    Name: str

class DetectLabelsImageQualityTypeDef(BaseModel):
    Brightness: Optional[float] = None
    Sharpness: Optional[float] = None
    Contrast: Optional[float] = None

class DominantColorTypeDef(BaseModel):
    Red: Optional[int] = None
    Blue: Optional[int] = None
    Green: Optional[int] = None
    HexCode: Optional[str] = None
    CSSColor: Optional[str] = None
    SimplifiedColor: Optional[str] = None
    PixelPercent: Optional[float] = None

class DetectLabelsImagePropertiesSettingsTypeDef(BaseModel):
    MaxDominantColors: Optional[int] = None

class GeneralLabelsSettingsTypeDef(BaseModel):
    LabelInclusionFilters: Optional[Sequence[str]] = None
    LabelExclusionFilters: Optional[Sequence[str]] = None
    LabelCategoryInclusionFilters: Optional[Sequence[str]] = None
    LabelCategoryExclusionFilters: Optional[Sequence[str]] = None

class HumanLoopActivationOutputTypeDef(BaseModel):
    HumanLoopArn: Optional[str] = None
    HumanLoopActivationReasons: Optional[List[str]] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[str] = None

class ProtectiveEquipmentSummarizationAttributesTypeDef(BaseModel):
    MinConfidence: float
    RequiredEquipmentTypes: Sequence[ProtectiveEquipmentTypeType]

class ProtectiveEquipmentSummaryTypeDef(BaseModel):
    PersonsWithRequiredEquipment: Optional[List[int]] = None
    PersonsWithoutRequiredEquipment: Optional[List[int]] = None
    PersonsIndeterminate: Optional[List[int]] = None

class DetectionFilterTypeDef(BaseModel):
    MinConfidence: Optional[float] = None
    MinBoundingBoxHeight: Optional[float] = None
    MinBoundingBoxWidth: Optional[float] = None

class DisassociateFacesRequestRequestTypeDef(BaseModel):
    CollectionId: str
    UserId: str
    FaceIds: Sequence[str]
    ClientRequestToken: Optional[str] = None

class DisassociatedFaceTypeDef(BaseModel):
    FaceId: Optional[str] = None

class UnsuccessfulFaceDisassociationTypeDef(BaseModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Reasons: Optional[List[UnsuccessfulFaceDisassociationReasonType]] = None

class DistributeDatasetTypeDef(BaseModel):
    Arn: str

class EyeDirectionTypeDef(BaseModel):
    Yaw: Optional[float] = None
    Pitch: Optional[float] = None
    Confidence: Optional[float] = None

class EyeOpenTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class EyeglassesTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class FaceOccludedTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class GenderTypeDef(BaseModel):
    Value: Optional[GenderTypeType] = None
    Confidence: Optional[float] = None

class MouthOpenTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class MustacheTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class SunglassesTypeDef(BaseModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None

class FaceSearchSettingsTypeDef(BaseModel):
    CollectionId: Optional[str] = None
    FaceMatchThreshold: Optional[float] = None

class PointTypeDef(BaseModel):
    X: Optional[float] = None
    Y: Optional[float] = None

class GetCelebrityInfoRequestRequestTypeDef(BaseModel):
    Id: str

class GetCelebrityRecognitionRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[CelebrityRecognitionSortByType] = None

class VideoMetadataTypeDef(BaseModel):
    Codec: Optional[str] = None
    DurationMillis: Optional[int] = None
    Format: Optional[str] = None
    FrameRate: Optional[float] = None
    FrameHeight: Optional[int] = None
    FrameWidth: Optional[int] = None
    ColorRange: Optional[VideoColorRangeType] = None

class GetContentModerationRequestMetadataTypeDef(BaseModel):
    SortBy: Optional[ContentModerationSortByType] = None
    AggregateBy: Optional[ContentModerationAggregateByType] = None

class GetContentModerationRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ContentModerationSortByType] = None
    AggregateBy: Optional[ContentModerationAggregateByType] = None

class GetFaceDetectionRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetFaceLivenessSessionResultsRequestRequestTypeDef(BaseModel):
    SessionId: str

class GetFaceSearchRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[FaceSearchSortByType] = None

class GetLabelDetectionRequestMetadataTypeDef(BaseModel):
    SortBy: Optional[LabelDetectionSortByType] = None
    AggregateBy: Optional[LabelDetectionAggregateByType] = None

class GetLabelDetectionRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[LabelDetectionSortByType] = None
    AggregateBy: Optional[LabelDetectionAggregateByType] = None

class GetMediaAnalysisJobRequestRequestTypeDef(BaseModel):
    JobId: str

class MediaAnalysisJobFailureDetailsTypeDef(BaseModel):
    Code: Optional[MediaAnalysisJobFailureCodeType] = None
    Message: Optional[str] = None

class MediaAnalysisOutputConfigTypeDef(BaseModel):
    S3Bucket: str
    S3KeyPrefix: Optional[str] = None

class GetPersonTrackingRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[PersonTrackingSortByType] = None

class GetSegmentDetectionRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SegmentTypeInfoTypeDef(BaseModel):
    Type: Optional[SegmentTypeType] = None
    ModelVersion: Optional[str] = None

class GetTextDetectionRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class HumanLoopDataAttributesTypeDef(BaseModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None

class KinesisDataStreamTypeDef(BaseModel):
    Arn: Optional[str] = None

class KinesisVideoStreamStartSelectorTypeDef(BaseModel):
    ProducerTimestamp: Optional[int] = None
    FragmentNumber: Optional[str] = None

class KinesisVideoStreamTypeDef(BaseModel):
    Arn: Optional[str] = None

class LabelAliasTypeDef(BaseModel):
    Name: Optional[str] = None

class LabelCategoryTypeDef(BaseModel):
    Name: Optional[str] = None

class ParentTypeDef(BaseModel):
    Name: Optional[str] = None

class ListCollectionsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDatasetEntriesRequestRequestTypeDef(BaseModel):
    DatasetArn: str
    ContainsLabels: Optional[Sequence[str]] = None
    Labeled: Optional[bool] = None
    SourceRefContains: Optional[str] = None
    HasErrors: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDatasetLabelsRequestRequestTypeDef(BaseModel):
    DatasetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFacesRequestRequestTypeDef(BaseModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    UserId: Optional[str] = None
    FaceIds: Optional[Sequence[str]] = None

class ListMediaAnalysisJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProjectPoliciesRequestRequestTypeDef(BaseModel):
    ProjectArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProjectPolicyTypeDef(BaseModel):
    ProjectArn: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    PolicyDocument: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class ListStreamProcessorsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StreamProcessorTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[StreamProcessorStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListUsersRequestRequestTypeDef(BaseModel):
    CollectionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UserTypeDef(BaseModel):
    UserId: Optional[str] = None
    UserStatus: Optional[UserStatusType] = None

class MatchedUserTypeDef(BaseModel):
    UserId: Optional[str] = None
    UserStatus: Optional[UserStatusType] = None

class MediaAnalysisDetectModerationLabelsConfigTypeDef(BaseModel):
    MinConfidence: Optional[float] = None
    ProjectVersion: Optional[str] = None

class MediaAnalysisModelVersionsTypeDef(BaseModel):
    Moderation: Optional[str] = None

class NotificationChannelTypeDef(BaseModel):
    SNSTopicArn: str
    RoleArn: str

class PutProjectPolicyRequestRequestTypeDef(BaseModel):
    ProjectArn: str
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None

class S3DestinationTypeDef(BaseModel):
    Bucket: Optional[str] = None
    KeyPrefix: Optional[str] = None

class SearchFacesRequestRequestTypeDef(BaseModel):
    CollectionId: str
    FaceId: str
    MaxFaces: Optional[int] = None
    FaceMatchThreshold: Optional[float] = None

class SearchUsersRequestRequestTypeDef(BaseModel):
    CollectionId: str
    UserId: Optional[str] = None
    FaceId: Optional[str] = None
    UserMatchThreshold: Optional[float] = None
    MaxUsers: Optional[int] = None

class SearchedFaceTypeDef(BaseModel):
    FaceId: Optional[str] = None

class SearchedUserTypeDef(BaseModel):
    UserId: Optional[str] = None

class ShotSegmentTypeDef(BaseModel):
    Index: Optional[int] = None
    Confidence: Optional[float] = None

class TechnicalCueSegmentTypeDef(BaseModel):
    Type: Optional[TechnicalCueTypeType] = None
    Confidence: Optional[float] = None

class StartProjectVersionRequestRequestTypeDef(BaseModel):
    ProjectVersionArn: str
    MinInferenceUnits: int
    MaxInferenceUnits: Optional[int] = None

class StartShotDetectionFilterTypeDef(BaseModel):
    MinSegmentConfidence: Optional[float] = None

class StreamProcessingStopSelectorTypeDef(BaseModel):
    MaxDurationInSeconds: Optional[int] = None

class StopProjectVersionRequestRequestTypeDef(BaseModel):
    ProjectVersionArn: str

class StopStreamProcessorRequestRequestTypeDef(BaseModel):
    Name: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CopyProjectVersionResponseTypeDef(BaseModel):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollectionResponseTypeDef(BaseModel):
    StatusCode: int
    CollectionArn: str
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(BaseModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFaceLivenessSessionResponseTypeDef(BaseModel):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(BaseModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectVersionResponseTypeDef(BaseModel):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamProcessorResponseTypeDef(BaseModel):
    StreamProcessorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCollectionResponseTypeDef(BaseModel):
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(BaseModel):
    Status: ProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectVersionResponseTypeDef(BaseModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCollectionResponseTypeDef(BaseModel):
    FaceCount: int
    FaceModelVersion: str
    CollectionARN: str
    CreationTimestamp: datetime
    UserCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollectionsResponseTypeDef(BaseModel):
    CollectionIds: List[str]
    FaceModelVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDatasetEntriesResponseTypeDef(BaseModel):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutProjectPolicyResponseTypeDef(BaseModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCelebrityRecognitionResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContentModerationResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFaceDetectionResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFaceSearchResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLabelDetectionResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMediaAnalysisJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPersonTrackingResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartProjectVersionResponseTypeDef(BaseModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSegmentDetectionResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartStreamProcessorResponseTypeDef(BaseModel):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTextDetectionResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopProjectVersionResponseTypeDef(BaseModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateFacesResponseTypeDef(BaseModel):
    AssociatedFaces: List[AssociatedFaceTypeDef]
    UnsuccessfulFaceAssociations: List[UnsuccessfulFaceAssociationTypeDef]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ComparedSourceImageFaceTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None

class FaceTypeDef(BaseModel):
    FaceId: Optional[str] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    ImageId: Optional[str] = None
    ExternalImageId: Optional[str] = None
    Confidence: Optional[float] = None
    IndexFacesModelVersion: Optional[str] = None
    UserId: Optional[str] = None

class AuditImageTypeDef(BaseModel):
    Bytes: Optional[bytes] = None
    S3Object: Optional[S3ObjectTypeDef] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None

class GroundTruthManifestTypeDef(BaseModel):
    S3Object: Optional[S3ObjectTypeDef] = None

class MediaAnalysisInputTypeDef(BaseModel):
    S3Object: S3ObjectTypeDef

class MediaAnalysisManifestSummaryTypeDef(BaseModel):
    S3Object: Optional[S3ObjectTypeDef] = None

class SummaryTypeDef(BaseModel):
    S3Object: Optional[S3ObjectTypeDef] = None

class VideoTypeDef(BaseModel):
    S3Object: Optional[S3ObjectTypeDef] = None

class StartTechnicalCueDetectionFilterTypeDef(BaseModel):
    MinSegmentConfidence: Optional[float] = None
    BlackFrame: Optional[BlackFrameTypeDef] = None

class DatasetChangesTypeDef(BaseModel):
    GroundTruth: BlobTypeDef

class ImageTypeDef(BaseModel):
    Bytes: Optional[BlobTypeDef] = None
    S3Object: Optional[S3ObjectTypeDef] = None

class GetCelebrityInfoResponseTypeDef(BaseModel):
    Urls: List[str]
    Name: str
    KnownGender: KnownGenderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComparedFaceTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    Landmarks: Optional[List[LandmarkTypeDef]] = None
    Pose: Optional[PoseTypeDef] = None
    Quality: Optional[ImageQualityTypeDef] = None
    Emotions: Optional[List[EmotionTypeDef]] = None
    Smile: Optional[SmileTypeDef] = None

class StreamProcessorSettingsForUpdateTypeDef(BaseModel):
    ConnectedHomeForUpdate: Optional[ConnectedHomeSettingsForUpdateTypeDef] = None

class ContentModerationDetectionTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    ModerationLabel: Optional[ModerationLabelTypeDef] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None
    ContentTypes: Optional[List[ContentTypeTypeDef]] = None

class CopyProjectVersionRequestRequestTypeDef(BaseModel):
    SourceProjectArn: str
    SourceProjectVersionArn: str
    DestinationProjectArn: str
    VersionName: str
    OutputConfig: OutputConfigTypeDef
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None

class EquipmentDetectionTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    Type: Optional[ProtectiveEquipmentTypeType] = None
    CoversBodyPart: Optional[CoversBodyPartTypeDef] = None

class CreateFaceLivenessSessionRequestSettingsTypeDef(BaseModel):
    OutputConfig: Optional[LivenessOutputConfigTypeDef] = None
    AuditImagesLimit: Optional[int] = None

class CustomizationFeatureConfigTypeDef(BaseModel):
    ContentModeration: Optional[CustomizationFeatureContentModerationConfigTypeDef] = None

class DatasetDescriptionTypeDef(BaseModel):
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    StatusMessageCode: Optional[DatasetStatusMessageCodeType] = None
    DatasetStats: Optional[DatasetStatsTypeDef] = None

class DatasetLabelDescriptionTypeDef(BaseModel):
    LabelName: Optional[str] = None
    LabelStats: Optional[DatasetLabelStatsTypeDef] = None

class ProjectDescriptionTypeDef(BaseModel):
    ProjectArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Status: Optional[ProjectStatusType] = None
    Datasets: Optional[List[DatasetMetadataTypeDef]] = None
    Feature: Optional[CustomizationFeatureType] = None
    AutoUpdate: Optional[ProjectAutoUpdateType] = None

class DeleteFacesResponseTypeDef(BaseModel):
    DeletedFaces: List[str]
    UnsuccessfulFaceDeletions: List[UnsuccessfulFaceDeletionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProjectVersionsRequestDescribeProjectVersionsPaginateTypeDef(BaseModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeProjectsRequestDescribeProjectsPaginateTypeDef(BaseModel):
    ProjectNames: Optional[Sequence[str]] = None
    Features: Optional[Sequence[CustomizationFeatureType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollectionsRequestListCollectionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef(BaseModel):
    DatasetArn: str
    ContainsLabels: Optional[Sequence[str]] = None
    Labeled: Optional[bool] = None
    SourceRefContains: Optional[str] = None
    HasErrors: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetLabelsRequestListDatasetLabelsPaginateTypeDef(BaseModel):
    DatasetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFacesRequestListFacesPaginateTypeDef(BaseModel):
    CollectionId: str
    UserId: Optional[str] = None
    FaceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectPoliciesRequestListProjectPoliciesPaginateTypeDef(BaseModel):
    ProjectArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamProcessorsRequestListStreamProcessorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeProjectVersionsRequestProjectVersionRunningWaitTypeDef(BaseModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeProjectVersionsRequestProjectVersionTrainingCompletedWaitTypeDef(BaseModel):
    ProjectArn: str
    VersionNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DetectLabelsImageBackgroundTypeDef(BaseModel):
    Quality: Optional[DetectLabelsImageQualityTypeDef] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None

class DetectLabelsImageForegroundTypeDef(BaseModel):
    Quality: Optional[DetectLabelsImageQualityTypeDef] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None

class InstanceTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None

class DetectLabelsSettingsTypeDef(BaseModel):
    GeneralLabels: Optional[GeneralLabelsSettingsTypeDef] = None
    ImageProperties: Optional[DetectLabelsImagePropertiesSettingsTypeDef] = None

class LabelDetectionSettingsTypeDef(BaseModel):
    GeneralLabels: Optional[GeneralLabelsSettingsTypeDef] = None

class DetectModerationLabelsResponseTypeDef(BaseModel):
    ModerationLabels: List[ModerationLabelTypeDef]
    ModerationModelVersion: str
    HumanLoopActivationOutput: HumanLoopActivationOutputTypeDef
    ProjectVersion: str
    ContentTypes: List[ContentTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFacesResponseTypeDef(BaseModel):
    DisassociatedFaces: List[DisassociatedFaceTypeDef]
    UnsuccessfulFaceDisassociations: List[UnsuccessfulFaceDisassociationTypeDef]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DistributeDatasetEntriesRequestRequestTypeDef(BaseModel):
    Datasets: Sequence[DistributeDatasetTypeDef]

class FaceDetailTypeDef(BaseModel):
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

class StreamProcessorSettingsOutputTypeDef(BaseModel):
    FaceSearch: Optional[FaceSearchSettingsTypeDef] = None
    ConnectedHome: Optional[ConnectedHomeSettingsOutputTypeDef] = None

class StreamProcessorSettingsTypeDef(BaseModel):
    FaceSearch: Optional[FaceSearchSettingsTypeDef] = None
    ConnectedHome: Optional[ConnectedHomeSettingsTypeDef] = None

class GeometryTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None

class RegionOfInterestOutputTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None

class RegionOfInterestTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[Sequence[PointTypeDef]] = None

class HumanLoopConfigTypeDef(BaseModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None

class StreamProcessingStartSelectorTypeDef(BaseModel):
    KVSStreamStartSelector: Optional[KinesisVideoStreamStartSelectorTypeDef] = None

class StreamProcessorInputTypeDef(BaseModel):
    KinesisVideoStream: Optional[KinesisVideoStreamTypeDef] = None

class ListProjectPoliciesResponseTypeDef(BaseModel):
    ProjectPolicies: List[ProjectPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStreamProcessorsResponseTypeDef(BaseModel):
    StreamProcessors: List[StreamProcessorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UserMatchTypeDef(BaseModel):
    Similarity: Optional[float] = None
    User: Optional[MatchedUserTypeDef] = None

class MediaAnalysisOperationsConfigTypeDef(BaseModel):
    DetectModerationLabels: Optional[MediaAnalysisDetectModerationLabelsConfigTypeDef] = None

class MediaAnalysisResultsTypeDef(BaseModel):
    S3Object: Optional[S3ObjectTypeDef] = None
    ModelVersions: Optional[MediaAnalysisModelVersionsTypeDef] = None

class StreamProcessorOutputTypeDef(BaseModel):
    KinesisDataStream: Optional[KinesisDataStreamTypeDef] = None
    S3Destination: Optional[S3DestinationTypeDef] = None

class SegmentDetectionTypeDef(BaseModel):
    Type: Optional[SegmentTypeType] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None
    StartTimecodeSMPTE: Optional[str] = None
    EndTimecodeSMPTE: Optional[str] = None
    DurationSMPTE: Optional[str] = None
    TechnicalCueSegment: Optional[TechnicalCueSegmentTypeDef] = None
    ShotSegment: Optional[ShotSegmentTypeDef] = None
    StartFrameNumber: Optional[int] = None
    EndFrameNumber: Optional[int] = None
    DurationFrames: Optional[int] = None

class FaceMatchTypeDef(BaseModel):
    Similarity: Optional[float] = None
    Face: Optional[FaceTypeDef] = None

class ListFacesResponseTypeDef(BaseModel):
    Faces: List[FaceTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetFaceLivenessSessionResultsResponseTypeDef(BaseModel):
    SessionId: str
    Status: LivenessSessionStatusType
    Confidence: float
    ReferenceImage: AuditImageTypeDef
    AuditImages: List[AuditImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssetTypeDef(BaseModel):
    GroundTruthManifest: Optional[GroundTruthManifestTypeDef] = None

class DatasetSourceTypeDef(BaseModel):
    GroundTruthManifest: Optional[GroundTruthManifestTypeDef] = None
    DatasetArn: Optional[str] = None

class EvaluationResultTypeDef(BaseModel):
    F1Score: Optional[float] = None
    Summary: Optional[SummaryTypeDef] = None

class StartCelebrityRecognitionRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None

class StartContentModerationRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    MinConfidence: Optional[float] = None
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None

class StartFaceDetectionRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    FaceAttributes: Optional[FaceAttributesType] = None
    JobTag: Optional[str] = None

class StartFaceSearchRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    CollectionId: str
    ClientRequestToken: Optional[str] = None
    FaceMatchThreshold: Optional[float] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None

class StartPersonTrackingRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None

class StartSegmentDetectionFiltersTypeDef(BaseModel):
    TechnicalCueFilter: Optional[StartTechnicalCueDetectionFilterTypeDef] = None
    ShotFilter: Optional[StartShotDetectionFilterTypeDef] = None

class UpdateDatasetEntriesRequestRequestTypeDef(BaseModel):
    DatasetArn: str
    Changes: DatasetChangesTypeDef

class CompareFacesRequestRequestTypeDef(BaseModel):
    SourceImage: ImageTypeDef
    TargetImage: ImageTypeDef
    SimilarityThreshold: Optional[float] = None
    QualityFilter: Optional[QualityFilterType] = None

class DetectCustomLabelsRequestRequestTypeDef(BaseModel):
    ProjectVersionArn: str
    Image: ImageTypeDef
    MaxResults: Optional[int] = None
    MinConfidence: Optional[float] = None

class DetectFacesRequestRequestTypeDef(BaseModel):
    Image: ImageTypeDef
    Attributes: Optional[Sequence[AttributeType]] = None

class DetectProtectiveEquipmentRequestRequestTypeDef(BaseModel):
    Image: ImageTypeDef
    SummarizationAttributes: Optional[ProtectiveEquipmentSummarizationAttributesTypeDef] = None

class IndexFacesRequestRequestTypeDef(BaseModel):
    CollectionId: str
    Image: ImageTypeDef
    ExternalImageId: Optional[str] = None
    DetectionAttributes: Optional[Sequence[AttributeType]] = None
    MaxFaces: Optional[int] = None
    QualityFilter: Optional[QualityFilterType] = None

class RecognizeCelebritiesRequestRequestTypeDef(BaseModel):
    Image: ImageTypeDef

class SearchFacesByImageRequestRequestTypeDef(BaseModel):
    CollectionId: str
    Image: ImageTypeDef
    MaxFaces: Optional[int] = None
    FaceMatchThreshold: Optional[float] = None
    QualityFilter: Optional[QualityFilterType] = None

class SearchUsersByImageRequestRequestTypeDef(BaseModel):
    CollectionId: str
    Image: ImageTypeDef
    UserMatchThreshold: Optional[float] = None
    MaxUsers: Optional[int] = None
    QualityFilter: Optional[QualityFilterType] = None

class CelebrityTypeDef(BaseModel):
    Urls: Optional[List[str]] = None
    Name: Optional[str] = None
    Id: Optional[str] = None
    Face: Optional[ComparedFaceTypeDef] = None
    MatchConfidence: Optional[float] = None
    KnownGender: Optional[KnownGenderTypeDef] = None

class CompareFacesMatchTypeDef(BaseModel):
    Similarity: Optional[float] = None
    Face: Optional[ComparedFaceTypeDef] = None

class GetContentModerationResponseTypeDef(BaseModel):
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

class ProtectiveEquipmentBodyPartTypeDef(BaseModel):
    Name: Optional[BodyPartType] = None
    Confidence: Optional[float] = None
    EquipmentDetections: Optional[List[EquipmentDetectionTypeDef]] = None

class CreateFaceLivenessSessionRequestRequestTypeDef(BaseModel):
    KmsKeyId: Optional[str] = None
    Settings: Optional[CreateFaceLivenessSessionRequestSettingsTypeDef] = None
    ClientRequestToken: Optional[str] = None

class DescribeDatasetResponseTypeDef(BaseModel):
    DatasetDescription: DatasetDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetLabelsResponseTypeDef(BaseModel):
    DatasetLabelDescriptions: List[DatasetLabelDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeProjectsResponseTypeDef(BaseModel):
    ProjectDescriptions: List[ProjectDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetectLabelsImagePropertiesTypeDef(BaseModel):
    Quality: Optional[DetectLabelsImageQualityTypeDef] = None
    DominantColors: Optional[List[DominantColorTypeDef]] = None
    Foreground: Optional[DetectLabelsImageForegroundTypeDef] = None
    Background: Optional[DetectLabelsImageBackgroundTypeDef] = None

class LabelTypeDef(BaseModel):
    Name: Optional[str] = None
    Confidence: Optional[float] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    Parents: Optional[List[ParentTypeDef]] = None
    Aliases: Optional[List[LabelAliasTypeDef]] = None
    Categories: Optional[List[LabelCategoryTypeDef]] = None

class DetectLabelsRequestRequestTypeDef(BaseModel):
    Image: ImageTypeDef
    MaxLabels: Optional[int] = None
    MinConfidence: Optional[float] = None
    Features: Optional[Sequence[DetectLabelsFeatureNameType]] = None
    Settings: Optional[DetectLabelsSettingsTypeDef] = None

class StartLabelDetectionRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    MinConfidence: Optional[float] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None
    Features: Optional[Sequence[Literal["GENERAL_LABELS"]]] = None
    Settings: Optional[LabelDetectionSettingsTypeDef] = None

class CelebrityDetailTypeDef(BaseModel):
    Urls: Optional[List[str]] = None
    Name: Optional[str] = None
    Id: Optional[str] = None
    Confidence: Optional[float] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Face: Optional[FaceDetailTypeDef] = None
    KnownGender: Optional[KnownGenderTypeDef] = None

class DetectFacesResponseTypeDef(BaseModel):
    FaceDetails: List[FaceDetailTypeDef]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef

class FaceDetectionTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    Face: Optional[FaceDetailTypeDef] = None

class FaceRecordTypeDef(BaseModel):
    Face: Optional[FaceTypeDef] = None
    FaceDetail: Optional[FaceDetailTypeDef] = None

class PersonDetailTypeDef(BaseModel):
    Index: Optional[int] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Face: Optional[FaceDetailTypeDef] = None

class SearchedFaceDetailsTypeDef(BaseModel):
    FaceDetail: Optional[FaceDetailTypeDef] = None

class UnindexedFaceTypeDef(BaseModel):
    Reasons: Optional[List[ReasonType]] = None
    FaceDetail: Optional[FaceDetailTypeDef] = None

class UnsearchedFaceTypeDef(BaseModel):
    FaceDetails: Optional[FaceDetailTypeDef] = None
    Reasons: Optional[List[UnsearchedFaceReasonType]] = None

class CustomLabelTypeDef(BaseModel):
    Name: Optional[str] = None
    Confidence: Optional[float] = None
    Geometry: Optional[GeometryTypeDef] = None

class TextDetectionTypeDef(BaseModel):
    DetectedText: Optional[str] = None
    Type: Optional[TextTypesType] = None
    Id: Optional[int] = None
    ParentId: Optional[int] = None
    Confidence: Optional[float] = None
    Geometry: Optional[GeometryTypeDef] = None

class DetectTextFiltersTypeDef(BaseModel):
    WordFilter: Optional[DetectionFilterTypeDef] = None
    RegionsOfInterest: Optional[Sequence[RegionOfInterestTypeDef]] = None

class StartTextDetectionFiltersTypeDef(BaseModel):
    WordFilter: Optional[DetectionFilterTypeDef] = None
    RegionsOfInterest: Optional[Sequence[RegionOfInterestTypeDef]] = None

class DetectModerationLabelsRequestRequestTypeDef(BaseModel):
    Image: ImageTypeDef
    MinConfidence: Optional[float] = None
    HumanLoopConfig: Optional[HumanLoopConfigTypeDef] = None
    ProjectVersion: Optional[str] = None

class StartStreamProcessorRequestRequestTypeDef(BaseModel):
    Name: str
    StartSelector: Optional[StreamProcessingStartSelectorTypeDef] = None
    StopSelector: Optional[StreamProcessingStopSelectorTypeDef] = None

class SearchUsersResponseTypeDef(BaseModel):
    UserMatches: List[UserMatchTypeDef]
    FaceModelVersion: str
    SearchedFace: SearchedFaceTypeDef
    SearchedUser: SearchedUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMediaAnalysisJobRequestRequestTypeDef(BaseModel):
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    ClientRequestToken: Optional[str] = None
    JobName: Optional[str] = None
    KmsKeyId: Optional[str] = None

class GetMediaAnalysisJobResponseTypeDef(BaseModel):
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

class MediaAnalysisJobDescriptionTypeDef(BaseModel):
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

class DescribeStreamProcessorResponseTypeDef(BaseModel):
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

class GetSegmentDetectionResponseTypeDef(BaseModel):
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

class SearchFacesByImageResponseTypeDef(BaseModel):
    SearchedFaceBoundingBox: BoundingBoxTypeDef
    SearchedFaceConfidence: float
    FaceMatches: List[FaceMatchTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFacesResponseTypeDef(BaseModel):
    SearchedFaceId: str
    FaceMatches: List[FaceMatchTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestingDataExtraOutputTypeDef(BaseModel):
    Assets: Optional[List[AssetTypeDef]] = None
    AutoCreate: Optional[bool] = None

class TestingDataOutputTypeDef(BaseModel):
    Assets: Optional[List[AssetTypeDef]] = None
    AutoCreate: Optional[bool] = None

class TestingDataTypeDef(BaseModel):
    Assets: Optional[Sequence[AssetTypeDef]] = None
    AutoCreate: Optional[bool] = None

class TrainingDataExtraOutputTypeDef(BaseModel):
    Assets: Optional[List[AssetTypeDef]] = None

class TrainingDataOutputTypeDef(BaseModel):
    Assets: Optional[List[AssetTypeDef]] = None

class TrainingDataTypeDef(BaseModel):
    Assets: Optional[Sequence[AssetTypeDef]] = None

class ValidationDataTypeDef(BaseModel):
    Assets: Optional[List[AssetTypeDef]] = None

class CreateDatasetRequestRequestTypeDef(BaseModel):
    DatasetType: DatasetTypeType
    ProjectArn: str
    DatasetSource: Optional[DatasetSourceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class StartSegmentDetectionRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    SegmentTypes: Sequence[SegmentTypeType]
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None
    Filters: Optional[StartSegmentDetectionFiltersTypeDef] = None

class RecognizeCelebritiesResponseTypeDef(BaseModel):
    CelebrityFaces: List[CelebrityTypeDef]
    UnrecognizedFaces: List[ComparedFaceTypeDef]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef

class CompareFacesResponseTypeDef(BaseModel):
    SourceImageFace: ComparedSourceImageFaceTypeDef
    FaceMatches: List[CompareFacesMatchTypeDef]
    UnmatchedFaces: List[ComparedFaceTypeDef]
    SourceImageOrientationCorrection: OrientationCorrectionType
    TargetImageOrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectiveEquipmentPersonTypeDef(BaseModel):
    BodyParts: Optional[List[ProtectiveEquipmentBodyPartTypeDef]] = None
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Confidence: Optional[float] = None
    Id: Optional[int] = None

class DetectLabelsResponseTypeDef(BaseModel):
    Labels: List[LabelTypeDef]
    OrientationCorrection: OrientationCorrectionType
    LabelModelVersion: str
    ImageProperties: DetectLabelsImagePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LabelDetectionTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    Label: Optional[LabelTypeDef] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None

class CelebrityRecognitionTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    Celebrity: Optional[CelebrityDetailTypeDef] = None

class GetFaceDetectionResponseTypeDef(BaseModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Faces: List[FaceDetectionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PersonDetectionTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    Person: Optional[PersonDetailTypeDef] = None

class PersonMatchTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    Person: Optional[PersonDetailTypeDef] = None
    FaceMatches: Optional[List[FaceMatchTypeDef]] = None

class IndexFacesResponseTypeDef(BaseModel):
    FaceRecords: List[FaceRecordTypeDef]
    OrientationCorrection: OrientationCorrectionType
    FaceModelVersion: str
    UnindexedFaces: List[UnindexedFaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchUsersByImageResponseTypeDef(BaseModel):
    UserMatches: List[UserMatchTypeDef]
    FaceModelVersion: str
    SearchedFace: SearchedFaceDetailsTypeDef
    UnsearchedFaces: List[UnsearchedFaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectCustomLabelsResponseTypeDef(BaseModel):
    CustomLabels: List[CustomLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectTextResponseTypeDef(BaseModel):
    TextDetections: List[TextDetectionTypeDef]
    TextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class TextDetectionResultTypeDef(BaseModel):
    Timestamp: Optional[int] = None
    TextDetection: Optional[TextDetectionTypeDef] = None

class DetectTextRequestRequestTypeDef(BaseModel):
    Image: ImageTypeDef
    Filters: Optional[DetectTextFiltersTypeDef] = None

class CreateStreamProcessorRequestRequestTypeDef(BaseModel):
    Input: StreamProcessorInputTypeDef
    Output: StreamProcessorOutputTypeDef
    Name: str
    Settings: StreamProcessorSettingsTypeDef
    RoleArn: str
    Tags: Optional[Mapping[str, str]] = None
    NotificationChannel: Optional[StreamProcessorNotificationChannelTypeDef] = None
    KmsKeyId: Optional[str] = None
    RegionsOfInterest: Optional[Sequence[RegionOfInterestUnionTypeDef]] = None
    DataSharingPreference: Optional[StreamProcessorDataSharingPreferenceTypeDef] = None

class UpdateStreamProcessorRequestRequestTypeDef(BaseModel):
    Name: str
    SettingsForUpdate: Optional[StreamProcessorSettingsForUpdateTypeDef] = None
    RegionsOfInterestForUpdate: Optional[Sequence[RegionOfInterestUnionTypeDef]] = None
    DataSharingPreferenceForUpdate: Optional[StreamProcessorDataSharingPreferenceTypeDef] = None
    ParametersToDelete: Optional[Sequence[StreamProcessorParameterToDeleteType]] = None

class StartTextDetectionRequestRequestTypeDef(BaseModel):
    Video: VideoTypeDef
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    JobTag: Optional[str] = None
    Filters: Optional[StartTextDetectionFiltersTypeDef] = None

class ListMediaAnalysisJobsResponseTypeDef(BaseModel):
    MediaAnalysisJobs: List[MediaAnalysisJobDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateProjectVersionRequestRequestTypeDef(BaseModel):
    ProjectArn: str
    VersionName: str
    OutputConfig: OutputConfigTypeDef
    TrainingData: Optional[TrainingDataTypeDef] = None
    TestingData: Optional[TestingDataTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None
    VersionDescription: Optional[str] = None
    FeatureConfig: Optional[CustomizationFeatureConfigTypeDef] = None

class TestingDataResultTypeDef(BaseModel):
    Input: Optional[TestingDataOutputTypeDef] = None
    Output: Optional[TestingDataOutputTypeDef] = None
    Validation: Optional[ValidationDataTypeDef] = None

class TrainingDataResultTypeDef(BaseModel):
    Input: Optional[TrainingDataOutputTypeDef] = None
    Output: Optional[TrainingDataOutputTypeDef] = None
    Validation: Optional[ValidationDataTypeDef] = None

class DetectProtectiveEquipmentResponseTypeDef(BaseModel):
    ProtectiveEquipmentModelVersion: str
    Persons: List[ProtectiveEquipmentPersonTypeDef]
    Summary: ProtectiveEquipmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLabelDetectionResponseTypeDef(BaseModel):
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

class GetCelebrityRecognitionResponseTypeDef(BaseModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Celebrities: List[CelebrityRecognitionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetPersonTrackingResponseTypeDef(BaseModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Persons: List[PersonDetectionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetFaceSearchResponseTypeDef(BaseModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Persons: List[PersonMatchTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTextDetectionResponseTypeDef(BaseModel):
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

class ProjectVersionDescriptionTypeDef(BaseModel):
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

class DescribeProjectVersionsResponseTypeDef(BaseModel):
    ProjectVersionDescriptions: List[ProjectVersionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

