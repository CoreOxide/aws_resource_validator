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
from aws_resource_validator.pydantic_models.auditmanager_constants import *

class AWSService(BaseValidatorModel):
    serviceName: Optional[str] = None


class Role(BaseValidatorModel):
    roleType: RoleTypeType
    roleArn: str


class ControlComment(BaseValidatorModel):
    authorName: Optional[str] = None
    commentBody: Optional[str] = None
    postedDate: Optional[datetime] = None


class FrameworkMetadata(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    complianceType: Optional[str] = None


class AssessmentReportsDestination(BaseValidatorModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None


class AssessmentReportEvidenceError(BaseValidatorModel):
    evidenceId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class AssociateAssessmentReportEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str


class BatchAssociateAssessmentReportEvidenceRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDelegationRequest(BaseValidatorModel):
    comment: Optional[str] = None
    controlSetId: Optional[str] = None
    roleArn: Optional[str] = None
    roleType: Optional[RoleTypeType] = None


class BatchDeleteDelegationByAssessmentError(BaseValidatorModel):
    delegationId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchDeleteDelegationByAssessmentRequest(BaseValidatorModel):
    delegationIds: Sequence[str]
    assessmentId: str


class BatchDisassociateAssessmentReportEvidenceRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]


class ManualEvidence(BaseValidatorModel):
    s3ResourcePath: Optional[str] = None
    textResponse: Optional[str] = None
    evidenceFileName: Optional[str] = None


class ChangeLog(BaseValidatorModel):
    objectType: Optional[ObjectTypeEnumType] = None
    objectName: Optional[str] = None
    action: Optional[ActionEnumType] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None


class EvidenceInsights(BaseValidatorModel):
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None


class SourceKeyword(BaseValidatorModel):
    keywordInputType: Optional[KeywordInputTypeType] = None
    keywordValue: Optional[str] = None


class CreateAssessmentReportRequest(BaseValidatorModel):
    name: str
    assessmentId: str
    description: Optional[str] = None
    queryStatement: Optional[str] = None


class DefaultExportDestination(BaseValidatorModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None


class DeleteAssessmentFrameworkRequest(BaseValidatorModel):
    frameworkId: str


class DeleteAssessmentFrameworkShareRequest(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType


class DeleteAssessmentReportRequest(BaseValidatorModel):
    assessmentId: str
    assessmentReportId: str


class DeleteAssessmentRequest(BaseValidatorModel):
    assessmentId: str


class DeleteControlRequest(BaseValidatorModel):
    controlId: str


class DeregisterOrganizationAdminAccountRequest(BaseValidatorModel):
    adminAccountId: Optional[str] = None


class DeregistrationPolicy(BaseValidatorModel):
    deleteResources: Optional[DeleteResourcesType] = None


class DisassociateAssessmentReportEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str


class EvidenceFinderEnablement(BaseValidatorModel):
    eventDataStoreArn: Optional[str] = None
    enablementStatus: Optional[EvidenceFinderEnablementStatusType] = None
    backfillStatus: Optional[EvidenceFinderBackfillStatusType] = None
    error: Optional[str] = None


class Resource(BaseValidatorModel):
    arn: Optional[str] = None
    value: Optional[str] = None
    complianceCheck: Optional[str] = None


class GetAssessmentFrameworkRequest(BaseValidatorModel):
    frameworkId: str


class GetAssessmentReportUrlRequest(BaseValidatorModel):
    assessmentReportId: str
    assessmentId: str


class URL(BaseValidatorModel):
    hyperlinkName: Optional[str] = None
    link: Optional[str] = None


class GetAssessmentRequest(BaseValidatorModel):
    assessmentId: str


class GetChangeLogsRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: Optional[str] = None
    controlId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetControlRequest(BaseValidatorModel):
    controlId: str


class GetDelegationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceByEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceFileUploadUrlRequest(BaseValidatorModel):
    fileName: str


class GetEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str


class GetEvidenceFoldersByAssessmentControlRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceFoldersByAssessmentRequest(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    evidenceId: str


class GetInsightsByAssessmentRequest(BaseValidatorModel):
    assessmentId: str


class InsightsByAssessment(BaseValidatorModel):
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None
    assessmentControlsCountByNoncompliantEvidence: Optional[int] = None
    totalAssessmentControlsCount: Optional[int] = None
    lastUpdated: Optional[datetime] = None


class Insights(BaseValidatorModel):
    activeAssessmentsCount: Optional[int] = None
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None
    assessmentControlsCountByNoncompliantEvidence: Optional[int] = None
    totalAssessmentControlsCount: Optional[int] = None
    lastUpdated: Optional[datetime] = None


class ServiceMetadata(BaseValidatorModel):
    name: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None


class GetSettingsRequest(BaseValidatorModel):
    attribute: SettingAttributeType


class ListAssessmentControlInsightsByControlDomainRequest(BaseValidatorModel):
    controlDomainId: str
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentFrameworkShareRequestsRequest(BaseValidatorModel):
    requestType: ShareRequestTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentFrameworksRequest(BaseValidatorModel):
    frameworkType: FrameworkTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentReportsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentsRequest(BaseValidatorModel):
    status: Optional[AssessmentStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlDomainInsightsByAssessmentRequest(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlDomainInsightsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlInsightsByControlDomainRequest(BaseValidatorModel):
    controlDomainId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlsRequest(BaseValidatorModel):
    controlType: ControlTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    controlCatalogId: Optional[str] = None


class ListKeywordsForDataSourceRequest(BaseValidatorModel):
    source: DataSourceTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListNotificationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterAccountRequest(BaseValidatorModel):
    kmsKey: Optional[str] = None
    delegatedAdminAccount: Optional[str] = None


class RegisterOrganizationAdminAccountRequest(BaseValidatorModel):
    adminAccountId: str


class StartAssessmentFrameworkShareRequest(BaseValidatorModel):
    frameworkId: str
    destinationAccount: str
    destinationRegion: str
    comment: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAssessmentControlRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    controlStatus: Optional[ControlStatusType] = None
    commentBody: Optional[str] = None


class UpdateAssessmentControlSetStatusRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    status: ControlSetStatusType
    comment: str


class UpdateAssessmentFrameworkShareRequest(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType
    action: ShareRequestActionType


class UpdateAssessmentStatusRequest(BaseValidatorModel):
    assessmentId: str
    status: AssessmentStatusType


class ValidateAssessmentReportIntegrityRequest(BaseValidatorModel):
    s3RelativePath: str


class AWSAccount(BaseValidatorModel):
    pass


class ScopeOutput(BaseValidatorModel):
    awsAccounts: Optional[List[AWSAccount]] = None
    awsServices: Optional[List[AWSService]] = None


class Scope(BaseValidatorModel):
    awsAccounts: Optional[Sequence[AWSAccount]] = None
    awsServices: Optional[Sequence[AWSService]] = None


class BatchAssociateAssessmentReportEvidenceResponse(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceError]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateAssessmentReportEvidenceResponse(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceError]
    ResponseMetadata: ResponseMetadata


class AssessmentReport(BaseValidatorModel):
    pass


class CreateAssessmentReportResponse(BaseValidatorModel):
    assessmentReport: AssessmentReport
    ResponseMetadata: ResponseMetadata


class DeregisterAccountResponse(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadata


class GetAccountStatusResponse(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadata


class GetEvidenceFileUploadUrlResponse(BaseValidatorModel):
    evidenceFileName: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadata


class AssessmentEvidenceFolder(BaseValidatorModel):
    pass


class GetEvidenceFolderResponse(BaseValidatorModel):
    evidenceFolder: AssessmentEvidenceFolder
    ResponseMetadata: ResponseMetadata


class GetEvidenceFoldersByAssessmentControlResponse(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolder]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetEvidenceFoldersByAssessmentResponse(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolder]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetOrganizationAdminAccountResponse(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadata


class AssessmentFrameworkShareRequest(BaseValidatorModel):
    pass


class ListAssessmentFrameworkShareRequestsResponse(BaseValidatorModel):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequest]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentFrameworkMetadata(BaseValidatorModel):
    pass


class ListAssessmentFrameworksResponse(BaseValidatorModel):
    frameworkMetadataList: List[AssessmentFrameworkMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentReportMetadata(BaseValidatorModel):
    pass


class ListAssessmentReportsResponse(BaseValidatorModel):
    assessmentReports: List[AssessmentReportMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListKeywordsForDataSourceResponse(BaseValidatorModel):
    keywords: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RegisterAccountResponse(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadata


class RegisterOrganizationAdminAccountResponse(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadata


class StartAssessmentFrameworkShareResponse(BaseValidatorModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequest
    ResponseMetadata: ResponseMetadata


class UpdateAssessmentFrameworkShareResponse(BaseValidatorModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequest
    ResponseMetadata: ResponseMetadata


class ValidateAssessmentReportIntegrityResponse(BaseValidatorModel):
    signatureValid: bool
    signatureAlgorithm: str
    signatureDateTime: str
    signatureKeyId: str
    validationErrors: List[str]
    ResponseMetadata: ResponseMetadata


class BatchCreateDelegationByAssessmentError(BaseValidatorModel):
    createDelegationRequest: Optional[CreateDelegationRequest] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchCreateDelegationByAssessmentRequest(BaseValidatorModel):
    createDelegationRequests: Sequence[CreateDelegationRequest]
    assessmentId: str


class BatchDeleteDelegationByAssessmentResponse(BaseValidatorModel):
    errors: List[BatchDeleteDelegationByAssessmentError]
    ResponseMetadata: ResponseMetadata


class BatchImportEvidenceToAssessmentControlError(BaseValidatorModel):
    manualEvidence: Optional[ManualEvidence] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchImportEvidenceToAssessmentControlRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    manualEvidence: Sequence[ManualEvidence]


class GetChangeLogsResponse(BaseValidatorModel):
    changeLogs: List[ChangeLog]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ControlMappingSource(BaseValidatorModel):
    sourceId: Optional[str] = None
    sourceName: Optional[str] = None
    sourceDescription: Optional[str] = None
    sourceSetUpOption: Optional[SourceSetUpOptionType] = None
    sourceType: Optional[SourceTypeType] = None
    sourceKeyword: Optional[SourceKeyword] = None
    sourceFrequency: Optional[SourceFrequencyType] = None
    troubleshootingText: Optional[str] = None


class CreateControlMappingSource(BaseValidatorModel):
    sourceName: Optional[str] = None
    sourceDescription: Optional[str] = None
    sourceSetUpOption: Optional[SourceSetUpOptionType] = None
    sourceType: Optional[SourceTypeType] = None
    sourceKeyword: Optional[SourceKeyword] = None
    sourceFrequency: Optional[SourceFrequencyType] = None
    troubleshootingText: Optional[str] = None


class ControlMetadata(BaseValidatorModel):
    pass


class ListControlsResponse(BaseValidatorModel):
    controlMetadataList: List[ControlMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAssessmentFrameworkControl(BaseValidatorModel):
    pass


class CreateAssessmentFrameworkControlSet(BaseValidatorModel):
    name: str
    controls: Optional[Sequence[CreateAssessmentFrameworkControl]] = None


class DelegationMetadata(BaseValidatorModel):
    pass


class GetDelegationsResponse(BaseValidatorModel):
    delegations: List[DelegationMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateSettingsRequest(BaseValidatorModel):
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestination] = None
    defaultProcessOwners: Optional[Sequence[Role]] = None
    kmsKey: Optional[str] = None
    evidenceFinderEnabled: Optional[bool] = None
    deregistrationPolicy: Optional[DeregistrationPolicy] = None
    defaultExportDestination: Optional[DefaultExportDestination] = None


class Settings(BaseValidatorModel):
    isAwsOrgEnabled: Optional[bool] = None
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestination] = None
    defaultProcessOwners: Optional[List[Role]] = None
    kmsKey: Optional[str] = None
    evidenceFinderEnablement: Optional[EvidenceFinderEnablement] = None
    deregistrationPolicy: Optional[DeregistrationPolicy] = None
    defaultExportDestination: Optional[DefaultExportDestination] = None


class GetAssessmentReportUrlResponse(BaseValidatorModel):
    preSignedUrl: URL
    ResponseMetadata: ResponseMetadata


class GetInsightsByAssessmentResponse(BaseValidatorModel):
    insights: InsightsByAssessment
    ResponseMetadata: ResponseMetadata


class GetInsightsResponse(BaseValidatorModel):
    insights: Insights
    ResponseMetadata: ResponseMetadata


class GetServicesInScopeResponse(BaseValidatorModel):
    serviceMetadata: List[ServiceMetadata]
    ResponseMetadata: ResponseMetadata


class Notification(BaseValidatorModel):
    pass


class ListNotificationsResponse(BaseValidatorModel):
    notifications: List[Notification]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentMetadataItem(BaseValidatorModel):
    pass


class ListAssessmentsResponse(BaseValidatorModel):
    assessmentMetadata: List[AssessmentMetadataItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentControl(BaseValidatorModel):
    pass


class UpdateAssessmentControlResponse(BaseValidatorModel):
    control: AssessmentControl
    ResponseMetadata: ResponseMetadata


class Delegation(BaseValidatorModel):
    pass


class BatchCreateDelegationByAssessmentResponse(BaseValidatorModel):
    delegations: List[Delegation]
    errors: List[BatchCreateDelegationByAssessmentError]
    ResponseMetadata: ResponseMetadata


class BatchImportEvidenceToAssessmentControlResponse(BaseValidatorModel):
    errors: List[BatchImportEvidenceToAssessmentControlError]
    ResponseMetadata: ResponseMetadata


class ControlDomainInsights(BaseValidatorModel):
    pass


class ListControlDomainInsightsByAssessmentResponse(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsights]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListControlDomainInsightsResponse(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsights]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ControlInsightsMetadataByAssessmentItem(BaseValidatorModel):
    pass


class ListAssessmentControlInsightsByControlDomainResponse(BaseValidatorModel):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ControlInsightsMetadataItem(BaseValidatorModel):
    pass


class ListControlInsightsByControlDomainResponse(BaseValidatorModel):
    controlInsightsMetadata: List[ControlInsightsMetadataItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateControlRequest(BaseValidatorModel):
    controlId: str
    name: str
    controlMappingSources: Sequence[ControlMappingSource]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None


class CreateControlRequest(BaseValidatorModel):
    name: str
    controlMappingSources: Sequence[CreateControlMappingSource]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateAssessmentFrameworkRequest(BaseValidatorModel):
    name: str
    controlSets: Sequence[CreateAssessmentFrameworkControlSet]
    description: Optional[str] = None
    complianceType: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAssessmentFrameworkControlSet(BaseValidatorModel):
    pass


class UpdateAssessmentFrameworkRequest(BaseValidatorModel):
    frameworkId: str
    name: str
    controlSets: Sequence[UpdateAssessmentFrameworkControlSet]
    description: Optional[str] = None
    complianceType: Optional[str] = None


class GetSettingsResponse(BaseValidatorModel):
    settings: Settings
    ResponseMetadata: ResponseMetadata


class UpdateSettingsResponse(BaseValidatorModel):
    settings: Settings
    ResponseMetadata: ResponseMetadata


class Evidence(BaseValidatorModel):
    pass


class GetEvidenceByEvidenceFolderResponse(BaseValidatorModel):
    evidence: List[Evidence]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetEvidenceResponse(BaseValidatorModel):
    evidence: Evidence
    ResponseMetadata: ResponseMetadata


class ScopeUnion(BaseValidatorModel):
    pass


class CreateAssessmentRequest(BaseValidatorModel):
    name: str
    assessmentReportsDestination: AssessmentReportsDestination
    scope: ScopeUnion
    roles: Sequence[Role]
    frameworkId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAssessmentRequest(BaseValidatorModel):
    assessmentId: str
    scope: ScopeUnion
    assessmentName: Optional[str] = None
    assessmentDescription: Optional[str] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestination] = None
    roles: Optional[Sequence[Role]] = None


class AssessmentControlSet(BaseValidatorModel):
    pass


class UpdateAssessmentControlSetStatusResponse(BaseValidatorModel):
    controlSet: AssessmentControlSet
    ResponseMetadata: ResponseMetadata


class Control(BaseValidatorModel):
    pass


class CreateControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


class GetControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


class UpdateControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


class AssessmentMetadata(BaseValidatorModel):
    pass


class AssessmentFramework(BaseValidatorModel):
    pass


class Assessment(BaseValidatorModel):
    arn: Optional[str] = None
    awsAccount: Optional[AWSAccount] = None
    metadata: Optional[AssessmentMetadata] = None
    framework: Optional[AssessmentFramework] = None
    tags: Optional[Dict[str, str]] = None


class CreateAssessmentResponse(BaseValidatorModel):
    assessment: Assessment
    ResponseMetadata: ResponseMetadata


class GetAssessmentResponse(BaseValidatorModel):
    assessment: Assessment
    userRole: Role
    ResponseMetadata: ResponseMetadata


class UpdateAssessmentResponse(BaseValidatorModel):
    assessment: Assessment
    ResponseMetadata: ResponseMetadata


class UpdateAssessmentStatusResponse(BaseValidatorModel):
    assessment: Assessment
    ResponseMetadata: ResponseMetadata


class Framework(BaseValidatorModel):
    pass


class CreateAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


class GetAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


class UpdateAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


