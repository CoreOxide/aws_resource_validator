# Ce Classes

# AnalysisDetailsTypeDef

### SavingsPlansPurchaseAnalysisDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseAnalysisDetailsTypeDef]


# AnalysisSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CommitmentPurchaseAnalysisConfigurationOutputTypeDef]


# AnomalyDateIntervalTypeDef

### StartDate
- **Type**: <class 'str'>
- **Required**: Yes

### EndDate
- **Type**: typing.Optional[str]


# AnomalyMonitorOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionOutputTypeDef]

### DimensionalValueCount
- **Type**: typing.Optional[int]


# AnomalyMonitorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionTypeDef]

### DimensionalValueCount
- **Type**: typing.Optional[int]


# AnomalyMonitorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnomalyScoreTypeDef

### MaxScore
- **Type**: <class 'float'>
- **Required**: Yes

### CurrentScore
- **Type**: <class 'float'>
- **Required**: Yes


# AnomalySubscriptionOutputTypeDef

### MonitorArnList
- **Type**: typing.List[str]
- **Required**: Yes

### Subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.SubscriberTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionOutputTypeDef]


# AnomalySubscriptionTypeDef

### MonitorArnList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subscribers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.SubscriberTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionTypeDef]


# AnomalySubscriptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnomalyTypeDef

### AnomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyScore
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.AnomalyScoreTypeDef'>
- **Required**: Yes

### Impact
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ImpactTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.RootCauseTypeDef]]

### Feedback
- **Type**: typing.Optional[typing.Literal['NO', 'PLANNED_ACTIVITY', 'YES']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitmentPurchaseAnalysisConfigurationOutputTypeDef

### SavingsPlansPurchaseAnalysisConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef]


# CommitmentPurchaseAnalysisConfigurationTypeDef

### SavingsPlansPurchaseAnalysisConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseAnalysisConfigurationTypeDef]


# CommitmentPurchaseAnalysisConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostAllocationTagBackfillRequestTypeDef

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


# CostAllocationTagStatusEntryTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes


# CostAllocationTagTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostCategoryInheritedValueDimensionTypeDef

### DimensionName
- **Type**: typing.Optional[typing.Literal['LINKED_ACCOUNT_NAME', 'TAG']]

### DimensionKey
- **Type**: typing.Optional[str]


# CostCategoryProcessingStatusTypeDef

### Component
- **Type**: typing.Optional[typing.Literal['COST_EXPLORER']]

### Status
- **Type**: typing.Optional[typing.Literal['APPLIED', 'PROCESSING']]


# CostCategoryReferenceTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.CostCategoryProcessingStatusTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[str]]

### DefaultValue
- **Type**: typing.Optional[str]


# CostCategoryRuleOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostCategoryRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostCategorySplitChargeRuleOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.CostCategorySplitChargeRuleParameterOutputTypeDef]]


# CostCategorySplitChargeRuleParameterOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostCategorySplitChargeRuleParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostCategorySplitChargeRuleTypeDef

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Method
- **Type**: typing.Literal['EVEN', 'FIXED', 'PROPORTIONAL']
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.CostCategorySplitChargeRuleParameterUnionTypeDef]]


# CostCategorySplitChargeRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostCategoryTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.CostCategoryRuleOutputTypeDef]
- **Required**: Yes

### EffectiveEnd
- **Type**: typing.Optional[str]

### SplitChargeRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.CostCategorySplitChargeRuleOutputTypeDef]]

### ProcessingStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.CostCategoryProcessingStatusTypeDef]]

### DefaultValue
- **Type**: typing.Optional[str]


# CostCategoryValuesOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# CostCategoryValuesTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# CostCategoryValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoverageByTimeTypeDef

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.ReservationCoverageGroupTypeDef]]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CoverageTypeDef]


# CoverageCostTypeDef

### OnDemandCost
- **Type**: typing.Optional[str]


# CoverageHoursTypeDef

### OnDemandHours
- **Type**: typing.Optional[str]

### ReservedHours
- **Type**: typing.Optional[str]

### TotalRunningHours
- **Type**: typing.Optional[str]

### CoverageHoursPercentage
- **Type**: typing.Optional[str]


# CoverageNormalizedUnitsTypeDef

### OnDemandNormalizedUnits
- **Type**: typing.Optional[str]

