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
from aws_resource_validator.pydantic_models.detective_constants import *

class AcceptInvitationRequestRequestTypeDef(BaseModel):
    GraphArn: str

class AccountTypeDef(BaseModel):
    AccountId: str
    EmailAddress: str

class AdministratorTypeDef(BaseModel):
    AccountId: Optional[str] = None
    GraphArn: Optional[str] = None
    DelegationTime: Optional[datetime] = None

class BatchGetGraphMemberDatasourcesRequestRequestTypeDef(BaseModel):
    GraphArn: str
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class UnprocessedAccountTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Reason: Optional[str] = None

class BatchGetMembershipDatasourcesRequestRequestTypeDef(BaseModel):
    GraphArns: Sequence[str]

class UnprocessedGraphTypeDef(BaseModel):
    GraphArn: Optional[str] = None
    Reason: Optional[str] = None

class CreateGraphRequestRequestTypeDef(BaseModel):
    Tags: Optional[Mapping[str, str]] = None

class TimestampForCollectionTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None

class DatasourcePackageUsageInfoTypeDef(BaseModel):
    VolumeUsageInBytes: Optional[int] = None
    VolumeUsageUpdateTime: Optional[datetime] = None

class DeleteGraphRequestRequestTypeDef(BaseModel):
    GraphArn: str

class DeleteMembersRequestRequestTypeDef(BaseModel):
    GraphArn: str
    AccountIds: Sequence[str]

class DescribeOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    GraphArn: str

class DisassociateMembershipRequestRequestTypeDef(BaseModel):
    GraphArn: str

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    AccountId: str

class StringFilterTypeDef(BaseModel):
    Value: str

class FlaggedIpAddressDetailTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    Reason: Optional[Literal["AWS_THREAT_INTELLIGENCE"]] = None

class GetInvestigationRequestRequestTypeDef(BaseModel):
    GraphArn: str
    InvestigationId: str

class GetMembersRequestRequestTypeDef(BaseModel):
    GraphArn: str
    AccountIds: Sequence[str]

class GraphTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class ImpossibleTravelDetailTypeDef(BaseModel):
    StartingIpAddress: Optional[str] = None
    EndingIpAddress: Optional[str] = None
    StartingLocation: Optional[str] = None
    EndingLocation: Optional[str] = None
    HourlyTimeDelta: Optional[int] = None

class NewAsoDetailTypeDef(BaseModel):
    Aso: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None

class NewGeolocationDetailTypeDef(BaseModel):
    Location: Optional[str] = None
    IpAddress: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None

class NewUserAgentDetailTypeDef(BaseModel):
    UserAgent: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None

class RelatedFindingDetailTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    IpAddress: Optional[str] = None

class RelatedFindingGroupDetailTypeDef(BaseModel):
    Id: Optional[str] = None

class TTPsObservedDetailTypeDef(BaseModel):
    Tactic: Optional[str] = None
    Technique: Optional[str] = None
    Procedure: Optional[str] = None
    IpAddress: Optional[str] = None
    APIName: Optional[str] = None
    APISuccessCount: Optional[int] = None
    APIFailureCount: Optional[int] = None

class InvestigationDetailTypeDef(BaseModel):
    InvestigationId: Optional[str] = None
    Severity: Optional[SeverityType] = None
    Status: Optional[StatusType] = None
    State: Optional[StateType] = None
    CreatedTime: Optional[datetime] = None
    EntityArn: Optional[str] = None
    EntityType: Optional[EntityTypeType] = None

