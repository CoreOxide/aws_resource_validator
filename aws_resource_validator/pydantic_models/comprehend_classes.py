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
from aws_resource_validator.pydantic_models.comprehend_constants import *

class AugmentedManifestsListItemPaginatorTypeDef(BaseValidatorModel):
    S3Uri: str
    AttributeNames: List[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None

class AugmentedManifestsListItemTypeDef(BaseValidatorModel):
    S3Uri: str
    AttributeNames: Sequence[str]
    Split: Optional[SplitType] = None
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None

class DominantLanguageTypeDef(BaseValidatorModel):
    LanguageCode: Optional[str] = None
    Score: Optional[float] = None

class BatchDetectDominantLanguageRequestRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]

class BatchItemErrorTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDetectEntitiesRequestRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class KeyPhraseTypeDef(BaseValidatorModel):
    Score: Optional[float] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class BatchDetectKeyPhrasesRequestRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class SentimentScoreTypeDef(BaseValidatorModel):
    Positive: Optional[float] = None
    Negative: Optional[float] = None
    Neutral: Optional[float] = None
    Mixed: Optional[float] = None

class BatchDetectSentimentRequestRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class BatchDetectSyntaxRequestRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: SyntaxLanguageCodeType

class BatchDetectTargetedSentimentRequestRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class ChildBlockTypeDef(BaseValidatorModel):
    ChildBlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class RelationshipsListItemTypeDef(BaseValidatorModel):
    Ids: Optional[List[str]] = None
    Type: Optional[Literal["CHILD"]] = None

class BoundingBoxTypeDef(BaseValidatorModel):
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None
    Width: Optional[float] = None

class ClassifierEvaluationMetricsTypeDef(BaseValidatorModel):
    Accuracy: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None
    MicroPrecision: Optional[float] = None
    MicroRecall: Optional[float] = None
    MicroF1Score: Optional[float] = None
    HammingLoss: Optional[float] = None