### ReservedNormalizedUnits
- **Type**: typing.Optional[str]

### TotalRunningNormalizedUnits
- **Type**: typing.Optional[str]

### CoverageNormalizedUnitsPercentage
- **Type**: typing.Optional[str]


# CoverageTypeDef

### CoverageHours
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CoverageHoursTypeDef]

### CoverageNormalizedUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CoverageNormalizedUnitsTypeDef]

### CoverageCost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CoverageCostTypeDef]


# CreateAnomalyMonitorRequestTypeDef

### AnomalyMonitor
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.AnomalyMonitorUnionTypeDef'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.ResourceTagTypeDef]]


# CreateAnomalyMonitorResponseTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAnomalySubscriptionRequestTypeDef

### AnomalySubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.AnomalySubscriptionUnionTypeDef'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.ResourceTagTypeDef]]


# CreateAnomalySubscriptionResponseTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCostCategoryDefinitionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleVersion
- **Type**: typing.Literal['CostCategoryExpression.v1']
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.CostCategoryRuleUnionTypeDef]
- **Required**: Yes

### EffectiveStart
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### SplitChargeRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.CostCategorySplitChargeRuleUnionTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.ResourceTagTypeDef]]


# CreateCostCategoryDefinitionResponseTypeDef

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveStart
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CurrentInstanceTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### InstanceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.TagValuesOutputTypeDef]]

### ResourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ResourceDetailsTypeDef]

### ResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ResourceUtilizationTypeDef]

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


# DateIntervalTypeDef

### Start
- **Type**: <class 'str'>
- **Required**: Yes

### End
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnomalyMonitorRequestTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnomalySubscriptionRequestTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCostCategoryDefinitionRequestTypeDef

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCostCategoryDefinitionResponseTypeDef

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveEnd
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCostCategoryDefinitionRequestTypeDef

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveOn
- **Type**: typing.Optional[str]


# DescribeCostCategoryDefinitionResponseTypeDef

### CostCategory
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.CostCategoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionValuesOutputTypeDef

### Key
- **Type**: typing.Optional[typing.Literal['AGREEMENT_END_DATE_TIME_AFTER', 'AGREEMENT_END_DATE_TIME_BEFORE', 'ANOMALY_TOTAL_IMPACT_ABSOLUTE', 'ANOMALY_TOTAL_IMPACT_PERCENTAGE', 'AZ', 'BILLING_ENTITY', 'CACHE_ENGINE', 'DATABASE_ENGINE', 'DEPLOYMENT_OPTION', 'INSTANCE_TYPE', 'INSTANCE_TYPE_FAMILY', 'INVOICING_ENTITY', 'LEGAL_ENTITY_NAME', 'LINKED_ACCOUNT', 'LINKED_ACCOUNT_NAME', 'OPERATING_SYSTEM', 'OPERATION', 'PAYMENT_OPTION', 'PLATFORM', 'PURCHASE_TYPE', 'RECORD_TYPE', 'REGION', 'RESERVATION_ID', 'RESOURCE_ID', 'RIGHTSIZING_TYPE', 'SAVINGS_PLANS_TYPE', 'SAVINGS_PLAN_ARN', 'SCOPE', 'SERVICE', 'SERVICE_CODE', 'SUBSCRIPTION_ID', 'TENANCY', 'USAGE_TYPE', 'USAGE_TYPE_GROUP']]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# DimensionValuesTypeDef

