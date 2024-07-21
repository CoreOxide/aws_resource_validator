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
from aws_resource_validator.pydantic_models.support_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddCommunicationToCaseRequestRequestTypeDef(BaseModel):
    communicationBody: str
    caseId: Optional[str] = None
    ccEmailAddresses: Optional[Sequence[str]] = None
    attachmentSetId: Optional[str] = None

class AttachmentDetailsTypeDef(BaseModel):
    attachmentId: Optional[str] = None
    fileName: Optional[str] = None

class AttachmentOutputTypeDef(BaseModel):
    fileName: Optional[str] = None
    data: Optional[bytes] = None

class CategoryTypeDef(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None

class DateIntervalTypeDef(BaseModel):
    startDateTime: Optional[str] = None
    endDateTime: Optional[str] = None

class SupportedHourTypeDef(BaseModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None

class CreateCaseRequestRequestTypeDef(BaseModel):
    subject: str
    communicationBody: str
    serviceCode: Optional[str] = None
    severityCode: Optional[str] = None
    categoryCode: Optional[str] = None
    ccEmailAddresses: Optional[Sequence[str]] = None
    language: Optional[str] = None
    issueType: Optional[str] = None
    attachmentSetId: Optional[str] = None

class DescribeAttachmentRequestRequestTypeDef(BaseModel):
    attachmentId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCasesRequestRequestTypeDef(BaseModel):
    caseIdList: Optional[Sequence[str]] = None
    displayId: Optional[str] = None
    afterTime: Optional[str] = None
    beforeTime: Optional[str] = None
    includeResolvedCases: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    language: Optional[str] = None
    includeCommunications: Optional[bool] = None

class DescribeCommunicationsRequestRequestTypeDef(BaseModel):
    caseId: str
    beforeTime: Optional[str] = None
    afterTime: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeCreateCaseOptionsRequestRequestTypeDef(BaseModel):
    issueType: str
    serviceCode: str
    language: str
    categoryCode: str

class DescribeServicesRequestRequestTypeDef(BaseModel):
    serviceCodeList: Optional[Sequence[str]] = None
    language: Optional[str] = None

class DescribeSeverityLevelsRequestRequestTypeDef(BaseModel):
    language: Optional[str] = None

class SeverityLevelTypeDef(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None

class DescribeSupportedLanguagesRequestRequestTypeDef(BaseModel):
    issueType: str
    serviceCode: str
    categoryCode: str

class SupportedLanguageTypeDef(BaseModel):
    code: Optional[str] = None
    language: Optional[str] = None
    display: Optional[str] = None

class DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef(BaseModel):
    checkIds: Sequence[str]

class TrustedAdvisorCheckRefreshStatusTypeDef(BaseModel):
    checkId: str
    status: str
    millisUntilNextRefreshable: int

class DescribeTrustedAdvisorCheckResultRequestRequestTypeDef(BaseModel):
    checkId: str
    language: Optional[str] = None

class DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef(BaseModel):
    checkIds: Sequence[str]

class DescribeTrustedAdvisorChecksRequestRequestTypeDef(BaseModel):
    language: str

class TrustedAdvisorCheckDescriptionTypeDef(BaseModel):
    id: str
    name: str
    description: str
    category: str
    metadata: List[str]

class RefreshTrustedAdvisorCheckRequestRequestTypeDef(BaseModel):
    checkId: str

class ResolveCaseRequestRequestTypeDef(BaseModel):
    caseId: Optional[str] = None

class TrustedAdvisorCostOptimizingSummaryTypeDef(BaseModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float

class TrustedAdvisorResourceDetailTypeDef(BaseModel):
    status: str
    resourceId: str
    metadata: List[str]
    region: Optional[str] = None
    isSuppressed: Optional[bool] = None

class TrustedAdvisorResourcesSummaryTypeDef(BaseModel):
    resourcesProcessed: int
    resourcesFlagged: int
    resourcesIgnored: int
    resourcesSuppressed: int

class AddAttachmentsToSetResponseTypeDef(BaseModel):
    attachmentSetId: str
    expiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddCommunicationToCaseResponseTypeDef(BaseModel):
    result: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseResponseTypeDef(BaseModel):
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveCaseResponseTypeDef(BaseModel):
    initialCaseStatus: str
    finalCaseStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class CommunicationTypeDef(BaseModel):
    caseId: Optional[str] = None
    body: Optional[str] = None
    submittedBy: Optional[str] = None
    timeCreated: Optional[str] = None
    attachmentSet: Optional[List[AttachmentDetailsTypeDef]] = None

class DescribeAttachmentResponseTypeDef(BaseModel):
    attachment: AttachmentOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentTypeDef(BaseModel):
    fileName: Optional[str] = None
    data: Optional[BlobTypeDef] = None

class ServiceTypeDef(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    categories: Optional[List[CategoryTypeDef]] = None

class CommunicationTypeOptionsTypeDef(BaseModel):
    type: Optional[str] = None
    supportedHours: Optional[List[SupportedHourTypeDef]] = None
    datesWithoutSupport: Optional[List[DateIntervalTypeDef]] = None

class DescribeCasesRequestDescribeCasesPaginateTypeDef(BaseModel):
    caseIdList: Optional[Sequence[str]] = None
    displayId: Optional[str] = None
    afterTime: Optional[str] = None
    beforeTime: Optional[str] = None
    includeResolvedCases: Optional[bool] = None
    language: Optional[str] = None
    includeCommunications: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCommunicationsRequestDescribeCommunicationsPaginateTypeDef(BaseModel):
    caseId: str
    beforeTime: Optional[str] = None
    afterTime: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSeverityLevelsResponseTypeDef(BaseModel):
    severityLevels: List[SeverityLevelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSupportedLanguagesResponseTypeDef(BaseModel):
    supportedLanguages: List[SupportedLanguageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef(BaseModel):
    statuses: List[TrustedAdvisorCheckRefreshStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshTrustedAdvisorCheckResponseTypeDef(BaseModel):
    status: TrustedAdvisorCheckRefreshStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustedAdvisorChecksResponseTypeDef(BaseModel):
    checks: List[TrustedAdvisorCheckDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrustedAdvisorCategorySpecificSummaryTypeDef(BaseModel):
    costOptimizing: Optional[TrustedAdvisorCostOptimizingSummaryTypeDef] = None

class DescribeCommunicationsResponseTypeDef(BaseModel):
    communications: List[CommunicationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecentCaseCommunicationsTypeDef(BaseModel):
    communications: Optional[List[CommunicationTypeDef]] = None
    nextToken: Optional[str] = None

class DescribeServicesResponseTypeDef(BaseModel):
    services: List[ServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCreateCaseOptionsResponseTypeDef(BaseModel):
    languageAvailability: str
    communicationTypes: List[CommunicationTypeOptionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrustedAdvisorCheckResultTypeDef(BaseModel):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummaryTypeDef
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummaryTypeDef
    flaggedResources: List[TrustedAdvisorResourceDetailTypeDef]

class TrustedAdvisorCheckSummaryTypeDef(BaseModel):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummaryTypeDef
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummaryTypeDef
    hasFlaggedResources: Optional[bool] = None

class CaseDetailsTypeDef(BaseModel):
    caseId: Optional[str] = None
    displayId: Optional[str] = None
    subject: Optional[str] = None
    status: Optional[str] = None
    serviceCode: Optional[str] = None
    categoryCode: Optional[str] = None
    severityCode: Optional[str] = None
    submittedBy: Optional[str] = None
    timeCreated: Optional[str] = None
    recentCommunications: Optional[RecentCaseCommunicationsTypeDef] = None
    ccEmailAddresses: Optional[List[str]] = None
    language: Optional[str] = None

class AddAttachmentsToSetRequestRequestTypeDef(BaseModel):
    attachments: Sequence[AttachmentUnionTypeDef]
    attachmentSetId: Optional[str] = None

class DescribeTrustedAdvisorCheckResultResponseTypeDef(BaseModel):
    result: TrustedAdvisorCheckResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustedAdvisorCheckSummariesResponseTypeDef(BaseModel):
    summaries: List[TrustedAdvisorCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCasesResponseTypeDef(BaseModel):
    cases: List[CaseDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

