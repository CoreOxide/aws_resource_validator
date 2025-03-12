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

class AWSServiceTypeDef(BaseValidatorModel):
    serviceName: Optional[str] = None


class RoleTypeDef(BaseValidatorModel):
    roleType: RoleTypeType
    roleArn: str


class ControlCommentTypeDef(BaseValidatorModel):
    authorName: Optional[str] = None
    commentBody: Optional[str] = None
    postedDate: Optional[datetime] = None


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


class AssociateAssessmentReportEvidenceFolderRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    evidenceFolderId: str


class BatchAssociateAssessmentReportEvidenceRequestTypeDef(BaseValidatorModel):
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


class BatchDeleteDelegationByAssessmentRequestTypeDef(BaseValidatorModel):
    delegationIds: Sequence[str]
    assessmentId: str


class BatchDisassociateAssessmentReportEvidenceRequestTypeDef(BaseValidatorModel):
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


class CreateAssessmentReportRequestTypeDef(BaseValidatorModel):
    name: str
    assessmentId: str
    description: Optional[str] = None
    queryStatement: Optional[str] = None


class DefaultExportDestinationTypeDef(BaseValidatorModel):
    destinationType: Optional[Literal["S3"]] = None
    destination: Optional[str] = None


class DeleteAssessmentFrameworkRequestTypeDef(BaseValidatorModel):
    frameworkId: str


