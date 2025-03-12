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
from aws_resource_validator.pydantic_models.shield_constants import *

class ResponseActionOutputTypeDef(BaseValidatorModel):
    Block: Optional[Dict[str, Any]] = None
    Count: Optional[Dict[str, Any]] = None


class AssociateDRTLogBucketRequestTypeDef(BaseValidatorModel):
    LogBucket: str


class AssociateDRTRoleRequestTypeDef(BaseValidatorModel):
    RoleArn: str


class AssociateHealthCheckRequestTypeDef(BaseValidatorModel):
    ProtectionId: str
    HealthCheckArn: str


class EmergencyContactTypeDef(BaseValidatorModel):
    EmailAddress: str
    PhoneNumber: Optional[str] = None
    ContactNotes: Optional[str] = None


class MitigationTypeDef(BaseValidatorModel):
    MitigationName: Optional[str] = None


class SummarizedCounterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    N: Optional[int] = None
    Unit: Optional[str] = None


class ContributorTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[int] = None


class AttackVectorDescriptionTypeDef(BaseValidatorModel):
    VectorType: str


class AttackVolumeStatisticsTypeDef(BaseValidatorModel):
    Max: float


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteProtectionGroupRequestTypeDef(BaseValidatorModel):
    ProtectionGroupId: str


class DeleteProtectionRequestTypeDef(BaseValidatorModel):
    ProtectionId: str


class DescribeAttackRequestTypeDef(BaseValidatorModel):
    AttackId: str


class TimeRangeOutputTypeDef(BaseValidatorModel):
    FromInclusive: Optional[datetime] = None
    ToExclusive: Optional[datetime] = None


class DescribeProtectionGroupRequestTypeDef(BaseValidatorModel):
    ProtectionGroupId: str


class DescribeProtectionRequestTypeDef(BaseValidatorModel):
    ProtectionId: Optional[str] = None
    ResourceArn: Optional[str] = None


class DisableApplicationLayerAutomaticResponseRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DisassociateDRTLogBucketRequestTypeDef(BaseValidatorModel):
    LogBucket: str


class DisassociateHealthCheckRequestTypeDef(BaseValidatorModel):
    ProtectionId: str
    HealthCheckArn: str


class InclusionProtectionFiltersTypeDef(BaseValidatorModel):
    ResourceArns: Optional[Sequence[str]] = None
    ProtectionNames: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[ProtectedResourceTypeType]] = None


