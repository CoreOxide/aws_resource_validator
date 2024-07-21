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
from aws_resource_validator.pydantic_models.wellarchitected_constants import *

class AccountJiraConfigurationInputTypeDef(BaseModel):
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    IntegrationStatus: Optional[Literal["NOT_CONFIGURED"]] = None

class AccountJiraConfigurationOutputTypeDef(BaseModel):
    IntegrationStatus: Optional[IntegrationStatusType] = None
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    Subdomain: Optional[str] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None

class ChoiceContentTypeDef(BaseModel):
    DisplayText: Optional[str] = None
    Url: Optional[str] = None

class ChoiceAnswerSummaryTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    Status: Optional[ChoiceStatusType] = None
    Reason: Optional[ChoiceReasonType] = None

class JiraConfigurationTypeDef(BaseModel):
    JiraIssueUrl: Optional[str] = None
    LastSyncedTime: Optional[datetime] = None

class ChoiceAnswerTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    Status: Optional[ChoiceStatusType] = None
    Reason: Optional[ChoiceReasonType] = None
    Notes: Optional[str] = None

class AssociateLensesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAliases: Sequence[str]

class AssociateProfilesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    ProfileArns: Sequence[str]

class BestPracticeTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None

class CheckDetailTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Provider: Optional[Literal["TRUSTED_ADVISOR"]] = None
    LensArn: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionId: Optional[str] = None
    ChoiceId: Optional[str] = None
    Status: Optional[CheckStatusType] = None
    AccountId: Optional[str] = None
    FlaggedResources: Optional[int] = None
    Reason: Optional[CheckFailureReasonType] = None
    UpdatedAt: Optional[datetime] = None

class CheckSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Provider: Optional[Literal["TRUSTED_ADVISOR"]] = None
    Description: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    LensArn: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionId: Optional[str] = None
    ChoiceId: Optional[str] = None
    Status: Optional[CheckStatusType] = None
    AccountSummary: Optional[Dict[CheckStatusType, int]] = None

class ChoiceImprovementPlanTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    DisplayText: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None

class ChoiceUpdateTypeDef(BaseModel):
    Status: ChoiceStatusType
    Reason: Optional[ChoiceReasonType] = None
    Notes: Optional[str] = None

class CreateLensShareInputRequestTypeDef(BaseModel):
    LensAlias: str
    SharedWith: str
    ClientRequestToken: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateLensVersionInputRequestTypeDef(BaseModel):
    LensAlias: str
    LensVersion: str
    ClientRequestToken: str
    IsMajorVersion: Optional[bool] = None

class CreateMilestoneInputRequestTypeDef(BaseModel):
    WorkloadId: str
    MilestoneName: str
    ClientRequestToken: str

class ProfileQuestionUpdateTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    SelectedChoiceIds: Optional[Sequence[str]] = None

class CreateProfileShareInputRequestTypeDef(BaseModel):
    ProfileArn: str
    SharedWith: str
    ClientRequestToken: str

class CreateReviewTemplateInputRequestTypeDef(BaseModel):
    TemplateName: str
    Description: str
    Lenses: Sequence[str]
    ClientRequestToken: str
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateTemplateShareInputRequestTypeDef(BaseModel):
    TemplateArn: str
    SharedWith: str
    ClientRequestToken: str

