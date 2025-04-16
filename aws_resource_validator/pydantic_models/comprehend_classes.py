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
from aws_resource_validator.pydantic_models.comprehend_constants import *

class AugmentedManifestsListItemOutput(BaseValidatorModel):
    S3Uri: str
    AttributeNames: List[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None


class AugmentedManifestsListItem(BaseValidatorModel):
    S3Uri: str
    AttributeNames: Sequence[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None


class DominantLanguage(BaseValidatorModel):
    LanguageCode: Optional[str] = None
    Score: Optional[float] = None


class BatchDetectDominantLanguageRequest(BaseValidatorModel):
    TextList: Sequence[str]


class BatchItemError(BaseValidatorModel):
    Index: Optional[int] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDetectEntitiesRequest(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class BatchDetectKeyPhrasesRequest(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class SentimentScore(BaseValidatorModel):
    Positive: Optional[float] = None
    Negative: Optional[float] = None
    Neutral: Optional[float] = None
    Mixed: Optional[float] = None


class BatchDetectSentimentRequest(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class BatchDetectSyntaxRequest(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: SyntaxLanguageCodeType


class BatchDetectTargetedSentimentRequest(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class ChildBlock(BaseValidatorModel):
    ChildBlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


class BoundingBox(BaseValidatorModel):
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None
    Width: Optional[float] = None


class ClassifierEvaluationMetrics(BaseValidatorModel):
    Accuracy: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None
    MicroPrecision: Optional[float] = None
    MicroRecall: Optional[float] = None
    MicroF1Score: Optional[float] = None
    HammingLoss: Optional[float] = None


class DocumentClass(BaseValidatorModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None


class DocumentLabel(BaseValidatorModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None


class ErrorsListItem(BaseValidatorModel):
    Page: Optional[int] = None
    ErrorCode: Optional[PageBasedErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class WarningsListItem(BaseValidatorModel):
    Page: Optional[int] = None
    WarnCode: Optional[PageBasedWarningCodeType] = None
    WarnMessage: Optional[str] = None


class EntityLabel(BaseValidatorModel):
    Name: Optional[PiiEntityTypeType] = None
    Score: Optional[float] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class DocumentClassifierOutputDataConfig(BaseValidatorModel):
    S3Uri: Optional[str] = None
    KmsKeyId: Optional[str] = None
    FlywheelStatsS3Prefix: Optional[str] = None


class VpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class VpcConfig(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]


class DatasetAugmentedManifestsListItem(BaseValidatorModel):
    AttributeNames: Sequence[str]
    S3Uri: str
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None


class DatasetDocumentClassifierInputDataConfig(BaseValidatorModel):
    S3Uri: str
    LabelDelimiter: Optional[str] = None


class DatasetEntityRecognizerAnnotations(BaseValidatorModel):
    S3Uri: str


class DatasetEntityRecognizerDocuments(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None


class DatasetEntityRecognizerEntityList(BaseValidatorModel):
    S3Uri: str


class DatasetProperties(BaseValidatorModel):
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetType: Optional[DatasetTypeType] = None
    DatasetS3Uri: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    Message: Optional[str] = None
    NumberOfDocuments: Optional[int] = None
    CreationTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class DeleteDocumentClassifierRequest(BaseValidatorModel):
    DocumentClassifierArn: str


class DeleteEndpointRequest(BaseValidatorModel):
    EndpointArn: str


class DeleteEntityRecognizerRequest(BaseValidatorModel):
    EntityRecognizerArn: str


class DeleteFlywheelRequest(BaseValidatorModel):
    FlywheelArn: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    PolicyRevisionId: Optional[str] = None


class DescribeDatasetRequest(BaseValidatorModel):
    DatasetArn: str


class DescribeDocumentClassificationJobRequest(BaseValidatorModel):
    JobId: str


class DescribeDocumentClassifierRequest(BaseValidatorModel):
    DocumentClassifierArn: str


class DescribeDominantLanguageDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeEndpointRequest(BaseValidatorModel):
    EndpointArn: str


class EndpointProperties(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    Status: Optional[EndpointStatusType] = None
    Message: Optional[str] = None
    ModelArn: Optional[str] = None
    DesiredModelArn: Optional[str] = None
    DesiredInferenceUnits: Optional[int] = None
    CurrentInferenceUnits: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    DesiredDataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class DescribeEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeEntityRecognizerRequest(BaseValidatorModel):
    EntityRecognizerArn: str


class DescribeEventsDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeFlywheelIterationRequest(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str


class DescribeFlywheelRequest(BaseValidatorModel):
    FlywheelArn: str


class DescribeKeyPhrasesDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribePiiEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DescribeSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeTargetedSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeTopicsDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DocumentClassificationConfigOutput(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[List[str]] = None


class DocumentClassificationConfig(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[Sequence[str]] = None


class OutputDataConfig(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class DocumentClassifierDocuments(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None


class DocumentReaderConfigOutput(BaseValidatorModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[List[DocumentReadFeatureTypesType]] = None


class DocumentReaderConfig(BaseValidatorModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[Sequence[DocumentReadFeatureTypesType]] = None


class DocumentClassifierSummary(BaseValidatorModel):
    DocumentClassifierName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None


class ExtractedCharactersListItem(BaseValidatorModel):
    Page: Optional[int] = None
    Count: Optional[int] = None


class EntityRecognizerAnnotations(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None


class EntityRecognizerDocuments(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None


class EntityRecognizerEntityList(BaseValidatorModel):
    S3Uri: str


class EntityRecognizerEvaluationMetrics(BaseValidatorModel):
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None


class EntityTypesEvaluationMetrics(BaseValidatorModel):
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None


class EntityRecognizerOutputDataConfig(BaseValidatorModel):
    FlywheelStatsS3Prefix: Optional[str] = None


class EntityRecognizerSummary(BaseValidatorModel):
    RecognizerName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None


class FlywheelModelEvaluationMetrics(BaseValidatorModel):
    AverageF1Score: Optional[float] = None
    AveragePrecision: Optional[float] = None
    AverageRecall: Optional[float] = None
    AverageAccuracy: Optional[float] = None


class FlywheelSummary(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    ActiveModelArn: Optional[str] = None
    DataLakeS3Uri: Optional[str] = None
    Status: Optional[FlywheelStatusType] = None
    ModelType: Optional[ModelTypeType] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LatestFlywheelIteration: Optional[str] = None


class Point(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDocumentClassifierSummariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntityRecognizerSummariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PartOfSpeechTag(BaseValidatorModel):
    Tag: Optional[PartOfSpeechTagTypeType] = None
    Score: Optional[float] = None


class PiiOutputDataConfig(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class RedactionConfigOutput(BaseValidatorModel):
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    PolicyRevisionId: Optional[str] = None


class RedactionConfig(BaseValidatorModel):
    PiiEntityTypes: Optional[Sequence[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None


class StartFlywheelIterationRequest(BaseValidatorModel):
    FlywheelArn: str
    ClientRequestToken: Optional[str] = None


class StopDominantLanguageDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopEventsDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopKeyPhrasesDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopPiiEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopTargetedSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopTrainingDocumentClassifierRequest(BaseValidatorModel):
    DocumentClassifierArn: str


class StopTrainingEntityRecognizerRequest(BaseValidatorModel):
    EntityRecognizerArn: str


class ToxicContent(BaseValidatorModel):
    Name: Optional[ToxicContentTypeType] = None
    Score: Optional[float] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateEndpointRequest(BaseValidatorModel):
    EndpointArn: str
    DesiredModelArn: Optional[str] = None
    DesiredInferenceUnits: Optional[int] = None
    DesiredDataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class BatchDetectDominantLanguageItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Languages: Optional[List[DominantLanguage]] = None


class CreateDatasetResponse(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadata


class CreateDocumentClassifierResponse(BaseValidatorModel):
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadata


class CreateEndpointResponse(BaseValidatorModel):
    EndpointArn: str
    ModelArn: str
    ResponseMetadata: ResponseMetadata


class CreateEntityRecognizerResponse(BaseValidatorModel):
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadata


class CreateFlywheelResponse(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: str
    ResponseMetadata: ResponseMetadata


class DescribeResourcePolicyResponse(BaseValidatorModel):
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


class DetectDominantLanguageResponse(BaseValidatorModel):
    Languages: List[DominantLanguage]
    ResponseMetadata: ResponseMetadata


class ImportModelResponse(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


class StartDocumentClassificationJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadata


class StartDominantLanguageDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadata


class StartEventsDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartFlywheelIterationResponse(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str
    ResponseMetadata: ResponseMetadata


class StartKeyPhrasesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartPiiEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartTargetedSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartTopicsDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopDominantLanguageDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopEventsDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopKeyPhrasesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopPiiEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopTargetedSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class UpdateEndpointResponse(BaseValidatorModel):
    DesiredModelArn: str
    ResponseMetadata: ResponseMetadata


class KeyPhrase(BaseValidatorModel):
    pass


class BatchDetectKeyPhrasesItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    KeyPhrases: Optional[List[KeyPhrase]] = None


class DetectKeyPhrasesResponse(BaseValidatorModel):
    KeyPhrases: List[KeyPhrase]
    ResponseMetadata: ResponseMetadata


class BatchDetectSentimentItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScore] = None


class DetectSentimentResponse(BaseValidatorModel):
    Sentiment: SentimentTypeType
    SentimentScore: SentimentScore
    ResponseMetadata: ResponseMetadata


class MentionSentiment(BaseValidatorModel):
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScore] = None


class BlockReference(BaseValidatorModel):
    BlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    ChildBlocks: Optional[List[ChildBlock]] = None


class ClassifierMetadata(BaseValidatorModel):
    NumberOfLabels: Optional[int] = None
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[ClassifierEvaluationMetrics] = None


class ContainsPiiEntitiesResponse(BaseValidatorModel):
    Labels: List[EntityLabel]
    ResponseMetadata: ResponseMetadata


class CreateEndpointRequest(BaseValidatorModel):
    EndpointName: str
    DesiredInferenceUnits: int
    ModelArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    DataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class ImportModelRequest(BaseValidatorModel):
    SourceModelArn: str
    ModelName: Optional[str] = None
    VersionName: Optional[str] = None
    ModelKmsKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class DataSecurityConfigOutput(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    DataLakeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class DataSecurityConfig(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    DataLakeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfig] = None


class DatasetEntityRecognizerInputDataConfig(BaseValidatorModel):
    Documents: DatasetEntityRecognizerDocuments
    Annotations: Optional[DatasetEntityRecognizerAnnotations] = None
    EntityList: Optional[DatasetEntityRecognizerEntityList] = None


class Timestamp(BaseValidatorModel):
    pass


class DatasetFilter(BaseValidatorModel):
    Status: Optional[DatasetStatusType] = None
    DatasetType: Optional[DatasetTypeType] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None


class DocumentClassificationJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class DocumentClassifierFilter(BaseValidatorModel):
    Status: Optional[ModelStatusType] = None
    DocumentClassifierName: Optional[str] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class DominantLanguageDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class EndpointFilter(BaseValidatorModel):
    ModelArn: Optional[str] = None
    Status: Optional[EndpointStatusType] = None
    CreationTimeBefore: Optional[Timestamp] = None
    CreationTimeAfter: Optional[Timestamp] = None


class EntitiesDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class EntityRecognizerFilter(BaseValidatorModel):
    Status: Optional[ModelStatusType] = None
    RecognizerName: Optional[str] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class EventsDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class FlywheelFilter(BaseValidatorModel):
    Status: Optional[FlywheelStatusType] = None
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None


class FlywheelIterationFilter(BaseValidatorModel):
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None


class KeyPhrasesDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class PiiEntitiesDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class SentimentDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class TargetedSentimentDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class TopicsDetectionJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class DescribeDatasetResponse(BaseValidatorModel):
    DatasetProperties: DatasetProperties
    ResponseMetadata: ResponseMetadata


class ListDatasetsResponse(BaseValidatorModel):
    DatasetPropertiesList: List[DatasetProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEndpointResponse(BaseValidatorModel):
    EndpointProperties: EndpointProperties
    ResponseMetadata: ResponseMetadata


class ListEndpointsResponse(BaseValidatorModel):
    EndpointPropertiesList: List[EndpointProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PiiEntity(BaseValidatorModel):
    pass


class DetectPiiEntitiesResponse(BaseValidatorModel):
    Entities: List[PiiEntity]
    ResponseMetadata: ResponseMetadata


class TextSegment(BaseValidatorModel):
    pass


class DetectToxicContentRequest(BaseValidatorModel):
    TextSegments: Sequence[TextSegment]
    LanguageCode: LanguageCodeType


class DocumentClassifierInputDataConfigOutput(BaseValidatorModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemOutput]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocuments] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigOutput] = None


class InputDataConfigOutput(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigOutput] = None


class DocumentClassifierInputDataConfig(BaseValidatorModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItem]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocuments] = None
    DocumentReaderConfig: Optional[DocumentReaderConfig] = None


class InputDataConfig(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfig] = None


class ListDocumentClassifierSummariesResponse(BaseValidatorModel):
    DocumentClassifierSummariesList: List[DocumentClassifierSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DocumentMetadata(BaseValidatorModel):
    Pages: Optional[int] = None
    ExtractedCharacters: Optional[List[ExtractedCharactersListItem]] = None


class EntityTypesListItem(BaseValidatorModel):
    pass


class EntityRecognitionConfigOutput(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItem]


class EntityRecognitionConfig(BaseValidatorModel):
    EntityTypes: Sequence[EntityTypesListItem]


class EntityRecognizerInputDataConfigOutput(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItem]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocuments] = None
    Annotations: Optional[EntityRecognizerAnnotations] = None
    EntityList: Optional[EntityRecognizerEntityList] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemOutput]] = None


class EntityRecognizerInputDataConfig(BaseValidatorModel):
    EntityTypes: Sequence[EntityTypesListItem]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocuments] = None
    Annotations: Optional[EntityRecognizerAnnotations] = None
    EntityList: Optional[EntityRecognizerEntityList] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItem]] = None


class ListEntityRecognizerSummariesResponse(BaseValidatorModel):
    EntityRecognizerSummariesList: List[EntityRecognizerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FlywheelIterationProperties(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    FlywheelIterationId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[FlywheelIterationStatusType] = None
    Message: Optional[str] = None
    EvaluatedModelArn: Optional[str] = None
    EvaluatedModelMetrics: Optional[FlywheelModelEvaluationMetrics] = None
    TrainedModelArn: Optional[str] = None
    TrainedModelMetrics: Optional[FlywheelModelEvaluationMetrics] = None
    EvaluationManifestS3Prefix: Optional[str] = None


class ListFlywheelsResponse(BaseValidatorModel):
    FlywheelSummaryList: List[FlywheelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Geometry(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class ToxicLabels(BaseValidatorModel):
    Labels: Optional[List[ToxicContent]] = None
    Toxicity: Optional[float] = None


class BatchDetectDominantLanguageResponse(BaseValidatorModel):
    ResultList: List[BatchDetectDominantLanguageItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class BatchDetectKeyPhrasesResponse(BaseValidatorModel):
    ResultList: List[BatchDetectKeyPhrasesItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class BatchDetectSentimentResponse(BaseValidatorModel):
    ResultList: List[BatchDetectSentimentItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class VpcConfigUnion(BaseValidatorModel):
    pass


class UpdateDataSecurityConfig(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None


class DatasetInputDataConfig(BaseValidatorModel):
    AugmentedManifests: Optional[Sequence[DatasetAugmentedManifestsListItem]] = None
    DataFormat: Optional[DatasetDataFormatType] = None
    DocumentClassifierInputDataConfig: Optional[DatasetDocumentClassifierInputDataConfig] = None
    EntityRecognizerInputDataConfig: Optional[DatasetEntityRecognizerInputDataConfig] = None


class ListDatasetsRequest(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    Filter: Optional[DatasetFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentClassificationJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDocumentClassificationJobsRequest(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentClassifiersRequestPaginate(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDocumentClassifiersRequest(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDominantLanguageDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDominantLanguageDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEndpointsRequestPaginate(BaseValidatorModel):
    Filter: Optional[EndpointFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEndpointsRequest(BaseValidatorModel):
    Filter: Optional[EndpointFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntitiesDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEntitiesDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntityRecognizersRequestPaginate(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEntityRecognizersRequest(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventsDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[EventsDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFlywheelsRequest(BaseValidatorModel):
    Filter: Optional[FlywheelFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFlywheelIterationHistoryRequest(BaseValidatorModel):
    FlywheelArn: str
    Filter: Optional[FlywheelIterationFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListKeyPhrasesDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeyPhrasesDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPiiEntitiesDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPiiEntitiesDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSentimentDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSentimentDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTargetedSentimentDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[TargetedSentimentDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTopicsDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTopicsDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DocumentClassifierProperties(BaseValidatorModel):
    DocumentClassifierArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[DocumentClassifierInputDataConfigOutput] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfig] = None
    ClassifierMetadata: Optional[ClassifierMetadata] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class DocumentClassificationJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    DocumentClassifierArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    FlywheelArn: Optional[str] = None


class DominantLanguageDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class EntitiesDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    EntityRecognizerArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    FlywheelArn: Optional[str] = None


class EventsDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    TargetEventTypes: Optional[List[str]] = None


class KeyPhrasesDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class PiiEntitiesDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[PiiOutputDataConfig] = None
    RedactionConfig: Optional[RedactionConfigOutput] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    Mode: Optional[PiiEntitiesDetectionModeType] = None


class SentimentDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class TargetedSentimentDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class TopicsDetectionJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutput] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    NumberOfTopics: Optional[int] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None


class DocumentTypeListItem(BaseValidatorModel):
    pass


class ClassifyDocumentResponse(BaseValidatorModel):
    Classes: List[DocumentClass]
    Labels: List[DocumentLabel]
    DocumentMetadata: DocumentMetadata
    DocumentType: List[DocumentTypeListItem]
    Errors: List[ErrorsListItem]
    Warnings: List[WarningsListItem]
    ResponseMetadata: ResponseMetadata


class TaskConfigOutput(BaseValidatorModel):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: Optional[DocumentClassificationConfigOutput] = None
    EntityRecognitionConfig: Optional[EntityRecognitionConfigOutput] = None


class TaskConfig(BaseValidatorModel):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: Optional[DocumentClassificationConfig] = None
    EntityRecognitionConfig: Optional[EntityRecognitionConfig] = None


class EntityRecognizerMetadataEntityTypesListItem(BaseValidatorModel):
    pass


class EntityRecognizerMetadata(BaseValidatorModel):
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[EntityRecognizerEvaluationMetrics] = None
    EntityTypes: Optional[List[EntityRecognizerMetadataEntityTypesListItem]] = None


class DescribeFlywheelIterationResponse(BaseValidatorModel):
    FlywheelIterationProperties: FlywheelIterationProperties
    ResponseMetadata: ResponseMetadata


class ListFlywheelIterationHistoryResponse(BaseValidatorModel):
    FlywheelIterationPropertiesList: List[FlywheelIterationProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SyntaxToken(BaseValidatorModel):
    pass


class BatchDetectSyntaxItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    SyntaxTokens: Optional[List[SyntaxToken]] = None


class DetectSyntaxResponse(BaseValidatorModel):
    SyntaxTokens: List[SyntaxToken]
    ResponseMetadata: ResponseMetadata


class DetectToxicContentResponse(BaseValidatorModel):
    ResultList: List[ToxicLabels]
    ResponseMetadata: ResponseMetadata


class TargetedSentimentMention(BaseValidatorModel):
    pass


class TargetedSentimentEntity(BaseValidatorModel):
    DescriptiveMentionIndex: Optional[List[int]] = None
    Mentions: Optional[List[TargetedSentimentMention]] = None


class Entity(BaseValidatorModel):
    pass


class BatchDetectEntitiesItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[Entity]] = None


class UpdateFlywheelRequest(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    DataSecurityConfig: Optional[UpdateDataSecurityConfig] = None


class CreateDatasetRequest(BaseValidatorModel):
    FlywheelArn: str
    DatasetName: str
    InputDataConfig: DatasetInputDataConfig
    DatasetType: Optional[DatasetTypeType] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class DescribeDocumentClassifierResponse(BaseValidatorModel):
    DocumentClassifierProperties: DocumentClassifierProperties
    ResponseMetadata: ResponseMetadata


class ListDocumentClassifiersResponse(BaseValidatorModel):
    DocumentClassifierPropertiesList: List[DocumentClassifierProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeDocumentClassificationJobResponse(BaseValidatorModel):
    DocumentClassificationJobProperties: DocumentClassificationJobProperties
    ResponseMetadata: ResponseMetadata


class ListDocumentClassificationJobsResponse(BaseValidatorModel):
    DocumentClassificationJobPropertiesList: List[DocumentClassificationJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeDominantLanguageDetectionJobResponse(BaseValidatorModel):
    DominantLanguageDetectionJobProperties: DominantLanguageDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListDominantLanguageDetectionJobsResponse(BaseValidatorModel):
    DominantLanguageDetectionJobPropertiesList: List[DominantLanguageDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEntitiesDetectionJobResponse(BaseValidatorModel):
    EntitiesDetectionJobProperties: EntitiesDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListEntitiesDetectionJobsResponse(BaseValidatorModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEventsDetectionJobResponse(BaseValidatorModel):
    EventsDetectionJobProperties: EventsDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListEventsDetectionJobsResponse(BaseValidatorModel):
    EventsDetectionJobPropertiesList: List[EventsDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeKeyPhrasesDetectionJobResponse(BaseValidatorModel):
    KeyPhrasesDetectionJobProperties: KeyPhrasesDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListKeyPhrasesDetectionJobsResponse(BaseValidatorModel):
    KeyPhrasesDetectionJobPropertiesList: List[KeyPhrasesDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePiiEntitiesDetectionJobResponse(BaseValidatorModel):
    PiiEntitiesDetectionJobProperties: PiiEntitiesDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListPiiEntitiesDetectionJobsResponse(BaseValidatorModel):
    PiiEntitiesDetectionJobPropertiesList: List[PiiEntitiesDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSentimentDetectionJobResponse(BaseValidatorModel):
    SentimentDetectionJobProperties: SentimentDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListSentimentDetectionJobsResponse(BaseValidatorModel):
    SentimentDetectionJobPropertiesList: List[SentimentDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeTargetedSentimentDetectionJobResponse(BaseValidatorModel):
    TargetedSentimentDetectionJobProperties: TargetedSentimentDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListTargetedSentimentDetectionJobsResponse(BaseValidatorModel):
    TargetedSentimentDetectionJobPropertiesList: List[ TargetedSentimentDetectionJobProperties ]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeTopicsDetectionJobResponse(BaseValidatorModel):
    TopicsDetectionJobProperties: TopicsDetectionJobProperties
    ResponseMetadata: ResponseMetadata


class ListTopicsDetectionJobsResponse(BaseValidatorModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DocumentClassifierInputDataConfigUnion(BaseValidatorModel):
    pass


class CreateDocumentClassifierRequest(BaseValidatorModel):
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: DocumentClassifierInputDataConfigUnion
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfig] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None


class InputDataConfigUnion(BaseValidatorModel):
    pass


class StartDocumentClassificationJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    DocumentClassifierArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None
    FlywheelArn: Optional[str] = None


class StartDominantLanguageDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class StartEntitiesDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    EntityRecognizerArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None
    FlywheelArn: Optional[str] = None


class StartEventsDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    TargetEventTypes: Sequence[str]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class StartKeyPhrasesDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class RedactionConfigUnion(BaseValidatorModel):
    pass


class StartPiiEntitiesDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    Mode: PiiEntitiesDetectionModeType
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    RedactionConfig: Optional[RedactionConfigUnion] = None
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class StartSentimentDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class StartTargetedSentimentDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class StartTopicsDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    NumberOfTopics: Optional[int] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class FlywheelProperties(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigOutput] = None
    DataLakeS3Uri: Optional[str] = None
    DataSecurityConfig: Optional[DataSecurityConfigOutput] = None
    Status: Optional[FlywheelStatusType] = None
    ModelType: Optional[ModelTypeType] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LatestFlywheelIteration: Optional[str] = None


class EntityRecognizerInputDataConfigUnion(BaseValidatorModel):
    pass


class CreateEntityRecognizerRequest(BaseValidatorModel):
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: EntityRecognizerInputDataConfigUnion
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None


class EntityRecognizerProperties(BaseValidatorModel):
    EntityRecognizerArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[EntityRecognizerInputDataConfigOutput] = None
    RecognizerMetadata: Optional[EntityRecognizerMetadata] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None
    OutputDataConfig: Optional[EntityRecognizerOutputDataConfig] = None


class Block(BaseValidatorModel):
    pass


class DetectEntitiesResponse(BaseValidatorModel):
    Entities: List[Entity]
    DocumentMetadata: DocumentMetadata
    DocumentType: List[DocumentTypeListItem]
    Blocks: List[Block]
    Errors: List[ErrorsListItem]
    ResponseMetadata: ResponseMetadata


class BatchDetectSyntaxResponse(BaseValidatorModel):
    ResultList: List[BatchDetectSyntaxItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class BatchDetectTargetedSentimentItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[TargetedSentimentEntity]] = None


class DetectTargetedSentimentResponse(BaseValidatorModel):
    Entities: List[TargetedSentimentEntity]
    ResponseMetadata: ResponseMetadata


class BatchDetectEntitiesResponse(BaseValidatorModel):
    ResultList: List[BatchDetectEntitiesItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class DescribeFlywheelResponse(BaseValidatorModel):
    FlywheelProperties: FlywheelProperties
    ResponseMetadata: ResponseMetadata


class UpdateFlywheelResponse(BaseValidatorModel):
    FlywheelProperties: FlywheelProperties
    ResponseMetadata: ResponseMetadata


class DataSecurityConfigUnion(BaseValidatorModel):
    pass


class TaskConfigUnion(BaseValidatorModel):
    pass


class CreateFlywheelRequest(BaseValidatorModel):
    FlywheelName: str
    DataAccessRoleArn: str
    DataLakeS3Uri: str
    ActiveModelArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigUnion] = None
    ModelType: Optional[ModelTypeType] = None
    DataSecurityConfig: Optional[DataSecurityConfigUnion] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class DescribeEntityRecognizerResponse(BaseValidatorModel):
    EntityRecognizerProperties: EntityRecognizerProperties
    ResponseMetadata: ResponseMetadata


class ListEntityRecognizersResponse(BaseValidatorModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchDetectTargetedSentimentResponse(BaseValidatorModel):
    ResultList: List[BatchDetectTargetedSentimentItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


