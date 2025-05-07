# Ce Classes

# AnalysisDetails

### SavingsPlansPurchaseAnalysisDetails
- **Type**: <class 'NoneType'>


# AnalysisSummary

### EstimatedCompletionTime
- **Type**: typing.Optional[str]

### AnalysisCompletionTime
- **Type**: typing.Optional[str]

### AnalysisStartedTime
- **Type**: typing.Optional[str]

### AnalysisStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_FAILURE', 'INVALID_ACCOUNT_ID', 'INVALID_SAVINGS_PLANS_TO_ADD', 'INVALID_SAVINGS_PLANS_TO_EXCLUDE', 'NO_USAGE_FOUND']]

### AnalysisId
- **Type**: typing.Optional[str]

### CommitmentPurchaseAnalysisConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.CommitmentPurchaseAnalysisConfigurationOutput]


# Anomaly

### AnomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyScore
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.AnomalyScore'>
- **Required**: Yes

### Impact
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.Impact'>
- **Required**: Yes

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyStartDate
- **Type**: typing.Optional[str]

### AnomalyEndDate
- **Type**: typing.Optional[str]

### DimensionValue
- **Type**: typing.Optional[str]

### RootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.RootCause]]

### Feedback
- **Type**: typing.Optional[typing.Literal['NO', 'PLANNED_ACTIVITY', 'YES']]


# AnomalyDateInterval

### StartDate
- **Type**: <class 'str'>
- **Required**: Yes

### EndDate
- **Type**: typing.Optional[str]


# AnomalyMonitor

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorType
- **Type**: typing.Literal['CUSTOM', 'DIMENSIONAL']
- **Required**: Yes

### MonitorArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### LastEvaluatedDate
- **Type**: typing.Optional[str]

### MonitorDimension
- **Type**: typing.Optional[typing.Literal['SERVICE']]

### MonitorSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.Expression]

### DimensionalValueCount
- **Type**: typing.Optional[int]


# AnomalyMonitorOutput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorType
- **Type**: typing.Literal['CUSTOM', 'DIMENSIONAL']
- **Required**: Yes

### MonitorArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### LastEvaluatedDate
- **Type**: typing.Optional[str]

### MonitorDimension
- **Type**: typing.Optional[typing.Literal['SERVICE']]

### MonitorSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput]

### DimensionalValueCount
- **Type**: typing.Optional[int]


# AnomalyScore

### MaxScore
- **Type**: <class 'float'>
- **Required**: Yes

### CurrentScore
- **Type**: <class 'float'>
- **Required**: Yes


# AnomalySubscription

### MonitorArnList
- **Type**: typing.List[str]
- **Required**: Yes

### Subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.Subscriber]
- **Required**: Yes

### Frequency
- **Type**: typing.Literal['DAILY', 'IMMEDIATE', 'WEEKLY']
- **Required**: Yes

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionArn
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.Expression]


# AnomalySubscriptionOutput

### MonitorArnList
- **Type**: typing.List[str]
- **Required**: Yes

### Subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.Subscriber]
- **Required**: Yes

### Frequency
- **Type**: typing.Literal['DAILY', 'IMMEDIATE', 'WEEKLY']
- **Required**: Yes

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionArn
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitmentPurchaseAnalysisConfiguration

### SavingsPlansPurchaseAnalysisConfiguration
- **Type**: <class 'NoneType'>


# CommitmentPurchaseAnalysisConfigurationOutput

### SavingsPlansPurchaseAnalysisConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansPurchaseAnalysisConfigurationOutput]


# CostAllocationTag

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AWSGenerated', 'UserDefined']
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### LastUpdatedDate
- **Type**: typing.Optional[str]

### LastUsedDate
- **Type**: typing.Optional[str]


# CostAllocationTagBackfillRequest

### BackfillFrom
- **Type**: typing.Optional[str]

### RequestedAt
- **Type**: typing.Optional[str]

### CompletedAt
- **Type**: typing.Optional[str]

### BackfillStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### LastUpdatedAt
- **Type**: typing.Optional[str]


# CostAllocationTagStatusEntry

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes


# CostCategory

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveStart
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleVersion
- **Type**: typing.Literal['CostCategoryExpression.v1']
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryRuleOutput]
- **Required**: Yes

### EffectiveEnd
- **Type**: typing.Optional[str]

### SplitChargeRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRuleOutput]]

### ProcessingStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryProcessingStatus]]

### DefaultValue
- **Type**: typing.Optional[str]


# CostCategoryInheritedValueDimension

### DimensionName
- **Type**: typing.Optional[typing.Literal['LINKED_ACCOUNT_NAME', 'TAG']]

### DimensionKey
- **Type**: typing.Optional[str]


# CostCategoryProcessingStatus

### Component
- **Type**: typing.Optional[typing.Literal['COST_EXPLORER']]

### Status
- **Type**: typing.Optional[typing.Literal['APPLIED', 'PROCESSING']]


# CostCategoryReference

### CostCategoryArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### EffectiveStart
- **Type**: typing.Optional[str]

### EffectiveEnd
- **Type**: typing.Optional[str]

### NumberOfRules
- **Type**: typing.Optional[int]

### ProcessingStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryProcessingStatus]]

### Values
- **Type**: typing.Optional[typing.List[str]]

### DefaultValue
- **Type**: typing.Optional[str]


# CostCategoryRule

### Value
- **Type**: typing.Optional[str]

### Rule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### InheritedValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryInheritedValueDimension]

### Type
- **Type**: typing.Optional[typing.Literal['INHERITED_VALUE', 'REGULAR']]


# CostCategoryRuleOutput

### Value
- **Type**: typing.Optional[str]

### Rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput]

### InheritedValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryInheritedValueDimension]

### Type
- **Type**: typing.Optional[typing.Literal['INHERITED_VALUE', 'REGULAR']]