class ListDatasourcePackagesRequestRequestTypeDef(BaseModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGraphsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIndicatorsRequestRequestTypeDef(BaseModel):
    GraphArn: str
    InvestigationId: str
    IndicatorType: Optional[IndicatorTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SortCriteriaTypeDef(BaseModel):
    Field: Optional[FieldType] = None
    SortOrder: Optional[SortOrderType] = None

class ListInvitationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMembersRequestRequestTypeDef(BaseModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class RejectInvitationRequestRequestTypeDef(BaseModel):
    GraphArn: str

class StartMonitoringMemberRequestRequestTypeDef(BaseModel):
    GraphArn: str
    AccountId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDatasourcePackagesRequestRequestTypeDef(BaseModel):
    GraphArn: str
    DatasourcePackages: Sequence[DatasourcePackageType]

class UpdateInvestigationStateRequestRequestTypeDef(BaseModel):
    GraphArn: str
    InvestigationId: str
    State: StateType

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    GraphArn: str
    AutoEnable: Optional[bool] = None

class CreateMembersRequestRequestTypeDef(BaseModel):
    GraphArn: str
    Accounts: Sequence[AccountTypeDef]
    Message: Optional[str] = None
    DisableEmailNotification: Optional[bool] = None

class CreateGraphResponseTypeDef(BaseModel):
    GraphArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(BaseModel):
    AutoEnable: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvestigationResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationAdminAccountsResponseTypeDef(BaseModel):
    Administrators: List[AdministratorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartInvestigationResponseTypeDef(BaseModel):
    InvestigationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(BaseModel):
    AccountIds: List[str]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DatasourcePackageIngestDetailTypeDef(BaseModel):
    DatasourcePackageIngestState: Optional[DatasourcePackageIngestStateType] = None
    LastIngestStateChange: Optional[       Dict[DatasourcePackageIngestStateType, TimestampForCollectionTypeDef] = None

class MembershipDatasourcesTypeDef(BaseModel):
    AccountId: Optional[str] = None
    GraphArn: Optional[str] = None
    DatasourcePackageIngestHistory: Optional[       Dict[         DatasourcePackageType = None

class MemberDetailTypeDef(BaseModel):
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
    VolumeUsageByDatasourcePackage: Optional[       Dict[DatasourcePackageType, DatasourcePackageUsageInfoTypeDef] = None
    DatasourcePackageIngestStates: Optional[       Dict[DatasourcePackageType, DatasourcePackageIngestStateType] = None

class DateFilterTypeDef(BaseModel):
    StartInclusive: TimestampTypeDef
    EndInclusive: TimestampTypeDef

class StartInvestigationRequestRequestTypeDef(BaseModel):
    GraphArn: str
    EntityArn: str
    ScopeStartTime: TimestampTypeDef
    ScopeEndTime: TimestampTypeDef

class ListGraphsResponseTypeDef(BaseModel):
    GraphList: List[GraphTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IndicatorDetailTypeDef(BaseModel):
    TTPsObservedDetail: Optional[TTPsObservedDetailTypeDef] = None
    ImpossibleTravelDetail: Optional[ImpossibleTravelDetailTypeDef] = None
    FlaggedIpAddressDetail: Optional[FlaggedIpAddressDetailTypeDef] = None
    NewGeolocationDetail: Optional[NewGeolocationDetailTypeDef] = None
    NewAsoDetail: Optional[NewAsoDetailTypeDef] = None
    NewUserAgentDetail: Optional[NewUserAgentDetailTypeDef] = None
    RelatedFindingDetail: Optional[RelatedFindingDetailTypeDef] = None
    RelatedFindingGroupDetail: Optional[RelatedFindingGroupDetailTypeDef] = None

class ListInvestigationsResponseTypeDef(BaseModel):
    InvestigationDetails: List[InvestigationDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasourcePackagesResponseTypeDef(BaseModel):
    DatasourcePackages: Dict[DatasourcePackageType, DatasourcePackageIngestDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetGraphMemberDatasourcesResponseTypeDef(BaseModel):
    MemberDatasources: List[MembershipDatasourcesTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetMembershipDatasourcesResponseTypeDef(BaseModel):
    MembershipDatasources: List[MembershipDatasourcesTypeDef]
    UnprocessedGraphs: List[UnprocessedGraphTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembersResponseTypeDef(BaseModel):
    Members: List[MemberDetailTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembersResponseTypeDef(BaseModel):
    MemberDetails: List[MemberDetailTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(BaseModel):
    Invitations: List[MemberDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseModel):
    MemberDetails: List[MemberDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FilterCriteriaTypeDef(BaseModel):
    Severity: Optional[StringFilterTypeDef] = None
    Status: Optional[StringFilterTypeDef] = None
    State: Optional[StringFilterTypeDef] = None
    EntityArn: Optional[StringFilterTypeDef] = None
    CreatedTime: Optional[DateFilterTypeDef] = None

class IndicatorTypeDef(BaseModel):
    IndicatorType: Optional[IndicatorTypeType] = None
    IndicatorDetail: Optional[IndicatorDetailTypeDef] = None

class ListInvestigationsRequestRequestTypeDef(BaseModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None

class ListIndicatorsResponseTypeDef(BaseModel):
    GraphArn: str
    InvestigationId: str
    NextToken: str
    Indicators: List[IndicatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

