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

class FindingMetricsValuePerSeverity(BaseValidatorModel):
    critical: Optional[float] = None
    high: Optional[float] = None
    info: Optional[float] = None
    low: Optional[float] = None
    medium: Optional[float] = None


class BatchGetFindingsError(BaseValidatorModel):
    errorCode: ErrorCodeType
    findingId: str
    message: str
    scanName: str


class FindingIdentifier(BaseValidatorModel):
    findingId: str
    scanName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CategoryWithFindingNum(BaseValidatorModel):
    categoryName: Optional[str] = None
    findingNumber: Optional[int] = None


class CodeLine(BaseValidatorModel):
    content: Optional[str] = None
    number: Optional[int] = None


class ResourceId(BaseValidatorModel):
    codeArtifactId: Optional[str] = None


class CreateUploadUrlRequest(BaseValidatorModel):
    scanName: str


class EncryptionConfig(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetFindingsRequest(BaseValidatorModel):
    scanName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[StatusType] = None


class GetScanRequest(BaseValidatorModel):
    scanName: str
    runId: Optional[str] = None


class ListScansRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScanSummary(BaseValidatorModel):
    createdAt: datetime
    runId: str
    scanName: str
    scanState: ScanStateType
    scanNameArn: Optional[str] = None
    updatedAt: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ScanNameWithFindingNum(BaseValidatorModel):
    findingNumber: Optional[int] = None
    scanName: Optional[str] = None


class Recommendation(BaseValidatorModel):
    text: Optional[str] = None
    url: Optional[str] = None


class SuggestedFix(BaseValidatorModel):
    code: Optional[str] = None
    description: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AccountFindingsMetric(BaseValidatorModel):
    closedFindings: Optional[FindingMetricsValuePerSeverity] = None
    date: Optional[datetime] = None
    meanTimeToClose: Optional[FindingMetricsValuePerSeverity] = None
    newFindings: Optional[FindingMetricsValuePerSeverity] = None
    openFindings: Optional[FindingMetricsValuePerSeverity] = None


class BatchGetFindingsRequest(BaseValidatorModel):
    findingIdentifiers: Sequence[FindingIdentifier]


class CreateUploadUrlResponse(BaseValidatorModel):
    codeArtifactId: str
    requestHeaders: Dict[str, str]
    s3Url: str
    ResponseMetadata: ResponseMetadata


class GetScanResponse(BaseValidatorModel):
    analysisType: AnalysisTypeType
    createdAt: datetime
    errorMessage: str
    numberOfRevisions: int
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class FilePath(BaseValidatorModel):
    codeSnippet: Optional[List[CodeLine]] = None
    endLine: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    startLine: Optional[int] = None


class CreateScanRequest(BaseValidatorModel):
    resourceId: ResourceId
    scanName: str
    analysisType: Optional[AnalysisTypeType] = None
    clientToken: Optional[str] = None
    scanType: Optional[ScanTypeType] = None
    tags: Optional[Mapping[str, str]] = None


class CreateScanResponse(BaseValidatorModel):
    resourceId: ResourceId
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    ResponseMetadata: ResponseMetadata


class GetAccountConfigurationResponse(BaseValidatorModel):
    encryptionConfig: EncryptionConfig
    ResponseMetadata: ResponseMetadata


class UpdateAccountConfigurationRequest(BaseValidatorModel):
    encryptionConfig: EncryptionConfig


class UpdateAccountConfigurationResponse(BaseValidatorModel):
    encryptionConfig: EncryptionConfig
    ResponseMetadata: ResponseMetadata


class GetFindingsRequestPaginate(BaseValidatorModel):
    scanName: str
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScansRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class GetMetricsSummaryRequest(BaseValidatorModel):
    date: Timestamp


class ListFindingsMetricsRequestPaginate(BaseValidatorModel):
    endDate: Timestamp
    startDate: Timestamp
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingsMetricsRequest(BaseValidatorModel):
    endDate: Timestamp
    startDate: Timestamp
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListScansResponse(BaseValidatorModel):
    summaries: List[ScanSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MetricsSummary(BaseValidatorModel):
    categoriesWithMostFindings: Optional[List[CategoryWithFindingNum]] = None
    date: Optional[datetime] = None
    openFindings: Optional[FindingMetricsValuePerSeverity] = None
    scansWithMostOpenCriticalFindings: Optional[List[ScanNameWithFindingNum]] = None
    scansWithMostOpenFindings: Optional[List[ScanNameWithFindingNum]] = None


class Remediation(BaseValidatorModel):
    recommendation: Optional[Recommendation] = None
    suggestedFixes: Optional[List[SuggestedFix]] = None


class ListFindingsMetricsResponse(BaseValidatorModel):
    findingsMetrics: List[AccountFindingsMetric]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetMetricsSummaryResponse(BaseValidatorModel):
    metricsSummary: MetricsSummary
    ResponseMetadata: ResponseMetadata


class Finding(BaseValidatorModel):
    pass


class BatchGetFindingsResponse(BaseValidatorModel):
    failedFindings: List[BatchGetFindingsError]
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata


class GetFindingsResponse(BaseValidatorModel):
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


