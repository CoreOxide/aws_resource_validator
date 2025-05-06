from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.rekognition.rekognition_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AgeRange(BaseValidatorModel):
    Low: Optional[int] = None
    High: Optional[int] = None


class AssociateFacesRequest(BaseValidatorModel):
    CollectionId: str
    UserId: str
    FaceIds: List[str]
    UserMatchThreshold: Optional[float] = None
    ClientRequestToken: Optional[str] = None


class AssociatedFace(BaseValidatorModel):
    FaceId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnsuccessfulFaceAssociation(BaseValidatorModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Confidence: Optional[float] = None
    Reasons: Optional[List[UnsuccessfulFaceAssociationReasonType]] = None


class AudioMetadata(BaseValidatorModel):
    Codec: Optional[str] = None
    DurationMillis: Optional[int] = None
    SampleRate: Optional[int] = None
    NumberOfChannels: Optional[int] = None


class BoundingBox(BaseValidatorModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None


class S3Object(BaseValidatorModel):
    Bucket: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None


class Beard(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class BlackFrame(BaseValidatorModel):
    MaxPixelThreshold: Optional[float] = None
    MinCoveragePercentage: Optional[float] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class KnownGender(BaseValidatorModel):
    Type: Optional[KnownGenderTypeType] = None


class Emotion(BaseValidatorModel):
    Type: Optional[EmotionNameType] = None
    Confidence: Optional[float] = None


class ImageQuality(BaseValidatorModel):
    Brightness: Optional[float] = None
    Sharpness: Optional[float] = None


class Landmark(BaseValidatorModel):
    Type: Optional[LandmarkTypeType] = None
    X: Optional[float] = None
    Y: Optional[float] = None


class Pose(BaseValidatorModel):
    Roll: Optional[float] = None
    Yaw: Optional[float] = None
    Pitch: Optional[float] = None


class Smile(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class ConnectedHomeSettingsForUpdate(BaseValidatorModel):
    Labels: Optional[List[str]] = None
    MinConfidence: Optional[float] = None


class ConnectedHomeSettingsOutput(BaseValidatorModel):
    Labels: List[str]
    MinConfidence: Optional[float] = None


class ConnectedHomeSettings(BaseValidatorModel):
    Labels: List[str]
    MinConfidence: Optional[float] = None


class ContentType(BaseValidatorModel):
    Confidence: Optional[float] = None
    Name: Optional[str] = None


class ModerationLabel(BaseValidatorModel):
    Confidence: Optional[float] = None
    Name: Optional[str] = None
    ParentName: Optional[str] = None
    TaxonomyLevel: Optional[int] = None


class OutputConfig(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3KeyPrefix: Optional[str] = None


class CoversBodyPart(BaseValidatorModel):
    Confidence: Optional[float] = None
    Value: Optional[bool] = None


class CreateCollectionRequest(BaseValidatorModel):
    CollectionId: str
    Tags: Optional[Dict[str, str]] = None


class LivenessOutputConfig(BaseValidatorModel):
    S3Bucket: str
    S3KeyPrefix: Optional[str] = None


class CreateProjectRequest(BaseValidatorModel):
    ProjectName: str
    Feature: Optional[CustomizationFeatureType] = None
    AutoUpdate: Optional[ProjectAutoUpdateType] = None
    Tags: Optional[Dict[str, str]] = None


class StreamProcessorDataSharingPreference(BaseValidatorModel):
    OptIn: bool


class StreamProcessorNotificationChannel(BaseValidatorModel):
    SNSTopicArn: str


class CreateUserRequest(BaseValidatorModel):
    CollectionId: str
    UserId: str
    ClientRequestToken: Optional[str] = None


class CustomizationFeatureContentModerationConfig(BaseValidatorModel):
    ConfidenceThreshold: Optional[float] = None


class DatasetStats(BaseValidatorModel):
    LabeledEntries: Optional[int] = None
    TotalEntries: Optional[int] = None
    TotalLabels: Optional[int] = None
    ErrorEntries: Optional[int] = None


class DatasetLabelStats(BaseValidatorModel):
    EntryCount: Optional[int] = None
    BoundingBoxCount: Optional[int] = None


class DatasetMetadata(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    DatasetType: Optional[DatasetTypeType] = None
    DatasetArn: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    StatusMessageCode: Optional[DatasetStatusMessageCodeType] = None


class DeleteCollectionRequest(BaseValidatorModel):
    CollectionId: str


class DeleteDatasetRequest(BaseValidatorModel):
    DatasetArn: str


class DeleteFacesRequest(BaseValidatorModel):
    CollectionId: str
    FaceIds: List[str]


class UnsuccessfulFaceDeletion(BaseValidatorModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Reasons: Optional[List[UnsuccessfulFaceDeletionReasonType]] = None


class DeleteProjectPolicyRequest(BaseValidatorModel):
    ProjectArn: str
    PolicyName: str
    PolicyRevisionId: Optional[str] = None


class DeleteProjectRequest(BaseValidatorModel):
    ProjectArn: str


class DeleteProjectVersionRequest(BaseValidatorModel):
    ProjectVersionArn: str


class DeleteStreamProcessorRequest(BaseValidatorModel):
    Name: str


class DeleteUserRequest(BaseValidatorModel):
    CollectionId: str
    UserId: str
    ClientRequestToken: Optional[str] = None


class DescribeCollectionRequest(BaseValidatorModel):
    CollectionId: str


class DescribeDatasetRequest(BaseValidatorModel):
    DatasetArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeProjectVersionsRequest(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeProjectsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProjectNames: Optional[List[str]] = None
    Features: Optional[List[CustomizationFeatureType]] = None


class DescribeStreamProcessorRequest(BaseValidatorModel):
    Name: str


class DetectLabelsImageQuality(BaseValidatorModel):
    Brightness: Optional[float] = None
    Sharpness: Optional[float] = None
    Contrast: Optional[float] = None


class DominantColor(BaseValidatorModel):
    Red: Optional[int] = None
    Blue: Optional[int] = None
    Green: Optional[int] = None
    HexCode: Optional[str] = None
    CSSColor: Optional[str] = None
    SimplifiedColor: Optional[str] = None
    PixelPercent: Optional[float] = None


class DetectLabelsImagePropertiesSettings(BaseValidatorModel):
    MaxDominantColors: Optional[int] = None


class GeneralLabelsSettings(BaseValidatorModel):
    LabelInclusionFilters: Optional[List[str]] = None
    LabelExclusionFilters: Optional[List[str]] = None
    LabelCategoryInclusionFilters: Optional[List[str]] = None
    LabelCategoryExclusionFilters: Optional[List[str]] = None


class HumanLoopActivationOutput(BaseValidatorModel):
    HumanLoopArn: Optional[str] = None
    HumanLoopActivationReasons: Optional[List[str]] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[str] = None


class ProtectiveEquipmentSummarizationAttributes(BaseValidatorModel):
    MinConfidence: float
    RequiredEquipmentTypes: List[ProtectiveEquipmentTypeType]


class ProtectiveEquipmentSummary(BaseValidatorModel):
    PersonsWithRequiredEquipment: Optional[List[int]] = None
    PersonsWithoutRequiredEquipment: Optional[List[int]] = None
    PersonsIndeterminate: Optional[List[int]] = None


class DetectionFilter(BaseValidatorModel):
    MinConfidence: Optional[float] = None
    MinBoundingBoxHeight: Optional[float] = None
    MinBoundingBoxWidth: Optional[float] = None


class DisassociateFacesRequest(BaseValidatorModel):
    CollectionId: str
    UserId: str
    FaceIds: List[str]
    ClientRequestToken: Optional[str] = None


class DisassociatedFace(BaseValidatorModel):
    FaceId: Optional[str] = None


class UnsuccessfulFaceDisassociation(BaseValidatorModel):
    FaceId: Optional[str] = None
    UserId: Optional[str] = None
    Reasons: Optional[List[UnsuccessfulFaceDisassociationReasonType]] = None


class DistributeDataset(BaseValidatorModel):
    Arn: str


class EyeDirection(BaseValidatorModel):
    Yaw: Optional[float] = None
    Pitch: Optional[float] = None
    Confidence: Optional[float] = None


class EyeOpen(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class Eyeglasses(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class FaceOccluded(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class Gender(BaseValidatorModel):
    Value: Optional[GenderTypeType] = None
    Confidence: Optional[float] = None


class MouthOpen(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class Mustache(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class Sunglasses(BaseValidatorModel):
    Value: Optional[bool] = None
    Confidence: Optional[float] = None


class FaceSearchSettings(BaseValidatorModel):
    CollectionId: Optional[str] = None
    FaceMatchThreshold: Optional[float] = None


class Point(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None


class GetCelebrityInfoRequest(BaseValidatorModel):
    Id: str


class GetCelebrityRecognitionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[CelebrityRecognitionSortByType] = None


class VideoMetadata(BaseValidatorModel):
    Codec: Optional[str] = None
    DurationMillis: Optional[int] = None
    Format: Optional[str] = None
    FrameRate: Optional[float] = None
    FrameHeight: Optional[int] = None
    FrameWidth: Optional[int] = None
    ColorRange: Optional[VideoColorRangeType] = None


class GetContentModerationRequestMetadata(BaseValidatorModel):
    SortBy: Optional[ContentModerationSortByType] = None
    AggregateBy: Optional[ContentModerationAggregateByType] = None


class GetContentModerationRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[ContentModerationSortByType] = None
    AggregateBy: Optional[ContentModerationAggregateByType] = None


class GetFaceDetectionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetFaceLivenessSessionResultsRequest(BaseValidatorModel):
    SessionId: str


class GetFaceSearchRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[FaceSearchSortByType] = None


class GetLabelDetectionRequestMetadata(BaseValidatorModel):
    SortBy: Optional[LabelDetectionSortByType] = None
    AggregateBy: Optional[LabelDetectionAggregateByType] = None


class GetLabelDetectionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[LabelDetectionSortByType] = None
    AggregateBy: Optional[LabelDetectionAggregateByType] = None


class GetMediaAnalysisJobRequest(BaseValidatorModel):
    JobId: str


class MediaAnalysisJobFailureDetails(BaseValidatorModel):
    Code: Optional[MediaAnalysisJobFailureCodeType] = None
    Message: Optional[str] = None


class MediaAnalysisOutputConfig(BaseValidatorModel):
    S3Bucket: str
    S3KeyPrefix: Optional[str] = None


class GetPersonTrackingRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[PersonTrackingSortByType] = None


class GetSegmentDetectionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SegmentTypeInfo(BaseValidatorModel):
    Type: Optional[SegmentTypeType] = None
    ModelVersion: Optional[str] = None


class GetTextDetectionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class HumanLoopDataAttributes(BaseValidatorModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None


class KinesisDataStream(BaseValidatorModel):
    Arn: Optional[str] = None


class KinesisVideoStreamStartSelector(BaseValidatorModel):
    ProducerTimestamp: Optional[int] = None
    FragmentNumber: Optional[str] = None


class KinesisVideoStream(BaseValidatorModel):
    Arn: Optional[str] = None


class LabelAlias(BaseValidatorModel):
    Name: Optional[str] = None


class LabelCategory(BaseValidatorModel):
    Name: Optional[str] = None


class Parent(BaseValidatorModel):
    Name: Optional[str] = None


class ListCollectionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatasetEntriesRequest(BaseValidatorModel):
    DatasetArn: str
    ContainsLabels: Optional[List[str]] = None
    Labeled: Optional[bool] = None
    SourceRefContains: Optional[str] = None
    HasErrors: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatasetLabelsRequest(BaseValidatorModel):
    DatasetArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFacesRequest(BaseValidatorModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    UserId: Optional[str] = None
    FaceIds: Optional[List[str]] = None


class ListMediaAnalysisJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProjectPoliciesRequest(BaseValidatorModel):
    ProjectArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProjectPolicy(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    PolicyDocument: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class ListStreamProcessorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StreamProcessor(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[StreamProcessorStatusType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListUsersRequest(BaseValidatorModel):
    CollectionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class User(BaseValidatorModel):
    UserId: Optional[str] = None
    UserStatus: Optional[UserStatusType] = None


class MatchedUser(BaseValidatorModel):
    UserId: Optional[str] = None
    UserStatus: Optional[UserStatusType] = None


class MediaAnalysisDetectModerationLabelsConfig(BaseValidatorModel):
    MinConfidence: Optional[float] = None
    ProjectVersion: Optional[str] = None


class MediaAnalysisModelVersions(BaseValidatorModel):
    Moderation: Optional[str] = None


class NotificationChannel(BaseValidatorModel):
    SNSTopicArn: str
    RoleArn: str


class PutProjectPolicyRequest(BaseValidatorModel):
    ProjectArn: str
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None


class S3Destination(BaseValidatorModel):
    Bucket: Optional[str] = None
    KeyPrefix: Optional[str] = None


class SearchFacesRequest(BaseValidatorModel):
    CollectionId: str
    FaceId: str
    MaxFaces: Optional[int] = None
    FaceMatchThreshold: Optional[float] = None


class SearchUsersRequest(BaseValidatorModel):
    CollectionId: str
    UserId: Optional[str] = None
    FaceId: Optional[str] = None
    UserMatchThreshold: Optional[float] = None
    MaxUsers: Optional[int] = None


class SearchedFace(BaseValidatorModel):
    FaceId: Optional[str] = None


class SearchedUser(BaseValidatorModel):
    UserId: Optional[str] = None


class ShotSegment(BaseValidatorModel):
    Index: Optional[int] = None
    Confidence: Optional[float] = None


class TechnicalCueSegment(BaseValidatorModel):
    Type: Optional[TechnicalCueTypeType] = None
    Confidence: Optional[float] = None


class StartProjectVersionRequest(BaseValidatorModel):
    ProjectVersionArn: str
    MinInferenceUnits: int
    MaxInferenceUnits: Optional[int] = None


class StartShotDetectionFilter(BaseValidatorModel):
    MinSegmentConfidence: Optional[float] = None


class StreamProcessingStopSelector(BaseValidatorModel):
    MaxDurationInSeconds: Optional[int] = None


class StopProjectVersionRequest(BaseValidatorModel):
    ProjectVersionArn: str


class StopStreamProcessorRequest(BaseValidatorModel):
    Name: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class CopyProjectVersionResponse(BaseValidatorModel):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadata


class CreateCollectionResponse(BaseValidatorModel):
    StatusCode: int
    CollectionArn: str
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadata


class CreateFaceLivenessSessionResponse(BaseValidatorModel):
    SessionId: str
    ResponseMetadata: ResponseMetadata


class CreateProjectResponse(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadata


class CreateProjectVersionResponse(BaseValidatorModel):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadata


class CreateStreamProcessorResponse(BaseValidatorModel):
    StreamProcessorArn: str
    ResponseMetadata: ResponseMetadata


class DeleteCollectionResponse(BaseValidatorModel):
    StatusCode: int
    ResponseMetadata: ResponseMetadata


class DeleteProjectResponse(BaseValidatorModel):
    Status: ProjectStatusType
    ResponseMetadata: ResponseMetadata


class DeleteProjectVersionResponse(BaseValidatorModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadata


class DescribeCollectionResponse(BaseValidatorModel):
    FaceCount: int
    FaceModelVersion: str
    CollectionARN: str
    CreationTimestamp: datetime
    UserCount: int
    ResponseMetadata: ResponseMetadata


class ListCollectionsResponse(BaseValidatorModel):
    CollectionIds: List[str]
    FaceModelVersions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDatasetEntriesResponse(BaseValidatorModel):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutProjectPolicyResponse(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


class StartCelebrityRecognitionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartContentModerationResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartFaceDetectionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartFaceSearchResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartLabelDetectionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartMediaAnalysisJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartPersonTrackingResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartProjectVersionResponse(BaseValidatorModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadata


class StartSegmentDetectionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartStreamProcessorResponse(BaseValidatorModel):
    SessionId: str
    ResponseMetadata: ResponseMetadata


class StartTextDetectionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StopProjectVersionResponse(BaseValidatorModel):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadata


class AssociateFacesResponse(BaseValidatorModel):
    AssociatedFaces: List[AssociatedFace]
    UnsuccessfulFaceAssociations: List[UnsuccessfulFaceAssociation]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadata


class ComparedSourceImageFace(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Confidence: Optional[float] = None


class Face(BaseValidatorModel):
    FaceId: Optional[str] = None
    BoundingBox: Optional[BoundingBox] = None
    ImageId: Optional[str] = None
    ExternalImageId: Optional[str] = None
    Confidence: Optional[float] = None
    IndexFacesModelVersion: Optional[str] = None
    UserId: Optional[str] = None


class AuditImage(BaseValidatorModel):
    Bytes: Optional[bytes] = None
    S3Object: Optional[S3Object] = None
    BoundingBox: Optional[BoundingBox] = None


class GroundTruthManifest(BaseValidatorModel):
    S3Object: Optional[S3Object] = None


class MediaAnalysisInput(BaseValidatorModel):
    S3Object: S3Object


class MediaAnalysisManifestSummary(BaseValidatorModel):
    S3Object: Optional[S3Object] = None


class Summary(BaseValidatorModel):
    S3Object: Optional[S3Object] = None


class Video(BaseValidatorModel):
    S3Object: Optional[S3Object] = None


class StartTechnicalCueDetectionFilter(BaseValidatorModel):
    MinSegmentConfidence: Optional[float] = None
    BlackFrame: Optional[BlackFrame] = None


class DatasetChanges(BaseValidatorModel):
    GroundTruth: Blob


class Image(BaseValidatorModel):
    Bytes: Optional[Blob] = None
    S3Object: Optional[S3Object] = None


class GetCelebrityInfoResponse(BaseValidatorModel):
    Urls: List[str]
    Name: str
    KnownGender: KnownGender
    ResponseMetadata: ResponseMetadata


class ComparedFace(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Confidence: Optional[float] = None
    Landmarks: Optional[List[Landmark]] = None
    Pose: Optional[Pose] = None
    Quality: Optional[ImageQuality] = None
    Emotions: Optional[List[Emotion]] = None
    Smile: Optional[Smile] = None


class StreamProcessorSettingsForUpdate(BaseValidatorModel):
    ConnectedHomeForUpdate: Optional[ConnectedHomeSettingsForUpdate] = None


class ContentModerationDetection(BaseValidatorModel):
    Timestamp: Optional[int] = None
    ModerationLabel: Optional[ModerationLabel] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None
    ContentTypes: Optional[List[ContentType]] = None


class CopyProjectVersionRequest(BaseValidatorModel):
    SourceProjectArn: str
    SourceProjectVersionArn: str
    DestinationProjectArn: str
    VersionName: str
    OutputConfig: OutputConfig
    Tags: Optional[Dict[str, str]] = None
    KmsKeyId: Optional[str] = None


class EquipmentDetection(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Confidence: Optional[float] = None
    Type: Optional[ProtectiveEquipmentTypeType] = None
    CoversBodyPart: Optional[CoversBodyPart] = None


class CreateFaceLivenessSessionRequestSettings(BaseValidatorModel):
    OutputConfig: Optional[LivenessOutputConfig] = None
    AuditImagesLimit: Optional[int] = None


class CustomizationFeatureConfig(BaseValidatorModel):
    ContentModeration: Optional[CustomizationFeatureContentModerationConfig] = None


class DatasetDescription(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    StatusMessageCode: Optional[DatasetStatusMessageCodeType] = None
    DatasetStats: Optional[DatasetStats] = None


class DatasetLabelDescription(BaseValidatorModel):
    LabelName: Optional[str] = None
    LabelStats: Optional[DatasetLabelStats] = None


class ProjectDescription(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Status: Optional[ProjectStatusType] = None
    Datasets: Optional[List[DatasetMetadata]] = None
    Feature: Optional[CustomizationFeatureType] = None
    AutoUpdate: Optional[ProjectAutoUpdateType] = None


class DeleteFacesResponse(BaseValidatorModel):
    DeletedFaces: List[str]
    UnsuccessfulFaceDeletions: List[UnsuccessfulFaceDeletion]
    ResponseMetadata: ResponseMetadata


class DescribeProjectVersionsRequestPaginate(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeProjectsRequestPaginate(BaseValidatorModel):
    ProjectNames: Optional[List[str]] = None
    Features: Optional[List[CustomizationFeatureType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollectionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetEntriesRequestPaginate(BaseValidatorModel):
    DatasetArn: str
    ContainsLabels: Optional[List[str]] = None
    Labeled: Optional[bool] = None
    SourceRefContains: Optional[str] = None
    HasErrors: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetLabelsRequestPaginate(BaseValidatorModel):
    DatasetArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFacesRequestPaginate(BaseValidatorModel):
    CollectionId: str
    UserId: Optional[str] = None
    FaceIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectPoliciesRequestPaginate(BaseValidatorModel):
    ProjectArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamProcessorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeProjectVersionsRequestWaitExtra(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeProjectVersionsRequestWait(BaseValidatorModel):
    ProjectArn: str
    VersionNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DetectLabelsImageBackground(BaseValidatorModel):
    Quality: Optional[DetectLabelsImageQuality] = None
    DominantColors: Optional[List[DominantColor]] = None


class DetectLabelsImageForeground(BaseValidatorModel):
    Quality: Optional[DetectLabelsImageQuality] = None
    DominantColors: Optional[List[DominantColor]] = None


class Instance(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Confidence: Optional[float] = None
    DominantColors: Optional[List[DominantColor]] = None


class DetectLabelsSettings(BaseValidatorModel):
    GeneralLabels: Optional[GeneralLabelsSettings] = None
    ImageProperties: Optional[DetectLabelsImagePropertiesSettings] = None


class LabelDetectionSettings(BaseValidatorModel):
    GeneralLabels: Optional[GeneralLabelsSettings] = None


class DetectModerationLabelsResponse(BaseValidatorModel):
    ModerationLabels: List[ModerationLabel]
    ModerationModelVersion: str
    HumanLoopActivationOutput: HumanLoopActivationOutput
    ProjectVersion: str
    ContentTypes: List[ContentType]
    ResponseMetadata: ResponseMetadata


class DisassociateFacesResponse(BaseValidatorModel):
    DisassociatedFaces: List[DisassociatedFace]
    UnsuccessfulFaceDisassociations: List[UnsuccessfulFaceDisassociation]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadata


class DistributeDatasetEntriesRequest(BaseValidatorModel):
    Datasets: List[DistributeDataset]


class FaceDetail(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    AgeRange: Optional[AgeRange] = None
    Smile: Optional[Smile] = None
    Eyeglasses: Optional[Eyeglasses] = None
    Sunglasses: Optional[Sunglasses] = None
    Gender: Optional[Gender] = None
    Beard: Optional[Beard] = None
    Mustache: Optional[Mustache] = None
    EyesOpen: Optional[EyeOpen] = None
    MouthOpen: Optional[MouthOpen] = None
    Emotions: Optional[List[Emotion]] = None
    Landmarks: Optional[List[Landmark]] = None
    Pose: Optional[Pose] = None
    Quality: Optional[ImageQuality] = None
    Confidence: Optional[float] = None
    FaceOccluded: Optional[FaceOccluded] = None
    EyeDirection: Optional[EyeDirection] = None


class StreamProcessorSettingsOutput(BaseValidatorModel):
    FaceSearch: Optional[FaceSearchSettings] = None
    ConnectedHome: Optional[ConnectedHomeSettingsOutput] = None


class StreamProcessorSettings(BaseValidatorModel):
    FaceSearch: Optional[FaceSearchSettings] = None
    ConnectedHome: Optional[ConnectedHomeSettings] = None


class Geometry(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class RegionOfInterestOutput(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class RegionOfInterest(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class HumanLoopConfig(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributes] = None


class StreamProcessingStartSelector(BaseValidatorModel):
    KVSStreamStartSelector: Optional[KinesisVideoStreamStartSelector] = None


class StreamProcessorInput(BaseValidatorModel):
    KinesisVideoStream: Optional[KinesisVideoStream] = None


class ListProjectPoliciesResponse(BaseValidatorModel):
    ProjectPolicies: List[ProjectPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStreamProcessorsResponse(BaseValidatorModel):
    StreamProcessors: List[StreamProcessor]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UserMatch(BaseValidatorModel):
    Similarity: Optional[float] = None
    User: Optional[MatchedUser] = None


class MediaAnalysisOperationsConfig(BaseValidatorModel):
    DetectModerationLabels: Optional[MediaAnalysisDetectModerationLabelsConfig] = None


class MediaAnalysisResults(BaseValidatorModel):
    S3Object: Optional[S3Object] = None
    ModelVersions: Optional[MediaAnalysisModelVersions] = None


class StreamProcessorOutput(BaseValidatorModel):
    KinesisDataStream: Optional[KinesisDataStream] = None
    S3Destination: Optional[S3Destination] = None


class SegmentDetection(BaseValidatorModel):
    Type: Optional[SegmentTypeType] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None
    StartTimecodeSMPTE: Optional[str] = None
    EndTimecodeSMPTE: Optional[str] = None
    DurationSMPTE: Optional[str] = None
    TechnicalCueSegment: Optional[TechnicalCueSegment] = None
    ShotSegment: Optional[ShotSegment] = None
    StartFrameNumber: Optional[int] = None
    EndFrameNumber: Optional[int] = None
    DurationFrames: Optional[int] = None


class FaceMatch(BaseValidatorModel):
    Similarity: Optional[float] = None
    Face: Optional[Face] = None


class ListFacesResponse(BaseValidatorModel):
    Faces: List[Face]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetFaceLivenessSessionResultsResponse(BaseValidatorModel):
    SessionId: str
    Status: LivenessSessionStatusType
    Confidence: float
    ReferenceImage: AuditImage
    AuditImages: List[AuditImage]
    ResponseMetadata: ResponseMetadata


class Asset(BaseValidatorModel):
    GroundTruthManifest: Optional[GroundTruthManifest] = None


class DatasetSource(BaseValidatorModel):
    GroundTruthManifest: Optional[GroundTruthManifest] = None
    DatasetArn: Optional[str] = None


class EvaluationResult(BaseValidatorModel):
    F1Score: Optional[float] = None
    Summary: Optional[Summary] = None


class StartCelebrityRecognitionRequest(BaseValidatorModel):
    Video: Video
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None


class StartContentModerationRequest(BaseValidatorModel):
    Video: Video
    MinConfidence: Optional[float] = None
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None


class StartFaceDetectionRequest(BaseValidatorModel):
    Video: Video
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    FaceAttributes: Optional[FaceAttributesType] = None
    JobTag: Optional[str] = None


class StartFaceSearchRequest(BaseValidatorModel):
    Video: Video
    CollectionId: str
    ClientRequestToken: Optional[str] = None
    FaceMatchThreshold: Optional[float] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None


class StartPersonTrackingRequest(BaseValidatorModel):
    Video: Video
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None


class StartSegmentDetectionFilters(BaseValidatorModel):
    TechnicalCueFilter: Optional[StartTechnicalCueDetectionFilter] = None
    ShotFilter: Optional[StartShotDetectionFilter] = None


class UpdateDatasetEntriesRequest(BaseValidatorModel):
    DatasetArn: str
    Changes: DatasetChanges


class CompareFacesRequest(BaseValidatorModel):
    SourceImage: Image
    TargetImage: Image
    SimilarityThreshold: Optional[float] = None
    QualityFilter: Optional[QualityFilterType] = None


class DetectCustomLabelsRequest(BaseValidatorModel):
    ProjectVersionArn: str
    Image: Image
    MaxResults: Optional[int] = None
    MinConfidence: Optional[float] = None


class DetectFacesRequest(BaseValidatorModel):
    Image: Image
    Attributes: Optional[List[AttributeType]] = None


class DetectProtectiveEquipmentRequest(BaseValidatorModel):
    Image: Image
    SummarizationAttributes: Optional[ProtectiveEquipmentSummarizationAttributes] = None


class IndexFacesRequest(BaseValidatorModel):
    CollectionId: str
    Image: Image
    ExternalImageId: Optional[str] = None
    DetectionAttributes: Optional[List[AttributeType]] = None
    MaxFaces: Optional[int] = None
    QualityFilter: Optional[QualityFilterType] = None


class RecognizeCelebritiesRequest(BaseValidatorModel):
    Image: Image


class SearchFacesByImageRequest(BaseValidatorModel):
    CollectionId: str
    Image: Image
    MaxFaces: Optional[int] = None
    FaceMatchThreshold: Optional[float] = None
    QualityFilter: Optional[QualityFilterType] = None


class SearchUsersByImageRequest(BaseValidatorModel):
    CollectionId: str
    Image: Image
    UserMatchThreshold: Optional[float] = None
    MaxUsers: Optional[int] = None
    QualityFilter: Optional[QualityFilterType] = None


class Celebrity(BaseValidatorModel):
    Urls: Optional[List[str]] = None
    Name: Optional[str] = None
    Id: Optional[str] = None
    Face: Optional[ComparedFace] = None
    MatchConfidence: Optional[float] = None
    KnownGender: Optional[KnownGender] = None


class CompareFacesMatch(BaseValidatorModel):
    Similarity: Optional[float] = None
    Face: Optional[ComparedFace] = None


class GetContentModerationResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    ModerationLabels: List[ContentModerationDetection]
    ModerationModelVersion: str
    JobId: str
    Video: Video
    JobTag: str
    GetRequestMetadata: GetContentModerationRequestMetadata
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ProtectiveEquipmentBodyPart(BaseValidatorModel):
    Name: Optional[BodyPartType] = None
    Confidence: Optional[float] = None
    EquipmentDetections: Optional[List[EquipmentDetection]] = None


class CreateFaceLivenessSessionRequest(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    Settings: Optional[CreateFaceLivenessSessionRequestSettings] = None
    ClientRequestToken: Optional[str] = None


class DescribeDatasetResponse(BaseValidatorModel):
    DatasetDescription: DatasetDescription
    ResponseMetadata: ResponseMetadata


class ListDatasetLabelsResponse(BaseValidatorModel):
    DatasetLabelDescriptions: List[DatasetLabelDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeProjectsResponse(BaseValidatorModel):
    ProjectDescriptions: List[ProjectDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DetectLabelsImageProperties(BaseValidatorModel):
    Quality: Optional[DetectLabelsImageQuality] = None
    DominantColors: Optional[List[DominantColor]] = None
    Foreground: Optional[DetectLabelsImageForeground] = None
    Background: Optional[DetectLabelsImageBackground] = None


class Label(BaseValidatorModel):
    Name: Optional[str] = None
    Confidence: Optional[float] = None
    Instances: Optional[List[Instance]] = None
    Parents: Optional[List[Parent]] = None
    Aliases: Optional[List[LabelAlias]] = None
    Categories: Optional[List[LabelCategory]] = None


class DetectLabelsRequest(BaseValidatorModel):
    Image: Image
    MaxLabels: Optional[int] = None
    MinConfidence: Optional[float] = None
    Features: Optional[List[DetectLabelsFeatureNameType]] = None
    Settings: Optional[DetectLabelsSettings] = None


class StartLabelDetectionRequest(BaseValidatorModel):
    Video: Video
    ClientRequestToken: Optional[str] = None
    MinConfidence: Optional[float] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None
    Features: Optional[List[Literal['GENERAL_LABELS']]] = None
    Settings: Optional[LabelDetectionSettings] = None


class CelebrityDetail(BaseValidatorModel):
    Urls: Optional[List[str]] = None
    Name: Optional[str] = None
    Id: Optional[str] = None
    Confidence: Optional[float] = None
    BoundingBox: Optional[BoundingBox] = None
    Face: Optional[FaceDetail] = None
    KnownGender: Optional[KnownGender] = None


class DetectFacesResponse(BaseValidatorModel):
    FaceDetails: List[FaceDetail]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadata


class FaceDetection(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Face: Optional[FaceDetail] = None


class FaceRecord(BaseValidatorModel):
    Face: Optional[Face] = None
    FaceDetail: Optional[FaceDetail] = None


class PersonDetail(BaseValidatorModel):
    Index: Optional[int] = None
    BoundingBox: Optional[BoundingBox] = None
    Face: Optional[FaceDetail] = None


class SearchedFaceDetails(BaseValidatorModel):
    FaceDetail: Optional[FaceDetail] = None


class UnindexedFace(BaseValidatorModel):
    Reasons: Optional[List[ReasonType]] = None
    FaceDetail: Optional[FaceDetail] = None


class UnsearchedFace(BaseValidatorModel):
    FaceDetails: Optional[FaceDetail] = None
    Reasons: Optional[List[UnsearchedFaceReasonType]] = None

StreamProcessorSettingsUnion = Union[StreamProcessorSettings, StreamProcessorSettingsOutput]


class CustomLabel(BaseValidatorModel):
    Name: Optional[str] = None
    Confidence: Optional[float] = None
    Geometry: Optional[Geometry] = None


class TextDetection(BaseValidatorModel):
    DetectedText: Optional[str] = None
    Type: Optional[TextTypesType] = None
    Id: Optional[int] = None
    ParentId: Optional[int] = None
    Confidence: Optional[float] = None
    Geometry: Optional[Geometry] = None

RegionOfInterestUnion = Union[RegionOfInterest, RegionOfInterestOutput]


class DetectModerationLabelsRequest(BaseValidatorModel):
    Image: Image
    MinConfidence: Optional[float] = None
    HumanLoopConfig: Optional[HumanLoopConfig] = None
    ProjectVersion: Optional[str] = None


class StartStreamProcessorRequest(BaseValidatorModel):
    Name: str
    StartSelector: Optional[StreamProcessingStartSelector] = None
    StopSelector: Optional[StreamProcessingStopSelector] = None


class SearchUsersResponse(BaseValidatorModel):
    UserMatches: List[UserMatch]
    FaceModelVersion: str
    SearchedFace: SearchedFace
    SearchedUser: SearchedUser
    ResponseMetadata: ResponseMetadata


class StartMediaAnalysisJobRequest(BaseValidatorModel):
    OperationsConfig: MediaAnalysisOperationsConfig
    Input: MediaAnalysisInput
    OutputConfig: MediaAnalysisOutputConfig
    ClientRequestToken: Optional[str] = None
    JobName: Optional[str] = None
    KmsKeyId: Optional[str] = None


class GetMediaAnalysisJobResponse(BaseValidatorModel):
    JobId: str
    JobName: str
    OperationsConfig: MediaAnalysisOperationsConfig
    Status: MediaAnalysisJobStatusType
    FailureDetails: MediaAnalysisJobFailureDetails
    CreationTimestamp: datetime
    CompletionTimestamp: datetime
    Input: MediaAnalysisInput
    OutputConfig: MediaAnalysisOutputConfig
    KmsKeyId: str
    Results: MediaAnalysisResults
    ManifestSummary: MediaAnalysisManifestSummary
    ResponseMetadata: ResponseMetadata


class MediaAnalysisJobDescription(BaseValidatorModel):
    JobId: str
    OperationsConfig: MediaAnalysisOperationsConfig
    Status: MediaAnalysisJobStatusType
    CreationTimestamp: datetime
    Input: MediaAnalysisInput
    OutputConfig: MediaAnalysisOutputConfig
    JobName: Optional[str] = None
    FailureDetails: Optional[MediaAnalysisJobFailureDetails] = None
    CompletionTimestamp: Optional[datetime] = None
    KmsKeyId: Optional[str] = None
    Results: Optional[MediaAnalysisResults] = None
    ManifestSummary: Optional[MediaAnalysisManifestSummary] = None


class DescribeStreamProcessorResponse(BaseValidatorModel):
    Name: str
    StreamProcessorArn: str
    Status: StreamProcessorStatusType
    StatusMessage: str
    CreationTimestamp: datetime
    LastUpdateTimestamp: datetime
    Input: StreamProcessorInput
    Output: StreamProcessorOutput
    RoleArn: str
    Settings: StreamProcessorSettingsOutput
    NotificationChannel: StreamProcessorNotificationChannel
    KmsKeyId: str
    RegionsOfInterest: List[RegionOfInterestOutput]
    DataSharingPreference: StreamProcessorDataSharingPreference
    ResponseMetadata: ResponseMetadata


class GetSegmentDetectionResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: List[VideoMetadata]
    AudioMetadata: List[AudioMetadata]
    Segments: List[SegmentDetection]
    SelectedSegmentTypes: List[SegmentTypeInfo]
    JobId: str
    Video: Video
    JobTag: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchFacesByImageResponse(BaseValidatorModel):
    SearchedFaceBoundingBox: BoundingBox
    SearchedFaceConfidence: float
    FaceMatches: List[FaceMatch]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadata


class SearchFacesResponse(BaseValidatorModel):
    SearchedFaceId: str
    FaceMatches: List[FaceMatch]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadata


class TestingDataOutput(BaseValidatorModel):
    Assets: Optional[List[Asset]] = None
    AutoCreate: Optional[bool] = None


class TestingData(BaseValidatorModel):
    Assets: Optional[List[Asset]] = None
    AutoCreate: Optional[bool] = None


class TrainingDataOutput(BaseValidatorModel):
    Assets: Optional[List[Asset]] = None


class TrainingData(BaseValidatorModel):
    Assets: Optional[List[Asset]] = None


class ValidationData(BaseValidatorModel):
    Assets: Optional[List[Asset]] = None


class CreateDatasetRequest(BaseValidatorModel):
    DatasetType: DatasetTypeType
    ProjectArn: str
    DatasetSource: Optional[DatasetSource] = None
    Tags: Optional[Dict[str, str]] = None


class StartSegmentDetectionRequest(BaseValidatorModel):
    Video: Video
    SegmentTypes: List[SegmentTypeType]
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None
    Filters: Optional[StartSegmentDetectionFilters] = None


class RecognizeCelebritiesResponse(BaseValidatorModel):
    CelebrityFaces: List[Celebrity]
    UnrecognizedFaces: List[ComparedFace]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadata


class CompareFacesResponse(BaseValidatorModel):
    SourceImageFace: ComparedSourceImageFace
    FaceMatches: List[CompareFacesMatch]
    UnmatchedFaces: List[ComparedFace]
    SourceImageOrientationCorrection: OrientationCorrectionType
    TargetImageOrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadata


class ProtectiveEquipmentPerson(BaseValidatorModel):
    BodyParts: Optional[List[ProtectiveEquipmentBodyPart]] = None
    BoundingBox: Optional[BoundingBox] = None
    Confidence: Optional[float] = None
    Id: Optional[int] = None


class DetectLabelsResponse(BaseValidatorModel):
    Labels: List[Label]
    OrientationCorrection: OrientationCorrectionType
    LabelModelVersion: str
    ImageProperties: DetectLabelsImageProperties
    ResponseMetadata: ResponseMetadata


class LabelDetection(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Label: Optional[Label] = None
    StartTimestampMillis: Optional[int] = None
    EndTimestampMillis: Optional[int] = None
    DurationMillis: Optional[int] = None


class CelebrityRecognition(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Celebrity: Optional[CelebrityDetail] = None


class GetFaceDetectionResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    Faces: List[FaceDetection]
    JobId: str
    Video: Video
    JobTag: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PersonDetection(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Person: Optional[PersonDetail] = None


class PersonMatch(BaseValidatorModel):
    Timestamp: Optional[int] = None
    Person: Optional[PersonDetail] = None
    FaceMatches: Optional[List[FaceMatch]] = None


class IndexFacesResponse(BaseValidatorModel):
    FaceRecords: List[FaceRecord]
    OrientationCorrection: OrientationCorrectionType
    FaceModelVersion: str
    UnindexedFaces: List[UnindexedFace]
    ResponseMetadata: ResponseMetadata


class SearchUsersByImageResponse(BaseValidatorModel):
    UserMatches: List[UserMatch]
    FaceModelVersion: str
    SearchedFace: SearchedFaceDetails
    UnsearchedFaces: List[UnsearchedFace]
    ResponseMetadata: ResponseMetadata


class DetectCustomLabelsResponse(BaseValidatorModel):
    CustomLabels: List[CustomLabel]
    ResponseMetadata: ResponseMetadata


class DetectTextResponse(BaseValidatorModel):
    TextDetections: List[TextDetection]
    TextModelVersion: str
    ResponseMetadata: ResponseMetadata


class TextDetectionResult(BaseValidatorModel):
    Timestamp: Optional[int] = None
    TextDetection: Optional[TextDetection] = None


class CreateStreamProcessorRequest(BaseValidatorModel):
    Input: StreamProcessorInput
    Output: StreamProcessorOutput
    Name: str
    Settings: StreamProcessorSettingsUnion
    RoleArn: str
    Tags: Optional[Dict[str, str]] = None
    NotificationChannel: Optional[StreamProcessorNotificationChannel] = None
    KmsKeyId: Optional[str] = None
    RegionsOfInterest: Optional[List[RegionOfInterestUnion]] = None
    DataSharingPreference: Optional[StreamProcessorDataSharingPreference] = None


class DetectTextFilters(BaseValidatorModel):
    WordFilter: Optional[DetectionFilter] = None
    RegionsOfInterest: Optional[List[RegionOfInterestUnion]] = None


class StartTextDetectionFilters(BaseValidatorModel):
    WordFilter: Optional[DetectionFilter] = None
    RegionsOfInterest: Optional[List[RegionOfInterestUnion]] = None


class UpdateStreamProcessorRequest(BaseValidatorModel):
    Name: str
    SettingsForUpdate: Optional[StreamProcessorSettingsForUpdate] = None
    RegionsOfInterestForUpdate: Optional[List[RegionOfInterestUnion]] = None
    DataSharingPreferenceForUpdate: Optional[StreamProcessorDataSharingPreference] = None
    ParametersToDelete: Optional[List[StreamProcessorParameterToDeleteType]] = None


class ListMediaAnalysisJobsResponse(BaseValidatorModel):
    MediaAnalysisJobs: List[MediaAnalysisJobDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

TestingDataUnion = Union[TestingData, TestingDataOutput]

TrainingDataUnion = Union[TrainingData, TrainingDataOutput]


class TestingDataResult(BaseValidatorModel):
    Input: Optional[TestingDataOutput] = None
    Output: Optional[TestingDataOutput] = None
    Validation: Optional[ValidationData] = None


class TrainingDataResult(BaseValidatorModel):
    Input: Optional[TrainingDataOutput] = None
    Output: Optional[TrainingDataOutput] = None
    Validation: Optional[ValidationData] = None


class DetectProtectiveEquipmentResponse(BaseValidatorModel):
    ProtectiveEquipmentModelVersion: str
    Persons: List[ProtectiveEquipmentPerson]
    Summary: ProtectiveEquipmentSummary
    ResponseMetadata: ResponseMetadata


class GetLabelDetectionResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    Labels: List[LabelDetection]
    LabelModelVersion: str
    JobId: str
    Video: Video
    JobTag: str
    GetRequestMetadata: GetLabelDetectionRequestMetadata
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCelebrityRecognitionResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    Celebrities: List[CelebrityRecognition]
    JobId: str
    Video: Video
    JobTag: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetPersonTrackingResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    Persons: List[PersonDetection]
    JobId: str
    Video: Video
    JobTag: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetFaceSearchResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    Persons: List[PersonMatch]
    JobId: str
    Video: Video
    JobTag: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetTextDetectionResponse(BaseValidatorModel):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadata
    TextDetections: List[TextDetectionResult]
    TextModelVersion: str
    JobId: str
    Video: Video
    JobTag: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DetectTextRequest(BaseValidatorModel):
    Image: Image
    Filters: Optional[DetectTextFilters] = None


class StartTextDetectionRequest(BaseValidatorModel):
    Video: Video
    ClientRequestToken: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    JobTag: Optional[str] = None
    Filters: Optional[StartTextDetectionFilters] = None


class CreateProjectVersionRequest(BaseValidatorModel):
    ProjectArn: str
    VersionName: str
    OutputConfig: OutputConfig
    TrainingData: Optional[TrainingDataUnion] = None
    TestingData: Optional[TestingDataUnion] = None
    Tags: Optional[Dict[str, str]] = None
    KmsKeyId: Optional[str] = None
    VersionDescription: Optional[str] = None
    FeatureConfig: Optional[CustomizationFeatureConfig] = None


class ProjectVersionDescription(BaseValidatorModel):
    ProjectVersionArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    MinInferenceUnits: Optional[int] = None
    Status: Optional[ProjectVersionStatusType] = None
    StatusMessage: Optional[str] = None
    BillableTrainingTimeInSeconds: Optional[int] = None
    TrainingEndTimestamp: Optional[datetime] = None
    OutputConfig: Optional[OutputConfig] = None
    TrainingDataResult: Optional[TrainingDataResult] = None
    TestingDataResult: Optional[TestingDataResult] = None
    EvaluationResult: Optional[EvaluationResult] = None
    ManifestSummary: Optional[GroundTruthManifest] = None
    KmsKeyId: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None
    SourceProjectVersionArn: Optional[str] = None
    VersionDescription: Optional[str] = None
    Feature: Optional[CustomizationFeatureType] = None
    BaseModelVersion: Optional[str] = None
    FeatureConfig: Optional[CustomizationFeatureConfig] = None


class DescribeProjectVersionsResponse(BaseValidatorModel):
    ProjectVersionDescriptions: List[ProjectVersionDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None