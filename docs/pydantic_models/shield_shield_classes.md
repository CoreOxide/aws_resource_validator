# Shield Shield Classes

# ApplicationLayerAutomaticResponseConfiguration

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseActionOutput'>
- **Required**: Yes


# AssociateDRTLogBucketRequest

### LogBucket
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateDRTRoleRequest

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateHealthCheckRequest

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateProactiveEngagementDetailsRequest

### EmergencyContactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.EmergencyContact]
- **Required**: Yes


# AttackDetail

### AttackId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### SubResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.SubResourceSummary]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### AttackCounters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.SummarizedCounter]]

### AttackProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.AttackProperty]]

### Mitigations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Mitigation]]


# AttackProperty

### AttackLayer
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'NETWORK']]

### AttackPropertyIdentifier
- **Type**: typing.Optional[typing.Literal['DESTINATION_URL', 'REFERRER', 'SOURCE_ASN', 'SOURCE_COUNTRY', 'SOURCE_IP_ADDRESS', 'SOURCE_USER_AGENT', 'WORDPRESS_PINGBACK_REFLECTOR', 'WORDPRESS_PINGBACK_SOURCE']]

### TopContributors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Contributor]]

### Unit
- **Type**: typing.Optional[typing.Literal['BITS', 'BYTES', 'PACKETS', 'REQUESTS']]

### Total
- **Type**: typing.Optional[int]


# AttackStatisticsDataItem

### AttackCount
- **Type**: <class 'int'>
- **Required**: Yes

### AttackVolume
- **Type**: <class 'NoneType'>


# AttackSummary

### AttackId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### AttackVectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.AttackVectorDescription]]


# AttackVectorDescription

### VectorType
- **Type**: <class 'str'>
- **Required**: Yes


# AttackVolume

### BitsPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.AttackVolumeStatistics]

### PacketsPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.AttackVolumeStatistics]

### RequestsPerSecond
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.AttackVolumeStatistics]


# AttackVolumeStatistics

### Max
- **Type**: <class 'float'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Contributor

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[int]


# CreateProtectionGroupRequest

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
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Tag]]


# CreateProtectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Tag]]


# CreateProtectionResponse

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProtectionGroupRequest

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProtectionRequest

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAttackRequest

### AttackId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAttackResponse

### Attack
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.AttackDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAttackStatisticsResponse

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.TimeRangeOutput'>
- **Required**: Yes

### DataItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.AttackStatisticsDataItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDRTAccessResponse

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogBucketList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEmergencyContactSettingsResponse

### EmergencyContactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.EmergencyContact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProtectionGroupRequest

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProtectionGroupResponse

### ProtectionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ProtectionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProtectionRequest

### ProtectionId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# DescribeProtectionResponse

### Protection
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.Protection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSubscriptionResponse

### Subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.Subscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# DisableApplicationLayerAutomaticResponseRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateDRTLogBucketRequest

### LogBucket
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateHealthCheckRequest

### ProtectionId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmergencyContact

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: typing.Optional[str]

### ContactNotes
- **Type**: typing.Optional[str]


# EnableApplicationLayerAutomaticResponseRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.shield.shield_classes.ResponseAction, aws_resource_validator.pydantic_models.shield.shield_classes.ResponseActionOutput]
- **Required**: Yes


# GetSubscriptionStateResponse

### SubscriptionState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# InclusionProtectionFilters

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ProtectionNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]]


# InclusionProtectionGroupFilters

### ProtectionGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Patterns
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ARBITRARY', 'BY_RESOURCE_TYPE']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['APPLICATION_LOAD_BALANCER', 'CLASSIC_LOAD_BALANCER', 'CLOUDFRONT_DISTRIBUTION', 'ELASTIC_IP_ALLOCATION', 'GLOBAL_ACCELERATOR', 'ROUTE_53_HOSTED_ZONE']]]

### Aggregations
- **Type**: typing.Optional[typing.List[typing.Literal['MAX', 'MEAN', 'SUM']]]