# CostCategorySplitChargeRule

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### Method
- **Type**: typing.Literal['EVEN', 'FIXED', 'PROPORTIONAL']
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRuleParameter, aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRuleParameterOutput]]]


# CostCategorySplitChargeRuleOutput

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### Method
- **Type**: typing.Literal['EVEN', 'FIXED', 'PROPORTIONAL']
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRuleParameterOutput]]


# CostCategorySplitChargeRuleParameter

### Type
- **Type**: typing.Literal['ALLOCATION_PERCENTAGES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CostCategorySplitChargeRuleParameterOutput

### Type
- **Type**: typing.Literal['ALLOCATION_PERCENTAGES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CostCategoryValues

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# CostCategoryValuesOutput

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# Coverage

### CoverageHours
- **Type**: <class 'NoneType'>

### CoverageNormalizedUnits
- **Type**: <class 'NoneType'>

### CoverageCost
- **Type**: <class 'NoneType'>


# CoverageByTime

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationCoverageGroup]]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.Coverage]


# CoverageCost

### OnDemandCost
- **Type**: typing.Optional[str]


# CoverageHours

### OnDemandHours
- **Type**: typing.Optional[str]

### ReservedHours
- **Type**: typing.Optional[str]

### TotalRunningHours
- **Type**: typing.Optional[str]

### CoverageHoursPercentage
- **Type**: typing.Optional[str]


# CoverageNormalizedUnits

### OnDemandNormalizedUnits
- **Type**: typing.Optional[str]

### ReservedNormalizedUnits
- **Type**: typing.Optional[str]

### TotalRunningNormalizedUnits
- **Type**: typing.Optional[str]

### CoverageNormalizedUnitsPercentage
- **Type**: typing.Optional[str]


# CreateAnomalyMonitorRequest

### AnomalyMonitor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.AnomalyMonitor, aws_resource_validator.pydantic_models.ce.ce_classes.AnomalyMonitorOutput]
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResourceTag]]


# CreateAnomalyMonitorResponse

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAnomalySubscriptionRequest

### AnomalySubscription
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.AnomalySubscription, aws_resource_validator.pydantic_models.ce.ce_classes.AnomalySubscriptionOutput]
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResourceTag]]


# CreateAnomalySubscriptionResponse

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCostCategoryDefinitionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleVersion
- **Type**: typing.Literal['CostCategoryExpression.v1']
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryRule, aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryRuleOutput]]
- **Required**: Yes

### EffectiveStart
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### SplitChargeRules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRule, aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRuleOutput]]]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResourceTag]]


# CreateCostCategoryDefinitionResponse

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveStart
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# CurrentInstance

### ResourceId
- **Type**: typing.Optional[str]

### InstanceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.TagValuesOutput]]

### ResourceDetails
- **Type**: <class 'NoneType'>

### ResourceUtilization
- **Type**: <class 'NoneType'>

### ReservationCoveredHoursInLookbackPeriod
- **Type**: typing.Optional[str]

### SavingsPlansCoveredHoursInLookbackPeriod
- **Type**: typing.Optional[str]

### OnDemandHoursInLookbackPeriod
- **Type**: typing.Optional[str]

### TotalRunningHoursInLookbackPeriod
- **Type**: typing.Optional[str]

### MonthlyCost
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]


# DateInterval

### Start
- **Type**: <class 'str'>
- **Required**: Yes

### End
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnomalyMonitorRequest

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnomalySubscriptionRequest

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCostCategoryDefinitionRequest

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCostCategoryDefinitionResponse

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveEnd
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCostCategoryDefinitionRequest

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveOn
- **Type**: typing.Optional[str]


# DescribeCostCategoryDefinitionResponse

### CostCategory
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.CostCategory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# DimensionValues

### Key
- **Type**: typing.Optional[typing.Literal['AGREEMENT_END_DATE_TIME_AFTER', 'AGREEMENT_END_DATE_TIME_BEFORE', 'ANOMALY_TOTAL_IMPACT_ABSOLUTE', 'ANOMALY_TOTAL_IMPACT_PERCENTAGE', 'AZ', 'BILLING_ENTITY', 'CACHE_ENGINE', 'DATABASE_ENGINE', 'DEPLOYMENT_OPTION', 'INSTANCE_TYPE', 'INSTANCE_TYPE_FAMILY', 'INVOICING_ENTITY', 'LEGAL_ENTITY_NAME', 'LINKED_ACCOUNT', 'LINKED_ACCOUNT_NAME', 'OPERATING_SYSTEM', 'OPERATION', 'PAYMENT_OPTION', 'PLATFORM', 'PURCHASE_TYPE', 'RECORD_TYPE', 'REGION', 'RESERVATION_ID', 'RESOURCE_ID', 'RIGHTSIZING_TYPE', 'SAVINGS_PLANS_TYPE', 'SAVINGS_PLAN_ARN', 'SCOPE', 'SERVICE', 'SERVICE_CODE', 'SUBSCRIPTION_ID', 'TENANCY', 'USAGE_TYPE', 'USAGE_TYPE_GROUP']]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# DimensionValuesOutput

### Key
- **Type**: typing.Optional[typing.Literal['AGREEMENT_END_DATE_TIME_AFTER', 'AGREEMENT_END_DATE_TIME_BEFORE', 'ANOMALY_TOTAL_IMPACT_ABSOLUTE', 'ANOMALY_TOTAL_IMPACT_PERCENTAGE', 'AZ', 'BILLING_ENTITY', 'CACHE_ENGINE', 'DATABASE_ENGINE', 'DEPLOYMENT_OPTION', 'INSTANCE_TYPE', 'INSTANCE_TYPE_FAMILY', 'INVOICING_ENTITY', 'LEGAL_ENTITY_NAME', 'LINKED_ACCOUNT', 'LINKED_ACCOUNT_NAME', 'OPERATING_SYSTEM', 'OPERATION', 'PAYMENT_OPTION', 'PLATFORM', 'PURCHASE_TYPE', 'RECORD_TYPE', 'REGION', 'RESERVATION_ID', 'RESOURCE_ID', 'RIGHTSIZING_TYPE', 'SAVINGS_PLANS_TYPE', 'SAVINGS_PLAN_ARN', 'SCOPE', 'SERVICE', 'SERVICE_CODE', 'SUBSCRIPTION_ID', 'TENANCY', 'USAGE_TYPE', 'USAGE_TYPE_GROUP']]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# DimensionValuesWithAttributes

