from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.wellarchitected.wellarchitected_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountJiraConfigurationInput(BaseValidatorModel):
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    IntegrationStatus: Optional[Literal['NOT_CONFIGURED']] = None


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


# This class is the input for the 'associate_lenses' function.
class AssociateLensesInput(BaseValidatorModel):
    WorkloadId: str
    LensAliases: List[str]


# This class is the input for the 'associate_profiles' function.
class AssociateProfilesInput(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: List[str]


class BestPractice(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None


class CheckDetail(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Provider: Optional[Literal['TRUSTED_ADVISOR']] = None
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
    Provider: Optional[Literal['TRUSTED_ADVISOR']] = None
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


# This class is the input for the 'create_lens_share' function.
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


# This class is the input for the 'create_lens_version' function.
class CreateLensVersionInput(BaseValidatorModel):
    LensAlias: str
    LensVersion: str
    ClientRequestToken: str
    IsMajorVersion: Optional[bool] = None


# This class is the input for the 'create_milestone' function.
class CreateMilestoneInput(BaseValidatorModel):
    WorkloadId: str
    MilestoneName: str
    ClientRequestToken: str


class ProfileQuestionUpdate(BaseValidatorModel):
    QuestionId: Optional[str] = None
    SelectedChoiceIds: Optional[List[str]] = None


# This class is the input for the 'create_profile_share' function.
class CreateProfileShareInput(BaseValidatorModel):
    ProfileArn: str
    SharedWith: str
    ClientRequestToken: str


# This class is the input for the 'create_review_template' function.
class CreateReviewTemplateInput(BaseValidatorModel):
    TemplateName: str
    Description: str
    Lenses: List[str]
    ClientRequestToken: str
    Notes: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_template_share' function.
class CreateTemplateShareInput(BaseValidatorModel):
    TemplateArn: str
    SharedWith: str
    ClientRequestToken: str


class WorkloadJiraConfigurationInput(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None


# This class is the input for the 'create_workload_share' function.
class CreateWorkloadShareInput(BaseValidatorModel):
    WorkloadId: str
    SharedWith: str
    PermissionType: PermissionTypeType
    ClientRequestToken: str


# This class is the input for the 'delete_lens' function.
class DeleteLensInput(BaseValidatorModel):
    LensAlias: str
    ClientRequestToken: str
    LensStatus: LensStatusTypeType


# This class is the input for the 'delete_lens_share' function.
class DeleteLensShareInput(BaseValidatorModel):
    ShareId: str
    LensAlias: str
    ClientRequestToken: str


# This class is the input for the 'delete_profile' function.
class DeleteProfileInput(BaseValidatorModel):
    ProfileArn: str
    ClientRequestToken: str


# This class is the input for the 'delete_profile_share' function.
class DeleteProfileShareInput(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ClientRequestToken: str


# This class is the input for the 'delete_review_template' function.
class DeleteReviewTemplateInput(BaseValidatorModel):
    TemplateArn: str
    ClientRequestToken: str


# This class is the input for the 'delete_template_share' function.
class DeleteTemplateShareInput(BaseValidatorModel):
    ShareId: str
    TemplateArn: str
    ClientRequestToken: str


# This class is the input for the 'delete_workload' function.
class DeleteWorkloadInput(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str


# This class is the input for the 'delete_workload_share' function.
class DeleteWorkloadShareInput(BaseValidatorModel):
    ShareId: str
    WorkloadId: str
    ClientRequestToken: str


# This class is the input for the 'disassociate_lenses' function.
class DisassociateLensesInput(BaseValidatorModel):
    WorkloadId: str
    LensAliases: List[str]


# This class is the input for the 'disassociate_profiles' function.
class DisassociateProfilesInput(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: List[str]


# This class is the input for the 'export_lens' function.
class ExportLensInput(BaseValidatorModel):
    LensAlias: str
    LensVersion: Optional[str] = None


# This class is the input for the 'get_answer' function.
class GetAnswerInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    MilestoneNumber: Optional[int] = None


# This class is the input for the 'get_consolidated_report' function.
class GetConsolidatedReportInput(BaseValidatorModel):
    Format: ReportFormatType
    IncludeSharedResources: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'get_lens' function.
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


# This class is the input for the 'get_lens_review' function.
class GetLensReviewInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None


# This class is the input for the 'get_lens_review_report' function.
class GetLensReviewReportInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None


class LensReviewReport(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    Base64String: Optional[str] = None


# This class is the input for the 'get_lens_version_difference' function.
class GetLensVersionDifferenceInput(BaseValidatorModel):
    LensAlias: str
    BaseLensVersion: Optional[str] = None
    TargetLensVersion: Optional[str] = None


# This class is the input for the 'get_milestone' function.
class GetMilestoneInput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int


# This class is the input for the 'get_profile' function.
class GetProfileInput(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: Optional[str] = None


# This class is the input for the 'get_review_template_answer' function.
class GetReviewTemplateAnswerInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str


# This class is the input for the 'get_review_template' function.
class GetReviewTemplateInput(BaseValidatorModel):
    TemplateArn: str


# This class is the input for the 'get_review_template_lens_review' function.
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


# This class is the input for the 'get_workload' function.
class GetWorkloadInput(BaseValidatorModel):
    WorkloadId: str


# This class is the input for the 'import_lens' function.
class ImportLensInput(BaseValidatorModel):
    JSONString: str
    ClientRequestToken: str
    LensAlias: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class SelectedPillarOutput(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[List[str]] = None


class SelectedPillar(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[List[str]] = None


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


# This class is the input for the 'list_answers' function.
class ListAnswersInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None


# This class is the input for the 'list_check_details' function.
class ListCheckDetailsInput(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_check_summaries' function.
class ListCheckSummariesInput(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_lens_review_improvements' function.
class ListLensReviewImprovementsInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None


# This class is the input for the 'list_lens_reviews' function.
class ListLensReviewsInput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_lens_shares' function.
class ListLensSharesInput(BaseValidatorModel):
    LensAlias: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


# This class is the input for the 'list_lenses' function.
class ListLensesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LensType: Optional[LensTypeType] = None
    LensStatus: Optional[LensStatusTypeType] = None
    LensName: Optional[str] = None


# This class is the input for the 'list_milestones' function.
class ListMilestonesInput(BaseValidatorModel):
    WorkloadId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_notifications' function.
class ListNotificationsInput(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceArn: Optional[str] = None


# This class is the input for the 'list_profile_notifications' function.
class ListProfileNotificationsInput(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProfileNotificationSummary(BaseValidatorModel):
    CurrentProfileVersion: Optional[str] = None
    LatestProfileVersion: Optional[str] = None
    Type: Optional[ProfileNotificationTypeType] = None
    ProfileArn: Optional[str] = None
    ProfileName: Optional[str] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None


# This class is the input for the 'list_profile_shares' function.
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


# This class is the input for the 'list_profiles' function.
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


# This class is the input for the 'list_review_template_answers' function.
class ListReviewTemplateAnswersInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    PillarId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_review_templates' function.
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


# This class is the input for the 'list_share_invitations' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    WorkloadArn: str


# This class is the input for the 'list_template_shares' function.
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


# This class is the input for the 'list_workload_shares' function.
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


# This class is the input for the 'list_workloads' function.
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
    Tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    WorkloadArn: str
    TagKeys: List[str]


# This class is the input for the 'update_integration' function.
class UpdateIntegrationInput(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str
    IntegratingService: Literal['JIRA']


# This class is the input for the 'update_review_template' function.
class UpdateReviewTemplateInput(BaseValidatorModel):
    TemplateArn: str
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None
    LensesToAssociate: Optional[List[str]] = None
    LensesToDisassociate: Optional[List[str]] = None


# This class is the input for the 'update_review_template_lens_review' function.
class UpdateReviewTemplateLensReviewInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Dict[str, str]] = None


# This class is the input for the 'update_share_invitation' function.
class UpdateShareInvitationInput(BaseValidatorModel):
    ShareInvitationId: str
    ShareInvitationAction: ShareInvitationActionType


# This class is the input for the 'update_workload_share' function.
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


# This class is the input for the 'upgrade_lens_review' function.
class UpgradeLensReviewInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneName: str
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'upgrade_profile_version' function.
class UpgradeProfileVersionInput(BaseValidatorModel):
    WorkloadId: str
    ProfileArn: str
    MilestoneName: Optional[str] = None
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'upgrade_review_template_lens_review' function.
class UpgradeReviewTemplateLensReviewInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    ClientRequestToken: Optional[str] = None


class WorkloadDiscoveryConfigOutput(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[List[DefinitionTypeType]] = None


class WorkloadDiscoveryConfig(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[List[DefinitionTypeType]] = None


class WorkloadJiraConfigurationOutput(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None


# This class is the input for the 'update_global_settings' function.
class UpdateGlobalSettingsInput(BaseValidatorModel):
    OrganizationSharingStatus: Optional[OrganizationSharingStatusType] = None
    DiscoveryIntegrationStatus: Optional[DiscoveryIntegrationStatusType] = None
    JiraConfiguration: Optional[AccountJiraConfigurationInput] = None


class AdditionalResources(BaseValidatorModel):
    Type: Optional[AdditionalResourceTypeType] = None
    Content: Optional[List[ChoiceContent]] = None


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


# This class is the input for the 'update_answer' function.
class UpdateAnswerInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[List[str]] = None
    ChoiceUpdates: Optional[Dict[str, ChoiceUpdate]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None


# This class is the input for the 'update_review_template_answer' function.
class UpdateReviewTemplateAnswerInput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[List[str]] = None
    ChoiceUpdates: Optional[Dict[str, ChoiceUpdate]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None


# This class is the output for the 'create_lens_share' function.
class CreateLensShareOutput(BaseValidatorModel):
    ShareId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_lens_version' function.
class CreateLensVersionOutput(BaseValidatorModel):
    LensArn: str
    LensVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_milestone' function.
class CreateMilestoneOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_profile' function.
class CreateProfileOutput(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_profile_share' function.
class CreateProfileShareOutput(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_review_template' function.
class CreateReviewTemplateOutput(BaseValidatorModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_template_share' function.
class CreateTemplateShareOutput(BaseValidatorModel):
    TemplateArn: str
    ShareId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workload' function.
class CreateWorkloadOutput(BaseValidatorModel):
    WorkloadId: str
    WorkloadArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_workload_share' function.
class CreateWorkloadShareOutput(BaseValidatorModel):
    WorkloadId: str
    ShareId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upgrade_review_template_lens_review' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_lens' function.
class ExportLensOutput(BaseValidatorModel):
    LensJSON: str
    ResponseMetadata: ResponseMetadata


class GetGlobalSettingsOutput(BaseValidatorModel):
    OrganizationSharingStatus: OrganizationSharingStatusType
    DiscoveryIntegrationStatus: DiscoveryIntegrationStatusType
    JiraConfiguration: AccountJiraConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_lens' function.
class ImportLensOutput(BaseValidatorModel):
    LensArn: str
    Status: ImportLensStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_check_details' function.
class ListCheckDetailsOutput(BaseValidatorModel):
    CheckDetails: List[CheckDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_check_summaries' function.
class ListCheckSummariesOutput(BaseValidatorModel):
    CheckSummaries: List[CheckSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_profile' function.
class CreateProfileInput(BaseValidatorModel):
    ProfileName: str
    ProfileDescription: str
    ProfileQuestions: List[ProfileQuestionUpdate]
    ClientRequestToken: str
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_profile' function.
class UpdateProfileInput(BaseValidatorModel):
    ProfileArn: str
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[List[ProfileQuestionUpdate]] = None


# This class is the output for the 'get_lens' function.
class GetLensOutput(BaseValidatorModel):
    Lens: Lens
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_lens_review_report' function.
class GetLensReviewReportOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewReport: LensReviewReport
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_review_template' function.
class GetReviewTemplateOutput(BaseValidatorModel):
    ReviewTemplate: ReviewTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_review_template' function.
class UpdateReviewTemplateOutput(BaseValidatorModel):
    ReviewTemplate: ReviewTemplate
    ResponseMetadata: ResponseMetadata


class JiraSelectedQuestionConfigurationOutput(BaseValidatorModel):
    SelectedPillars: Optional[List[SelectedPillarOutput]] = None


class JiraSelectedQuestionConfiguration(BaseValidatorModel):
    SelectedPillars: Optional[List[SelectedPillar]] = None


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


# This class is the output for the 'list_lens_shares' function.
class ListLensSharesOutput(BaseValidatorModel):
    LensShareSummaries: List[LensShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_lenses' function.
class ListLensesOutput(BaseValidatorModel):
    LensSummaries: List[LensSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NotificationSummary(BaseValidatorModel):
    Type: Optional[NotificationTypeType] = None
    LensUpgradeSummary: Optional[LensUpgradeSummary] = None


# This class is the output for the 'list_profile_notifications' function.
class ListProfileNotificationsOutput(BaseValidatorModel):
    NotificationSummaries: List[ProfileNotificationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_profile_shares' function.
class ListProfileSharesOutput(BaseValidatorModel):
    ProfileShareSummaries: List[ProfileShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_profiles' function.
class ListProfilesOutput(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_review_templates' function.
class ListReviewTemplatesOutput(BaseValidatorModel):
    ReviewTemplates: List[ReviewTemplateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_share_invitations' function.
class ListShareInvitationsOutput(BaseValidatorModel):
    ShareInvitationSummaries: List[ShareInvitationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_template_shares' function.
class ListTemplateSharesOutput(BaseValidatorModel):
    TemplateArn: str
    TemplateShareSummaries: List[TemplateShareSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_workload_shares' function.
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


# This class is the output for the 'update_share_invitation' function.
class UpdateShareInvitationOutput(BaseValidatorModel):
    ShareInvitation: ShareInvitation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_workload_share' function.
class UpdateWorkloadShareOutput(BaseValidatorModel):
    WorkloadId: str
    WorkloadShare: WorkloadShare
    ResponseMetadata: ResponseMetadata

WorkloadDiscoveryConfigUnion = Union[WorkloadDiscoveryConfig, WorkloadDiscoveryConfigOutput]


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


# This class is the output for the 'list_lens_review_improvements' function.
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

JiraSelectedQuestionConfigurationUnion = Union[JiraSelectedQuestionConfiguration, JiraSelectedQuestionConfigurationOutput]


# This class is the output for the 'list_lens_reviews' function.
class ListLensReviewsOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List[LensReviewSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_workloads' function.
class ListWorkloadsOutput(BaseValidatorModel):
    WorkloadSummaries: List[WorkloadSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MilestoneSummary(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    WorkloadSummary: Optional[WorkloadSummary] = None


# This class is the output for the 'list_notifications' function.
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


# This class is the output for the 'get_review_template_lens_review' function.
class GetReviewTemplateLensReviewOutput(BaseValidatorModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReview
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_review_template_lens_review' function.
class UpdateReviewTemplateLensReviewOutput(BaseValidatorModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReview
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_workload' function.
class CreateWorkloadInput(BaseValidatorModel):
    WorkloadName: str
    Description: str
    Environment: WorkloadEnvironmentType
    Lenses: List[str]
    ClientRequestToken: str
    AccountIds: Optional[List[str]] = None
    AwsRegions: Optional[List[str]] = None
    NonAwsRegions: Optional[List[str]] = None
    PillarPriorities: Optional[List[str]] = None
    ArchitecturalDesign: Optional[str] = None
    ReviewOwner: Optional[str] = None
    IndustryType: Optional[str] = None
    Industry: Optional[str] = None
    Notes: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigUnion] = None
    Applications: Optional[List[str]] = None
    ProfileArns: Optional[List[str]] = None
    ReviewTemplateArns: Optional[List[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInput] = None


# This class is the input for the 'update_workload' function.
class UpdateWorkloadInput(BaseValidatorModel):
    WorkloadId: str
    WorkloadName: Optional[str] = None
    Description: Optional[str] = None
    Environment: Optional[WorkloadEnvironmentType] = None
    AccountIds: Optional[List[str]] = None
    AwsRegions: Optional[List[str]] = None
    NonAwsRegions: Optional[List[str]] = None
    PillarPriorities: Optional[List[str]] = None
    ArchitecturalDesign: Optional[str] = None
    ReviewOwner: Optional[str] = None
    IsReviewOwnerUpdateAcknowledged: Optional[bool] = None
    IndustryType: Optional[str] = None
    Industry: Optional[str] = None
    Notes: Optional[str] = None
    ImprovementStatus: Optional[WorkloadImprovementStatusType] = None
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigUnion] = None
    Applications: Optional[List[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInput] = None


# This class is the output for the 'get_workload' function.
class GetWorkloadOutput(BaseValidatorModel):
    Workload: Workload
    ResponseMetadata: ResponseMetadata


class Milestone(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    Workload: Optional[Workload] = None


# This class is the output for the 'update_workload' function.
class UpdateWorkloadOutput(BaseValidatorModel):
    Workload: Workload
    ResponseMetadata: ResponseMetadata


class AnswerSummary(BaseValidatorModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Choices: Optional[List[Choice]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswerSummaries: Optional[List[ChoiceAnswerSummary]] = None
    IsApplicable: Optional[bool] = None
    Risk: Optional[RiskType] = None
    Reason: Optional[AnswerReasonType] = None
    QuestionType: Optional[QuestionTypeType] = None
    JiraConfiguration: Optional[JiraConfiguration] = None


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


class ReviewTemplateAnswerSummary(BaseValidatorModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Choices: Optional[List[Choice]] = None
    SelectedChoices: Optional[List[str]] = None
    ChoiceAnswerSummaries: Optional[List[ChoiceAnswerSummary]] = None
    IsApplicable: Optional[bool] = None
    AnswerStatus: Optional[ReviewTemplateAnswerStatusType] = None
    Reason: Optional[AnswerReasonType] = None
    QuestionType: Optional[QuestionTypeType] = None


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


# This class is the output for the 'get_lens_review' function.
class GetLensReviewOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReview: LensReview
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_lens_review' function.
class UpdateLensReviewOutput(BaseValidatorModel):
    WorkloadId: str
    LensReview: LensReview
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_lens_review' function.
class UpdateLensReviewInput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Dict[str, str]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationUnion] = None


# This class is the output for the 'list_milestones' function.
class ListMilestonesOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneSummaries: List[MilestoneSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_lens_version_difference' function.
class GetLensVersionDifferenceOutput(BaseValidatorModel):
    LensAlias: str
    LensArn: str
    BaseLensVersion: str
    TargetLensVersion: str
    LatestLensVersion: str
    VersionDifferences: VersionDifferences
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_profile' function.
class GetProfileOutput(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_profile' function.
class UpdateProfileOutput(BaseValidatorModel):
    Profile: Profile
    ResponseMetadata: ResponseMetadata


class GetProfileTemplateOutput(BaseValidatorModel):
    ProfileTemplate: ProfileTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_milestone' function.
class GetMilestoneOutput(BaseValidatorModel):
    WorkloadId: str
    Milestone: Milestone
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_answers' function.
class ListAnswersOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    AnswerSummaries: List[AnswerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_answer' function.
class GetAnswerOutput(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    Answer: Answer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_answer' function.
class UpdateAnswerOutput(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensArn: str
    Answer: Answer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_review_template_answers' function.
class ListReviewTemplateAnswersOutput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    AnswerSummaries: List[ReviewTemplateAnswerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_review_template_answer' function.
class GetReviewTemplateAnswerOutput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_review_template_answer' function.
class UpdateReviewTemplateAnswerOutput(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswer
    ResponseMetadata: ResponseMetadata


class ConsolidatedReportMetric(BaseValidatorModel):
    MetricType: Optional[Literal['WORKLOAD']] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    WorkloadArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    Lenses: Optional[List[LensMetric]] = None
    LensesAppliedCount: Optional[int] = None


# This class is the output for the 'get_consolidated_report' function.
class GetConsolidatedReportOutput(BaseValidatorModel):
    Metrics: List[ConsolidatedReportMetric]
    Base64String: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None