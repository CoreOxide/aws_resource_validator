from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptEngagementInvitationRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str


class AccountReceiver(BaseValidatorModel):
    AwsAccountId: str
    Alias: Optional[str] = None


class AddressSummary(BaseValidatorModel):
    City: Optional[str] = None
    CountryCode: Optional[CountryCodeType] = None
    PostalCode: Optional[str] = None
    StateOrRegion: Optional[str] = None


class Address(BaseValidatorModel):
    City: Optional[str] = None
    CountryCode: Optional[CountryCodeType] = None
    PostalCode: Optional[str] = None
    StateOrRegion: Optional[str] = None
    StreetAddress: Optional[str] = None


class AssigneeContact(BaseValidatorModel):
    BusinessTitle: str
    Email: str
    FirstName: str
    LastName: str


class AssociateOpportunityRequest(BaseValidatorModel):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType


class Contact(BaseValidatorModel):
    BusinessTitle: Optional[str] = None
    Email: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None


class AwsOpportunityInsights(BaseValidatorModel):
    EngagementScore: Optional[EngagementScoreType] = None
    NextBestActions: Optional[str] = None


class ProfileNextStepsHistory(BaseValidatorModel):
    Time: datetime
    Value: str


class ExpectedCustomerSpend(BaseValidatorModel):
    Amount: str
    CurrencyCode: ExpectedCustomerSpendCurrencyCodeEnumType
    Frequency: Literal['Monthly']
    TargetCompany: str
    EstimationUrl: Optional[str] = None


class AwsOpportunityRelatedEntities(BaseValidatorModel):
    AwsProducts: Optional[List[str]] = None
    Solutions: Optional[List[str]] = None


class AwsSubmission(BaseValidatorModel):
    InvolvementType: SalesInvolvementTypeType
    Visibility: Optional[VisibilityType] = None


class AwsTeamMember(BaseValidatorModel):
    BusinessTitle: Optional[AwsMemberBusinessTitleType] = None
    Email: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateResourceSnapshotRequest(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal['Opportunity']


class EngagementCustomerProjectDetails(BaseValidatorModel):
    BusinessProblem: str
    TargetCompletionDate: str
    Title: str


class EngagementCustomer(BaseValidatorModel):
    CompanyName: str
    CountryCode: CountryCodeType
    Industry: IndustryType
    WebsiteUrl: str


class DeleteResourceSnapshotJobRequest(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class DisassociateOpportunityRequest(BaseValidatorModel):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType


class EngagementMemberSummary(BaseValidatorModel):
    CompanyName: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class EngagementMember(BaseValidatorModel):
    AccountId: Optional[str] = None
    CompanyName: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class EngagementResourceAssociationSummary(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[str] = None
    EngagementId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal['Opportunity']] = None


class EngagementSort(BaseValidatorModel):
    SortBy: Literal['CreatedDate']
    SortOrder: SortOrderType


class EngagementSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    Id: Optional[str] = None
    MemberCount: Optional[int] = None
    Title: Optional[str] = None


class GetAwsOpportunitySummaryRequest(BaseValidatorModel):
    Catalog: str
    RelatedOpportunityIdentifier: str


class GetEngagementInvitationRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str


class GetEngagementRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str


class GetOpportunityRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str


class MarketingOutput(BaseValidatorModel):
    AwsFundingUsed: Optional[AwsFundingUsedType] = None
    CampaignName: Optional[str] = None
    Channels: Optional[List[ChannelType]] = None
    Source: Optional[MarketingSourceType] = None
    UseCases: Optional[List[str]] = None


class RelatedEntityIdentifiers(BaseValidatorModel):
    AwsMarketplaceOffers: Optional[List[str]] = None
    AwsProducts: Optional[List[str]] = None
    Solutions: Optional[List[str]] = None


class GetResourceSnapshotJobRequest(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class GetResourceSnapshotRequest(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal['Opportunity']
    Revision: Optional[int] = None


class GetSellingSystemSettingsRequest(BaseValidatorModel):
    Catalog: str

Timestamp = Union[datetime, str]


class LifeCycleForView(BaseValidatorModel):
    NextSteps: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class NextStepsHistoryOutput(BaseValidatorModel):
    Time: datetime
    Value: str


class LifeCycleSummary(BaseValidatorModel):
    ClosedLostReason: Optional[ClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    ReviewComments: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    ReviewStatusReason: Optional[str] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class ListEngagementByAcceptingInvitationTaskSummary(BaseValidatorModel):
    EngagementInvitationId: Optional[str] = None
    Message: Optional[str] = None
    OpportunityId: Optional[str] = None
    ReasonCode: Optional[ReasonCodeType] = None
    ResourceSnapshotJobId: Optional[str] = None
    StartTime: Optional[datetime] = None
    TaskArn: Optional[str] = None
    TaskId: Optional[str] = None
    TaskStatus: Optional[TaskStatusType] = None


class ListTasksSortBase(BaseValidatorModel):
    SortBy: Literal['StartTime']
    SortOrder: SortOrderType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEngagementFromOpportunityTaskSummary(BaseValidatorModel):
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


class OpportunityEngagementInvitationSort(BaseValidatorModel):
    SortBy: Literal['InvitationDate']
    SortOrder: SortOrderType


class ListEngagementMembersRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEngagementResourceAssociationsRequest(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[str] = None
    EngagementIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[Literal['Opportunity']] = None


class OpportunitySort(BaseValidatorModel):
    SortBy: OpportunitySortNameType
    SortOrder: SortOrderType


class SortObject(BaseValidatorModel):
    SortBy: Optional[Literal['CreatedDate']] = None
    SortOrder: Optional[SortOrderType] = None


class ResourceSnapshotJobSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    EngagementId: Optional[str] = None
    Id: Optional[str] = None
    Status: Optional[ResourceSnapshotJobStatusType] = None


class ListResourceSnapshotsRequest(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: str
    CreatedBy: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceSnapshotTemplateIdentifier: Optional[str] = None
    ResourceType: Optional[Literal['Opportunity']] = None


class ResourceSnapshotSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedBy: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceSnapshotTemplateName: Optional[str] = None
    ResourceType: Optional[Literal['Opportunity']] = None
    Revision: Optional[int] = None


class SolutionSort(BaseValidatorModel):
    SortBy: SolutionSortNameType
    SortOrder: SortOrderType


class SolutionBase(BaseValidatorModel):
    Catalog: str
    Category: str
    CreatedDate: datetime
    Id: str
    Name: str
    Status: SolutionStatusType
    Arn: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class Marketing(BaseValidatorModel):
    AwsFundingUsed: Optional[AwsFundingUsedType] = None
    CampaignName: Optional[str] = None
    Channels: Optional[List[ChannelType]] = None
    Source: Optional[MarketingSourceType] = None
    UseCases: Optional[List[str]] = None


class MonetaryValue(BaseValidatorModel):
    Amount: str
    CurrencyCode: CurrencyCodeType


class SenderContact(BaseValidatorModel):
    Email: str
    BusinessTitle: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Phone: Optional[str] = None


class PutSellingSystemSettingsRequest(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobRoleIdentifier: Optional[str] = None


class RejectEngagementInvitationRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str
    RejectionReason: Optional[str] = None


class StartResourceSnapshotJobRequest(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class StopResourceSnapshotJobRequest(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobIdentifier: str


class SubmitOpportunityRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str
    InvolvementType: SalesInvolvementTypeType
    Visibility: Optional[VisibilityType] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class Receiver(BaseValidatorModel):
    Account: Optional[AccountReceiver] = None


class AccountSummary(BaseValidatorModel):
    CompanyName: str
    Address: Optional[AddressSummary] = None
    Industry: Optional[IndustryType] = None
    OtherIndustry: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class Account(BaseValidatorModel):
    CompanyName: str
    Address: Optional[Address] = None
    AwsAccountId: Optional[str] = None
    Duns: Optional[str] = None
    Industry: Optional[IndustryType] = None
    OtherIndustry: Optional[str] = None
    WebsiteUrl: Optional[str] = None


class AssignOpportunityRequest(BaseValidatorModel):
    Assignee: AssigneeContact
    Catalog: str
    Identifier: str


class AwsOpportunityCustomer(BaseValidatorModel):
    Contacts: Optional[List[Contact]] = None


class AwsOpportunityLifeCycle(BaseValidatorModel):
    ClosedLostReason: Optional[AwsClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    NextStepsHistory: Optional[List[ProfileNextStepsHistory]] = None
    Stage: Optional[AwsOpportunityStageType] = None
    TargetCloseDate: Optional[str] = None


class AwsOpportunityProject(BaseValidatorModel):
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpend]] = None


class ProjectDetailsOutput(BaseValidatorModel):
    BusinessProblem: str
    ExpectedCustomerSpend: List[ExpectedCustomerSpend]
    TargetCompletionDate: str
    Title: str


class ProjectDetails(BaseValidatorModel):
    BusinessProblem: str
    ExpectedCustomerSpend: List[ExpectedCustomerSpend]
    TargetCompletionDate: str
    Title: str


class ProjectOutput(BaseValidatorModel):
    AdditionalComments: Optional[str] = None
    ApnPrograms: Optional[List[str]] = None
    CompetitorName: Optional[CompetitorNameType] = None
    CustomerBusinessProblem: Optional[str] = None
    CustomerUseCase: Optional[str] = None
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpend]] = None
    OtherCompetitorNames: Optional[str] = None
    OtherSolutionDescription: Optional[str] = None
    RelatedOpportunityIdentifier: Optional[str] = None
    SalesActivities: Optional[List[SalesActivityType]] = None
    Title: Optional[str] = None


class ProjectSummary(BaseValidatorModel):
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpend]] = None


class Project(BaseValidatorModel):
    AdditionalComments: Optional[str] = None
    ApnPrograms: Optional[List[str]] = None
    CompetitorName: Optional[CompetitorNameType] = None
    CustomerBusinessProblem: Optional[str] = None
    CustomerUseCase: Optional[str] = None
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpend]] = None
    OtherCompetitorNames: Optional[str] = None
    OtherSolutionDescription: Optional[str] = None
    RelatedOpportunityIdentifier: Optional[str] = None
    SalesActivities: Optional[List[SalesActivityType]] = None
    Title: Optional[str] = None


class ProjectView(BaseValidatorModel):
    CustomerUseCase: Optional[str] = None
    DeliveryModels: Optional[List[DeliveryModelType]] = None
    ExpectedCustomerSpend: Optional[List[ExpectedCustomerSpend]] = None
    OtherSolutionDescription: Optional[str] = None
    SalesActivities: Optional[List[SalesActivityType]] = None


class CreateEngagementInvitationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateEngagementResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateOpportunityResponse(BaseValidatorModel):
    Id: str
    LastModifiedDate: datetime
    PartnerOpportunityIdentifier: str
    ResponseMetadata: ResponseMetadata


class CreateResourceSnapshotJobResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateResourceSnapshotResponse(BaseValidatorModel):
    Arn: str
    Revision: int
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetResourceSnapshotJobResponse(BaseValidatorModel):
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
    ResourceType: Literal['Opportunity']
    Status: ResourceSnapshotJobStatusType
    ResponseMetadata: ResponseMetadata


class GetSellingSystemSettingsResponse(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobRoleArn: str
    ResponseMetadata: ResponseMetadata


class PutSellingSystemSettingsResponse(BaseValidatorModel):
    Catalog: str
    ResourceSnapshotJobRoleArn: str
    ResponseMetadata: ResponseMetadata


class StartEngagementByAcceptingInvitationTaskResponse(BaseValidatorModel):
    EngagementInvitationId: str
    Message: str
    OpportunityId: str
    ReasonCode: ReasonCodeType
    ResourceSnapshotJobId: str
    StartTime: datetime
    TaskArn: str
    TaskId: str
    TaskStatus: TaskStatusType
    ResponseMetadata: ResponseMetadata


class StartEngagementFromOpportunityTaskResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class UpdateOpportunityResponse(BaseValidatorModel):
    Id: str
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


class CreateResourceSnapshotJobRequest(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal['Opportunity']
    Tags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartEngagementByAcceptingInvitationTaskRequest(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    Identifier: str
    Tags: Optional[List[Tag]] = None


class StartEngagementFromOpportunityTaskRequest(BaseValidatorModel):
    AwsSubmission: AwsSubmission
    Catalog: str
    ClientToken: str
    Identifier: str
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CustomerProjectsContext(BaseValidatorModel):
    Customer: Optional[EngagementCustomer] = None
    Project: Optional[EngagementCustomerProjectDetails] = None


class ListEngagementMembersResponse(BaseValidatorModel):
    EngagementMemberList: List[EngagementMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEngagementResourceAssociationsResponse(BaseValidatorModel):
    EngagementResourceAssociationSummaries: List[EngagementResourceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEngagementsRequest(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[List[str]] = None
    EngagementIdentifier: Optional[List[str]] = None
    ExcludeCreatedBy: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[EngagementSort] = None


class ListEngagementsResponse(BaseValidatorModel):
    EngagementSummaryList: List[EngagementSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LastModifiedDate(BaseValidatorModel):
    AfterLastModifiedDate: Optional[Timestamp] = None
    BeforeLastModifiedDate: Optional[Timestamp] = None


class NextStepsHistory(BaseValidatorModel):
    Time: Timestamp
    Value: str


class LifeCycleOutput(BaseValidatorModel):
    ClosedLostReason: Optional[ClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    NextStepsHistory: Optional[List[NextStepsHistoryOutput]] = None
    ReviewComments: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    ReviewStatusReason: Optional[str] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class ListEngagementByAcceptingInvitationTasksResponse(BaseValidatorModel):
    TaskSummaries: List[ListEngagementByAcceptingInvitationTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEngagementByAcceptingInvitationTasksRequest(BaseValidatorModel):
    Catalog: str
    EngagementInvitationIdentifier: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OpportunityIdentifier: Optional[List[str]] = None
    Sort: Optional[ListTasksSortBase] = None
    TaskIdentifier: Optional[List[str]] = None
    TaskStatus: Optional[List[TaskStatusType]] = None


class ListEngagementFromOpportunityTasksRequest(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OpportunityIdentifier: Optional[List[str]] = None
    Sort: Optional[ListTasksSortBase] = None
    TaskIdentifier: Optional[List[str]] = None
    TaskStatus: Optional[List[TaskStatusType]] = None


class ListEngagementByAcceptingInvitationTasksRequestPaginate(BaseValidatorModel):
    Catalog: str
    EngagementInvitationIdentifier: Optional[List[str]] = None
    OpportunityIdentifier: Optional[List[str]] = None
    Sort: Optional[ListTasksSortBase] = None
    TaskIdentifier: Optional[List[str]] = None
    TaskStatus: Optional[List[TaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementFromOpportunityTasksRequestPaginate(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[List[str]] = None
    OpportunityIdentifier: Optional[List[str]] = None
    Sort: Optional[ListTasksSortBase] = None
    TaskIdentifier: Optional[List[str]] = None
    TaskStatus: Optional[List[TaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementMembersRequestPaginate(BaseValidatorModel):
    Catalog: str
    Identifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementResourceAssociationsRequestPaginate(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[str] = None
    EngagementIdentifier: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[Literal['Opportunity']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementsRequestPaginate(BaseValidatorModel):
    Catalog: str
    CreatedBy: Optional[List[str]] = None
    EngagementIdentifier: Optional[List[str]] = None
    ExcludeCreatedBy: Optional[List[str]] = None
    Sort: Optional[EngagementSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceSnapshotsRequestPaginate(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: str
    CreatedBy: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceSnapshotTemplateIdentifier: Optional[str] = None
    ResourceType: Optional[Literal['Opportunity']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementFromOpportunityTasksResponse(BaseValidatorModel):
    TaskSummaries: List[ListEngagementFromOpportunityTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEngagementInvitationsRequestPaginate(BaseValidatorModel):
    Catalog: str
    ParticipantType: ParticipantTypeType
    EngagementIdentifier: Optional[List[str]] = None
    PayloadType: Optional[List[Literal['OpportunityInvitation']]] = None
    SenderAwsAccountId: Optional[List[str]] = None
    Sort: Optional[OpportunityEngagementInvitationSort] = None
    Status: Optional[List[InvitationStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementInvitationsRequest(BaseValidatorModel):
    Catalog: str
    ParticipantType: ParticipantTypeType
    EngagementIdentifier: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PayloadType: Optional[List[Literal['OpportunityInvitation']]] = None
    SenderAwsAccountId: Optional[List[str]] = None
    Sort: Optional[OpportunityEngagementInvitationSort] = None
    Status: Optional[List[InvitationStatusType]] = None


class ListResourceSnapshotJobsRequestPaginate(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[str] = None
    Sort: Optional[SortObject] = None
    Status: Optional[ResourceSnapshotJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceSnapshotJobsRequest(BaseValidatorModel):
    Catalog: str
    EngagementIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SortObject] = None
    Status: Optional[ResourceSnapshotJobStatusType] = None


class ListResourceSnapshotJobsResponse(BaseValidatorModel):
    ResourceSnapshotJobSummaries: List[ResourceSnapshotJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceSnapshotsResponse(BaseValidatorModel):
    ResourceSnapshotSummaries: List[ResourceSnapshotSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSolutionsRequestPaginate(BaseValidatorModel):
    Catalog: str
    Category: Optional[List[str]] = None
    Identifier: Optional[List[str]] = None
    Sort: Optional[SolutionSort] = None
    Status: Optional[List[SolutionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolutionsRequest(BaseValidatorModel):
    Catalog: str
    Category: Optional[List[str]] = None
    Identifier: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SolutionSort] = None
    Status: Optional[List[SolutionStatusType]] = None


class ListSolutionsResponse(BaseValidatorModel):
    SolutionSummaries: List[SolutionBase]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MarketingUnion = Union[Marketing, MarketingOutput]


class SoftwareRevenue(BaseValidatorModel):
    DeliveryModel: Optional[RevenueModelType] = None
    EffectiveDate: Optional[str] = None
    ExpirationDate: Optional[str] = None
    Value: Optional[MonetaryValue] = None


class EngagementInvitationSummary(BaseValidatorModel):
    Catalog: str
    Id: str
    Arn: Optional[str] = None
    EngagementId: Optional[str] = None
    EngagementTitle: Optional[str] = None
    ExpirationDate: Optional[datetime] = None
    InvitationDate: Optional[datetime] = None
    ParticipantType: Optional[ParticipantTypeType] = None
    PayloadType: Optional[Literal['OpportunityInvitation']] = None
    Receiver: Optional[Receiver] = None
    SenderAwsAccountId: Optional[str] = None
    SenderCompanyName: Optional[str] = None
    Status: Optional[InvitationStatusType] = None


class CustomerSummary(BaseValidatorModel):
    Account: Optional[AccountSummary] = None


class CustomerOutput(BaseValidatorModel):
    Account: Optional[Account] = None
    Contacts: Optional[List[Contact]] = None


class Customer(BaseValidatorModel):
    Account: Optional[Account] = None
    Contacts: Optional[List[Contact]] = None


class GetAwsOpportunitySummaryResponse(BaseValidatorModel):
    Catalog: str
    Customer: AwsOpportunityCustomer
    Insights: AwsOpportunityInsights
    InvolvementType: SalesInvolvementTypeType
    InvolvementTypeChangeReason: InvolvementTypeChangeReasonType
    LifeCycle: AwsOpportunityLifeCycle
    OpportunityTeam: List[AwsTeamMember]
    Origin: OpportunityOriginType
    Project: AwsOpportunityProject
    RelatedEntityIds: AwsOpportunityRelatedEntities
    RelatedOpportunityId: str
    Visibility: VisibilityType
    ResponseMetadata: ResponseMetadata


class OpportunityInvitationPayloadOutput(BaseValidatorModel):
    Customer: EngagementCustomer
    Project: ProjectDetailsOutput
    ReceiverResponsibilities: List[ReceiverResponsibilityType]
    SenderContacts: Optional[List[SenderContact]] = None

ProjectDetailsUnion = Union[ProjectDetails, ProjectDetailsOutput]

ProjectUnion = Union[Project, ProjectOutput]


class EngagementContextPayload(BaseValidatorModel):
    CustomerProject: Optional[CustomerProjectsContext] = None


class ListOpportunitiesRequestPaginate(BaseValidatorModel):
    Catalog: str
    CustomerCompanyName: Optional[List[str]] = None
    Identifier: Optional[List[str]] = None
    LastModifiedDate: Optional[LastModifiedDate] = None
    LifeCycleReviewStatus: Optional[List[ReviewStatusType]] = None
    LifeCycleStage: Optional[List[StageType]] = None
    Sort: Optional[OpportunitySort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOpportunitiesRequest(BaseValidatorModel):
    Catalog: str
    CustomerCompanyName: Optional[List[str]] = None
    Identifier: Optional[List[str]] = None
    LastModifiedDate: Optional[LastModifiedDate] = None
    LifeCycleReviewStatus: Optional[List[ReviewStatusType]] = None
    LifeCycleStage: Optional[List[StageType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[OpportunitySort] = None


class LifeCycle(BaseValidatorModel):
    ClosedLostReason: Optional[ClosedLostReasonType] = None
    NextSteps: Optional[str] = None
    NextStepsHistory: Optional[List[NextStepsHistory]] = None
    ReviewComments: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    ReviewStatusReason: Optional[str] = None
    Stage: Optional[StageType] = None
    TargetCloseDate: Optional[str] = None


class ListEngagementInvitationsResponse(BaseValidatorModel):
    EngagementInvitationSummaries: List[EngagementInvitationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OpportunitySummary(BaseValidatorModel):
    Catalog: str
    Arn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Customer: Optional[CustomerSummary] = None
    Id: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LifeCycle: Optional[LifeCycleSummary] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    PartnerOpportunityIdentifier: Optional[str] = None
    Project: Optional[ProjectSummary] = None


class GetOpportunityResponse(BaseValidatorModel):
    Arn: str
    Catalog: str
    CreatedDate: datetime
    Customer: CustomerOutput
    Id: str
    LastModifiedDate: datetime
    LifeCycle: LifeCycleOutput
    Marketing: MarketingOutput
    NationalSecurity: NationalSecurityType
    OpportunityTeam: List[Contact]
    OpportunityType: OpportunityTypeType
    PartnerOpportunityIdentifier: str
    PrimaryNeedsFromAws: List[PrimaryNeedFromAwsType]
    Project: ProjectOutput
    RelatedEntityIdentifiers: RelatedEntityIdentifiers
    SoftwareRevenue: SoftwareRevenue
    ResponseMetadata: ResponseMetadata


class OpportunitySummaryView(BaseValidatorModel):
    Customer: Optional[CustomerOutput] = None
    Lifecycle: Optional[LifeCycleForView] = None
    OpportunityTeam: Optional[List[Contact]] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    PrimaryNeedsFromAws: Optional[List[PrimaryNeedFromAwsType]] = None
    Project: Optional[ProjectView] = None
    RelatedEntityIdentifiers: Optional[RelatedEntityIdentifiers] = None

CustomerUnion = Union[Customer, CustomerOutput]


class PayloadOutput(BaseValidatorModel):
    OpportunityInvitation: Optional[OpportunityInvitationPayloadOutput] = None


class OpportunityInvitationPayload(BaseValidatorModel):
    Customer: EngagementCustomer
    Project: ProjectDetailsUnion
    ReceiverResponsibilities: List[ReceiverResponsibilityType]
    SenderContacts: Optional[List[SenderContact]] = None


class EngagementContextDetails(BaseValidatorModel):
    Type: Literal['CustomerProject']
    Payload: Optional[EngagementContextPayload] = None

LifeCycleUnion = Union[LifeCycle, LifeCycleOutput]


class ListOpportunitiesResponse(BaseValidatorModel):
    OpportunitySummaries: List[OpportunitySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResourceSnapshotPayload(BaseValidatorModel):
    OpportunitySummary: Optional[OpportunitySummaryView] = None


class GetEngagementInvitationResponse(BaseValidatorModel):
    Arn: str
    Catalog: str
    EngagementDescription: str
    EngagementId: str
    EngagementTitle: str
    ExistingMembers: List[EngagementMemberSummary]
    ExpirationDate: datetime
    Id: str
    InvitationDate: datetime
    InvitationMessage: str
    Payload: PayloadOutput
    PayloadType: Literal['OpportunityInvitation']
    Receiver: Receiver
    RejectionReason: str
    SenderAwsAccountId: str
    SenderCompanyName: str
    Status: InvitationStatusType
    ResponseMetadata: ResponseMetadata

OpportunityInvitationPayloadUnion = Union[OpportunityInvitationPayload, OpportunityInvitationPayloadOutput]


class CreateEngagementRequest(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    Description: str
    Title: str
    Contexts: Optional[List[EngagementContextDetails]] = None


class GetEngagementResponse(BaseValidatorModel):
    Arn: str
    Contexts: List[EngagementContextDetails]
    CreatedAt: datetime
    CreatedBy: str
    Description: str
    Id: str
    MemberCount: int
    Title: str
    ResponseMetadata: ResponseMetadata


class CreateOpportunityRequest(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    Customer: Optional[CustomerUnion] = None
    LifeCycle: Optional[LifeCycleUnion] = None
    Marketing: Optional[MarketingUnion] = None
    NationalSecurity: Optional[NationalSecurityType] = None
    OpportunityTeam: Optional[List[Contact]] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    Origin: Optional[OpportunityOriginType] = None
    PartnerOpportunityIdentifier: Optional[str] = None
    PrimaryNeedsFromAws: Optional[List[PrimaryNeedFromAwsType]] = None
    Project: Optional[ProjectUnion] = None
    SoftwareRevenue: Optional[SoftwareRevenue] = None


class UpdateOpportunityRequest(BaseValidatorModel):
    Catalog: str
    Identifier: str
    LastModifiedDate: Timestamp
    Customer: Optional[CustomerUnion] = None
    LifeCycle: Optional[LifeCycleUnion] = None
    Marketing: Optional[MarketingUnion] = None
    NationalSecurity: Optional[NationalSecurityType] = None
    OpportunityType: Optional[OpportunityTypeType] = None
    PartnerOpportunityIdentifier: Optional[str] = None
    PrimaryNeedsFromAws: Optional[List[PrimaryNeedFromAwsType]] = None
    Project: Optional[ProjectUnion] = None
    SoftwareRevenue: Optional[SoftwareRevenue] = None


class GetResourceSnapshotResponse(BaseValidatorModel):
    Arn: str
    Catalog: str
    CreatedAt: datetime
    CreatedBy: str
    EngagementId: str
    Payload: ResourceSnapshotPayload
    ResourceId: str
    ResourceSnapshotTemplateName: str
    ResourceType: Literal['Opportunity']
    Revision: int
    ResponseMetadata: ResponseMetadata


class Payload(BaseValidatorModel):
    OpportunityInvitation: Optional[OpportunityInvitationPayloadUnion] = None

PayloadUnion = Union[Payload, PayloadOutput]


class Invitation(BaseValidatorModel):
    Message: str
    Payload: PayloadUnion
    Receiver: Receiver


class CreateEngagementInvitationRequest(BaseValidatorModel):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    Invitation: Invitation