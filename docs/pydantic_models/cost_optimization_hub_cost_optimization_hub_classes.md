# Cost Optimization Hub Cost Optimization Hub Classes

# AccountEnrollmentStatus

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### lastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### createdTimestamp
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockStoragePerformanceConfiguration

### iops
- **Type**: typing.Optional[float]

### throughput
- **Type**: typing.Optional[float]


# ComputeConfiguration

### vCpu
- **Type**: typing.Optional[float]

### memorySizeInMB
- **Type**: typing.Optional[int]

### architecture
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]


# ComputeSavingsPlans

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ComputeSavingsPlansConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SavingsPlansCostCalculation]


# ComputeSavingsPlansConfiguration

### accountScope
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### hourlyCommitment
- **Type**: typing.Optional[str]


# DbInstanceConfiguration

### dbInstanceClass
- **Type**: typing.Optional[str]


# EbsVolume

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.EbsVolumeConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# EbsVolumeConfiguration

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.StorageConfiguration]

### performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.BlockStoragePerformanceConfiguration]

### attachmentState
- **Type**: typing.Optional[str]


# Ec2AutoScalingGroup

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2AutoScalingGroupConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# Ec2AutoScalingGroupConfiguration

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.InstanceConfiguration]

### mixedInstances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.MixedInstanceConfiguration]]

### type
- **Type**: typing.Optional[typing.Literal['MixedInstanceTypes', 'SingleInstanceType']]

### allocationStrategy
- **Type**: typing.Optional[typing.Literal['LowestPrice', 'Prioritized']]


# Ec2Instance

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2InstanceConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# Ec2InstanceConfiguration

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.InstanceConfiguration]


# Ec2InstanceSavingsPlans

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2InstanceSavingsPlansConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SavingsPlansCostCalculation]


# Ec2InstanceSavingsPlansConfiguration

### accountScope
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### hourlyCommitment
- **Type**: typing.Optional[str]

### instanceFamily
- **Type**: typing.Optional[str]

### savingsPlansRegion
- **Type**: typing.Optional[str]


# Ec2ReservedInstances

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2ReservedInstancesConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ReservedInstancesCostCalculation]


# Ec2ReservedInstancesConfiguration

### accountScope
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### normalizedUnitsToPurchase
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### numberOfInstancesToPurchase
- **Type**: typing.Optional[str]

### offeringClass
- **Type**: typing.Optional[str]

### instanceFamily
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### reservedInstancesRegion
- **Type**: typing.Optional[str]

### currentGeneration
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]

### tenancy
- **Type**: typing.Optional[str]

### sizeFlexEligible
- **Type**: typing.Optional[bool]

### upfrontCost
- **Type**: typing.Optional[str]

### monthlyRecurringCost
- **Type**: typing.Optional[str]


# EcsService

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.EcsServiceConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# EcsServiceConfiguration

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ComputeConfiguration]


# ElastiCacheReservedInstances

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ElastiCacheReservedInstancesConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ReservedInstancesCostCalculation]


# ElastiCacheReservedInstancesConfiguration

### accountScope
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### normalizedUnitsToPurchase
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### numberOfInstancesToPurchase
- **Type**: typing.Optional[str]

### instanceFamily
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### reservedInstancesRegion
- **Type**: typing.Optional[str]

### currentGeneration
- **Type**: typing.Optional[str]

### sizeFlexEligible
- **Type**: typing.Optional[bool]

### upfrontCost
- **Type**: typing.Optional[str]

### monthlyRecurringCost
- **Type**: typing.Optional[str]


# EstimatedDiscounts

### savingsPlansDiscount
- **Type**: typing.Optional[float]

### reservedInstancesDiscount
- **Type**: typing.Optional[float]

### otherDiscount
- **Type**: typing.Optional[float]


# Filter

### restartNeeded
- **Type**: typing.Optional[bool]

### rollbackPossible
- **Type**: typing.Optional[bool]

