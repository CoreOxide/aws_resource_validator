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


# This class is the input for the 'batch_associate_assessment_report_evidence' function.
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


# This class is the input for the 'batch_delete_delegation_by_assessment' function.
class BatchDeleteDelegationByAssessmentRequest(BaseValidatorModel):
    delegationIds: List[str]
    assessmentId: str


# This class is the input for the 'batch_disassociate_assessment_report_evidence' function.
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


# This class is the input for the 'create_assessment_report' function.
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


# This class is the input for the 'get_assessment_framework' function.
class GetAssessmentFrameworkRequest(BaseValidatorModel):
    frameworkId: str


# This class is the input for the 'get_assessment_report_url' function.
class GetAssessmentReportUrlRequest(BaseValidatorModel):
    assessmentReportId: str
    assessmentId: str


class URL(BaseValidatorModel):
    hyperlinkName: Optional[str] = None
    link: Optional[str] = None


# This class is the input for the 'get_assessment' function.
class GetAssessmentRequest(BaseValidatorModel):
    assessmentId: str


# This class is the input for the 'get_change_logs' function.
class GetChangeLogsRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: Optional[str] = None
    controlId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_control' function.
class GetControlRequest(BaseValidatorModel):
    controlId: str


# This class is the input for the 'get_delegations' function.
class GetDelegationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_evidence_by_evidence_folder' function.
class GetEvidenceByEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_evidence_file_upload_url' function.
class GetEvidenceFileUploadUrlRequest(BaseValidatorModel):
    fileName: str


# This class is the input for the 'get_evidence_folder' function.
class GetEvidenceFolderRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str


