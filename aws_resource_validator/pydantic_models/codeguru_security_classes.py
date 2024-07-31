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
from aws_resource_validator.pydantic_models.codeguru_security_constants import *

class FindingMetricsValuePerSeverityTypeDef(BaseModel):
    critical: Optional[float] = None
    high: Optional[float] = None
    info: Optional[float] = None
    low: Optional[float] = None
    medium: Optional[float] = None

class BatchGetFindingsErrorTypeDef(BaseModel):
    errorCode: ErrorCodeType
    findingId: str
    message: str
    scanName: str

class FindingIdentifierTypeDef(BaseModel):
    findingId: str
    scanName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CategoryWithFindingNumTypeDef(BaseModel):
    categoryName: Optional[str] = None
    findingNumber: Optional[int] = None

class CodeLineTypeDef(BaseModel):
    content: Optional[str] = None
    number: Optional[int] = None

class ResourceIdTypeDef(BaseModel):
    codeArtifactId: Optional[str] = None

class CreateUploadUrlRequestRequestTypeDef(BaseModel):
    scanName: str

class EncryptionConfigTypeDef(BaseModel):
    kmsKeyArn: Optional[str] = None

class ResourceTypeDef(BaseModel):
    id: Optional[str] = None
    subResourceId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetFindingsRequestRequestTypeDef(BaseModel):
    scanName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[StatusType] = None

class GetScanRequestRequestTypeDef(BaseModel):
    scanName: str
    runId: Optional[str] = None

class ListScansRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ScanSummaryTypeDef(BaseModel):
    createdAt: datetime
    runId: str
    scanName: str
    scanState: ScanStateType
    scanNameArn: Optional[str] = None
    updatedAt: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ScanNameWithFindingNumTypeDef(BaseModel):
    findingNumber: Optional[int] = None
    scanName: Optional[str] = None

class RecommendationTypeDef(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

class SuggestedFixTypeDef(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AccountFindingsMetricTypeDef(BaseModel):
    closedFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    date: Optional[datetime] = None
    meanTimeToClose: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    newFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    openFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None

class BatchGetFindingsRequestRequestTypeDef(BaseModel):
    findingIdentifiers: Sequence[FindingIdentifierTypeDef]

class CreateUploadUrlResponseTypeDef(BaseModel):
    codeArtifactId: str
    requestHeaders: Dict[str, str]
    s3Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetScanResponseTypeDef(BaseModel):
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class FilePathTypeDef(BaseModel):
    codeSnippet: Optional[List[CodeLineTypeDef]] = None
    endLine: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    startLine: Optional[int] = None

class CreateScanRequestRequestTypeDef(BaseModel):
    resourceId: ResourceIdTypeDef
    scanName: str
    analysisType: Optional[AnalysisTypeType] = None
    clientToken: Optional[str] = None
    scanType: Optional[ScanTypeType] = None
    tags: Optional[Mapping[str, str]] = None

class CreateScanResponseTypeDef(BaseModel):
    resourceId: ResourceIdTypeDef
    runId: str
    scanName: str
    scanNameArn: str
    scanState: ScanStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountConfigurationResponseTypeDef(BaseModel):
    encryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountConfigurationRequestRequestTypeDef(BaseModel):
    encryptionConfig: EncryptionConfigTypeDef

class UpdateAccountConfigurationResponseTypeDef(BaseModel):
    encryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsRequestGetFindingsPaginateTypeDef(BaseModel):
    scanName: str
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScansRequestListScansPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetMetricsSummaryRequestRequestTypeDef(BaseModel):
    date: TimestampTypeDef

class ListFindingsMetricsRequestListFindingsMetricsPaginateTypeDef(BaseModel):
    endDate: TimestampTypeDef
    startDate: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingsMetricsRequestRequestTypeDef(BaseModel):
    endDate: TimestampTypeDef
    startDate: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListScansResponseTypeDef(BaseModel):
    nextToken: str
    summaries: List[ScanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricsSummaryTypeDef(BaseModel):
    categoriesWithMostFindings: Optional[List[CategoryWithFindingNumTypeDef]] = None
    date: Optional[datetime] = None
    openFindings: Optional[FindingMetricsValuePerSeverityTypeDef] = None
    scansWithMostOpenCriticalFindings: Optional[List[ScanNameWithFindingNumTypeDef]] = None
    scansWithMostOpenFindings: Optional[List[ScanNameWithFindingNumTypeDef]] = None

class RemediationTypeDef(BaseModel):
    recommendation: Optional[RecommendationTypeDef] = None
    suggestedFixes: Optional[List[SuggestedFixTypeDef]] = None

class ListFindingsMetricsResponseTypeDef(BaseModel):
    findingsMetrics: List[AccountFindingsMetricTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class VulnerabilityTypeDef(BaseModel):
    filePath: Optional[FilePathTypeDef] = None
    id: Optional[str] = None
    itemCount: Optional[int] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None

class GetMetricsSummaryResponseTypeDef(BaseModel):
    metricsSummary: MetricsSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FindingTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    detectorId: Optional[str] = None
    detectorName: Optional[str] = None
    detectorTags: Optional[List[str]] = None
    generatorId: Optional[str] = None
    id: Optional[str] = None
    remediation: Optional[RemediationTypeDef] = None
    resource: Optional[ResourceTypeDef] = None
    ruleId: Optional[str] = None
    severity: Optional[SeverityType] = None
    status: Optional[StatusType] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updatedAt: Optional[datetime] = None
    vulnerability: Optional[VulnerabilityTypeDef] = None

class BatchGetFindingsResponseTypeDef(BaseModel):
    failedFindings: List[BatchGetFindingsErrorTypeDef]
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingsResponseTypeDef(BaseModel):
    findings: List[FindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