# Limit

### Type
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[int]


# ListAttacksRequest

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Union[aws_resource_validator.pydantic_models.shield.shield_classes.TimeRange, aws_resource_validator.pydantic_models.shield.shield_classes.TimeRangeOutput, NoneType]

### EndTime
- **Type**: typing.Union[aws_resource_validator.pydantic_models.shield.shield_classes.TimeRange, aws_resource_validator.pydantic_models.shield.shield_classes.TimeRangeOutput, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAttacksRequestPaginate

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Union[aws_resource_validator.pydantic_models.shield.shield_classes.TimeRange, aws_resource_validator.pydantic_models.shield.shield_classes.TimeRangeOutput, NoneType]

### EndTime
- **Type**: typing.Union[aws_resource_validator.pydantic_models.shield.shield_classes.TimeRange, aws_resource_validator.pydantic_models.shield.shield_classes.TimeRangeOutput, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.PaginatorConfig]


# ListAttacksResponse

### AttackSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.AttackSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectionGroupsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### InclusionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.InclusionProtectionGroupFilters]


# ListProtectionGroupsResponse

### ProtectionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.ProtectionGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectionsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### InclusionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.InclusionProtectionFilters]


# ListProtectionsRequestPaginate

### InclusionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.InclusionProtectionFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.shield.shield_classes.PaginatorConfig]


# ListProtectionsResponse

### Protections
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Protection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesInProtectionGroupRequest

### ProtectionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourcesInProtectionGroupResponse

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ResponseMetadata'>
- **Required**: Yes


# Mitigation

### MitigationName
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Protection

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
- **Type**: <class 'NoneType'>


# ProtectionGroup

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


# ProtectionGroupArbitraryPatternLimits

### MaxMembers
- **Type**: <class 'int'>
- **Required**: Yes


# ProtectionGroupLimits

### MaxProtectionGroups
- **Type**: <class 'int'>
- **Required**: Yes

### PatternTypeLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ProtectionGroupPatternTypeLimits'>
- **Required**: Yes


# ProtectionGroupPatternTypeLimits

### ArbitraryPatternLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ProtectionGroupArbitraryPatternLimits'>
- **Required**: Yes


# ProtectionLimits

### ProtectedResourceTypeLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Limit]
- **Required**: Yes


# ResponseAction

### Block
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Count
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ResponseActionOutput

### Block
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Count
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ResponseMetadata

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


# SubResourceSummary

### Type
- **Type**: typing.Optional[typing.Literal['IP', 'URL']]

### Id
- **Type**: typing.Optional[str]

### AttackVectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.SummarizedAttackVector]]

### Counters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.SummarizedCounter]]


# Subscription

### SubscriptionLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.SubscriptionLimits'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Limit]]

### ProactiveEngagementStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PENDING']]

### SubscriptionArn
- **Type**: typing.Optional[str]


# SubscriptionLimits

### ProtectionLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ProtectionLimits'>
- **Required**: Yes

### ProtectionGroupLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.shield.shield_classes.ProtectionGroupLimits'>
- **Required**: Yes


# SummarizedAttackVector

### VectorType
- **Type**: <class 'str'>
- **Required**: Yes

### VectorCounters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.SummarizedCounter]]


# SummarizedCounter

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


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.Tag]
- **Required**: Yes


# TimeRange

### FromInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ToExclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TimeRangeOutput

### FromInclusive
- **Type**: typing.Optional[datetime.datetime]

### ToExclusive
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationLayerAutomaticResponseRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.shield.shield_classes.ResponseAction, aws_resource_validator.pydantic_models.shield.shield_classes.ResponseActionOutput]
- **Required**: Yes


# UpdateEmergencyContactSettingsRequest

### EmergencyContactList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.shield.shield_classes.EmergencyContact]]


# UpdateProtectionGroupRequest

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
- **Type**: typing.Optional[typing.List[str]]


# UpdateSubscriptionRequest

### AutoRenew
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


