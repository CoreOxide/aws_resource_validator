from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.detective.detective_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_invitation' function.
class AcceptInvitationRequest(BaseValidatorModel):
    GraphArn: str


class Account(BaseValidatorModel):
    AccountId: str
    EmailAddress: str


class Administrator(BaseValidatorModel):
    AccountId: Optional[str] = None
    GraphArn: Optional[str] = None
    DelegationTime: Optional[datetime] = None


# This class is the input for the 'batch_get_graph_member_datasources' function.
class BatchGetGraphMemberDatasourcesRequest(BaseValidatorModel):
    GraphArn: str
    AccountIds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedAccount(BaseValidatorModel):
    AccountId: Optional[str] = None
    Reason: Optional[str] = None


# This class is the input for the 'batch_get_membership_datasources' function.
class BatchGetMembershipDatasourcesRequest(BaseValidatorModel):
    GraphArns: List[str]


class UnprocessedGraph(BaseValidatorModel):
    GraphArn: Optional[str] = None
    Reason: Optional[str] = None


# This class is the input for the 'create_graph' function.
class CreateGraphRequest(BaseValidatorModel):
    Tags: Optional[Dict[str, str]] = None


class TimestampForCollection(BaseValidatorModel):
    Timestamp: Optional[datetime] = None


class DatasourcePackageUsageInfo(BaseValidatorModel):
    VolumeUsageInBytes: Optional[int] = None
    VolumeUsageUpdateTime: Optional[datetime] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'delete_graph' function.
class DeleteGraphRequest(BaseValidatorModel):
    GraphArn: str


# This class is the input for the 'delete_members' function.
class DeleteMembersRequest(BaseValidatorModel):
    GraphArn: str
    AccountIds: List[str]


# This class is the input for the 'describe_organization_configuration' function.
class DescribeOrganizationConfigurationRequest(BaseValidatorModel):
    GraphArn: str


# This class is the input for the 'disassociate_membership' function.
class DisassociateMembershipRequest(BaseValidatorModel):
    GraphArn: str


# This class is the input for the 'enable_organization_admin_account' function.
class EnableOrganizationAdminAccountRequest(BaseValidatorModel):
    AccountId: str


class StringFilter(BaseValidatorModel):
    Value: str