### implementationEfforts
- **Type**: typing.Optional[typing.List[typing.Literal['High', 'Low', 'Medium', 'VeryHigh', 'VeryLow']]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### regions
- **Type**: typing.Optional[typing.List[str]]

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ComputeSavingsPlans', 'EbsVolume', 'Ec2AutoScalingGroup', 'Ec2Instance', 'Ec2InstanceSavingsPlans', 'Ec2ReservedInstances', 'EcsService', 'ElastiCacheReservedInstances', 'LambdaFunction', 'OpenSearchReservedInstances', 'RdsDbInstance', 'RdsDbInstanceStorage', 'RdsReservedInstances', 'RedshiftReservedInstances', 'SageMakerSavingsPlans']]]

### actionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Delete', 'MigrateToGraviton', 'PurchaseReservedInstances', 'PurchaseSavingsPlans', 'Rightsize', 'ScaleIn', 'Stop', 'Upgrade']]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Tag]]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### recommendationIds
- **Type**: typing.Optional[typing.List[str]]


# GetPreferencesResponse

### savingsEstimationMode
- **Type**: typing.Literal['AfterDiscounts', 'BeforeDiscounts']
- **Required**: Yes

### memberAccountDiscountVisibility
- **Type**: typing.Literal['All', 'None']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommendationRequest

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommendationResponse

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### currencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationLookbackPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes

### costCalculationLookbackPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes

### estimatedSavingsPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### estimatedSavingsOverCostCalculationLookbackPeriod
- **Type**: <class 'float'>
- **Required**: Yes

### currentResourceType
- **Type**: typing.Literal['ComputeSavingsPlans', 'EbsVolume', 'Ec2AutoScalingGroup', 'Ec2Instance', 'Ec2InstanceSavingsPlans', 'Ec2ReservedInstances', 'EcsService', 'ElastiCacheReservedInstances', 'LambdaFunction', 'OpenSearchReservedInstances', 'RdsDbInstance', 'RdsDbInstanceStorage', 'RdsReservedInstances', 'RedshiftReservedInstances', 'SageMakerSavingsPlans']
- **Required**: Yes

### recommendedResourceType
- **Type**: typing.Literal['ComputeSavingsPlans', 'EbsVolume', 'Ec2AutoScalingGroup', 'Ec2Instance', 'Ec2InstanceSavingsPlans', 'Ec2ReservedInstances', 'EcsService', 'ElastiCacheReservedInstances', 'LambdaFunction', 'OpenSearchReservedInstances', 'RdsDbInstance', 'RdsDbInstanceStorage', 'RdsReservedInstances', 'RedshiftReservedInstances', 'SageMakerSavingsPlans']
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: typing.Literal['ComputeOptimizer', 'CostExplorer']
- **Required**: Yes

### lastRefreshTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### estimatedMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes

### estimatedMonthlyCost
- **Type**: <class 'float'>
- **Required**: Yes

### implementationEffort
- **Type**: typing.Literal['High', 'Low', 'Medium', 'VeryHigh', 'VeryLow']
- **Required**: Yes

### restartNeeded
- **Type**: <class 'bool'>
- **Required**: Yes

### actionType
- **Type**: typing.Literal['Delete', 'MigrateToGraviton', 'PurchaseReservedInstances', 'PurchaseSavingsPlans', 'Rightsize', 'ScaleIn', 'Stop', 'Upgrade']
- **Required**: Yes

### rollbackPossible
- **Type**: <class 'bool'>
- **Required**: Yes

### currentResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceDetails'>
- **Required**: Yes

### recommendedResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceDetails'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceConfiguration

### type
- **Type**: typing.Optional[str]


# LambdaFunction

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.LambdaFunctionConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# LambdaFunctionConfiguration

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ComputeConfiguration]


# ListEnrollmentStatusesRequest

### includeOrganizationInfo
- **Type**: typing.Optional[bool]

### accountId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnrollmentStatusesRequestPaginate

### includeOrganizationInfo
- **Type**: typing.Optional[bool]

### accountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.PaginatorConfig]


# ListEnrollmentStatusesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.AccountEnrollmentStatus]
- **Required**: Yes

### includeMemberAccounts
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationSummariesRequest

### groupBy
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Filter]

