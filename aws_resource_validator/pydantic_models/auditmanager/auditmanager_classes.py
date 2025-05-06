from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.auditmanager.auditmanager_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AWSAccount(BaseValidatorModel):
    id: Optional[str] = None
    emailAddress: Optional[str] = None
    name: Optional[str] = None


class AWSService(BaseValidatorModel):
    serviceName: Optional[str] = None


class Delegation(BaseValidatorModel):
    id: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentId: Optional[str] = None
    status: Optional[DelegationStatusType] = None
    roleArn: Optional[str] = None
    roleType: Optional[RoleTypeType] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None
    controlSetId: Optional[str] = None
    comment: Optional[str] = None
    createdBy: Optional[str] = None


class Role(BaseValidatorModel):
    roleType: RoleTypeType
    roleArn: str


class ControlComment(BaseValidatorModel):
    authorName: Optional[str] = None
    commentBody: Optional[str] = None
    postedDate: Optional[datetime] = None


class AssessmentEvidenceFolder(BaseValidatorModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    assessmentId: Optional[str] = None
    controlSetId: Optional[str] = None
    controlId: Optional[str] = None
    id: Optional[str] = None
    dataSource: Optional[str] = None
    author: Optional[str] = None
    totalEvidence: Optional[int] = None
    assessmentReportSelectionCount: Optional[int] = None
    controlName: Optional[str] = None
    evidenceResourcesIncludedCount: Optional[int] = None
    evidenceByTypeConfigurationDataCount: Optional[int] = None
    evidenceByTypeManualCount: Optional[int] = None
    evidenceByTypeComplianceCheckCount: Optional[int] = None
    evidenceByTypeComplianceCheckIssuesCount: Optional[int] = None
    evidenceByTypeUserActivityCount: Optional[int] = None
    evidenceAwsServiceSourceCount: Optional[int] = None


class AssessmentFrameworkMetadata(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    type: Optional[FrameworkTypeType] = None
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    complianceType: Optional[str] = None
    controlsCount: Optional[int] = None
    controlSetsCount: Optional[int] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


class AssessmentFrameworkShareRequest(BaseValidatorModel):
    id: Optional[str] = None
    frameworkId: Optional[str] = None
    frameworkName: Optional[str] = None
    frameworkDescription: Optional[str] = None
    status: Optional[ShareRequestStatusType] = None
    sourceAccount: Optional[str] = None
    destinationAccount: Optional[str] = None
    destinationRegion: Optional[str] = None
    expirationTime: Optional[datetime] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None
    comment: Optional[str] = None
    standardControlsCount: Optional[int] = None
    customControlsCount: Optional[int] = None
    complianceType: Optional[str] = None


class FrameworkMetadata(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    complianceType: Optional[str] = None


class AssessmentReportsDestination(BaseValidatorModel):
    destinationType: Optional[Literal['S3']] = None
    destination: Optional[str] = None


class AssessmentReportEvidenceError(BaseValidatorModel):
    evidenceId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class AssessmentReportMetadata(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    author: Optional[str] = None
    status: Optional[AssessmentReportStatusType] = None
    creationTime: Optional[datetime] = None


class AssessmentReport(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    awsAccountId: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    author: Optional[str] = None
    status: Optional[AssessmentReportStatusType] = None
    creationTime: Optional[datetime] = None


class AssociateAssessmentReportEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str


class BatchAssociateAssessmentReportEvidenceRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: List[str]


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
    delegationIds: List[str]
    assessmentId: str


class BatchDisassociateAssessmentReportEvidenceRequest(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: List[str]


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


class ControlMetadata(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    controlSources: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


class CreateAssessmentFrameworkControl(BaseValidatorModel):
    id: str


class CreateAssessmentReportRequest(BaseValidatorModel):
    name: str
    assessmentId: str
    description: Optional[str] = None
    queryStatement: Optional[str] = None


class DefaultExportDestination(BaseValidatorModel):
    destinationType: Optional[Literal['S3']] = None
    destination: Optional[str] = None


class DelegationMetadata(BaseValidatorModel):
    id: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentId: Optional[str] = None
    status: Optional[DelegationStatusType] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    controlSetName: Optional[str] = None


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


class Notification(BaseValidatorModel):
    id: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    controlSetId: Optional[str] = None
    controlSetName: Optional[str] = None
    description: Optional[str] = None
    eventTime: Optional[datetime] = None
    source: Optional[str] = None


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
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


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


class ScopeOutput(BaseValidatorModel):
    awsAccounts: Optional[List[AWSAccount]] = None
    awsServices: Optional[List[AWSService]] = None


class Scope(BaseValidatorModel):
    awsAccounts: Optional[List[AWSAccount]] = None
    awsServices: Optional[List[AWSService]] = None


class AssessmentMetadataItem(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    complianceType: Optional[str] = None
    status: Optional[AssessmentStatusType] = None
    roles: Optional[List[Role]] = None
    delegations: Optional[List[Delegation]] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None


class AssessmentControl(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ControlStatusType] = None
    response: Optional[ControlResponseType] = None
    comments: Optional[List[ControlComment]] = None
    evidenceSources: Optional[List[str]] = None
    evidenceCount: Optional[int] = None
    assessmentReportEvidenceCount: Optional[int] = None


class BatchAssociateAssessmentReportEvidenceResponse(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceError]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateAssessmentReportEvidenceResponse(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceError]
    ResponseMetadata: ResponseMetadata


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


class ListAssessmentFrameworkShareRequestsResponse(BaseValidatorModel):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequest]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssessmentFrameworksResponse(BaseValidatorModel):
    frameworkMetadataList: List[AssessmentFrameworkMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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
    createDelegationRequests: List[CreateDelegationRequest]
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
    manualEvidence: List[ManualEvidence]


class GetChangeLogsResponse(BaseValidatorModel):
    changeLogs: List[ChangeLog]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ControlDomainInsights(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    controlsCountByNoncompliantEvidence: Optional[int] = None
    totalControlsCount: Optional[int] = None
    evidenceInsights: Optional[EvidenceInsights] = None
    lastUpdated: Optional[datetime] = None


class ControlInsightsMetadataByAssessmentItem(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    evidenceInsights: Optional[EvidenceInsights] = None
    controlSetName: Optional[str] = None
    lastUpdated: Optional[datetime] = None


class ControlInsightsMetadataItem(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    evidenceInsights: Optional[EvidenceInsights] = None
    lastUpdated: Optional[datetime] = None


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


class ListControlsResponse(BaseValidatorModel):
    controlMetadataList: List[ControlMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAssessmentFrameworkControlSet(BaseValidatorModel):
    name: str
    controls: Optional[List[CreateAssessmentFrameworkControl]] = None


class UpdateAssessmentFrameworkControlSet(BaseValidatorModel):
    name: str
    controls: List[CreateAssessmentFrameworkControl]
    id: Optional[str] = None


class GetDelegationsResponse(BaseValidatorModel):
    delegations: List[DelegationMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateSettingsRequest(BaseValidatorModel):
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestination] = None
    defaultProcessOwners: Optional[List[Role]] = None
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


class Evidence(BaseValidatorModel):
    dataSource: Optional[str] = None
    evidenceAwsAccountId: Optional[str] = None
    time: Optional[datetime] = None
    eventSource: Optional[str] = None
    eventName: Optional[str] = None
    evidenceByType: Optional[str] = None
    resourcesIncluded: Optional[List[Resource]] = None
    attributes: Optional[Dict[str, str]] = None
    iamId: Optional[str] = None
    complianceCheck: Optional[str] = None
    awsOrganization: Optional[str] = None
    awsAccountId: Optional[str] = None
    evidenceFolderId: Optional[str] = None
    id: Optional[str] = None
    assessmentReportSelection: Optional[str] = None


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


class ListNotificationsResponse(BaseValidatorModel):
    notifications: List[Notification]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentMetadata(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    description: Optional[str] = None
    complianceType: Optional[str] = None
    status: Optional[AssessmentStatusType] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestination] = None
    scope: Optional[ScopeOutput] = None
    roles: Optional[List[Role]] = None
    delegations: Optional[List[Delegation]] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None

ScopeUnion = Union[Scope, ScopeOutput]


class ListAssessmentsResponse(BaseValidatorModel):
    assessmentMetadata: List[AssessmentMetadataItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssessmentControlSet(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ControlSetStatusType] = None
    roles: Optional[List[Role]] = None
    controls: Optional[List[AssessmentControl]] = None
    delegations: Optional[List[Delegation]] = None
    systemEvidenceCount: Optional[int] = None
    manualEvidenceCount: Optional[int] = None


class UpdateAssessmentControlResponse(BaseValidatorModel):
    control: AssessmentControl
    ResponseMetadata: ResponseMetadata


class BatchCreateDelegationByAssessmentResponse(BaseValidatorModel):
    delegations: List[Delegation]
    errors: List[BatchCreateDelegationByAssessmentError]
    ResponseMetadata: ResponseMetadata


class BatchImportEvidenceToAssessmentControlResponse(BaseValidatorModel):
    errors: List[BatchImportEvidenceToAssessmentControlError]
    ResponseMetadata: ResponseMetadata


class ListControlDomainInsightsByAssessmentResponse(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsights]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListControlDomainInsightsResponse(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsights]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssessmentControlInsightsByControlDomainResponse(BaseValidatorModel):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListControlInsightsByControlDomainResponse(BaseValidatorModel):
    controlInsightsMetadata: List[ControlInsightsMetadataItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Control(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    type: Optional[ControlTypeType] = None
    name: Optional[str] = None
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    controlSources: Optional[str] = None
    controlMappingSources: Optional[List[ControlMappingSource]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    state: Optional[ControlStateType] = None


class UpdateControlRequest(BaseValidatorModel):
    controlId: str
    name: str
    controlMappingSources: List[ControlMappingSource]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None


class CreateControlRequest(BaseValidatorModel):
    name: str
    controlMappingSources: List[CreateControlMappingSource]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateAssessmentFrameworkRequest(BaseValidatorModel):
    name: str
    controlSets: List[CreateAssessmentFrameworkControlSet]
    description: Optional[str] = None
    complianceType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateAssessmentFrameworkRequest(BaseValidatorModel):
    frameworkId: str
    name: str
    controlSets: List[UpdateAssessmentFrameworkControlSet]
    description: Optional[str] = None
    complianceType: Optional[str] = None


class GetSettingsResponse(BaseValidatorModel):
    settings: Settings
    ResponseMetadata: ResponseMetadata


class UpdateSettingsResponse(BaseValidatorModel):
    settings: Settings
    ResponseMetadata: ResponseMetadata


class GetEvidenceByEvidenceFolderResponse(BaseValidatorModel):
    evidence: List[Evidence]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetEvidenceResponse(BaseValidatorModel):
    evidence: Evidence
    ResponseMetadata: ResponseMetadata


class CreateAssessmentRequest(BaseValidatorModel):
    name: str
    assessmentReportsDestination: AssessmentReportsDestination
    scope: ScopeUnion
    roles: List[Role]
    frameworkId: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateAssessmentRequest(BaseValidatorModel):
    assessmentId: str
    scope: ScopeUnion
    assessmentName: Optional[str] = None
    assessmentDescription: Optional[str] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestination] = None
    roles: Optional[List[Role]] = None


class AssessmentFramework(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    metadata: Optional[FrameworkMetadata] = None
    controlSets: Optional[List[AssessmentControlSet]] = None


class UpdateAssessmentControlSetStatusResponse(BaseValidatorModel):
    controlSet: AssessmentControlSet
    ResponseMetadata: ResponseMetadata


class ControlSet(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    controls: Optional[List[Control]] = None


class CreateControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


class GetControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


class UpdateControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


class Assessment(BaseValidatorModel):
    arn: Optional[str] = None
    awsAccount: Optional[AWSAccount] = None
    metadata: Optional[AssessmentMetadata] = None
    framework: Optional[AssessmentFramework] = None
    tags: Optional[Dict[str, str]] = None


class Framework(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[FrameworkTypeType] = None
    complianceType: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    controlSources: Optional[str] = None
    controlSets: Optional[List[ControlSet]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
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


class CreateAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


class GetAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


class UpdateAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata