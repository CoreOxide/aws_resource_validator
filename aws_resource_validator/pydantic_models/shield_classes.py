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
from aws_resource_validator.pydantic_models.shield_constants import *

class ResponseActionOutputTypeDef(BaseModel):
    Block: Optional[Dict[str, Any]] = None
    Count: Optional[Dict[str, Any]] = None

class AssociateDRTLogBucketRequestRequestTypeDef(BaseModel):
    LogBucket: str

class AssociateDRTRoleRequestRequestTypeDef(BaseModel):
    RoleArn: str

class AssociateHealthCheckRequestRequestTypeDef(BaseModel):
    ProtectionId: str
    HealthCheckArn: str

class EmergencyContactTypeDef(BaseModel):
    EmailAddress: str
    PhoneNumber: Optional[str] = None
    ContactNotes: Optional[str] = None

class MitigationTypeDef(BaseModel):
    MitigationName: Optional[str] = None

class SummarizedCounterTypeDef(BaseModel):
    Name: Optional[str] = None
    Max: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    N: Optional[int] = None
    Unit: Optional[str] = None

class ContributorTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[int] = None

class AttackVectorDescriptionTypeDef(BaseModel):
    VectorType: str

class AttackVolumeStatisticsTypeDef(BaseModel):
    Max: float

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteProtectionGroupRequestRequestTypeDef(BaseModel):
    ProtectionGroupId: str

class DeleteProtectionRequestRequestTypeDef(BaseModel):
    ProtectionId: str

class DescribeAttackRequestRequestTypeDef(BaseModel):
    AttackId: str

class TimeRangeOutputTypeDef(BaseModel):
    FromInclusive: Optional[datetime] = None
    ToExclusive: Optional[datetime] = None

class DescribeProtectionGroupRequestRequestTypeDef(BaseModel):
    ProtectionGroupId: str

class ProtectionGroupTypeDef(BaseModel):
    ProtectionGroupId: str
    Aggregation: ProtectionGroupAggregationType
    Pattern: ProtectionGroupPatternType
    Members: List[str]
    ResourceType: Optional[ProtectedResourceTypeType] = None
    ProtectionGroupArn: Optional[str] = None

class DescribeProtectionRequestRequestTypeDef(BaseModel):
    ProtectionId: Optional[str] = None
    ResourceArn: Optional[str] = None

class DisableApplicationLayerAutomaticResponseRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DisassociateDRTLogBucketRequestRequestTypeDef(BaseModel):
    LogBucket: str

class DisassociateHealthCheckRequestRequestTypeDef(BaseModel):
    ProtectionId: str
    HealthCheckArn: str

class ResponseActionTypeDef(BaseModel):
    Block: Optional[Mapping[str, Any]] = None
    Count: Optional[Mapping[str, Any]] = None

class InclusionProtectionFiltersTypeDef(BaseModel):
    ResourceArns: Optional[Sequence[str]] = None
    ProtectionNames: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[ProtectedResourceTypeType]] = None

class InclusionProtectionGroupFiltersTypeDef(BaseModel):
    ProtectionGroupIds: Optional[Sequence[str]] = None
    Patterns: Optional[Sequence[ProtectionGroupPatternType]] = None
    ResourceTypes: Optional[Sequence[ProtectedResourceTypeType]] = None
    Aggregations: Optional[Sequence[ProtectionGroupAggregationType]] = None

class LimitTypeDef(BaseModel):
    Type: Optional[str] = None
    Max: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListResourcesInProtectionGroupRequestRequestTypeDef(BaseModel):
    ProtectionGroupId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ProtectionGroupArbitraryPatternLimitsTypeDef(BaseModel):
    MaxMembers: int

