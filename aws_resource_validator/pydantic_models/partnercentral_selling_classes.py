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
from aws_resource_validator.pydantic_models.partnercentral_selling_constants import *

class AcceptEngagementInvitationRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str


class AccountReceiverTypeDef(BaseValidatorModel):
    AwsAccountId: str
    Alias: Optional[str] = None


class AddressSummaryTypeDef(BaseValidatorModel):
    City: Optional[str] = None
    CountryCode: Optional[CountryCodeType] = None
    PostalCode: Optional[str] = None
    StateOrRegion: Optional[str] = None


class AddressTypeDef(BaseValidatorModel):
    City: Optional[str] = None
    CountryCode: Optional[CountryCodeType] = None
    PostalCode: Optional[str] = None
    StateOrRegion: Optional[str] = None
    StreetAddress: Optional[str] = None


class AssigneeContactTypeDef(BaseValidatorModel):
    BusinessTitle: str
    Email: str
    FirstName: str
    LastName: str


class AssociateOpportunityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType


class ContactTypeDef(BaseValidatorModel):
    BusinessTitle: Optional[str] = None
    Email: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None


class AwsOpportunityInsightsTypeDef(BaseValidatorModel):
    EngagementScore: Optional[EngagementScoreType] = None
    NextBestActions: Optional[str] = None


class ProfileNextStepsHistoryTypeDef(BaseValidatorModel):
    Time: datetime
    Value: str


class ExpectedCustomerSpendTypeDef(BaseValidatorModel):
    Amount: str
    CurrencyCode: ExpectedCustomerSpendCurrencyCodeEnumType
    Frequency: Literal["Monthly"]
    TargetCompany: str
    EstimationUrl: Optional[str] = None


class AwsOpportunityRelatedEntitiesTypeDef(BaseValidatorModel):
    AwsProducts: Optional[List[str]] = None
    Solutions: Optional[List[str]] = None


class AwsSubmissionTypeDef(BaseValidatorModel):
    InvolvementType: SalesInvolvementTypeType
    Visibility: Optional[VisibilityType] = None


class AwsTeamMemberTypeDef(BaseValidatorModel):
    BusinessTitle: Optional[AwsMemberBusinessTitleType] = None
    Email: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateResourceSnapshotRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal["Opportunity"]


class EngagementCustomerProjectDetailsTypeDef(BaseValidatorModel):
    BusinessProblem: str
    TargetCompletionDate: str
    Title: str


class EngagementCustomerTypeDef(BaseValidatorModel):
    CompanyName: str
    CountryCode: CountryCodeType
    Industry: IndustryType
    WebsiteUrl: str


class DeleteResourceSnapshotJobRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class DisassociateOpportunityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType


class EngagementMemberSummaryTypeDef(BaseValidatorModel):
    CompanyName: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class EngagementMemberTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    CompanyName: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class EngagementResourceAssociationSummaryTypeDef(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[str] = None
    EngagementId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal["Opportunity"]] = None


class EngagementSortTypeDef(BaseValidatorModel):
    SortBy: Literal["CreatedDate"]
    SortOrder: SortOrderType


class EngagementSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    Id: Optional[str] = None
    MemberCount: Optional[int] = None
    Title: Optional[str] = None


class GetAwsOpportunitySummaryRequestTypeDef(BaseValidatorModel):
    Catalog: str
    RelatedOpportunityIdentifier: str


class GetEngagementInvitationRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str


class GetEngagementRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str


class GetOpportunityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str


class MarketingOutputTypeDef(BaseValidatorModel):
    AwsFundingUsed: Optional[AwsFundingUsedType] = None
    CampaignName: Optional[str] = None
    Channels: Optional[List[ChannelType]] = None
    Source: Optional[MarketingSourceType] = None
    UseCases: Optional[List[str]] = None


class RelatedEntityIdentifiersTypeDef(BaseValidatorModel):
    AwsMarketplaceOffers: Optional[List[str]] = None
    AwsProducts: Optional[List[str]] = None
    Solutions: Optional[List[str]] = None


class GetResourceSnapshotJobRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class GetResourceSnapshotRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal["Opportunity"]
    Revision: Optional[int] = None