### Value
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# DiskResourceUtilization

### DiskReadOpsPerSecond
- **Type**: typing.Optional[str]

### DiskWriteOpsPerSecond
- **Type**: typing.Optional[str]

### DiskReadBytesPerSecond
- **Type**: typing.Optional[str]

### DiskWriteBytesPerSecond
- **Type**: typing.Optional[str]


# DynamoDBCapacityDetails

### CapacityUnits
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# EBSResourceUtilization

### EbsReadOpsPerSecond
- **Type**: typing.Optional[str]

### EbsWriteOpsPerSecond
- **Type**: typing.Optional[str]

### EbsReadBytesPerSecond
- **Type**: typing.Optional[str]

### EbsWriteBytesPerSecond
- **Type**: typing.Optional[str]


# EC2InstanceDetails

### Family
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[str]

### Tenancy
- **Type**: typing.Optional[str]

### CurrentGeneration
- **Type**: typing.Optional[bool]

### SizeFlexEligible
- **Type**: typing.Optional[bool]


# EC2ResourceDetails

### HourlyOnDemandRate
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Sku
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### NetworkPerformance
- **Type**: typing.Optional[str]

### Storage
- **Type**: typing.Optional[str]

### Vcpu
- **Type**: typing.Optional[str]


# EC2ResourceUtilization

### MaxCpuUtilizationPercentage
- **Type**: typing.Optional[str]

### MaxMemoryUtilizationPercentage
- **Type**: typing.Optional[str]

### MaxStorageUtilizationPercentage
- **Type**: typing.Optional[str]

### EBSResourceUtilization
- **Type**: <class 'NoneType'>

### DiskResourceUtilization
- **Type**: <class 'NoneType'>

### NetworkResourceUtilization
- **Type**: <class 'NoneType'>


# EC2Specification

### OfferingClass
- **Type**: typing.Optional[typing.Literal['CONVERTIBLE', 'STANDARD']]


# ESInstanceDetails

### InstanceClass
- **Type**: typing.Optional[str]

### InstanceSize
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### CurrentGeneration
- **Type**: typing.Optional[bool]

### SizeFlexEligible
- **Type**: typing.Optional[bool]


# ElastiCacheInstanceDetails

### Family
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### CurrentGeneration
- **Type**: typing.Optional[bool]

### SizeFlexEligible
- **Type**: typing.Optional[bool]


# Expression

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### And
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Not
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Dimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.DimensionValues, aws_resource_validator.pydantic_models.ce.ce_classes.DimensionValuesOutput, NoneType]

### Tags
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.TagValues, aws_resource_validator.pydantic_models.ce.ce_classes.TagValuesOutput, NoneType]

### CostCategories
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryValues, aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryValuesOutput, NoneType]


# ExpressionOutput

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### And
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Not
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.DimensionValuesOutput]

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.TagValuesOutput]

### CostCategories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryValuesOutput]


# ForecastResult

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval]

### MeanValue
- **Type**: typing.Optional[str]

### PredictionIntervalLowerBound
- **Type**: typing.Optional[str]

### PredictionIntervalUpperBound
- **Type**: typing.Optional[str]


# GenerationSummary

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### GenerationStartedTime
- **Type**: typing.Optional[str]

### GenerationCompletionTime
- **Type**: typing.Optional[str]

### EstimatedCompletionTime
- **Type**: typing.Optional[str]


# GetAnomaliesRequest

### DateInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.AnomalyDateInterval'>
- **Required**: Yes

### MonitorArn
- **Type**: typing.Optional[str]

### Feedback
- **Type**: typing.Optional[typing.Literal['NO', 'PLANNED_ACTIVITY', 'YES']]

### TotalImpact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.TotalImpactFilter]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnomaliesResponse

### Anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.Anomaly]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetAnomalyMonitorsRequest

### MonitorArnList
- **Type**: typing.Optional[typing.List[str]]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnomalyMonitorsResponse

### AnomalyMonitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.AnomalyMonitorOutput]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetAnomalySubscriptionsRequest

### SubscriptionArnList
- **Type**: typing.Optional[typing.List[str]]

### MonitorArn
- **Type**: typing.Optional[str]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnomalySubscriptionsResponse

### AnomalySubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.AnomalySubscriptionOutput]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetApproximateUsageRecordsRequest

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### ApproximationDimension
- **Type**: typing.Literal['RESOURCE', 'SERVICE']
- **Required**: Yes

### Services
- **Type**: typing.Optional[typing.List[str]]


# GetApproximateUsageRecordsResponse

### Services
- **Type**: typing.Dict[str, int]
- **Required**: Yes

### TotalRecords
- **Type**: <class 'int'>
- **Required**: Yes

### LookbackPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetCommitmentPurchaseAnalysisRequest

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommitmentPurchaseAnalysisResponse

### EstimatedCompletionTime
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisCompletionTime
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisStartedTime
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisStatus
- **Type**: typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['INTERNAL_FAILURE', 'INVALID_ACCOUNT_ID', 'INVALID_SAVINGS_PLANS_TO_ADD', 'INVALID_SAVINGS_PLANS_TO_EXCLUDE', 'NO_USAGE_FOUND']
- **Required**: Yes

### AnalysisDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.AnalysisDetails'>
- **Required**: Yes

### CommitmentPurchaseAnalysisConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.CommitmentPurchaseAnalysisConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetCostAndUsageRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Metrics
- **Type**: typing.List[str]
- **Required**: Yes

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]]

### BillingViewArn
- **Type**: typing.Optional[str]

### NextPageToken
- **Type**: typing.Optional[str]