class FlaggedIpAddressDetail(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Reason: Optional[Literal['AWS_THREAT_INTELLIGENCE']] = None


# This class is the input for the 'get_investigation' function.
class GetInvestigationRequest(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str


# This class is the input for the 'get_members' function.
class GetMembersRequest(BaseValidatorModel):
    GraphArn: str
    AccountIds: List[str]


class Graph(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None


class ImpossibleTravelDetail(BaseValidatorModel):
    StartingIpAddress: Optional[str] = None
    EndingIpAddress: Optional[str] = None
    StartingLocation: Optional[str] = None
    EndingLocation: Optional[str] = None
    HourlyTimeDelta: Optional[int] = None


class NewAsoDetail(BaseValidatorModel):
    Aso: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None


class NewGeolocationDetail(BaseValidatorModel):
    Location: Optional[str] = None
    IpAddress: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None


class NewUserAgentDetail(BaseValidatorModel):
    UserAgent: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None


class RelatedFindingDetail(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    IpAddress: Optional[str] = None


class RelatedFindingGroupDetail(BaseValidatorModel):
    Id: Optional[str] = None


class TTPsObservedDetail(BaseValidatorModel):
    Tactic: Optional[str] = None
    Technique: Optional[str] = None
    Procedure: Optional[str] = None
    IpAddress: Optional[str] = None
    APIName: Optional[str] = None
    APISuccessCount: Optional[int] = None
    APIFailureCount: Optional[int] = None


class InvestigationDetail(BaseValidatorModel):
    InvestigationId: Optional[str] = None
    Severity: Optional[SeverityType] = None
    Status: Optional[StatusType] = None
    State: Optional[StateType] = None
    CreatedTime: Optional[datetime] = None
    EntityArn: Optional[str] = None
    EntityType: Optional[EntityTypeType] = None


# This class is the input for the 'list_datasource_packages' function.
class ListDatasourcePackagesRequest(BaseValidatorModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_graphs' function.
class ListGraphsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_indicators' function.
class ListIndicatorsRequest(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    IndicatorType: Optional[IndicatorTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SortCriteria(BaseValidatorModel):
    Field: Optional[FieldType] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_invitations' function.
class ListInvitationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_members' function.
class ListMembersRequest(BaseValidatorModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_organization_admin_accounts' function.
class ListOrganizationAdminAccountsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'reject_invitation' function.
class RejectInvitationRequest(BaseValidatorModel):
    GraphArn: str


# This class is the input for the 'start_monitoring_member' function.
class StartMonitoringMemberRequest(BaseValidatorModel):
    GraphArn: str
    AccountId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_datasource_packages' function.
class UpdateDatasourcePackagesRequest(BaseValidatorModel):
    GraphArn: str
    DatasourcePackages: List[DatasourcePackageType]


# This class is the input for the 'update_investigation_state' function.
class UpdateInvestigationStateRequest(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    State: StateType


# This class is the input for the 'update_organization_configuration' function.
class UpdateOrganizationConfigurationRequest(BaseValidatorModel):
    GraphArn: str
    AutoEnable: Optional[bool] = None


# This class is the input for the 'create_members' function.
class CreateMembersRequest(BaseValidatorModel):
    GraphArn: str
    Accounts: List[Account]
    Message: Optional[str] = None
    DisableEmailNotification: Optional[bool] = None


# This class is the output for the 'create_graph' function.
class CreateGraphResponse(BaseValidatorModel):
    GraphArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_organization_configuration' function.
class DescribeOrganizationConfigurationResponse(BaseValidatorModel):
    AutoEnable: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_organization_configuration' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_investigation' function.
class GetInvestigationResponse(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    EntityArn: str
    EntityType: EntityTypeType
    CreatedTime: datetime
    ScopeStartTime: datetime
    ScopeEndTime: datetime
    Status: StatusType
    Severity: SeverityType
    State: StateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_organization_admin_accounts' function.
class ListOrganizationAdminAccountsResponse(BaseValidatorModel):
    Administrators: List[Administrator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_investigation' function.
class StartInvestigationResponse(BaseValidatorModel):
    InvestigationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_members' function.
class DeleteMembersResponse(BaseValidatorModel):
    AccountIds: List[str]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


class DatasourcePackageIngestDetail(BaseValidatorModel):
    DatasourcePackageIngestState: Optional[DatasourcePackageIngestStateType] = None
    LastIngestStateChange: Optional[Dict[DatasourcePackageIngestStateType, TimestampForCollection]] = None


class MembershipDatasources(BaseValidatorModel):
    AccountId: Optional[str] = None
    GraphArn: Optional[str] = None
    DatasourcePackageIngestHistory: Optional[Dict[DatasourcePackageType, Dict[DatasourcePackageIngestStateType, TimestampForCollection]]] = None


class MemberDetail(BaseValidatorModel):
    AccountId: Optional[str] = None
    EmailAddress: Optional[str] = None
    GraphArn: Optional[str] = None
    MasterId: Optional[str] = None
    AdministratorId: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    DisabledReason: Optional[MemberDisabledReasonType] = None
    InvitedTime: Optional[datetime] = None
    UpdatedTime: Optional[datetime] = None
    VolumeUsageInBytes: Optional[int] = None
    VolumeUsageUpdatedTime: Optional[datetime] = None
    PercentOfGraphUtilization: Optional[float] = None
    PercentOfGraphUtilizationUpdatedTime: Optional[datetime] = None
    InvitationType: Optional[InvitationTypeType] = None
    VolumeUsageByDatasourcePackage: Optional[Dict[DatasourcePackageType, DatasourcePackageUsageInfo]] = None
    DatasourcePackageIngestStates: Optional[Dict[DatasourcePackageType, DatasourcePackageIngestStateType]] = None


class DateFilter(BaseValidatorModel):
    StartInclusive: Timestamp
    EndInclusive: Timestamp


# This class is the input for the 'start_investigation' function.
class StartInvestigationRequest(BaseValidatorModel):
    GraphArn: str
    EntityArn: str
    ScopeStartTime: Timestamp
    ScopeEndTime: Timestamp


# This class is the output for the 'list_graphs' function.
class ListGraphsResponse(BaseValidatorModel):
    GraphList: List[Graph]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IndicatorDetail(BaseValidatorModel):
    TTPsObservedDetail: Optional[TTPsObservedDetail] = None
    ImpossibleTravelDetail: Optional[ImpossibleTravelDetail] = None
    FlaggedIpAddressDetail: Optional[FlaggedIpAddressDetail] = None
    NewGeolocationDetail: Optional[NewGeolocationDetail] = None
    NewAsoDetail: Optional[NewAsoDetail] = None
    NewUserAgentDetail: Optional[NewUserAgentDetail] = None
    RelatedFindingDetail: Optional[RelatedFindingDetail] = None
    RelatedFindingGroupDetail: Optional[RelatedFindingGroupDetail] = None


# This class is the output for the 'list_investigations' function.
class ListInvestigationsResponse(BaseValidatorModel):
    InvestigationDetails: List[InvestigationDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_datasource_packages' function.
class ListDatasourcePackagesResponse(BaseValidatorModel):
    DatasourcePackages: Dict[DatasourcePackageType, DatasourcePackageIngestDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_get_graph_member_datasources' function.
class BatchGetGraphMemberDatasourcesResponse(BaseValidatorModel):
    MemberDatasources: List[MembershipDatasources]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_membership_datasources' function.
class BatchGetMembershipDatasourcesResponse(BaseValidatorModel):
    MembershipDatasources: List[MembershipDatasources]
    UnprocessedGraphs: List[UnprocessedGraph]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_members' function.
class CreateMembersResponse(BaseValidatorModel):
    Members: List[MemberDetail]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_members' function.
class GetMembersResponse(BaseValidatorModel):
    MemberDetails: List[MemberDetail]
    UnprocessedAccounts: List[UnprocessedAccount]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_invitations' function.
class ListInvitationsResponse(BaseValidatorModel):
    Invitations: List[MemberDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_members' function.
class ListMembersResponse(BaseValidatorModel):
    MemberDetails: List[MemberDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FilterCriteria(BaseValidatorModel):
    Severity: Optional[StringFilter] = None
    Status: Optional[StringFilter] = None
    State: Optional[StringFilter] = None
    EntityArn: Optional[StringFilter] = None
    CreatedTime: Optional[DateFilter] = None


class Indicator(BaseValidatorModel):
    IndicatorType: Optional[IndicatorTypeType] = None
    IndicatorDetail: Optional[IndicatorDetail] = None


# This class is the input for the 'list_investigations' function.
class ListInvestigationsRequest(BaseValidatorModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[FilterCriteria] = None
    SortCriteria: Optional[SortCriteria] = None


# This class is the output for the 'list_indicators' function.
class ListIndicatorsResponse(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    Indicators: List[Indicator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None