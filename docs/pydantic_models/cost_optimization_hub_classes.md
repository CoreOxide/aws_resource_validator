# cost_optimization_hub_classes

# AccountEnrollmentStatusTypeDef

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

# BlockStoragePerformanceConfigurationTypeDef

### iops
- **Type**: typing.Optional[float]

### throughput
- **Type**: typing.Optional[float]


# ComputeConfigurationTypeDef

### vCpu
- **Type**: typing.Optional[float]

### memorySizeInMB
- **Type**: typing.Optional[int]

### architecture
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[str]


# ComputeSavingsPlansConfigurationTypeDef

### accountScope
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### hourlyCommitment
- **Type**: typing.Optional[str]


# ComputeSavingsPlansTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ComputeSavingsPlansConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.SavingsPlansCostCalculationTypeDef]


# DbInstanceConfigurationTypeDef

### dbInstanceClass
- **Type**: typing.Optional[str]


# EbsVolumeConfigurationTypeDef

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.StorageConfigurationTypeDef]

### performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.BlockStoragePerformanceConfigurationTypeDef]

### attachmentState
- **Type**: typing.Optional[str]


# EbsVolumeTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.EbsVolumeConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# Ec2AutoScalingGroupConfigurationTypeDef

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.InstanceConfigurationTypeDef]


# Ec2AutoScalingGroupTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2AutoScalingGroupConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# Ec2InstanceConfigurationTypeDef

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.InstanceConfigurationTypeDef]


# Ec2InstanceSavingsPlansConfigurationTypeDef

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


# Ec2InstanceSavingsPlansTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2InstanceSavingsPlansConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.SavingsPlansCostCalculationTypeDef]


# Ec2InstanceTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2InstanceConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# Ec2ReservedInstancesConfigurationTypeDef

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


# Ec2ReservedInstancesTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2ReservedInstancesConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ReservedInstancesCostCalculationTypeDef]


# EcsServiceConfigurationTypeDef

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ComputeConfigurationTypeDef]


# EcsServiceTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.EcsServiceConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# ElastiCacheReservedInstancesConfigurationTypeDef

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


# ElastiCacheReservedInstancesTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ElastiCacheReservedInstancesConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ReservedInstancesCostCalculationTypeDef]


# EstimatedDiscountsTypeDef

### savingsPlansDiscount
- **Type**: typing.Optional[float]

### reservedInstancesDiscount
- **Type**: typing.Optional[float]

### otherDiscount
- **Type**: typing.Optional[float]


# FilterTypeDef

### restartNeeded
- **Type**: typing.Optional[bool]

### rollbackPossible
- **Type**: typing.Optional[bool]

### implementationEfforts
- **Type**: typing.Optional[typing.Sequence[typing.Literal['High', 'Low', 'Medium', 'VeryHigh', 'VeryLow']]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ComputeSavingsPlans', 'EbsVolume', 'Ec2AutoScalingGroup', 'Ec2Instance', 'Ec2InstanceSavingsPlans', 'Ec2ReservedInstances', 'EcsService', 'ElastiCacheReservedInstances', 'LambdaFunction', 'OpenSearchReservedInstances', 'RdsDbInstance', 'RdsDbInstanceStorage', 'RdsReservedInstances', 'RedshiftReservedInstances', 'SageMakerSavingsPlans']]]

### actionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['MigrateToGraviton', 'PurchaseReservedInstances', 'PurchaseSavingsPlans', 'Rightsize', 'Stop', 'Upgrade']]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.TagTypeDef]]

### resourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### recommendationIds
- **Type**: typing.Optional[typing.Sequence[str]]


# GetPreferencesResponseTypeDef

### savingsEstimationMode
- **Type**: typing.Literal['AfterDiscounts', 'BeforeDiscounts']
- **Required**: Yes

### memberAccountDiscountVisibility
- **Type**: typing.Literal['All', 'None']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommendationRequestRequestTypeDef

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommendationResponseTypeDef

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
- **Type**: typing.Literal['MigrateToGraviton', 'PurchaseReservedInstances', 'PurchaseSavingsPlans', 'Rightsize', 'Stop', 'Upgrade']
- **Required**: Yes

### rollbackPossible
- **Type**: <class 'bool'>
- **Required**: Yes

### currentResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceDetailsTypeDef'>
- **Required**: Yes

### recommendedResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceDetailsTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceConfigurationTypeDef

### type
- **Type**: typing.Optional[str]


# LambdaFunctionConfigurationTypeDef

### compute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ComputeConfigurationTypeDef]


# LambdaFunctionTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.LambdaFunctionConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# ListEnrollmentStatusesRequestListEnrollmentStatusesPaginateTypeDef

### includeOrganizationInfo
- **Type**: typing.Optional[bool]

### accountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.PaginatorConfigTypeDef]


# ListEnrollmentStatusesRequestRequestTypeDef

### includeOrganizationInfo
- **Type**: typing.Optional[bool]

### accountId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnrollmentStatusesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.AccountEnrollmentStatusTypeDef]
- **Required**: Yes

### includeMemberAccounts
- **Type**: <class 'bool'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationSummariesRequestListRecommendationSummariesPaginateTypeDef

### groupBy
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.FilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.PaginatorConfigTypeDef]


# ListRecommendationSummariesRequestRequestTypeDef

### groupBy
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.FilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationSummariesResponseTypeDef

### estimatedTotalDedupedSavings
- **Type**: <class 'float'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RecommendationSummaryTypeDef]
- **Required**: Yes