### maxResults
- **Type**: typing.Optional[int]

### metrics
- **Type**: typing.Optional[typing.List[typing.Literal['SavingsPercentage']]]

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationSummariesRequestPaginate

### groupBy
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Filter]

### metrics
- **Type**: typing.Optional[typing.List[typing.Literal['SavingsPercentage']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.PaginatorConfig]


# ListRecommendationSummariesResponse

### estimatedTotalDedupedSavings
- **Type**: <class 'float'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RecommendationSummary]
- **Required**: Yes

### groupBy
- **Type**: <class 'str'>
- **Required**: Yes

### currencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SummaryMetricsResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequest

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Filter]

### orderBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.OrderBy]

### includeAllRecommendations
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequestPaginate

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Filter]

### orderBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.OrderBy]

### includeAllRecommendations
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.PaginatorConfig]


# ListRecommendationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Recommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MixedInstanceConfiguration

### type
- **Type**: typing.Optional[str]


# OpenSearchReservedInstances

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.OpenSearchReservedInstancesConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ReservedInstancesCostCalculation]


# OpenSearchReservedInstancesConfiguration

### accountScope
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### normalizedUnitsToPurchase
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### numberOfInstancesToPurchase
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### reservedInstancesRegion
- **Type**: typing.Optional[str]

### currentGeneration
- **Type**: typing.Optional[str]

### sizeFlexEligible
- **Type**: typing.Optional[bool]

### upfrontCost
- **Type**: typing.Optional[str]

### monthlyRecurringCost
- **Type**: typing.Optional[str]


# OrderBy

### dimension
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[typing.Literal['Asc', 'Desc']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RdsDbInstance

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RdsDbInstanceConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# RdsDbInstanceConfiguration

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.DbInstanceConfiguration]


# RdsDbInstanceStorage

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RdsDbInstanceStorageConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourceCostCalculation]


# RdsDbInstanceStorageConfiguration

### storageType
- **Type**: typing.Optional[str]

### allocatedStorageInGb
- **Type**: typing.Optional[float]

### iops
- **Type**: typing.Optional[float]

### storageThroughput
- **Type**: typing.Optional[float]


# RdsReservedInstances

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RdsReservedInstancesConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ReservedInstancesCostCalculation]


# RdsReservedInstancesConfiguration

### accountScope
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### normalizedUnitsToPurchase
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### numberOfInstancesToPurchase
- **Type**: typing.Optional[str]

### instanceFamily
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### reservedInstancesRegion
- **Type**: typing.Optional[str]

### sizeFlexEligible
- **Type**: typing.Optional[bool]

### currentGeneration
- **Type**: typing.Optional[str]

### upfrontCost
- **Type**: typing.Optional[str]

### monthlyRecurringCost
- **Type**: typing.Optional[str]

### licenseModel
- **Type**: typing.Optional[str]

### databaseEdition
- **Type**: typing.Optional[str]

### databaseEngine
- **Type**: typing.Optional[str]

### deploymentOption
- **Type**: typing.Optional[str]


# Recommendation

### recommendationId
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]

### currentResourceType
- **Type**: typing.Optional[str]

### recommendedResourceType
- **Type**: typing.Optional[str]

### estimatedMonthlySavings
- **Type**: typing.Optional[float]

### estimatedSavingsPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlyCost
- **Type**: typing.Optional[float]

### currencyCode
- **Type**: typing.Optional[str]

### implementationEffort
- **Type**: typing.Optional[str]

### restartNeeded
- **Type**: typing.Optional[bool]

### actionType
- **Type**: typing.Optional[str]

### rollbackPossible
- **Type**: typing.Optional[bool]

### currentResourceSummary
- **Type**: typing.Optional[str]

### recommendedResourceSummary
- **Type**: typing.Optional[str]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### recommendationLookbackPeriodInDays
- **Type**: typing.Optional[int]

### source
- **Type**: typing.Optional[typing.Literal['ComputeOptimizer', 'CostExplorer']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Tag]]


# RecommendationSummary

### group
- **Type**: typing.Optional[str]