# GetCostAndUsageResponse

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### GroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]
- **Required**: Yes

### ResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResultByTime]
- **Required**: Yes

### DimensionValueAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.DimensionValuesWithAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetCostAndUsageWithResourcesRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput]
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[typing.List[str]]

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]]

### BillingViewArn
- **Type**: typing.Optional[str]

### NextPageToken
- **Type**: typing.Optional[str]


# GetCostAndUsageWithResourcesResponse

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### GroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]
- **Required**: Yes

### ResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResultByTime]
- **Required**: Yes

### DimensionValueAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.DimensionValuesWithAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetCostCategoriesRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### SearchString
- **Type**: typing.Optional[str]

### CostCategoryName
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### SortBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]]

### BillingViewArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetCostCategoriesResponse

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### CostCategoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### CostCategoryValues
- **Type**: typing.List[str]
- **Required**: Yes

### ReturnSize
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetCostForecastRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Metric
- **Type**: typing.Literal['AMORTIZED_COST', 'BLENDED_COST', 'NET_AMORTIZED_COST', 'NET_UNBLENDED_COST', 'NORMALIZED_USAGE_AMOUNT', 'UNBLENDED_COST', 'USAGE_QUANTITY']
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### BillingViewArn
- **Type**: typing.Optional[str]

### PredictionIntervalLevel
- **Type**: typing.Optional[int]


# GetCostForecastResponse

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.MetricValue'>
- **Required**: Yes

### ForecastResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ForecastResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetDimensionValuesRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Dimension
- **Type**: typing.Literal['AGREEMENT_END_DATE_TIME_AFTER', 'AGREEMENT_END_DATE_TIME_BEFORE', 'ANOMALY_TOTAL_IMPACT_ABSOLUTE', 'ANOMALY_TOTAL_IMPACT_PERCENTAGE', 'AZ', 'BILLING_ENTITY', 'CACHE_ENGINE', 'DATABASE_ENGINE', 'DEPLOYMENT_OPTION', 'INSTANCE_TYPE', 'INSTANCE_TYPE_FAMILY', 'INVOICING_ENTITY', 'LEGAL_ENTITY_NAME', 'LINKED_ACCOUNT', 'LINKED_ACCOUNT_NAME', 'OPERATING_SYSTEM', 'OPERATION', 'PAYMENT_OPTION', 'PLATFORM', 'PURCHASE_TYPE', 'RECORD_TYPE', 'REGION', 'RESERVATION_ID', 'RESOURCE_ID', 'RIGHTSIZING_TYPE', 'SAVINGS_PLANS_TYPE', 'SAVINGS_PLAN_ARN', 'SCOPE', 'SERVICE', 'SERVICE_CODE', 'SUBSCRIPTION_ID', 'TENANCY', 'USAGE_TYPE', 'USAGE_TYPE_GROUP']
- **Required**: Yes

### SearchString
- **Type**: typing.Optional[str]

### Context
- **Type**: typing.Optional[typing.Literal['COST_AND_USAGE', 'RESERVATIONS', 'SAVINGS_PLANS']]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### SortBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]]

### BillingViewArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetDimensionValuesResponse

### DimensionValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.DimensionValuesWithAttributes]
- **Required**: Yes

### ReturnSize
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSize
- **Type**: <class 'int'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetReservationCoverageRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]]

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### Metrics
- **Type**: typing.Optional[typing.List[str]]

### NextPageToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]

### MaxResults
- **Type**: typing.Optional[int]


# GetReservationCoverageResponse

### CoveragesByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CoverageByTime]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.Coverage'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetReservationPurchaseRecommendationRequest

### Service
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### ServiceSpecification
- **Type**: <class 'NoneType'>

### PageSize
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetReservationPurchaseRecommendationResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ReservationPurchaseRecommendationMetadata'>
- **Required**: Yes

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationPurchaseRecommendation]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetReservationUtilizationRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]]

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetReservationUtilizationResponse

### UtilizationsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.UtilizationByTime]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ReservationAggregates'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetRightsizingRecommendationRequest

### Service
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.RightsizingRecommendationConfiguration]

### PageSize
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetRightsizingRecommendationResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.RightsizingRecommendationMetadata'>
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.RightsizingRecommendationSummary'>
- **Required**: Yes

### RightsizingRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.RightsizingRecommendation]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.RightsizingRecommendationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetSavingsPlanPurchaseRecommendationDetailsRequest

### RecommendationDetailId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSavingsPlanPurchaseRecommendationDetailsResponse

### RecommendationDetailId
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationDetailData
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.RecommendationDetailData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetSavingsPlansCoverageRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GroupDefinition]]

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### Metrics
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]


# GetSavingsPlansCoverageResponse

### SavingsPlansCoverages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansCoverage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSavingsPlansPurchaseRecommendationRequest

### SavingsPlansType
- **Type**: typing.Literal['COMPUTE_SP', 'EC2_INSTANCE_SP', 'SAGEMAKER_SP']
- **Required**: Yes

### TermInYears
- **Type**: typing.Literal['ONE_YEAR', 'THREE_YEARS']
- **Required**: Yes

### PaymentOption
- **Type**: typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']
- **Required**: Yes

### LookbackPeriodInDays
- **Type**: typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']
- **Required**: Yes

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### NextPageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]


# GetSavingsPlansPurchaseRecommendationResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansPurchaseRecommendationMetadata'>
- **Required**: Yes

### SavingsPlansPurchaseRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansPurchaseRecommendation'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetSavingsPlansUtilizationDetailsRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### DataType
- **Type**: typing.Optional[typing.List[typing.Literal['AMORTIZED_COMMITMENT', 'ATTRIBUTES', 'SAVINGS', 'UTILIZATION']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]


# GetSavingsPlansUtilizationDetailsResponse

### SavingsPlansUtilizationDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilizationDetail]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilizationAggregates'>
- **Required**: Yes

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSavingsPlansUtilizationRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]


