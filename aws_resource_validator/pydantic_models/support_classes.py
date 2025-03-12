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
from aws_resource_validator.pydantic_models.support_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddCommunicationToCaseRequestTypeDef(BaseValidatorModel):
    communicationBody: str
    caseId: Optional[str] = None
    ccEmailAddresses: Optional[Sequence[str]] = None
    attachmentSetId: Optional[str] = None


class AttachmentDetailsTypeDef(BaseValidatorModel):
    attachmentId: Optional[str] = None
    fileName: Optional[str] = None


class AttachmentOutputTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    data: Optional[bytes] = None


class CategoryTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None


class DateIntervalTypeDef(BaseValidatorModel):
    startDateTime: Optional[str] = None
    endDateTime: Optional[str] = None


class SupportedHourTypeDef(BaseValidatorModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None


class CreateCaseRequestTypeDef(BaseValidatorModel):
    subject: str
    communicationBody: str
    serviceCode: Optional[str] = None
    severityCode: Optional[str] = None
    categoryCode: Optional[str] = None
    ccEmailAddresses: Optional[Sequence[str]] = None
    language: Optional[str] = None
    issueType: Optional[str] = None
    attachmentSetId: Optional[str] = None


class DescribeAttachmentRequestTypeDef(BaseValidatorModel):
    attachmentId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCasesRequestTypeDef(BaseValidatorModel):
    caseIdList: Optional[Sequence[str]] = None
    displayId: Optional[str] = None
    afterTime: Optional[str] = None
    beforeTime: Optional[str] = None
    includeResolvedCases: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    language: Optional[str] = None
    includeCommunications: Optional[bool] = None


class DescribeCommunicationsRequestTypeDef(BaseValidatorModel):
    caseId: str
    beforeTime: Optional[str] = None
    afterTime: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeCreateCaseOptionsRequestTypeDef(BaseValidatorModel):
    issueType: str
    serviceCode: str
    language: str
    categoryCode: str


class DescribeServicesRequestTypeDef(BaseValidatorModel):
    serviceCodeList: Optional[Sequence[str]] = None
    language: Optional[str] = None


class DescribeSeverityLevelsRequestTypeDef(BaseValidatorModel):
    language: Optional[str] = None


class SeverityLevelTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None


class DescribeSupportedLanguagesRequestTypeDef(BaseValidatorModel):
    issueType: str
    serviceCode: str
    categoryCode: str


class SupportedLanguageTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    language: Optional[str] = None
    display: Optional[str] = None


class DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef(BaseValidatorModel):
    checkIds: Sequence[str]


class TrustedAdvisorCheckRefreshStatusTypeDef(BaseValidatorModel):
    checkId: str
    status: str
    millisUntilNextRefreshable: int


class DescribeTrustedAdvisorCheckResultRequestTypeDef(BaseValidatorModel):
    checkId: str
    language: Optional[str] = None


class DescribeTrustedAdvisorCheckSummariesRequestTypeDef(BaseValidatorModel):
    checkIds: Sequence[str]


class DescribeTrustedAdvisorChecksRequestTypeDef(BaseValidatorModel):
    language: str


class RefreshTrustedAdvisorCheckRequestTypeDef(BaseValidatorModel):
    checkId: str


class ResolveCaseRequestTypeDef(BaseValidatorModel):
    caseId: Optional[str] = None


class TrustedAdvisorCostOptimizingSummaryTypeDef(BaseValidatorModel):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float


class TrustedAdvisorResourceDetailTypeDef(BaseValidatorModel):
    status: str
    resourceId: str
    metadata: List[str]
    region: Optional[str] = None
    isSuppressed: Optional[bool] = None


class TrustedAdvisorResourcesSummaryTypeDef(BaseValidatorModel):
    resourcesProcessed: int
    resourcesFlagged: int
    resourcesIgnored: int
    resourcesSuppressed: int


class AddAttachmentsToSetResponseTypeDef(BaseValidatorModel):
    attachmentSetId: str
    expiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddCommunicationToCaseResponseTypeDef(BaseValidatorModel):
    result: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCaseResponseTypeDef(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResolveCaseResponseTypeDef(BaseValidatorModel):
    initialCaseStatus: str
    finalCaseStatus: str
    ResponseMetadata: ResponseMetadataTypeDef


class CommunicationTypeDef(BaseValidatorModel):
    caseId: Optional[str] = None
    body: Optional[str] = None
    submittedBy: Optional[str] = None
    timeCreated: Optional[str] = None
    attachmentSet: Optional[List[AttachmentDetailsTypeDef]] = None


class DescribeAttachmentResponseTypeDef(BaseValidatorModel):
    attachment: AttachmentOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class AttachmentTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    data: Optional[BlobTypeDef] = None


class ServiceTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    name: Optional[str] = None
    categories: Optional[List[CategoryTypeDef]] = None


class DescribeCasesRequestPaginateTypeDef(BaseValidatorModel):
    caseIdList: Optional[Sequence[str]] = None
    displayId: Optional[str] = None
    afterTime: Optional[str] = None
    beforeTime: Optional[str] = None
    includeResolvedCases: Optional[bool] = None
    language: Optional[str] = None
    includeCommunications: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCommunicationsRequestPaginateTypeDef(BaseValidatorModel):
    caseId: str
    beforeTime: Optional[str] = None
    afterTime: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSeverityLevelsResponseTypeDef(BaseValidatorModel):
    severityLevels: List[SeverityLevelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSupportedLanguagesResponseTypeDef(BaseValidatorModel):
    supportedLanguages: List[SupportedLanguageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef(BaseValidatorModel):
    statuses: List[TrustedAdvisorCheckRefreshStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RefreshTrustedAdvisorCheckResponseTypeDef(BaseValidatorModel):
    status: TrustedAdvisorCheckRefreshStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TrustedAdvisorCheckDescriptionTypeDef(BaseValidatorModel):
    pass


class DescribeTrustedAdvisorChecksResponseTypeDef(BaseValidatorModel):
    checks: List[TrustedAdvisorCheckDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TrustedAdvisorCategorySpecificSummaryTypeDef(BaseValidatorModel):
    costOptimizing: Optional[TrustedAdvisorCostOptimizingSummaryTypeDef] = None


class DescribeCommunicationsResponseTypeDef(BaseValidatorModel):
    communications: List[CommunicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecentCaseCommunicationsTypeDef(BaseValidatorModel):
    communications: Optional[List[CommunicationTypeDef]] = None
    nextToken: Optional[str] = None


class DescribeServicesResponseTypeDef(BaseValidatorModel):
    services: List[ServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CommunicationTypeOptionsTypeDef(BaseValidatorModel):
    pass


class DescribeCreateCaseOptionsResponseTypeDef(BaseValidatorModel):
    languageAvailability: str
    communicationTypes: List[CommunicationTypeOptionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TrustedAdvisorCheckResultTypeDef(BaseValidatorModel):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummaryTypeDef
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummaryTypeDef
    flaggedResources: List[TrustedAdvisorResourceDetailTypeDef]


class TrustedAdvisorCheckSummaryTypeDef(BaseValidatorModel):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: TrustedAdvisorResourcesSummaryTypeDef
    categorySpecificSummary: TrustedAdvisorCategorySpecificSummaryTypeDef
    hasFlaggedResources: Optional[bool] = None


class CaseDetailsTypeDef(BaseValidatorModel):
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


class AttachmentUnionTypeDef(BaseValidatorModel):
    pass


class AddAttachmentsToSetRequestTypeDef(BaseValidatorModel):
    attachments: Sequence[AttachmentUnionTypeDef]
    attachmentSetId: Optional[str] = None


class DescribeTrustedAdvisorCheckResultResponseTypeDef(BaseValidatorModel):
    result: TrustedAdvisorCheckResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTrustedAdvisorCheckSummariesResponseTypeDef(BaseValidatorModel):
    summaries: List[TrustedAdvisorCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCasesResponseTypeDef(BaseValidatorModel):
    cases: List[CaseDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


