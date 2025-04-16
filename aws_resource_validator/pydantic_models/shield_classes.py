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

class ResponseActionOutput(BaseValidatorModel):
    Block: Optional[Dict[str, Any]] = None
    Count: Optional[Dict[str, Any]] = None


class AssociateDRTLogBucketRequest(BaseValidatorModel):
    LogBucket: str


class AssociateDRTRoleRequest(BaseValidatorModel):
    RoleArn: str


class AssociateHealthCheckRequest(BaseValidatorModel):
    ProtectionId: str
    HealthCheckArn: str


class EmergencyContact(BaseValidatorModel):
    EmailAddress: str
    PhoneNumber: Optional[str] = None
    ContactNotes: Optional[str] = None


class Mitigation(BaseValidatorModel):
    MitigationName: Optional[str] = None


class SummarizedCounter(BaseValidatorModel):
    Name: Optional[str] = None
    Max: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    N: Optional[int] = None
    Unit: Optional[str] = None


class Contributor(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[int] = None


class AttackVectorDescription(BaseValidatorModel):
    VectorType: str


class AttackVolumeStatistics(BaseValidatorModel):
    Max: float


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteProtectionGroupRequest(BaseValidatorModel):
    ProtectionGroupId: str


class DeleteProtectionRequest(BaseValidatorModel):
    ProtectionId: str


class DescribeAttackRequest(BaseValidatorModel):
    AttackId: str


class TimeRangeOutput(BaseValidatorModel):
    FromInclusive: Optional[datetime] = None
    ToExclusive: Optional[datetime] = None


class DescribeProtectionGroupRequest(BaseValidatorModel):
    ProtectionGroupId: str


class DescribeProtectionRequest(BaseValidatorModel):
    ProtectionId: Optional[str] = None
    ResourceArn: Optional[str] = None


class DisableApplicationLayerAutomaticResponseRequest(BaseValidatorModel):
    ResourceArn: str


class DisassociateDRTLogBucketRequest(BaseValidatorModel):
    LogBucket: str


class DisassociateHealthCheckRequest(BaseValidatorModel):
    ProtectionId: str
    HealthCheckArn: str


class InclusionProtectionFilters(BaseValidatorModel):
    ResourceArns: Optional[Sequence[str]] = None
    ProtectionNames: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[ProtectedResourceTypeType]] = None