class GetSellingSystemSettingsRequestTypeDef(BaseValidatorModel):
    Catalog: str


class LifeCycleForViewTypeDef(BaseValidatorModel):
    NextSteps: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class NextStepsHistoryOutputTypeDef(BaseValidatorModel):
    Time: datetime
    Value: str


class LifeCycleSummaryTypeDef(BaseValidatorModel):
    ClosedLostReason: Optional[ClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    ReviewComments: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    ReviewStatusReason: Optional[str] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class ListEngagementByAcceptingInvitationTaskSummaryTypeDef(BaseValidatorModel):
    EngagementInvitationId: Optional[str] = None
    Message: Optional[str] = None
    OpportunityId: Optional[str] = None
    ReasonCode: Optional[ReasonCodeType] = None
    ResourceSnapshotJobId: Optional[str] = None
    StartTime: Optional[datetime] = None
    TaskArn: Optional[str] = None
    TaskId: Optional[str] = None
    TaskStatus: Optional[TaskStatusType] = None


class ListTasksSortBaseTypeDef(BaseValidatorModel):
    SortBy: Literal["StartTime"]
    SortOrder: SortOrderType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEngagementFromOpportunityTaskSummaryTypeDef(BaseValidatorModel):
    EngagementId: Optional[str] = None
    EngagementInvitationId: Optional[str] = None
    Message: Optional[str] = None
    OpportunityId: Optional[str] = None
    ReasonCode: Optional[ReasonCodeType] = None
    ResourceSnapshotJobId: Optional[str] = None
    StartTime: Optional[datetime] = None
    TaskArn: Optional[str] = None
    TaskId: Optional[str] = None
    TaskStatus: Optional[TaskStatusType] = None


class OpportunityEngagementInvitationSortTypeDef(BaseValidatorModel):
    SortBy: Literal["InvitationDate"]
    SortOrder: SortOrderType


class ListEngagementMembersRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEngagementResourceAssociationsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[str] = None
    EngagementIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[Literal["Opportunity"]] = None


class OpportunitySortTypeDef(BaseValidatorModel):
    SortBy: OpportunitySortNameType
    SortOrder: SortOrderType


class SortObjectTypeDef(BaseValidatorModel):
    SortBy: Optional[Literal["CreatedDate"]] = None
    SortOrder: Optional[SortOrderType] = None


class ResourceSnapshotJobSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    EngagementId: Optional[str] = None
    Id: Optional[str] = None
    Status: Optional[ResourceSnapshotJobStatusType] = None


class ListResourceSnapshotsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: str
    CreatedBy: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceSnapshotTemplateIdentifier: Optional[str] = None
    ResourceType: Optional[Literal["Opportunity"]] = None


class ResourceSnapshotSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedBy: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceSnapshotTemplateName: Optional[str] = None
    ResourceType: Optional[Literal["Opportunity"]] = None
    Revision: Optional[int] = None


class SolutionSortTypeDef(BaseValidatorModel):
    SortBy: SolutionSortNameType
    SortOrder: SortOrderType


class SolutionBaseTypeDef(BaseValidatorModel):
    Catalog: str
    Category: str
    CreatedDate: datetime
    Id: str
    Name: str
    Status: SolutionStatusType
    Arn: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class MarketingTypeDef(BaseValidatorModel):
    AwsFundingUsed: Optional[AwsFundingUsedType] = None
    CampaignName: Optional[str] = None
    Channels: Optional[Sequence[ChannelType]] = None
    Source: Optional[MarketingSourceType] = None
    UseCases: Optional[Sequence[str]] = None


class MonetaryValueTypeDef(BaseValidatorModel):
    Amount: str
    CurrencyCode: CurrencyCodeType


class SenderContactTypeDef(BaseValidatorModel):
    Email: str
    BusinessTitle: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None


class PutSellingSystemSettingsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobRoleIdentifier: Optional[str] = None


class RejectEngagementInvitationRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str
    RejectionReason: Optional[str] = None


class StartResourceSnapshotJobRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class StopResourceSnapshotJobRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class SubmitOpportunityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str
    InvolvementType: SalesInvolvementTypeType
    Visibility: Optional[VisibilityType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class ReceiverTypeDef(BaseValidatorModel):
    Account: Optional[AccountReceiverTypeDef] = None


class AccountSummaryTypeDef(BaseValidatorModel):
    CompanyName: str
    Address: Optional[AddressSummaryTypeDef] = None
    Industry: Optional[IndustryType] = None
    OtherIndustry: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class AccountTypeDef(BaseValidatorModel):
    CompanyName: str
    Address: Optional[AddressTypeDef] = None
    AwsAccountId: Optional[str] = None
    Duns: Optional[str] = None
    Industry: Optional[IndustryType] = None
    OtherIndustry: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class AssignOpportunityRequestTypeDef(BaseValidatorModel):
    Assignee: AssigneeContactTypeDef
    Catalog: str
    Identifier: str


class AwsOpportunityCustomerTypeDef(BaseValidatorModel):
    Contacts: Optional[List[ContactTypeDef]] = None


class AwsOpportunityLifeCycleTypeDef(BaseValidatorModel):
    ClosedLostReason: Optional[AwsClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    NextStepsHistory: Optional[List[ProfileNextStepsHistoryTypeDef]] = None
    Stage: Optional[AwsOpportunityStageType] = None
    TargetCloseDate: Optional[str] = None


class AwsOpportunityProjectTypeDef(BaseValidatorModel):
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpendTypeDef]] = None


class ProjectDetailsOutputTypeDef(BaseValidatorModel):
    BusinessProblem: str
    ExpectedCustomerSpend: List[ExpectedCustomerSpendTypeDef]
    TargetCompletionDate: str
    Title: str


class ProjectDetailsTypeDef(BaseValidatorModel):
    BusinessProblem: str
    ExpectedCustomerSpend: Sequence[ExpectedCustomerSpendTypeDef]
    TargetCompletionDate: str
    Title: str


class ProjectOutputTypeDef(BaseValidatorModel):
    AdditionalComments: Optional[str] = None
    ApnPrograms: Optional[List[str]] = None
    CompetitorName: Optional[CompetitorNameType] = None
    CustomerBusinessProblem: Optional[str] = None
    CustomerUseCase: Optional[str] = None
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpendTypeDef]] = None
    OtherCompetitorNames: Optional[str] = None
    OtherSolutionDescription: Optional[str] = None
    RelatedOpportunityIdentifier: Optional[str] = None
    SalesActivities: Optional[List[SalesActivityType]] = None
    Title: Optional[str] = None


