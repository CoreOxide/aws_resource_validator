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

class AugmentedManifestsListItemOutputTypeDef(BaseValidatorModel):
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


class BatchDetectDominantLanguageRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]


class BatchItemErrorTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDetectEntitiesRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class BatchDetectKeyPhrasesRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class SentimentScoreTypeDef(BaseValidatorModel):
    Positive: Optional[float] = None
    Negative: Optional[float] = None
    Neutral: Optional[float] = None
    Mixed: Optional[float] = None


class BatchDetectSentimentRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class BatchDetectSyntaxRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: SyntaxLanguageCodeType


class BatchDetectTargetedSentimentRequestTypeDef(BaseValidatorModel):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType


class ChildBlockTypeDef(BaseValidatorModel):
    ChildBlockId: Optional[str] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None


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


class DocumentClassTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None


class DocumentLabelTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Score: Optional[float] = None
    Page: Optional[int] = None


class ErrorsListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    ErrorCode: Optional[PageBasedErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class WarningsListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    WarnCode: Optional[PageBasedWarningCodeType] = None
    WarnMessage: Optional[str] = None


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


class VpcConfigOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    Subnets: List[str]


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


class DeleteDocumentClassifierRequestTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str


class DeleteEndpointRequestTypeDef(BaseValidatorModel):
    EndpointArn: str


class DeleteEntityRecognizerRequestTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str


class DeleteFlywheelRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    PolicyRevisionId: Optional[str] = None


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    DatasetArn: str


class DescribeDocumentClassificationJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeDocumentClassifierRequestTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str


class DescribeDominantLanguageDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeEndpointRequestTypeDef(BaseValidatorModel):
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


class DescribeEntitiesDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeEntityRecognizerRequestTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str


class DescribeEventsDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeFlywheelIterationRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    FlywheelIterationId: str


class DescribeFlywheelRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str


class DescribeKeyPhrasesDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribePiiEntitiesDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DescribeSentimentDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeTargetedSentimentDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeTopicsDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DocumentClassificationConfigOutputTypeDef(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[List[str]] = None


class DocumentClassificationConfigTypeDef(BaseValidatorModel):
    Mode: DocumentClassifierModeType
    Labels: Optional[Sequence[str]] = None


class OutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class DocumentClassifierDocumentsTypeDef(BaseValidatorModel):
    S3Uri: str
    TestS3Uri: Optional[str] = None


class DocumentReaderConfigOutputTypeDef(BaseValidatorModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[List[DocumentReadFeatureTypesType]] = None


class DocumentReaderConfigTypeDef(BaseValidatorModel):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: Optional[DocumentReadModeType] = None
    FeatureTypes: Optional[Sequence[DocumentReadFeatureTypesType]] = None


class DocumentClassifierSummaryTypeDef(BaseValidatorModel):
    DocumentClassifierName: Optional[str] = None
    NumberOfVersions: Optional[int] = None
    LatestVersionCreatedAt: Optional[datetime] = None
    LatestVersionName: Optional[str] = None
    LatestVersionStatus: Optional[ModelStatusType] = None


class ExtractedCharactersListItemTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    Count: Optional[int] = None


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


class ListDocumentClassifierSummariesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntityRecognizerSummariesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PartOfSpeechTagTypeDef(BaseValidatorModel):
    Tag: Optional[PartOfSpeechTagTypeType] = None
    Score: Optional[float] = None


class PiiOutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class RedactionConfigOutputTypeDef(BaseValidatorModel):
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    PolicyRevisionId: Optional[str] = None


class RedactionConfigTypeDef(BaseValidatorModel):
    PiiEntityTypes: Optional[Sequence[PiiEntityTypeType]] = None
    MaskMode: Optional[PiiEntitiesDetectionMaskModeType] = None
    MaskCharacter: Optional[str] = None


class StartFlywheelIterationRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    ClientRequestToken: Optional[str] = None


class StopDominantLanguageDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopEntitiesDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopEventsDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopKeyPhrasesDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopPiiEntitiesDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopSentimentDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopTargetedSentimentDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopTrainingDocumentClassifierRequestTypeDef(BaseValidatorModel):
    DocumentClassifierArn: str


class StopTrainingEntityRecognizerRequestTypeDef(BaseValidatorModel):
    EntityRecognizerArn: str


class ToxicContentTypeDef(BaseValidatorModel):
    Name: Optional[ToxicContentTypeType] = None
    Score: Optional[float] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateEndpointRequestTypeDef(BaseValidatorModel):
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


class KeyPhraseTypeDef(BaseValidatorModel):
    pass


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


class ContainsPiiEntitiesResponseTypeDef(BaseValidatorModel):
    Labels: List[EntityLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    DesiredInferenceUnits: int
    ModelArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class ImportModelRequestTypeDef(BaseValidatorModel):
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


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class DataSecurityConfigOutputTypeDef(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    DataLakeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None


class DataSecurityConfigTypeDef(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    DataLakeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None


class DatasetEntityRecognizerInputDataConfigTypeDef(BaseValidatorModel):
    Documents: DatasetEntityRecognizerDocumentsTypeDef
    Annotations: Optional[DatasetEntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[DatasetEntityRecognizerEntityListTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeEndpointResponseTypeDef(BaseValidatorModel):
    EndpointProperties: EndpointPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEndpointsResponseTypeDef(BaseValidatorModel):
    EndpointPropertiesList: List[EndpointPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PiiEntityTypeDef(BaseValidatorModel):
    pass


class DetectPiiEntitiesResponseTypeDef(BaseValidatorModel):
    Entities: List[PiiEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TextSegmentTypeDef(BaseValidatorModel):
    pass


class DetectToxicContentRequestTypeDef(BaseValidatorModel):
    TextSegments: Sequence[TextSegmentTypeDef]
    LanguageCode: LanguageCodeType


class DocumentClassifierInputDataConfigOutputTypeDef(BaseValidatorModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemOutputTypeDef]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocumentsTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigOutputTypeDef] = None


class InputDataConfigOutputTypeDef(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigOutputTypeDef] = None


class DocumentClassifierInputDataConfigTypeDef(BaseValidatorModel):
    DataFormat: Optional[DocumentClassifierDataFormatType] = None
    S3Uri: Optional[str] = None
    TestS3Uri: Optional[str] = None
    LabelDelimiter: Optional[str] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItemTypeDef]] = None
    DocumentType: Optional[DocumentClassifierDocumentTypeFormatType] = None
    Documents: Optional[DocumentClassifierDocumentsTypeDef] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None


class InputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    InputFormat: Optional[InputFormatType] = None
    DocumentReaderConfig: Optional[DocumentReaderConfigTypeDef] = None


class ListDocumentClassifierSummariesResponseTypeDef(BaseValidatorModel):
    DocumentClassifierSummariesList: List[DocumentClassifierSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DocumentMetadataTypeDef(BaseValidatorModel):
    Pages: Optional[int] = None
    ExtractedCharacters: Optional[List[ExtractedCharactersListItemTypeDef]] = None


class EntityTypesListItemTypeDef(BaseValidatorModel):
    pass


class EntityRecognitionConfigOutputTypeDef(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItemTypeDef]


class EntityRecognitionConfigTypeDef(BaseValidatorModel):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]


class EntityRecognizerInputDataConfigOutputTypeDef(BaseValidatorModel):
    EntityTypes: List[EntityTypesListItemTypeDef]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocumentsTypeDef] = None
    Annotations: Optional[EntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[EntityRecognizerEntityListTypeDef] = None
    AugmentedManifests: Optional[List[AugmentedManifestsListItemOutputTypeDef]] = None


class EntityRecognizerInputDataConfigTypeDef(BaseValidatorModel):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]
    DataFormat: Optional[EntityRecognizerDataFormatType] = None
    Documents: Optional[EntityRecognizerDocumentsTypeDef] = None
    Annotations: Optional[EntityRecognizerAnnotationsTypeDef] = None
    EntityList: Optional[EntityRecognizerEntityListTypeDef] = None
    AugmentedManifests: Optional[Sequence[AugmentedManifestsListItemTypeDef]] = None


class ListEntityRecognizerSummariesResponseTypeDef(BaseValidatorModel):
    EntityRecognizerSummariesList: List[EntityRecognizerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None


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


class VpcConfigUnionTypeDef(BaseValidatorModel):
    pass


class UpdateDataSecurityConfigTypeDef(BaseValidatorModel):
    ModelKmsKeyId: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None


class DatasetInputDataConfigTypeDef(BaseValidatorModel):
    AugmentedManifests: Optional[Sequence[DatasetAugmentedManifestsListItemTypeDef]] = None
    DataFormat: Optional[DatasetDataFormatType] = None
    DocumentClassifierInputDataConfig: Optional[DatasetDocumentClassifierInputDataConfigTypeDef] = None
    EntityRecognizerInputDataConfig: Optional[DatasetEntityRecognizerInputDataConfigTypeDef] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    Filter: Optional[DatasetFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentClassificationJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDocumentClassificationJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassificationJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentClassifiersRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDocumentClassifiersRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DocumentClassifierFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDominantLanguageDetectionJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDominantLanguageDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DominantLanguageDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[EndpointFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEndpointsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EndpointFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntitiesDetectionJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEntitiesDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EntitiesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEntityRecognizersRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEntityRecognizersRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EntityRecognizerFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventsDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[EventsDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFlywheelsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[FlywheelFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFlywheelIterationHistoryRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    Filter: Optional[FlywheelIterationFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListKeyPhrasesDetectionJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKeyPhrasesDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[KeyPhrasesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPiiEntitiesDetectionJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPiiEntitiesDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[PiiEntitiesDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSentimentDetectionJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSentimentDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[SentimentDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTargetedSentimentDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[TargetedSentimentDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTopicsDetectionJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTopicsDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[TopicsDetectionJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DocumentClassifierPropertiesTypeDef(BaseValidatorModel):
    DocumentClassifierArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[DocumentClassifierInputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfigTypeDef] = None
    ClassifierMetadata: Optional[ClassifierMetadataTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None


class DocumentClassificationJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    DocumentClassifierArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    FlywheelArn: Optional[str] = None


class DominantLanguageDetectionJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None


class EntitiesDetectionJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    EntityRecognizerArn: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    FlywheelArn: Optional[str] = None


class EventsDetectionJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
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
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None


class PiiEntitiesDetectionJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[PiiOutputDataConfigTypeDef] = None
    RedactionConfig: Optional[RedactionConfigOutputTypeDef] = None
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
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None


class TargetedSentimentDetectionJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None


class TopicsDetectionJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobArn: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigOutputTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    NumberOfTopics: Optional[int] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None


class DocumentTypeListItemTypeDef(BaseValidatorModel):
    pass


class ClassifyDocumentResponseTypeDef(BaseValidatorModel):
    Classes: List[DocumentClassTypeDef]
    Labels: List[DocumentLabelTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    Warnings: List[WarningsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TaskConfigOutputTypeDef(BaseValidatorModel):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: Optional[DocumentClassificationConfigOutputTypeDef] = None
    EntityRecognitionConfig: Optional[EntityRecognitionConfigOutputTypeDef] = None


class TaskConfigTypeDef(BaseValidatorModel):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: Optional[DocumentClassificationConfigTypeDef] = None
    EntityRecognitionConfig: Optional[EntityRecognitionConfigTypeDef] = None


class EntityRecognizerMetadataEntityTypesListItemTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SyntaxTokenTypeDef(BaseValidatorModel):
    pass


class BatchDetectSyntaxItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    SyntaxTokens: Optional[List[SyntaxTokenTypeDef]] = None


class DetectSyntaxResponseTypeDef(BaseValidatorModel):
    SyntaxTokens: List[SyntaxTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetectToxicContentResponseTypeDef(BaseValidatorModel):
    ResultList: List[ToxicLabelsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TargetedSentimentMentionTypeDef(BaseValidatorModel):
    pass


class TargetedSentimentEntityTypeDef(BaseValidatorModel):
    DescriptiveMentionIndex: Optional[List[int]] = None
    Mentions: Optional[List[TargetedSentimentMentionTypeDef]] = None


class EntityTypeDef(BaseValidatorModel):
    pass


class BatchDetectEntitiesItemResultTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Entities: Optional[List[EntityTypeDef]] = None


class UpdateFlywheelRequestTypeDef(BaseValidatorModel):
    FlywheelArn: str
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    DataSecurityConfig: Optional[UpdateDataSecurityConfigTypeDef] = None


class CreateDatasetRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeDocumentClassificationJobResponseTypeDef(BaseValidatorModel):
    DocumentClassificationJobProperties: DocumentClassificationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDocumentClassificationJobsResponseTypeDef(BaseValidatorModel):
    DocumentClassificationJobPropertiesList: List[DocumentClassificationJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeDominantLanguageDetectionJobResponseTypeDef(BaseValidatorModel):
    DominantLanguageDetectionJobProperties: DominantLanguageDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDominantLanguageDetectionJobsResponseTypeDef(BaseValidatorModel):
    DominantLanguageDetectionJobPropertiesList: List[DominantLanguageDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    EntitiesDetectionJobProperties: EntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEntitiesDetectionJobsResponseTypeDef(BaseValidatorModel):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeEventsDetectionJobResponseTypeDef(BaseValidatorModel):
    EventsDetectionJobProperties: EventsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEventsDetectionJobsResponseTypeDef(BaseValidatorModel):
    EventsDetectionJobPropertiesList: List[EventsDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeKeyPhrasesDetectionJobResponseTypeDef(BaseValidatorModel):
    KeyPhrasesDetectionJobProperties: KeyPhrasesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListKeyPhrasesDetectionJobsResponseTypeDef(BaseValidatorModel):
    KeyPhrasesDetectionJobPropertiesList: List[KeyPhrasesDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribePiiEntitiesDetectionJobResponseTypeDef(BaseValidatorModel):
    PiiEntitiesDetectionJobProperties: PiiEntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPiiEntitiesDetectionJobsResponseTypeDef(BaseValidatorModel):
    PiiEntitiesDetectionJobPropertiesList: List[PiiEntitiesDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    SentimentDetectionJobProperties: SentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSentimentDetectionJobsResponseTypeDef(BaseValidatorModel):
    SentimentDetectionJobPropertiesList: List[SentimentDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeTargetedSentimentDetectionJobResponseTypeDef(BaseValidatorModel):
    TargetedSentimentDetectionJobProperties: TargetedSentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTargetedSentimentDetectionJobsResponseTypeDef(BaseValidatorModel):
    TargetedSentimentDetectionJobPropertiesList: List[ TargetedSentimentDetectionJobPropertiesTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeTopicsDetectionJobResponseTypeDef(BaseValidatorModel):
    TopicsDetectionJobProperties: TopicsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTopicsDetectionJobsResponseTypeDef(BaseValidatorModel):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DocumentClassifierInputDataConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateDocumentClassifierRequestTypeDef(BaseValidatorModel):
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: DocumentClassifierInputDataConfigUnionTypeDef
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OutputDataConfig: Optional[DocumentClassifierOutputDataConfigTypeDef] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Mode: Optional[DocumentClassifierModeType] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None


class InputDataConfigUnionTypeDef(BaseValidatorModel):
    pass


class StartDocumentClassificationJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    DocumentClassifierArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FlywheelArn: Optional[str] = None


class StartDominantLanguageDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartEntitiesDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    EntityRecognizerArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    FlywheelArn: Optional[str] = None


class StartEventsDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    TargetEventTypes: Sequence[str]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartKeyPhrasesDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class RedactionConfigUnionTypeDef(BaseValidatorModel):
    pass


class StartPiiEntitiesDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    Mode: PiiEntitiesDetectionModeType
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    RedactionConfig: Optional[RedactionConfigUnionTypeDef] = None
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartSentimentDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartTargetedSentimentDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartTopicsDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: Optional[str] = None
    NumberOfTopics: Optional[int] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class FlywheelPropertiesTypeDef(BaseValidatorModel):
    FlywheelArn: Optional[str] = None
    ActiveModelArn: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigOutputTypeDef] = None
    DataLakeS3Uri: Optional[str] = None
    DataSecurityConfig: Optional[DataSecurityConfigOutputTypeDef] = None
    Status: Optional[FlywheelStatusType] = None
    ModelType: Optional[ModelTypeType] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LatestFlywheelIteration: Optional[str] = None


class EntityRecognizerInputDataConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateEntityRecognizerRequestTypeDef(BaseValidatorModel):
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: EntityRecognizerInputDataConfigUnionTypeDef
    LanguageCode: LanguageCodeType
    VersionName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnionTypeDef] = None
    ModelKmsKeyId: Optional[str] = None
    ModelPolicy: Optional[str] = None


class EntityRecognizerPropertiesTypeDef(BaseValidatorModel):
    EntityRecognizerArn: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Status: Optional[ModelStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TrainingStartTime: Optional[datetime] = None
    TrainingEndTime: Optional[datetime] = None
    InputDataConfig: Optional[EntityRecognizerInputDataConfigOutputTypeDef] = None
    RecognizerMetadata: Optional[EntityRecognizerMetadataTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    VolumeKmsKeyId: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    ModelKmsKeyId: Optional[str] = None
    VersionName: Optional[str] = None
    SourceModelArn: Optional[str] = None
    FlywheelArn: Optional[str] = None
    OutputDataConfig: Optional[EntityRecognizerOutputDataConfigTypeDef] = None


class BlockTypeDef(BaseValidatorModel):
    pass


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


class DataSecurityConfigUnionTypeDef(BaseValidatorModel):
    pass


class TaskConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateFlywheelRequestTypeDef(BaseValidatorModel):
    FlywheelName: str
    DataAccessRoleArn: str
    DataLakeS3Uri: str
    ActiveModelArn: Optional[str] = None
    TaskConfig: Optional[TaskConfigUnionTypeDef] = None
    ModelType: Optional[ModelTypeType] = None
    DataSecurityConfig: Optional[DataSecurityConfigUnionTypeDef] = None
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeEntityRecognizerResponseTypeDef(BaseValidatorModel):
    EntityRecognizerProperties: EntityRecognizerPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEntityRecognizersResponseTypeDef(BaseValidatorModel):
    EntityRecognizerPropertiesList: List[EntityRecognizerPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchDetectTargetedSentimentResponseTypeDef(BaseValidatorModel):
    ResultList: List[BatchDetectTargetedSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