class WorkloadDiscoveryConfigTypeDef(BaseModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[Sequence[DefinitionTypeType]] = None

class WorkloadJiraConfigurationInputTypeDef(BaseModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None

class CreateWorkloadShareInputRequestTypeDef(BaseModel):
    WorkloadId: str
    SharedWith: str
    PermissionType: PermissionTypeType
    ClientRequestToken: str

class DeleteLensInputRequestTypeDef(BaseModel):
    LensAlias: str
    ClientRequestToken: str
    LensStatus: LensStatusTypeType

class DeleteLensShareInputRequestTypeDef(BaseModel):
    ShareId: str
    LensAlias: str
    ClientRequestToken: str

class DeleteProfileInputRequestTypeDef(BaseModel):
    ProfileArn: str
    ClientRequestToken: str

class DeleteProfileShareInputRequestTypeDef(BaseModel):
    ShareId: str
    ProfileArn: str
    ClientRequestToken: str

class DeleteReviewTemplateInputRequestTypeDef(BaseModel):
    TemplateArn: str
    ClientRequestToken: str

class DeleteTemplateShareInputRequestTypeDef(BaseModel):
    ShareId: str
    TemplateArn: str
    ClientRequestToken: str

class DeleteWorkloadInputRequestTypeDef(BaseModel):
    WorkloadId: str
    ClientRequestToken: str

class DeleteWorkloadShareInputRequestTypeDef(BaseModel):
    ShareId: str
    WorkloadId: str
    ClientRequestToken: str

class DisassociateLensesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAliases: Sequence[str]

class DisassociateProfilesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    ProfileArns: Sequence[str]

class ExportLensInputRequestTypeDef(BaseModel):
    LensAlias: str
    LensVersion: Optional[str] = None

class GetAnswerInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    MilestoneNumber: Optional[int] = None

class GetConsolidatedReportInputRequestTypeDef(BaseModel):
    Format: ReportFormatType
    IncludeSharedResources: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetLensInputRequestTypeDef(BaseModel):
    LensAlias: str
    LensVersion: Optional[str] = None

class LensTypeDef(BaseModel):
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    ShareInvitationId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class GetLensReviewInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None

class GetLensReviewReportInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None

class LensReviewReportTypeDef(BaseModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    Base64String: Optional[str] = None

class GetLensVersionDifferenceInputRequestTypeDef(BaseModel):
    LensAlias: str
    BaseLensVersion: Optional[str] = None
    TargetLensVersion: Optional[str] = None

class GetMilestoneInputRequestTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int

class GetProfileInputRequestTypeDef(BaseModel):
    ProfileArn: str
    ProfileVersion: Optional[str] = None

class GetReviewTemplateAnswerInputRequestTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str

class GetReviewTemplateInputRequestTypeDef(BaseModel):
    TemplateArn: str

class GetReviewTemplateLensReviewInputRequestTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str

class ReviewTemplateTypeDef(BaseModel):
    Description: Optional[str] = None
    Lenses: Optional[List[str]] = None
    Notes: Optional[str] = None
    QuestionCounts: Optional[Dict[QuestionType, int]] = None
    Owner: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    TemplateArn: Optional[str] = None
    TemplateName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    UpdateStatus: Optional[ReviewTemplateUpdateStatusType] = None
    ShareInvitationId: Optional[str] = None

class GetWorkloadInputRequestTypeDef(BaseModel):
    WorkloadId: str

class ImportLensInputRequestTypeDef(BaseModel):
    JSONString: str
    ClientRequestToken: str
    LensAlias: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class SelectedPillarTypeDef(BaseModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[List[str]] = None

class WorkloadProfileTypeDef(BaseModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None

class PillarReviewSummaryTypeDef(BaseModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    Notes: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None

class LensShareSummaryTypeDef(BaseModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None

class LensSummaryTypeDef(BaseModel):
    LensArn: Optional[str] = None
    LensAlias: Optional[str] = None
    LensName: Optional[str] = None
    LensType: Optional[LensTypeType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    LensVersion: Optional[str] = None
    Owner: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None

class LensUpgradeSummaryTypeDef(BaseModel):
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    CurrentLensVersion: Optional[str] = None
    LatestLensVersion: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceName: Optional[str] = None

class ListAnswersInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None

class ListCheckDetailsInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCheckSummariesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLensReviewImprovementsInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None

class ListLensReviewsInputRequestTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLensSharesInputRequestTypeDef(BaseModel):
    LensAlias: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None

class ListLensesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LensType: Optional[LensTypeType] = None
    LensStatus: Optional[LensStatusTypeType] = None
    LensName: Optional[str] = None

class ListMilestonesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListNotificationsInputRequestTypeDef(BaseModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceArn: Optional[str] = None

class ListProfileNotificationsInputRequestTypeDef(BaseModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProfileNotificationSummaryTypeDef(BaseModel):
    CurrentProfileVersion: Optional[str] = None
    LatestProfileVersion: Optional[str] = None
    Type: Optional[ProfileNotificationTypeType] = None
    ProfileArn: Optional[str] = None
    ProfileName: Optional[str] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None

class ListProfileSharesInputRequestTypeDef(BaseModel):
    ProfileArn: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None

class ProfileShareSummaryTypeDef(BaseModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None

class ListProfilesInputRequestTypeDef(BaseModel):
    ProfileNamePrefix: Optional[str] = None
    ProfileOwnerType: Optional[ProfileOwnerTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProfileSummaryTypeDef(BaseModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None
    ProfileName: Optional[str] = None
    ProfileDescription: Optional[str] = None
    Owner: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ListReviewTemplateAnswersInputRequestTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    PillarId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReviewTemplatesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ReviewTemplateSummaryTypeDef(BaseModel):
    Description: Optional[str] = None
    Lenses: Optional[List[str]] = None
    Owner: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    TemplateArn: Optional[str] = None
    TemplateName: Optional[str] = None
    UpdateStatus: Optional[ReviewTemplateUpdateStatusType] = None

class ListShareInvitationsInputRequestTypeDef(BaseModel):
    WorkloadNamePrefix: Optional[str] = None
    LensNamePrefix: Optional[str] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProfileNamePrefix: Optional[str] = None
    TemplateNamePrefix: Optional[str] = None

class ShareInvitationSummaryTypeDef(BaseModel):
    ShareInvitationId: Optional[str] = None
    SharedBy: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    WorkloadName: Optional[str] = None
    WorkloadId: Optional[str] = None
    LensName: Optional[str] = None
    LensArn: Optional[str] = None
    ProfileName: Optional[str] = None
    ProfileArn: Optional[str] = None
    TemplateName: Optional[str] = None
    TemplateArn: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    WorkloadArn: str

class ListTemplateSharesInputRequestTypeDef(BaseModel):
    TemplateArn: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None

class TemplateShareSummaryTypeDef(BaseModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None

class ListWorkloadSharesInputRequestTypeDef(BaseModel):
    WorkloadId: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None

class WorkloadShareSummaryTypeDef(BaseModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None

class ListWorkloadsInputRequestTypeDef(BaseModel):
    WorkloadNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QuestionDifferenceTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    DifferenceStatus: Optional[DifferenceStatusType] = None

class ProfileChoiceTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None
    ChoiceDescription: Optional[str] = None

class ProfileTemplateChoiceTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None
    ChoiceDescription: Optional[str] = None

class ReviewTemplatePillarReviewSummaryTypeDef(BaseModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    Notes: Optional[str] = None
    QuestionCounts: Optional[Dict[QuestionType, int]] = None

class ShareInvitationTypeDef(BaseModel):
    ShareInvitationId: Optional[str] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    WorkloadId: Optional[str] = None
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    ProfileArn: Optional[str] = None
    TemplateArn: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    WorkloadArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    WorkloadArn: str
    TagKeys: Sequence[str]

class UpdateIntegrationInputRequestTypeDef(BaseModel):
    WorkloadId: str
    ClientRequestToken: str
    IntegratingService: Literal["JIRA"]

class UpdateReviewTemplateInputRequestTypeDef(BaseModel):
    TemplateArn: str
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None
    LensesToAssociate: Optional[Sequence[str]] = None
    LensesToDisassociate: Optional[Sequence[str]] = None

class UpdateReviewTemplateLensReviewInputRequestTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None

class UpdateShareInvitationInputRequestTypeDef(BaseModel):
    ShareInvitationId: str
    ShareInvitationAction: ShareInvitationActionType

class UpdateWorkloadShareInputRequestTypeDef(BaseModel):
    ShareId: str
    WorkloadId: str
    PermissionType: PermissionTypeType

class WorkloadShareTypeDef(BaseModel):
    ShareId: Optional[str] = None
    SharedBy: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    Status: Optional[ShareStatusType] = None
    WorkloadName: Optional[str] = None
    WorkloadId: Optional[str] = None

class UpgradeLensReviewInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    MilestoneName: str
    ClientRequestToken: Optional[str] = None

class UpgradeProfileVersionInputRequestTypeDef(BaseModel):
    WorkloadId: str
    ProfileArn: str
    MilestoneName: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class UpgradeReviewTemplateLensReviewInputRequestTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    ClientRequestToken: Optional[str] = None

class WorkloadJiraConfigurationOutputTypeDef(BaseModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None

class UpdateGlobalSettingsInputRequestTypeDef(BaseModel):
    OrganizationSharingStatus: Optional[OrganizationSharingStatusType] = None
    DiscoveryIntegrationStatus: Optional[DiscoveryIntegrationStatusType] = None
    JiraConfiguration: Optional[AccountJiraConfigurationInputTypeDef] = None

class AdditionalResourcesTypeDef(BaseModel):
    Type: Optional[AdditionalResourceTypeType] = None
    Content: Optional[List[ChoiceContentTypeDef]] = None

class QuestionMetricTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    Risk: Optional[RiskType] = None
    BestPractices: Optional[List[BestPracticeTypeDef]] = None

class ImprovementSummaryTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Risk: Optional[RiskType] = None
    ImprovementPlanUrl: Optional[str] = None
    ImprovementPlans: Optional[List[ChoiceImprovementPlanTypeDef]] = None
    JiraConfiguration: Optional[JiraConfigurationTypeDef] = None

class UpdateAnswerInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdateTypeDef]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None

class UpdateReviewTemplateAnswerInputRequestTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdateTypeDef]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None

class CreateLensShareOutputTypeDef(BaseModel):
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLensVersionOutputTypeDef(BaseModel):
    LensArn: str
    LensVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMilestoneOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileOutputTypeDef(BaseModel):
    ProfileArn: str
    ProfileVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileShareOutputTypeDef(BaseModel):
    ShareId: str
    ProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReviewTemplateOutputTypeDef(BaseModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateShareOutputTypeDef(BaseModel):
    TemplateArn: str
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkloadOutputTypeDef(BaseModel):
    WorkloadId: str
    WorkloadArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkloadShareOutputTypeDef(BaseModel):
    WorkloadId: str
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLensOutputTypeDef(BaseModel):
    LensJSON: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlobalSettingsOutputTypeDef(BaseModel):
    OrganizationSharingStatus: OrganizationSharingStatusType
    DiscoveryIntegrationStatus: DiscoveryIntegrationStatusType
    JiraConfiguration: AccountJiraConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportLensOutputTypeDef(BaseModel):
    LensArn: str
    Status: ImportLensStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListCheckDetailsOutputTypeDef(BaseModel):
    CheckDetails: List[CheckDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCheckSummariesOutputTypeDef(BaseModel):
    CheckSummaries: List[CheckSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileInputRequestTypeDef(BaseModel):
    ProfileName: str
    ProfileDescription: str
    ProfileQuestions: Sequence[ProfileQuestionUpdateTypeDef]
    ClientRequestToken: str
    Tags: Optional[Mapping[str, str]] = None

class UpdateProfileInputRequestTypeDef(BaseModel):
    ProfileArn: str
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[Sequence[ProfileQuestionUpdateTypeDef]] = None

class CreateWorkloadInputRequestTypeDef(BaseModel):
    WorkloadName: str
    Description: str
    Environment: WorkloadEnvironmentType
    Lenses: Sequence[str]
    ClientRequestToken: str
    AccountIds: Optional[Sequence[str]] = None
    AwsRegions: Optional[Sequence[str]] = None
    NonAwsRegions: Optional[Sequence[str]] = None
    PillarPriorities: Optional[Sequence[str]] = None
    ArchitecturalDesign: Optional[str] = None
    ReviewOwner: Optional[str] = None
    IndustryType: Optional[str] = None
    Industry: Optional[str] = None
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigTypeDef] = None
    Applications: Optional[Sequence[str]] = None
    ProfileArns: Optional[Sequence[str]] = None
    ReviewTemplateArns: Optional[Sequence[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInputTypeDef] = None

class UpdateWorkloadInputRequestTypeDef(BaseModel):
    WorkloadId: str
    WorkloadName: Optional[str] = None
    Description: Optional[str] = None
    Environment: Optional[WorkloadEnvironmentType] = None
    AccountIds: Optional[Sequence[str]] = None
    AwsRegions: Optional[Sequence[str]] = None
    NonAwsRegions: Optional[Sequence[str]] = None
    PillarPriorities: Optional[Sequence[str]] = None
    ArchitecturalDesign: Optional[str] = None
    ReviewOwner: Optional[str] = None
    IsReviewOwnerUpdateAcknowledged: Optional[bool] = None
    IndustryType: Optional[str] = None
    Industry: Optional[str] = None
    Notes: Optional[str] = None
    ImprovementStatus: Optional[WorkloadImprovementStatusType] = None
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigTypeDef] = None
    Applications: Optional[Sequence[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInputTypeDef] = None

class GetLensOutputTypeDef(BaseModel):
    Lens: LensTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLensReviewReportOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewReport: LensReviewReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReviewTemplateOutputTypeDef(BaseModel):
    ReviewTemplate: ReviewTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReviewTemplateOutputTypeDef(BaseModel):
    ReviewTemplate: ReviewTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JiraSelectedQuestionConfigurationTypeDef(BaseModel):
    SelectedPillars: Optional[List[SelectedPillarTypeDef]] = None

class LensReviewSummaryTypeDef(BaseModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    UpdatedAt: Optional[datetime] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None

class WorkloadSummaryTypeDef(BaseModel):
    WorkloadId: Optional[str] = None
    WorkloadArn: Optional[str] = None
    WorkloadName: Optional[str] = None
    Owner: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    Lenses: Optional[List[str]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    ImprovementStatus: Optional[WorkloadImprovementStatusType] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None

class ListLensSharesOutputTypeDef(BaseModel):
    LensShareSummaries: List[LensShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLensesOutputTypeDef(BaseModel):
    LensSummaries: List[LensSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotificationSummaryTypeDef(BaseModel):
    Type: Optional[NotificationTypeType] = None
    LensUpgradeSummary: Optional[LensUpgradeSummaryTypeDef] = None

class ListProfileNotificationsOutputTypeDef(BaseModel):
    NotificationSummaries: List[ProfileNotificationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileSharesOutputTypeDef(BaseModel):
    ProfileShareSummaries: List[ProfileShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesOutputTypeDef(BaseModel):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewTemplatesOutputTypeDef(BaseModel):
    ReviewTemplates: List[ReviewTemplateSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListShareInvitationsOutputTypeDef(BaseModel):
    ShareInvitationSummaries: List[ShareInvitationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateSharesOutputTypeDef(BaseModel):
    TemplateArn: str
    TemplateShareSummaries: List[TemplateShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkloadSharesOutputTypeDef(BaseModel):
    WorkloadId: str
    WorkloadShareSummaries: List[WorkloadShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PillarDifferenceTypeDef(BaseModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    DifferenceStatus: Optional[DifferenceStatusType] = None
    QuestionDifferences: Optional[List[QuestionDifferenceTypeDef]] = None

class ProfileQuestionTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    QuestionChoices: Optional[List[ProfileChoiceTypeDef]] = None
    SelectedChoiceIds: Optional[List[str]] = None
    MinSelectedChoices: Optional[int] = None
    MaxSelectedChoices: Optional[int] = None

class ProfileTemplateQuestionTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    QuestionChoices: Optional[List[ProfileTemplateChoiceTypeDef]] = None
    MinSelectedChoices: Optional[int] = None
    MaxSelectedChoices: Optional[int] = None

class ReviewTemplateLensReviewTypeDef(BaseModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    PillarReviewSummaries: Optional[List[ReviewTemplatePillarReviewSummaryTypeDef]] = None
    UpdatedAt: Optional[datetime] = None
    Notes: Optional[str] = None
    QuestionCounts: Optional[Dict[QuestionType, int]] = None
    NextToken: Optional[str] = None

class UpdateShareInvitationOutputTypeDef(BaseModel):
    ShareInvitation: ShareInvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkloadShareOutputTypeDef(BaseModel):
    WorkloadId: str
    WorkloadShare: WorkloadShareTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkloadTypeDef(BaseModel):
    WorkloadId: Optional[str] = None
    WorkloadArn: Optional[str] = None
    WorkloadName: Optional[str] = None
    Description: Optional[str] = None
    Environment: Optional[WorkloadEnvironmentType] = None
    UpdatedAt: Optional[datetime] = None
    AccountIds: Optional[List[str]] = None
    AwsRegions: Optional[List[str]] = None
    NonAwsRegions: Optional[List[str]] = None
    ArchitecturalDesign: Optional[str] = None
    ReviewOwner: Optional[str] = None
    ReviewRestrictionDate: Optional[datetime] = None
    IsReviewOwnerUpdateAcknowledged: Optional[bool] = None
    IndustryType: Optional[str] = None
    Industry: Optional[str] = None
    Notes: Optional[str] = None
    ImprovementStatus: Optional[WorkloadImprovementStatusType] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    PillarPriorities: Optional[List[str]] = None
    Lenses: Optional[List[str]] = None
    Owner: Optional[str] = None
    ShareInvitationId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigTypeDef] = None
    Applications: Optional[List[str]] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationOutputTypeDef] = None

class ChoiceTypeDef(BaseModel):
    ChoiceId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    HelpfulResource: Optional[ChoiceContentTypeDef] = None
    ImprovementPlan: Optional[ChoiceContentTypeDef] = None
    AdditionalResources: Optional[List[AdditionalResourcesTypeDef]] = None

class PillarMetricTypeDef(BaseModel):
    PillarId: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    Questions: Optional[List[QuestionMetricTypeDef]] = None

class ListLensReviewImprovementsOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    ImprovementSummaries: List[ImprovementSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LensReviewTypeDef(BaseModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    PillarReviewSummaries: Optional[List[PillarReviewSummaryTypeDef]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationTypeDef] = None
    UpdatedAt: Optional[datetime] = None
    Notes: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    NextToken: Optional[str] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None

class UpdateLensReviewInputRequestTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationTypeDef] = None

class ListLensReviewsOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List[LensReviewSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkloadsOutputTypeDef(BaseModel):
    WorkloadSummaries: List[WorkloadSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MilestoneSummaryTypeDef(BaseModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    WorkloadSummary: Optional[WorkloadSummaryTypeDef] = None

class ListNotificationsOutputTypeDef(BaseModel):
    NotificationSummaries: List[NotificationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class VersionDifferencesTypeDef(BaseModel):
    PillarDifferences: Optional[List[PillarDifferenceTypeDef]] = None

class ProfileTypeDef(BaseModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None
    ProfileName: Optional[str] = None
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[List[ProfileQuestionTypeDef]] = None
    Owner: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ShareInvitationId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ProfileTemplateTypeDef(BaseModel):
    TemplateName: Optional[str] = None
    TemplateQuestions: Optional[List[ProfileTemplateQuestionTypeDef]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class GetReviewTemplateLensReviewOutputTypeDef(BaseModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReviewTemplateLensReviewOutputTypeDef(BaseModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkloadOutputTypeDef(BaseModel):
    Workload: WorkloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MilestoneTypeDef(BaseModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    Workload: Optional[WorkloadTypeDef] = None

class UpdateWorkloadOutputTypeDef(BaseModel):
    Workload: WorkloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnswerSummaryTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Choices: Optional[List[ChoiceTypeDef]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswerSummaries: Optional[List[ChoiceAnswerSummaryTypeDef]] = None
    IsApplicable: Optional[bool] = None
    Risk: Optional[RiskType] = None
    Reason: Optional[AnswerReasonType] = None
    QuestionType: Optional[QuestionTypeType] = None
    JiraConfiguration: Optional[JiraConfigurationTypeDef] = None

class AnswerTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None
    HelpfulResourceUrl: Optional[str] = None
    HelpfulResourceDisplayText: Optional[str] = None
    Choices: Optional[List[ChoiceTypeDef]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswers: Optional[List[ChoiceAnswerTypeDef]] = None
    IsApplicable: Optional[bool] = None
    Risk: Optional[RiskType] = None
    Notes: Optional[str] = None
    Reason: Optional[AnswerReasonType] = None
    JiraConfiguration: Optional[JiraConfigurationTypeDef] = None

class ReviewTemplateAnswerSummaryTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Choices: Optional[List[ChoiceTypeDef]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswerSummaries: Optional[List[ChoiceAnswerSummaryTypeDef]] = None
    IsApplicable: Optional[bool] = None
    AnswerStatus: Optional[ReviewTemplateAnswerStatusType] = None
    Reason: Optional[AnswerReasonType] = None
    QuestionType: Optional[QuestionTypeType] = None

class ReviewTemplateAnswerTypeDef(BaseModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None
    HelpfulResourceUrl: Optional[str] = None
    HelpfulResourceDisplayText: Optional[str] = None
    Choices: Optional[List[ChoiceTypeDef]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswers: Optional[List[ChoiceAnswerTypeDef]] = None
    IsApplicable: Optional[bool] = None
    AnswerStatus: Optional[ReviewTemplateAnswerStatusType] = None
    Notes: Optional[str] = None
    Reason: Optional[AnswerReasonType] = None

class LensMetricTypeDef(BaseModel):
    LensArn: Optional[str] = None
    Pillars: Optional[List[PillarMetricTypeDef]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None

class GetLensReviewOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReview: LensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLensReviewOutputTypeDef(BaseModel):
    WorkloadId: str
    LensReview: LensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMilestonesOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneSummaries: List[MilestoneSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLensVersionDifferenceOutputTypeDef(BaseModel):
    LensAlias: str
    LensArn: str
    BaseLensVersion: str
    TargetLensVersion: str
    LatestLensVersion: str
    VersionDifferences: VersionDifferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileOutputTypeDef(BaseModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileOutputTypeDef(BaseModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileTemplateOutputTypeDef(BaseModel):
    ProfileTemplate: ProfileTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMilestoneOutputTypeDef(BaseModel):
    WorkloadId: str
    Milestone: MilestoneTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnswersOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    AnswerSummaries: List[AnswerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnswerOutputTypeDef(BaseModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    Answer: AnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnswerOutputTypeDef(BaseModel):
    WorkloadId: str
    LensAlias: str
    LensArn: str
    Answer: AnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewTemplateAnswersOutputTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    AnswerSummaries: List[ReviewTemplateAnswerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReviewTemplateAnswerOutputTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReviewTemplateAnswerOutputTypeDef(BaseModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConsolidatedReportMetricTypeDef(BaseModel):
    MetricType: Optional[Literal["WORKLOAD"]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    WorkloadArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    Lenses: Optional[List[LensMetricTypeDef]] = None
    LensesAppliedCount: Optional[int] = None

class GetConsolidatedReportOutputTypeDef(BaseModel):
    Metrics: List[ConsolidatedReportMetricTypeDef]
    NextToken: str
    Base64String: str
    ResponseMetadata: ResponseMetadataTypeDef

