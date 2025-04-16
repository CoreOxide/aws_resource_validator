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
from aws_resource_validator.pydantic_models.textract_constants import *

class AdapterOverview(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AdapterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None


class Adapter(BaseValidatorModel):
    AdapterId: str
    Version: str
    Pages: Optional[Sequence[str]] = None


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
    ValueType: Optional[Literal["DATE"]] = None


class BoundingBox(BaseValidatorModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None


class CreateAdapterRequest(BaseValidatorModel):
    AdapterName: str
    FeatureTypes: Sequence[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None
    Tags: Optional[Mapping[str, str]] = None


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


class Point(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None


class GetAdapterRequest(BaseValidatorModel):
    AdapterId: str


class GetAdapterVersionRequest(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str


class GetDocumentAnalysisRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Warning(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Pages: Optional[List[int]] = None


class GetDocumentTextDetectionRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetExpenseAnalysisRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetLendingAnalysisRequest(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetLendingAnalysisSummaryRequest(BaseValidatorModel):
    JobId: str


class HumanLoopDataAttributes(BaseValidatorModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class NotificationChannel(BaseValidatorModel):
    SNSTopicArn: str
    RoleArn: str


class Prediction(BaseValidatorModel):
    Value: Optional[str] = None
    Confidence: Optional[float] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateAdapterRequest(BaseValidatorModel):
    AdapterId: str
    Description: Optional[str] = None
    AdapterName: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None


class AdaptersConfig(BaseValidatorModel):
    Adapters: Sequence[Adapter]


class AdapterVersionDatasetConfig(BaseValidatorModel):
    ManifestS3Object: Optional[S3Object] = None


class DocumentLocation(BaseValidatorModel):
    S3Object: Optional[S3Object] = None


class AdapterVersionEvaluationMetric(BaseValidatorModel):
    Baseline: Optional[EvaluationMetric] = None
    AdapterVersion: Optional[EvaluationMetric] = None
    FeatureType: Optional[FeatureTypeType] = None


class CreateAdapterResponse(BaseValidatorModel):
    AdapterId: str
    ResponseMetadata: ResponseMetadata


class CreateAdapterVersionResponse(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str
    ResponseMetadata: ResponseMetadata


class GetAdapterResponse(BaseValidatorModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListAdapterVersionsResponse(BaseValidatorModel):
    AdapterVersions: List[AdapterVersionOverview]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAdaptersResponse(BaseValidatorModel):
    Adapters: List[AdapterOverview]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartDocumentAnalysisResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartDocumentTextDetectionResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartExpenseAnalysisResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartLendingAnalysisResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class UpdateAdapterResponse(BaseValidatorModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class Document(BaseValidatorModel):
    Bytes: Optional[Blob] = None
    S3Object: Optional[S3Object] = None


class Geometry(BaseValidatorModel):
    BoundingBox: Optional[BoundingBox] = None
    Polygon: Optional[List[Point]] = None


class HumanLoopConfig(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributes] = None


class Timestamp(BaseValidatorModel):
    pass


class ListAdapterVersionsRequestPaginate(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[Timestamp] = None
    BeforeCreationTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


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


class ListAdaptersRequest(BaseValidatorModel):
    AfterCreationTime: Optional[Timestamp] = None
    BeforeCreationTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PageClassification(BaseValidatorModel):
    PageType: List[Prediction]
    PageNumber: List[Prediction]


class CreateAdapterVersionRequest(BaseValidatorModel):
    AdapterId: str
    DatasetConfig: AdapterVersionDatasetConfig
    OutputConfig: OutputConfig
    ClientRequestToken: Optional[str] = None
    KMSKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class StartDocumentTextDetectionRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None


class StartExpenseAnalysisRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None


class StartLendingAnalysisRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None


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


class AnalyzeExpenseRequest(BaseValidatorModel):
    Document: Document


class AnalyzeIDRequest(BaseValidatorModel):
    DocumentPages: Sequence[Document]


class DetectDocumentTextRequest(BaseValidatorModel):
    Document: Document


class DocumentGroup(BaseValidatorModel):
    pass


class LendingSummary(BaseValidatorModel):
    DocumentGroups: Optional[List[DocumentGroup]] = None
    UndetectedDocumentTypes: Optional[List[str]] = None


class SignatureDetection(BaseValidatorModel):
    Confidence: Optional[float] = None
    Geometry: Optional[Geometry] = None


class QueryUnion(BaseValidatorModel):
    pass


class QueriesConfig(BaseValidatorModel):
    Queries: Sequence[QueryUnion]


class GetLendingAnalysisSummaryResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Summary: LendingSummary
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadata


class Block(BaseValidatorModel):
    pass


class AnalyzeDocumentResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    Blocks: List[Block]
    HumanLoopActivationOutput: HumanLoopActivationOutput
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadata


class DetectDocumentTextResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    Blocks: List[Block]
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadata


class GetDocumentAnalysisResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Blocks: List[Block]
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDocumentTextDetectionResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Blocks: List[Block]
    Warnings: List[Warning]
    StatusMessage: str
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IdentityDocumentField(BaseValidatorModel):
    pass


class IdentityDocument(BaseValidatorModel):
    DocumentIndex: Optional[int] = None
    IdentityDocumentFields: Optional[List[IdentityDocumentField]] = None
    Blocks: Optional[List[Block]] = None


class AnalyzeDocumentRequest(BaseValidatorModel):
    Document: Document
    FeatureTypes: Sequence[FeatureTypeType]
    HumanLoopConfig: Optional[HumanLoopConfig] = None
    QueriesConfig: Optional[QueriesConfig] = None
    AdaptersConfig: Optional[AdaptersConfig] = None


class StartDocumentAnalysisRequest(BaseValidatorModel):
    DocumentLocation: DocumentLocation
    FeatureTypes: Sequence[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannel] = None
    OutputConfig: Optional[OutputConfig] = None
    KMSKeyId: Optional[str] = None
    QueriesConfig: Optional[QueriesConfig] = None
    AdaptersConfig: Optional[AdaptersConfig] = None


class AnalyzeIDResponse(BaseValidatorModel):
    IdentityDocuments: List[IdentityDocument]
    DocumentMetadata: DocumentMetadata
    AnalyzeIDModelVersion: str
    ResponseMetadata: ResponseMetadata


class ExpenseField(BaseValidatorModel):
    pass


class LineItemFields(BaseValidatorModel):
    LineItemExpenseFields: Optional[List[ExpenseField]] = None


class LendingField(BaseValidatorModel):
    pass


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


class AnalyzeExpenseResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    ExpenseDocuments: List[ExpenseDocument]
    ResponseMetadata: ResponseMetadata


class Extraction(BaseValidatorModel):
    LendingDocument: Optional[LendingDocument] = None
    ExpenseDocument: Optional[ExpenseDocument] = None
    IdentityDocument: Optional[IdentityDocument] = None


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


class GetLendingAnalysisResponse(BaseValidatorModel):
    DocumentMetadata: DocumentMetadata
    JobStatus: JobStatusType
    Results: List[LendingResult]
    Warnings: List[Warning]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