class DocumentReaderConfigTypeDef(BaseValidatorModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[Sequence[DocumentReadFeatureTypesType]] = None

class DocumentClassTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None

class DocumentLabelTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None

class DocumentTypeListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    Type: Optional[DocumentTypeType] = None

class ErrorsListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    ErrorCode: Optional[PageBasedErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class WarningsListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    WarnCode: Optional[PageBasedWarningCodeType] = None
    WarnMessage: Optional[str] = None

class ContainsPiiEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType

class EntityLabelTypeDef(BaseValidatorModel):
    Name: Optional[PiiEntityTypeType] = None
    Score: Optional[float] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class DocumentClassifierOutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None
    KmsKeyId: Optional[str] = None
    FlywheelStatsS3Prefix: Optional[str] = None

class VpcConfigTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class DatasetAugmentedManifestsListItemTypeDef(BaseValidatorModel):
    AttributeNames: Sequence[str]
    S3Uri: str
    AnnotationDataS3Uri: Optional[str] = None
    SourceDocumentsS3Uri: Optional[str] = None
    DocumentType: Optional[AugmentedManifestsDocumentTypeFormatType] = None

class DatasetDocumentClassifierInputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    LabelDelimiter: Optional[str] = None

class DatasetEntityRecognizerAnnotationsTypeDef(BaseValidatorModel):
    S3Uri: str

class DatasetEntityRecognizerDocumentsTypeDef(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None

class DatasetEntityRecognizerEntityListTypeDef(BaseValidatorModel):
    S3Uri: str

class DatasetPropertiesTypeDef(BaseValidatorModel):
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

class DeleteDocumentClassifierRequestRequestTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str

class DeleteEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointArn: str

class DeleteEntityRecognizerRequestRequestTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str

class DeleteFlywheelRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    PolicyRevisionId: Optional[str] = None

class DescribeDatasetRequestRequestTypeDef(BaseValidatorModel):
    DatasetArn: str

class DescribeDocumentClassificationJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeDocumentClassifierRequestRequestTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str

class DescribeDominantLanguageDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointArn: str

class EndpointPropertiesTypeDef(BaseValidatorModel):
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

class DescribeEntitiesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeEntityRecognizerRequestRequestTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str

class DescribeEventsDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeFlywheelIterationRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str

class DescribeFlywheelRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str

class DescribeKeyPhrasesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribePiiEntitiesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DescribeSentimentDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeTargetedSentimentDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeTopicsDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DetectDominantLanguageRequestRequestTypeDef(BaseValidatorModel):
    Text: str

class DetectKeyPhrasesRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType

class DetectPiiEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType

class PiiEntityTypeDef(BaseValidatorModel):
    Score: Optional[float] = None
    Type: Optional[PiiEntityTypeType] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class DetectSentimentRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType

class DetectSyntaxRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    LanguageCode: SyntaxLanguageCodeType

class DetectTargetedSentimentRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    LanguageCode: LanguageCodeType

class TextSegmentTypeDef(BaseValidatorModel):
    Text: str

class DocumentClassificationConfigTypeDef(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[Sequence[str]] = None

class OutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class VpcConfigPaginatorTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class DocumentClassifierDocumentsTypeDef(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None

class DocumentReaderConfigPaginatorTypeDef(BaseValidatorModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[List[DocumentReadFeatureTypesType]] = None

class DocumentClassifierSummaryTypeDef(BaseValidatorModel):
    DocumentClassifierName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None

class ExtractedCharactersListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    Count: Optional[int] = None

class EntityTypesListItemTypeDef(BaseValidatorModel):
    Type: str

class EntityRecognizerAnnotationsTypeDef(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None

class EntityRecognizerDocumentsTypeDef(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None

class EntityRecognizerEntityListTypeDef(BaseValidatorModel):
    S3Uri: str

class EntityRecognizerEvaluationMetricsTypeDef(BaseValidatorModel):
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None

class EntityTypesEvaluationMetricsTypeDef(BaseValidatorModel):
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1Score: Optional[float] = None

class EntityRecognizerOutputDataConfigTypeDef(BaseValidatorModel):
    FlywheelStatsS3Prefix: Optional[str] = None

class EntityRecognizerSummaryTypeDef(BaseValidatorModel):
    RecognizerName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None

class FlywheelModelEvaluationMetricsTypeDef(BaseValidatorModel):
    AverageF1Score: Optional[float] = None
    AveragePrecision: Optional[float] = None
    AverageRecall: Optional[float] = None
    AverageAccuracy: Optional[float] = None

class FlywheelSummaryTypeDef(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    ActiveModelArn: Optional[str] = None
    DataLakeS3Uri: Optional[str] = None
    Status: Optional[FlywheelStatusType] = None
    ModelType: Optional[ModelTypeType] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LatestFlywheelIteration: Optional[str] = None

class PointTypeDef(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDocumentClassifierSummariesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntityRecognizerSummariesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PartOfSpeechTagTypeDef(BaseValidatorModel):
    Tag: Optional[PartOfSpeechTagTypeType] = None
    Score: Optional[float] = None

class PiiOutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class RedactionConfigTypeDef(BaseValidatorModel):
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    PolicyRevisionId: Optional[str] = None

class StartFlywheelIterationRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    ClientRequestToken: Optional[str] = None

class StopDominantLanguageDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopEntitiesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopEventsDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopKeyPhrasesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopPiiEntitiesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopSentimentDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopTargetedSentimentDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopTrainingDocumentClassifierRequestRequestTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str

class StopTrainingEntityRecognizerRequestRequestTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str

class ToxicContentTypeDef(BaseValidatorModel):
    Name: Optional[ToxicContentTypeType] = None
    Score: Optional[float] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointArn: str
    DesiredModelArn: Optional[str] = None
    DesiredInferenceUnits: Optional[int] = None
    DesiredDataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None

class BatchDetectDominantLanguageItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Languages: Optional[List[DominantLanguageTypeDef]] = None

class CreateDatasetResponseTypeDef(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDocumentClassifierResponseTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointResponseTypeDef(BaseValidatorModel):
    EndpointArn: str
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityRecognizerResponseTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlywheelResponseTypeDef(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectDominantLanguageResponseTypeDef(BaseValidatorModel):
    Languages: List[DominantLanguageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportModelResponseTypeDef(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDocumentClassificationJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDominantLanguageDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartEventsDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlywheelIterationResponseTypeDef(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartKeyPhrasesDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartPiiEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTargetedSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTopicsDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDominantLanguageDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopEventsDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopKeyPhrasesDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopPiiEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopTargetedSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointResponseTypeDef(BaseValidatorModel):
    DesiredModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectKeyPhrasesItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    KeyPhrases: Optional[List[KeyPhraseTypeDef]] = None

class DetectKeyPhrasesResponseTypeDef(BaseValidatorModel):
    KeyPhrases: List[KeyPhraseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSentimentItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScoreTypeDef] = None

class DetectSentimentResponseTypeDef(BaseValidatorModel):
    Sentiment: SentimentTypeType
    SentimentScore: SentimentScoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MentionSentimentTypeDef(BaseValidatorModel):
    Sentiment: Optional[SentimentTypeType] = None
    SentimentScore: Optional[SentimentScoreTypeDef] = None

class BlockReferenceTypeDef(BaseValidatorModel):
    BlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    ChildBlocks: Optional[List[ChildBlockTypeDef]] = None

class ClassifierMetadataTypeDef(BaseValidatorModel):
    NumberOfLabels: Optional[int] = None
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[ClassifierEvaluationMetricsTypeDef] = None

class ClassifyDocumentRequestRequestTypeDef(BaseValidatorModel):
    EndpointArn: str
    Text: Optional[str] = None
    Bytes: Optional[BlobTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class DetectEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    EndpointArn: Optional[str] = None
    Bytes: Optional[BlobTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class InputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class ContainsPiiEntitiesResponseTypeDef(BaseValidatorModel):
    Labels: List[EntityLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    DesiredInferenceUnits: int
    ModelArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None

class ImportModelRequestRequestTypeDef(BaseValidatorModel):
    SourceModelArn: str
    ModelName: Optional[str] = None
    VersionName: Optional[str] = None
    ModelKmsKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class DataSecurityConfigTypeDef(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    DataLakeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class UpdateDataSecurityConfigTypeDef(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None

class DatasetEntityRecognizerInputDataConfigTypeDef(BaseValidatorModel):
    Documents: DatasetEntityRecognizerDocumentsTypeDef
    Annotations: Optional[DatasetEntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[DatasetEntityRecognizerEntityListTypeDef] = None

class DatasetFilterTypeDef(BaseValidatorModel):
    Status: Optional[DatasetStatusType] = None
    DatasetType: Optional[DatasetTypeType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None

class DocumentClassificationJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class DocumentClassifierFilterTypeDef(BaseValidatorModel):
    Status: Optional[ModelStatusType] = None
    DocumentClassifierName: Optional[str] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class DominantLanguageDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class EndpointFilterTypeDef(BaseValidatorModel):
    ModelArn: Optional[str] = None
    Status: Optional[EndpointStatusType] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None

class EntitiesDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class EntityRecognizerFilterTypeDef(BaseValidatorModel):
    Status: Optional[ModelStatusType] = None
    RecognizerName: Optional[str] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class EventsDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class FlywheelFilterTypeDef(BaseValidatorModel):
    Status: Optional[FlywheelStatusType] = None
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None

class FlywheelIterationFilterTypeDef(BaseValidatorModel):
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None

class KeyPhrasesDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class PiiEntitiesDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class SentimentDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class TargetedSentimentDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class TopicsDetectionJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    DatasetProperties: DatasetPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseValidatorModel):
    DatasetPropertiesList: List[DatasetPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointResponseTypeDef(BaseValidatorModel):
    EndpointProperties: EndpointPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointsResponseTypeDef(BaseValidatorModel):
    EndpointPropertiesList: List[EndpointPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectPiiEntitiesResponseTypeDef(BaseValidatorModel):
    Entities: List[PiiEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectToxicContentRequestRequestTypeDef(BaseValidatorModel):
    TextSegments: Sequence[TextSegmentTypeDef]
    LanguageCode: LanguageCodeType

class DocumentClassifierInputDataConfigTypeDef(BaseValidatorModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItemTypeDef]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocumentsTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None

class DocumentClassifierInputDataConfigPaginatorTypeDef(BaseValidatorModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemPaginatorTypeDef]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocumentsTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigPaginatorTypeDef] = None

class InputDataConfigPaginatorTypeDef(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigPaginatorTypeDef] = None

class ListDocumentClassifierSummariesResponseTypeDef(BaseValidatorModel):
    DocumentClassifierSummariesList: List[DocumentClassifierSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentMetadataTypeDef(BaseValidatorModel):
    Pages: Optional[int] = None
    ExtractedCharacters: Optional[List[ExtractedCharactersListItemTypeDef]] = None

class EntityRecognitionConfigTypeDef(BaseValidatorModel):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]

class EntityRecognizerInputDataConfigPaginatorTypeDef(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItemTypeDef]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocumentsTypeDef] = None
    Annotations: Optional[EntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[EntityRecognizerEntityListTypeDef] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemPaginatorTypeDef]] = None

class EntityRecognizerInputDataConfigTypeDef(BaseValidatorModel):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocumentsTypeDef] = None
    Annotations: Optional[EntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[EntityRecognizerEntityListTypeDef] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItemTypeDef]] = None

class EntityRecognizerMetadataEntityTypesListItemTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    EvaluationMetrics: Optional[EntityTypesEvaluationMetricsTypeDef] = None
    NumberOfTrainMentions: Optional[int] = None

class ListEntityRecognizerSummariesResponseTypeDef(BaseValidatorModel):
    EntityRecognizerSummariesList: List[EntityRecognizerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FlywheelIterationPropertiesTypeDef(BaseValidatorModel):
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

class ListFlywheelsResponseTypeDef(BaseValidatorModel):
    FlywheelSummaryList: List[FlywheelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None

class SyntaxTokenTypeDef(BaseValidatorModel):
    TokenId: Optional[int] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    PartOfSpeech: Optional[PartOfSpeechTagTypeDef] = None

class ToxicLabelsTypeDef(BaseValidatorModel):
    Labels: Optional[List[ToxicContentTypeDef]] = None
    Toxicity: Optional[float] = None

class BatchDetectDominantLanguageResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectDominantLanguageItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectKeyPhrasesResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectKeyPhrasesItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSentimentResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetedSentimentMentionTypeDef(BaseValidatorModel):
    Score: Optional[float] = None
    GroupScore: Optional[float] = None
    Text: Optional[str] = None
    Type: Optional[TargetedSentimentEntityTypeType] = None
    MentionSentiment: Optional[MentionSentimentTypeDef] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None

class EntityTypeDef(BaseValidatorModel):
    Score: Optional[float] = None
    Type: Optional[EntityTypeType] = None
    Text: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    BlockReferences: Optional[List[BlockReferenceTypeDef]] = None

class DocumentClassificationJobPropertiesTypeDef(BaseValidatorModel):
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

class DominantLanguageDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class EntitiesDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class EventsDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class KeyPhrasesDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class PiiEntitiesDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class SentimentDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class StartDocumentClassificationJobRequestRequestTypeDef(BaseValidatorModel):
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

class StartDominantLanguageDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartEntitiesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
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

class StartEventsDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    TargetEventTypes: Sequence[str]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartKeyPhrasesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartPiiEntitiesDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    Mode: PiiEntitiesDetectionModeType
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    RedactionConfig: Optional[RedactionConfigTypeDef] = None
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartSentimentDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartTargetedSentimentDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartTopicsDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    NumberOfTopics: Optional[int] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TargetedSentimentDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class TopicsDetectionJobPropertiesTypeDef(BaseValidatorModel):
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

class UpdateFlywheelRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    DataSecurityConfig: Optional[UpdateDataSecurityConfigTypeDef] = None

class DatasetInputDataConfigTypeDef(BaseValidatorModel):
    AugmentedManifests: Optional[Sequence[DatasetAugmentedManifestsListItemTypeDef]] = None
    DataFormat: Optional[DatasetDataFormatType] = None
    DocumentClassifierInputDataConfig: Optional[       DatasetDocumentClassifierInputDataConfigTypeDef     ] = None
    EntityRecognizerInputDataConfig: Optional[       DatasetEntityRecognizerInputDataConfigTypeDef     ] = None

class ListDatasetsRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    Filter: Optional[DatasetFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDocumentClassificationJobsRequestListDocumentClassificationJobsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentClassificationJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDocumentClassifiersRequestListDocumentClassifiersPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentClassifiersRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDominantLanguageDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEndpointsRequestListEndpointsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[EndpointFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EndpointFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntitiesDetectionJobsRequestListEntitiesDetectionJobsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitiesDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEntityRecognizersRequestListEntityRecognizersPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntityRecognizersRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventsDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EventsDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFlywheelsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[FlywheelFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFlywheelIterationHistoryRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    Filter: Optional[FlywheelIterationFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListKeyPhrasesDetectionJobsRequestListKeyPhrasesDetectionJobsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyPhrasesDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPiiEntitiesDetectionJobsRequestListPiiEntitiesDetectionJobsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPiiEntitiesDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSentimentDetectionJobsRequestListSentimentDetectionJobsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSentimentDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTargetedSentimentDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[TargetedSentimentDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTopicsDetectionJobsRequestListTopicsDetectionJobsPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicsDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class CreateDocumentClassifierRequestRequestTypeDef(BaseValidatorModel):
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

class DocumentClassifierPropertiesTypeDef(BaseValidatorModel):
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

class DocumentClassifierPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class DocumentClassificationJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class DominantLanguageDetectionJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class EntitiesDetectionJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class KeyPhrasesDetectionJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class PiiEntitiesDetectionJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class SentimentDetectionJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class TopicsDetectionJobPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class ClassifyDocumentResponseTypeDef(BaseValidatorModel):
    Classes: List[DocumentClassTypeDef]
    Labels: List[DocumentLabelTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    Warnings: List[WarningsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaskConfigTypeDef(BaseValidatorModel):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: Optional[DocumentClassificationConfigTypeDef] = None
    EntityRecognitionConfig: Optional[EntityRecognitionConfigTypeDef] = None

class CreateEntityRecognizerRequestRequestTypeDef(BaseValidatorModel):
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

class EntityRecognizerMetadataTypeDef(BaseValidatorModel):
    NumberOfTrainedDocuments: Optional[int] = None
    NumberOfTestDocuments: Optional[int] = None
    EvaluationMetrics: Optional[EntityRecognizerEvaluationMetricsTypeDef] = None
    EntityTypes: Optional[List[EntityRecognizerMetadataEntityTypesListItemTypeDef]] = None

class DescribeFlywheelIterationResponseTypeDef(BaseValidatorModel):
    FlywheelIterationProperties: FlywheelIterationPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlywheelIterationHistoryResponseTypeDef(BaseValidatorModel):
    FlywheelIterationPropertiesList: List[FlywheelIterationPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BlockTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    BlockType: Optional[BlockTypeType] = None
    Text: Optional[str] = None
    Page: Optional[int] = None
    Geometry: Optional[GeometryTypeDef] = None
    Relationships: Optional[List[RelationshipsListItemTypeDef]] = None

class BatchDetectSyntaxItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    SyntaxTokens: Optional[List[SyntaxTokenTypeDef]] = None

class DetectSyntaxResponseTypeDef(BaseValidatorModel):
    SyntaxTokens: List[SyntaxTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectToxicContentResponseTypeDef(BaseValidatorModel):
    ResultList: List[ToxicLabelsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetedSentimentEntityTypeDef(BaseValidatorModel):
    DescriptiveMentionIndex: Optional[List[int]] = None
    Mentions: Optional[List[TargetedSentimentMentionTypeDef]] = None

class BatchDetectEntitiesItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[EntityTypeDef]] = None

class DescribeDocumentClassificationJobResponseTypeDef(BaseValidatorModel):
    DocumentClassificationJobProperties: DocumentClassificationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassificationJobsResponseTypeDef(BaseValidatorModel):
    DocumentClassificationJobPropertiesList: List[DocumentClassificationJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDominantLanguageDetectionJobResponseTypeDef(BaseValidatorModel):
    DominantLanguageDetectionJobProperties: DominantLanguageDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDominantLanguageDetectionJobsResponseTypeDef(BaseValidatorModel):
    DominantLanguageDetectionJobPropertiesList: List[       DominantLanguageDetectionJobPropertiesTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    EntitiesDetectionJobProperties: EntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionJobsResponseTypeDef(BaseValidatorModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsDetectionJobResponseTypeDef(BaseValidatorModel):
    EventsDetectionJobProperties: EventsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventsDetectionJobsResponseTypeDef(BaseValidatorModel):
    EventsDetectionJobPropertiesList: List[EventsDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyPhrasesDetectionJobResponseTypeDef(BaseValidatorModel):
    KeyPhrasesDetectionJobProperties: KeyPhrasesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPhrasesDetectionJobsResponseTypeDef(BaseValidatorModel):
    KeyPhrasesDetectionJobPropertiesList: List[KeyPhrasesDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePiiEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    PiiEntitiesDetectionJobProperties: PiiEntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPiiEntitiesDetectionJobsResponseTypeDef(BaseValidatorModel):
    PiiEntitiesDetectionJobPropertiesList: List[PiiEntitiesDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    SentimentDetectionJobProperties: SentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSentimentDetectionJobsResponseTypeDef(BaseValidatorModel):
    SentimentDetectionJobPropertiesList: List[SentimentDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTargetedSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    TargetedSentimentDetectionJobProperties: TargetedSentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetedSentimentDetectionJobsResponseTypeDef(BaseValidatorModel):
    TargetedSentimentDetectionJobPropertiesList: List[       TargetedSentimentDetectionJobPropertiesTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTopicsDetectionJobResponseTypeDef(BaseValidatorModel):
    TopicsDetectionJobProperties: TopicsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicsDetectionJobsResponseTypeDef(BaseValidatorModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    DatasetName: str
    InputDataConfig: DatasetInputDataConfigTypeDef
    DatasetType: Optional[DatasetTypeType] = None
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeDocumentClassifierResponseTypeDef(BaseValidatorModel):
    DocumentClassifierProperties: DocumentClassifierPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassifiersResponseTypeDef(BaseValidatorModel):
    DocumentClassifierPropertiesList: List[DocumentClassifierPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassifiersResponsePaginatorTypeDef(BaseValidatorModel):
    DocumentClassifierPropertiesList: List[DocumentClassifierPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassificationJobsResponsePaginatorTypeDef(BaseValidatorModel):
    DocumentClassificationJobPropertiesList: List[       DocumentClassificationJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDominantLanguageDetectionJobsResponsePaginatorTypeDef(BaseValidatorModel):
    DominantLanguageDetectionJobPropertiesList: List[       DominantLanguageDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionJobsResponsePaginatorTypeDef(BaseValidatorModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPhrasesDetectionJobsResponsePaginatorTypeDef(BaseValidatorModel):
    KeyPhrasesDetectionJobPropertiesList: List[       KeyPhrasesDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPiiEntitiesDetectionJobsResponsePaginatorTypeDef(BaseValidatorModel):
    PiiEntitiesDetectionJobPropertiesList: List[       PiiEntitiesDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSentimentDetectionJobsResponsePaginatorTypeDef(BaseValidatorModel):
    SentimentDetectionJobPropertiesList: List[       SentimentDetectionJobPropertiesPaginatorTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicsDetectionJobsResponsePaginatorTypeDef(BaseValidatorModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlywheelRequestRequestTypeDef(BaseValidatorModel):
    FlywheelName: str
    DataAccessRoleArn: str
    DataLakeS3Uri: str
    ActiveModelArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigTypeDef] = None
    ModelType: Optional[ModelTypeType] = None
    DataSecurityConfig: Optional[DataSecurityConfigTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class FlywheelPropertiesTypeDef(BaseValidatorModel):
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

class EntityRecognizerPropertiesPaginatorTypeDef(BaseValidatorModel):
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

class EntityRecognizerPropertiesTypeDef(BaseValidatorModel):
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

class DetectEntitiesResponseTypeDef(BaseValidatorModel):
    Entities: List[EntityTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Blocks: List[BlockTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSyntaxResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectSyntaxItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectTargetedSentimentItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[TargetedSentimentEntityTypeDef]] = None

class DetectTargetedSentimentResponseTypeDef(BaseValidatorModel):
    Entities: List[TargetedSentimentEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectEntitiesResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectEntitiesItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlywheelResponseTypeDef(BaseValidatorModel):
    FlywheelProperties: FlywheelPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlywheelResponseTypeDef(BaseValidatorModel):
    FlywheelProperties: FlywheelPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntityRecognizersResponsePaginatorTypeDef(BaseValidatorModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerPropertiesPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityRecognizerResponseTypeDef(BaseValidatorModel):
    EntityRecognizerProperties: EntityRecognizerPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntityRecognizersResponseTypeDef(BaseValidatorModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectTargetedSentimentResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectTargetedSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

