from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.comprehend.comprehend_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AugmentedManifestsListItemOutput(BaseValidatorModel):
    S3Uri: str
    AttributeNames: List[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None


class AugmentedManifestsListItem(BaseValidatorModel):
    S3Uri: str
    AttributeNames: List[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None


class DominantLanguage(BaseValidatorModel):
    LanguageCode: Optional[str] = None
    Score: Optional[float] = None


# This class is the input for the 'batch_detect_dominant_language' function.
class BatchDetectDominantLanguageRequest(BaseValidatorModel):
    TextList: List[str]


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


# This class is the input for the 'batch_detect_entities' function.
class BatchDetectEntitiesRequest(BaseValidatorModel):
    TextList: List[str]
    LanguageCode: LanguageCodeType


class KeyPhrase(BaseValidatorModel):
    Score: Optional[float] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


# This class is the input for the 'batch_detect_key_phrases' function.
class BatchDetectKeyPhrasesRequest(BaseValidatorModel):
    TextList: List[str]
    LanguageCode: LanguageCodeType


class SentimentScore(BaseValidatorModel):
    Positive: Optional[float] = None
    Negative: Optional[float] = None
    Neutral: Optional[float] = None
    Mixed: Optional[float] = None


# This class is the input for the 'batch_detect_sentiment' function.
class BatchDetectSentimentRequest(BaseValidatorModel):
    TextList: List[str]
    LanguageCode: LanguageCodeType


# This class is the input for the 'batch_detect_syntax' function.
class BatchDetectSyntaxRequest(BaseValidatorModel):
    TextList: List[str]
    LanguageCode: SyntaxLanguageCodeType


# This class is the input for the 'batch_detect_targeted_sentiment' function.
class BatchDetectTargetedSentimentRequest(BaseValidatorModel):
    TextList: List[str]
    LanguageCode: LanguageCodeType

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ChildBlock(BaseValidatorModel):
    ChildBlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


class RelationshipsListItem(BaseValidatorModel):
    Ids: Optional[List[str]] = None
    Type: Optional[Literal['CHILD']] = None


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


class DocumentTypeListItem(BaseValidatorModel):
    Page: Optional[int] = None
    Type: Optional[DocumentTypeType] = None


class ErrorsListItem(BaseValidatorModel):
    Page: Optional[int] = None
    ErrorCode: Optional[PageBasedErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class WarningsListItem(BaseValidatorModel):
    Page: Optional[int] = None
    WarnCode: Optional[PageBasedWarningCodeType] = None
    WarnMessage: Optional[str] = None


# This class is the input for the 'contains_pii_entities' function.
class ContainsPiiEntitiesRequest(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType


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
    SecurityGroupIds: List[str]
    Subnets: List[str]


class DatasetAugmentedManifestsListItem(BaseValidatorModel):
    AttributeNames: List[str]
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

Timestamp = Union[datetime, str]


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


# This class is the input for the 'describe_dataset' function.
class DescribeDatasetRequest(BaseValidatorModel):
    DatasetArn: str


# This class is the input for the 'describe_document_classification_job' function.
class DescribeDocumentClassificationJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_document_classifier' function.
class DescribeDocumentClassifierRequest(BaseValidatorModel):
    DocumentClassifierArn: str


# This class is the input for the 'describe_dominant_language_detection_job' function.
class DescribeDominantLanguageDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_endpoint' function.
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


# This class is the input for the 'describe_entities_detection_job' function.
class DescribeEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_entity_recognizer' function.
class DescribeEntityRecognizerRequest(BaseValidatorModel):
    EntityRecognizerArn: str


# This class is the input for the 'describe_events_detection_job' function.
class DescribeEventsDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_flywheel_iteration' function.
class DescribeFlywheelIterationRequest(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str


# This class is the input for the 'describe_flywheel' function.
class DescribeFlywheelRequest(BaseValidatorModel):
    FlywheelArn: str


# This class is the input for the 'describe_key_phrases_detection_job' function.
class DescribeKeyPhrasesDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_pii_entities_detection_job' function.
class DescribePiiEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_resource_policy' function.
class DescribeResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'describe_sentiment_detection_job' function.
class DescribeSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_targeted_sentiment_detection_job' function.
class DescribeTargetedSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_topics_detection_job' function.
class DescribeTopicsDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'detect_dominant_language' function.
class DetectDominantLanguageRequest(BaseValidatorModel):
    Text: str


# This class is the input for the 'detect_key_phrases' function.
class DetectKeyPhrasesRequest(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType


# This class is the input for the 'detect_pii_entities' function.
class DetectPiiEntitiesRequest(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType


class PiiEntity(BaseValidatorModel):
    Score: Optional[float] = None
    Type: Optional[PiiEntityTypeType] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


# This class is the input for the 'detect_sentiment' function.
class DetectSentimentRequest(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType


# This class is the input for the 'detect_syntax' function.
class DetectSyntaxRequest(BaseValidatorModel):
    Text: str
    LanguageCode: SyntaxLanguageCodeType


# This class is the input for the 'detect_targeted_sentiment' function.
class DetectTargetedSentimentRequest(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType


class TextSegment(BaseValidatorModel):
    Text: str


class DocumentClassificationConfigOutput(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[List[str]] = None


class DocumentClassificationConfig(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[List[str]] = None


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
    FeatureTypes: Optional[List[DocumentReadFeatureTypesType]] = None


class DocumentClassifierSummary(BaseValidatorModel):
    DocumentClassifierName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None


class ExtractedCharactersListItem(BaseValidatorModel):
    Page: Optional[int] = None
    Count: Optional[int] = None


class EntityTypesListItem(BaseValidatorModel):
    Type: str


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


# This class is the input for the 'list_document_classifier_summaries' function.
class ListDocumentClassifierSummariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_entity_recognizer_summaries' function.
class ListEntityRecognizerSummariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
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


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    PolicyRevisionId: Optional[str] = None


class RedactionConfig(BaseValidatorModel):
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None


# This class is the input for the 'start_flywheel_iteration' function.
class StartFlywheelIterationRequest(BaseValidatorModel):
    FlywheelArn: str
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'stop_dominant_language_detection_job' function.
class StopDominantLanguageDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_entities_detection_job' function.
class StopEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_events_detection_job' function.
class StopEventsDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_key_phrases_detection_job' function.
class StopKeyPhrasesDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_pii_entities_detection_job' function.
class StopPiiEntitiesDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_sentiment_detection_job' function.
class StopSentimentDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_targeted_sentiment_detection_job' function.
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
    TagKeys: List[str]


# This class is the input for the 'update_endpoint' function.
class UpdateEndpointRequest(BaseValidatorModel):
    EndpointArn: str
    DesiredModelArn: Optional[str] = None
    DesiredInferenceUnits: Optional[int] = None
    DesiredDataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class BatchDetectDominantLanguageItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Languages: Optional[List[DominantLanguage]] = None


# This class is the output for the 'create_dataset' function.
class CreateDatasetResponse(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_document_classifier' function.
class CreateDocumentClassifierResponse(BaseValidatorModel):
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_endpoint' function.
class CreateEndpointResponse(BaseValidatorModel):
    EndpointArn: str
    ModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_entity_recognizer' function.
class CreateEntityRecognizerResponse(BaseValidatorModel):
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_flywheel' function.
class CreateFlywheelResponse(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource_policy' function.
class DescribeResourcePolicyResponse(BaseValidatorModel):
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_dominant_language' function.
class DetectDominantLanguageResponse(BaseValidatorModel):
    Languages: List[DominantLanguage]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_model' function.
class ImportModelResponse(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_document_classification_job' function.
class StartDocumentClassificationJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_dominant_language_detection_job' function.
class StartDominantLanguageDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_entities_detection_job' function.
class StartEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_events_detection_job' function.
class StartEventsDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_flywheel_iteration' function.
class StartFlywheelIterationResponse(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_key_phrases_detection_job' function.
class StartKeyPhrasesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_pii_entities_detection_job' function.
class StartPiiEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_sentiment_detection_job' function.
class StartSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_targeted_sentiment_detection_job' function.
class StartTargetedSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_topics_detection_job' function.
class StartTopicsDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_dominant_language_detection_job' function.
class StopDominantLanguageDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_entities_detection_job' function.
class StopEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_events_detection_job' function.
class StopEventsDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_key_phrases_detection_job' function.
class StopKeyPhrasesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_pii_entities_detection_job' function.
class StopPiiEntitiesDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_sentiment_detection_job' function.
class StopSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_targeted_sentiment_detection_job' function.
class StopTargetedSentimentDetectionJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_endpoint' function.
class UpdateEndpointResponse(BaseValidatorModel):
    DesiredModelArn: str
    ResponseMetadata: ResponseMetadata


class BatchDetectKeyPhrasesItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    KeyPhrases: Optional[List[KeyPhrase]] = None


# This class is the output for the 'detect_key_phrases' function.
class DetectKeyPhrasesResponse(BaseValidatorModel):
    KeyPhrases: List[KeyPhrase]
    ResponseMetadata: ResponseMetadata


class BatchDetectSentimentItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScore] = None


# This class is the output for the 'detect_sentiment' function.
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


# This class is the output for the 'contains_pii_entities' function.
class ContainsPiiEntitiesResponse(BaseValidatorModel):
    Labels: List[EntityLabel]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_endpoint' function.
class CreateEndpointRequest(BaseValidatorModel):
    EndpointName: str
    DesiredInferenceUnits: int
    ModelArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


# This class is the input for the 'import_model' function.
class ImportModelRequest(BaseValidatorModel):
    SourceModelArn: str
    ModelName: Optional[str] = None
    VersionName: Optional[str] = None
    ModelKmsKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


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

VpcConfigUnion = Union[VpcConfig, VpcConfigOutput]


class DatasetEntityRecognizerInputDataConfig(BaseValidatorModel):
    Documents: DatasetEntityRecognizerDocuments
    Annotations: Optional[DatasetEntityRecognizerAnnotations] = None
    EntityList: Optional[DatasetEntityRecognizerEntityList] = None


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


# This class is the output for the 'describe_dataset' function.
class DescribeDatasetResponse(BaseValidatorModel):
    DatasetProperties: DatasetProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_datasets' function.
class ListDatasetsResponse(BaseValidatorModel):
    DatasetPropertiesList: List[DatasetProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_endpoint' function.
class DescribeEndpointResponse(BaseValidatorModel):
    EndpointProperties: EndpointProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_endpoints' function.
class ListEndpointsResponse(BaseValidatorModel):
    EndpointPropertiesList: List[EndpointProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'detect_pii_entities' function.
class DetectPiiEntitiesResponse(BaseValidatorModel):
    Entities: List[PiiEntity]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'detect_toxic_content' function.
class DetectToxicContentRequest(BaseValidatorModel):
    TextSegments: List[TextSegment]
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
    AugmentedManifests: Optional[List[AugmentedManifestsListItem]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocuments] = None
    DocumentReaderConfig: Optional[DocumentReaderConfig] = None

DocumentReaderConfigUnion = Union[DocumentReaderConfig, DocumentReaderConfigOutput]


class InputDataConfig(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfig] = None


# This class is the output for the 'list_document_classifier_summaries' function.
class ListDocumentClassifierSummariesResponse(BaseValidatorModel):
    DocumentClassifierSummariesList: List[DocumentClassifierSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DocumentMetadata(BaseValidatorModel):
    Pages: Optional[int] = None
    ExtractedCharacters: Optional[List[ExtractedCharactersListItem]] = None


class EntityRecognitionConfigOutput(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItem]


class EntityRecognitionConfig(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItem]


class EntityRecognizerInputDataConfigOutput(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItem]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocuments] = None
    Annotations: Optional[EntityRecognizerAnnotations] = None
    EntityList: Optional[EntityRecognizerEntityList] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemOutput]] = None


class EntityRecognizerInputDataConfig(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItem]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocuments] = None
    Annotations: Optional[EntityRecognizerAnnotations] = None
    EntityList: Optional[EntityRecognizerEntityList] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItem]] = None


class EntityRecognizerMetadataEntityTypesListItem(BaseValidatorModel):
    Type: Optional[str] = None
    EvaluationMetrics: Optional[EntityTypesEvaluationMetrics] = None
    NumberOfTrainMentions: Optional[int] = None


# This class is the output for the 'list_entity_recognizer_summaries' function.
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


# This class is the output for the 'list_flywheels' function.
class ListFlywheelsResponse(BaseValidatorModel):
    FlywheelSummaryList: List[FlywheelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Geometry(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class SyntaxToken(BaseValidatorModel):
    TokenId: Optional[int] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    PartOfSpeech: Optional[PartOfSpeechTag] = None

RedactionConfigUnion = Union[RedactionConfig, RedactionConfigOutput]


class ToxicLabels(BaseValidatorModel):
    Labels: Optional[List[ToxicContent]] = None
    Toxicity: Optional[float] = None


# This class is the output for the 'batch_detect_dominant_language' function.
class BatchDetectDominantLanguageResponse(BaseValidatorModel):
    ResultList: List[BatchDetectDominantLanguageItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_detect_key_phrases' function.
class BatchDetectKeyPhrasesResponse(BaseValidatorModel):
    ResultList: List[BatchDetectKeyPhrasesItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_detect_sentiment' function.
class BatchDetectSentimentResponse(BaseValidatorModel):
    ResultList: List[BatchDetectSentimentItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class TargetedSentimentMention(BaseValidatorModel):
    Score: Optional[float] = None
    GroupScore: Optional[float] = None
    Text: Optional[str] = None
    Type: Optional[TargetedSentimentEntityTypeType] = None
    MentionSentiment: Optional[MentionSentiment] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


class Entity(BaseValidatorModel):
    Score: Optional[float] = None
    Type: Optional[EntityTypeType] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    BlockReferences: Optional[List[BlockReference]] = None

DataSecurityConfigUnion = Union[DataSecurityConfig, DataSecurityConfigOutput]


class UpdateDataSecurityConfig(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None


class DatasetInputDataConfig(BaseValidatorModel):
    AugmentedManifests: Optional[List[DatasetAugmentedManifestsListItem]] = None
    DataFormat: Optional[DatasetDataFormatType] = None
    DocumentClassifierInputDataConfig: Optional[DatasetDocumentClassifierInputDataConfig] = None
    EntityRecognizerInputDataConfig: Optional[DatasetEntityRecognizerInputDataConfig] = None


# This class is the input for the 'list_datasets' function.
class ListDatasetsRequest(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    Filter: Optional[DatasetFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentClassificationJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_document_classification_jobs' function.
class ListDocumentClassificationJobsRequest(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentClassifiersRequestPaginate(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_document_classifiers' function.
class ListDocumentClassifiersRequest(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDominantLanguageDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_dominant_language_detection_jobs' function.
class ListDominantLanguageDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEndpointsRequestPaginate(BaseValidatorModel):
    Filter: Optional[EndpointFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_endpoints' function.
class ListEndpointsRequest(BaseValidatorModel):
    Filter: Optional[EndpointFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntitiesDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_entities_detection_jobs' function.
class ListEntitiesDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntityRecognizersRequestPaginate(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_entity_recognizers' function.
class ListEntityRecognizersRequest(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_events_detection_jobs' function.
class ListEventsDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[EventsDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_flywheels' function.
class ListFlywheelsRequest(BaseValidatorModel):
    Filter: Optional[FlywheelFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_flywheel_iteration_history' function.
class ListFlywheelIterationHistoryRequest(BaseValidatorModel):
    FlywheelArn: str
    Filter: Optional[FlywheelIterationFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListKeyPhrasesDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_key_phrases_detection_jobs' function.
class ListKeyPhrasesDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPiiEntitiesDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_pii_entities_detection_jobs' function.
class ListPiiEntitiesDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSentimentDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_sentiment_detection_jobs' function.
class ListSentimentDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_targeted_sentiment_detection_jobs' function.
class ListTargetedSentimentDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[TargetedSentimentDetectionJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTopicsDetectionJobsRequestPaginate(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_topics_detection_jobs' function.
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

DocumentClassifierInputDataConfigUnion = Union[DocumentClassifierInputDataConfig, DocumentClassifierInputDataConfigOutput]


# This class is the input for the 'classify_document' function.
class ClassifyDocumentRequest(BaseValidatorModel):
    EndpointArn: str
    Text: Optional[str] = None
    Bytes: Optional[Blob] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigUnion] = None


# This class is the input for the 'detect_entities' function.
class DetectEntitiesRequest(BaseValidatorModel):
    Text: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    EndpointArn: Optional[str] = None
    Bytes: Optional[Blob] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigUnion] = None

InputDataConfigUnion = Union[InputDataConfig, InputDataConfigOutput]


# This class is the output for the 'classify_document' function.
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

EntityRecognizerInputDataConfigUnion = Union[EntityRecognizerInputDataConfig, EntityRecognizerInputDataConfigOutput]


class EntityRecognizerMetadata(BaseValidatorModel):
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[EntityRecognizerEvaluationMetrics] = None
    EntityTypes: Optional[List[EntityRecognizerMetadataEntityTypesListItem]] = None


# This class is the output for the 'describe_flywheel_iteration' function.
class DescribeFlywheelIterationResponse(BaseValidatorModel):
    FlywheelIterationProperties: FlywheelIterationProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_flywheel_iteration_history' function.
class ListFlywheelIterationHistoryResponse(BaseValidatorModel):
    FlywheelIterationPropertiesList: List[FlywheelIterationProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Block(BaseValidatorModel):
    Id: Optional[str] = None
    BlockType: Optional[BlockTypeType] = None
    Text: Optional[str] = None
    Page: Optional[int] = None
    Geometry: Optional[Geometry] = None
    Relationships: Optional[List[RelationshipsListItem]] = None


class BatchDetectSyntaxItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    SyntaxTokens: Optional[List[SyntaxToken]] = None


# This class is the output for the 'detect_syntax' function.
class DetectSyntaxResponse(BaseValidatorModel):
    SyntaxTokens: List[SyntaxToken]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_toxic_content' function.
class DetectToxicContentResponse(BaseValidatorModel):
    ResultList: List[ToxicLabels]
    ResponseMetadata: ResponseMetadata


class TargetedSentimentEntity(BaseValidatorModel):
    DescriptiveMentionIndex: Optional[List[int]] = None
    Mentions: Optional[List[TargetedSentimentMention]] = None


class BatchDetectEntitiesItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[Entity]] = None


# This class is the input for the 'update_flywheel' function.
class UpdateFlywheelRequest(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    DataSecurityConfig: Optional[UpdateDataSecurityConfig] = None


# This class is the input for the 'create_dataset' function.
class CreateDatasetRequest(BaseValidatorModel):
    FlywheelArn: str
    DatasetName: str
    InputDataConfig: DatasetInputDataConfig
    DatasetType: Optional[DatasetTypeType] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_document_classifier' function.
class DescribeDocumentClassifierResponse(BaseValidatorModel):
    DocumentClassifierProperties: DocumentClassifierProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_document_classifiers' function.
class ListDocumentClassifiersResponse(BaseValidatorModel):
    DocumentClassifierPropertiesList: List[DocumentClassifierProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_document_classification_job' function.
class DescribeDocumentClassificationJobResponse(BaseValidatorModel):
    DocumentClassificationJobProperties: DocumentClassificationJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_document_classification_jobs' function.
class ListDocumentClassificationJobsResponse(BaseValidatorModel):
    DocumentClassificationJobPropertiesList: List[DocumentClassificationJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_dominant_language_detection_job' function.
class DescribeDominantLanguageDetectionJobResponse(BaseValidatorModel):
    DominantLanguageDetectionJobProperties: DominantLanguageDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_dominant_language_detection_jobs' function.
class ListDominantLanguageDetectionJobsResponse(BaseValidatorModel):
    DominantLanguageDetectionJobPropertiesList: List[DominantLanguageDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_entities_detection_job' function.
class DescribeEntitiesDetectionJobResponse(BaseValidatorModel):
    EntitiesDetectionJobProperties: EntitiesDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_entities_detection_jobs' function.
class ListEntitiesDetectionJobsResponse(BaseValidatorModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_events_detection_job' function.
class DescribeEventsDetectionJobResponse(BaseValidatorModel):
    EventsDetectionJobProperties: EventsDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_events_detection_jobs' function.
class ListEventsDetectionJobsResponse(BaseValidatorModel):
    EventsDetectionJobPropertiesList: List[EventsDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_key_phrases_detection_job' function.
class DescribeKeyPhrasesDetectionJobResponse(BaseValidatorModel):
    KeyPhrasesDetectionJobProperties: KeyPhrasesDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_key_phrases_detection_jobs' function.
class ListKeyPhrasesDetectionJobsResponse(BaseValidatorModel):
    KeyPhrasesDetectionJobPropertiesList: List[KeyPhrasesDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_pii_entities_detection_job' function.
class DescribePiiEntitiesDetectionJobResponse(BaseValidatorModel):
    PiiEntitiesDetectionJobProperties: PiiEntitiesDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_pii_entities_detection_jobs' function.
class ListPiiEntitiesDetectionJobsResponse(BaseValidatorModel):
    PiiEntitiesDetectionJobPropertiesList: List[PiiEntitiesDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_sentiment_detection_job' function.
class DescribeSentimentDetectionJobResponse(BaseValidatorModel):
    SentimentDetectionJobProperties: SentimentDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_sentiment_detection_jobs' function.
class ListSentimentDetectionJobsResponse(BaseValidatorModel):
    SentimentDetectionJobPropertiesList: List[SentimentDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_targeted_sentiment_detection_job' function.
class DescribeTargetedSentimentDetectionJobResponse(BaseValidatorModel):
    TargetedSentimentDetectionJobProperties: TargetedSentimentDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_targeted_sentiment_detection_jobs' function.
class ListTargetedSentimentDetectionJobsResponse(BaseValidatorModel):
    TargetedSentimentDetectionJobPropertiesList: List[TargetedSentimentDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_topics_detection_job' function.
class DescribeTopicsDetectionJobResponse(BaseValidatorModel):
    TopicsDetectionJobProperties: TopicsDetectionJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_topics_detection_jobs' function.
class ListTopicsDetectionJobsResponse(BaseValidatorModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_document_classifier' function.
class CreateDocumentClassifierRequest(BaseValidatorModel):
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: DocumentClassifierInputDataConfigUnion
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfig] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None


# This class is the input for the 'start_document_classification_job' function.
class StartDocumentClassificationJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    DocumentClassifierArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None
    FlywheelArn: Optional[str] = None


# This class is the input for the 'start_dominant_language_detection_job' function.
class StartDominantLanguageDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_entities_detection_job' function.
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
    Tags: Optional[List[Tag]] = None
    FlywheelArn: Optional[str] = None


# This class is the input for the 'start_events_detection_job' function.
class StartEventsDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    TargetEventTypes: List[str]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_key_phrases_detection_job' function.
class StartKeyPhrasesDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_pii_entities_detection_job' function.
class StartPiiEntitiesDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    Mode: PiiEntitiesDetectionModeType
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    RedactionConfig: Optional[RedactionConfigUnion] = None
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_sentiment_detection_job' function.
class StartSentimentDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_targeted_sentiment_detection_job' function.
class StartTargetedSentimentDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_topics_detection_job' function.
class StartTopicsDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnion
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    NumberOfTopics: Optional[int] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    Tags: Optional[List[Tag]] = None


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

TaskConfigUnion = Union[TaskConfig, TaskConfigOutput]


# This class is the input for the 'create_entity_recognizer' function.
class CreateEntityRecognizerRequest(BaseValidatorModel):
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: EntityRecognizerInputDataConfigUnion
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
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


# This class is the output for the 'detect_entities' function.
class DetectEntitiesResponse(BaseValidatorModel):
    Entities: List[Entity]
    DocumentMetadata: DocumentMetadata
    DocumentType: List[DocumentTypeListItem]
    Blocks: List[Block]
    Errors: List[ErrorsListItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_detect_syntax' function.
class BatchDetectSyntaxResponse(BaseValidatorModel):
    ResultList: List[BatchDetectSyntaxItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


class BatchDetectTargetedSentimentItemResult(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[TargetedSentimentEntity]] = None


# This class is the output for the 'detect_targeted_sentiment' function.
class DetectTargetedSentimentResponse(BaseValidatorModel):
    Entities: List[TargetedSentimentEntity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_detect_entities' function.
class BatchDetectEntitiesResponse(BaseValidatorModel):
    ResultList: List[BatchDetectEntitiesItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_flywheel' function.
class DescribeFlywheelResponse(BaseValidatorModel):
    FlywheelProperties: FlywheelProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_flywheel' function.
class UpdateFlywheelResponse(BaseValidatorModel):
    FlywheelProperties: FlywheelProperties
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_flywheel' function.
class CreateFlywheelRequest(BaseValidatorModel):
    FlywheelName: str
    DataAccessRoleArn: str
    DataLakeS3Uri: str
    ActiveModelArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigUnion] = None
    ModelType: Optional[ModelTypeType] = None
    DataSecurityConfig: Optional[DataSecurityConfigUnion] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_entity_recognizer' function.
class DescribeEntityRecognizerResponse(BaseValidatorModel):
    EntityRecognizerProperties: EntityRecognizerProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_entity_recognizers' function.
class ListEntityRecognizersResponse(BaseValidatorModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_detect_targeted_sentiment' function.
class BatchDetectTargetedSentimentResponse(BaseValidatorModel):
    ResultList: List[BatchDetectTargetedSentimentItemResult]
    ErrorList: List[BatchItemError]
    ResponseMetadata: ResponseMetadata