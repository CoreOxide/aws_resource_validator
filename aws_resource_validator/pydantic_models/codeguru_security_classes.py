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
from aws_resource_validator.pydantic_models.codeguru_security_constants import *

class FindingMetricsValuePerSeverityTypeDef(BaseValidatorModel):
    critical: Optional[float] = None
    high: Optional[float] = None
    info: Optional[float] = None
    low: Optional[float] = None
    medium: Optional[float] = None


class BatchGetFindingsErrorTypeDef(BaseValidatorModel):
    errorCode: ErrorCodeType
    findingId: str
    message: str
    scanName: str


class FindingIdentifierTypeDef(BaseValidatorModel):
    findingId: str
    scanName: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CategoryWithFindingNumTypeDef(BaseValidatorModel):
    categoryName: Optional[str] = None
    findingNumber: Optional[int] = None


class CodeLineTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    number: Optional[int] = None


class ResourceIdTypeDef(BaseValidatorModel):
    codeArtifactId: Optional[str] = None


class CreateUploadUrlRequestTypeDef(BaseValidatorModel):
    scanName: str


class EncryptionConfigTypeDef(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetFindingsRequestTypeDef(BaseValidatorModel):
    scanName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[StatusType] = None


class GetScanRequestTypeDef(BaseValidatorModel):
    scanName: str
    runId: Optional[str] = None


class ListScansRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScanSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    runId: str
    scanName: str
    scanState: ScanStateType
    scanNameArn: Optional[str] = None
    updatedAt: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ScanNameWithFindingNumTypeDef(BaseValidatorModel):
    findingNumber: Optional[int] = None
    scanName: Optional[str] = None


class RecommendationTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    url: Optional[str] = None


class SuggestedFixTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    description: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AccountFindingsMetricTypeDef(BaseValidatorModel):
    closedFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    date: Optional[datetime] = None
    meanTimeToClose: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    newFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    openFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None


class BatchGetFindingsRequestTypeDef(BaseValidatorModel):
    findingIdentifiers: Sequence[FindingIdentifierTypeDef]


class CreateUploadUrlResponseTypeDef(BaseValidatorModel):
    codeArtifactId: str
    requestHeaders: Dict[str, str]
    s3Url: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetScanResponseTypeDef(BaseValidatorModel):
    analysisType: AnalysisTypeType
    createdAt: datetime
    errorMessage: str
    numberOfRevisions: int
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class FilePathTypeDef(BaseValidatorModel):
    codeSnippet: Optional[List[CodeLineTypeDef]] = None
    endLine: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    startLine: Optional[int] = None


class CreateScanRequestTypeDef(BaseValidatorModel):
    resourceId: ResourceIdTypeDef
    scanName: str
    analysisType: Optional[AnalysisTypeType] = None
    clientToken: Optional[str] = None
    scanType: Optional[ScanTypeType] = None
    tags: Optional[Mapping[str, str]] = None


class CreateScanResponseTypeDef(BaseValidatorModel):
    resourceId: ResourceIdTypeDef
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    encryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAccountConfigurationRequestTypeDef(BaseValidatorModel):
    encryptionConfig: EncryptionConfigTypeDef


class UpdateAccountConfigurationResponseTypeDef(BaseValidatorModel):
    encryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFindingsRequestPaginateTypeDef(BaseValidatorModel):
    scanName: str
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListScansRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetMetricsSummaryRequestTypeDef(BaseValidatorModel):
    date: TimestampTypeDef


class ListFindingsMetricsRequestPaginateTypeDef(BaseValidatorModel):
    endDate: TimestampTypeDef
    startDate: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFindingsMetricsRequestTypeDef(BaseValidatorModel):
    endDate: TimestampTypeDef
    startDate: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListScansResponseTypeDef(BaseValidatorModel):
    summaries: List[ScanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MetricsSummaryTypeDef(BaseValidatorModel):
    categoriesWithMostFindings: Optional[List[CategoryWithFindingNumTypeDef]] = None
    date: Optional[datetime] = None
    openFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    scansWithMostOpenCriticalFindings: Optional[List[ScanNameWithFindingNumTypeDef]] = None
    scansWithMostOpenFindings: Optional[List[ScanNameWithFindingNumTypeDef]] = None


class RemediationTypeDef(BaseValidatorModel):
    recommendation: Optional[RecommendationTypeDef] = None
    suggestedFixes: Optional[List[SuggestedFixTypeDef]] = None


class ListFindingsMetricsResponseTypeDef(BaseValidatorModel):
    findingsMetrics: List[AccountFindingsMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetMetricsSummaryResponseTypeDef(BaseValidatorModel):
    metricsSummary: MetricsSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FindingTypeDef(BaseValidatorModel):
    pass


class BatchGetFindingsResponseTypeDef(BaseValidatorModel):
    failedFindings: List[BatchGetFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


