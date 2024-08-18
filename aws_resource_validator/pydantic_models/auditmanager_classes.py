from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AWSAccountTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    emailAddress: Optional[str] = None
    name: Optional[str] = None

class AWSServiceTypeDef(BaseValidatorModel):
    serviceName: Optional[str] = None

class DelegationTypeDef(BaseValidatorModel):
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

class RoleTypeDef(BaseValidatorModel):
    roleType: RoleTypeType
    roleArn: str

class ControlCommentTypeDef(BaseValidatorModel):
    authorName: Optional[str] = None
    commentBody: Optional[str] = None
    postedDate: Optional[datetime] = None

class AssessmentEvidenceFolderTypeDef(BaseValidatorModel):
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

class AssessmentFrameworkMetadataTypeDef(BaseValidatorModel):
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

class AssessmentFrameworkShareRequestTypeDef(BaseValidatorModel):
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

class FrameworkMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    complianceType: Optional[str] = None

class AssessmentReportsDestinationTypeDef(BaseValidatorModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None

class AssessmentReportEvidenceErrorTypeDef(BaseValidatorModel):
    evidenceId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class AssessmentReportMetadataTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    author: Optional[str] = None
    status: Optional[AssessmentReportStatusType] = None
    creationTime: Optional[datetime] = None

class AssessmentReportTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    awsAccountId: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    author: Optional[str] = None
    status: Optional[AssessmentReportStatusType] = None
    creationTime: Optional[datetime] = None

class AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str

class BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDelegationRequestTypeDef(BaseValidatorModel):
    comment: Optional[str] = None
    controlSetId: Optional[str] = None
    roleArn: Optional[str] = None
    roleType: Optional[RoleTypeType] = None

class BatchDeleteDelegationByAssessmentErrorTypeDef(BaseValidatorModel):
    delegationId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchDeleteDelegationByAssessmentRequestRequestTypeDef(BaseValidatorModel):
    delegationIds: Sequence[str]
    assessmentId: str

class BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]

class ManualEvidenceTypeDef(BaseValidatorModel):
    s3ResourcePath: Optional[str] = None
    textResponse: Optional[str] = None
    evidenceFileName: Optional[str] = None

class ChangeLogTypeDef(BaseValidatorModel):
    objectType: Optional[ObjectTypeEnumType] = None
    objectName: Optional[str] = None
    action: Optional[ActionEnumType] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None

class EvidenceInsightsTypeDef(BaseValidatorModel):
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None

class SourceKeywordTypeDef(BaseValidatorModel):
    keywordInputType: Optional[KeywordInputTypeType] = None
    keywordValue: Optional[str] = None

class ControlMetadataTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    controlSources: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class CreateAssessmentFrameworkControlTypeDef(BaseValidatorModel):
    id: str

class CreateAssessmentReportRequestRequestTypeDef(BaseValidatorModel):
    name: str
    assessmentId: str
    description: Optional[str] = None
    queryStatement: Optional[str] = None