class ProjectSummaryTypeDef(BaseValidatorModel):
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpendTypeDef]] = None


class ProjectTypeDef(BaseValidatorModel):
    AdditionalComments: Optional[str] = None
    ApnPrograms: Optional[Sequence[str]] = None
    CompetitorName: Optional[CompetitorNameType] = None
    CustomerBusinessProblem: Optional[str] = None
    CustomerUseCase: Optional[str] = None
    DeliveryModels: Optional[Sequence[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[Sequence[ExpectedCustomerSpendTypeDef]] = None
    OtherCompetitorNames: Optional[str] = None
    OtherSolutionDescription: Optional[str] = None
    RelatedOpportunityIdentifier: Optional[str] = None
    SalesActivities: Optional[Sequence[SalesActivityType]] = None
    Title: Optional[str] = None


class ProjectViewTypeDef(BaseValidatorModel):
    CustomerUseCase: Optional[str] = None
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpendTypeDef]] = None
    OtherSolutionDescription: Optional[str] = None
    SalesActivities: Optional[List[SalesActivityType]] = None


class CreateEngagementInvitationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEngagementResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOpportunityResponseTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedDate: datetime
    PartnerOpportunityIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceSnapshotJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceSnapshotResponseTypeDef(BaseValidatorModel):
    Arn: str
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceSnapshotJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    Catalog: str
    CreatedAt: datetime
    EngagementId: str
    Id: str
    LastFailure: str
    LastSuccessfulExecutionDate: datetime
    ResourceArn: str
    ResourceId: str
    ResourceSnapshotTemplateName: str
    ResourceType: Literal["Opportunity"]
    Status: ResourceSnapshotJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetSellingSystemSettingsResponseTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutSellingSystemSettingsResponseTypeDef(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartEngagementByAcceptingInvitationTaskResponseTypeDef(BaseValidatorModel):
    EngagementInvitationId: str
    Message: str
    OpportunityId: str
    ReasonCode: ReasonCodeType
    ResourceSnapshotJobId: str
    StartTime: datetime
    TaskArn: str
    TaskId: str
    TaskStatus: TaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartEngagementFromOpportunityTaskResponseTypeDef(BaseValidatorModel):
    EngagementId: str
    EngagementInvitationId: str
    Message: str
    OpportunityId: str
    ReasonCode: ReasonCodeType
    ResourceSnapshotJobId: str
    StartTime: datetime
    TaskArn: str
    TaskId: str
    TaskStatus: TaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateOpportunityResponseTypeDef(BaseValidatorModel):
    Id: str
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceSnapshotJobRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal["Opportunity"]
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartEngagementByAcceptingInvitationTaskRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    Identifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class StartEngagementFromOpportunityTaskRequestTypeDef(BaseValidatorModel):
    AwsSubmission: AwsSubmissionTypeDef
    Catalog: str
    ClientToken: str
    Identifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CustomerProjectsContextTypeDef(BaseValidatorModel):
    Customer: Optional[EngagementCustomerTypeDef] = None
    Project: Optional[EngagementCustomerProjectDetailsTypeDef] = None


class ListEngagementMembersResponseTypeDef(BaseValidatorModel):
    EngagementMemberList: List[EngagementMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEngagementResourceAssociationsResponseTypeDef(BaseValidatorModel):
    EngagementResourceAssociationSummaries: List[EngagementResourceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEngagementsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[Sequence[str]] = None
    EngagementIdentifier: Optional[Sequence[str]] = None
    ExcludeCreatedBy: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[EngagementSortTypeDef] = None


class ListEngagementsResponseTypeDef(BaseValidatorModel):
    EngagementSummaryList: List[EngagementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class LastModifiedDateTypeDef(BaseValidatorModel):
    AfterLastModifiedDate: Optional[TimestampTypeDef] = None
    BeforeLastModifiedDate: Optional[TimestampTypeDef] = None


class NextStepsHistoryTypeDef(BaseValidatorModel):
    Time: TimestampTypeDef
    Value: str


class LifeCycleOutputTypeDef(BaseValidatorModel):
    ClosedLostReason: Optional[ClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    NextStepsHistory: Optional[List[NextStepsHistoryOutputTypeDef]] = None
    ReviewComments: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    ReviewStatusReason: Optional[str] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class ListEngagementByAcceptingInvitationTasksResponseTypeDef(BaseValidatorModel):
    TaskSummaries: List[ListEngagementByAcceptingInvitationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEngagementByAcceptingInvitationTasksRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementInvitationIdentifier: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OpportunityIdentifier: Optional[Sequence[str]] = None
    Sort: Optional[ListTasksSortBaseTypeDef] = None
    TaskIdentifier: Optional[Sequence[str]] = None
    TaskStatus: Optional[Sequence[TaskStatusType]] = None


class ListEngagementFromOpportunityTasksRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OpportunityIdentifier: Optional[Sequence[str]] = None
    Sort: Optional[ListTasksSortBaseTypeDef] = None
    TaskIdentifier: Optional[Sequence[str]] = None
    TaskStatus: Optional[Sequence[TaskStatusType]] = None


class ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementInvitationIdentifier: Optional[Sequence[str]] = None
    OpportunityIdentifier: Optional[Sequence[str]] = None
    Sort: Optional[ListTasksSortBaseTypeDef] = None
    TaskIdentifier: Optional[Sequence[str]] = None
    TaskStatus: Optional[Sequence[TaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementFromOpportunityTasksRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[Sequence[str]] = None
    OpportunityIdentifier: Optional[Sequence[str]] = None
    Sort: Optional[ListTasksSortBaseTypeDef] = None
    TaskIdentifier: Optional[Sequence[str]] = None
    TaskStatus: Optional[Sequence[TaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementMembersRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementResourceAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[str] = None
    EngagementIdentifier: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[Literal["Opportunity"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[Sequence[str]] = None
    EngagementIdentifier: Optional[Sequence[str]] = None
    ExcludeCreatedBy: Optional[Sequence[str]] = None
    Sort: Optional[EngagementSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: str
    CreatedBy: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceSnapshotTemplateIdentifier: Optional[str] = None
    ResourceType: Optional[Literal["Opportunity"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementFromOpportunityTasksResponseTypeDef(BaseValidatorModel):
    TaskSummaries: List[ListEngagementFromOpportunityTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEngagementInvitationsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    ParticipantType: ParticipantTypeType
    EngagementIdentifier: Optional[Sequence[str]] = None
    PayloadType: Optional[Sequence[Literal["OpportunityInvitation"]]] = None
    SenderAwsAccountId: Optional[Sequence[str]] = None
    Sort: Optional[OpportunityEngagementInvitationSortTypeDef] = None
    Status: Optional[Sequence[InvitationStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementInvitationsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ParticipantType: ParticipantTypeType
    EngagementIdentifier: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PayloadType: Optional[Sequence[Literal["OpportunityInvitation"]]] = None
    SenderAwsAccountId: Optional[Sequence[str]] = None
    Sort: Optional[OpportunityEngagementInvitationSortTypeDef] = None
    Status: Optional[Sequence[InvitationStatusType]] = None


class ListResourceSnapshotJobsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[str] = None
    Sort: Optional[SortObjectTypeDef] = None
    Status: Optional[ResourceSnapshotJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceSnapshotJobsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SortObjectTypeDef] = None
    Status: Optional[ResourceSnapshotJobStatusType] = None


class ListResourceSnapshotJobsResponseTypeDef(BaseValidatorModel):
    ResourceSnapshotJobSummaries: List[ResourceSnapshotJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceSnapshotsResponseTypeDef(BaseValidatorModel):
    ResourceSnapshotSummaries: List[ResourceSnapshotSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSolutionsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    Category: Optional[Sequence[str]] = None
    Identifier: Optional[Sequence[str]] = None
    Sort: Optional[SolutionSortTypeDef] = None
    Status: Optional[Sequence[SolutionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolutionsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Category: Optional[Sequence[str]] = None
    Identifier: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SolutionSortTypeDef] = None
    Status: Optional[Sequence[SolutionStatusType]] = None


class ListSolutionsResponseTypeDef(BaseValidatorModel):
    SolutionSummaries: List[SolutionBaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SoftwareRevenueTypeDef(BaseValidatorModel):
    DeliveryModel: Optional[RevenueModelType] = None
    EffectiveDate: Optional[str] = None
    ExpirationDate: Optional[str] = None
    Value: Optional[MonetaryValueTypeDef] = None


class EngagementInvitationSummaryTypeDef(BaseValidatorModel):
    Catalog: str
    Id: str
    Arn: Optional[str] = None
    EngagementId: Optional[str] = None
    EngagementTitle: Optional[str] = None
    ExpirationDate: Optional[datetime] = None
    InvitationDate: Optional[datetime] = None
    ParticipantType: Optional[ParticipantTypeType] = None
    PayloadType: Optional[Literal["OpportunityInvitation"]] = None
    Receiver: Optional[ReceiverTypeDef] = None
    SenderAwsAccountId: Optional[str] = None
    SenderCompanyName: Optional[str] = None
    Status: Optional[InvitationStatusType] = None


class CustomerSummaryTypeDef(BaseValidatorModel):
    Account: Optional[AccountSummaryTypeDef] = None


class CustomerOutputTypeDef(BaseValidatorModel):
    Account: Optional[AccountTypeDef] = None
    Contacts: Optional[List[ContactTypeDef]] = None


class CustomerTypeDef(BaseValidatorModel):
    Account: Optional[AccountTypeDef] = None
    Contacts: Optional[Sequence[ContactTypeDef]] = None


class GetAwsOpportunitySummaryResponseTypeDef(BaseValidatorModel):
    Catalog: str
    Customer: AwsOpportunityCustomerTypeDef
    Insights: AwsOpportunityInsightsTypeDef
    InvolvementType: SalesInvolvementTypeType
    InvolvementTypeChangeReason: InvolvementTypeChangeReasonType
    LifeCycle: AwsOpportunityLifeCycleTypeDef
    OpportunityTeam: List[AwsTeamMemberTypeDef]
    Origin: OpportunityOriginType
    Project: AwsOpportunityProjectTypeDef
    RelatedEntityIds: AwsOpportunityRelatedEntitiesTypeDef
    RelatedOpportunityId: str
    Visibility: VisibilityType
    ResponseMetadata: ResponseMetadataTypeDef


class OpportunityInvitationPayloadOutputTypeDef(BaseValidatorModel):
    Customer: EngagementCustomerTypeDef
    Project: ProjectDetailsOutputTypeDef
    ReceiverResponsibilities: List[ReceiverResponsibilityType]
    SenderContacts: Optional[List[SenderContactTypeDef]] = None


class EngagementContextPayloadTypeDef(BaseValidatorModel):
    CustomerProject: Optional[CustomerProjectsContextTypeDef] = None


class ListOpportunitiesRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    CustomerCompanyName: Optional[Sequence[str]] = None
    Identifier: Optional[Sequence[str]] = None
    LastModifiedDate: Optional[LastModifiedDateTypeDef] = None
    LifeCycleReviewStatus: Optional[Sequence[ReviewStatusType]] = None
    LifeCycleStage: Optional[Sequence[StageType]] = None
    Sort: Optional[OpportunitySortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOpportunitiesRequestTypeDef(BaseValidatorModel):
    Catalog: str
    CustomerCompanyName: Optional[Sequence[str]] = None
    Identifier: Optional[Sequence[str]] = None
    LastModifiedDate: Optional[LastModifiedDateTypeDef] = None
    LifeCycleReviewStatus: Optional[Sequence[ReviewStatusType]] = None
    LifeCycleStage: Optional[Sequence[StageType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[OpportunitySortTypeDef] = None


class LifeCycleTypeDef(BaseValidatorModel):
    ClosedLostReason: Optional[ClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    NextStepsHistory: Optional[Sequence[NextStepsHistoryTypeDef]] = None
    ReviewComments: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    ReviewStatusReason: Optional[str] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class ListEngagementInvitationsResponseTypeDef(BaseValidatorModel):
    EngagementInvitationSummaries: List[EngagementInvitationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class OpportunitySummaryTypeDef(BaseValidatorModel):
    Catalog: str
    Arn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Customer: Optional[CustomerSummaryTypeDef] = None
    Id: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LifeCycle: Optional[LifeCycleSummaryTypeDef] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    PartnerOpportunityIdentifier: Optional[str] = None
    Project: Optional[ProjectSummaryTypeDef] = None


class GetOpportunityResponseTypeDef(BaseValidatorModel):
    Arn: str
    Catalog: str
    CreatedDate: datetime
    Customer: CustomerOutputTypeDef
    Id: str
    LastModifiedDate: datetime
    LifeCycle: LifeCycleOutputTypeDef
    Marketing: MarketingOutputTypeDef
    NationalSecurity: NationalSecurityType
    OpportunityTeam: List[ContactTypeDef]
    OpportunityType: OpportunityTypeType
    PartnerOpportunityIdentifier: str
    PrimaryNeedsFromAws: List[PrimaryNeedFromAwsType]
    Project: ProjectOutputTypeDef
    RelatedEntityIdentifiers: RelatedEntityIdentifiersTypeDef
    SoftwareRevenue: SoftwareRevenueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OpportunitySummaryViewTypeDef(BaseValidatorModel):
    Customer: Optional[CustomerOutputTypeDef] = None
    Lifecycle: Optional[LifeCycleForViewTypeDef] = None
    OpportunityTeam: Optional[List[ContactTypeDef]] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    PrimaryNeedsFromAws: Optional[List[PrimaryNeedFromAwsType]] = None
    Project: Optional[ProjectViewTypeDef] = None
    RelatedEntityIdentifiers: Optional[RelatedEntityIdentifiersTypeDef] = None


class PayloadOutputTypeDef(BaseValidatorModel):
    OpportunityInvitation: Optional[OpportunityInvitationPayloadOutputTypeDef] = None


class ProjectDetailsUnionTypeDef(BaseValidatorModel):
    pass


class OpportunityInvitationPayloadTypeDef(BaseValidatorModel):
    Customer: EngagementCustomerTypeDef
    Project: ProjectDetailsUnionTypeDef
    ReceiverResponsibilities: Sequence[ReceiverResponsibilityType]
    SenderContacts: Optional[Sequence[SenderContactTypeDef]] = None


class ListOpportunitiesResponseTypeDef(BaseValidatorModel):
    OpportunitySummaries: List[OpportunitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResourceSnapshotPayloadTypeDef(BaseValidatorModel):
    OpportunitySummary: Optional[OpportunitySummaryViewTypeDef] = None


class GetEngagementInvitationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Catalog: str
    EngagementDescription: str
    EngagementId: str
    EngagementTitle: str
    ExistingMembers: List[EngagementMemberSummaryTypeDef]
    ExpirationDate: datetime
    Id: str
    InvitationDate: datetime
    InvitationMessage: str
    Payload: PayloadOutputTypeDef
    PayloadType: Literal["OpportunityInvitation"]
    Receiver: ReceiverTypeDef
    RejectionReason: str
    SenderAwsAccountId: str
    SenderCompanyName: str
    Status: InvitationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EngagementContextDetailsTypeDef(BaseValidatorModel):
    pass


class CreateEngagementRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    Description: str
    Title: str
    Contexts: Optional[Sequence[EngagementContextDetailsTypeDef]] = None


class GetEngagementResponseTypeDef(BaseValidatorModel):
    Arn: str
    Contexts: List[EngagementContextDetailsTypeDef]
    CreatedAt: datetime
    CreatedBy: str
    Description: str
    Id: str
    MemberCount: int
    Title: str
    ResponseMetadata: ResponseMetadataTypeDef


class ProjectUnionTypeDef(BaseValidatorModel):
    pass


class CustomerUnionTypeDef(BaseValidatorModel):
    pass


class MarketingUnionTypeDef(BaseValidatorModel):
    pass


class LifeCycleUnionTypeDef(BaseValidatorModel):
    pass


class CreateOpportunityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    Customer: Optional[CustomerUnionTypeDef] = None
    LifeCycle: Optional[LifeCycleUnionTypeDef] = None
    Marketing: Optional[MarketingUnionTypeDef] = None
    NationalSecurity: Optional[NationalSecurityType] = None
    OpportunityTeam: Optional[Sequence[ContactTypeDef]] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    Origin: Optional[OpportunityOriginType] = None
    PartnerOpportunityIdentifier: Optional[str] = None
    PrimaryNeedsFromAws: Optional[Sequence[PrimaryNeedFromAwsType]] = None
    Project: Optional[ProjectUnionTypeDef] = None
    SoftwareRevenue: Optional[SoftwareRevenueTypeDef] = None


class UpdateOpportunityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    Identifier: str
    LastModifiedDate: TimestampTypeDef
    Customer: Optional[CustomerUnionTypeDef] = None
    LifeCycle: Optional[LifeCycleUnionTypeDef] = None
    Marketing: Optional[MarketingUnionTypeDef] = None
    NationalSecurity: Optional[NationalSecurityType] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    PartnerOpportunityIdentifier: Optional[str] = None
    PrimaryNeedsFromAws: Optional[Sequence[PrimaryNeedFromAwsType]] = None
    Project: Optional[ProjectUnionTypeDef] = None
    SoftwareRevenue: Optional[SoftwareRevenueTypeDef] = None


class GetResourceSnapshotResponseTypeDef(BaseValidatorModel):
    Arn: str
    Catalog: str
    CreatedAt: datetime
    CreatedBy: str
    EngagementId: str
    Payload: ResourceSnapshotPayloadTypeDef
    ResourceId: str
    ResourceSnapshotTemplateName: str
    ResourceType: Literal["Opportunity"]
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef


class OpportunityInvitationPayloadUnionTypeDef(BaseValidatorModel):
    pass


class PayloadTypeDef(BaseValidatorModel):
    OpportunityInvitation: Optional[OpportunityInvitationPayloadUnionTypeDef] = None


class PayloadUnionTypeDef(BaseValidatorModel):
    pass


class InvitationTypeDef(BaseValidatorModel):
    Message: str
    Payload: PayloadUnionTypeDef
    Receiver: ReceiverTypeDef


class CreateEngagementInvitationRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    Invitation: InvitationTypeDef