### Key
- **Type**: typing.Optional[typing.Literal['AGREEMENT_END_DATE_TIME_AFTER', 'AGREEMENT_END_DATE_TIME_BEFORE', 'ANOMALY_TOTAL_IMPACT_ABSOLUTE', 'ANOMALY_TOTAL_IMPACT_PERCENTAGE', 'AZ', 'BILLING_ENTITY', 'CACHE_ENGINE', 'DATABASE_ENGINE', 'DEPLOYMENT_OPTION', 'INSTANCE_TYPE', 'INSTANCE_TYPE_FAMILY', 'INVOICING_ENTITY', 'LEGAL_ENTITY_NAME', 'LINKED_ACCOUNT', 'LINKED_ACCOUNT_NAME', 'OPERATING_SYSTEM', 'OPERATION', 'PAYMENT_OPTION', 'PLATFORM', 'PURCHASE_TYPE', 'RECORD_TYPE', 'REGION', 'RESERVATION_ID', 'RESOURCE_ID', 'RIGHTSIZING_TYPE', 'SAVINGS_PLANS_TYPE', 'SAVINGS_PLAN_ARN', 'SCOPE', 'SERVICE', 'SERVICE_CODE', 'SUBSCRIPTION_ID', 'TENANCY', 'USAGE_TYPE', 'USAGE_TYPE_GROUP']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# DimensionValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DimensionValuesWithAttributesTypeDef

### Value
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# DiskResourceUtilizationTypeDef

### DiskReadOpsPerSecond
- **Type**: typing.Optional[str]

### DiskWriteOpsPerSecond
- **Type**: typing.Optional[str]

### DiskReadBytesPerSecond
- **Type**: typing.Optional[str]

### DiskWriteBytesPerSecond
- **Type**: typing.Optional[str]


# DynamoDBCapacityDetailsTypeDef

### CapacityUnits
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# EBSResourceUtilizationTypeDef

### EbsReadOpsPerSecond
- **Type**: typing.Optional[str]

### EbsWriteOpsPerSecond
- **Type**: typing.Optional[str]

### EbsReadBytesPerSecond
- **Type**: typing.Optional[str]

### EbsWriteBytesPerSecond
- **Type**: typing.Optional[str]


# EC2InstanceDetailsTypeDef

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


# EC2ResourceDetailsTypeDef

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


# EC2ResourceUtilizationTypeDef

### MaxCpuUtilizationPercentage
- **Type**: typing.Optional[str]

### MaxMemoryUtilizationPercentage
- **Type**: typing.Optional[str]

### MaxStorageUtilizationPercentage
- **Type**: typing.Optional[str]

### EBSResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.EBSResourceUtilizationTypeDef]

### DiskResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DiskResourceUtilizationTypeDef]

### NetworkResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.NetworkResourceUtilizationTypeDef]


# EC2SpecificationTypeDef

### OfferingClass
- **Type**: typing.Optional[typing.Literal['CONVERTIBLE', 'STANDARD']]


# ESInstanceDetailsTypeDef

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


# ElastiCacheInstanceDetailsTypeDef

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


# ExpressionOutputTypeDef

### Or
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### And
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Not
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DimensionValuesOutputTypeDef]

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.TagValuesOutputTypeDef]

### CostCategories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CostCategoryValuesOutputTypeDef]


# ExpressionTypeDef

### Or
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### And
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### Not
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DimensionValuesUnionTypeDef]

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.TagValuesUnionTypeDef]

### CostCategories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CostCategoryValuesUnionTypeDef]


# ExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ForecastResultTypeDef

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef]

### MeanValue
- **Type**: typing.Optional[str]

### PredictionIntervalLowerBound
- **Type**: typing.Optional[str]

### PredictionIntervalUpperBound
- **Type**: typing.Optional[str]


# GenerationSummaryTypeDef

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


# GetAnomaliesRequestTypeDef

### DateInterval
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.AnomalyDateIntervalTypeDef'>
- **Required**: Yes

### MonitorArn
- **Type**: typing.Optional[str]

### Feedback
- **Type**: typing.Optional[typing.Literal['NO', 'PLANNED_ACTIVITY', 'YES']]

### TotalImpact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.TotalImpactFilterTypeDef]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnomaliesResponseTypeDef

### Anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.AnomalyTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnomalyMonitorsRequestTypeDef

### MonitorArnList
- **Type**: typing.Optional[typing.Sequence[str]]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnomalyMonitorsResponseTypeDef

### AnomalyMonitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.AnomalyMonitorOutputTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAnomalySubscriptionsRequestTypeDef

### SubscriptionArnList
- **Type**: typing.Optional[typing.Sequence[str]]

### MonitorArn
- **Type**: typing.Optional[str]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnomalySubscriptionsResponseTypeDef

### AnomalySubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.AnomalySubscriptionOutputTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApproximateUsageRecordsRequestTypeDef

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### ApproximationDimension
- **Type**: typing.Literal['RESOURCE', 'SERVICE']
- **Required**: Yes

### Services
- **Type**: typing.Optional[typing.Sequence[str]]


# GetApproximateUsageRecordsResponseTypeDef

### Services
- **Type**: typing.Dict[str, int]
- **Required**: Yes

### TotalRecords
- **Type**: <class 'int'>
- **Required**: Yes

### LookbackPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCommitmentPurchaseAnalysisRequestTypeDef

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommitmentPurchaseAnalysisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.AnalysisDetailsTypeDef'>
- **Required**: Yes

### CommitmentPurchaseAnalysisConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.CommitmentPurchaseAnalysisConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCostAndUsageRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Metrics
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]]

### BillingViewArn
- **Type**: typing.Optional[str]

### NextPageToken
- **Type**: typing.Optional[str]


# GetCostAndUsageResponseTypeDef

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### GroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]
- **Required**: Yes

### ResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.ResultByTimeTypeDef]
- **Required**: Yes

### DimensionValueAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.DimensionValuesWithAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCostAndUsageWithResourcesRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[typing.Sequence[str]]

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]]

### BillingViewArn
- **Type**: typing.Optional[str]

### NextPageToken
- **Type**: typing.Optional[str]


# GetCostAndUsageWithResourcesResponseTypeDef

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### GroupDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]
- **Required**: Yes

### ResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.ResultByTimeTypeDef]
- **Required**: Yes

### DimensionValueAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.DimensionValuesWithAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCostCategoriesRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### SearchString
- **Type**: typing.Optional[str]

### CostCategoryName
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]]

### BillingViewArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetCostCategoriesResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCostForecastRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Metric
- **Type**: typing.Literal['AMORTIZED_COST', 'BLENDED_COST', 'NET_AMORTIZED_COST', 'NET_UNBLENDED_COST', 'NORMALIZED_USAGE_AMOUNT', 'UNBLENDED_COST', 'USAGE_QUANTITY']
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### BillingViewArn
- **Type**: typing.Optional[str]

### PredictionIntervalLevel
- **Type**: typing.Optional[int]


# GetCostForecastResponseTypeDef

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.MetricValueTypeDef'>
- **Required**: Yes

### ForecastResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.ForecastResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDimensionValuesRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Dimension
- **Type**: typing.Literal['AGREEMENT_END_DATE_TIME_AFTER', 'AGREEMENT_END_DATE_TIME_BEFORE', 'ANOMALY_TOTAL_IMPACT_ABSOLUTE', 'ANOMALY_TOTAL_IMPACT_PERCENTAGE', 'AZ', 'BILLING_ENTITY', 'CACHE_ENGINE', 'DATABASE_ENGINE', 'DEPLOYMENT_OPTION', 'INSTANCE_TYPE', 'INSTANCE_TYPE_FAMILY', 'INVOICING_ENTITY', 'LEGAL_ENTITY_NAME', 'LINKED_ACCOUNT', 'LINKED_ACCOUNT_NAME', 'OPERATING_SYSTEM', 'OPERATION', 'PAYMENT_OPTION', 'PLATFORM', 'PURCHASE_TYPE', 'RECORD_TYPE', 'REGION', 'RESERVATION_ID', 'RESOURCE_ID', 'RIGHTSIZING_TYPE', 'SAVINGS_PLANS_TYPE', 'SAVINGS_PLAN_ARN', 'SCOPE', 'SERVICE', 'SERVICE_CODE', 'SUBSCRIPTION_ID', 'TENANCY', 'USAGE_TYPE', 'USAGE_TYPE_GROUP']
- **Required**: Yes

### SearchString
- **Type**: typing.Optional[str]

### Context
- **Type**: typing.Optional[typing.Literal['COST_AND_USAGE', 'RESERVATIONS', 'SAVINGS_PLANS']]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]]

### BillingViewArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetDimensionValuesResponseTypeDef

### DimensionValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.DimensionValuesWithAttributesTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReservationCoverageRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]]

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Sequence[str]]

### NextPageToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]

### MaxResults
- **Type**: typing.Optional[int]


# GetReservationCoverageResponseTypeDef

### CoveragesByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.CoverageByTimeTypeDef]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.CoverageTypeDef'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReservationPurchaseRecommendationRequestTypeDef

### Service
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### ServiceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ServiceSpecificationTypeDef]

### PageSize
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetReservationPurchaseRecommendationResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ReservationPurchaseRecommendationMetadataTypeDef'>
- **Required**: Yes

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.ReservationPurchaseRecommendationTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReservationUtilizationRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]]

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]

### NextPageToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetReservationUtilizationResponseTypeDef

### UtilizationsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.UtilizationByTimeTypeDef]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ReservationAggregatesTypeDef'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRightsizingRecommendationRequestTypeDef

### Service
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.RightsizingRecommendationConfigurationTypeDef]

### PageSize
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetRightsizingRecommendationResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.RightsizingRecommendationMetadataTypeDef'>
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.RightsizingRecommendationSummaryTypeDef'>
- **Required**: Yes

### RightsizingRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.RightsizingRecommendationTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.RightsizingRecommendationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef

### RecommendationDetailId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef

### RecommendationDetailId
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationDetailData
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.RecommendationDetailDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSavingsPlansCoverageRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.GroupDefinitionTypeDef]]

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]


# GetSavingsPlansCoverageResponseTypeDef

### SavingsPlansCoverages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansCoverageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSavingsPlansPurchaseRecommendationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]


# GetSavingsPlansPurchaseRecommendationResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseRecommendationMetadataTypeDef'>
- **Required**: Yes

### SavingsPlansPurchaseRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseRecommendationTypeDef'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSavingsPlansUtilizationDetailsRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### DataType
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AMORTIZED_COMMITMENT', 'ATTRIBUTES', 'SAVINGS', 'UTILIZATION']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]


# GetSavingsPlansUtilizationDetailsResponseTypeDef

### SavingsPlansUtilizationDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationDetailTypeDef]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationAggregatesTypeDef'>
- **Required**: Yes

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSavingsPlansUtilizationRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Granularity
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY']]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### SortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]


# GetSavingsPlansUtilizationResponseTypeDef

### SavingsPlansUtilizationsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationByTimeTypeDef]
- **Required**: Yes

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationAggregatesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTagsRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### SearchString
- **Type**: typing.Optional[str]

### TagKey
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.SortDefinitionTypeDef]]

### BillingViewArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# GetTagsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUsageForecastRequestTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Metric
- **Type**: typing.Literal['AMORTIZED_COST', 'BLENDED_COST', 'NET_AMORTIZED_COST', 'NET_UNBLENDED_COST', 'NORMALIZED_USAGE_AMOUNT', 'UNBLENDED_COST', 'USAGE_QUANTITY']
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MONTHLY']
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]

### BillingViewArn
- **Type**: typing.Optional[str]

### PredictionIntervalLevel
- **Type**: typing.Optional[int]


# GetUsageForecastResponseTypeDef

### Total
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.MetricValueTypeDef'>
- **Required**: Yes

### ForecastResultsByTime
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.ForecastResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GroupTypeDef

### Keys
- **Type**: typing.Optional[typing.List[str]]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ce_classes.MetricValueTypeDef]]


# ImpactTypeDef

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


# InstanceDetailsTypeDef

### EC2InstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.EC2InstanceDetailsTypeDef]

### RDSInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.RDSInstanceDetailsTypeDef]

### RedshiftInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.RedshiftInstanceDetailsTypeDef]

### ElastiCacheInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ElastiCacheInstanceDetailsTypeDef]

### ESInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ESInstanceDetailsTypeDef]

### MemoryDBInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.MemoryDBInstanceDetailsTypeDef]


# ListCommitmentPurchaseAnalysesRequestTypeDef

### AnalysisStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### NextPageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### AnalysisIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListCommitmentPurchaseAnalysesResponseTypeDef

### AnalysisSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.AnalysisSummaryTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCostAllocationTagBackfillHistoryRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCostAllocationTagBackfillHistoryResponseTypeDef

### BackfillRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.CostAllocationTagBackfillRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCostAllocationTagsResponseTypeDef

### CostAllocationTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.CostAllocationTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCostCategoryDefinitionsRequestTypeDef

### EffectiveOn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCostCategoryDefinitionsResponseTypeDef

### CostCategoryReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.CostCategoryReferenceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef

### GenerationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCEEDED']]

### RecommendationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PageSize
- **Type**: typing.Optional[int]

### NextPageToken
- **Type**: typing.Optional[str]


# ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef

### GenerationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.GenerationSummaryTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MemoryDBInstanceDetailsTypeDef

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


# MetricValueTypeDef

### Amount
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# ModifyRecommendationDetailTypeDef

### TargetInstances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.TargetInstanceTypeDef]]


# NetworkResourceUtilizationTypeDef

### NetworkInBytesPerSecond
- **Type**: typing.Optional[str]

### NetworkOutBytesPerSecond
- **Type**: typing.Optional[str]