# This class is the input for the 'get_evidence_folders_by_assessment_control' function.
class GetEvidenceFoldersByAssessmentControlRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_evidence_folders_by_assessment' function.
class GetEvidenceFoldersByAssessmentRequest(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_evidence' function.
class GetEvidenceRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    evidenceId: str


# This class is the input for the 'get_insights_by_assessment' function.
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


# This class is the input for the 'get_settings' function.
class GetSettingsRequest(BaseValidatorModel):
    attribute: SettingAttributeType


# This class is the input for the 'list_assessment_control_insights_by_control_domain' function.
class ListAssessmentControlInsightsByControlDomainRequest(BaseValidatorModel):
    controlDomainId: str
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_assessment_framework_share_requests' function.
class ListAssessmentFrameworkShareRequestsRequest(BaseValidatorModel):
    requestType: ShareRequestTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_assessment_frameworks' function.
class ListAssessmentFrameworksRequest(BaseValidatorModel):
    frameworkType: FrameworkTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_assessment_reports' function.
class ListAssessmentReportsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_assessments' function.
class ListAssessmentsRequest(BaseValidatorModel):
    status: Optional[AssessmentStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_control_domain_insights_by_assessment' function.
class ListControlDomainInsightsByAssessmentRequest(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_control_domain_insights' function.
class ListControlDomainInsightsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_control_insights_by_control_domain' function.
class ListControlInsightsByControlDomainRequest(BaseValidatorModel):
    controlDomainId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_controls' function.
class ListControlsRequest(BaseValidatorModel):
    controlType: ControlTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    controlCatalogId: Optional[str] = None


# This class is the input for the 'list_keywords_for_data_source' function.
class ListKeywordsForDataSourceRequest(BaseValidatorModel):
    source: DataSourceTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_notifications' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'register_account' function.
class RegisterAccountRequest(BaseValidatorModel):
    kmsKey: Optional[str] = None
    delegatedAdminAccount: Optional[str] = None


# This class is the input for the 'register_organization_admin_account' function.
class RegisterOrganizationAdminAccountRequest(BaseValidatorModel):
    adminAccountId: str


# This class is the input for the 'start_assessment_framework_share' function.
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


# This class is the input for the 'update_assessment_control' function.
class UpdateAssessmentControlRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    controlStatus: Optional[ControlStatusType] = None
    commentBody: Optional[str] = None


# This class is the input for the 'update_assessment_control_set_status' function.
class UpdateAssessmentControlSetStatusRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    status: ControlSetStatusType
    comment: str


# This class is the input for the 'update_assessment_framework_share' function.
class UpdateAssessmentFrameworkShareRequest(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType
    action: ShareRequestActionType


# This class is the input for the 'update_assessment_status' function.
class UpdateAssessmentStatusRequest(BaseValidatorModel):
    assessmentId: str
    status: AssessmentStatusType


# This class is the input for the 'validate_assessment_report_integrity' function.
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


# This class is the output for the 'batch_associate_assessment_report_evidence' function.
class BatchAssociateAssessmentReportEvidenceResponse(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_assessment_report_evidence' function.
class BatchDisassociateAssessmentReportEvidenceResponse(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_assessment_report' function.
class CreateAssessmentReportResponse(BaseValidatorModel):
    assessmentReport: AssessmentReport
    ResponseMetadata: ResponseMetadata


class DeregisterAccountResponse(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadata


class GetAccountStatusResponse(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_evidence_file_upload_url' function.
class GetEvidenceFileUploadUrlResponse(BaseValidatorModel):
    evidenceFileName: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_evidence_folder' function.
class GetEvidenceFolderResponse(BaseValidatorModel):
    evidenceFolder: AssessmentEvidenceFolder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_evidence_folders_by_assessment_control' function.
class GetEvidenceFoldersByAssessmentControlResponse(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolder]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_evidence_folders_by_assessment' function.
class GetEvidenceFoldersByAssessmentResponse(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolder]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetOrganizationAdminAccountResponse(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_assessment_framework_share_requests' function.
class ListAssessmentFrameworkShareRequestsResponse(BaseValidatorModel):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequest]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_assessment_frameworks' function.
class ListAssessmentFrameworksResponse(BaseValidatorModel):
    frameworkMetadataList: List[AssessmentFrameworkMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_assessment_reports' function.
class ListAssessmentReportsResponse(BaseValidatorModel):
    assessmentReports: List[AssessmentReportMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_keywords_for_data_source' function.
class ListKeywordsForDataSourceResponse(BaseValidatorModel):
    keywords: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_account' function.
class RegisterAccountResponse(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_organization_admin_account' function.
class RegisterOrganizationAdminAccountResponse(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_assessment_framework_share' function.
class StartAssessmentFrameworkShareResponse(BaseValidatorModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_assessment_framework_share' function.
class UpdateAssessmentFrameworkShareResponse(BaseValidatorModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'validate_assessment_report_integrity' function.
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


# This class is the input for the 'batch_create_delegation_by_assessment' function.
class BatchCreateDelegationByAssessmentRequest(BaseValidatorModel):
    createDelegationRequests: List[CreateDelegationRequest]
    assessmentId: str


# This class is the output for the 'batch_delete_delegation_by_assessment' function.
class BatchDeleteDelegationByAssessmentResponse(BaseValidatorModel):
    errors: List[BatchDeleteDelegationByAssessmentError]
    ResponseMetadata: ResponseMetadata


class BatchImportEvidenceToAssessmentControlError(BaseValidatorModel):
    manualEvidence: Optional[ManualEvidence] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'batch_import_evidence_to_assessment_control' function.
class BatchImportEvidenceToAssessmentControlRequest(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    manualEvidence: List[ManualEvidence]


# This class is the output for the 'get_change_logs' function.
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


# This class is the output for the 'list_controls' function.
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


# This class is the output for the 'get_delegations' function.
class GetDelegationsResponse(BaseValidatorModel):
    delegations: List[DelegationMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'update_settings' function.
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


# This class is the output for the 'get_assessment_report_url' function.
class GetAssessmentReportUrlResponse(BaseValidatorModel):
    preSignedUrl: URL
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_insights_by_assessment' function.
class GetInsightsByAssessmentResponse(BaseValidatorModel):
    insights: InsightsByAssessment
    ResponseMetadata: ResponseMetadata


class GetInsightsResponse(BaseValidatorModel):
    insights: Insights
    ResponseMetadata: ResponseMetadata


class GetServicesInScopeResponse(BaseValidatorModel):
    serviceMetadata: List[ServiceMetadata]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_notifications' function.
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


# This class is the output for the 'list_assessments' function.
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


# This class is the output for the 'update_assessment_control' function.
class UpdateAssessmentControlResponse(BaseValidatorModel):
    control: AssessmentControl
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_create_delegation_by_assessment' function.
class BatchCreateDelegationByAssessmentResponse(BaseValidatorModel):
    delegations: List[Delegation]
    errors: List[BatchCreateDelegationByAssessmentError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_import_evidence_to_assessment_control' function.
class BatchImportEvidenceToAssessmentControlResponse(BaseValidatorModel):
    errors: List[BatchImportEvidenceToAssessmentControlError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_control_domain_insights_by_assessment' function.
class ListControlDomainInsightsByAssessmentResponse(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsights]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_control_domain_insights' function.
class ListControlDomainInsightsResponse(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsights]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_assessment_control_insights_by_control_domain' function.
class ListAssessmentControlInsightsByControlDomainResponse(BaseValidatorModel):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_control_insights_by_control_domain' function.
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


# This class is the input for the 'update_control' function.
class UpdateControlRequest(BaseValidatorModel):
    controlId: str
    name: str
    controlMappingSources: List[ControlMappingSource]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None


# This class is the input for the 'create_control' function.
class CreateControlRequest(BaseValidatorModel):
    name: str
    controlMappingSources: List[CreateControlMappingSource]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_assessment_framework' function.
class CreateAssessmentFrameworkRequest(BaseValidatorModel):
    name: str
    controlSets: List[CreateAssessmentFrameworkControlSet]
    description: Optional[str] = None
    complianceType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_assessment_framework' function.
class UpdateAssessmentFrameworkRequest(BaseValidatorModel):
    frameworkId: str
    name: str
    controlSets: List[UpdateAssessmentFrameworkControlSet]
    description: Optional[str] = None
    complianceType: Optional[str] = None


# This class is the output for the 'get_settings' function.
class GetSettingsResponse(BaseValidatorModel):
    settings: Settings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_settings' function.
class UpdateSettingsResponse(BaseValidatorModel):
    settings: Settings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_evidence_by_evidence_folder' function.
class GetEvidenceByEvidenceFolderResponse(BaseValidatorModel):
    evidence: List[Evidence]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_evidence' function.
class GetEvidenceResponse(BaseValidatorModel):
    evidence: Evidence
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_assessment' function.
class CreateAssessmentRequest(BaseValidatorModel):
    name: str
    assessmentReportsDestination: AssessmentReportsDestination
    scope: ScopeUnion
    roles: List[Role]
    frameworkId: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_assessment' function.
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


# This class is the output for the 'update_assessment_control_set_status' function.
class UpdateAssessmentControlSetStatusResponse(BaseValidatorModel):
    controlSet: AssessmentControlSet
    ResponseMetadata: ResponseMetadata


class ControlSet(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    controls: Optional[List[Control]] = None


# This class is the output for the 'create_control' function.
class CreateControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_control' function.
class GetControlResponse(BaseValidatorModel):
    control: Control
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_control' function.
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


# This class is the output for the 'create_assessment' function.
class CreateAssessmentResponse(BaseValidatorModel):
    assessment: Assessment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_assessment' function.
class GetAssessmentResponse(BaseValidatorModel):
    assessment: Assessment
    userRole: Role
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_assessment' function.
class UpdateAssessmentResponse(BaseValidatorModel):
    assessment: Assessment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_assessment_status' function.
class UpdateAssessmentStatusResponse(BaseValidatorModel):
    assessment: Assessment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_assessment_framework' function.
class CreateAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_assessment_framework' function.
class GetAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_assessment_framework' function.
class UpdateAssessmentFrameworkResponse(BaseValidatorModel):
    framework: Framework
    ResponseMetadata: ResponseMetadata