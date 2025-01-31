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
from aws_resource_validator.pydantic_models.detective_constants import *

class AcceptInvitationRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str

class AccountTypeDef(BaseValidatorModel):
    AccountId: str
    EmailAddress: str

class AdministratorTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    GraphArn: Optional[str] = None
    DelegationTime: Optional[datetime] = None

class BatchGetGraphMemberDatasourcesRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class UnprocessedAccountTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Reason: Optional[str] = None

class BatchGetMembershipDatasourcesRequestRequestTypeDef(BaseValidatorModel):
    GraphArns: Sequence[str]

class UnprocessedGraphTypeDef(BaseValidatorModel):
    GraphArn: Optional[str] = None
    Reason: Optional[str] = None

class CreateGraphRequestRequestTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None

class TimestampForCollectionTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None

class DatasourcePackageUsageInfoTypeDef(BaseValidatorModel):
    VolumeUsageInBytes: Optional[int] = None
    VolumeUsageUpdateTime: Optional[datetime] = None

class DeleteGraphRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str

class DeleteMembersRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    AccountIds: Sequence[str]

class DescribeOrganizationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str

class DisassociateMembershipRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class StringFilterTypeDef(BaseValidatorModel):
    Value: str

class FlaggedIpAddressDetailTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Reason: Optional[Literal["AWS_THREAT_INTELLIGENCE"]] = None

class GetInvestigationRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str

class GetMembersRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    AccountIds: Sequence[str]

class GraphTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class ImpossibleTravelDetailTypeDef(BaseValidatorModel):
    StartingIpAddress: Optional[str] = None
    EndingIpAddress: Optional[str] = None
    StartingLocation: Optional[str] = None
    EndingLocation: Optional[str] = None
    HourlyTimeDelta: Optional[int] = None

class NewAsoDetailTypeDef(BaseValidatorModel):
    Aso: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None

class NewGeolocationDetailTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    IpAddress: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None

class NewUserAgentDetailTypeDef(BaseValidatorModel):
    UserAgent: Optional[str] = None
    IsNewForEntireAccount: Optional[bool] = None

class RelatedFindingDetailTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[str] = None
    IpAddress: Optional[str] = None

class RelatedFindingGroupDetailTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class TTPsObservedDetailTypeDef(BaseValidatorModel):
    Tactic: Optional[str] = None
    Technique: Optional[str] = None
    Procedure: Optional[str] = None
    IpAddress: Optional[str] = None
    APIName: Optional[str] = None
    APISuccessCount: Optional[int] = None
    APIFailureCount: Optional[int] = None

class InvestigationDetailTypeDef(BaseValidatorModel):
    InvestigationId: Optional[str] = None
    Severity: Optional[SeverityType] = None
    Status: Optional[StatusType] = None
    State: Optional[StateType] = None
    CreatedTime: Optional[datetime] = None
    EntityArn: Optional[str] = None
    EntityType: Optional[EntityTypeType] = None

class ListDatasourcePackagesRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGraphsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIndicatorsRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    IndicatorType: Optional[IndicatorTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SortCriteriaTypeDef(BaseValidatorModel):
    Field: Optional[FieldType] = None
    SortOrder: Optional[SortOrderType] = None

class ListInvitationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMembersRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class RejectInvitationRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str

class StartMonitoringMemberRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    AccountId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDatasourcePackagesRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    DatasourcePackages: Sequence[DatasourcePackageType]

class UpdateInvestigationStateRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    State: StateType

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    AutoEnable: Optional[bool] = None

class CreateMembersRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    Accounts: Sequence[AccountTypeDef]
    Message: Optional[str] = None
    DisableEmailNotification: Optional[bool] = None

class CreateGraphResponseTypeDef(BaseValidatorModel):
    GraphArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    AutoEnable: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvestigationResponseTypeDef(BaseValidatorModel):
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

class ListOrganizationAdminAccountsResponseTypeDef(BaseValidatorModel):
    Administrators: List[AdministratorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartInvestigationResponseTypeDef(BaseValidatorModel):
    InvestigationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DatasourcePackageIngestDetailTypeDef(BaseValidatorModel):
    DatasourcePackageIngestState: Optional[DatasourcePackageIngestStateType] = None
    LastIngestStateChange: Optional[       Dict[DatasourcePackageIngestStateType, TimestampForCollectionTypeDef]] = None

class MembershipDatasourcesTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    GraphArn: Optional[str] = None
    DatasourcePackageIngestHistory: Optional[       List[         DatasourcePackageType]] = None

class MemberDetailTypeDef(BaseValidatorModel):
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
    VolumeUsageByDatasourcePackage: Optional[       Dict[DatasourcePackageType, DatasourcePackageUsageInfoTypeDef]] = None
    DatasourcePackageIngestStates: Optional[       Dict[DatasourcePackageType, DatasourcePackageIngestStateType]] = None

class DateFilterTypeDef(BaseValidatorModel):
    StartInclusive: TimestampTypeDef
    EndInclusive: TimestampTypeDef

class StartInvestigationRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    EntityArn: str
    ScopeStartTime: TimestampTypeDef
    ScopeEndTime: TimestampTypeDef

class ListGraphsResponseTypeDef(BaseValidatorModel):
    GraphList: List[GraphTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IndicatorDetailTypeDef(BaseValidatorModel):
    TTPsObservedDetail: Optional[TTPsObservedDetailTypeDef] = None
    ImpossibleTravelDetail: Optional[ImpossibleTravelDetailTypeDef] = None
    FlaggedIpAddressDetail: Optional[FlaggedIpAddressDetailTypeDef] = None
    NewGeolocationDetail: Optional[NewGeolocationDetailTypeDef] = None
    NewAsoDetail: Optional[NewAsoDetailTypeDef] = None
    NewUserAgentDetail: Optional[NewUserAgentDetailTypeDef] = None
    RelatedFindingDetail: Optional[RelatedFindingDetailTypeDef] = None
    RelatedFindingGroupDetail: Optional[RelatedFindingGroupDetailTypeDef] = None

class ListInvestigationsResponseTypeDef(BaseValidatorModel):
    InvestigationDetails: List[InvestigationDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasourcePackagesResponseTypeDef(BaseValidatorModel):
    DatasourcePackages: Dict[DatasourcePackageType, DatasourcePackageIngestDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetGraphMemberDatasourcesResponseTypeDef(BaseValidatorModel):
    MemberDatasources: List[MembershipDatasourcesTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetMembershipDatasourcesResponseTypeDef(BaseValidatorModel):
    MembershipDatasources: List[MembershipDatasourcesTypeDef]
    UnprocessedGraphs: List[UnprocessedGraphTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberDetailTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembersResponseTypeDef(BaseValidatorModel):
    MemberDetails: List[MemberDetailTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(BaseValidatorModel):
    Invitations: List[MemberDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseValidatorModel):
    MemberDetails: List[MemberDetailTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FilterCriteriaTypeDef(BaseValidatorModel):
    Severity: Optional[StringFilterTypeDef] = None
    Status: Optional[StringFilterTypeDef] = None
    State: Optional[StringFilterTypeDef] = None
    EntityArn: Optional[StringFilterTypeDef] = None
    CreatedTime: Optional[DateFilterTypeDef] = None

class IndicatorTypeDef(BaseValidatorModel):
    IndicatorType: Optional[IndicatorTypeType] = None
    IndicatorDetail: Optional[IndicatorDetailTypeDef] = None

class ListInvestigationsRequestRequestTypeDef(BaseValidatorModel):
    GraphArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    SortCriteria: Optional[SortCriteriaTypeDef] = None

class ListIndicatorsResponseTypeDef(BaseValidatorModel):
    GraphArn: str
    InvestigationId: str
    NextToken: str
    Indicators: List[IndicatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