### NetworkPacketsInPerSecond
- **Type**: typing.Optional[str]

### NetworkPacketsOutPerSecond
- **Type**: typing.Optional[str]


# ProvideAnomalyFeedbackRequestTypeDef

### AnomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### Feedback
- **Type**: typing.Literal['NO', 'PLANNED_ACTIVITY', 'YES']
- **Required**: Yes


# ProvideAnomalyFeedbackResponseTypeDef

### AnomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RDSInstanceDetailsTypeDef

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


# RecommendationDetailDataTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.RecommendationDetailHourlyMetricsTypeDef]]


# RecommendationDetailHourlyMetricsTypeDef

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


# RedshiftInstanceDetailsTypeDef

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


# ReservationAggregatesTypeDef

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


# ReservationCoverageGroupTypeDef

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Coverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CoverageTypeDef]


# ReservationPurchaseRecommendationDetailTypeDef

### AccountId
- **Type**: typing.Optional[str]

### InstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.InstanceDetailsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ReservedCapacityDetailsTypeDef]

### RecommendedNumberOfCapacityUnitsToPurchase
- **Type**: typing.Optional[str]

### MinimumNumberOfCapacityUnitsUsedPerHour
- **Type**: typing.Optional[str]

### MaximumNumberOfCapacityUnitsUsedPerHour
- **Type**: typing.Optional[str]

### AverageNumberOfCapacityUnitsUsedPerHour
- **Type**: typing.Optional[str]


# ReservationPurchaseRecommendationMetadataTypeDef

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### AdditionalMetadata
- **Type**: typing.Optional[str]


# ReservationPurchaseRecommendationSummaryTypeDef

### TotalEstimatedMonthlySavingsAmount
- **Type**: typing.Optional[str]

### TotalEstimatedMonthlySavingsPercentage
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]


# ReservationPurchaseRecommendationTypeDef

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### TermInYears
- **Type**: typing.Optional[typing.Literal['ONE_YEAR', 'THREE_YEARS']]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'HEAVY_UTILIZATION', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### ServiceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ServiceSpecificationTypeDef]

### RecommendationDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.ReservationPurchaseRecommendationDetailTypeDef]]

### RecommendationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ReservationPurchaseRecommendationSummaryTypeDef]


# ReservationUtilizationGroupTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Utilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ReservationAggregatesTypeDef]


# ReservedCapacityDetailsTypeDef

### DynamoDBCapacityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DynamoDBCapacityDetailsTypeDef]


# ResourceDetailsTypeDef

### EC2ResourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.EC2ResourceDetailsTypeDef]


# ResourceTagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceUtilizationTypeDef

### EC2ResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.EC2ResourceUtilizationTypeDef]


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


# ResultByTimeTypeDef

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef]

### Total
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ce_classes.MetricValueTypeDef]]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.GroupTypeDef]]

### Estimated
- **Type**: typing.Optional[bool]


# RightsizingRecommendationConfigurationTypeDef

### RecommendationTarget
- **Type**: typing.Literal['CROSS_INSTANCE_FAMILY', 'SAME_INSTANCE_FAMILY']
- **Required**: Yes

### BenefitsConsidered
- **Type**: <class 'bool'>
- **Required**: Yes


# RightsizingRecommendationMetadataTypeDef

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### LookbackPeriodInDays
- **Type**: typing.Optional[typing.Literal['SEVEN_DAYS', 'SIXTY_DAYS', 'THIRTY_DAYS']]

### AdditionalMetadata
- **Type**: typing.Optional[str]


# RightsizingRecommendationSummaryTypeDef

### TotalRecommendationCount
- **Type**: typing.Optional[str]

### EstimatedTotalMonthlySavingsAmount
- **Type**: typing.Optional[str]

### SavingsCurrencyCode
- **Type**: typing.Optional[str]

### SavingsPercentage
- **Type**: typing.Optional[str]


# RightsizingRecommendationTypeDef

### AccountId
- **Type**: typing.Optional[str]

### CurrentInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.CurrentInstanceTypeDef]

### RightsizingType
- **Type**: typing.Optional[typing.Literal['MODIFY', 'TERMINATE']]

### ModifyRecommendationDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ModifyRecommendationDetailTypeDef]

### TerminateRecommendationDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.TerminateRecommendationDetailTypeDef]

### FindingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CPU_OVER_PROVISIONED', 'CPU_UNDER_PROVISIONED', 'DISK_IOPS_OVER_PROVISIONED', 'DISK_IOPS_UNDER_PROVISIONED', 'DISK_THROUGHPUT_OVER_PROVISIONED', 'DISK_THROUGHPUT_UNDER_PROVISIONED', 'EBS_IOPS_OVER_PROVISIONED', 'EBS_IOPS_UNDER_PROVISIONED', 'EBS_THROUGHPUT_OVER_PROVISIONED', 'EBS_THROUGHPUT_UNDER_PROVISIONED', 'MEMORY_OVER_PROVISIONED', 'MEMORY_UNDER_PROVISIONED', 'NETWORK_BANDWIDTH_OVER_PROVISIONED', 'NETWORK_BANDWIDTH_UNDER_PROVISIONED', 'NETWORK_PPS_OVER_PROVISIONED', 'NETWORK_PPS_UNDER_PROVISIONED']]]


# RootCauseImpactTypeDef

### Contribution
- **Type**: <class 'float'>
- **Required**: Yes


# RootCauseTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.RootCauseImpactTypeDef]


# SavingsPlansAmortizedCommitmentTypeDef

### AmortizedRecurringCommitment
- **Type**: typing.Optional[str]

### AmortizedUpfrontCommitment
- **Type**: typing.Optional[str]

### TotalAmortizedCommitment
- **Type**: typing.Optional[str]


# SavingsPlansCoverageDataTypeDef

### SpendCoveredBySavingsPlans
- **Type**: typing.Optional[str]

### OnDemandCost
- **Type**: typing.Optional[str]

### TotalCost
- **Type**: typing.Optional[str]

### CoveragePercentage
- **Type**: typing.Optional[str]


# SavingsPlansCoverageTypeDef

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Coverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansCoverageDataTypeDef]

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef]


# SavingsPlansDetailsTypeDef

### Region
- **Type**: typing.Optional[str]

### InstanceFamily
- **Type**: typing.Optional[str]

### OfferingId
- **Type**: typing.Optional[str]


# SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef

### AnalysisType
- **Type**: typing.Literal['CUSTOM_COMMITMENT', 'MAX_SAVINGS']
- **Required**: Yes

### SavingsPlansToAdd
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansTypeDef]
- **Required**: Yes

### LookBackTimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### AccountId
- **Type**: typing.Optional[str]

### SavingsPlansToExclude
- **Type**: typing.Optional[typing.List[str]]


# SavingsPlansPurchaseAnalysisConfigurationTypeDef

### AnalysisType
- **Type**: typing.Literal['CUSTOM_COMMITMENT', 'MAX_SAVINGS']
- **Required**: Yes

### SavingsPlansToAdd
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansTypeDef]
- **Required**: Yes

### LookBackTimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### AccountScope
- **Type**: typing.Optional[typing.Literal['LINKED', 'PAYER']]

### AccountId
- **Type**: typing.Optional[str]

### SavingsPlansToExclude
- **Type**: typing.Optional[typing.Sequence[str]]


# SavingsPlansPurchaseAnalysisDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.RecommendationDetailHourlyMetricsTypeDef]]


# SavingsPlansPurchaseRecommendationDetailTypeDef

### SavingsPlansDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansDetailsTypeDef]

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


# SavingsPlansPurchaseRecommendationMetadataTypeDef

### RecommendationId
- **Type**: typing.Optional[str]

### GenerationTimestamp
- **Type**: typing.Optional[str]

### AdditionalMetadata
- **Type**: typing.Optional[str]


# SavingsPlansPurchaseRecommendationSummaryTypeDef

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


# SavingsPlansPurchaseRecommendationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseRecommendationDetailTypeDef]]

### SavingsPlansPurchaseRecommendationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansPurchaseRecommendationSummaryTypeDef]


# SavingsPlansSavingsTypeDef

### NetSavings
- **Type**: typing.Optional[str]

### OnDemandCostEquivalent
- **Type**: typing.Optional[str]


# SavingsPlansTypeDef

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


# SavingsPlansUtilizationAggregatesTypeDef

### Utilization
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationTypeDef'>
- **Required**: Yes

### Savings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansSavingsTypeDef]

### AmortizedCommitment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansAmortizedCommitmentTypeDef]


# SavingsPlansUtilizationByTimeTypeDef

### TimePeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef'>
- **Required**: Yes

### Utilization
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationTypeDef'>
- **Required**: Yes

### Savings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansSavingsTypeDef]

### AmortizedCommitment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansAmortizedCommitmentTypeDef]


# SavingsPlansUtilizationDetailTypeDef

### SavingsPlanArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Utilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansUtilizationTypeDef]

### Savings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansSavingsTypeDef]

### AmortizedCommitment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.SavingsPlansAmortizedCommitmentTypeDef]


# SavingsPlansUtilizationTypeDef

### TotalCommitment
- **Type**: typing.Optional[str]

### UsedCommitment
- **Type**: typing.Optional[str]

### UnusedCommitment
- **Type**: typing.Optional[str]

### UtilizationPercentage
- **Type**: typing.Optional[str]


# ServiceSpecificationTypeDef

### EC2Specification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.EC2SpecificationTypeDef]


# SortDefinitionTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# StartCommitmentPurchaseAnalysisRequestTypeDef

### CommitmentPurchaseAnalysisConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.CommitmentPurchaseAnalysisConfigurationUnionTypeDef'>
- **Required**: Yes


# StartCommitmentPurchaseAnalysisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartCostAllocationTagBackfillRequestTypeDef

### BackfillFrom
- **Type**: <class 'str'>
- **Required**: Yes


# StartCostAllocationTagBackfillResponseTypeDef

### BackfillRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.CostAllocationTagBackfillRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubscriberTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.ResourceTagTypeDef]
- **Required**: Yes


# TagValuesOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### MatchOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# TagValuesTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ABSENT', 'CASE_INSENSITIVE', 'CASE_SENSITIVE', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN_OR_EQUAL', 'STARTS_WITH']]]


# TagValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetInstanceTypeDef

### EstimatedMonthlyCost
- **Type**: typing.Optional[str]

### EstimatedMonthlySavings
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### DefaultTargetInstance
- **Type**: typing.Optional[bool]

### ResourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ResourceDetailsTypeDef]

### ExpectedResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ResourceUtilizationTypeDef]

### PlatformDifferences
- **Type**: typing.Optional[typing.List[typing.Literal['HYPERVISOR', 'INSTANCE_STORE_AVAILABILITY', 'NETWORK_INTERFACE', 'STORAGE_INTERFACE', 'VIRTUALIZATION_TYPE']]]


# TerminateRecommendationDetailTypeDef

### EstimatedMonthlySavings
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]


# TotalImpactFilterTypeDef

### NumericOperator
- **Type**: typing.Literal['BETWEEN', 'EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL']
- **Required**: Yes

### StartValue
- **Type**: <class 'float'>
- **Required**: Yes

### EndValue
- **Type**: typing.Optional[float]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnomalyMonitorRequestTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorName
- **Type**: typing.Optional[str]


# UpdateAnomalyMonitorResponseTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAnomalySubscriptionRequestTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Threshold
- **Type**: typing.Optional[float]

### Frequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'IMMEDIATE', 'WEEKLY']]

### MonitorArnList
- **Type**: typing.Optional[typing.Sequence[str]]

### Subscribers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.SubscriberTypeDef]]

### SubscriptionName
- **Type**: typing.Optional[str]

### ThresholdExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ExpressionUnionTypeDef]


# UpdateAnomalySubscriptionResponseTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCostAllocationTagsStatusErrorTypeDef

### TagKey
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# UpdateCostAllocationTagsStatusRequestTypeDef

### CostAllocationTagsStatus
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.CostAllocationTagStatusEntryTypeDef]
- **Required**: Yes


# UpdateCostAllocationTagsStatusResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ce_classes.UpdateCostAllocationTagsStatusErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCostCategoryDefinitionRequestTypeDef

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleVersion
- **Type**: typing.Literal['CostCategoryExpression.v1']
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.CostCategoryRuleUnionTypeDef]
- **Required**: Yes

### EffectiveStart
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### SplitChargeRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ce_classes.CostCategorySplitChargeRuleUnionTypeDef]]


# UpdateCostCategoryDefinitionResponseTypeDef

### CostCategoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveStart
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ce_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UtilizationByTimeTypeDef

### TimePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.DateIntervalTypeDef]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ce_classes.ReservationUtilizationGroupTypeDef]]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ce_classes.ReservationAggregatesTypeDef]