class DeleteAssessmentFrameworkShareRequestTypeDef(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType


class DeleteAssessmentReportRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    assessmentReportId: str


class DeleteAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentId: str


class DeleteControlRequestTypeDef(BaseValidatorModel):
    controlId: str


class DeregisterOrganizationAdminAccountRequestTypeDef(BaseValidatorModel):
    adminAccountId: Optional[str] = None


class DeregistrationPolicyTypeDef(BaseValidatorModel):
    deleteResources: Optional[DeleteResourcesType] = None


class DisassociateAssessmentReportEvidenceFolderRequestTypeDef(BaseValidatorModel):
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


class GetAssessmentFrameworkRequestTypeDef(BaseValidatorModel):
    frameworkId: str


class GetAssessmentReportUrlRequestTypeDef(BaseValidatorModel):
    assessmentReportId: str
    assessmentId: str


class URLTypeDef(BaseValidatorModel):
    hyperlinkName: Optional[str] = None
    link: Optional[str] = None


class GetAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentId: str


class GetChangeLogsRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: Optional[str] = None
    controlId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetControlRequestTypeDef(BaseValidatorModel):
    controlId: str


class GetDelegationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceByEvidenceFolderRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceFileUploadUrlRequestTypeDef(BaseValidatorModel):
    fileName: str


class GetEvidenceFolderRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str


class GetEvidenceFoldersByAssessmentControlRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceFoldersByAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEvidenceRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    evidenceId: str


class GetInsightsByAssessmentRequestTypeDef(BaseValidatorModel):
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


class GetSettingsRequestTypeDef(BaseValidatorModel):
    attribute: SettingAttributeType


class ListAssessmentControlInsightsByControlDomainRequestTypeDef(BaseValidatorModel):
    controlDomainId: str
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentFrameworkShareRequestsRequestTypeDef(BaseValidatorModel):
    requestType: ShareRequestTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentFrameworksRequestTypeDef(BaseValidatorModel):
    frameworkType: FrameworkTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentReportsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssessmentsRequestTypeDef(BaseValidatorModel):
    status: Optional[AssessmentStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlDomainInsightsByAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlDomainInsightsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlInsightsByControlDomainRequestTypeDef(BaseValidatorModel):
    controlDomainId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListControlsRequestTypeDef(BaseValidatorModel):
    controlType: ControlTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    controlCatalogId: Optional[str] = None


class ListKeywordsForDataSourceRequestTypeDef(BaseValidatorModel):
    source: DataSourceTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListNotificationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class RegisterAccountRequestTypeDef(BaseValidatorModel):
    kmsKey: Optional[str] = None
    delegatedAdminAccount: Optional[str] = None


class RegisterOrganizationAdminAccountRequestTypeDef(BaseValidatorModel):
    adminAccountId: str


class StartAssessmentFrameworkShareRequestTypeDef(BaseValidatorModel):
    frameworkId: str
    destinationAccount: str
    destinationRegion: str
    comment: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAssessmentControlRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    controlStatus: Optional[ControlStatusType] = None
    commentBody: Optional[str] = None


class UpdateAssessmentControlSetStatusRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    status: ControlSetStatusType
    comment: str


class UpdateAssessmentFrameworkShareRequestTypeDef(BaseValidatorModel):
    requestId: str
    requestType: ShareRequestTypeType
    action: ShareRequestActionType


class UpdateAssessmentStatusRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    status: AssessmentStatusType


class ValidateAssessmentReportIntegrityRequestTypeDef(BaseValidatorModel):
    s3RelativePath: str


class AWSAccountTypeDef(BaseValidatorModel):
    pass


class ScopeOutputTypeDef(BaseValidatorModel):
    awsAccounts: Optional[List[AWSAccountTypeDef]] = None
    awsServices: Optional[List[AWSServiceTypeDef]] = None


class ScopeTypeDef(BaseValidatorModel):
    awsAccounts: Optional[Sequence[AWSAccountTypeDef]] = None
    awsServices: Optional[Sequence[AWSServiceTypeDef]] = None


class BatchAssociateAssessmentReportEvidenceResponseTypeDef(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDisassociateAssessmentReportEvidenceResponseTypeDef(BaseValidatorModel):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssessmentReportTypeDef(BaseValidatorModel):
    pass


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


class AssessmentEvidenceFolderTypeDef(BaseValidatorModel):
    pass


class GetEvidenceFolderResponseTypeDef(BaseValidatorModel):
    evidenceFolder: AssessmentEvidenceFolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetEvidenceFoldersByAssessmentControlResponseTypeDef(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetEvidenceFoldersByAssessmentResponseTypeDef(BaseValidatorModel):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetOrganizationAdminAccountResponseTypeDef(BaseValidatorModel):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssessmentFrameworkShareRequestTypeDef(BaseValidatorModel):
    pass


class ListAssessmentFrameworkShareRequestsResponseTypeDef(BaseValidatorModel):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssessmentFrameworkMetadataTypeDef(BaseValidatorModel):
    pass


class ListAssessmentFrameworksResponseTypeDef(BaseValidatorModel):
    frameworkMetadataList: List[AssessmentFrameworkMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssessmentReportMetadataTypeDef(BaseValidatorModel):
    pass


class ListAssessmentReportsResponseTypeDef(BaseValidatorModel):
    assessmentReports: List[AssessmentReportMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKeywordsForDataSourceResponseTypeDef(BaseValidatorModel):
    keywords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class BatchCreateDelegationByAssessmentRequestTypeDef(BaseValidatorModel):
    createDelegationRequests: Sequence[CreateDelegationRequestTypeDef]
    assessmentId: str


class BatchDeleteDelegationByAssessmentResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchImportEvidenceToAssessmentControlErrorTypeDef(BaseValidatorModel):
    manualEvidence: Optional[ManualEvidenceTypeDef] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchImportEvidenceToAssessmentControlRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    controlSetId: str
    controlId: str
    manualEvidence: Sequence[ManualEvidenceTypeDef]


class GetChangeLogsResponseTypeDef(BaseValidatorModel):
    changeLogs: List[ChangeLogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class ControlMetadataTypeDef(BaseValidatorModel):
    pass


class ListControlsResponseTypeDef(BaseValidatorModel):
    controlMetadataList: List[ControlMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateAssessmentFrameworkControlTypeDef(BaseValidatorModel):
    pass


class CreateAssessmentFrameworkControlSetTypeDef(BaseValidatorModel):
    name: str
    controls: Optional[Sequence[CreateAssessmentFrameworkControlTypeDef]] = None


class DelegationMetadataTypeDef(BaseValidatorModel):
    pass


class GetDelegationsResponseTypeDef(BaseValidatorModel):
    delegations: List[DelegationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateSettingsRequestTypeDef(BaseValidatorModel):
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


class NotificationTypeDef(BaseValidatorModel):
    pass


class ListNotificationsResponseTypeDef(BaseValidatorModel):
    notifications: List[NotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssessmentMetadataItemTypeDef(BaseValidatorModel):
    pass


class ListAssessmentsResponseTypeDef(BaseValidatorModel):
    assessmentMetadata: List[AssessmentMetadataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssessmentControlTypeDef(BaseValidatorModel):
    pass


class UpdateAssessmentControlResponseTypeDef(BaseValidatorModel):
    control: AssessmentControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DelegationTypeDef(BaseValidatorModel):
    pass


class BatchCreateDelegationByAssessmentResponseTypeDef(BaseValidatorModel):
    delegations: List[DelegationTypeDef]
    errors: List[BatchCreateDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchImportEvidenceToAssessmentControlResponseTypeDef(BaseValidatorModel):
    errors: List[BatchImportEvidenceToAssessmentControlErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ControlDomainInsightsTypeDef(BaseValidatorModel):
    pass


class ListControlDomainInsightsByAssessmentResponseTypeDef(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListControlDomainInsightsResponseTypeDef(BaseValidatorModel):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ControlInsightsMetadataByAssessmentItemTypeDef(BaseValidatorModel):
    pass


class ListAssessmentControlInsightsByControlDomainResponseTypeDef(BaseValidatorModel):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ControlInsightsMetadataItemTypeDef(BaseValidatorModel):
    pass


class ListControlInsightsByControlDomainResponseTypeDef(BaseValidatorModel):
    controlInsightsMetadata: List[ControlInsightsMetadataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateControlRequestTypeDef(BaseValidatorModel):
    controlId: str
    name: str
    controlMappingSources: Sequence[ControlMappingSourceTypeDef]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None


class CreateControlRequestTypeDef(BaseValidatorModel):
    name: str
    controlMappingSources: Sequence[CreateControlMappingSourceTypeDef]
    description: Optional[str] = None
    testingInformation: Optional[str] = None
    actionPlanTitle: Optional[str] = None
    actionPlanInstructions: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateAssessmentFrameworkRequestTypeDef(BaseValidatorModel):
    name: str
    controlSets: Sequence[CreateAssessmentFrameworkControlSetTypeDef]
    description: Optional[str] = None
    complianceType: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAssessmentFrameworkControlSetTypeDef(BaseValidatorModel):
    pass


class UpdateAssessmentFrameworkRequestTypeDef(BaseValidatorModel):
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


class EvidenceTypeDef(BaseValidatorModel):
    pass


class GetEvidenceByEvidenceFolderResponseTypeDef(BaseValidatorModel):
    evidence: List[EvidenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetEvidenceResponseTypeDef(BaseValidatorModel):
    evidence: EvidenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ScopeUnionTypeDef(BaseValidatorModel):
    pass


class CreateAssessmentRequestTypeDef(BaseValidatorModel):
    name: str
    assessmentReportsDestination: AssessmentReportsDestinationTypeDef
    scope: ScopeUnionTypeDef
    roles: Sequence[RoleTypeDef]
    frameworkId: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateAssessmentRequestTypeDef(BaseValidatorModel):
    assessmentId: str
    scope: ScopeUnionTypeDef
    assessmentName: Optional[str] = None
    assessmentDescription: Optional[str] = None
    assessmentReportsDestination: Optional[AssessmentReportsDestinationTypeDef] = None
    roles: Optional[Sequence[RoleTypeDef]] = None


class AssessmentControlSetTypeDef(BaseValidatorModel):
    pass


class UpdateAssessmentControlSetStatusResponseTypeDef(BaseValidatorModel):
    controlSet: AssessmentControlSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ControlTypeDef(BaseValidatorModel):
    pass


class CreateControlResponseTypeDef(BaseValidatorModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetControlResponseTypeDef(BaseValidatorModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateControlResponseTypeDef(BaseValidatorModel):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssessmentMetadataTypeDef(BaseValidatorModel):
    pass


class AssessmentFrameworkTypeDef(BaseValidatorModel):
    pass


class AssessmentTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    awsAccount: Optional[AWSAccountTypeDef] = None
    metadata: Optional[AssessmentMetadataTypeDef] = None
    framework: Optional[AssessmentFrameworkTypeDef] = None
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


class FrameworkTypeDef(BaseValidatorModel):
    pass


class CreateAssessmentFrameworkResponseTypeDef(BaseValidatorModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAssessmentFrameworkResponseTypeDef(BaseValidatorModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssessmentFrameworkResponseTypeDef(BaseValidatorModel):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


