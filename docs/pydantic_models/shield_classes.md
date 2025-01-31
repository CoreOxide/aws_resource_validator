# shield_classes

# ApplicationLayerAutomaticResponseConfigurationTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseActionOutputTypeDef'>
- **Required**: Yes


# AssociateDRTLogBucketRequestRequestTypeDef

### LogBucket
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateDRTRoleRequestRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateHealthCheckRequestRequestTypeDef

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateProactiveEngagementDetailsRequestRequestTypeDef

### EmergencyContactList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.shield_classes.EmergencyContactTypeDef]
- **Required**: Yes


# AttackDetailTypeDef

### AttackId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### SubResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.SubResourceSummaryTypeDef]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### AttackCounters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.SummarizedCounterTypeDef]]

### AttackProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.AttackPropertyTypeDef]]

### Mitigations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.MitigationTypeDef]]


# AttackPropertyTypeDef

### AttackLayer
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'NETWORK']]

### AttackPropertyIdentifier
- **Type**: typing.Optional[typing.Literal['DESTINATION_URL', 'REFERRER', 'SOURCE_ASN', 'SOURCE_COUNTRY', 'SOURCE_IP_ADDRESS', 'SOURCE_USER_AGENT', 'WORDPRESS_PINGBACK_REFLECTOR', 'WORDPRESS_PINGBACK_SOURCE']]

### TopContributors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.ContributorTypeDef]]

### Unit
- **Type**: typing.Optional[typing.Literal['BITS', 'BYTES', 'PACKETS', 'REQUESTS']]

### Total
- **Type**: typing.Optional[int]


# AttackStatisticsDataItemTypeDef

### AttackCount
- **Type**: <class 'int'>
- **Required**: Yes

### AttackVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.AttackVolumeTypeDef]


# AttackSummaryTypeDef

### AttackId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### AttackVectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.AttackVectorDescriptionTypeDef]]


# AttackVectorDescriptionTypeDef

### VectorType
- **Type**: <class 'str'>
- **Required**: Yes


# AttackVolumeStatisticsTypeDef

### Max
- **Type**: <class 'float'>
- **Required**: Yes


# AttackVolumeTypeDef

### BitsPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.AttackVolumeStatisticsTypeDef]

### PacketsPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.AttackVolumeStatisticsTypeDef]

### RequestsPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.AttackVolumeStatisticsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContributorTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[int]


# CreateProtectionGroupRequestRequestTypeDef

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Aggregation
- **Type**: typing.Literal['MAX', 'MEAN', 'SUM']
- **Required**: Yes

### Pattern
- **Type**: typing.Literal['ALL', 'ARBITRARY', 'BY_RESOURCE_TYPE']
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]

### Members
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.shield_classes.TagTypeDef]]


# CreateProtectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.shield_classes.TagTypeDef]]


# CreateProtectionResponseTypeDef

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProtectionGroupRequestRequestTypeDef

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProtectionRequestRequestTypeDef

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAttackRequestRequestTypeDef

### AttackId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAttackResponseTypeDef

### Attack
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.AttackDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAttackStatisticsResponseTypeDef

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.TimeRangeOutputTypeDef'>
- **Required**: Yes

### DataItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.AttackStatisticsDataItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDRTAccessResponseTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogBucketList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEmergencyContactSettingsResponseTypeDef

### EmergencyContactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.EmergencyContactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProtectionGroupRequestRequestTypeDef

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProtectionGroupResponseTypeDef

### ProtectionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ProtectionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProtectionRequestRequestTypeDef

### ProtectionId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# DescribeProtectionResponseTypeDef

### Protection
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ProtectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSubscriptionResponseTypeDef

### Subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.SubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableApplicationLayerAutomaticResponseRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateDRTLogBucketRequestRequestTypeDef

### LogBucket
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateHealthCheckRequestRequestTypeDef

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmergencyContactTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: typing.Optional[str]

### ContactNotes
- **Type**: typing.Optional[str]


# EnableApplicationLayerAutomaticResponseRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseActionTypeDef'>
- **Required**: Yes


# GetSubscriptionStateResponseTypeDef

### SubscriptionState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InclusionProtectionFiltersTypeDef

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ProtectionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]]


# InclusionProtectionGroupFiltersTypeDef

### ProtectionGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Patterns
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ARBITRARY', 'BY_RESOURCE_TYPE']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]]

### Aggregations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['MAX', 'MEAN', 'SUM']]]


# LimitTypeDef

### Type
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[int]