# GetSavingsPlansUtilizationResponse

### SavingsPlansUtilizationsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilizationByTime]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilizationAggregates'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetTagsRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### SearchString
- **Type**: typing.Optional[str]

### TagKey
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### SortBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SortDefinition]]

### BillingViewArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetTagsResponse

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[str]
- **Required**: Yes

### ReturnSize
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# GetUsageForecastRequest

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Metric
- **Type**: typing.Literal['AMORTIZED_COST', 'BLENDED_COST', 'NET_AMORTIZED_COST', 'NET_UNBLENDED_COST', 'NORMALIZED_USAGE_AMOUNT', 'UNBLENDED_COST', 'USAGE_QUANTITY']
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]

### BillingViewArn
- **Type**: typing.Optional[str]

### PredictionIntervalLevel
- **Type**: typing.Optional[int]


# GetUsageForecastResponse

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.MetricValue'>
- **Required**: Yes

### ForecastResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ForecastResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# Group

### Keys
- **Type**: typing.Optional[typing.List[str]]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ce.ce_classes.MetricValue]]


# GroupDefinition

### Type
- **Type**: typing.Optional[typing.Literal['COST_CATEGORY', 'DIMENSION', 'TAG']]

### Key
- **Type**: typing.Optional[str]


# Impact

### MaxImpact
- **Type**: <class 'float'>
- **Required**: Yes

### TotalImpact
- **Type**: typing.Optional[float]

### TotalActualSpend
- **Type**: typing.Optional[float]

### TotalExpectedSpend
- **Type**: typing.Optional[float]

### TotalImpactPercentage
- **Type**: typing.Optional[float]


# InstanceDetails

### EC2InstanceDetails
- **Type**: <class 'NoneType'>

### RDSInstanceDetails
- **Type**: <class 'NoneType'>

### RedshiftInstanceDetails
- **Type**: <class 'NoneType'>

### ElastiCacheInstanceDetails
- **Type**: <class 'NoneType'>

### ESInstanceDetails
- **Type**: <class 'NoneType'>

### MemoryDBInstanceDetails
- **Type**: <class 'NoneType'>


# ListCommitmentPurchaseAnalysesRequest

### AnalysisStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### NextPageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### AnalysisIds
- **Type**: typing.Optional[typing.List[str]]


# ListCommitmentPurchaseAnalysesResponse

### AnalysisSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.AnalysisSummary]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# ListCostAllocationTagBackfillHistoryRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCostAllocationTagBackfillHistoryResponse

### BackfillRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostAllocationTagBackfillRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCostAllocationTagsRequest

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['AWSGenerated', 'UserDefined']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCostAllocationTagsResponse

### CostAllocationTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostAllocationTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCostCategoryDefinitionsRequest

### EffectiveOn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCostCategoryDefinitionsResponse

### CostCategoryReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryReference]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSavingsPlansPurchaseRecommendationGenerationRequest

### GenerationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### RecommendationIds
- **Type**: typing.Optional[typing.List[str]]

### PageSize
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# ListSavingsPlansPurchaseRecommendationGenerationResponse

### GenerationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.GenerationSummary]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# MemoryDBInstanceDetails

### Family
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### CurrentGeneration
- **Type**: typing.Optional[bool]

### SizeFlexEligible
- **Type**: typing.Optional[bool]


# MetricValue

### Amount
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# ModifyRecommendationDetail

### TargetInstances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.TargetInstance]]


# NetworkResourceUtilization

### NetworkInBytesPerSecond
- **Type**: typing.Optional[str]

### NetworkOutBytesPerSecond
- **Type**: typing.Optional[str]

### NetworkPacketsInPerSecond
- **Type**: typing.Optional[str]

### NetworkPacketsOutPerSecond
- **Type**: typing.Optional[str]


# ProvideAnomalyFeedbackRequest

### AnomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### Feedback
- **Type**: typing.Literal['NO', 'PLANNED_ACTIVITY', 'YES']
- **Required**: Yes


# ProvideAnomalyFeedbackResponse

### AnomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# RDSInstanceDetails

### Family
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### DatabaseEngine
- **Type**: typing.Optional[str]

### DatabaseEdition
- **Type**: typing.Optional[str]

### DeploymentOption
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### CurrentGeneration
- **Type**: typing.Optional[bool]

### SizeFlexEligible
- **Type**: typing.Optional[bool]


# RecommendationDetailData

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### SavingsPlansType
- **Type**: typing.Optional[typing.Literal['COMPUTE_SP', 'EC2_INSTANCE_SP', 'SAGEMAKER_SP']]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### AccountId
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### InstanceFamily
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### OfferingId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### LatestUsageTimestamp
- **Type**: typing.Optional[str]

### CurrentAverageHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentMaximumHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentMinimumHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### EstimatedAverageUtilization
- **Type**: typing.Optional[str]

### EstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### EstimatedOnDemandCost
- **Type**: typing.Optional[str]

### EstimatedOnDemandCostWithCurrentCommitment
- **Type**: typing.Optional[str]

### EstimatedROI
- **Type**: typing.Optional[str]

### EstimatedSPCost
- **Type**: typing.Optional[str]

### EstimatedSavingsAmount
- **Type**: typing.Optional[str]

### EstimatedSavingsPercentage
- **Type**: typing.Optional[str]

### ExistingHourlyCommitment
- **Type**: typing.Optional[str]

### HourlyCommitmentToPurchase
- **Type**: typing.Optional[str]

### UpfrontCost
- **Type**: typing.Optional[str]

### CurrentAverageCoverage
- **Type**: typing.Optional[str]

### EstimatedAverageCoverage
- **Type**: typing.Optional[str]

### MetricsOverLookbackPeriod
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.RecommendationDetailHourlyMetrics]]


# RecommendationDetailHourlyMetrics

### StartTime
- **Type**: typing.Optional[str]

### EstimatedOnDemandCost
- **Type**: typing.Optional[str]

