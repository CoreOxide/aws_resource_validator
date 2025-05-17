from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.textract.textract_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AdapterOverview(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AdapterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None


class Adapter(BaseValidatorModel):
    AdapterId: str
    Version: str
    Pages: Optional[List[str]] = None


class S3Object(BaseValidatorModel):
    Bucket: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None


class EvaluationMetric(BaseValidatorModel):
    F1Score: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None


class AdapterVersionOverview(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AdapterVersion: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None
    Status: Optional[AdapterVersionStatusType] = None
    StatusMessage: Optional[str] = None


class DocumentMetadata(BaseValidatorModel):
    Pages: Optional[int] = None


class HumanLoopActivationOutput(BaseValidatorModel):
    HumanLoopArn: Optional[str] = None
    HumanLoopActivationReasons: Optional[List[str]] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class NormalizedValue(BaseValidatorModel):
    Value: Optional[str] = None
    ValueType: Optional[Literal['DATE']] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class QueryOutput(BaseValidatorModel):
    Text: str
    Alias: Optional[str] = None
    Pages: Optional[List[str]] = None


class Relationship(BaseValidatorModel):
    Type: Optional[RelationshipTypeType] = None
    Ids: Optional[List[str]] = None


class BoundingBox(BaseValidatorModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None


# This class is the input for the 'create_adapter' function.
class CreateAdapterRequest(BaseValidatorModel):
    AdapterName: str
    FeatureTypes: List[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None
    Tags: Optional[Dict[str, str]] = None


class OutputConfig(BaseValidatorModel):
    S3Bucket: str
    S3Prefix: Optional[str] = None


class DeleteAdapterRequest(BaseValidatorModel):
    AdapterId: str


class DeleteAdapterVersionRequest(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str


class DetectedSignature(BaseValidatorModel):
    Page: Optional[int] = None


class SplitDocument(BaseValidatorModel):
    Index: Optional[int] = None
    Pages: Optional[List[int]] = None


class UndetectedSignature(BaseValidatorModel):
    Page: Optional[int] = None


class ExpenseCurrency(BaseValidatorModel):
    Code: Optional[str] = None
    Confidence: Optional[float] = None


class ExpenseGroupProperty(BaseValidatorModel):
    Types: Optional[List[str]] = None
    Id: Optional[str] = None


class ExpenseType(BaseValidatorModel):
    Text: Optional[str] = None
    Confidence: Optional[float] = None


class Point(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None


# This class is the input for the 'get_adapter' function.
class GetAdapterRequest(BaseValidatorModel):
    AdapterId: str


# This class is the input for the 'get_adapter_version' function.
class GetAdapterVersionRequest(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str


# This class is the input for the 'get_document_analysis' function.
class GetDocumentAnalysisRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Warning(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Pages: Optional[List[int]] = None


# This class is the input for the 'get_document_text_detection' function.
class GetDocumentTextDetectionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_expense_analysis' function.
class GetExpenseAnalysisRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_lending_analysis' function.
class GetLendingAnalysisRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_lending_analysis_summary' function.
class GetLendingAnalysisSummaryRequest(BaseValidatorModel):
    JobId: str


class HumanLoopDataAttributes(BaseValidatorModel):
    ContentClassifiers: Optional[List[ContentClassifierType]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class NotificationChannel(BaseValidatorModel):
    SNSTopicArn: str
    RoleArn: str


class Prediction(BaseValidatorModel):
    Value: Optional[str] = None
    Confidence: Optional[float] = None


class Query(BaseValidatorModel):
    Text: str
    Alias: Optional[str] = None
    Pages: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_adapter' function.
class UpdateAdapterRequest(BaseValidatorModel):
    AdapterId: str
    Description: Optional[str] = None
    AdapterName: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None


class AdaptersConfig(BaseValidatorModel):
    Adapters: List[Adapter]


class AdapterVersionDatasetConfig(BaseValidatorModel):
    ManifestS3Object: Optional[S3Object] = None


class DocumentLocation(BaseValidatorModel):
    S3Object: Optional[S3Object] = None


class AdapterVersionEvaluationMetric(BaseValidatorModel):
    Baseline: Optional[EvaluationMetric] = None
    AdapterVersion: Optional[EvaluationMetric] = None
    FeatureType: Optional[FeatureTypeType] = None


# This class is the output for the 'create_adapter' function.
class CreateAdapterResponse(BaseValidatorModel):
    AdapterId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_adapter_version' function.
class CreateAdapterVersionResponse(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_adapter' function.
class GetAdapterResponse(BaseValidatorModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_adapter_versions' function.
class ListAdapterVersionsResponse(BaseValidatorModel):
    AdapterVersions: List[AdapterVersionOverview]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_adapters' function.
class ListAdaptersResponse(BaseValidatorModel):
    Adapters: List[AdapterOverview]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_document_analysis' function.
class StartDocumentAnalysisResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_document_text_detection' function.
class StartDocumentTextDetectionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_expense_analysis' function.
class StartExpenseAnalysisResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_lending_analysis' function.
class StartLendingAnalysisResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_adapter' function.
class UpdateAdapterResponse(BaseValidatorModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    ResponseMetadata: ResponseMetadata


class AnalyzeIDDetections(BaseValidatorModel):
    Text: str
    NormalizedValue: Optional[NormalizedValue] = None
    Confidence: Optional[float] = None


class Document(BaseValidatorModel):
    Bytes: Optional[Blob] = None
    S3Object: Optional[S3Object] = None


class DocumentGroup(BaseValidatorModel):
    Type: Optional[str] = None
    SplitDocuments: Optional[List[SplitDocument]] = None
    DetectedSignatures: Optional[List[DetectedSignature]] = None
    UndetectedSignatures: Optional[List[UndetectedSignature]] = None


class Geometry(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class HumanLoopConfig(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributes] = None


class ListAdapterVersionsRequestPaginate(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[Timestamp] = None
    BeforeCreationTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_adapter_versions' function.
class ListAdapterVersionsRequest(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[Timestamp] = None
    BeforeCreationTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAdaptersRequestPaginate(BaseValidatorModel):
    AfterCreationTime: Optional[Timestamp] = None
    BeforeCreationTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_adapters' function.
class ListAdaptersRequest(BaseValidatorModel):
    AfterCreationTime: Optional[Timestamp] = None
    BeforeCreationTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PageClassification(BaseValidatorModel):
    PageType: List[Prediction]
    PageNumber: List[Prediction]

QueryUnion = Union[Query, QueryOutput]


# This class is the input for the 'create_adapter_version' function.
class CreateAdapterVersionRequest(BaseValidatorModel):
    AdapterId: str
    DatasetConfig: AdapterVersionDatasetConfig
    OutputConfig: OutputConfig
    ClientRequestToken: Optional[str] = None
    KMSKeyId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'start_document_text_detection' function.
class StartDocumentTextDetectionRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None


# This class is the input for the 'start_expense_analysis' function.
class StartExpenseAnalysisRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None


# This class is the input for the 'start_lending_analysis' function.
class StartLendingAnalysisRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None


# This class is the output for the 'get_adapter_version' function.
class GetAdapterVersionResponse(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str
    CreationTime: datetime
    FeatureTypes: List[FeatureTypeType]
    Status: AdapterVersionStatusType
    StatusMessage: str
    DatasetConfig: AdapterVersionDatasetConfig
    KMSKeyId: str
    OutputConfig: OutputConfig
    EvaluationMetrics: List[AdapterVersionEvaluationMetric]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class IdentityDocumentField(BaseValidatorModel):
    Type: Optional[AnalyzeIDDetections] = None
    ValueDetection: Optional[AnalyzeIDDetections] = None


# This class is the input for the 'analyze_expense' function.
class AnalyzeExpenseRequest(BaseValidatorModel):
    Document: Document


# This class is the input for the 'analyze_id' function.
class AnalyzeIDRequest(BaseValidatorModel):
    DocumentPages: List[Document]


# This class is the input for the 'detect_document_text' function.
class DetectDocumentTextRequest(BaseValidatorModel):
    Document: Document


class LendingSummary(BaseValidatorModel):
    DocumentGroups: Optional[List[DocumentGroup]] = None
    UndetectedDocumentTypes: Optional[List[str]] = None


class Block(BaseValidatorModel):
    BlockType: Optional[BlockTypeType] = None
    Confidence: Optional[float] = None
    Text: Optional[str] = None
    TextType: Optional[TextTypeType] = None
    RowIndex: Optional[int] = None
    ColumnIndex: Optional[int] = None
    RowSpan: Optional[int] = None
    ColumnSpan: Optional[int] = None
    Geometry: Optional[Geometry] = None
    Id: Optional[str] = None
    Relationships: Optional[List[Relationship]] = None
    EntityTypes: Optional[List[EntityTypeType]] = None
    SelectionStatus: Optional[SelectionStatusType] = None
    Page: Optional[int] = None
    Query: Optional[QueryOutput] = None


class ExpenseDetection(BaseValidatorModel):
    Text: Optional[str] = None
    Geometry: Optional[Geometry] = None
    Confidence: Optional[float] = None


class LendingDetection(BaseValidatorModel):
    Text: Optional[str] = None
    SelectionStatus: Optional[SelectionStatusType] = None
    Geometry: Optional[Geometry] = None
    Confidence: Optional[float] = None


class SignatureDetection(BaseValidatorModel):
    Confidence: Optional[float] = None
    Geometry: Optional[Geometry] = None


class QueriesConfig(BaseValidatorModel):
    Queries: List[QueryUnion]


# This class is the output for the 'get_lending_analysis_summary' function.
class GetLendingAnalysisSummaryResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Summary: LendingSummary
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'analyze_document' function.
class AnalyzeDocumentResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    Blocks: List[Block]
    HumanLoopActivationOutput: HumanLoopActivationOutput
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_document_text' function.
class DetectDocumentTextResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    Blocks: List[Block]
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_document_analysis' function.
class GetDocumentAnalysisResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Blocks: List[Block]
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_document_text_detection' function.
class GetDocumentTextDetectionResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Blocks: List[Block]
    Warnings: List[Warning]
    StatusMessage: str
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IdentityDocument(BaseValidatorModel):
    DocumentIndex: Optional[int] = None
    IdentityDocumentFields: Optional[List[IdentityDocumentField]] = None
    Blocks: Optional[List[Block]] = None


class ExpenseField(BaseValidatorModel):
    Type: Optional[ExpenseType] = None
    LabelDetection: Optional[ExpenseDetection] = None
    ValueDetection: Optional[ExpenseDetection] = None
    PageNumber: Optional[int] = None
    Currency: Optional[ExpenseCurrency] = None
    GroupProperties: Optional[List[ExpenseGroupProperty]] = None


class LendingField(BaseValidatorModel):
    Type: Optional[str] = None
    KeyDetection: Optional[LendingDetection] = None
    ValueDetections: Optional[List[LendingDetection]] = None


# This class is the input for the 'analyze_document' function.
class AnalyzeDocumentRequest(BaseValidatorModel):
    Document: Document
    FeatureTypes: List[FeatureTypeType]
    HumanLoopConfig: Optional[HumanLoopConfig] = None
    QueriesConfig: Optional[QueriesConfig] = None
    AdaptersConfig: Optional[AdaptersConfig] = None


# This class is the input for the 'start_document_analysis' function.
class StartDocumentAnalysisRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    FeatureTypes: List[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None
    QueriesConfig: Optional[QueriesConfig] = None
    AdaptersConfig: Optional[AdaptersConfig] = None


# This class is the output for the 'analyze_id' function.
class AnalyzeIDResponse(BaseValidatorModel):
    IdentityDocuments: List[IdentityDocument]
    DocumentMetadata: DocumentMetadata
    AnalyzeIDModelVersion: str
    ResponseMetadata: ResponseMetadata


class LineItemFields(BaseValidatorModel):
    LineItemExpenseFields: Optional[List[ExpenseField]] = None


class LendingDocument(BaseValidatorModel):
    LendingFields: Optional[List[LendingField]] = None
    SignatureDetections: Optional[List[SignatureDetection]] = None


class LineItemGroup(BaseValidatorModel):
    LineItemGroupIndex: Optional[int] = None
    LineItems: Optional[List[LineItemFields]] = None


class ExpenseDocument(BaseValidatorModel):
    ExpenseIndex: Optional[int] = None
    SummaryFields: Optional[List[ExpenseField]] = None
    LineItemGroups: Optional[List[LineItemGroup]] = None
    Blocks: Optional[List[Block]] = None


# This class is the output for the 'analyze_expense' function.
class AnalyzeExpenseResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    ExpenseDocuments: List[ExpenseDocument]
    ResponseMetadata: ResponseMetadata


class Extraction(BaseValidatorModel):
    LendingDocument: Optional[LendingDocument] = None
    ExpenseDocument: Optional[ExpenseDocument] = None
    IdentityDocument: Optional[IdentityDocument] = None


# This class is the output for the 'get_expense_analysis' function.
class GetExpenseAnalysisResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    ExpenseDocuments: List[ExpenseDocument]
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeExpenseModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LendingResult(BaseValidatorModel):
    Page: Optional[int] = None
    PageClassification: Optional[PageClassification] = None
    Extractions: Optional[List[Extraction]] = None


# This class is the output for the 'get_lending_analysis' function.
class GetLendingAnalysisResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Results: List[LendingResult]
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None