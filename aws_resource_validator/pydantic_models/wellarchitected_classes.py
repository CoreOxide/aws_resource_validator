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
from aws_resource_validator.pydantic_models.wellarchitected_constants import *

class AccountJiraConfigurationInput(BaseValidatorModel):
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    IntegrationStatus: Optional[Literal["NOT_CONFIGURED"]] = None


class AccountJiraConfigurationOutput(BaseValidatorModel):
    IntegrationStatus: Optional[IntegrationStatusType] = None
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    Subdomain: Optional[str] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None


class ChoiceContent(BaseValidatorModel):
    DisplayText: Optional[str] = None
    Url: Optional[str] = None


class ChoiceAnswerSummary(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    Status: Optional[ChoiceStatusType] = None
    Reason: Optional[ChoiceReasonType] = None


class JiraConfiguration(BaseValidatorModel):
    JiraIssueUrl: Optional[str] = None
    LastSyncedTime: Optional[datetime] = None


class ChoiceAnswer(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    Status: Optional[ChoiceStatusType] = None
    Reason: Optional[ChoiceReasonType] = None
    Notes: Optional[str] = None


class AssociateLensesInput(BaseValidatorModel):
    WorkloadId: str
    LensAliases: Sequence[str]


class AssociateProfilesInput(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: Sequence[str]


class BestPractice(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None


class CheckDetail(BaseValidatorModel):
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


class CheckSummary(BaseValidatorModel):
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


class ChoiceImprovementPlan(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    DisplayText: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None


class ChoiceUpdate(BaseValidatorModel):
    Status: ChoiceStatusType
    Reason: Optional[ChoiceReasonType] = None
    Notes: Optional[str] = None


class CreateLensShareInput(BaseValidatorModel):
    LensAlias: str
    SharedWith: str
    ClientRequestToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateLensVersionInput(BaseValidatorModel):
    LensAlias: str
    LensVersion: str
    ClientRequestToken: str
    IsMajorVersion: Optional[bool] = None


class CreateMilestoneInput(BaseValidatorModel):
    WorkloadId: str
    MilestoneName: str
    ClientRequestToken: str


class ProfileQuestionUpdate(BaseValidatorModel):
    QuestionId: Optional[str] = None
    SelectedChoiceIds: Optional[Sequence[str]] = None


class CreateProfileShareInput(BaseValidatorModel):
    ProfileArn: str
    SharedWith: str
    ClientRequestToken: str


class CreateReviewTemplateInput(BaseValidatorModel):
    TemplateName: str
    Description: str
    Lenses: Sequence[str]
    ClientRequestToken: str
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateTemplateShareInput(BaseValidatorModel):
    TemplateArn: str
    SharedWith: str
    ClientRequestToken: str


class WorkloadJiraConfigurationInput(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None


class CreateWorkloadShareInput(BaseValidatorModel):
    WorkloadId: str
    SharedWith: str
    PermissionType: PermissionTypeType
    ClientRequestToken: str


class DeleteLensInput(BaseValidatorModel):
    LensAlias: str
    ClientRequestToken: str
    LensStatus: LensStatusTypeType


class DeleteLensShareInput(BaseValidatorModel):
    ShareId: str
    LensAlias: str
    ClientRequestToken: str


class DeleteProfileInput(BaseValidatorModel):
    ProfileArn: str
    ClientRequestToken: str


class DeleteProfileShareInput(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ClientRequestToken: str


class DeleteReviewTemplateInput(BaseValidatorModel):
    TemplateArn: str
    ClientRequestToken: str


class DeleteTemplateShareInput(BaseValidatorModel):
    ShareId: str
    TemplateArn: str
    ClientRequestToken: str


class DeleteWorkloadInput(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str


class DeleteWorkloadShareInput(BaseValidatorModel):
    ShareId: str
    WorkloadId: str
    ClientRequestToken: str


class DisassociateLensesInput(BaseValidatorModel):
    WorkloadId: str
    LensAliases: Sequence[str]


class DisassociateProfilesInput(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: Sequence[str]


class ExportLensInput(BaseValidatorModel):
    LensAlias: str
    LensVersion: Optional[str] = None


class GetAnswerInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    MilestoneNumber: Optional[int] = None


class GetConsolidatedReportInput(BaseValidatorModel):
    Format: ReportFormatType
    IncludeSharedResources: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetLensInput(BaseValidatorModel):
    LensAlias: str
    LensVersion: Optional[str] = None


class Lens(BaseValidatorModel):
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    ShareInvitationId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class GetLensReviewInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None


class GetLensReviewReportInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None


class LensReviewReport(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    Base64String: Optional[str] = None


class GetLensVersionDifferenceInput(BaseValidatorModel):
    LensAlias: str
    BaseLensVersion: Optional[str] = None
    TargetLensVersion: Optional[str] = None


class GetMilestoneInput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int


class GetProfileInput(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: Optional[str] = None


class GetReviewTemplateAnswerInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str


class GetReviewTemplateInput(BaseValidatorModel):
    TemplateArn: str


class GetReviewTemplateLensReviewInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str


class ReviewTemplate(BaseValidatorModel):
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


class GetWorkloadInput(BaseValidatorModel):
    WorkloadId: str


class ImportLensInput(BaseValidatorModel):
    JSONString: str
    ClientRequestToken: str
    LensAlias: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class SelectedPillarOutput(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[List[str]] = None


class SelectedPillar(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[Sequence[str]] = None


class WorkloadProfile(BaseValidatorModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None


class PillarReviewSummary(BaseValidatorModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    Notes: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class LensShareSummary(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class LensSummary(BaseValidatorModel):
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


class LensUpgradeSummary(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    CurrentLensVersion: Optional[str] = None
    LatestLensVersion: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceName: Optional[str] = None


class ListAnswersInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None


class ListCheckDetailsInput(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCheckSummariesInput(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLensReviewImprovementsInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None


class ListLensReviewsInput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLensSharesInput(BaseValidatorModel):
    LensAlias: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class ListLensesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LensType: Optional[LensTypeType] = None
    LensStatus: Optional[LensStatusTypeType] = None
    LensName: Optional[str] = None


class ListMilestonesInput(BaseValidatorModel):
    WorkloadId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListNotificationsInput(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceArn: Optional[str] = None


class ListProfileNotificationsInput(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileSharesInput(BaseValidatorModel):
    ProfileArn: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class ProfileShareSummary(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class ListProfilesInput(BaseValidatorModel):
    ProfileNamePrefix: Optional[str] = None
    ProfileOwnerType: Optional[ProfileOwnerTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProfileSummary(BaseValidatorModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None
    ProfileName: Optional[str] = None
    ProfileDescription: Optional[str] = None
    Owner: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ListReviewTemplateAnswersInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    PillarId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReviewTemplatesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ReviewTemplateSummary(BaseValidatorModel):
    Description: Optional[str] = None
    Lenses: Optional[List[str]] = None
    Owner: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    TemplateArn: Optional[str] = None
    TemplateName: Optional[str] = None
    UpdateStatus: Optional[ReviewTemplateUpdateStatusType] = None


class ListShareInvitationsInput(BaseValidatorModel):
    WorkloadNamePrefix: Optional[str] = None
    LensNamePrefix: Optional[str] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProfileNamePrefix: Optional[str] = None
    TemplateNamePrefix: Optional[str] = None


class ShareInvitationSummary(BaseValidatorModel):
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


class ListTagsForResourceInput(BaseValidatorModel):
    WorkloadArn: str


class ListTemplateSharesInput(BaseValidatorModel):
    TemplateArn: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class TemplateShareSummary(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class ListWorkloadSharesInput(BaseValidatorModel):
    WorkloadId: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class WorkloadShareSummary(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class ListWorkloadsInput(BaseValidatorModel):
    WorkloadNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QuestionDifference(BaseValidatorModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    DifferenceStatus: Optional[DifferenceStatusType] = None


class ProfileChoice(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None
    ChoiceDescription: Optional[str] = None


class ProfileTemplateChoice(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None
    ChoiceDescription: Optional[str] = None


class ReviewTemplatePillarReviewSummary(BaseValidatorModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    Notes: Optional[str] = None
    QuestionCounts: Optional[Dict[QuestionType, int]] = None


class ShareInvitation(BaseValidatorModel):
    ShareInvitationId: Optional[str] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    WorkloadId: Optional[str] = None
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    ProfileArn: Optional[str] = None
    TemplateArn: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    WorkloadArn: str
    Tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    WorkloadArn: str
    TagKeys: Sequence[str]


class UpdateIntegrationInput(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str
    IntegratingService: Literal["JIRA"]


class UpdateReviewTemplateInput(BaseValidatorModel):
    TemplateArn: str
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None
    LensesToAssociate: Optional[Sequence[str]] = None
    LensesToDisassociate: Optional[Sequence[str]] = None


class UpdateReviewTemplateLensReviewInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None


class UpdateShareInvitationInput(BaseValidatorModel):
    ShareInvitationId: str
    ShareInvitationAction: ShareInvitationActionType


class UpdateWorkloadShareInput(BaseValidatorModel):
    ShareId: str
    WorkloadId: str
    PermissionType: PermissionTypeType


class WorkloadShare(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedBy: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    Status: Optional[ShareStatusType] = None
    WorkloadName: Optional[str] = None
    WorkloadId: Optional[str] = None


class UpgradeLensReviewInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneName: str
    ClientRequestToken: Optional[str] = None


class UpgradeProfileVersionInput(BaseValidatorModel):
    WorkloadId: str
    ProfileArn: str
    MilestoneName: Optional[str] = None
    ClientRequestToken: Optional[str] = None


class UpgradeReviewTemplateLensReviewInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    ClientRequestToken: Optional[str] = None


class WorkloadDiscoveryConfigOutput(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[List[DefinitionTypeType]] = None


class WorkloadDiscoveryConfig(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[Sequence[DefinitionTypeType]] = None


class WorkloadJiraConfigurationOutput(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None


class UpdateGlobalSettingsInput(BaseValidatorModel):
    OrganizationSharingStatus: Optional[OrganizationSharingStatusType] = None
    DiscoveryIntegrationStatus: Optional[DiscoveryIntegrationStatusType] = None
    JiraConfiguration: Optional[AccountJiraConfigurationInput] = None


class QuestionMetric(BaseValidatorModel):
    QuestionId: Optional[str] = None
    Risk: Optional[RiskType] = None
    BestPractices: Optional[List[BestPractice]] = None


class ImprovementSummary(BaseValidatorModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Risk: Optional[RiskType] = None
    ImprovementPlanUrl: Optional[str] = None
    ImprovementPlans: Optional[List[ChoiceImprovementPlan]] = None
    JiraConfiguration: Optional[JiraConfiguration] = None


class UpdateAnswerInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdate]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None


class UpdateReviewTemplateAnswerInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdate]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None


class CreateLensShareOutput(BaseValidatorModel):
    ShareId: str
    ResponseMetadata: ResponseMetadata


class CreateLensVersionOutput(BaseValidatorModel):
    LensArn: str
    LensVersion: str
    ResponseMetadata: ResponseMetadata


class CreateMilestoneOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    ResponseMetadata: ResponseMetadata


class CreateProfileOutput(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: str
    ResponseMetadata: ResponseMetadata


class CreateProfileShareOutput(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ResponseMetadata: ResponseMetadata


class CreateReviewTemplateOutput(BaseValidatorModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadata


class CreateTemplateShareOutput(BaseValidatorModel):
    TemplateArn: str
    ShareId: str
    ResponseMetadata: ResponseMetadata


class CreateWorkloadOutput(BaseValidatorModel):
    WorkloadId: str
    WorkloadArn: str
    ResponseMetadata: ResponseMetadata


class CreateWorkloadShareOutput(BaseValidatorModel):
    WorkloadId: str
    ShareId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExportLensOutput(BaseValidatorModel):
    LensJSON: str
    ResponseMetadata: ResponseMetadata


class GetGlobalSettingsOutput(BaseValidatorModel):
    OrganizationSharingStatus: OrganizationSharingStatusType
    DiscoveryIntegrationStatus: DiscoveryIntegrationStatusType
    JiraConfiguration: AccountJiraConfigurationOutput
    ResponseMetadata: ResponseMetadata


class ImportLensOutput(BaseValidatorModel):
    LensArn: str
    Status: ImportLensStatusType
    ResponseMetadata: ResponseMetadata


class ListCheckDetailsOutput(BaseValidatorModel):
    CheckDetails: List[CheckDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCheckSummariesOutput(BaseValidatorModel):
    CheckSummaries: List[CheckSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateProfileInput(BaseValidatorModel):
    ProfileName: str
    ProfileDescription: str
    ProfileQuestions: Sequence[ProfileQuestionUpdate]
    ClientRequestToken: str
    Tags: Optional[Mapping[str, str]] = None


class UpdateProfileInput(BaseValidatorModel):
    ProfileArn: str
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[Sequence[ProfileQuestionUpdate]] = None


class GetLensOutput(BaseValidatorModel):
    Lens: Lens
    ResponseMetadata: ResponseMetadata


class GetLensReviewReportOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewReport: LensReviewReport
    ResponseMetadata: ResponseMetadata


class GetReviewTemplateOutput(BaseValidatorModel):
    ReviewTemplate: ReviewTemplate
    ResponseMetadata: ResponseMetadata


class UpdateReviewTemplateOutput(BaseValidatorModel):
    ReviewTemplate: ReviewTemplate
    ResponseMetadata: ResponseMetadata


class JiraSelectedQuestionConfigurationOutput(BaseValidatorModel):
    SelectedPillars: Optional[List[SelectedPillarOutput]] = None


class JiraSelectedQuestionConfiguration(BaseValidatorModel):
    SelectedPillars: Optional[Sequence[SelectedPillar]] = None


class LensReviewSummary(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    UpdatedAt: Optional[datetime] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    Profiles: Optional[List[WorkloadProfile]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class WorkloadSummary(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    WorkloadArn: Optional[str] = None
    WorkloadName: Optional[str] = None
    Owner: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    Lenses: Optional[List[str]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    ImprovementStatus: Optional[WorkloadImprovementStatusType] = None
    Profiles: Optional[List[WorkloadProfile]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class ListLensSharesOutput(BaseValidatorModel):
    LensShareSummaries: List[LensShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLensesOutput(BaseValidatorModel):
    LensSummaries: List[LensSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ProfileNotificationSummary(BaseValidatorModel):
    pass


class ListProfileNotificationsOutput(BaseValidatorModel):
    NotificationSummaries: List[ProfileNotificationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfileSharesOutput(BaseValidatorModel):
    ProfileShareSummaries: List[ProfileShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfilesOutput(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListReviewTemplatesOutput(BaseValidatorModel):
    ReviewTemplates: List[ReviewTemplateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListShareInvitationsOutput(BaseValidatorModel):
    ShareInvitationSummaries: List[ShareInvitationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTemplateSharesOutput(BaseValidatorModel):
    TemplateArn: str
    TemplateShareSummaries: List[TemplateShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWorkloadSharesOutput(BaseValidatorModel):
    WorkloadId: str
    WorkloadShareSummaries: List[WorkloadShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PillarDifference(BaseValidatorModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    DifferenceStatus: Optional[DifferenceStatusType] = None
    QuestionDifferences: Optional[List[QuestionDifference]] = None


class ProfileQuestion(BaseValidatorModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    QuestionChoices: Optional[List[ProfileChoice]] = None
    SelectedChoiceIds: Optional[List[str]] = None
    MinSelectedChoices: Optional[int] = None
    MaxSelectedChoices: Optional[int] = None


class ProfileTemplateQuestion(BaseValidatorModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    QuestionChoices: Optional[List[ProfileTemplateChoice]] = None
    MinSelectedChoices: Optional[int] = None
    MaxSelectedChoices: Optional[int] = None


class ReviewTemplateLensReview(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    PillarReviewSummaries: Optional[List[ReviewTemplatePillarReviewSummary]] = None
    UpdatedAt: Optional[datetime] = None
    Notes: Optional[str] = None
    QuestionCounts: Optional[Dict[QuestionType, int]] = None
    NextToken: Optional[str] = None


class UpdateShareInvitationOutput(BaseValidatorModel):
    ShareInvitation: ShareInvitation
    ResponseMetadata: ResponseMetadata


class UpdateWorkloadShareOutput(BaseValidatorModel):
    WorkloadId: str
    WorkloadShare: WorkloadShare
    ResponseMetadata: ResponseMetadata


class Workload(BaseValidatorModel):
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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigOutput] = None
    Applications: Optional[List[str]] = None
    Profiles: Optional[List[WorkloadProfile]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationOutput] = None


class AdditionalResources(BaseValidatorModel):
    pass


class Choice(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    HelpfulResource: Optional[ChoiceContent] = None
    ImprovementPlan: Optional[ChoiceContent] = None
    AdditionalResources: Optional[List[AdditionalResources]] = None


class PillarMetric(BaseValidatorModel):
    PillarId: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    Questions: Optional[List[QuestionMetric]] = None


class ListLensReviewImprovementsOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    ImprovementSummaries: List[ImprovementSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LensReview(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    PillarReviewSummaries: Optional[List[PillarReviewSummary]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationOutput] = None
    UpdatedAt: Optional[datetime] = None
    Notes: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    NextToken: Optional[str] = None
    Profiles: Optional[List[WorkloadProfile]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class ListLensReviewsOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List[LensReviewSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWorkloadsOutput(BaseValidatorModel):
    WorkloadSummaries: List[WorkloadSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MilestoneSummary(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    WorkloadSummary: Optional[WorkloadSummary] = None


class NotificationSummary(BaseValidatorModel):
    pass


class ListNotificationsOutput(BaseValidatorModel):
    NotificationSummaries: List[NotificationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class VersionDifferences(BaseValidatorModel):
    PillarDifferences: Optional[List[PillarDifference]] = None


class Profile(BaseValidatorModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None
    ProfileName: Optional[str] = None
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[List[ProfileQuestion]] = None
    Owner: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ShareInvitationId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ProfileTemplate(BaseValidatorModel):
    TemplateName: Optional[str] = None
    TemplateQuestions: Optional[List[ProfileTemplateQuestion]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class GetReviewTemplateLensReviewOutput(BaseValidatorModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReview
    ResponseMetadata: ResponseMetadata


class UpdateReviewTemplateLensReviewOutput(BaseValidatorModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReview
    ResponseMetadata: ResponseMetadata


class WorkloadDiscoveryConfigUnion(BaseValidatorModel):
    pass


class CreateWorkloadInput(BaseValidatorModel):
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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigUnion] = None
    Applications: Optional[Sequence[str]] = None
    ProfileArns: Optional[Sequence[str]] = None
    ReviewTemplateArns: Optional[Sequence[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInput] = None


class UpdateWorkloadInput(BaseValidatorModel):
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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigUnion] = None
    Applications: Optional[Sequence[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInput] = None


class GetWorkloadOutput(BaseValidatorModel):
    Workload: Workload
    ResponseMetadata: ResponseMetadata


class Milestone(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    Workload: Optional[Workload] = None


class UpdateWorkloadOutput(BaseValidatorModel):
    Workload: Workload
    ResponseMetadata: ResponseMetadata


class Answer(BaseValidatorModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None
    HelpfulResourceUrl: Optional[str] = None
    HelpfulResourceDisplayText: Optional[str] = None
    Choices: Optional[List[Choice]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswers: Optional[List[ChoiceAnswer]] = None
    IsApplicable: Optional[bool] = None
    Risk: Optional[RiskType] = None
    Notes: Optional[str] = None
    Reason: Optional[AnswerReasonType] = None
    JiraConfiguration: Optional[JiraConfiguration] = None


class ReviewTemplateAnswer(BaseValidatorModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None
    HelpfulResourceUrl: Optional[str] = None
    HelpfulResourceDisplayText: Optional[str] = None
    Choices: Optional[List[Choice]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswers: Optional[List[ChoiceAnswer]] = None
    IsApplicable: Optional[bool] = None
    AnswerStatus: Optional[ReviewTemplateAnswerStatusType] = None
    Notes: Optional[str] = None
    Reason: Optional[AnswerReasonType] = None


class LensMetric(BaseValidatorModel):
    LensArn: Optional[str] = None
    Pillars: Optional[List[PillarMetric]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None


class GetLensReviewOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReview: LensReview
    ResponseMetadata: ResponseMetadata


class UpdateLensReviewOutput(BaseValidatorModel):
    WorkloadId: str
    LensReview: LensReview
    ResponseMetadata: ResponseMetadata


class JiraSelectedQuestionConfigurationUnion(BaseValidatorModel):
    pass


class UpdateLensReviewInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationUnion] = None


class ListMilestonesOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneSummaries: List[MilestoneSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetLensVersionDifferenceOutput(BaseValidatorModel):
    LensAlias: str
    LensArn: str
    BaseLensVersion: str
    TargetLensVersion: str
    LatestLensVersion: str
    VersionDifferences: VersionDifferences
    ResponseMetadata: ResponseMetadata


class GetProfileOutput(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


class UpdateProfileOutput(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


class GetProfileTemplateOutput(BaseValidatorModel):
    ProfileTemplate: ProfileTemplate
    ResponseMetadata: ResponseMetadata


class GetMilestoneOutput(BaseValidatorModel):
    WorkloadId: str
    Milestone: Milestone
    ResponseMetadata: ResponseMetadata


class AnswerSummary(BaseValidatorModel):
    pass


class ListAnswersOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    AnswerSummaries: List[AnswerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetAnswerOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    Answer: Answer
    ResponseMetadata: ResponseMetadata


class UpdateAnswerOutput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensArn: str
    Answer: Answer
    ResponseMetadata: ResponseMetadata


class ReviewTemplateAnswerSummary(BaseValidatorModel):
    pass


class ListReviewTemplateAnswersOutput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    AnswerSummaries: List[ReviewTemplateAnswerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetReviewTemplateAnswerOutput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswer
    ResponseMetadata: ResponseMetadata


class UpdateReviewTemplateAnswerOutput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswer
    ResponseMetadata: ResponseMetadata


class ConsolidatedReportMetric(BaseValidatorModel):
    MetricType: Optional[Literal["WORKLOAD"]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    WorkloadArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    Lenses: Optional[List[LensMetric]] = None
    LensesAppliedCount: Optional[int] = None


class GetConsolidatedReportOutput(BaseValidatorModel):
    Metrics: List[ConsolidatedReportMetric]
    Base64String: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


