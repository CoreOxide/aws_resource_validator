from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codeguru_security.codeguru_security_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'create_upload_url' function.
class CreateUploadUrlRequest(BaseValidatorModel):
    scanName: str


class EncryptionConfig(BaseValidatorModel):
    kmsKeyArn: Optional[str] = None


class Resource(BaseValidatorModel):
    id: Optional[str] = None
    subResourceId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_findings' function.
class GetFindingsRequest(BaseValidatorModel):
    scanName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[StatusType] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'get_scan' function.
class GetScanRequest(BaseValidatorModel):
    scanName: str
    runId: Optional[str] = None


# This class is the input for the 'list_scans' function.
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


# This class is the input for the 'list_tags_for_resource' function.
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
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AccountFindingsMetric(BaseValidatorModel):
    closedFindings: Optional[FindingMetricsValuePerSeverity] = None
    date: Optional[datetime] = None
    meanTimeToClose: Optional[FindingMetricsValuePerSeverity] = None
    newFindings: Optional[FindingMetricsValuePerSeverity] = None
    openFindings: Optional[FindingMetricsValuePerSeverity] = None


# This class is the input for the 'batch_get_findings' function.
class BatchGetFindingsRequest(BaseValidatorModel):
    findingIdentifiers: List[FindingIdentifier]


# This class is the output for the 'create_upload_url' function.
class CreateUploadUrlResponse(BaseValidatorModel):
    codeArtifactId: str
    requestHeaders: Dict[str, str]
    s3Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_scan' function.
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


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class FilePath(BaseValidatorModel):
    codeSnippet: Optional[List[CodeLine]] = None
    endLine: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    startLine: Optional[int] = None


# This class is the input for the 'create_scan' function.
class CreateScanRequest(BaseValidatorModel):
    resourceId: ResourceId
    scanName: str
    analysisType: Optional[AnalysisTypeType] = None
    clientToken: Optional[str] = None
    scanType: Optional[ScanTypeType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_scan' function.
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


# This class is the input for the 'update_account_configuration' function.
class UpdateAccountConfigurationRequest(BaseValidatorModel):
    encryptionConfig: EncryptionConfig


# This class is the output for the 'update_account_configuration' function.
class UpdateAccountConfigurationResponse(BaseValidatorModel):
    encryptionConfig: EncryptionConfig
    ResponseMetadata: ResponseMetadata


class GetFindingsRequestPaginate(BaseValidatorModel):
    scanName: str
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScansRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_metrics_summary' function.
class GetMetricsSummaryRequest(BaseValidatorModel):
    date: Timestamp


class ListFindingsMetricsRequestPaginate(BaseValidatorModel):
    endDate: Timestamp
    startDate: Timestamp
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_findings_metrics' function.
class ListFindingsMetricsRequest(BaseValidatorModel):
    endDate: Timestamp
    startDate: Timestamp
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_scans' function.
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


# This class is the output for the 'list_findings_metrics' function.
class ListFindingsMetricsResponse(BaseValidatorModel):
    findingsMetrics: List[AccountFindingsMetric]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Vulnerability(BaseValidatorModel):
    filePath: Optional[FilePath] = None
    id: Optional[str] = None
    itemCount: Optional[int] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None


# This class is the output for the 'get_metrics_summary' function.
class GetMetricsSummaryResponse(BaseValidatorModel):
    metricsSummary: MetricsSummary
    ResponseMetadata: ResponseMetadata


class Finding(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    detectorId: Optional[str] = None
    detectorName: Optional[str] = None
    detectorTags: Optional[List[str]] = None
    generatorId: Optional[str] = None
    id: Optional[str] = None
    remediation: Optional[Remediation] = None
    resource: Optional[Resource] = None
    ruleId: Optional[str] = None
    severity: Optional[SeverityType] = None
    status: Optional[StatusType] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updatedAt: Optional[datetime] = None
    vulnerability: Optional[Vulnerability] = None


# This class is the output for the 'batch_get_findings' function.
class BatchGetFindingsResponse(BaseValidatorModel):
    failedFindings: List[BatchGetFindingsError]
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_findings' function.
class GetFindingsResponse(BaseValidatorModel):
    findings: List[Finding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None