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
from aws_resource_validator.pydantic_models.auditmanager_constants import *

class AWSAccountTypeDef(BaseModel):
    id: Optional[str] = None
    emailAddress: Optional[str] = None
    name: Optional[str] = None

class AWSServiceTypeDef(BaseModel):
    serviceName: Optional[str] = None

class DelegationTypeDef(BaseModel):
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

class RoleTypeDef(BaseModel):
    roleType: RoleTypeType
    roleArn: str

class ControlCommentTypeDef(BaseModel):
    authorName: Optional[str] = None
    commentBody: Optional[str] = None
    postedDate: Optional[datetime] = None

class AssessmentEvidenceFolderTypeDef(BaseModel):
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

class AssessmentFrameworkMetadataTypeDef(BaseModel):
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

class AssessmentFrameworkShareRequestTypeDef(BaseModel):
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

class FrameworkMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    complianceType: Optional[str] = None

class AssessmentReportsDestinationTypeDef(BaseModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None

class AssessmentReportEvidenceErrorTypeDef(BaseModel):
    evidenceId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class AssessmentReportMetadataTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    author: Optional[str] = None
    status: Optional[AssessmentReportStatusType] = None
    creationTime: Optional[datetime] = None

class AssessmentReportTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    awsAccountId: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    author: Optional[str] = None
    status: Optional[AssessmentReportStatusType] = None
    creationTime: Optional[datetime] = None

class AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef(BaseModel):
    assessmentId: str
    evidenceFolderId: str

class BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef(BaseModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDelegationRequestTypeDef(BaseModel):
    comment: Optional[str] = None
    controlSetId: Optional[str] = None
    roleArn: Optional[str] = None
    roleType: Optional[RoleTypeType] = None

class BatchDeleteDelegationByAssessmentErrorTypeDef(BaseModel):
    delegationId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchDeleteDelegationByAssessmentRequestRequestTypeDef(BaseModel):
    delegationIds: Sequence[str]
    assessmentId: str

class BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef(BaseModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]

class ManualEvidenceTypeDef(BaseModel):
    s3ResourcePath: Optional[str] = None
    textResponse: Optional[str] = None
    evidenceFileName: Optional[str] = None

class ChangeLogTypeDef(BaseModel):
    objectType: Optional[ObjectTypeEnumType] = None
    objectName: Optional[str] = None
    action: Optional[ActionEnumType] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None

class EvidenceInsightsTypeDef(BaseModel):
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None

class SourceKeywordTypeDef(BaseModel):
    keywordInputType: Optional[KeywordInputTypeType] = None
    keywordValue: Optional[str] = None

class ControlMetadataTypeDef(BaseModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    controlSources: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class CreateAssessmentFrameworkControlTypeDef(BaseModel):
    id: str

class CreateAssessmentReportRequestRequestTypeDef(BaseModel):
    name: str
    assessmentId: str
    description: Optional[str] = None
    queryStatement: Optional[str] = None

class DefaultExportDestinationTypeDef(BaseModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None

class DelegationMetadataTypeDef(BaseModel):
    id: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentId: Optional[str] = None
    status: Optional[DelegationStatusType] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    controlSetName: Optional[str] = None

class DeleteAssessmentFrameworkRequestRequestTypeDef(BaseModel):
    frameworkId: str

class DeleteAssessmentFrameworkShareRequestRequestTypeDef(BaseModel):
    requestId: str
    requestType: ShareRequestTypeType

class DeleteAssessmentReportRequestRequestTypeDef(BaseModel):
    assessmentId: str
    assessmentReportId: str

class DeleteAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str

class DeleteControlRequestRequestTypeDef(BaseModel):
    controlId: str

class DeregisterOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    adminAccountId: Optional[str] = None

class DeregistrationPolicyTypeDef(BaseModel):
    deleteResources: Optional[DeleteResourcesType] = None

class DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef(BaseModel):
    assessmentId: str
    evidenceFolderId: str

class EvidenceFinderEnablementTypeDef(BaseModel):
    eventDataStoreArn: Optional[str] = None
    enablementStatus: Optional[EvidenceFinderEnablementStatusType] = None
    backfillStatus: Optional[EvidenceFinderBackfillStatusType] = None
    error: Optional[str] = None

class ResourceTypeDef(BaseModel):
    arn: Optional[str] = None
    value: Optional[str] = None
    complianceCheck: Optional[str] = None

class GetAssessmentFrameworkRequestRequestTypeDef(BaseModel):
    frameworkId: str

class GetAssessmentReportUrlRequestRequestTypeDef(BaseModel):
    assessmentReportId: str
    assessmentId: str

class URLTypeDef(BaseModel):
    hyperlinkName: Optional[str] = None
    link: Optional[str] = None

class GetAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str

class GetChangeLogsRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: Optional[str] = None
    controlId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetControlRequestRequestTypeDef(BaseModel):
    controlId: str

class GetDelegationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceByEvidenceFolderRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceFileUploadUrlRequestRequestTypeDef(BaseModel):
    fileName: str

class GetEvidenceFolderRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str

class GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceFoldersByAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    evidenceId: str

class GetInsightsByAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str

class InsightsByAssessmentTypeDef(BaseModel):
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None
    assessmentControlsCountByNoncompliantEvidence: Optional[int] = None
    totalAssessmentControlsCount: Optional[int] = None
    lastUpdated: Optional[datetime] = None

class InsightsTypeDef(BaseModel):
    activeAssessmentsCount: Optional[int] = None
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None
    assessmentControlsCountByNoncompliantEvidence: Optional[int] = None
    totalAssessmentControlsCount: Optional[int] = None
    lastUpdated: Optional[datetime] = None

class ServiceMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

class GetSettingsRequestRequestTypeDef(BaseModel):
    attribute: SettingAttributeType

class ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef(BaseModel):
    controlDomainId: str
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentFrameworkShareRequestsRequestRequestTypeDef(BaseModel):
    requestType: ShareRequestTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentFrameworksRequestRequestTypeDef(BaseModel):
    frameworkType: FrameworkTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentReportsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentsRequestRequestTypeDef(BaseModel):
    status: Optional[AssessmentStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlDomainInsightsByAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlDomainInsightsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlInsightsByControlDomainRequestRequestTypeDef(BaseModel):
    controlDomainId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlsRequestRequestTypeDef(BaseModel):
    controlType: ControlTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    controlCatalogId: Optional[str] = None

class ListKeywordsForDataSourceRequestRequestTypeDef(BaseModel):
    source: DataSourceTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListNotificationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class NotificationTypeDef(BaseModel):
    id: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    controlSetId: Optional[str] = None
    controlSetName: Optional[str] = None
    description: Optional[str] = None
    eventTime: Optional[datetime] = None
    source: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RegisterAccountRequestRequestTypeDef(BaseModel):
    kmsKey: Optional[str] = None
    delegatedAdminAccount: Optional[str] = None

class RegisterOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    adminAccountId: str

class StartAssessmentFrameworkShareRequestRequestTypeDef(BaseModel):
    frameworkId: str
    destinationAccount: str
    destinationRegion: str
    comment: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAssessmentControlRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    controlStatus: Optional[ControlStatusType] = None
    commentBody: Optional[str] = None

class UpdateAssessmentControlSetStatusRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    status: ControlSetStatusType
    comment: str

class UpdateAssessmentFrameworkShareRequestRequestTypeDef(BaseModel):
    requestId: str
    requestType: ShareRequestTypeType
    action: ShareRequestActionType

class UpdateAssessmentStatusRequestRequestTypeDef(BaseModel):
    assessmentId: str
    status: AssessmentStatusType

class ValidateAssessmentReportIntegrityRequestRequestTypeDef(BaseModel):
    s3RelativePath: str

class ScopeOutputTypeDef(BaseModel):
    awsAccounts: Optional[List[AWSAccountTypeDef]] = None
    awsServices: Optional[List[AWSServiceTypeDef]] = None

class ScopeTypeDef(BaseModel):
    awsAccounts: Optional[Sequence[AWSAccountTypeDef]] = None
    awsServices: Optional[Sequence[AWSServiceTypeDef]] = None

class AssessmentMetadataItemTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    complianceType: Optional[str] = None
    status: Optional[AssessmentStatusType] = None
    roles: Optional[List[RoleTypeDef]] = None
    delegations: Optional[List[DelegationTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None

class AssessmentControlTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ControlStatusType] = None
    response: Optional[ControlResponseType] = None
    comments: Optional[List[ControlCommentTypeDef]] = None
    evidenceSources: Optional[List[str]] = None
    evidenceCount: Optional[int] = None
    assessmentReportEvidenceCount: Optional[int] = None

class BatchAssociateAssessmentReportEvidenceResponseTypeDef(BaseModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateAssessmentReportEvidenceResponseTypeDef(BaseModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentReportResponseTypeDef(BaseModel):
    assessmentReport: AssessmentReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterAccountResponseTypeDef(BaseModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountStatusResponseTypeDef(BaseModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFileUploadUrlResponseTypeDef(BaseModel):
    evidenceFileName: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFolderResponseTypeDef(BaseModel):
    evidenceFolder: AssessmentEvidenceFolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFoldersByAssessmentControlResponseTypeDef(BaseModel):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFoldersByAssessmentResponseTypeDef(BaseModel):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationAdminAccountResponseTypeDef(BaseModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentFrameworkShareRequestsResponseTypeDef(BaseModel):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequestTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentFrameworksResponseTypeDef(BaseModel):
    frameworkMetadataList: List[AssessmentFrameworkMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentReportsResponseTypeDef(BaseModel):
    assessmentReports: List[AssessmentReportMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeywordsForDataSourceResponseTypeDef(BaseModel):
    keywords: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAccountResponseTypeDef(BaseModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterOrganizationAdminAccountResponseTypeDef(BaseModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentFrameworkShareResponseTypeDef(BaseModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentFrameworkShareResponseTypeDef(BaseModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateAssessmentReportIntegrityResponseTypeDef(BaseModel):
    signatureValid: bool
    signatureAlgorithm: str
    signatureDateTime: str
    signatureKeyId: str
    validationErrors: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDelegationByAssessmentErrorTypeDef(BaseModel):
    createDelegationRequest: Optional[CreateDelegationRequestTypeDef] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchCreateDelegationByAssessmentRequestRequestTypeDef(BaseModel):
    createDelegationRequests: Sequence[CreateDelegationRequestTypeDef]
    assessmentId: str

class BatchDeleteDelegationByAssessmentResponseTypeDef(BaseModel):
    errors: List[BatchDeleteDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchImportEvidenceToAssessmentControlErrorTypeDef(BaseModel):
    manualEvidence: Optional[ManualEvidenceTypeDef] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchImportEvidenceToAssessmentControlRequestRequestTypeDef(BaseModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    manualEvidence: Sequence[ManualEvidenceTypeDef]

class GetChangeLogsResponseTypeDef(BaseModel):
    changeLogs: List[ChangeLogTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ControlDomainInsightsTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    controlsCountByNoncompliantEvidence: Optional[int] = None
    totalControlsCount: Optional[int] = None
    evidenceInsights: Optional[EvidenceInsightsTypeDef] = None
    lastUpdated: Optional[datetime] = None

class ControlInsightsMetadataByAssessmentItemTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    evidenceInsights: Optional[EvidenceInsightsTypeDef] = None
    controlSetName: Optional[str] = None
    lastUpdated: Optional[datetime] = None

class ControlInsightsMetadataItemTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    evidenceInsights: Optional[EvidenceInsightsTypeDef] = None
    lastUpdated: Optional[datetime] = None

class ControlMappingSourceTypeDef(BaseModel):
    sourceId: Optional[str] = None
    sourceName: Optional[str] = None
    sourceDescription: Optional[str] = None
    sourceSetUpOption: Optional[SourceSetUpOptionType] = None
    sourceType: Optional[SourceTypeType] = None
    sourceKeyword: Optional[SourceKeywordTypeDef] = None
    sourceFrequency: Optional[SourceFrequencyType] = None
    troubleshootingText: Optional[str] = None

class CreateControlMappingSourceTypeDef(BaseModel):
    sourceName: Optional[str] = None
    sourceDescription: Optional[str] = None
    sourceSetUpOption: Optional[SourceSetUpOptionType] = None
    sourceType: Optional[SourceTypeType] = None
    sourceKeyword: Optional[SourceKeywordTypeDef] = None
    sourceFrequency: Optional[SourceFrequencyType] = None
    troubleshootingText: Optional[str] = None

class ListControlsResponseTypeDef(BaseModel):
    controlMetadataList: List[ControlMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentFrameworkControlSetTypeDef(BaseModel):
    name: str
    controls: Optional[Sequence[CreateAssessmentFrameworkControlTypeDef]] = None

class UpdateAssessmentFrameworkControlSetTypeDef(BaseModel):
    name: str
    controls: Sequence[CreateAssessmentFrameworkControlTypeDef]
    id: Optional[str] = None

class GetDelegationsResponseTypeDef(BaseModel):
    delegations: List[DelegationMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsRequestRequestTypeDef(BaseModel):
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    defaultProcessOwners: Optional[Sequence[RoleTypeDef]] = None
    kmsKey: Optional[str] = None
    evidenceFinderEnabled: Optional[bool] = None
    deregistrationPolicy: Optional[DeregistrationPolicyTypeDef] = None
    defaultExportDestination: Optional[DefaultExportDestinationTypeDef] = None

class SettingsTypeDef(BaseModel):
    isAwsOrgEnabled: Optional[bool] = None
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    defaultProcessOwners: Optional[List[RoleTypeDef]] = None
    kmsKey: Optional[str] = None
    evidenceFinderEnablement: Optional[EvidenceFinderEnablementTypeDef] = None
    deregistrationPolicy: Optional[DeregistrationPolicyTypeDef] = None
    defaultExportDestination: Optional[DefaultExportDestinationTypeDef] = None

class EvidenceTypeDef(BaseModel):
    dataSource: Optional[str] = None
    evidenceAwsAccountId: Optional[str] = None
    time: Optional[datetime] = None
    eventSource: Optional[str] = None
    eventName: Optional[str] = None
    evidenceByType: Optional[str] = None
    resourcesIncluded: Optional[List[ResourceTypeDef]] = None
    attributes: Optional[Dict[str, str]] = None
    iamId: Optional[str] = None
    complianceCheck: Optional[str] = None
    awsOrganization: Optional[str] = None
    awsAccountId: Optional[str] = None
    evidenceFolderId: Optional[str] = None
    id: Optional[str] = None
    assessmentReportSelection: Optional[str] = None

class GetAssessmentReportUrlResponseTypeDef(BaseModel):
    preSignedUrl: URLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsByAssessmentResponseTypeDef(BaseModel):
    insights: InsightsByAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsResponseTypeDef(BaseModel):
    insights: InsightsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServicesInScopeResponseTypeDef(BaseModel):
    serviceMetadata: List[ServiceMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationsResponseTypeDef(BaseModel):
    notifications: List[NotificationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    description: Optional[str] = None
    complianceType: Optional[str] = None
    status: Optional[AssessmentStatusType] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    scope: Optional[ScopeOutputTypeDef] = None
    roles: Optional[List[RoleTypeDef]] = None
    delegations: Optional[List[DelegationTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None

class CreateAssessmentRequestRequestTypeDef(BaseModel):
    name: str
    assessmentReportsDestination: AssessmentReportsDestinationTypeDef
    scope: ScopeTypeDef
    roles: Sequence[RoleTypeDef]
    frameworkId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAssessmentRequestRequestTypeDef(BaseModel):
    assessmentId: str
    scope: ScopeTypeDef
    assessmentName: Optional[str] = None
    assessmentDescription: Optional[str] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    roles: Optional[Sequence[RoleTypeDef]] = None

class ListAssessmentsResponseTypeDef(BaseModel):
    assessmentMetadata: List[AssessmentMetadataItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentControlSetTypeDef(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ControlSetStatusType] = None
    roles: Optional[List[RoleTypeDef]] = None
    controls: Optional[List[AssessmentControlTypeDef]] = None
    delegations: Optional[List[DelegationTypeDef]] = None
    systemEvidenceCount: Optional[int] = None
    manualEvidenceCount: Optional[int] = None

class UpdateAssessmentControlResponseTypeDef(BaseModel):
    control: AssessmentControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDelegationByAssessmentResponseTypeDef(BaseModel):
    delegations: List[DelegationTypeDef]
    errors: List[BatchCreateDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchImportEvidenceToAssessmentControlResponseTypeDef(BaseModel):
    errors: List[BatchImportEvidenceToAssessmentControlErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlDomainInsightsByAssessmentResponseTypeDef(BaseModel):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlDomainInsightsResponseTypeDef(BaseModel):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentControlInsightsByControlDomainResponseTypeDef(BaseModel):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlInsightsByControlDomainResponseTypeDef(BaseModel):
    controlInsightsMetadata: List[ControlInsightsMetadataItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ControlTypeDef(BaseModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    type: Optional[ControlTypeType] = None
    name: Optional[str] = None
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    controlSources: Optional[str] = None
    controlMappingSources: Optional[List[ControlMappingSourceTypeDef]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    state: Optional[ControlStateType] = None

class UpdateControlRequestRequestTypeDef(BaseModel):
    controlId: str
    name: str
    controlMappingSources: Sequence[ControlMappingSourceTypeDef]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None

class CreateControlRequestRequestTypeDef(BaseModel):
    name: str
    controlMappingSources: Sequence[CreateControlMappingSourceTypeDef]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateAssessmentFrameworkRequestRequestTypeDef(BaseModel):
    name: str
    controlSets: Sequence[CreateAssessmentFrameworkControlSetTypeDef]
    description: Optional[str] = None
    complianceType: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAssessmentFrameworkRequestRequestTypeDef(BaseModel):
    frameworkId: str
    name: str
    controlSets: Sequence[UpdateAssessmentFrameworkControlSetTypeDef]
    description: Optional[str] = None
    complianceType: Optional[str] = None

class GetSettingsResponseTypeDef(BaseModel):
    settings: SettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsResponseTypeDef(BaseModel):
    settings: SettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceByEvidenceFolderResponseTypeDef(BaseModel):
    evidence: List[EvidenceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceResponseTypeDef(BaseModel):
    evidence: EvidenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentFrameworkTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    metadata: Optional[FrameworkMetadataTypeDef] = None
    controlSets: Optional[List[AssessmentControlSetTypeDef]] = None

class UpdateAssessmentControlSetStatusResponseTypeDef(BaseModel):
    controlSet: AssessmentControlSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ControlSetTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    controls: Optional[List[ControlTypeDef]] = None

class CreateControlResponseTypeDef(BaseModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetControlResponseTypeDef(BaseModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateControlResponseTypeDef(BaseModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentTypeDef(BaseModel):
    arn: Optional[str] = None
    awsAccount: Optional[AWSAccountTypeDef] = None
    metadata: Optional[AssessmentMetadataTypeDef] = None
    framework: Optional[AssessmentFrameworkTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class FrameworkTypeDef(BaseModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[FrameworkTypeType] = None
    complianceType: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    controlSources: Optional[str] = None
    controlSets: Optional[List[ControlSetTypeDef]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateAssessmentResponseTypeDef(BaseModel):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentResponseTypeDef(BaseModel):
    assessment: AssessmentTypeDef
    userRole: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentResponseTypeDef(BaseModel):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentStatusResponseTypeDef(BaseModel):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentFrameworkResponseTypeDef(BaseModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentFrameworkResponseTypeDef(BaseModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentFrameworkResponseTypeDef(BaseModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

