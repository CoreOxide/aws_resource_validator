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
from aws_resource_validator.pydantic_models.textract_constants import *

class AdapterOverviewTypeDef(BaseModel):
    AdapterId: Optional[str] = None
    AdapterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None

class AdapterTypeDef(BaseModel):
    AdapterId: str
    Version: str
    Pages: Optional[Sequence[str]] = None

class S3ObjectTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None

class EvaluationMetricTypeDef(BaseModel):
    F1Score: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None

class AdapterVersionOverviewTypeDef(BaseModel):
    AdapterId: Optional[str] = None
    AdapterVersion: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None
    Status: Optional[AdapterVersionStatusType] = None
    StatusMessage: Optional[str] = None

class DocumentMetadataTypeDef(BaseModel):
    Pages: Optional[int] = None

class HumanLoopActivationOutputTypeDef(BaseModel):
    HumanLoopArn: Optional[str] = None
    HumanLoopActivationReasons: Optional[List[str]] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class NormalizedValueTypeDef(BaseModel):
    Value: Optional[str] = None
    ValueType: Optional[Literal["DATE"]] = None

class QueryTypeDef(BaseModel):
    Text: str
    Alias: Optional[str] = None
    Pages: Optional[Sequence[str]] = None

class RelationshipTypeDef(BaseModel):
    Type: Optional[RelationshipTypeType] = None
    Ids: Optional[List[str]] = None

