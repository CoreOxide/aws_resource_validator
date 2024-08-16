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

class AssociateLensesInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAliases: Sequence[str]

class AssociateProfilesInputRequestTypeDef(BaseValidatorModel):
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

class CreateLensShareInputRequestTypeDef(BaseValidatorModel):
    LensAlias: str
    SharedWith: str
    ClientRequestToken: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateLensVersionInputRequestTypeDef(BaseValidatorModel):
    LensAlias: str
    LensVersion: str
    ClientRequestToken: str
    IsMajorVersion: Optional[bool] = None

class CreateMilestoneInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneName: str
    ClientRequestToken: str

class ProfileQuestionUpdateTypeDef(BaseValidatorModel):
    QuestionId: Optional[str] = None
    SelectedChoiceIds: Optional[Sequence[str]] = None

class CreateProfileShareInputRequestTypeDef(BaseValidatorModel):
    ProfileArn: str
    SharedWith: str
    ClientRequestToken: str

class CreateReviewTemplateInputRequestTypeDef(BaseValidatorModel):
    TemplateName: str
    Description: str
    Lenses: Sequence[str]
    ClientRequestToken: str
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateTemplateShareInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    SharedWith: str
    ClientRequestToken: str

class WorkloadDiscoveryConfigTypeDef(BaseValidatorModel):
    TrustedAdvisorIntegrationStatus: Optional[TrustedAdvisorIntegrationStatusType] = None
    WorkloadResourceDefinition: Optional[Sequence[DefinitionTypeType]] = None

class WorkloadJiraConfigurationInputTypeDef(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None

class CreateWorkloadShareInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    SharedWith: str
    PermissionType: PermissionTypeType
    ClientRequestToken: str

class DeleteLensInputRequestTypeDef(BaseValidatorModel):
    LensAlias: str
    ClientRequestToken: str
    LensStatus: LensStatusTypeType

class DeleteLensShareInputRequestTypeDef(BaseValidatorModel):
    ShareId: str
    LensAlias: str
    ClientRequestToken: str

class DeleteProfileInputRequestTypeDef(BaseValidatorModel):
    ProfileArn: str
    ClientRequestToken: str

class DeleteProfileShareInputRequestTypeDef(BaseValidatorModel):
    ShareId: str
    ProfileArn: str
    ClientRequestToken: str

class DeleteReviewTemplateInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    ClientRequestToken: str

class DeleteTemplateShareInputRequestTypeDef(BaseValidatorModel):
    ShareId: str
    TemplateArn: str
    ClientRequestToken: str

class DeleteWorkloadInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str

class DeleteWorkloadShareInputRequestTypeDef(BaseValidatorModel):
    ShareId: str
    WorkloadId: str
    ClientRequestToken: str

class DisassociateLensesInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAliases: Sequence[str]

class DisassociateProfilesInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    ProfileArns: Sequence[str]

class ExportLensInputRequestTypeDef(BaseValidatorModel):
    LensAlias: str
    LensVersion: Optional[str] = None

class GetAnswerInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    MilestoneNumber: Optional[int] = None

class GetConsolidatedReportInputRequestTypeDef(BaseValidatorModel):
    Format: ReportFormatType
    IncludeSharedResources: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetLensInputRequestTypeDef(BaseValidatorModel):
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

class GetLensReviewInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None

class GetLensReviewReportInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneNumber: Optional[int] = None

class LensReviewReportTypeDef(BaseValidatorModel):
    LensAlias: Optional[str] = None
    LensArn: Optional[str] = None
    Base64String: Optional[str] = None

class GetLensVersionDifferenceInputRequestTypeDef(BaseValidatorModel):
    LensAlias: str
    BaseLensVersion: Optional[str] = None
    TargetLensVersion: Optional[str] = None

class GetMilestoneInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int

class GetProfileInputRequestTypeDef(BaseValidatorModel):
    ProfileArn: str
    ProfileVersion: Optional[str] = None

class GetReviewTemplateAnswerInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    QuestionId: str

class GetReviewTemplateInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str

class GetReviewTemplateLensReviewInputRequestTypeDef(BaseValidatorModel):
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

class GetWorkloadInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str

class ImportLensInputRequestTypeDef(BaseValidatorModel):
    JSONString: str
    ClientRequestToken: str
    LensAlias: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class SelectedPillarTypeDef(BaseValidatorModel):
    PillarId: Optional[str] = None
    SelectedQuestionIds: Optional[List[str]] = None

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

class ListAnswersInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None

class ListCheckDetailsInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCheckSummariesInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensArn: str
    PillarId: str
    QuestionId: str
    ChoiceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLensReviewImprovementsInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    PillarId: Optional[str] = None
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuestionPriority: Optional[QuestionPriorityType] = None

class ListLensReviewsInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLensSharesInputRequestTypeDef(BaseValidatorModel):
    LensAlias: str
    SharedWithPrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ShareStatusType] = None

class ListLensesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LensType: Optional[LensTypeType] = None
    LensStatus: Optional[LensStatusTypeType] = None
    LensName: Optional[str] = None

class ListMilestonesInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListNotificationsInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceArn: Optional[str] = None

class ListProfileNotificationsInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProfileNotificationSummaryTypeDef(BaseValidatorModel):
    CurrentProfileVersion: Optional[str] = None
    LatestProfileVersion: Optional[str] = None
    Type: Optional[ProfileNotificationTypeType] = None
    ProfileArn: Optional[str] = None
    ProfileName: Optional[str] = None
    WorkloadId: Optional[str] = None
    WorkloadName: Optional[str] = None

class ListProfileSharesInputRequestTypeDef(BaseValidatorModel):
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

class ListProfilesInputRequestTypeDef(BaseValidatorModel):
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

class ListReviewTemplateAnswersInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    PillarId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReviewTemplatesInputRequestTypeDef(BaseValidatorModel):
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

class ListShareInvitationsInputRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    WorkloadArn: str

class ListTemplateSharesInputRequestTypeDef(BaseValidatorModel):
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

class ListWorkloadSharesInputRequestTypeDef(BaseValidatorModel):
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

class ListWorkloadsInputRequestTypeDef(BaseValidatorModel):
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

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    WorkloadArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    WorkloadArn: str
    TagKeys: Sequence[str]

class UpdateIntegrationInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    ClientRequestToken: str
    IntegratingService: Literal["JIRA"]

class UpdateReviewTemplateInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None
    LensesToAssociate: Optional[Sequence[str]] = None
    LensesToDisassociate: Optional[Sequence[str]] = None

class UpdateReviewTemplateLensReviewInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None

class UpdateShareInvitationInputRequestTypeDef(BaseValidatorModel):
    ShareInvitationId: str
    ShareInvitationAction: ShareInvitationActionType

class UpdateWorkloadShareInputRequestTypeDef(BaseValidatorModel):
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

class UpgradeLensReviewInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    MilestoneName: str
    ClientRequestToken: Optional[str] = None

class UpgradeProfileVersionInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    ProfileArn: str
    MilestoneName: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class UpgradeReviewTemplateLensReviewInputRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    ClientRequestToken: Optional[str] = None

class WorkloadJiraConfigurationOutputTypeDef(BaseValidatorModel):
    IssueManagementStatus: Optional[WorkloadIssueManagementStatusType] = None
    IssueManagementType: Optional[IssueManagementTypeType] = None
    JiraProjectKey: Optional[str] = None
    StatusMessage: Optional[str] = None

class UpdateGlobalSettingsInputRequestTypeDef(BaseValidatorModel):
    OrganizationSharingStatus: Optional[OrganizationSharingStatusType] = None
    DiscoveryIntegrationStatus: Optional[DiscoveryIntegrationStatusType] = None
    JiraConfiguration: Optional[AccountJiraConfigurationInputTypeDef] = None

class AdditionalResourcesTypeDef(BaseValidatorModel):
    Type: Optional[AdditionalResourceTypeType] = None
    Content: Optional[List[ChoiceContentTypeDef]] = None

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

class UpdateAnswerInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    QuestionId: str
    SelectedChoices: Optional[Sequence[str]] = None
    ChoiceUpdates: Optional[Mapping[str, ChoiceUpdateTypeDef]] = None
    Notes: Optional[str] = None
    IsApplicable: Optional[bool] = None
    Reason: Optional[AnswerReasonType] = None

class UpdateReviewTemplateAnswerInputRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCheckSummariesOutputTypeDef(BaseValidatorModel):
    CheckSummaries: List[CheckSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileInputRequestTypeDef(BaseValidatorModel):
    ProfileName: str
    ProfileDescription: str
    ProfileQuestions: Sequence[ProfileQuestionUpdateTypeDef]
    ClientRequestToken: str
    Tags: Optional[Mapping[str, str]] = None

class UpdateProfileInputRequestTypeDef(BaseValidatorModel):
    ProfileArn: str
    ProfileDescription: Optional[str] = None
    ProfileQuestions: Optional[Sequence[ProfileQuestionUpdateTypeDef]] = None

class CreateWorkloadInputRequestTypeDef(BaseValidatorModel):
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

class UpdateWorkloadInputRequestTypeDef(BaseValidatorModel):
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

class JiraSelectedQuestionConfigurationTypeDef(BaseValidatorModel):
    SelectedPillars: Optional[List[SelectedPillarTypeDef]] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLensesOutputTypeDef(BaseValidatorModel):
    LensSummaries: List[LensSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotificationSummaryTypeDef(BaseValidatorModel):
    Type: Optional[NotificationTypeType] = None
    LensUpgradeSummary: Optional[LensUpgradeSummaryTypeDef] = None

class ListProfileNotificationsOutputTypeDef(BaseValidatorModel):
    NotificationSummaries: List[ProfileNotificationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileSharesOutputTypeDef(BaseValidatorModel):
    ProfileShareSummaries: List[ProfileShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesOutputTypeDef(BaseValidatorModel):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewTemplatesOutputTypeDef(BaseValidatorModel):
    ReviewTemplates: List[ReviewTemplateSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListShareInvitationsOutputTypeDef(BaseValidatorModel):
    ShareInvitationSummaries: List[ShareInvitationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateSharesOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    TemplateShareSummaries: List[TemplateShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkloadSharesOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadShareSummaries: List[WorkloadShareSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    DiscoveryConfig: Optional[WorkloadDiscoveryConfigTypeDef] = None
    Applications: Optional[List[str]] = None
    Profiles: Optional[List[WorkloadProfileTypeDef]] = None
    PrioritizedRiskCounts: Optional[Dict[RiskType, int]] = None
    JiraConfiguration: Optional[WorkloadJiraConfigurationOutputTypeDef] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LensReviewTypeDef(BaseValidatorModel):
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

class UpdateLensReviewInputRequestTypeDef(BaseValidatorModel):
    WorkloadId: str
    LensAlias: str
    LensNotes: Optional[str] = None
    PillarNotes: Optional[Mapping[str, str]] = None
    JiraConfiguration: Optional[JiraSelectedQuestionConfigurationTypeDef] = None

class ListLensReviewsOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List[LensReviewSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkloadsOutputTypeDef(BaseValidatorModel):
    WorkloadSummaries: List[WorkloadSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MilestoneSummaryTypeDef(BaseValidatorModel):
    MilestoneNumber: Optional[int] = None
    MilestoneName: Optional[str] = None
    RecordedAt: Optional[datetime] = None
    WorkloadSummary: Optional[WorkloadSummaryTypeDef] = None

class ListNotificationsOutputTypeDef(BaseValidatorModel):
    NotificationSummaries: List[NotificationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class AnswerSummaryTypeDef(BaseValidatorModel):
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

class ReviewTemplateAnswerSummaryTypeDef(BaseValidatorModel):
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

class ListMilestonesOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneSummaries: List[MilestoneSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListAnswersOutputTypeDef(BaseValidatorModel):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    LensArn: str
    AnswerSummaries: List[AnswerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListReviewTemplateAnswersOutputTypeDef(BaseValidatorModel):
    TemplateArn: str
    LensAlias: str
    AnswerSummaries: List[ReviewTemplateAnswerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    Base64String: str
    ResponseMetadata: ResponseMetadataTypeDef