# ListAttacksRequestListAttacksPaginateTypeDef

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.TimeRangeTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.TimeRangeTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.PaginatorConfigTypeDef]


# ListAttacksRequestRequestTypeDef

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.TimeRangeTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.TimeRangeTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAttacksResponseTypeDef

### AttackSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.AttackSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectionGroupsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### InclusionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.InclusionProtectionGroupFiltersTypeDef]


# ListProtectionGroupsResponseTypeDef

### ProtectionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.ProtectionGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectionsRequestListProtectionsPaginateTypeDef

### InclusionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.InclusionProtectionFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.PaginatorConfigTypeDef]


# ListProtectionsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### InclusionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.InclusionProtectionFiltersTypeDef]


# ListProtectionsResponseTypeDef

### Protections
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.ProtectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesInProtectionGroupRequestRequestTypeDef

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourcesInProtectionGroupResponseTypeDef

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MitigationTypeDef

### MitigationName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProtectionGroupArbitraryPatternLimitsTypeDef

### MaxMembers
- **Type**: <class 'int'>
- **Required**: Yes


# ProtectionGroupLimitsTypeDef

### MaxProtectionGroups
- **Type**: <class 'int'>
- **Required**: Yes

### PatternTypeLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ProtectionGroupPatternTypeLimitsTypeDef'>
- **Required**: Yes


# ProtectionGroupPatternTypeLimitsTypeDef

### ArbitraryPatternLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ProtectionGroupArbitraryPatternLimitsTypeDef'>
- **Required**: Yes


# ProtectionGroupTypeDef

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Aggregation
- **Type**: typing.Literal['MAX', 'MEAN', 'SUM']
- **Required**: Yes

### Pattern
- **Type**: typing.Literal['ALL', 'ARBITRARY', 'BY_RESOURCE_TYPE']
- **Required**: Yes

### Members
- **Type**: typing.List[str]
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]

### ProtectionGroupArn
- **Type**: typing.Optional[str]


# ProtectionLimitsTypeDef

### ProtectedResourceTypeLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield_classes.LimitTypeDef]
- **Required**: Yes


# ProtectionTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### HealthCheckIds
- **Type**: typing.Optional[typing.List[str]]

### ProtectionArn
- **Type**: typing.Optional[str]

### ApplicationLayerAutomaticResponseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield_classes.ApplicationLayerAutomaticResponseConfigurationTypeDef]


# ResponseActionExtraOutputTypeDef

### Block
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Count
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ResponseActionOutputTypeDef

### Block
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Count
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ResponseActionTypeDef

### Block
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Count
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# SubResourceSummaryTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['IP', 'URL']]

### Id
- **Type**: typing.Optional[str]

### AttackVectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.SummarizedAttackVectorTypeDef]]

### Counters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.SummarizedCounterTypeDef]]


# SubscriptionLimitsTypeDef

### ProtectionLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ProtectionLimitsTypeDef'>
- **Required**: Yes

### ProtectionGroupLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ProtectionGroupLimitsTypeDef'>
- **Required**: Yes


# SubscriptionTypeDef

### SubscriptionLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.SubscriptionLimitsTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### TimeCommitmentInSeconds
- **Type**: typing.Optional[int]

### AutoRenew
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Limits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.LimitTypeDef]]

### ProactiveEngagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PENDING']]

### SubscriptionArn
- **Type**: typing.Optional[str]


# SummarizedAttackVectorTypeDef

### VectorType
- **Type**: <class 'str'>
- **Required**: Yes

### VectorCounters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield_classes.SummarizedCounterTypeDef]]


# SummarizedCounterTypeDef

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[float]

### Average
- **Type**: typing.Optional[float]

### Sum
- **Type**: typing.Optional[float]

### N
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.shield_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TimeRangeOutputTypeDef

### FromInclusive
- **Type**: typing.Optional[datetime.datetime]

### ToExclusive
- **Type**: typing.Optional[datetime.datetime]


# TimeRangeTypeDef

### FromInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ToExclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.shield_classes.ResponseActionTypeDef'>
- **Required**: Yes


# UpdateEmergencyContactSettingsRequestRequestTypeDef

### EmergencyContactList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.shield_classes.EmergencyContactTypeDef]]


# UpdateProtectionGroupRequestRequestTypeDef

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Aggregation
- **Type**: typing.Literal['MAX', 'MEAN', 'SUM']
- **Required**: Yes

### Pattern
- **Type**: typing.Literal['ALL', 'ARBITRARY', 'BY_RESOURCE_TYPE']
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]

### Members
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateSubscriptionRequestRequestTypeDef

### AutoRenew
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