class ResponseActionExtraOutputTypeDef(BaseModel):
    Block: Optional[Dict[str, Any]] = None
    Count: Optional[Dict[str, Any]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateProtectionGroupRequestRequestTypeDef(BaseModel):
    ProtectionGroupId: str
    Aggregation: ProtectionGroupAggregationType
    Pattern: ProtectionGroupPatternType
    ResourceType: Optional[ProtectedResourceTypeType] = None
    Members: Optional[Sequence[str]] = None

class UpdateSubscriptionRequestRequestTypeDef(BaseModel):
    AutoRenew: Optional[AutoRenewType] = None

class ApplicationLayerAutomaticResponseConfigurationTypeDef(BaseModel):
    Status: ApplicationLayerAutomaticResponseStatusType
    Action: ResponseActionOutputTypeDef

class AssociateProactiveEngagementDetailsRequestRequestTypeDef(BaseModel):
    EmergencyContactList: Sequence[EmergencyContactTypeDef]

class UpdateEmergencyContactSettingsRequestRequestTypeDef(BaseModel):
    EmergencyContactList: Optional[Sequence[EmergencyContactTypeDef]] = None

class SummarizedAttackVectorTypeDef(BaseModel):
    VectorType: str
    VectorCounters: Optional[List[SummarizedCounterTypeDef]] = None

class AttackPropertyTypeDef(BaseModel):
    AttackLayer: Optional[AttackLayerType] = None
    AttackPropertyIdentifier: Optional[AttackPropertyIdentifierType] = None
    TopContributors: Optional[List[ContributorTypeDef]] = None
    Unit: Optional[UnitType] = None
    Total: Optional[int] = None

class AttackSummaryTypeDef(BaseModel):
    AttackId: Optional[str] = None
    ResourceArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    AttackVectors: Optional[List[AttackVectorDescriptionTypeDef]] = None

class AttackVolumeTypeDef(BaseModel):
    BitsPerSecond: Optional[AttackVolumeStatisticsTypeDef] = None
    PacketsPerSecond: Optional[AttackVolumeStatisticsTypeDef] = None
    RequestsPerSecond: Optional[AttackVolumeStatisticsTypeDef] = None

class CreateProtectionGroupRequestRequestTypeDef(BaseModel):
    ProtectionGroupId: str
    Aggregation: ProtectionGroupAggregationType
    Pattern: ProtectionGroupPatternType
    ResourceType: Optional[ProtectedResourceTypeType] = None
    Members: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateProtectionRequestRequestTypeDef(BaseModel):
    Name: str
    ResourceArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateProtectionResponseTypeDef(BaseModel):
    ProtectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDRTAccessResponseTypeDef(BaseModel):
    RoleArn: str
    LogBucketList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEmergencyContactSettingsResponseTypeDef(BaseModel):
    EmergencyContactList: List[EmergencyContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionStateResponseTypeDef(BaseModel):
    SubscriptionState: SubscriptionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesInProtectionGroupResponseTypeDef(BaseModel):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProtectionGroupResponseTypeDef(BaseModel):
    ProtectionGroup: ProtectionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectionGroupsResponseTypeDef(BaseModel):
    ProtectionGroups: List[ProtectionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EnableApplicationLayerAutomaticResponseRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Action: ResponseActionTypeDef

class UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Action: ResponseActionTypeDef

class ListProtectionsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InclusionFilters: Optional[InclusionProtectionFiltersTypeDef] = None

class ListProtectionGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InclusionFilters: Optional[InclusionProtectionGroupFiltersTypeDef] = None

class ProtectionLimitsTypeDef(BaseModel):
    ProtectedResourceTypeLimits: List[LimitTypeDef]

class ListProtectionsRequestListProtectionsPaginateTypeDef(BaseModel):
    InclusionFilters: Optional[InclusionProtectionFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ProtectionGroupPatternTypeLimitsTypeDef(BaseModel):
    ArbitraryPatternLimits: ProtectionGroupArbitraryPatternLimitsTypeDef

class TimeRangeTypeDef(BaseModel):
    FromInclusive: Optional[TimestampTypeDef] = None
    ToExclusive: Optional[TimestampTypeDef] = None

class ProtectionTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    ResourceArn: Optional[str] = None
    HealthCheckIds: Optional[List[str]] = None
    ProtectionArn: Optional[str] = None
    ApplicationLayerAutomaticResponseConfiguration: Optional[       ApplicationLayerAutomaticResponseConfigurationTypeDef     ] = None

class SubResourceSummaryTypeDef(BaseModel):
    Type: Optional[SubResourceTypeType] = None
    Id: Optional[str] = None
    AttackVectors: Optional[List[SummarizedAttackVectorTypeDef]] = None
    Counters: Optional[List[SummarizedCounterTypeDef]] = None

class ListAttacksResponseTypeDef(BaseModel):
    AttackSummaries: List[AttackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AttackStatisticsDataItemTypeDef(BaseModel):
    AttackCount: int
    AttackVolume: Optional[AttackVolumeTypeDef] = None

class ProtectionGroupLimitsTypeDef(BaseModel):
    MaxProtectionGroups: int
    PatternTypeLimits: ProtectionGroupPatternTypeLimitsTypeDef

class ListAttacksRequestListAttacksPaginateTypeDef(BaseModel):
    ResourceArns: Optional[Sequence[str]] = None
    StartTime: Optional[TimeRangeTypeDef] = None
    EndTime: Optional[TimeRangeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttacksRequestRequestTypeDef(BaseModel):
    ResourceArns: Optional[Sequence[str]] = None
    StartTime: Optional[TimeRangeTypeDef] = None
    EndTime: Optional[TimeRangeTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeProtectionResponseTypeDef(BaseModel):
    Protection: ProtectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectionsResponseTypeDef(BaseModel):
    Protections: List[ProtectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AttackDetailTypeDef(BaseModel):
    AttackId: Optional[str] = None
    ResourceArn: Optional[str] = None
    SubResources: Optional[List[SubResourceSummaryTypeDef]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    AttackCounters: Optional[List[SummarizedCounterTypeDef]] = None
    AttackProperties: Optional[List[AttackPropertyTypeDef]] = None
    Mitigations: Optional[List[MitigationTypeDef]] = None

class DescribeAttackStatisticsResponseTypeDef(BaseModel):
    TimeRange: TimeRangeOutputTypeDef
    DataItems: List[AttackStatisticsDataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionLimitsTypeDef(BaseModel):
    ProtectionLimits: ProtectionLimitsTypeDef
    ProtectionGroupLimits: ProtectionGroupLimitsTypeDef

class DescribeAttackResponseTypeDef(BaseModel):
    Attack: AttackDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionTypeDef(BaseModel):
    SubscriptionLimits: SubscriptionLimitsTypeDef
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TimeCommitmentInSeconds: Optional[int] = None
    AutoRenew: Optional[AutoRenewType] = None
    Limits: Optional[List[LimitTypeDef]] = None
    ProactiveEngagementStatus: Optional[ProactiveEngagementStatusType] = None
    SubscriptionArn: Optional[str] = None

class DescribeSubscriptionResponseTypeDef(BaseModel):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