class InclusionProtectionGroupFiltersTypeDef(BaseValidatorModel):
    ProtectionGroupIds: Optional[Sequence[str]] = None
    Patterns: Optional[Sequence[ProtectionGroupPatternType]] = None
    ResourceTypes: Optional[Sequence[ProtectedResourceTypeType]] = None
    Aggregations: Optional[Sequence[ProtectionGroupAggregationType]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListResourcesInProtectionGroupRequestTypeDef(BaseValidatorModel):
    ProtectionGroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class ProtectionGroupArbitraryPatternLimitsTypeDef(BaseValidatorModel):
    MaxMembers: int


class ResponseActionTypeDef(BaseValidatorModel):
    Block: Optional[Mapping[str, Any]] = None
    Count: Optional[Mapping[str, Any]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateSubscriptionRequestTypeDef(BaseValidatorModel):
    AutoRenew: Optional[AutoRenewType] = None


class ApplicationLayerAutomaticResponseConfigurationTypeDef(BaseValidatorModel):
    Status: ApplicationLayerAutomaticResponseStatusType
    Action: ResponseActionOutputTypeDef


class AssociateProactiveEngagementDetailsRequestTypeDef(BaseValidatorModel):
    EmergencyContactList: Sequence[EmergencyContactTypeDef]


class UpdateEmergencyContactSettingsRequestTypeDef(BaseValidatorModel):
    EmergencyContactList: Optional[Sequence[EmergencyContactTypeDef]] = None


class SummarizedAttackVectorTypeDef(BaseValidatorModel):
    VectorType: str
    VectorCounters: Optional[List[SummarizedCounterTypeDef]] = None


class AttackPropertyTypeDef(BaseValidatorModel):
    AttackLayer: Optional[AttackLayerType] = None
    AttackPropertyIdentifier: Optional[AttackPropertyIdentifierType] = None
    TopContributors: Optional[List[ContributorTypeDef]] = None
    Unit: Optional[UnitType] = None
    Total: Optional[int] = None


class AttackSummaryTypeDef(BaseValidatorModel):
    AttackId: Optional[str] = None
    ResourceArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    AttackVectors: Optional[List[AttackVectorDescriptionTypeDef]] = None


class AttackVolumeTypeDef(BaseValidatorModel):
    BitsPerSecond: Optional[AttackVolumeStatisticsTypeDef] = None
    PacketsPerSecond: Optional[AttackVolumeStatisticsTypeDef] = None
    RequestsPerSecond: Optional[AttackVolumeStatisticsTypeDef] = None


class CreateProtectionRequestTypeDef(BaseValidatorModel):
    Name: str
    ResourceArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateProtectionResponseTypeDef(BaseValidatorModel):
    ProtectionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDRTAccessResponseTypeDef(BaseValidatorModel):
    RoleArn: str
    LogBucketList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEmergencyContactSettingsResponseTypeDef(BaseValidatorModel):
    EmergencyContactList: List[EmergencyContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSubscriptionStateResponseTypeDef(BaseValidatorModel):
    SubscriptionState: SubscriptionStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourcesInProtectionGroupResponseTypeDef(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProtectionGroupTypeDef(BaseValidatorModel):
    pass


class DescribeProtectionGroupResponseTypeDef(BaseValidatorModel):
    ProtectionGroup: ProtectionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListProtectionGroupsResponseTypeDef(BaseValidatorModel):
    ProtectionGroups: List[ProtectionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProtectionsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InclusionFilters: Optional[InclusionProtectionFiltersTypeDef] = None


class ListProtectionGroupsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InclusionFilters: Optional[InclusionProtectionGroupFiltersTypeDef] = None


class LimitTypeDef(BaseValidatorModel):
    pass


class ProtectionLimitsTypeDef(BaseValidatorModel):
    ProtectedResourceTypeLimits: List[LimitTypeDef]


class ListProtectionsRequestPaginateTypeDef(BaseValidatorModel):
    InclusionFilters: Optional[InclusionProtectionFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ProtectionGroupPatternTypeLimitsTypeDef(BaseValidatorModel):
    ArbitraryPatternLimits: ProtectionGroupArbitraryPatternLimitsTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class TimeRangeTypeDef(BaseValidatorModel):
    FromInclusive: Optional[TimestampTypeDef] = None
    ToExclusive: Optional[TimestampTypeDef] = None


class ProtectionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    ResourceArn: Optional[str] = None
    HealthCheckIds: Optional[List[str]] = None
    ProtectionArn: Optional[str] = None
    ApplicationLayerAutomaticResponseConfiguration: Optional[ ApplicationLayerAutomaticResponseConfigurationTypeDef ] = None


class ListAttacksResponseTypeDef(BaseValidatorModel):
    AttackSummaries: List[AttackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AttackStatisticsDataItemTypeDef(BaseValidatorModel):
    AttackCount: int
    AttackVolume: Optional[AttackVolumeTypeDef] = None


class ProtectionGroupLimitsTypeDef(BaseValidatorModel):
    MaxProtectionGroups: int
    PatternTypeLimits: ProtectionGroupPatternTypeLimitsTypeDef


class ResponseActionUnionTypeDef(BaseValidatorModel):
    pass


class EnableApplicationLayerAutomaticResponseRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Action: ResponseActionUnionTypeDef


class UpdateApplicationLayerAutomaticResponseRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Action: ResponseActionUnionTypeDef


class DescribeProtectionResponseTypeDef(BaseValidatorModel):
    Protection: ProtectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListProtectionsResponseTypeDef(BaseValidatorModel):
    Protections: List[ProtectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SubResourceSummaryTypeDef(BaseValidatorModel):
    pass


class AttackDetailTypeDef(BaseValidatorModel):
    AttackId: Optional[str] = None
    ResourceArn: Optional[str] = None
    SubResources: Optional[List[SubResourceSummaryTypeDef]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    AttackCounters: Optional[List[SummarizedCounterTypeDef]] = None
    AttackProperties: Optional[List[AttackPropertyTypeDef]] = None
    Mitigations: Optional[List[MitigationTypeDef]] = None


class DescribeAttackStatisticsResponseTypeDef(BaseValidatorModel):
    TimeRange: TimeRangeOutputTypeDef
    DataItems: List[AttackStatisticsDataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SubscriptionLimitsTypeDef(BaseValidatorModel):
    ProtectionLimits: ProtectionLimitsTypeDef
    ProtectionGroupLimits: ProtectionGroupLimitsTypeDef


class TimeRangeUnionTypeDef(BaseValidatorModel):
    pass


class ListAttacksRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArns: Optional[Sequence[str]] = None
    StartTime: Optional[TimeRangeUnionTypeDef] = None
    EndTime: Optional[TimeRangeUnionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttacksRequestTypeDef(BaseValidatorModel):
    ResourceArns: Optional[Sequence[str]] = None
    StartTime: Optional[TimeRangeUnionTypeDef] = None
    EndTime: Optional[TimeRangeUnionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeAttackResponseTypeDef(BaseValidatorModel):
    Attack: AttackDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SubscriptionTypeDef(BaseValidatorModel):
    SubscriptionLimits: SubscriptionLimitsTypeDef
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TimeCommitmentInSeconds: Optional[int] = None
    AutoRenew: Optional[AutoRenewType] = None
    Limits: Optional[List[LimitTypeDef]] = None
    ProactiveEngagementStatus: Optional[ProactiveEngagementStatusType] = None
    SubscriptionArn: Optional[str] = None


class DescribeSubscriptionResponseTypeDef(BaseValidatorModel):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


