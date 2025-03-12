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

class AccountJiraConfigurationInputTypeDef(BaseValidatorModel):
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    IntegrationStatus: Optional[Literal["NOT_CONFIGURED"]] = None


class AccountJiraConfigurationOutputTypeDef(BaseValidatorModel):
    IntegrationStatus: Optional[IntegrationStatusType] = None
    IssueManagementStatus: Optional[AccountJiraIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    Subdomain: Optional[str] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None


class ChoiceContentTypeDef(BaseValidatorModel):
    DisplayText: Optional[str] = None
    Url: Optional[str] = None


class ChoiceAnswerSummaryTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    Status: Optional[ChoiceStatusType] = None
    Reason: Optional[ChoiceReasonType] = None


class JiraConfigurationTypeDef(BaseValidatorModel):
    JiraIssueUrl: Optional[str] = None
    LastSyncedTime: Optional[datetime] = None


class ChoiceAnswerTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    Status: Optional[ChoiceStatusType] = None
    Reason: Optional[ChoiceReasonType] = None
    Notes: Optional[str] = None


class AssociateLensesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAliases: Sequence[str]


class AssociateProfilesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: Sequence[str]


class BestPracticeTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None


class CheckDetailTypeDef(BaseValidatorModel):
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


class CheckSummaryTypeDef(BaseValidatorModel):
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


class ChoiceImprovementPlanTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    DisplayText: Optional[str] = None
    ImprovementPlanUrl: Optional[str] = None


class ChoiceUpdateTypeDef(BaseValidatorModel):
    Status: ChoiceStatusType
    Reason: Optional[ChoiceReasonType] = None
    Notes: Optional[str] = None


class CreateLensShareInputTypeDef(BaseValidatorModel):
    LensAlias: str
    SharedWith: str
    ClientRequestToken: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateLensVersionInputTypeDef(BaseValidatorModel):
    LensAlias: str
    LensVersion: str
    ClientRequestToken: str
    IsMajorVersion: Optional[bool] = None


class CreateMilestoneInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneName: str
    ClientRequestToken: str


class ProfileQuestionUpdateTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    SelectedChoiceIds: Optional[Sequence[str]] = None


class CreateProfileShareInputTypeDef(BaseValidatorModel):
    ProfileArn: str
    SharedWith: str
    ClientRequestToken: str


class CreateReviewTemplateInputTypeDef(BaseValidatorModel):
    TemplateName: str
    Description: str
    Lenses: Sequence[str]
    ClientRequestToken: str
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateTemplateShareInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    SharedWith: str
    ClientRequestToken: str


class WorkloadJiraConfigurationInputTypeDef(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None


class CreateWorkloadShareInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    SharedWith: str
    PermissionType: PermissionTypeType
    ClientRequestToken: str


class DeleteLensInputTypeDef(BaseValidatorModel):
    LensAlias: str
    ClientRequestToken: str
    LensStatus: LensStatusTypeType


class DeleteLensShareInputTypeDef(BaseValidatorModel):
    ShareId: str
    LensAlias: str
    ClientRequestToken: str


class DeleteProfileInputTypeDef(BaseValidatorModel):
    ProfileArn: str
    ClientRequestToken: str


class DeleteProfileShareInputTypeDef(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ClientRequestToken: str


class DeleteReviewTemplateInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    ClientRequestToken: str


class DeleteTemplateShareInputTypeDef(BaseValidatorModel):
    ShareId: str
    TemplateArn: str
    ClientRequestToken: str


class DeleteWorkloadInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str


class DeleteWorkloadShareInputTypeDef(BaseValidatorModel):
    ShareId: str
    WorkloadId: str
    ClientRequestToken: str


class DisassociateLensesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAliases: Sequence[str]


class DisassociateProfilesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: Sequence[str]


class ExportLensInputTypeDef(BaseValidatorModel):
    LensAlias: str
    LensVersion: Optional[str] = None


class GetAnswerInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    MilestoneNumber: Optional[int] = None


class GetConsolidatedReportInputTypeDef(BaseValidatorModel):
    Format: ReportFormatType
    IncludeSharedResources: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetLensInputTypeDef(BaseValidatorModel):
    LensAlias: str
    LensVersion: Optional[str] = None


class LensTypeDef(BaseValidatorModel):
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    ShareInvitationId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class GetLensReviewInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None


class GetLensReviewReportInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None


class LensReviewReportTypeDef(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    Base64String: Optional[str] = None


class GetLensVersionDifferenceInputTypeDef(BaseValidatorModel):
    LensAlias: str
    BaseLensVersion: Optional[str] = None
    TargetLensVersion: Optional[str] = None


class GetMilestoneInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int


class GetProfileInputTypeDef(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: Optional[str] = None


class GetReviewTemplateAnswerInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str


class GetReviewTemplateInputTypeDef(BaseValidatorModel):
    TemplateArn: str


class GetReviewTemplateLensReviewInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str


class ReviewTemplateTypeDef(BaseValidatorModel):
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


class GetWorkloadInputTypeDef(BaseValidatorModel):
    WorkloadId: str


class ImportLensInputTypeDef(BaseValidatorModel):
    JSONString: str
    ClientRequestToken: str
    LensAlias: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class SelectedPillarOutputTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[List[str]] = None


class SelectedPillarTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[Sequence[str]] = None


class WorkloadProfileTypeDef(BaseValidatorModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None


class PillarReviewSummaryTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    Notes: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class LensShareSummaryTypeDef(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class LensSummaryTypeDef(BaseValidatorModel):
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


class LensUpgradeSummaryTypeDef(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    CurrentLensVersion: Optional[str] = None
    LatestLensVersion: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceName: Optional[str] = None


class ListAnswersInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None


class ListCheckDetailsInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCheckSummariesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLensReviewImprovementsInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None


class ListLensReviewsInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLensSharesInputTypeDef(BaseValidatorModel):
    LensAlias: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class ListLensesInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LensType: Optional[LensTypeType] = None
    LensStatus: Optional[LensStatusTypeType] = None
    LensName: Optional[str] = None


class ListMilestonesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListNotificationsInputTypeDef(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceArn: Optional[str] = None


class ListProfileNotificationsInputTypeDef(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileSharesInputTypeDef(BaseValidatorModel):
    ProfileArn: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class ProfileShareSummaryTypeDef(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class ListProfilesInputTypeDef(BaseValidatorModel):
    ProfileNamePrefix: Optional[str] = None
    ProfileOwnerType: Optional[ProfileOwnerTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProfileSummaryTypeDef(BaseValidatorModel):
    ProfileArn: Optional[str] = None
    ProfileVersion: Optional[str] = None
    ProfileName: Optional[str] = None
    ProfileDescription: Optional[str] = None
    Owner: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ListReviewTemplateAnswersInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    PillarId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReviewTemplatesInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ReviewTemplateSummaryTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Lenses: Optional[List[str]] = None
    Owner: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    TemplateArn: Optional[str] = None
    TemplateName: Optional[str] = None
    UpdateStatus: Optional[ReviewTemplateUpdateStatusType] = None


class ListShareInvitationsInputTypeDef(BaseValidatorModel):
    WorkloadNamePrefix: Optional[str] = None
    LensNamePrefix: Optional[str] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProfileNamePrefix: Optional[str] = None
    TemplateNamePrefix: Optional[str] = None


class ShareInvitationSummaryTypeDef(BaseValidatorModel):
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


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    WorkloadArn: str


class ListTemplateSharesInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class TemplateShareSummaryTypeDef(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class ListWorkloadSharesInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None


class WorkloadShareSummaryTypeDef(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    Status: Optional[ShareStatusType] = None
    StatusMessage: Optional[str] = None


class ListWorkloadsInputTypeDef(BaseValidatorModel):
    WorkloadNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QuestionDifferenceTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    DifferenceStatus: Optional[DifferenceStatusType] = None


class ProfileChoiceTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None
    ChoiceDescription: Optional[str] = None


class ProfileTemplateChoiceTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    ChoiceTitle: Optional[str] = None
    ChoiceDescription: Optional[str] = None


class ReviewTemplatePillarReviewSummaryTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    Notes: Optional[str] = None
    QuestionCounts: Optional[Dict[QuestionType, int]] = None


class ShareInvitationTypeDef(BaseValidatorModel):
    ShareInvitationId: Optional[str] = None
    ShareResourceType: Optional[ShareResourceTypeType] = None
    WorkloadId: Optional[str] = None
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    ProfileArn: Optional[str] = None
    TemplateArn: Optional[str] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    WorkloadArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    WorkloadArn: str
    TagKeys: Sequence[str]


class UpdateIntegrationInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str
    IntegratingService: Literal["JIRA"]


class UpdateReviewTemplateInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None
    LensesToAssociate: Optional[Sequence[str]] = None
    LensesToDisassociate: Optional[Sequence[str]] = None


class UpdateReviewTemplateLensReviewInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None


class UpdateShareInvitationInputTypeDef(BaseValidatorModel):
    ShareInvitationId: str
    ShareInvitationAction: ShareInvitationActionType


class UpdateWorkloadShareInputTypeDef(BaseValidatorModel):
    ShareId: str
    WorkloadId: str
    PermissionType: PermissionTypeType


class WorkloadShareTypeDef(BaseValidatorModel):
    ShareId: Optional[str] = None
    SharedBy: Optional[str] = None
    SharedWith: Optional[str] = None
    PermissionType: Optional[PermissionTypeType] = None
    Status: Optional[ShareStatusType] = None
    WorkloadName: Optional[str] = None
    WorkloadId: Optional[str] = None


class UpgradeLensReviewInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneName: str
    ClientRequestToken: Optional[str] = None


class UpgradeProfileVersionInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    ProfileArn: str
    MilestoneName: Optional[str] = None
    ClientRequestToken: Optional[str] = None


class UpgradeReviewTemplateLensReviewInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    ClientRequestToken: Optional[str] = None


class WorkloadDiscoveryConfigOutputTypeDef(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[List[DefinitionTypeType]] = None


class WorkloadDiscoveryConfigTypeDef(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[Sequence[DefinitionTypeType]] = None


class WorkloadJiraConfigurationOutputTypeDef(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None


class UpdateGlobalSettingsInputTypeDef(BaseValidatorModel):
    OrganizationSharingStatus: Optional[OrganizationSharingStatusType] = None
    DiscoveryIntegrationStatus: Optional[DiscoveryIntegrationStatusType] = None
    JiraConfiguration: Optional[AccountJiraConfigurationInputTypeDef] = None


class QuestionMetricTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    Risk: Optional[RiskType] = None
    BestPractices: Optional[List[BestPracticeTypeDef]] = None


class ImprovementSummaryTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    PillarId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    Risk: Optional[RiskType] = None
    ImprovementPlanUrl: Optional[str] = None
    ImprovementPlans: Optional[List[ChoiceImprovementPlanTypeDef]] = None
    JiraConfiguration: Optional[JiraConfigurationTypeDef] = None


class UpdateAnswerInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdateTypeDef]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None


class UpdateReviewTemplateAnswerInputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdateTypeDef]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None


class CreateLensShareOutputTypeDef(BaseValidatorModel):
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLensVersionOutputTypeDef(BaseValidatorModel):
    LensArn: str
    LensVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMilestoneOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProfileOutputTypeDef(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProfileShareOutputTypeDef(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateReviewTemplateOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTemplateShareOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkloadOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkloadShareOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    ShareId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExportLensOutputTypeDef(BaseValidatorModel):
    LensJSON: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetGlobalSettingsOutputTypeDef(BaseValidatorModel):
    OrganizationSharingStatus: OrganizationSharingStatusType
    DiscoveryIntegrationStatus: DiscoveryIntegrationStatusType
    JiraConfiguration: AccountJiraConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImportLensOutputTypeDef(BaseValidatorModel):
    LensArn: str
    Status: ImportLensStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListCheckDetailsOutputTypeDef(BaseValidatorModel):
    CheckDetails: List[CheckDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCheckSummariesOutputTypeDef(BaseValidatorModel):
    CheckSummaries: List[CheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProfileInputTypeDef(BaseValidatorModel):
    ProfileName: str
    ProfileDescription: str
    ProfileQuestions: Sequence[ProfileQuestionUpdateTypeDef]
    ClientRequestToken: str
    Tags: Optional[Mapping[str, str]] = None


class UpdateProfileInputTypeDef(BaseValidatorModel):
    ProfileArn: str
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[Sequence[ProfileQuestionUpdateTypeDef]] = None


class GetLensOutputTypeDef(BaseValidatorModel):
    Lens: LensTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLensReviewReportOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewReport: LensReviewReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetReviewTemplateOutputTypeDef(BaseValidatorModel):
    ReviewTemplate: ReviewTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateReviewTemplateOutputTypeDef(BaseValidatorModel):
    ReviewTemplate: ReviewTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JiraSelectedQuestionConfigurationOutputTypeDef(BaseValidatorModel):
    SelectedPillars: Optional[List[SelectedPillarOutputTypeDef]] = None


class JiraSelectedQuestionConfigurationTypeDef(BaseValidatorModel):
    SelectedPillars: Optional[Sequence[SelectedPillarTypeDef]] = None


class LensReviewSummaryTypeDef(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    UpdatedAt: Optional[datetime] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class WorkloadSummaryTypeDef(BaseValidatorModel):
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


class ListLensSharesOutputTypeDef(BaseValidatorModel):
    LensShareSummaries: List[LensShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLensesOutputTypeDef(BaseValidatorModel):
    LensSummaries: List[LensSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ProfileNotificationSummaryTypeDef(BaseValidatorModel):
    pass


class ListProfileNotificationsOutputTypeDef(BaseValidatorModel):
    NotificationSummaries: List[ProfileNotificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProfileSharesOutputTypeDef(BaseValidatorModel):
    ProfileShareSummaries: List[ProfileShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProfilesOutputTypeDef(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReviewTemplatesOutputTypeDef(BaseValidatorModel):
    ReviewTemplates: List[ReviewTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListShareInvitationsOutputTypeDef(BaseValidatorModel):
    ShareInvitationSummaries: List[ShareInvitationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTemplateSharesOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    TemplateShareSummaries: List[TemplateShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWorkloadSharesOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadShareSummaries: List[WorkloadShareSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PillarDifferenceTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    PillarName: Optional[str] = None
    DifferenceStatus: Optional[DifferenceStatusType] = None
    QuestionDifferences: Optional[List[QuestionDifferenceTypeDef]] = None


class ProfileQuestionTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    QuestionChoices: Optional[List[ProfileChoiceTypeDef]] = None
    SelectedChoiceIds: Optional[List[str]] = None
    MinSelectedChoices: Optional[int] = None
    MaxSelectedChoices: Optional[int] = None


class ProfileTemplateQuestionTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    QuestionTitle: Optional[str] = None
    QuestionDescription: Optional[str] = None
    QuestionChoices: Optional[List[ProfileTemplateChoiceTypeDef]] = None
    MinSelectedChoices: Optional[int] = None
    MaxSelectedChoices: Optional[int] = None


class ReviewTemplateLensReviewTypeDef(BaseValidatorModel):
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


class UpdateShareInvitationOutputTypeDef(BaseValidatorModel):
    ShareInvitation: ShareInvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWorkloadShareOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadShare: WorkloadShareTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WorkloadTypeDef(BaseValidatorModel):
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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigOutputTypeDef] = None
    Applications: Optional[List[str]] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationOutputTypeDef] = None


class AdditionalResourcesTypeDef(BaseValidatorModel):
    pass


class ChoiceTypeDef(BaseValidatorModel):
    ChoiceId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    HelpfulResource: Optional[ChoiceContentTypeDef] = None
    ImprovementPlan: Optional[ChoiceContentTypeDef] = None
    AdditionalResources: Optional[List[AdditionalResourcesTypeDef]] = None


class PillarMetricTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    Questions: Optional[List[QuestionMetricTypeDef]] = None


class ListLensReviewImprovementsOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    ImprovementSummaries: List[ImprovementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LensReviewTypeDef(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    LensVersion: Optional[str] = None
    LensName: Optional[str] = None
    LensStatus: Optional[LensStatusType] = None
    PillarReviewSummaries: Optional[List[PillarReviewSummaryTypeDef]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationOutputTypeDef] = None
    UpdatedAt: Optional[datetime] = None
    Notes: Optional[str] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    NextToken: Optional[str] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None


class ListLensReviewsOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List[LensReviewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWorkloadsOutputTypeDef(BaseValidatorModel):
    WorkloadSummaries: List[WorkloadSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MilestoneSummaryTypeDef(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    WorkloadSummary: Optional[WorkloadSummaryTypeDef] = None


class NotificationSummaryTypeDef(BaseValidatorModel):
    pass


class ListNotificationsOutputTypeDef(BaseValidatorModel):
    NotificationSummaries: List[NotificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class VersionDifferencesTypeDef(BaseValidatorModel):
    PillarDifferences: Optional[List[PillarDifferenceTypeDef]] = None


class ProfileTypeDef(BaseValidatorModel):
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


class ProfileTemplateTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    TemplateQuestions: Optional[List[ProfileTemplateQuestionTypeDef]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class GetReviewTemplateLensReviewOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateReviewTemplateLensReviewOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensReview: ReviewTemplateLensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WorkloadDiscoveryConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateWorkloadInputTypeDef(BaseValidatorModel):
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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigUnionTypeDef] = None
    Applications: Optional[Sequence[str]] = None
    ProfileArns: Optional[Sequence[str]] = None
    ReviewTemplateArns: Optional[Sequence[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInputTypeDef] = None


class UpdateWorkloadInputTypeDef(BaseValidatorModel):
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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigUnionTypeDef] = None
    Applications: Optional[Sequence[str]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationInputTypeDef] = None


class GetWorkloadOutputTypeDef(BaseValidatorModel):
    Workload: WorkloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MilestoneTypeDef(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    Workload: Optional[WorkloadTypeDef] = None


class UpdateWorkloadOutputTypeDef(BaseValidatorModel):
    Workload: WorkloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AnswerTypeDef(BaseValidatorModel):
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


class ReviewTemplateAnswerTypeDef(BaseValidatorModel):
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


class LensMetricTypeDef(BaseValidatorModel):
    LensArn: Optional[str] = None
    Pillars: Optional[List[PillarMetricTypeDef]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None


class GetLensReviewOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReview: LensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLensReviewOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensReview: LensReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JiraSelectedQuestionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateLensReviewInputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationUnionTypeDef] = None


class ListMilestonesOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneSummaries: List[MilestoneSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetLensVersionDifferenceOutputTypeDef(BaseValidatorModel):
    LensAlias: str
    LensArn: str
    BaseLensVersion: str
    TargetLensVersion: str
    LatestLensVersion: str
    VersionDifferences: VersionDifferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetProfileOutputTypeDef(BaseValidatorModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProfileOutputTypeDef(BaseValidatorModel):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetProfileTemplateOutputTypeDef(BaseValidatorModel):
    ProfileTemplate: ProfileTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMilestoneOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    Milestone: MilestoneTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AnswerSummaryTypeDef(BaseValidatorModel):
    pass


class ListAnswersOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    AnswerSummaries: List[AnswerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetAnswerOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    Answer: AnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAnswerOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensArn: str
    Answer: AnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReviewTemplateAnswerSummaryTypeDef(BaseValidatorModel):
    pass


class ListReviewTemplateAnswersOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    AnswerSummaries: List[ReviewTemplateAnswerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetReviewTemplateAnswerOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateReviewTemplateAnswerOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    Answer: ReviewTemplateAnswerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConsolidatedReportMetricTypeDef(BaseValidatorModel):
    MetricType: Optional[Literal["WORKLOAD"]] = None
    RiskCounts: Optional[Dict[RiskType, int]] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None
    WorkloadArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    Lenses: Optional[List[LensMetricTypeDef]] = None
    LensesAppliedCount: Optional[int] = None


class GetConsolidatedReportOutputTypeDef(BaseValidatorModel):
    Metrics: List[ConsolidatedReportMetricTypeDef]
    Base64String: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