class InclusionProtectionGroupFilters(BaseValidatorModel):
    ProtectionGroupIds: Optional[Sequence[str]] = None
    Patterns: Optional[Sequence[ProtectionGroupPatternType]] = None
    ResourceTypes: Optional[Sequence[ProtectedResourceTypeType]] = None
    Aggregations: Optional[Sequence[ProtectionGroupAggregationType]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListResourcesInProtectionGroupRequest(BaseValidatorModel):
    ProtectionGroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class ProtectionGroupArbitraryPatternLimits(BaseValidatorModel):
    MaxMembers: int


class ResponseAction(BaseValidatorModel):
    Block: Optional[Mapping[str, Any]] = None
    Count: Optional[Mapping[str, Any]] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateSubscriptionRequest(BaseValidatorModel):
    AutoRenew: Optional[AutoRenewType] = None


class ApplicationLayerAutomaticResponseConfiguration(BaseValidatorModel):
    Status: ApplicationLayerAutomaticResponseStatusType
    Action: ResponseActionOutput


class AssociateProactiveEngagementDetailsRequest(BaseValidatorModel):
    EmergencyContactList: Sequence[EmergencyContact]


class UpdateEmergencyContactSettingsRequest(BaseValidatorModel):
    EmergencyContactList: Optional[Sequence[EmergencyContact]] = None


class SummarizedAttackVector(BaseValidatorModel):
    VectorType: str
    VectorCounters: Optional[List[SummarizedCounter]] = None


class AttackProperty(BaseValidatorModel):
    AttackLayer: Optional[AttackLayerType] = None
    AttackPropertyIdentifier: Optional[AttackPropertyIdentifierType] = None
    TopContributors: Optional[List[Contributor]] = None
    Unit: Optional[UnitType] = None
    Total: Optional[int] = None


class AttackSummary(BaseValidatorModel):
    AttackId: Optional[str] = None
    ResourceArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    AttackVectors: Optional[List[AttackVectorDescription]] = None


class AttackVolume(BaseValidatorModel):
    BitsPerSecond: Optional[AttackVolumeStatistics] = None
    PacketsPerSecond: Optional[AttackVolumeStatistics] = None
    RequestsPerSecond: Optional[AttackVolumeStatistics] = None


class CreateProtectionRequest(BaseValidatorModel):
    Name: str
    ResourceArn: str
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateProtectionResponse(BaseValidatorModel):
    ProtectionId: str
    ResponseMetadata: ResponseMetadata


class DescribeDRTAccessResponse(BaseValidatorModel):
    RoleArn: str
    LogBucketList: List[str]
    ResponseMetadata: ResponseMetadata


class DescribeEmergencyContactSettingsResponse(BaseValidatorModel):
    EmergencyContactList: List[EmergencyContact]
    ResponseMetadata: ResponseMetadata


class GetSubscriptionStateResponse(BaseValidatorModel):
    SubscriptionState: SubscriptionStateType
    ResponseMetadata: ResponseMetadata


class ListResourcesInProtectionGroupResponse(BaseValidatorModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ProtectionGroup(BaseValidatorModel):
    pass


class DescribeProtectionGroupResponse(BaseValidatorModel):
    ProtectionGroup: ProtectionGroup
    ResponseMetadata: ResponseMetadata


class ListProtectionGroupsResponse(BaseValidatorModel):
    ProtectionGroups: List[ProtectionGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProtectionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InclusionFilters: Optional[InclusionProtectionFilters] = None


class ListProtectionGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InclusionFilters: Optional[InclusionProtectionGroupFilters] = None


class Limit(BaseValidatorModel):
    pass


class ProtectionLimits(BaseValidatorModel):
    ProtectedResourceTypeLimits: List[Limit]


class ListProtectionsRequestPaginate(BaseValidatorModel):
    InclusionFilters: Optional[InclusionProtectionFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ProtectionGroupPatternTypeLimits(BaseValidatorModel):
    ArbitraryPatternLimits: ProtectionGroupArbitraryPatternLimits


class Timestamp(BaseValidatorModel):
    pass


class TimeRange(BaseValidatorModel):
    FromInclusive: Optional[Timestamp] = None
    ToExclusive: Optional[Timestamp] = None


class Protection(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    ResourceArn: Optional[str] = None
    HealthCheckIds: Optional[List[str]] = None
    ProtectionArn: Optional[str] = None
    ApplicationLayerAutomaticResponseConfiguration: Optional[ ApplicationLayerAutomaticResponseConfiguration ] = None


class ListAttacksResponse(BaseValidatorModel):
    AttackSummaries: List[AttackSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AttackStatisticsDataItem(BaseValidatorModel):
    AttackCount: int
    AttackVolume: Optional[AttackVolume] = None


class ProtectionGroupLimits(BaseValidatorModel):
    MaxProtectionGroups: int
    PatternTypeLimits: ProtectionGroupPatternTypeLimits


class ResponseActionUnion(BaseValidatorModel):
    pass


class EnableApplicationLayerAutomaticResponseRequest(BaseValidatorModel):
    ResourceArn: str
    Action: ResponseActionUnion


class UpdateApplicationLayerAutomaticResponseRequest(BaseValidatorModel):
    ResourceArn: str
    Action: ResponseActionUnion


class DescribeProtectionResponse(BaseValidatorModel):
    Protection: Protection
    ResponseMetadata: ResponseMetadata


class ListProtectionsResponse(BaseValidatorModel):
    Protections: List[Protection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SubResourceSummary(BaseValidatorModel):
    pass


class AttackDetail(BaseValidatorModel):
    AttackId: Optional[str] = None
    ResourceArn: Optional[str] = None
    SubResources: Optional[List[SubResourceSummary]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    AttackCounters: Optional[List[SummarizedCounter]] = None
    AttackProperties: Optional[List[AttackProperty]] = None
    Mitigations: Optional[List[Mitigation]] = None


class DescribeAttackStatisticsResponse(BaseValidatorModel):
    TimeRange: TimeRangeOutput
    DataItems: List[AttackStatisticsDataItem]
    ResponseMetadata: ResponseMetadata


class SubscriptionLimits(BaseValidatorModel):
    ProtectionLimits: ProtectionLimits
    ProtectionGroupLimits: ProtectionGroupLimits


class TimeRangeUnion(BaseValidatorModel):
    pass


class ListAttacksRequestPaginate(BaseValidatorModel):
    ResourceArns: Optional[Sequence[str]] = None
    StartTime: Optional[TimeRangeUnion] = None
    EndTime: Optional[TimeRangeUnion] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttacksRequest(BaseValidatorModel):
    ResourceArns: Optional[Sequence[str]] = None
    StartTime: Optional[TimeRangeUnion] = None
    EndTime: Optional[TimeRangeUnion] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeAttackResponse(BaseValidatorModel):
    Attack: AttackDetail
    ResponseMetadata: ResponseMetadata


class Subscription(BaseValidatorModel):
    SubscriptionLimits: SubscriptionLimits
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TimeCommitmentInSeconds: Optional[int] = None
    AutoRenew: Optional[AutoRenewType] = None
    Limits: Optional[List[Limit]] = None
    ProactiveEngagementStatus: Optional[ProactiveEngagementStatusType] = None
    SubscriptionArn: Optional[str] = None


class DescribeSubscriptionResponse(BaseValidatorModel):
    Subscription: Subscription
    ResponseMetadata: ResponseMetadata


