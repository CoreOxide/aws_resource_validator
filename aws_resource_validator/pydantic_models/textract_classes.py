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

class AdapterOverviewTypeDef(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AdapterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None


class AdapterTypeDef(BaseValidatorModel):
    AdapterId: str
    Version: str
    Pages: Optional[Sequence[str]] = None


class S3ObjectTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[str] = None


class EvaluationMetricTypeDef(BaseValidatorModel):
    F1Score: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None


class AdapterVersionOverviewTypeDef(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AdapterVersion: Optional[str] = None
    CreationTime: Optional[datetime] = None
    FeatureTypes: Optional[List[FeatureTypeType]] = None
    Status: Optional[AdapterVersionStatusType] = None
    StatusMessage: Optional[str] = None


class DocumentMetadataTypeDef(BaseValidatorModel):
    Pages: Optional[int] = None


class HumanLoopActivationOutputTypeDef(BaseValidatorModel):
    HumanLoopArn: Optional[str] = None
    HumanLoopActivationReasons: Optional[List[str]] = None
    HumanLoopActivationConditionsEvaluationResults: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class NormalizedValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    ValueType: Optional[Literal["DATE"]] = None


class BoundingBoxTypeDef(BaseValidatorModel):
    Width: Optional[float] = None
    Height: Optional[float] = None
    Left: Optional[float] = None
    Top: Optional[float] = None


class CreateAdapterRequestTypeDef(BaseValidatorModel):
    AdapterName: str
    FeatureTypes: Sequence[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    Description: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None
    Tags: Optional[Mapping[str, str]] = None


class OutputConfigTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3Prefix: Optional[str] = None


class DeleteAdapterRequestTypeDef(BaseValidatorModel):
    AdapterId: str


class DeleteAdapterVersionRequestTypeDef(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str


class DetectedSignatureTypeDef(BaseValidatorModel):
    Page: Optional[int] = None


class SplitDocumentTypeDef(BaseValidatorModel):
    Index: Optional[int] = None
    Pages: Optional[List[int]] = None


class UndetectedSignatureTypeDef(BaseValidatorModel):
    Page: Optional[int] = None


class ExpenseCurrencyTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Confidence: Optional[float] = None


class ExpenseGroupPropertyTypeDef(BaseValidatorModel):
    Types: Optional[List[str]] = None
    Id: Optional[str] = None


class PointTypeDef(BaseValidatorModel):
    X: Optional[float] = None
    Y: Optional[float] = None


class GetAdapterRequestTypeDef(BaseValidatorModel):
    AdapterId: str


class GetAdapterVersionRequestTypeDef(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str


class GetDocumentAnalysisRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class WarningTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Pages: Optional[List[int]] = None


class GetDocumentTextDetectionRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetExpenseAnalysisRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetLendingAnalysisRequestTypeDef(BaseValidatorModel):
    JobId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetLendingAnalysisSummaryRequestTypeDef(BaseValidatorModel):
    JobId: str


class HumanLoopDataAttributesTypeDef(BaseValidatorModel):
    ContentClassifiers: Optional[Sequence[ContentClassifierType]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class NotificationChannelTypeDef(BaseValidatorModel):
    SNSTopicArn: str
    RoleArn: str


class PredictionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Confidence: Optional[float] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateAdapterRequestTypeDef(BaseValidatorModel):
    AdapterId: str
    Description: Optional[str] = None
    AdapterName: Optional[str] = None
    AutoUpdate: Optional[AutoUpdateType] = None


class AdaptersConfigTypeDef(BaseValidatorModel):
    Adapters: Sequence[AdapterTypeDef]


class AdapterVersionDatasetConfigTypeDef(BaseValidatorModel):
    ManifestS3Object: Optional[S3ObjectTypeDef] = None


class DocumentLocationTypeDef(BaseValidatorModel):
    S3Object: Optional[S3ObjectTypeDef] = None


class AdapterVersionEvaluationMetricTypeDef(BaseValidatorModel):
    Baseline: Optional[EvaluationMetricTypeDef] = None
    AdapterVersion: Optional[EvaluationMetricTypeDef] = None
    FeatureType: Optional[FeatureTypeType] = None


class CreateAdapterResponseTypeDef(BaseValidatorModel):
    AdapterId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAdapterVersionResponseTypeDef(BaseValidatorModel):
    AdapterId: str
    AdapterVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAdapterResponseTypeDef(BaseValidatorModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAdapterVersionsResponseTypeDef(BaseValidatorModel):
    AdapterVersions: List[AdapterVersionOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAdaptersResponseTypeDef(BaseValidatorModel):
    Adapters: List[AdapterOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartDocumentAnalysisResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDocumentTextDetectionResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartExpenseAnalysisResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartLendingAnalysisResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAdapterResponseTypeDef(BaseValidatorModel):
    AdapterId: str
    AdapterName: str
    CreationTime: datetime
    Description: str
    FeatureTypes: List[FeatureTypeType]
    AutoUpdate: AutoUpdateType
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class DocumentTypeDef(BaseValidatorModel):
    Bytes: Optional[BlobTypeDef] = None
    S3Object: Optional[S3ObjectTypeDef] = None


class GeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[BoundingBoxTypeDef] = None
    Polygon: Optional[List[PointTypeDef]] = None


class HumanLoopConfigTypeDef(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListAdapterVersionsRequestPaginateTypeDef(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAdapterVersionsRequestTypeDef(BaseValidatorModel):
    AdapterId: Optional[str] = None
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAdaptersRequestPaginateTypeDef(BaseValidatorModel):
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAdaptersRequestTypeDef(BaseValidatorModel):
    AfterCreationTime: Optional[TimestampTypeDef] = None
    BeforeCreationTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PageClassificationTypeDef(BaseValidatorModel):
    PageType: List[PredictionTypeDef]
    PageNumber: List[PredictionTypeDef]


class CreateAdapterVersionRequestTypeDef(BaseValidatorModel):
    AdapterId: str
    DatasetConfig: AdapterVersionDatasetConfigTypeDef
    OutputConfig: OutputConfigTypeDef
    ClientRequestToken: Optional[str] = None
    KMSKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class StartDocumentTextDetectionRequestTypeDef(BaseValidatorModel):
    DocumentLocation: DocumentLocationTypeDef
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None


class StartExpenseAnalysisRequestTypeDef(BaseValidatorModel):
    DocumentLocation: DocumentLocationTypeDef
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None


class StartLendingAnalysisRequestTypeDef(BaseValidatorModel):
    DocumentLocation: DocumentLocationTypeDef
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None


class GetAdapterVersionResponseTypeDef(BaseValidatorModel):
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


class AnalyzeExpenseRequestTypeDef(BaseValidatorModel):
    Document: DocumentTypeDef


class AnalyzeIDRequestTypeDef(BaseValidatorModel):
    DocumentPages: Sequence[DocumentTypeDef]


class DetectDocumentTextRequestTypeDef(BaseValidatorModel):
    Document: DocumentTypeDef


class DocumentGroupTypeDef(BaseValidatorModel):
    pass


class LendingSummaryTypeDef(BaseValidatorModel):
    DocumentGroups: Optional[List[DocumentGroupTypeDef]] = None
    UndetectedDocumentTypes: Optional[List[str]] = None


class SignatureDetectionTypeDef(BaseValidatorModel):
    Confidence: Optional[float] = None
    Geometry: Optional[GeometryTypeDef] = None


class QueryUnionTypeDef(BaseValidatorModel):
    pass


class QueriesConfigTypeDef(BaseValidatorModel):
    Queries: Sequence[QueryUnionTypeDef]


class GetLendingAnalysisSummaryResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    Summary: LendingSummaryTypeDef
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class BlockTypeDef(BaseValidatorModel):
    pass


class AnalyzeDocumentResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    Blocks: List[BlockTypeDef]
    HumanLoopActivationOutput: HumanLoopActivationOutputTypeDef
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class DetectDocumentTextResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    Blocks: List[BlockTypeDef]
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDocumentAnalysisResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    Blocks: List[BlockTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeDocumentModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDocumentTextDetectionResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    Blocks: List[BlockTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    DetectDocumentTextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IdentityDocumentFieldTypeDef(BaseValidatorModel):
    pass


class IdentityDocumentTypeDef(BaseValidatorModel):
    DocumentIndex: Optional[int] = None
    IdentityDocumentFields: Optional[List[IdentityDocumentFieldTypeDef]] = None
    Blocks: Optional[List[BlockTypeDef]] = None


class AnalyzeDocumentRequestTypeDef(BaseValidatorModel):
    Document: DocumentTypeDef
    FeatureTypes: Sequence[FeatureTypeType]
    HumanLoopConfig: Optional[HumanLoopConfigTypeDef] = None
    QueriesConfig: Optional[QueriesConfigTypeDef] = None
    AdaptersConfig: Optional[AdaptersConfigTypeDef] = None


class StartDocumentAnalysisRequestTypeDef(BaseValidatorModel):
    DocumentLocation: DocumentLocationTypeDef
    FeatureTypes: Sequence[FeatureTypeType]
    ClientRequestToken: Optional[str] = None
    JobTag: Optional[str] = None
    NotificationChannel: Optional[NotificationChannelTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    KMSKeyId: Optional[str] = None
    QueriesConfig: Optional[QueriesConfigTypeDef] = None
    AdaptersConfig: Optional[AdaptersConfigTypeDef] = None


class AnalyzeIDResponseTypeDef(BaseValidatorModel):
    IdentityDocuments: List[IdentityDocumentTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    AnalyzeIDModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class ExpenseFieldTypeDef(BaseValidatorModel):
    pass


class LineItemFieldsTypeDef(BaseValidatorModel):
    LineItemExpenseFields: Optional[List[ExpenseFieldTypeDef]] = None


class LendingFieldTypeDef(BaseValidatorModel):
    pass


class LendingDocumentTypeDef(BaseValidatorModel):
    LendingFields: Optional[List[LendingFieldTypeDef]] = None
    SignatureDetections: Optional[List[SignatureDetectionTypeDef]] = None


class LineItemGroupTypeDef(BaseValidatorModel):
    LineItemGroupIndex: Optional[int] = None
    LineItems: Optional[List[LineItemFieldsTypeDef]] = None


class ExpenseDocumentTypeDef(BaseValidatorModel):
    ExpenseIndex: Optional[int] = None
    SummaryFields: Optional[List[ExpenseFieldTypeDef]] = None
    LineItemGroups: Optional[List[LineItemGroupTypeDef]] = None
    Blocks: Optional[List[BlockTypeDef]] = None


class AnalyzeExpenseResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    ExpenseDocuments: List[ExpenseDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExtractionTypeDef(BaseValidatorModel):
    LendingDocument: Optional[LendingDocumentTypeDef] = None
    ExpenseDocument: Optional[ExpenseDocumentTypeDef] = None
    IdentityDocument: Optional[IdentityDocumentTypeDef] = None


class GetExpenseAnalysisResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    ExpenseDocuments: List[ExpenseDocumentTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeExpenseModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LendingResultTypeDef(BaseValidatorModel):
    Page: Optional[int] = None
    PageClassification: Optional[PageClassificationTypeDef] = None
    Extractions: Optional[List[ExtractionTypeDef]] = None


class GetLendingAnalysisResponseTypeDef(BaseValidatorModel):
    DocumentMetadata: DocumentMetadataTypeDef
    JobStatus: JobStatusType
    Results: List[LendingResultTypeDef]
    Warnings: List[WarningTypeDef]
    StatusMessage: str
    AnalyzeLendingModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