### estimatedMonthlySavings
- **Type**: typing.Optional[float]

### recommendationCount
- **Type**: typing.Optional[int]


# RedshiftReservedInstances

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RedshiftReservedInstancesConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ReservedInstancesCostCalculation]


# RedshiftReservedInstancesConfiguration

### accountScope
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### normalizedUnitsToPurchase
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### numberOfInstancesToPurchase
- **Type**: typing.Optional[str]

### instanceFamily
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### reservedInstancesRegion
- **Type**: typing.Optional[str]

### sizeFlexEligible
- **Type**: typing.Optional[bool]

### currentGeneration
- **Type**: typing.Optional[str]

### upfrontCost
- **Type**: typing.Optional[str]

### monthlyRecurringCost
- **Type**: typing.Optional[str]


# ReservedInstancesCostCalculation

### pricing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ReservedInstancesPricing]


# ReservedInstancesPricing

### estimatedOnDemandCost
- **Type**: typing.Optional[float]

### monthlyReservationEligibleCost
- **Type**: typing.Optional[float]

### savingsPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlyAmortizedReservationCost
- **Type**: typing.Optional[float]


# ResourceCostCalculation

### usages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Usage]]

### pricing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResourcePricing]


# ResourceDetails

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.LambdaFunction]

### ecsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.EcsService]

### ec2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2Instance]

### ebsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.EbsVolume]

### ec2AutoScalingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2AutoScalingGroup]

### ec2ReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2ReservedInstances]

### rdsReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RdsReservedInstances]

### elastiCacheReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ElastiCacheReservedInstances]

### openSearchReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.OpenSearchReservedInstances]

### redshiftReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RedshiftReservedInstances]

### ec2InstanceSavingsPlans
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.Ec2InstanceSavingsPlans]

### computeSavingsPlans
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ComputeSavingsPlans]

### sageMakerSavingsPlans
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SageMakerSavingsPlans]

### rdsDbInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RdsDbInstance]

### rdsDbInstanceStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.RdsDbInstanceStorage]


# ResourcePricing

### estimatedCostBeforeDiscounts
- **Type**: typing.Optional[float]

### estimatedNetUnusedAmortizedCommitments
- **Type**: typing.Optional[float]

### estimatedDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.EstimatedDiscounts]

### estimatedCostAfterDiscounts
- **Type**: typing.Optional[float]


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


# SageMakerSavingsPlans

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SageMakerSavingsPlansConfiguration]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SavingsPlansCostCalculation]


# SageMakerSavingsPlansConfiguration

### accountScope
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### hourlyCommitment
- **Type**: typing.Optional[str]


# SavingsPlansCostCalculation

### pricing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.SavingsPlansPricing]


# SavingsPlansPricing

### monthlySavingsPlansEligibleCost
- **Type**: typing.Optional[float]

### estimatedMonthlyCommitment
- **Type**: typing.Optional[float]

### savingsPercentage
- **Type**: typing.Optional[float]

### estimatedOnDemandCost
- **Type**: typing.Optional[float]


# StorageConfiguration

### type
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[float]


# SummaryMetricsResult

### savingsPercentage
- **Type**: typing.Optional[str]


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# UpdateEnrollmentStatusRequest

### status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# UpdateEnrollmentStatusResponse

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePreferencesRequest

### savingsEstimationMode
- **Type**: typing.Optional[typing.Literal['AfterDiscounts', 'BeforeDiscounts']]

### memberAccountDiscountVisibility
- **Type**: typing.Optional[typing.Literal['All', 'None']]


# UpdatePreferencesResponse

### savingsEstimationMode
- **Type**: typing.Literal['AfterDiscounts', 'BeforeDiscounts']
- **Required**: Yes

### memberAccountDiscountVisibility
- **Type**: typing.Literal['All', 'None']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub.cost_optimization_hub_classes.ResponseMetadata'>
- **Required**: Yes


# Usage

### usageType
- **Type**: typing.Optional[str]

### usageAmount
- **Type**: typing.Optional[float]

### operation
- **Type**: typing.Optional[str]

### productCode
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]