### CurrentCoverage
- **Type**: typing.Optional[str]

### EstimatedCoverage
- **Type**: typing.Optional[str]

### EstimatedNewCommitmentUtilization
- **Type**: typing.Optional[str]


# RedshiftInstanceDetails

### Family
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### CurrentGeneration
- **Type**: typing.Optional[bool]

### SizeFlexEligible
- **Type**: typing.Optional[bool]


# ReservationAggregates

### UtilizationPercentage
- **Type**: typing.Optional[str]

### UtilizationPercentageInUnits
- **Type**: typing.Optional[str]

### PurchasedHours
- **Type**: typing.Optional[str]

### PurchasedUnits
- **Type**: typing.Optional[str]

### TotalActualHours
- **Type**: typing.Optional[str]

### TotalActualUnits
- **Type**: typing.Optional[str]

### UnusedHours
- **Type**: typing.Optional[str]

### UnusedUnits
- **Type**: typing.Optional[str]

### OnDemandCostOfRIHoursUsed
- **Type**: typing.Optional[str]

### NetRISavings
- **Type**: typing.Optional[str]

### TotalPotentialRISavings
- **Type**: typing.Optional[str]

### AmortizedUpfrontFee
- **Type**: typing.Optional[str]

### AmortizedRecurringFee
- **Type**: typing.Optional[str]

### TotalAmortizedFee
- **Type**: typing.Optional[str]

### RICostForUnusedHours
- **Type**: typing.Optional[str]

### RealizedSavings
- **Type**: typing.Optional[str]

### UnrealizedSavings
- **Type**: typing.Optional[str]


# ReservationCoverageGroup

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Coverage
- **Type**: <class 'NoneType'>


# ReservationPurchaseRecommendation

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### ServiceSpecification
- **Type**: <class 'NoneType'>

### RecommendationDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationPurchaseRecommendationDetail]]

### RecommendationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationPurchaseRecommendationSummary]


# ReservationPurchaseRecommendationDetail

### AccountId
- **Type**: typing.Optional[str]

### InstanceDetails
- **Type**: <class 'NoneType'>

### RecommendedNumberOfInstancesToPurchase
- **Type**: typing.Optional[str]

### RecommendedNormalizedUnitsToPurchase
- **Type**: typing.Optional[str]

### MinimumNumberOfInstancesUsedPerHour
- **Type**: typing.Optional[str]

### MinimumNormalizedUnitsUsedPerHour
- **Type**: typing.Optional[str]

### MaximumNumberOfInstancesUsedPerHour
- **Type**: typing.Optional[str]

### MaximumNormalizedUnitsUsedPerHour
- **Type**: typing.Optional[str]

### AverageNumberOfInstancesUsedPerHour
- **Type**: typing.Optional[str]

### AverageNormalizedUnitsUsedPerHour
- **Type**: typing.Optional[str]

### AverageUtilization
- **Type**: typing.Optional[str]

### EstimatedBreakEvenInMonths
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### EstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### EstimatedMonthlySavingsPercentage
- **Type**: typing.Optional[str]

### EstimatedMonthlyOnDemandCost
- **Type**: typing.Optional[str]

### EstimatedReservationCostForLookbackPeriod
- **Type**: typing.Optional[str]

### UpfrontCost
- **Type**: typing.Optional[str]

### RecurringStandardMonthlyCost
- **Type**: typing.Optional[str]

### ReservedCapacityDetails
- **Type**: <class 'NoneType'>

### RecommendedNumberOfCapacityUnitsToPurchase
- **Type**: typing.Optional[str]

### MinimumNumberOfCapacityUnitsUsedPerHour
- **Type**: typing.Optional[str]

### MaximumNumberOfCapacityUnitsUsedPerHour
- **Type**: typing.Optional[str]

### AverageNumberOfCapacityUnitsUsedPerHour
- **Type**: typing.Optional[str]


# ReservationPurchaseRecommendationMetadata

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### AdditionalMetadata
- **Type**: typing.Optional[str]


# ReservationPurchaseRecommendationSummary

### TotalEstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### TotalEstimatedMonthlySavingsPercentage
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]


# ReservationUtilizationGroup

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Utilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationAggregates]


# ReservedCapacityDetails

### DynamoDBCapacityDetails
- **Type**: <class 'NoneType'>


# ResourceDetails

### EC2ResourceDetails
- **Type**: <class 'NoneType'>


# ResourceTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceUtilization

### EC2ResourceUtilization
- **Type**: <class 'NoneType'>


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


# ResultByTime

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval]

### Total
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ce.ce_classes.MetricValue]]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.Group]]

### Estimated
- **Type**: typing.Optional[bool]


# RightsizingRecommendation

### AccountId
- **Type**: typing.Optional[str]

### CurrentInstance
- **Type**: <class 'NoneType'>

### RightsizingType
- **Type**: typing.Optional[typing.Literal['MODIFY', 'TERMINATE']]

### ModifyRecommendationDetail
- **Type**: <class 'NoneType'>

### TerminateRecommendationDetail
- **Type**: <class 'NoneType'>

### FindingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CPU_OVER_PROVISIONED', 'CPU_UNDER_PROVISIONED', 'DISK_IOPS_OVER_PROVISIONED', 'DISK_IOPS_UNDER_PROVISIONED', 'DISK_THROUGHPUT_OVER_PROVISIONED', 'DISK_THROUGHPUT_UNDER_PROVISIONED', 'EBS_IOPS_OVER_PROVISIONED', 'EBS_IOPS_UNDER_PROVISIONED', 'EBS_THROUGHPUT_OVER_PROVISIONED', 'EBS_THROUGHPUT_UNDER_PROVISIONED', 'MEMORY_OVER_PROVISIONED', 'MEMORY_UNDER_PROVISIONED', 'NETWORK_BANDWIDTH_OVER_PROVISIONED', 'NETWORK_BANDWIDTH_UNDER_PROVISIONED', 'NETWORK_PPS_OVER_PROVISIONED', 'NETWORK_PPS_UNDER_PROVISIONED']]]


