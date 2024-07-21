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
from aws_resource_validator.pydantic_models.comprehend_constants import *

class AugmentedManifestsListItemPaginatorTypeDef(BaseModel):
    S3Uri: str
    AttributeNames: List[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None

class AugmentedManifestsListItemTypeDef(BaseModel):
    S3Uri: str
    AttributeNames: Sequence[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None

class DominantLanguageTypeDef(BaseModel):
    LanguageCode: Optional[str] = None
    Score: Optional[float] = None

class BatchDetectDominantLanguageRequestRequestTypeDef(BaseModel):
    TextList: Sequence[str]

class BatchItemErrorTypeDef(BaseModel):
    Index: Optional[int] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDetectEntitiesRequestRequestTypeDef(BaseModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class KeyPhraseTypeDef(BaseModel):
    Score: Optional[float] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class BatchDetectKeyPhrasesRequestRequestTypeDef(BaseModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class SentimentScoreTypeDef(BaseModel):
    Positive: Optional[float] = None
    Negative: Optional[float] = None
    Neutral: Optional[float] = None
    Mixed: Optional[float] = None

class BatchDetectSentimentRequestRequestTypeDef(BaseModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class BatchDetectSyntaxRequestRequestTypeDef(BaseModel):
    TextList: Sequence[str]
    LanguageCode: SyntaxLanguageCodeType

class BatchDetectTargetedSentimentRequestRequestTypeDef(BaseModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class ChildBlockTypeDef(BaseModel):
    ChildBlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class RelationshipsListItemTypeDef(BaseModel):
    Ids: Optional[List[str]] = None
    Type: Optional[Literal["CHILD"]] = None

class BoundingBoxTypeDef(BaseModel):
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None
    Width: Optional[float] = None

class ClassifierEvaluationMetricsTypeDef(BaseModel):
    Accuracy: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None
    MicroPrecision: Optional[float] = None
    MicroRecall: Optional[float] = None
    MicroF1Score: Optional[float] = None
    HammingLoss: Optional[float] = None

class DocumentReaderConfigTypeDef(BaseModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[Sequence[DocumentReadFeatureTypesType]] = None

class DocumentClassTypeDef(BaseModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None

class DocumentLabelTypeDef(BaseModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None

class DocumentTypeListItemTypeDef(BaseModel):
    Page: Optional[int] = None
    Type: Optional[DocumentTypeType] = None

class ErrorsListItemTypeDef(BaseModel):
    Page: Optional[int] = None
    ErrorCode: Optional[PageBasedErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class WarningsListItemTypeDef(BaseModel):
    Page: Optional[int] = None
    WarnCode: Optional[PageBasedWarningCodeType] = None
    WarnMessage: Optional[str] = None

class ContainsPiiEntitiesRequestRequestTypeDef(BaseModel):
    Text: str
    LanguageCode: LanguageCodeType

class EntityLabelTypeDef(BaseModel):
    Name: Optional[PiiEntityTypeType] = None
    Score: Optional[float] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class DocumentClassifierOutputDataConfigTypeDef(BaseModel):
    S3Uri: Optional[str] = None
    KmsKeyId: Optional[str] = None
    FlywheelStatsS3Prefix: Optional[str] = None

class VpcConfigTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class DatasetAugmentedManifestsListItemTypeDef(BaseModel):
    AttributeNames: Sequence[str]
    S3Uri: str
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None

class DatasetDocumentClassifierInputDataConfigTypeDef(BaseModel):
    S3Uri: str
    LabelDelimiter: Optional[str] = None

class DatasetEntityRecognizerAnnotationsTypeDef(BaseModel):
    S3Uri: str

class DatasetEntityRecognizerDocumentsTypeDef(BaseModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None

class DatasetEntityRecognizerEntityListTypeDef(BaseModel):
    S3Uri: str

class DatasetPropertiesTypeDef(BaseModel):
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

class DeleteDocumentClassifierRequestRequestTypeDef(BaseModel):
    DocumentClassifierArn: str

class DeleteEndpointRequestRequestTypeDef(BaseModel):
    EndpointArn: str

class DeleteEntityRecognizerRequestRequestTypeDef(BaseModel):
    EntityRecognizerArn: str

class DeleteFlywheelRequestRequestTypeDef(BaseModel):
    FlywheelArn: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    PolicyRevisionId: Optional[str] = None

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    DatasetArn: str

class DescribeDocumentClassificationJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeDocumentClassifierRequestRequestTypeDef(BaseModel):
    DocumentClassifierArn: str

class DescribeDominantLanguageDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeEndpointRequestRequestTypeDef(BaseModel):
    EndpointArn: str

class EndpointPropertiesTypeDef(BaseModel):
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

class DescribeEntitiesDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeEntityRecognizerRequestRequestTypeDef(BaseModel):
    EntityRecognizerArn: str

class DescribeEventsDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeFlywheelIterationRequestRequestTypeDef(BaseModel):
    FlywheelArn: str
    FlywheelIterationId: str

class DescribeFlywheelRequestRequestTypeDef(BaseModel):
    FlywheelArn: str

class DescribeKeyPhrasesDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribePiiEntitiesDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DescribeSentimentDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeTargetedSentimentDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeTopicsDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DetectDominantLanguageRequestRequestTypeDef(BaseModel):
    Text: str

class DetectKeyPhrasesRequestRequestTypeDef(BaseModel):
    Text: str
    LanguageCode: LanguageCodeType

class DetectPiiEntitiesRequestRequestTypeDef(BaseModel):
    Text: str
    LanguageCode: LanguageCodeType

class PiiEntityTypeDef(BaseModel):
    Score: Optional[float] = None
    Type: Optional[PiiEntityTypeType] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class DetectSentimentRequestRequestTypeDef(BaseModel):
    Text: str
    LanguageCode: LanguageCodeType

class DetectSyntaxRequestRequestTypeDef(BaseModel):
    Text: str
    LanguageCode: SyntaxLanguageCodeType

class DetectTargetedSentimentRequestRequestTypeDef(BaseModel):
    Text: str
    LanguageCode: LanguageCodeType

class TextSegmentTypeDef(BaseModel):
    Text: str

class DocumentClassificationConfigTypeDef(BaseModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[Sequence[str]] = None

class OutputDataConfigTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class VpcConfigPaginatorTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class DocumentClassifierDocumentsTypeDef(BaseModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None

class DocumentReaderConfigPaginatorTypeDef(BaseModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[List[DocumentReadFeatureTypesType]] = None

class DocumentClassifierSummaryTypeDef(BaseModel):
    DocumentClassifierName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None

class ExtractedCharactersListItemTypeDef(BaseModel):
    Page: Optional[int] = None
    Count: Optional[int] = None

class EntityTypesListItemTypeDef(BaseModel):
    Type: str

class EntityRecognizerAnnotationsTypeDef(BaseModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None

class EntityRecognizerDocumentsTypeDef(BaseModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None

class EntityRecognizerEntityListTypeDef(BaseModel):
    S3Uri: str

class EntityRecognizerEvaluationMetricsTypeDef(BaseModel):
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None

class EntityTypesEvaluationMetricsTypeDef(BaseModel):
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None

class EntityRecognizerOutputDataConfigTypeDef(BaseModel):
    FlywheelStatsS3Prefix: Optional[str] = None

class EntityRecognizerSummaryTypeDef(BaseModel):
    RecognizerName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None

class FlywheelModelEvaluationMetricsTypeDef(BaseModel):
    AverageF1Score: Optional[float] = None
    AveragePrecision: Optional[float] = None
    AverageRecall: Optional[float] = None
    AverageAccuracy: Optional[float] = None

class FlywheelSummaryTypeDef(BaseModel):
    FlywheelArn: Optional[str] = None
    ActiveModelArn: Optional[str] = None
    DataLakeS3Uri: Optional[str] = None
    Status: Optional[FlywheelStatusType] = None
    ModelType: Optional[ModelTypeType] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LatestFlywheelIteration: Optional[str] = None

class PointTypeDef(BaseModel):
    X: Optional[float] = None
    Y: Optional[float] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDocumentClassifierSummariesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntityRecognizerSummariesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PartOfSpeechTagTypeDef(BaseModel):
    Tag: Optional[PartOfSpeechTagTypeType] = None
    Score: Optional[float] = None

class PiiOutputDataConfigTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class RedactionConfigTypeDef(BaseModel):
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourcePolicy: str
    PolicyRevisionId: Optional[str] = None

class StartFlywheelIterationRequestRequestTypeDef(BaseModel):
    FlywheelArn: str
    ClientRequestToken: Optional[str] = None

class StopDominantLanguageDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopEntitiesDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopEventsDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopKeyPhrasesDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopPiiEntitiesDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopSentimentDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopTargetedSentimentDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopTrainingDocumentClassifierRequestRequestTypeDef(BaseModel):
    DocumentClassifierArn: str

class StopTrainingEntityRecognizerRequestRequestTypeDef(BaseModel):
    EntityRecognizerArn: str

class ToxicContentTypeDef(BaseModel):
    Name: Optional[ToxicContentTypeType] = None
    Score: Optional[float] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateEndpointRequestRequestTypeDef(BaseModel):
    EndpointArn: str
    DesiredModelArn: Optional[str] = None
    DesiredInferenceUnits: Optional[int] = None
    DesiredDataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None

class BatchDetectDominantLanguageItemResultTypeDef(BaseModel):
    Index: Optional[int] = None
    Languages: Optional[List[DominantLanguageTypeDef]] = None

class CreateDatasetResponseTypeDef(BaseModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDocumentClassifierResponseTypeDef(BaseModel):
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointResponseTypeDef(BaseModel):
    EndpointArn: str
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityRecognizerResponseTypeDef(BaseModel):
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlywheelResponseTypeDef(BaseModel):
    FlywheelArn: str
    ActiveModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(BaseModel):
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectDominantLanguageResponseTypeDef(BaseModel):
    Languages: List[DominantLanguageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportModelResponseTypeDef(BaseModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDocumentClassificationJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDominantLanguageDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartEntitiesDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartEventsDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlywheelIterationResponseTypeDef(BaseModel):
    FlywheelArn: str
    FlywheelIterationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartKeyPhrasesDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartPiiEntitiesDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSentimentDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTargetedSentimentDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTopicsDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDominantLanguageDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopEntitiesDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopEventsDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopKeyPhrasesDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopPiiEntitiesDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopSentimentDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopTargetedSentimentDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointResponseTypeDef(BaseModel):
    DesiredModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectKeyPhrasesItemResultTypeDef(BaseModel):
    Index: Optional[int] = None
    KeyPhrases: Optional[List[KeyPhraseTypeDef]] = None

class DetectKeyPhrasesResponseTypeDef(BaseModel):
    KeyPhrases: List[KeyPhraseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSentimentItemResultTypeDef(BaseModel):
    Index: Optional[int] = None
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScoreTypeDef] = None

class DetectSentimentResponseTypeDef(BaseModel):
    Sentiment: SentimentTypeType
    SentimentScore: SentimentScoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MentionSentimentTypeDef(BaseModel):
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScoreTypeDef] = None

class BlockReferenceTypeDef(BaseModel):
    BlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    ChildBlocks: Optional[List[ChildBlockTypeDef]] = None

class ClassifierMetadataTypeDef(BaseModel):
    NumberOfLabels: Optional[int] = None
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[ClassifierEvaluationMetricsTypeDef] = None

class ClassifyDocumentRequestRequestTypeDef(BaseModel):
    EndpointArn: str
    Text: Optional[str] = None
    Bytes: Optional[BlobTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class DetectEntitiesRequestRequestTypeDef(BaseModel):
    Text: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    EndpointArn: Optional[str] = None
    Bytes: Optional[BlobTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class InputDataConfigTypeDef(BaseModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class ContainsPiiEntitiesResponseTypeDef(BaseModel):
    Labels: List[EntityLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointRequestRequestTypeDef(BaseModel):
    EndpointName: str
    DesiredInferenceUnits: int
    ModelArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None

class ImportModelRequestRequestTypeDef(BaseModel):
    SourceModelArn: str
    ModelName: Optional[str] = None
    VersionName: Optional[str] = None
    ModelKmsKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class DataSecurityConfigTypeDef(BaseModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    DataLakeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class UpdateDataSecurityConfigTypeDef(BaseModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class DatasetEntityRecognizerInputDataConfigTypeDef(BaseModel):
    Documents: DatasetEntityRecognizerDocumentsTypeDef
    Annotations: Optional[DatasetEntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[DatasetEntityRecognizerEntityListTypeDef] = None

class DatasetFilterTypeDef(BaseModel):
    Status: Optional[DatasetStatusType] = None
    DatasetType: Optional[DatasetTypeType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None

class DocumentClassificationJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class DocumentClassifierFilterTypeDef(BaseModel):
    Status: Optional[ModelStatusType] = None
    DocumentClassifierName: Optional[str] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class DominantLanguageDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class EndpointFilterTypeDef(BaseModel):
    ModelArn: Optional[str] = None
    Status: Optional[EndpointStatusType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class EntitiesDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class EntityRecognizerFilterTypeDef(BaseModel):
    Status: Optional[ModelStatusType] = None
    RecognizerName: Optional[str] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class EventsDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class FlywheelFilterTypeDef(BaseModel):
    Status: Optional[FlywheelStatusType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None

class FlywheelIterationFilterTypeDef(BaseModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None

class KeyPhrasesDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class PiiEntitiesDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class SentimentDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class TargetedSentimentDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class TopicsDetectionJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class DescribeDatasetResponseTypeDef(BaseModel):
    DatasetProperties: DatasetPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseModel):
    DatasetPropertiesList: List[DatasetPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointResponseTypeDef(BaseModel):
    EndpointProperties: EndpointPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointsResponseTypeDef(BaseModel):
    EndpointPropertiesList: List[EndpointPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectPiiEntitiesResponseTypeDef(BaseModel):
    Entities: List[PiiEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectToxicContentRequestRequestTypeDef(BaseModel):
    TextSegments: Sequence[TextSegmentTypeDef]
    LanguageCode: LanguageCodeType

class DocumentClassifierInputDataConfigTypeDef(BaseModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItemTypeDef]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocumentsTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class DocumentClassifierInputDataConfigPaginatorTypeDef(BaseModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemPaginatorTypeDef]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocumentsTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigPaginatorTypeDef] = None

class InputDataConfigPaginatorTypeDef(BaseModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigPaginatorTypeDef] = None

class ListDocumentClassifierSummariesResponseTypeDef(BaseModel):
    DocumentClassifierSummariesList: List[DocumentClassifierSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentMetadataTypeDef(BaseModel):
    Pages: Optional[int] = None
    ExtractedCharacters: Optional[List[ExtractedCharactersListItemTypeDef]] = None

class EntityRecognitionConfigTypeDef(BaseModel):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]

class EntityRecognizerInputDataConfigPaginatorTypeDef(BaseModel):
    EntityTypes: List[EntityTypesListItemTypeDef]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocumentsTypeDef] = None
    Annotations: Optional[EntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[EntityRecognizerEntityListTypeDef] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemPaginatorTypeDef]] = None

class EntityRecognizerInputDataConfigTypeDef(BaseModel):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocumentsTypeDef] = None
    Annotations: Optional[EntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[EntityRecognizerEntityListTypeDef] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItemTypeDef]] = None

class EntityRecognizerMetadataEntityTypesListItemTypeDef(BaseModel):
    Type: Optional[str] = None
    EvaluationMetrics: Optional[EntityTypesEvaluationMetricsTypeDef] = None
    NumberOfTrainMentions: Optional[int] = None

class ListEntityRecognizerSummariesResponseTypeDef(BaseModel):
    EntityRecognizerSummariesList: List[EntityRecognizerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FlywheelIterationPropertiesTypeDef(BaseModel):
    FlywheelArn: Optional[str] = None
    FlywheelIterationId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[FlywheelIterationStatusType] = None
    Message: Optional[str] = None
    EvaluatedModelArn: Optional[str] = None
    EvaluatedModelMetrics: Optional[FlywheelModelEvaluationMetricsTypeDef] = None
    TrainedModelArn: Optional[str] = None
    TrainedModelMetrics: Optional[FlywheelModelEvaluationMetricsTypeDef] = None
    EvaluationManifestS3Prefix: Optional[str] = None

class ListFlywheelsResponseTypeDef(BaseModel):
    FlywheelSummaryList: List[FlywheelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GeometryTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None

class SyntaxTokenTypeDef(BaseModel):
    TokenId: Optional[int] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    PartOfSpeech: Optional[PartOfSpeechTagTypeDef] = None

class ToxicLabelsTypeDef(BaseModel):
    Labels: Optional[List[ToxicContentTypeDef]] = None
    Toxicity: Optional[float] = None

class BatchDetectDominantLanguageResponseTypeDef(BaseModel):
    ResultList: List[BatchDetectDominantLanguageItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectKeyPhrasesResponseTypeDef(BaseModel):
    ResultList: List[BatchDetectKeyPhrasesItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSentimentResponseTypeDef(BaseModel):
    ResultList: List[BatchDetectSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetedSentimentMentionTypeDef(BaseModel):
    Score: Optional[float] = None
    GroupScore: Optional[float] = None
    Text: Optional[str] = None
    Type: Optional[TargetedSentimentEntityTypeType] = None
    MentionSentiment: Optional[MentionSentimentTypeDef] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class EntityTypeDef(BaseModel):
    Score: Optional[float] = None
    Type: Optional[EntityTypeType] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    BlockReferences: Optional[List[BlockReferenceTypeDef]] = None

class DocumentClassificationJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    DocumentClassifierArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    FlywheelArn: Optional[str] = None

class DominantLanguageDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class EntitiesDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    EntityRecognizerArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    FlywheelArn: Optional[str] = None

class EventsDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    TargetEventTypes: Optional[List[str]] = None

class KeyPhrasesDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class PiiEntitiesDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[PiiOutputDataConfigTypeDef] = None
    RedactionConfig: Optional[RedactionConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    Mode: Optional[PiiEntitiesDetectionModeType] = None

class SentimentDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class StartDocumentClassificationJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    DocumentClassifierArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FlywheelArn: Optional[str] = None

class StartDominantLanguageDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartEntitiesDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    EntityRecognizerArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FlywheelArn: Optional[str] = None

class StartEventsDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    TargetEventTypes: Sequence[str]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartKeyPhrasesDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartPiiEntitiesDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    Mode: PiiEntitiesDetectionModeType
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    RedactionConfig: Optional[RedactionConfigTypeDef] = None
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartSentimentDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartTargetedSentimentDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartTopicsDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    NumberOfTopics: Optional[int] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TargetedSentimentDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class TopicsDetectionJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    NumberOfTopics: Optional[int] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class UpdateFlywheelRequestRequestTypeDef(BaseModel):
    FlywheelArn: str
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    DataSecurityConfig: Optional[UpdateDataSecurityConfigTypeDef] = None

class DatasetInputDataConfigTypeDef(BaseModel):
    AugmentedManifests: Optional[Sequence[DatasetAugmentedManifestsListItemTypeDef]] = None
    DataFormat: Optional[DatasetDataFormatType] = None
    DocumentClassifierInputDataConfig: Optional[       DatasetDocumentClassifierInputDataConfigTypeDef     ] = None
    EntityRecognizerInputDataConfig: Optional[       DatasetEntityRecognizerInputDataConfigTypeDef     ] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    FlywheelArn: Optional[str] = None
    Filter: Optional[DatasetFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDocumentClassificationJobsRequestListDocumentClassificationJobsPaginateTypeDef(BaseModel):
    Filter: Optional[DocumentClassificationJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentClassificationJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[DocumentClassificationJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDocumentClassifiersRequestListDocumentClassifiersPaginateTypeDef(BaseModel):
    Filter: Optional[DocumentClassifierFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentClassifiersRequestRequestTypeDef(BaseModel):
    Filter: Optional[DocumentClassifierFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDominantLanguageDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[DominantLanguageDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEndpointsRequestListEndpointsPaginateTypeDef(BaseModel):
    Filter: Optional[EndpointFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointsRequestRequestTypeDef(BaseModel):
    Filter: Optional[EndpointFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntitiesDetectionJobsRequestListEntitiesDetectionJobsPaginateTypeDef(BaseModel):
    Filter: Optional[EntitiesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitiesDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[EntitiesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntityRecognizersRequestListEntityRecognizersPaginateTypeDef(BaseModel):
    Filter: Optional[EntityRecognizerFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntityRecognizersRequestRequestTypeDef(BaseModel):
    Filter: Optional[EntityRecognizerFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventsDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[EventsDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFlywheelsRequestRequestTypeDef(BaseModel):
    Filter: Optional[FlywheelFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFlywheelIterationHistoryRequestRequestTypeDef(BaseModel):
    FlywheelArn: str
    Filter: Optional[FlywheelIterationFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListKeyPhrasesDetectionJobsRequestListKeyPhrasesDetectionJobsPaginateTypeDef(BaseModel):
    Filter: Optional[KeyPhrasesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyPhrasesDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[KeyPhrasesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPiiEntitiesDetectionJobsRequestListPiiEntitiesDetectionJobsPaginateTypeDef(BaseModel):
    Filter: Optional[PiiEntitiesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPiiEntitiesDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[PiiEntitiesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSentimentDetectionJobsRequestListSentimentDetectionJobsPaginateTypeDef(BaseModel):
    Filter: Optional[SentimentDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSentimentDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[SentimentDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTargetedSentimentDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[TargetedSentimentDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTopicsDetectionJobsRequestListTopicsDetectionJobsPaginateTypeDef(BaseModel):
    Filter: Optional[TopicsDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicsDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[TopicsDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class CreateDocumentClassifierRequestRequestTypeDef(BaseModel):
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: DocumentClassifierInputDataConfigTypeDef
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfigTypeDef] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None

class DocumentClassifierPropertiesTypeDef(BaseModel):
    DocumentClassifierArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[DocumentClassifierInputDataConfigTypeDef] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfigTypeDef] = None
    ClassifierMetadata: Optional[ClassifierMetadataTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None

class DocumentClassifierPropertiesPaginatorTypeDef(BaseModel):
    DocumentClassifierArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[DocumentClassifierInputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfigTypeDef] = None
    ClassifierMetadata: Optional[ClassifierMetadataTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None

class DocumentClassificationJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    DocumentClassifierArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None
    FlywheelArn: Optional[str] = None

class DominantLanguageDetectionJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None

class EntitiesDetectionJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    EntityRecognizerArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None
    FlywheelArn: Optional[str] = None

class KeyPhrasesDetectionJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None

class PiiEntitiesDetectionJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[PiiOutputDataConfigTypeDef] = None
    RedactionConfig: Optional[RedactionConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    Mode: Optional[PiiEntitiesDetectionModeType] = None

class SentimentDetectionJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None

class TopicsDetectionJobPropertiesPaginatorTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigPaginatorTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    NumberOfTopics: Optional[int] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None

class ClassifyDocumentResponseTypeDef(BaseModel):
    Classes: List[DocumentClassTypeDef]
    Labels: List[DocumentLabelTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    Warnings: List[WarningsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaskConfigTypeDef(BaseModel):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: Optional[DocumentClassificationConfigTypeDef] = None
    EntityRecognitionConfig: Optional[EntityRecognitionConfigTypeDef] = None

class CreateEntityRecognizerRequestRequestTypeDef(BaseModel):
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: EntityRecognizerInputDataConfigTypeDef
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None

class EntityRecognizerMetadataTypeDef(BaseModel):
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[EntityRecognizerEvaluationMetricsTypeDef] = None
    EntityTypes: Optional[List[EntityRecognizerMetadataEntityTypesListItemTypeDef]] = None

class DescribeFlywheelIterationResponseTypeDef(BaseModel):
    FlywheelIterationProperties: FlywheelIterationPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlywheelIterationHistoryResponseTypeDef(BaseModel):
    FlywheelIterationPropertiesList: List[FlywheelIterationPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BlockTypeDef(BaseModel):
    Id: Optional[str] = None
    BlockType: Optional[BlockTypeType] = None
    Text: Optional[str] = None
    Page: Optional[int] = None
    Geometry: Optional[GeometryTypeDef] = None
    Relationships: Optional[List[RelationshipsListItemTypeDef]] = None

class BatchDetectSyntaxItemResultTypeDef(BaseModel):
    Index: Optional[int] = None
    SyntaxTokens: Optional[List[SyntaxTokenTypeDef]] = None

class DetectSyntaxResponseTypeDef(BaseModel):
    SyntaxTokens: List[SyntaxTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectToxicContentResponseTypeDef(BaseModel):
    ResultList: List[ToxicLabelsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetedSentimentEntityTypeDef(BaseModel):
    DescriptiveMentionIndex: Optional[List[int]] = None
    Mentions: Optional[List[TargetedSentimentMentionTypeDef]] = None

class BatchDetectEntitiesItemResultTypeDef(BaseModel):
    Index: Optional[int] = None
    Entities: Optional[List[EntityTypeDef]] = None

class DescribeDocumentClassificationJobResponseTypeDef(BaseModel):
    DocumentClassificationJobProperties: DocumentClassificationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassificationJobsResponseTypeDef(BaseModel):
    DocumentClassificationJobPropertiesList: List[DocumentClassificationJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDominantLanguageDetectionJobResponseTypeDef(BaseModel):
    DominantLanguageDetectionJobProperties: DominantLanguageDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDominantLanguageDetectionJobsResponseTypeDef(BaseModel):
    DominantLanguageDetectionJobPropertiesList: List[       DominantLanguageDetectionJobPropertiesTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntitiesDetectionJobResponseTypeDef(BaseModel):
    EntitiesDetectionJobProperties: EntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionJobsResponseTypeDef(BaseModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsDetectionJobResponseTypeDef(BaseModel):
    EventsDetectionJobProperties: EventsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventsDetectionJobsResponseTypeDef(BaseModel):
    EventsDetectionJobPropertiesList: List[EventsDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyPhrasesDetectionJobResponseTypeDef(BaseModel):
    KeyPhrasesDetectionJobProperties: KeyPhrasesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPhrasesDetectionJobsResponseTypeDef(BaseModel):
    KeyPhrasesDetectionJobPropertiesList: List[KeyPhrasesDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePiiEntitiesDetectionJobResponseTypeDef(BaseModel):
    PiiEntitiesDetectionJobProperties: PiiEntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPiiEntitiesDetectionJobsResponseTypeDef(BaseModel):
    PiiEntitiesDetectionJobPropertiesList: List[PiiEntitiesDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSentimentDetectionJobResponseTypeDef(BaseModel):
    SentimentDetectionJobProperties: SentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSentimentDetectionJobsResponseTypeDef(BaseModel):
    SentimentDetectionJobPropertiesList: List[SentimentDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTargetedSentimentDetectionJobResponseTypeDef(BaseModel):
    TargetedSentimentDetectionJobProperties: TargetedSentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetedSentimentDetectionJobsResponseTypeDef(BaseModel):
    TargetedSentimentDetectionJobPropertiesList: List[       TargetedSentimentDetectionJobPropertiesTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTopicsDetectionJobResponseTypeDef(BaseModel):
    TopicsDetectionJobProperties: TopicsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicsDetectionJobsResponseTypeDef(BaseModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestRequestTypeDef(BaseModel):
    FlywheelArn: str
    DatasetName: str
    InputDataConfig: DatasetInputDataConfigTypeDef
    DatasetType: Optional[DatasetTypeType] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeDocumentClassifierResponseTypeDef(BaseModel):
    DocumentClassifierProperties: DocumentClassifierPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassifiersResponseTypeDef(BaseModel):
    DocumentClassifierPropertiesList: List[DocumentClassifierPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassifiersResponsePaginatorTypeDef(BaseModel):
    DocumentClassifierPropertiesList: List[DocumentClassifierPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassificationJobsResponsePaginatorTypeDef(BaseModel):
    DocumentClassificationJobPropertiesList: List[       DocumentClassificationJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDominantLanguageDetectionJobsResponsePaginatorTypeDef(BaseModel):
    DominantLanguageDetectionJobPropertiesList: List[       DominantLanguageDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionJobsResponsePaginatorTypeDef(BaseModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPhrasesDetectionJobsResponsePaginatorTypeDef(BaseModel):
    KeyPhrasesDetectionJobPropertiesList: List[       KeyPhrasesDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPiiEntitiesDetectionJobsResponsePaginatorTypeDef(BaseModel):
    PiiEntitiesDetectionJobPropertiesList: List[       PiiEntitiesDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSentimentDetectionJobsResponsePaginatorTypeDef(BaseModel):
    SentimentDetectionJobPropertiesList: List[       SentimentDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicsDetectionJobsResponsePaginatorTypeDef(BaseModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlywheelRequestRequestTypeDef(BaseModel):
    FlywheelName: str
    DataAccessRoleArn: str
    DataLakeS3Uri: str
    ActiveModelArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigTypeDef] = None
    ModelType: Optional[ModelTypeType] = None
    DataSecurityConfig: Optional[DataSecurityConfigTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class FlywheelPropertiesTypeDef(BaseModel):
    FlywheelArn: Optional[str] = None
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigTypeDef] = None
    DataLakeS3Uri: Optional[str] = None
    DataSecurityConfig: Optional[DataSecurityConfigTypeDef] = None
    Status: Optional[FlywheelStatusType] = None
    ModelType: Optional[ModelTypeType] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LatestFlywheelIteration: Optional[str] = None

class EntityRecognizerPropertiesPaginatorTypeDef(BaseModel):
    EntityRecognizerArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[EntityRecognizerInputDataConfigPaginatorTypeDef] = None
    RecognizerMetadata: Optional[EntityRecognizerMetadataTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None
    OutputDataConfig: Optional[EntityRecognizerOutputDataConfigTypeDef] = None

class EntityRecognizerPropertiesTypeDef(BaseModel):
    EntityRecognizerArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[EntityRecognizerInputDataConfigTypeDef] = None
    RecognizerMetadata: Optional[EntityRecognizerMetadataTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None
    OutputDataConfig: Optional[EntityRecognizerOutputDataConfigTypeDef] = None

class DetectEntitiesResponseTypeDef(BaseModel):
    Entities: List[EntityTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Blocks: List[BlockTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSyntaxResponseTypeDef(BaseModel):
    ResultList: List[BatchDetectSyntaxItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectTargetedSentimentItemResultTypeDef(BaseModel):
    Index: Optional[int] = None
    Entities: Optional[List[TargetedSentimentEntityTypeDef]] = None

class DetectTargetedSentimentResponseTypeDef(BaseModel):
    Entities: List[TargetedSentimentEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectEntitiesResponseTypeDef(BaseModel):
    ResultList: List[BatchDetectEntitiesItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlywheelResponseTypeDef(BaseModel):
    FlywheelProperties: FlywheelPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlywheelResponseTypeDef(BaseModel):
    FlywheelProperties: FlywheelPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntityRecognizersResponsePaginatorTypeDef(BaseModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityRecognizerResponseTypeDef(BaseModel):
    EntityRecognizerProperties: EntityRecognizerPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntityRecognizersResponseTypeDef(BaseModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectTargetedSentimentResponseTypeDef(BaseModel):
    ResultList: List[BatchDetectTargetedSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