### groupBy
- **Type**: <class 'str'>
- **Required**: Yes

### currencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationsRequestListRecommendationsPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.FilterTypeDef]

### orderBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.OrderByTypeDef]

### includeAllRecommendations
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.PaginatorConfigTypeDef]


# ListRecommendationsRequestRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.FilterTypeDef]

### orderBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.OrderByTypeDef]

### includeAllRecommendations
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RecommendationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OpenSearchReservedInstancesConfigurationTypeDef

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


# OpenSearchReservedInstancesTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.OpenSearchReservedInstancesConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ReservedInstancesCostCalculationTypeDef]


# OrderByTypeDef

### dimension
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[typing.Literal['Asc', 'Desc']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RdsDbInstanceConfigurationTypeDef

### instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.DbInstanceConfigurationTypeDef]


# RdsDbInstanceStorageConfigurationTypeDef

### storageType
- **Type**: typing.Optional[str]

### allocatedStorageInGb
- **Type**: typing.Optional[float]

### iops
- **Type**: typing.Optional[float]

### storageThroughput
- **Type**: typing.Optional[float]


# RdsDbInstanceStorageTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RdsDbInstanceStorageConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# RdsDbInstanceTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RdsDbInstanceConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourceCostCalculationTypeDef]


# RdsReservedInstancesConfigurationTypeDef

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


# RdsReservedInstancesTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RdsReservedInstancesConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ReservedInstancesCostCalculationTypeDef]


# RecommendationSummaryTypeDef

### group
- **Type**: typing.Optional[str]

### estimatedMonthlySavings
- **Type**: typing.Optional[float]

### recommendationCount
- **Type**: typing.Optional[int]


# RecommendationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.TagTypeDef]]


# RedshiftReservedInstancesConfigurationTypeDef

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


# RedshiftReservedInstancesTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RedshiftReservedInstancesConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ReservedInstancesCostCalculationTypeDef]


# ReservedInstancesCostCalculationTypeDef

### pricing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ReservedInstancesPricingTypeDef]


# ReservedInstancesPricingTypeDef

### estimatedOnDemandCost
- **Type**: typing.Optional[float]

### monthlyReservationEligibleCost
- **Type**: typing.Optional[float]

### savingsPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlyAmortizedReservationCost
- **Type**: typing.Optional[float]


# ResourceCostCalculationTypeDef

### usages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.UsageTypeDef]]

### pricing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResourcePricingTypeDef]


# ResourceDetailsTypeDef

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.LambdaFunctionTypeDef]

### ecsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.EcsServiceTypeDef]

### ec2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2InstanceTypeDef]

### ebsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.EbsVolumeTypeDef]

### ec2AutoScalingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2AutoScalingGroupTypeDef]

### ec2ReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2ReservedInstancesTypeDef]

### rdsReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RdsReservedInstancesTypeDef]

### elastiCacheReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ElastiCacheReservedInstancesTypeDef]

### openSearchReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.OpenSearchReservedInstancesTypeDef]

### redshiftReservedInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RedshiftReservedInstancesTypeDef]

### ec2InstanceSavingsPlans
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.Ec2InstanceSavingsPlansTypeDef]

### computeSavingsPlans
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ComputeSavingsPlansTypeDef]

### sageMakerSavingsPlans
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.SageMakerSavingsPlansTypeDef]

### rdsDbInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RdsDbInstanceTypeDef]

### rdsDbInstanceStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.RdsDbInstanceStorageTypeDef]


# ResourcePricingTypeDef

### estimatedCostBeforeDiscounts
- **Type**: typing.Optional[float]

### estimatedNetUnusedAmortizedCommitments
- **Type**: typing.Optional[float]

### estimatedDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.EstimatedDiscountsTypeDef]

### estimatedCostAfterDiscounts
- **Type**: typing.Optional[float]


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


# SageMakerSavingsPlansConfigurationTypeDef

### accountScope
- **Type**: typing.Optional[str]

### term
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[str]

### hourlyCommitment
- **Type**: typing.Optional[str]


# SageMakerSavingsPlansTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.SageMakerSavingsPlansConfigurationTypeDef]

### costCalculation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.SavingsPlansCostCalculationTypeDef]


# SavingsPlansCostCalculationTypeDef

### pricing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cost_optimization_hub_classes.SavingsPlansPricingTypeDef]


# SavingsPlansPricingTypeDef

### monthlySavingsPlansEligibleCost
- **Type**: typing.Optional[float]

### estimatedMonthlyCommitment
- **Type**: typing.Optional[float]

### savingsPercentage
- **Type**: typing.Optional[float]

### estimatedOnDemandCost
- **Type**: typing.Optional[float]


# StorageConfigurationTypeDef

### type
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[float]


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# UpdateEnrollmentStatusRequestRequestTypeDef

### status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# UpdateEnrollmentStatusResponseTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePreferencesRequestRequestTypeDef

### savingsEstimationMode
- **Type**: typing.Optional[typing.Literal['AfterDiscounts', 'BeforeDiscounts']]

### memberAccountDiscountVisibility
- **Type**: typing.Optional[typing.Literal['All', 'None']]


# UpdatePreferencesResponseTypeDef

### savingsEstimationMode
- **Type**: typing.Literal['AfterDiscounts', 'BeforeDiscounts']
- **Required**: Yes

### memberAccountDiscountVisibility
- **Type**: typing.Literal['All', 'None']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cost_optimization_hub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageTypeDef

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