# RightsizingRecommendationConfiguration

### RecommendationTarget
- **Type**: typing.Literal['CROSS_INSTANCE_FAMILY', 'SAME_INSTANCE_FAMILY']
- **Required**: Yes

### BenefitsConsidered
- **Type**: <class 'bool'>
- **Required**: Yes


# RightsizingRecommendationMetadata

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### AdditionalMetadata
- **Type**: typing.Optional[str]


# RightsizingRecommendationSummary

### TotalRecommendationCount
- **Type**: typing.Optional[str]

### EstimatedTotalMonthlySavingsAmount
- **Type**: typing.Optional[str]

### SavingsCurrencyCode
- **Type**: typing.Optional[str]

### SavingsPercentage
- **Type**: typing.Optional[str]


# RootCause

### Service
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### LinkedAccount
- **Type**: typing.Optional[str]

### LinkedAccountName
- **Type**: typing.Optional[str]

### UsageType
- **Type**: typing.Optional[str]

### Impact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.RootCauseImpact]


# RootCauseImpact

### Contribution
- **Type**: <class 'float'>
- **Required**: Yes


# SavingsPlans

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### SavingsPlansType
- **Type**: typing.Optional[typing.Literal['COMPUTE_SP', 'EC2_INSTANCE_SP', 'SAGEMAKER_SP']]

### Region
- **Type**: typing.Optional[str]

### InstanceFamily
- **Type**: typing.Optional[str]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### SavingsPlansCommitment
- **Type**: typing.Optional[float]

### OfferingId
- **Type**: typing.Optional[str]


# SavingsPlansAmortizedCommitment

### AmortizedRecurringCommitment
- **Type**: typing.Optional[str]

### AmortizedUpfrontCommitment
- **Type**: typing.Optional[str]

### TotalAmortizedCommitment
- **Type**: typing.Optional[str]


# SavingsPlansCoverage

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Coverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansCoverageData]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval]


# SavingsPlansCoverageData

### SpendCoveredBySavingsPlans
- **Type**: typing.Optional[str]

### OnDemandCost
- **Type**: typing.Optional[str]

### TotalCost
- **Type**: typing.Optional[str]

### CoveragePercentage
- **Type**: typing.Optional[str]


# SavingsPlansDetails

### Region
- **Type**: typing.Optional[str]

### InstanceFamily
- **Type**: typing.Optional[str]

### OfferingId
- **Type**: typing.Optional[str]


# SavingsPlansPurchaseAnalysisConfiguration

### AnalysisType
- **Type**: typing.Literal['CUSTOM_COMMITMENT', 'MAX_SAVINGS']
- **Required**: Yes

### SavingsPlansToAdd
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlans]
- **Required**: Yes

### LookBackTimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### AccountId
- **Type**: typing.Optional[str]

### SavingsPlansToExclude
- **Type**: typing.Optional[typing.List[str]]


# SavingsPlansPurchaseAnalysisConfigurationOutput

### AnalysisType
- **Type**: typing.Literal['CUSTOM_COMMITMENT', 'MAX_SAVINGS']
- **Required**: Yes

### SavingsPlansToAdd
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlans]
- **Required**: Yes

### LookBackTimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### AccountId
- **Type**: typing.Optional[str]

### SavingsPlansToExclude
- **Type**: typing.Optional[typing.List[str]]


# SavingsPlansPurchaseAnalysisDetails

### CurrencyCode
- **Type**: typing.Optional[str]

### LookbackPeriodInHours
- **Type**: typing.Optional[str]

### CurrentAverageCoverage
- **Type**: typing.Optional[str]

### CurrentAverageHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentMaximumHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentMinimumHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentOnDemandSpend
- **Type**: typing.Optional[str]

### ExistingHourlyCommitment
- **Type**: typing.Optional[str]

### HourlyCommitmentToPurchase
- **Type**: typing.Optional[str]

### EstimatedAverageCoverage
- **Type**: typing.Optional[str]

### EstimatedAverageUtilization
- **Type**: typing.Optional[str]

### EstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### EstimatedOnDemandCost
- **Type**: typing.Optional[str]

### EstimatedOnDemandCostWithCurrentCommitment
- **Type**: typing.Optional[str]

### EstimatedROI
- **Type**: typing.Optional[str]

### EstimatedSavingsAmount
- **Type**: typing.Optional[str]

### EstimatedSavingsPercentage
- **Type**: typing.Optional[str]

### EstimatedCommitmentCost
- **Type**: typing.Optional[str]

### LatestUsageTimestamp
- **Type**: typing.Optional[str]

### UpfrontCost
- **Type**: typing.Optional[str]

### AdditionalMetadata
- **Type**: typing.Optional[str]

### MetricsOverLookbackPeriod
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.RecommendationDetailHourlyMetrics]]


# SavingsPlansPurchaseRecommendation

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### SavingsPlansType
- **Type**: typing.Optional[typing.Literal['COMPUTE_SP', 'EC2_INSTANCE_SP', 'SAGEMAKER_SP']]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### SavingsPlansPurchaseRecommendationDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansPurchaseRecommendationDetail]]

### SavingsPlansPurchaseRecommendationSummary
- **Type**: <class 'NoneType'>


# SavingsPlansPurchaseRecommendationDetail

### SavingsPlansDetails
- **Type**: <class 'NoneType'>

### AccountId
- **Type**: typing.Optional[str]

### UpfrontCost
- **Type**: typing.Optional[str]

### EstimatedROI
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### EstimatedSPCost
- **Type**: typing.Optional[str]

### EstimatedOnDemandCost
- **Type**: typing.Optional[str]

### EstimatedOnDemandCostWithCurrentCommitment
- **Type**: typing.Optional[str]

### EstimatedSavingsAmount
- **Type**: typing.Optional[str]

### EstimatedSavingsPercentage
- **Type**: typing.Optional[str]

