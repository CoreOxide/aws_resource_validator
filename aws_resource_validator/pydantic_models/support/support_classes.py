from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.support.support_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddCommunicationToCaseRequest(BaseValidatorModel):
    communicationBody: str
    caseId: Optional[str] = None
    ccEmailAddresses: Optional[List[str]] = None
    attachmentSetId: Optional[str] = None


class AttachmentDetails(BaseValidatorModel):
    attachmentId: Optional[str] = None
    fileName: Optional[str] = None


class AttachmentOutput(BaseValidatorModel):
    fileName: Optional[str] = None
    data: Optional[bytes] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Category(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None


class DateInterval(BaseValidatorModel):
    startDateTime: Optional[str] = None
    endDateTime: Optional[str] = None


class SupportedHour(BaseValidatorModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None


class CreateCaseRequest(BaseValidatorModel):
    subject: str
    communicationBody: str
    serviceCode: Optional[str] = None
    severityCode: Optional[str] = None
    categoryCode: Optional[str] = None
    ccEmailAddresses: Optional[List[str]] = None
    language: Optional[str] = None
    issueType: Optional[str] = None
    attachmentSetId: Optional[str] = None


class DescribeAttachmentRequest(BaseValidatorModel):
    attachmentId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCasesRequest(BaseValidatorModel):
    caseIdList: Optional[List[str]] = None
    displayId: Optional[str] = None
    afterTime: Optional[str] = None
    beforeTime: Optional[str] = None
    includeResolvedCases: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    language: Optional[str] = None
    includeCommunications: Optional[bool] = None


class DescribeCommunicationsRequest(BaseValidatorModel):
    caseId: str
    beforeTime: Optional[str] = None
    afterTime: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeCreateCaseOptionsRequest(BaseValidatorModel):
    issueType: str
    serviceCode: str
    language: str
    categoryCode: str


class DescribeServicesRequest(BaseValidatorModel):
    serviceCodeList: Optional[List[str]] = None
    language: Optional[str] = None


class DescribeSeverityLevelsRequest(BaseValidatorModel):
    language: Optional[str] = None


class SeverityLevel(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None


class DescribeSupportedLanguagesRequest(BaseValidatorModel):
    issueType: str
    serviceCode: str
    categoryCode: str


class SupportedLanguage(BaseValidatorModel):
    code: Optional[str] = None
    language: Optional[str] = None
    display: Optional[str] = None


class DescribeTrustedAdvisorCheckRefreshStatusesRequest(BaseValidatorModel):
    checkIds: List[str]


class TrustedAdvisorCheckRefreshStatus(BaseValidatorModel):
    checkId: str
    status: str
    millisUntilNextRefreshable: int


class DescribeTrustedAdvisorCheckResultRequest(BaseValidatorModel):
    checkId: str
    language: Optional[str] = None


class DescribeTrustedAdvisorCheckSummariesRequest(BaseValidatorModel):
    checkIds: List[str]


class DescribeTrustedAdvisorChecksRequest(BaseValidatorModel):
    language: str


class TrustedAdvisorCheckDescription(BaseValidatorModel):
    id: str
    name: str
    description: str
    category: str
    metadata: List[str]


class RefreshTrustedAdvisorCheckRequest(BaseValidatorModel):
    checkId: str


class ResolveCaseRequest(BaseValidatorModel):
    caseId: Optional[str] = None


class TrustedAdvisorCostOptimizingSummary(BaseValidatorModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float


class TrustedAdvisorResourceDetail(BaseValidatorModel):
    status: str
    resourceId: str
    metadata: List[str]
    region: Optional[str] = None
    isSuppressed: Optional[bool] = None


class TrustedAdvisorResourcesSummary(BaseValidatorModel):
    resourcesProcessed: int
    resourcesFlagged: int
    resourcesIgnored: int
    resourcesSuppressed: int


class AddAttachmentsToSetResponse(BaseValidatorModel):
    attachmentSetId: str
    expiryTime: str
    ResponseMetadata: ResponseMetadata


class AddCommunicationToCaseResponse(BaseValidatorModel):
    result: bool
    ResponseMetadata: ResponseMetadata


class CreateCaseResponse(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadata


class ResolveCaseResponse(BaseValidatorModel):
    initialCaseStatus: str
    finalCaseStatus: str
    ResponseMetadata: ResponseMetadata


class Communication(BaseValidatorModel):
    caseId: Optional[str] = None
    body: Optional[str] = None
    submittedBy: Optional[str] = None
    timeCreated: Optional[str] = None
    attachmentSet: Optional[List[AttachmentDetails]] = None


class DescribeAttachmentResponse(BaseValidatorModel):
    attachment: AttachmentOutput
    ResponseMetadata: ResponseMetadata


class Attachment(BaseValidatorModel):
    fileName: Optional[str] = None
    data: Optional[Blob] = None


class Service(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None
    categories: Optional[List[Category]] = None


class CommunicationTypeOptions(BaseValidatorModel):
    type: Optional[str] = None
    supportedHours: Optional[List[SupportedHour]] = None
    datesWithoutSupport: Optional[List[DateInterval]] = None


class DescribeCasesRequestPaginate(BaseValidatorModel):
    caseIdList: Optional[List[str]] = None
    displayId: Optional[str] = None
    afterTime: Optional[str] = None
    beforeTime: Optional[str] = None
    includeResolvedCases: Optional[bool] = None
    language: Optional[str] = None
    includeCommunications: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCommunicationsRequestPaginate(BaseValidatorModel):
    caseId: str
    beforeTime: Optional[str] = None
    afterTime: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSeverityLevelsResponse(BaseValidatorModel):
    severityLevels: List[SeverityLevel]
    ResponseMetadata: ResponseMetadata


class DescribeSupportedLanguagesResponse(BaseValidatorModel):
    supportedLanguages: List[SupportedLanguage]
    ResponseMetadata: ResponseMetadata


class DescribeTrustedAdvisorCheckRefreshStatusesResponse(BaseValidatorModel):
    statuses: List[TrustedAdvisorCheckRefreshStatus]
    ResponseMetadata: ResponseMetadata


class RefreshTrustedAdvisorCheckResponse(BaseValidatorModel):
    status: TrustedAdvisorCheckRefreshStatus
    ResponseMetadata: ResponseMetadata


class DescribeTrustedAdvisorChecksResponse(BaseValidatorModel):
    checks: List[TrustedAdvisorCheckDescription]
    ResponseMetadata: ResponseMetadata


class TrustedAdvisorCategorySpecificSummary(BaseValidatorModel):
    costOptimizing: Optional[TrustedAdvisorCostOptimizingSummary] = None


class DescribeCommunicationsResponse(BaseValidatorModel):
    communications: List[Communication]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecentCaseCommunications(BaseValidatorModel):
    communications: Optional[List[Communication]] = None
    nextToken: Optional[str] = None

AttachmentUnion = Union[Attachment, AttachmentOutput]


class DescribeServicesResponse(BaseValidatorModel):
    services: List[Service]
    ResponseMetadata: ResponseMetadata


class DescribeCreateCaseOptionsResponse(BaseValidatorModel):
    languageAvailability: str
    communicationTypes: List[CommunicationTypeOptions]
    ResponseMetadata: ResponseMetadata


class TrustedAdvisorCheckResult(BaseValidatorModel):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummary
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummary
    flaggedResources: List[TrustedAdvisorResourceDetail]


class TrustedAdvisorCheckSummary(BaseValidatorModel):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummary
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummary
    hasFlaggedResources: Optional[bool] = None


class CaseDetails(BaseValidatorModel):
    caseId: Optional[str] = None
    displayId: Optional[str] = None
    subject: Optional[str] = None
    status: Optional[str] = None
    serviceCode: Optional[str] = None
    categoryCode: Optional[str] = None
    severityCode: Optional[str] = None
    submittedBy: Optional[str] = None
    timeCreated: Optional[str] = None
    recentCommunications: Optional[RecentCaseCommunications] = None
    ccEmailAddresses: Optional[List[str]] = None
    language: Optional[str] = None


class AddAttachmentsToSetRequest(BaseValidatorModel):
    attachments: List[AttachmentUnion]
    attachmentSetId: Optional[str] = None


class DescribeTrustedAdvisorCheckResultResponse(BaseValidatorModel):
    result: TrustedAdvisorCheckResult
    ResponseMetadata: ResponseMetadata


class DescribeTrustedAdvisorCheckSummariesResponse(BaseValidatorModel):
    summaries: List[TrustedAdvisorCheckSummary]
    ResponseMetadata: ResponseMetadata


class DescribeCasesResponse(BaseValidatorModel):
    cases: List[CaseDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None