class DefaultExportDestinationTypeDef(BaseValidatorModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None

class DelegationMetadataTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    assessmentName: Optional[str] = None
    assessmentId: Optional[str] = None
    status: Optional[DelegationStatusType] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    controlSetName: Optional[str] = None

class DeleteAssessmentFrameworkRequestRequestTypeDef(BaseValidatorModel):
    frameworkId: str

class DeleteAssessmentFrameworkShareRequestRequestTypeDef(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType

class DeleteAssessmentReportRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    assessmentReportId: str

class DeleteAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str

class DeleteControlRequestRequestTypeDef(BaseValidatorModel):
    controlId: str

class DeregisterOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    adminAccountId: Optional[str] = None

class DeregistrationPolicyTypeDef(BaseValidatorModel):
    deleteResources: Optional[DeleteResourcesType] = None

class DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str

class EvidenceFinderEnablementTypeDef(BaseValidatorModel):
    eventDataStoreArn: Optional[str] = None
    enablementStatus: Optional[EvidenceFinderEnablementStatusType] = None
    backfillStatus: Optional[EvidenceFinderBackfillStatusType] = None
    error: Optional[str] = None

class ResourceTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    value: Optional[str] = None
    complianceCheck: Optional[str] = None

class GetAssessmentFrameworkRequestRequestTypeDef(BaseValidatorModel):
    frameworkId: str

class GetAssessmentReportUrlRequestRequestTypeDef(BaseValidatorModel):
    assessmentReportId: str
    assessmentId: str

class URLTypeDef(BaseValidatorModel):
    hyperlinkName: Optional[str] = None
    link: Optional[str] = None

class GetAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str

class GetChangeLogsRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: Optional[str] = None
    controlId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetControlRequestRequestTypeDef(BaseValidatorModel):
    controlId: str

class GetDelegationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceByEvidenceFolderRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceFileUploadUrlRequestRequestTypeDef(BaseValidatorModel):
    fileName: str

class GetEvidenceFolderRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str

class GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceFoldersByAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEvidenceRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    evidenceId: str

class GetInsightsByAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str

class InsightsByAssessmentTypeDef(BaseValidatorModel):
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None
    assessmentControlsCountByNoncompliantEvidence: Optional[int] = None
    totalAssessmentControlsCount: Optional[int] = None
    lastUpdated: Optional[datetime] = None

class InsightsTypeDef(BaseValidatorModel):
    activeAssessmentsCount: Optional[int] = None
    noncompliantEvidenceCount: Optional[int] = None
    compliantEvidenceCount: Optional[int] = None
    inconclusiveEvidenceCount: Optional[int] = None
    assessmentControlsCountByNoncompliantEvidence: Optional[int] = None
    totalAssessmentControlsCount: Optional[int] = None
    lastUpdated: Optional[datetime] = None

class ServiceMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

class GetSettingsRequestRequestTypeDef(BaseValidatorModel):
    attribute: SettingAttributeType

class ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef(BaseValidatorModel):
    controlDomainId: str
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentFrameworkShareRequestsRequestRequestTypeDef(BaseValidatorModel):
    requestType: ShareRequestTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentFrameworksRequestRequestTypeDef(BaseValidatorModel):
    frameworkType: FrameworkTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentReportsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssessmentsRequestRequestTypeDef(BaseValidatorModel):
    status: Optional[AssessmentStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlDomainInsightsByAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlDomainInsightsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlInsightsByControlDomainRequestRequestTypeDef(BaseValidatorModel):
    controlDomainId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListControlsRequestRequestTypeDef(BaseValidatorModel):
    controlType: ControlTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    controlCatalogId: Optional[str] = None

class ListKeywordsForDataSourceRequestRequestTypeDef(BaseValidatorModel):
    source: DataSourceTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListNotificationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class NotificationTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    assessmentId: Optional[str] = None
    assessmentName: Optional[str] = None
    controlSetId: Optional[str] = None
    controlSetName: Optional[str] = None
    description: Optional[str] = None
    eventTime: Optional[datetime] = None
    source: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class RegisterAccountRequestRequestTypeDef(BaseValidatorModel):
    kmsKey: Optional[str] = None
    delegatedAdminAccount: Optional[str] = None

class RegisterOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    adminAccountId: str

class StartAssessmentFrameworkShareRequestRequestTypeDef(BaseValidatorModel):
    frameworkId: str
    destinationAccount: str
    destinationRegion: str
    comment: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAssessmentControlRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    controlStatus: Optional[ControlStatusType] = None
    commentBody: Optional[str] = None

class UpdateAssessmentControlSetStatusRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    status: ControlSetStatusType
    comment: str

class UpdateAssessmentFrameworkShareRequestRequestTypeDef(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType
    action: ShareRequestActionType

class UpdateAssessmentStatusRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    status: AssessmentStatusType

class ValidateAssessmentReportIntegrityRequestRequestTypeDef(BaseValidatorModel):
    s3RelativePath: str

class ScopeOutputTypeDef(BaseValidatorModel):
    awsAccounts: Optional[List[AWSAccountTypeDef]] = None
    awsServices: Optional[List[AWSServiceTypeDef]] = None

class ScopeTypeDef(BaseValidatorModel):
    awsAccounts: Optional[Sequence[AWSAccountTypeDef]] = None
    awsServices: Optional[Sequence[AWSServiceTypeDef]] = None

class AssessmentMetadataItemTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    complianceType: Optional[str] = None
    status: Optional[AssessmentStatusType] = None
    roles: Optional[List[RoleTypeDef]] = None
    delegations: Optional[List[DelegationTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None

class AssessmentControlTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ControlStatusType] = None
    response: Optional[ControlResponseType] = None
    comments: Optional[List[ControlCommentTypeDef]] = None
    evidenceSources: Optional[List[str]] = None
    evidenceCount: Optional[int] = None
    assessmentReportEvidenceCount: Optional[int] = None

class BatchAssociateAssessmentReportEvidenceResponseTypeDef(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateAssessmentReportEvidenceResponseTypeDef(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentReportResponseTypeDef(BaseValidatorModel):
    assessmentReport: AssessmentReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterAccountResponseTypeDef(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountStatusResponseTypeDef(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFileUploadUrlResponseTypeDef(BaseValidatorModel):
    evidenceFileName: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFolderResponseTypeDef(BaseValidatorModel):
    evidenceFolder: AssessmentEvidenceFolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFoldersByAssessmentControlResponseTypeDef(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFoldersByAssessmentResponseTypeDef(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationAdminAccountResponseTypeDef(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentFrameworkShareRequestsResponseTypeDef(BaseValidatorModel):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequestTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentFrameworksResponseTypeDef(BaseValidatorModel):
    frameworkMetadataList: List[AssessmentFrameworkMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentReportsResponseTypeDef(BaseValidatorModel):
    assessmentReports: List[AssessmentReportMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeywordsForDataSourceResponseTypeDef(BaseValidatorModel):
    keywords: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAccountResponseTypeDef(BaseValidatorModel):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterOrganizationAdminAccountResponseTypeDef(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentFrameworkShareResponseTypeDef(BaseValidatorModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentFrameworkShareResponseTypeDef(BaseValidatorModel):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateAssessmentReportIntegrityResponseTypeDef(BaseValidatorModel):
    signatureValid: bool
    signatureAlgorithm: str
    signatureDateTime: str
    signatureKeyId: str
    validationErrors: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDelegationByAssessmentErrorTypeDef(BaseValidatorModel):
    createDelegationRequest: Optional[CreateDelegationRequestTypeDef] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchCreateDelegationByAssessmentRequestRequestTypeDef(BaseValidatorModel):
    createDelegationRequests: Sequence[CreateDelegationRequestTypeDef]
    assessmentId: str

class BatchDeleteDelegationByAssessmentResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchImportEvidenceToAssessmentControlErrorTypeDef(BaseValidatorModel):
    manualEvidence: Optional[ManualEvidenceTypeDef] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchImportEvidenceToAssessmentControlRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    manualEvidence: Sequence[ManualEvidenceTypeDef]

class GetChangeLogsResponseTypeDef(BaseValidatorModel):
    changeLogs: List[ChangeLogTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ControlDomainInsightsTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    controlsCountByNoncompliantEvidence: Optional[int] = None
    totalControlsCount: Optional[int] = None
    evidenceInsights: Optional[EvidenceInsightsTypeDef] = None
    lastUpdated: Optional[datetime] = None

class ControlInsightsMetadataByAssessmentItemTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    evidenceInsights: Optional[EvidenceInsightsTypeDef] = None
    controlSetName: Optional[str] = None
    lastUpdated: Optional[datetime] = None

class ControlInsightsMetadataItemTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    evidenceInsights: Optional[EvidenceInsightsTypeDef] = None
    lastUpdated: Optional[datetime] = None

class ControlMappingSourceTypeDef(BaseValidatorModel):
    sourceId: Optional[str] = None
    sourceName: Optional[str] = None
    sourceDescription: Optional[str] = None
    sourceSetUpOption: Optional[SourceSetUpOptionType] = None
    sourceType: Optional[SourceTypeType] = None
    sourceKeyword: Optional[SourceKeywordTypeDef] = None
    sourceFrequency: Optional[SourceFrequencyType] = None
    troubleshootingText: Optional[str] = None

class CreateControlMappingSourceTypeDef(BaseValidatorModel):
    sourceName: Optional[str] = None
    sourceDescription: Optional[str] = None
    sourceSetUpOption: Optional[SourceSetUpOptionType] = None
    sourceType: Optional[SourceTypeType] = None
    sourceKeyword: Optional[SourceKeywordTypeDef] = None
    sourceFrequency: Optional[SourceFrequencyType] = None
    troubleshootingText: Optional[str] = None

class ListControlsResponseTypeDef(BaseValidatorModel):
    controlMetadataList: List[ControlMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentFrameworkControlSetTypeDef(BaseValidatorModel):
    name: str
    controls: Optional[Sequence[CreateAssessmentFrameworkControlTypeDef]] = None

class UpdateAssessmentFrameworkControlSetTypeDef(BaseValidatorModel):
    name: str
    controls: Sequence[CreateAssessmentFrameworkControlTypeDef]
    id: Optional[str] = None

class GetDelegationsResponseTypeDef(BaseValidatorModel):
    delegations: List[DelegationMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsRequestRequestTypeDef(BaseValidatorModel):
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    defaultProcessOwners: Optional[Sequence[RoleTypeDef]] = None
    kmsKey: Optional[str] = None
    evidenceFinderEnabled: Optional[bool] = None
    deregistrationPolicy: Optional[DeregistrationPolicyTypeDef] = None
    defaultExportDestination: Optional[DefaultExportDestinationTypeDef] = None

class SettingsTypeDef(BaseValidatorModel):
    isAwsOrgEnabled: Optional[bool] = None
    snsTopic: Optional[str] = None
    defaultAssessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    defaultProcessOwners: Optional[List[RoleTypeDef]] = None
    kmsKey: Optional[str] = None
    evidenceFinderEnablement: Optional[EvidenceFinderEnablementTypeDef] = None
    deregistrationPolicy: Optional[DeregistrationPolicyTypeDef] = None
    defaultExportDestination: Optional[DefaultExportDestinationTypeDef] = None

class EvidenceTypeDef(BaseValidatorModel):
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

class GetAssessmentReportUrlResponseTypeDef(BaseValidatorModel):
    preSignedUrl: URLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsByAssessmentResponseTypeDef(BaseValidatorModel):
    insights: InsightsByAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsResponseTypeDef(BaseValidatorModel):
    insights: InsightsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServicesInScopeResponseTypeDef(BaseValidatorModel):
    serviceMetadata: List[ServiceMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationsResponseTypeDef(BaseValidatorModel):
    notifications: List[NotificationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentMetadataTypeDef(BaseValidatorModel):
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

class CreateAssessmentRequestRequestTypeDef(BaseValidatorModel):
    name: str
    assessmentReportsDestination: AssessmentReportsDestinationTypeDef
    scope: ScopeTypeDef
    roles: Sequence[RoleTypeDef]
    frameworkId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAssessmentRequestRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    scope: ScopeTypeDef
    assessmentName: Optional[str] = None
    assessmentDescription: Optional[str] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    roles: Optional[Sequence[RoleTypeDef]] = None

class ListAssessmentsResponseTypeDef(BaseValidatorModel):
    assessmentMetadata: List[AssessmentMetadataItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentControlSetTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ControlSetStatusType] = None
    roles: Optional[List[RoleTypeDef]] = None
    controls: Optional[List[AssessmentControlTypeDef]] = None
    delegations: Optional[List[DelegationTypeDef]] = None
    systemEvidenceCount: Optional[int] = None
    manualEvidenceCount: Optional[int] = None

class UpdateAssessmentControlResponseTypeDef(BaseValidatorModel):
    control: AssessmentControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDelegationByAssessmentResponseTypeDef(BaseValidatorModel):
    delegations: List[DelegationTypeDef]
    errors: List[BatchCreateDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchImportEvidenceToAssessmentControlResponseTypeDef(BaseValidatorModel):
    errors: List[BatchImportEvidenceToAssessmentControlErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlDomainInsightsByAssessmentResponseTypeDef(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlDomainInsightsResponseTypeDef(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentControlInsightsByControlDomainResponseTypeDef(BaseValidatorModel):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlInsightsByControlDomainResponseTypeDef(BaseValidatorModel):
    controlInsightsMetadata: List[ControlInsightsMetadataItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ControlTypeDef(BaseValidatorModel):
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

class UpdateControlRequestRequestTypeDef(BaseValidatorModel):
    controlId: str
    name: str
    controlMappingSources: Sequence[ControlMappingSourceTypeDef]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None

class CreateControlRequestRequestTypeDef(BaseValidatorModel):
    name: str
    controlMappingSources: Sequence[CreateControlMappingSourceTypeDef]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateAssessmentFrameworkRequestRequestTypeDef(BaseValidatorModel):
    name: str
    controlSets: Sequence[CreateAssessmentFrameworkControlSetTypeDef]
    description: Optional[str] = None
    complianceType: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateAssessmentFrameworkRequestRequestTypeDef(BaseValidatorModel):
    frameworkId: str
    name: str
    controlSets: Sequence[UpdateAssessmentFrameworkControlSetTypeDef]
    description: Optional[str] = None
    complianceType: Optional[str] = None

class GetSettingsResponseTypeDef(BaseValidatorModel):
    settings: SettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsResponseTypeDef(BaseValidatorModel):
    settings: SettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceByEvidenceFolderResponseTypeDef(BaseValidatorModel):
    evidence: List[EvidenceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceResponseTypeDef(BaseValidatorModel):
    evidence: EvidenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentFrameworkTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    metadata: Optional[FrameworkMetadataTypeDef] = None
    controlSets: Optional[List[AssessmentControlSetTypeDef]] = None

class UpdateAssessmentControlSetStatusResponseTypeDef(BaseValidatorModel):
    controlSet: AssessmentControlSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ControlSetTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    controls: Optional[List[ControlTypeDef]] = None

class CreateControlResponseTypeDef(BaseValidatorModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetControlResponseTypeDef(BaseValidatorModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateControlResponseTypeDef(BaseValidatorModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    awsAccount: Optional[AWSAccountTypeDef] = None
    metadata: Optional[AssessmentMetadataTypeDef] = None
    framework: Optional[AssessmentFrameworkTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class FrameworkTypeDef(BaseValidatorModel):
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

class CreateAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AssessmentTypeDef
    userRole: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentResponseTypeDef(BaseValidatorModel):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentStatusResponseTypeDef(BaseValidatorModel):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentFrameworkResponseTypeDef(BaseValidatorModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentFrameworkResponseTypeDef(BaseValidatorModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentFrameworkResponseTypeDef(BaseValidatorModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