class BoundingBoxTypeDef(BaseModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None

class CreateAdapterRequestRequestTypeDef(BaseModel):
    AdapterName: str
    FeatureTypes: Sequence[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None
    Tags: Optional[Mapping[str, str]] = None

class OutputConfigTypeDef(BaseModel):
    S3Bucket: str
    S3Prefix: Optional[str] = None

class DeleteAdapterRequestRequestTypeDef(BaseModel):
    AdapterId: str

class DeleteAdapterVersionRequestRequestTypeDef(BaseModel):
    AdapterId: str
    AdapterVersion: str

class DetectedSignatureTypeDef(BaseModel):
    Page: Optional[int] = None

class SplitDocumentTypeDef(BaseModel):
    Index: Optional[int] = None
    Pages: Optional[List[int]] = None

class UndetectedSignatureTypeDef(BaseModel):
    Page: Optional[int] = None

class ExpenseCurrencyTypeDef(BaseModel):
    Code: Optional[str] = None
    Confidence: Optional[float] = None

class ExpenseGroupPropertyTypeDef(BaseModel):
    Types: Optional[List[str]] = None
    Id: Optional[str] = None

class ExpenseTypeTypeDef(BaseModel):
    Text: Optional[str] = None
    Confidence: Optional[float] = None

class PointTypeDef(BaseModel):
    X: Optional[float] = None
    Y: Optional[float] = None

class GetAdapterRequestRequestTypeDef(BaseModel):
    AdapterId: str

class GetAdapterVersionRequestRequestTypeDef(BaseModel):
    AdapterId: str
    AdapterVersion: str

class GetDocumentAnalysisRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class WarningTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    Pages: Optional[List[int]] = None

class GetDocumentTextDetectionRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetExpenseAnalysisRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetLendingAnalysisRequestRequestTypeDef(BaseModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetLendingAnalysisSummaryRequestRequestTypeDef(BaseModel):
    JobId: str

class HumanLoopDataAttributesTypeDef(BaseModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class NotificationChannelTypeDef(BaseModel):
    SNSTopicArn: str
    RoleArn: str

class PredictionTypeDef(BaseModel):
    Value: Optional[str] = None
    Confidence: Optional[float] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAdapterRequestRequestTypeDef(BaseModel):
    AdapterId: str
    Description: Optional[str] = None
    AdapterName: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None

class AdaptersConfigTypeDef(BaseModel):
    Adapters: Sequence[AdapterTypeDef]

class AdapterVersionDatasetConfigTypeDef(BaseModel):
    ManifestS3Object: Optional[S3ObjectTypeDef] = None

class DocumentLocationTypeDef(BaseModel):
    S3Object: Optional[S3ObjectTypeDef] = None

class AdapterVersionEvaluationMetricTypeDef(BaseModel):
    Baseline: Optional[EvaluationMetricTypeDef] = None
    AdapterVersion: Optional[EvaluationMetricTypeDef] = None
    FeatureType: Optional[FeatureTypeType] = None

class CreateAdapterResponseTypeDef(BaseModel):
    AdapterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAdapterVersionResponseTypeDef(BaseModel):
    AdapterId: str
    AdapterVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdapterResponseTypeDef(BaseModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAdapterVersionsResponseTypeDef(BaseModel):
    AdapterVersions: List[AdapterVersionOverviewTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAdaptersResponseTypeDef(BaseModel):
    Adapters: List[AdapterOverviewTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDocumentAnalysisResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDocumentTextDetectionResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExpenseAnalysisResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLendingAnalysisResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAdapterResponseTypeDef(BaseModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    ResponseMetadata: ResponseMetadataTypeDef

class AnalyzeIDDetectionsTypeDef(BaseModel):
    Text: str
    NormalizedValue: Optional[NormalizedValueTypeDef] = None
    Confidence: Optional[float] = None

class DocumentTypeDef(BaseModel):
    Bytes: Optional[BlobTypeDef] = None
    S3Object: Optional[S3ObjectTypeDef] = None

class QueriesConfigTypeDef(BaseModel):
    Queries: Sequence[QueryTypeDef]

class DocumentGroupTypeDef(BaseModel):
    Type: Optional[str] = None
    SplitDocuments: Optional[List[SplitDocumentTypeDef]] = None
    DetectedSignatures: Optional[List[DetectedSignatureTypeDef]] = None
    UndetectedSignatures: Optional[List[UndetectedSignatureTypeDef]] = None

class GeometryTypeDef(BaseModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None

class HumanLoopConfigTypeDef(BaseModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None

class ListAdapterVersionsRequestListAdapterVersionsPaginateTypeDef(BaseModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAdapterVersionsRequestRequestTypeDef(BaseModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAdaptersRequestListAdaptersPaginateTypeDef(BaseModel):
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAdaptersRequestRequestTypeDef(BaseModel):
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PageClassificationTypeDef(BaseModel):
    PageType: List[PredictionTypeDef]
    PageNumber: List[PredictionTypeDef]

class CreateAdapterVersionRequestRequestTypeDef(BaseModel):
    AdapterId: str
    DatasetConfig: AdapterVersionDatasetConfigTypeDef
    OutputConfig: OutputConfigTypeDef
    ClientRequestToken: Optional[str] = None
    KMSKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class StartDocumentTextDetectionRequestRequestTypeDef(BaseModel):
    DocumentLocation: DocumentLocationTypeDef
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None

class StartExpenseAnalysisRequestRequestTypeDef(BaseModel):
    DocumentLocation: DocumentLocationTypeDef
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None

class StartLendingAnalysisRequestRequestTypeDef(BaseModel):
    DocumentLocation: DocumentLocationTypeDef
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None

class GetAdapterVersionResponseTypeDef(BaseModel):
    AdapterId: str
    AdapterVersion: str
    CreationTime: datetime
    FeatureTypes: List[FeatureTypeType]
    Status: AdapterVersionStatusType
    StatusMessage: str
    DatasetConfig: AdapterVersionDatasetConfigTypeDef
    KMSKeyId: str
    OutputConfig: OutputConfigTypeDef
    EvaluationMetrics: List[AdapterVersionEvaluationMetricTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class IdentityDocumentFieldTypeDef(BaseModel):
    Type: Optional[AnalyzeIDDetectionsTypeDef] = None
    ValueDetection: Optional[AnalyzeIDDetectionsTypeDef] = None

class AnalyzeExpenseRequestRequestTypeDef(BaseModel):
    Document: DocumentTypeDef

class AnalyzeIDRequestRequestTypeDef(BaseModel):
    DocumentPages: Sequence[DocumentTypeDef]

class DetectDocumentTextRequestRequestTypeDef(BaseModel):
    Document: DocumentTypeDef

class StartDocumentAnalysisRequestRequestTypeDef(BaseModel):
    DocumentLocation: DocumentLocationTypeDef
    FeatureTypes: Sequence[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None
    QueriesConfig: Optional[QueriesConfigTypeDef] = None
    AdaptersConfig: Optional[AdaptersConfigTypeDef] = None

class LendingSummaryTypeDef(BaseModel):
    DocumentGroups: Optional[List[DocumentGroupTypeDef]] = None
    UndetectedDocumentTypes: Optional[List[str]] = None

class BlockTypeDef(BaseModel):
    BlockType: Optional[BlockTypeType] = None
    Confidence: Optional[float] = None
    Text: Optional[str] = None
    TextType: Optional[TextTypeType] = None
    RowIndex: Optional[int] = None
    ColumnIndex: Optional[int] = None
    RowSpan: Optional[int] = None
    ColumnSpan: Optional[int] = None
    Geometry: Optional[GeometryTypeDef] = None
    Id: Optional[str] = None
    Relationships: Optional[List[RelationshipTypeDef]] = None
    EntityTypes: Optional[List[EntityTypeType]] = None
    SelectionStatus: Optional[SelectionStatusType] = None
    Page: Optional[int] = None
    Query: Optional[QueryTypeDef] = None

class ExpenseDetectionTypeDef(BaseModel):
    Text: Optional[str] = None
    Geometry: Optional[GeometryTypeDef] = None
    Confidence: Optional[float] = None

class LendingDetectionTypeDef(BaseModel):
    Text: Optional[str] = None
    SelectionStatus: Optional[SelectionStatusType] = None
    Geometry: Optional[GeometryTypeDef] = None
    Confidence: Optional[float] = None

class SignatureDetectionTypeDef(BaseModel):
    Confidence: Optional[float] = None
    Geometry: Optional[GeometryTypeDef] = None

class AnalyzeDocumentRequestRequestTypeDef(BaseModel):
    Document: DocumentTypeDef
    FeatureTypes: Sequence[FeatureTypeType]
    HumanLoopConfig: Optional[HumanLoopConfigTypeDef] = None
    QueriesConfig: Optional[QueriesConfigTypeDef] = None
    AdaptersConfig: Optional[AdaptersConfigTypeDef] = None

class GetLendingAnalysisSummaryResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    Summary: LendingSummaryTypeDef
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class AnalyzeDocumentResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    Blocks: List[BlockTypeDef]
    HumanLoopActivationOutput: HumanLoopActivationOutputTypeDef
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectDocumentTextResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    Blocks: List[BlockTypeDef]
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentAnalysisResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    NextToken: str
    Blocks: List[BlockTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentTextDetectionResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    NextToken: str
    Blocks: List[BlockTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class IdentityDocumentTypeDef(BaseModel):
    DocumentIndex: Optional[int] = None
    IdentityDocumentFields: Optional[List[IdentityDocumentFieldTypeDef]] = None
    Blocks: Optional[List[BlockTypeDef]] = None

class ExpenseFieldTypeDef(BaseModel):
    Type: Optional[ExpenseTypeTypeDef] = None
    LabelDetection: Optional[ExpenseDetectionTypeDef] = None
    ValueDetection: Optional[ExpenseDetectionTypeDef] = None
    PageNumber: Optional[int] = None
    Currency: Optional[ExpenseCurrencyTypeDef] = None
    GroupProperties: Optional[List[ExpenseGroupPropertyTypeDef]] = None

class LendingFieldTypeDef(BaseModel):
    Type: Optional[str] = None
    KeyDetection: Optional[LendingDetectionTypeDef] = None
    ValueDetections: Optional[List[LendingDetectionTypeDef]] = None

class AnalyzeIDResponseTypeDef(BaseModel):
    IdentityDocuments: List[IdentityDocumentTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    AnalyzeIDModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class LineItemFieldsTypeDef(BaseModel):
    LineItemExpenseFields: Optional[List[ExpenseFieldTypeDef]] = None

class LendingDocumentTypeDef(BaseModel):
    LendingFields: Optional[List[LendingFieldTypeDef]] = None
    SignatureDetections: Optional[List[SignatureDetectionTypeDef]] = None

class LineItemGroupTypeDef(BaseModel):
    LineItemGroupIndex: Optional[int] = None
    LineItems: Optional[List[LineItemFieldsTypeDef]] = None

class ExpenseDocumentTypeDef(BaseModel):
    ExpenseIndex: Optional[int] = None
    SummaryFields: Optional[List[ExpenseFieldTypeDef]] = None
    LineItemGroups: Optional[List[LineItemGroupTypeDef]] = None
    Blocks: Optional[List[BlockTypeDef]] = None

class AnalyzeExpenseResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    ExpenseDocuments: List[ExpenseDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExtractionTypeDef(BaseModel):
    LendingDocument: Optional[LendingDocumentTypeDef] = None
    ExpenseDocument: Optional[ExpenseDocumentTypeDef] = None
    IdentityDocument: Optional[IdentityDocumentTypeDef] = None

class GetExpenseAnalysisResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    NextToken: str
    ExpenseDocuments: List[ExpenseDocumentTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeExpenseModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class LendingResultTypeDef(BaseModel):
    Page: Optional[int] = None
    PageClassification: Optional[PageClassificationTypeDef] = None
    Extractions: Optional[List[ExtractionTypeDef]] = None

class GetLendingAnalysisResponseTypeDef(BaseModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    NextToken: str
    Results: List[LendingResultTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