### HourlyCommitmentToPurchase
- **Type**: typing.Optional[str]

### EstimatedAverageUtilization
- **Type**: typing.Optional[str]

### EstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### CurrentMinimumHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentMaximumHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### CurrentAverageHourlyOnDemandSpend
- **Type**: typing.Optional[str]

### RecommendationDetailId
- **Type**: typing.Optional[str]


# SavingsPlansPurchaseRecommendationMetadata

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### AdditionalMetadata
- **Type**: typing.Optional[str]


# SavingsPlansPurchaseRecommendationSummary

### EstimatedROI
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### EstimatedTotalCost
- **Type**: typing.Optional[str]

### CurrentOnDemandSpend
- **Type**: typing.Optional[str]

### EstimatedSavingsAmount
- **Type**: typing.Optional[str]

### TotalRecommendationCount
- **Type**: typing.Optional[str]

### DailyCommitmentToPurchase
- **Type**: typing.Optional[str]

### HourlyCommitmentToPurchase
- **Type**: typing.Optional[str]

### EstimatedSavingsPercentage
- **Type**: typing.Optional[str]

### EstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### EstimatedOnDemandCostWithCurrentCommitment
- **Type**: typing.Optional[str]


# SavingsPlansSavings

### NetSavings
- **Type**: typing.Optional[str]

### OnDemandCostEquivalent
- **Type**: typing.Optional[str]


# SavingsPlansUtilization

### TotalCommitment
- **Type**: typing.Optional[str]

### UsedCommitment
- **Type**: typing.Optional[str]

### UnusedCommitment
- **Type**: typing.Optional[str]

### UtilizationPercentage
- **Type**: typing.Optional[str]


# SavingsPlansUtilizationAggregates

### Utilization
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilization'>
- **Required**: Yes

### Savings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansSavings]

### AmortizedCommitment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansAmortizedCommitment]


# SavingsPlansUtilizationByTime

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval'>
- **Required**: Yes

### Utilization
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilization'>
- **Required**: Yes

### Savings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansSavings]

### AmortizedCommitment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansAmortizedCommitment]


# SavingsPlansUtilizationDetail

### SavingsPlanArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Utilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansUtilization]

### Savings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansSavings]

### AmortizedCommitment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.SavingsPlansAmortizedCommitment]


# ServiceSpecification

### EC2Specification
- **Type**: <class 'NoneType'>


# SortDefinition

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# StartCommitmentPurchaseAnalysisRequest

### CommitmentPurchaseAnalysisConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CommitmentPurchaseAnalysisConfiguration, aws_resource_validator.pydantic_models.ce.ce_classes.CommitmentPurchaseAnalysisConfigurationOutput]
- **Required**: Yes


# StartCommitmentPurchaseAnalysisResponse

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisStartedTime
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedCompletionTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# StartCostAllocationTagBackfillRequest

### BackfillFrom
- **Type**: <class 'str'>
- **Required**: Yes


# StartCostAllocationTagBackfillResponse

### BackfillRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.CostAllocationTagBackfillRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# StartSavingsPlansPurchaseRecommendationGenerationResponse

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### GenerationStartedTime
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedCompletionTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# Subscriber

### Address
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SNS']]

### Status
- **Type**: typing.Optional[typing.Literal['CONFIRMED', 'DECLINED']]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ResourceTag]
- **Required**: Yes


# TagValues

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# TagValuesOutput

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# TargetInstance

### EstimatedMonthlyCost
- **Type**: typing.Optional[str]

### EstimatedMonthlySavings
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### DefaultTargetInstance
- **Type**: typing.Optional[bool]

### ResourceDetails
- **Type**: <class 'NoneType'>

### ExpectedResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ResourceUtilization]

### PlatformDifferences
- **Type**: typing.Optional[typing.List[typing.Literal['HYPERVISOR', 'INSTANCE_STORE_AVAILABILITY', 'NETWORK_INTERFACE', 'STORAGE_INTERFACE', 'VIRTUALIZATION_TYPE']]]


# TerminateRecommendationDetail

### EstimatedMonthlySavings
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]


# TotalImpactFilter

### NumericOperator
- **Type**: typing.Literal['BETWEEN', 'EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL']
- **Required**: Yes

### StartValue
- **Type**: <class 'float'>
- **Required**: Yes

### EndValue
- **Type**: typing.Optional[float]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAnomalyMonitorRequest

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorName
- **Type**: typing.Optional[str]


# UpdateAnomalyMonitorResponse

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAnomalySubscriptionRequest

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Threshold
- **Type**: typing.Optional[float]

### Frequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'IMMEDIATE', 'WEEKLY']]

### MonitorArnList
- **Type**: typing.Optional[typing.List[str]]

### Subscribers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.Subscriber]]

### SubscriptionName
- **Type**: typing.Optional[str]

### ThresholdExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.Expression, aws_resource_validator.pydantic_models.ce.ce_classes.ExpressionOutput, NoneType]


# UpdateAnomalySubscriptionResponse

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCostAllocationTagsStatusError

### TagKey
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# UpdateCostAllocationTagsStatusRequest

### CostAllocationTagsStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.CostAllocationTagStatusEntry]
- **Required**: Yes


# UpdateCostAllocationTagsStatusResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.UpdateCostAllocationTagsStatusError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCostCategoryDefinitionRequest

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleVersion
- **Type**: typing.Literal['CostCategoryExpression.v1']
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryRule, aws_resource_validator.pydantic_models.ce.ce_classes.CostCategoryRuleOutput]]
- **Required**: Yes

### EffectiveStart
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### SplitChargeRules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRule, aws_resource_validator.pydantic_models.ce.ce_classes.CostCategorySplitChargeRuleOutput]]]


# UpdateCostCategoryDefinitionResponse

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveStart
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce.ce_classes.ResponseMetadata'>
- **Required**: Yes


# UtilizationByTime

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.DateInterval]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationUtilizationGroup]]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce.ce_classes.ReservationAggregates]


