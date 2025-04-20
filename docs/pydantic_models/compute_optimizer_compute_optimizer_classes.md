# Compute Optimizer Compute Optimizer Classes

# AccountEnrollmentStatus

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Failed', 'Inactive', 'Pending']]

### statusReason
- **Type**: typing.Optional[str]

### lastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AutoScalingGroupConfiguration

### desiredCapacity
- **Type**: typing.Optional[int]

### minSize
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]

### instanceType
- **Type**: typing.Optional[str]

### allocationStrategy
- **Type**: typing.Optional[typing.Literal['LowestPrice', 'Prioritized']]

### estimatedInstanceHourReductionPercentage
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['MixedInstanceTypes', 'SingleInstanceType']]

### mixedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]


# AutoScalingGroupEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# AutoScalingGroupRecommendation

### accountId
- **Type**: typing.Optional[str]

### autoScalingGroupArn
- **Type**: typing.Optional[str]

### autoScalingGroupName
- **Type**: typing.Optional[str]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Overprovisioned', 'Underprovisioned']]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationMetric]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### currentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AutoScalingGroupConfiguration]

### currentInstanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GpuInfo]

### recommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AutoScalingGroupRecommendationOption]]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EffectiveRecommendationPreferences]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AmazonEmr', 'ApacheCassandra', 'ApacheHadoop', 'Kafka', 'Memcached', 'Nginx', 'PostgreSql', 'Redis', 'SQLServer']]]


# AutoScalingGroupRecommendationOption

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AutoScalingGroupConfiguration]

### instanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GpuInfo]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationMetric]]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AutoScalingGroupSavingsOpportunityAfterDiscounts]

### migrationEffort
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]


# AutoScalingGroupSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AutoScalingGroupEstimatedMonthlySavings]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerConfiguration

### containerName
- **Type**: typing.Optional[str]

### memorySizeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.MemorySizeConfiguration]

### cpu
- **Type**: typing.Optional[int]


# ContainerRecommendation

### containerName
- **Type**: typing.Optional[str]

### memorySizeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.MemorySizeConfiguration]

### cpu
- **Type**: typing.Optional[int]


# CurrentPerformanceRiskRatings

### high
- **Type**: typing.Optional[int]

### medium
- **Type**: typing.Optional[int]

### low
- **Type**: typing.Optional[int]

### veryLow
- **Type**: typing.Optional[int]


# CustomizableMetricParameters

### threshold
- **Type**: typing.Optional[typing.Literal['P90', 'P95', 'P99_5']]

### headroom
- **Type**: typing.Optional[typing.Literal['PERCENT_0', 'PERCENT_10', 'PERCENT_20', 'PERCENT_30']]


# DBStorageConfiguration

### storageType
- **Type**: typing.Optional[str]

### allocatedStorage
- **Type**: typing.Optional[int]

### iops
- **Type**: typing.Optional[int]

### maxAllocatedStorage
- **Type**: typing.Optional[int]

### storageThroughput
- **Type**: typing.Optional[int]


# DeleteRecommendationPreferencesRequest

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### recommendationPreferenceNames
- **Type**: typing.List[typing.Literal['EnhancedInfrastructureMetrics', 'ExternalMetricsPreference', 'InferredWorkloadTypes', 'LookBackPeriodPreference', 'PreferredResources', 'UtilizationPreferences']]
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Scope]


# DescribeRecommendationExportJobsRequest

### jobIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.JobFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRecommendationExportJobsRequestPaginate

### jobIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.JobFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.PaginatorConfig]


# DescribeRecommendationExportJobsResponse

### recommendationExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationExportJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# EBSEffectiveRecommendationPreferences

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSSavingsEstimationMode]


# EBSEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# EBSFilter

### name
- **Type**: typing.Optional[typing.Literal['Finding']]

### values
- **Type**: typing.Optional[typing.List[str]]


# EBSSavingsEstimationMode

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# EBSSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSEstimatedMonthlySavings]


# EBSUtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['VolumeReadBytesPerSecond', 'VolumeReadOpsPerSecond', 'VolumeWriteBytesPerSecond', 'VolumeWriteOpsPerSecond']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# ECSEffectiveRecommendationPreferences

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSSavingsEstimationMode]


# ECSEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# ECSSavingsEstimationMode

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# ECSSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSEstimatedMonthlySavings]


# ECSServiceProjectedMetric

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'Memory']]

### timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### upperBoundValues
- **Type**: typing.Optional[typing.List[float]]

### lowerBoundValues
- **Type**: typing.Optional[typing.List[float]]


# ECSServiceProjectedUtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'Memory']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### lowerBoundValue
- **Type**: typing.Optional[float]

### upperBoundValue
- **Type**: typing.Optional[float]


# ECSServiceRecommendation

### serviceArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ServiceConfiguration]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceUtilizationMetric]]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'Fargate']]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### finding
- **Type**: typing.Optional[typing.Literal['Optimized', 'Overprovisioned', 'Underprovisioned']]

### findingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CPUOverprovisioned', 'CPUUnderprovisioned', 'MemoryOverprovisioned', 'MemoryUnderprovisioned']]]

### serviceRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceRecommendationOption]]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSEffectiveRecommendationPreferences]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]


# ECSServiceRecommendationFilter

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCode']]

### values
- **Type**: typing.Optional[typing.List[str]]


# ECSServiceRecommendationOption

### memory
- **Type**: typing.Optional[int]

### cpu
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSSavingsOpportunityAfterDiscounts]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceProjectedUtilizationMetric]]

### containerRecommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ContainerRecommendation]]


# ECSServiceRecommendedOptionProjectedMetric

### recommendedCpuUnits
- **Type**: typing.Optional[int]

### recommendedMemorySize
- **Type**: typing.Optional[int]

### projectedMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceProjectedMetric]]


# ECSServiceUtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'Memory']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# EffectivePreferredResource

### name
- **Type**: typing.Optional[typing.Literal['Ec2InstanceTypes']]

### includeList
- **Type**: typing.Optional[typing.List[str]]

### effectiveIncludeList
- **Type**: typing.Optional[typing.List[str]]

### excludeList
- **Type**: typing.Optional[typing.List[str]]


# EffectiveRecommendationPreferences

### cpuVendorArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['AWS_ARM64', 'CURRENT']]]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### externalMetricsPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ExternalMetricsPreference]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### utilizationPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationPreference]]

### preferredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EffectivePreferredResource]]

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.InstanceSavingsEstimationMode]


# EnrollmentFilter

### name
- **Type**: typing.Optional[typing.Literal['Status']]

### values
- **Type**: typing.Optional[typing.List[str]]


# EstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# ExportAutoScalingGroupRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Filter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'AutoScalingGroupArn', 'AutoScalingGroupName', 'CurrentConfigurationAllocationStrategy', 'CurrentConfigurationDesiredCapacity', 'CurrentConfigurationInstanceType', 'CurrentConfigurationMaxSize', 'CurrentConfigurationMinSize', 'CurrentConfigurationMixedInstanceTypes', 'CurrentConfigurationType', 'CurrentInstanceGpuInfo', 'CurrentMemory', 'CurrentNetwork', 'CurrentOnDemandPrice', 'CurrentPerformanceRisk', 'CurrentStandardOneYearNoUpfrontReservedPrice', 'CurrentStandardThreeYearNoUpfrontReservedPrice', 'CurrentStorage', 'CurrentVCpus', 'EffectiveRecommendationPreferencesCpuVendorArchitectures', 'EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics', 'EffectiveRecommendationPreferencesInferredWorkloadTypes', 'EffectiveRecommendationPreferencesLookBackPeriod', 'EffectiveRecommendationPreferencesPreferredResources', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'InferredWorkloadTypes', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsConfigurationAllocationStrategy', 'RecommendationOptionsConfigurationDesiredCapacity', 'RecommendationOptionsConfigurationEstimatedInstanceHourReductionPercentage', 'RecommendationOptionsConfigurationInstanceType', 'RecommendationOptionsConfigurationMaxSize', 'RecommendationOptionsConfigurationMinSize', 'RecommendationOptionsConfigurationMixedInstanceTypes', 'RecommendationOptionsConfigurationType', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsInstanceGpuInfo', 'RecommendationOptionsMemory', 'RecommendationOptionsMigrationEffort', 'RecommendationOptionsNetwork', 'RecommendationOptionsOnDemandPrice', 'RecommendationOptionsPerformanceRisk', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'RecommendationOptionsStandardOneYearNoUpfrontReservedPrice', 'RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice', 'RecommendationOptionsStorage', 'RecommendationOptionsVcpus', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDiskReadBytesPerSecondMaximum', 'UtilizationMetricsDiskReadOpsPerSecondMaximum', 'UtilizationMetricsDiskWriteBytesPerSecondMaximum', 'UtilizationMetricsDiskWriteOpsPerSecondMaximum', 'UtilizationMetricsEbsReadBytesPerSecondMaximum', 'UtilizationMetricsEbsReadOpsPerSecondMaximum', 'UtilizationMetricsEbsWriteBytesPerSecondMaximum', 'UtilizationMetricsEbsWriteOpsPerSecondMaximum', 'UtilizationMetricsGpuMemoryPercentageMaximum', 'UtilizationMetricsGpuPercentageMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkInBytesPerSecondMaximum', 'UtilizationMetricsNetworkOutBytesPerSecondMaximum', 'UtilizationMetricsNetworkPacketsInPerSecondMaximum', 'UtilizationMetricsNetworkPacketsOutPerSecondMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# ExportAutoScalingGroupRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportDestination

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination]


# ExportEBSVolumeRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSFilter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'CurrentConfigurationRootVolume', 'CurrentConfigurationVolumeBaselineIOPS', 'CurrentConfigurationVolumeBaselineThroughput', 'CurrentConfigurationVolumeBurstIOPS', 'CurrentConfigurationVolumeBurstThroughput', 'CurrentConfigurationVolumeSize', 'CurrentConfigurationVolumeType', 'CurrentMonthlyPrice', 'CurrentPerformanceRisk', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsConfigurationVolumeBaselineIOPS', 'RecommendationOptionsConfigurationVolumeBaselineThroughput', 'RecommendationOptionsConfigurationVolumeBurstIOPS', 'RecommendationOptionsConfigurationVolumeBurstThroughput', 'RecommendationOptionsConfigurationVolumeSize', 'RecommendationOptionsConfigurationVolumeType', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsMonthlyPrice', 'RecommendationOptionsPerformanceRisk', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'RootVolume', 'Tags', 'UtilizationMetricsVolumeReadBytesPerSecondMaximum', 'UtilizationMetricsVolumeReadOpsPerSecondMaximum', 'UtilizationMetricsVolumeWriteBytesPerSecondMaximum', 'UtilizationMetricsVolumeWriteOpsPerSecondMaximum', 'VolumeArn']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportEBSVolumeRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportEC2InstanceRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Filter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'CurrentInstanceGpuInfo', 'CurrentInstanceType', 'CurrentMemory', 'CurrentNetwork', 'CurrentOnDemandPrice', 'CurrentPerformanceRisk', 'CurrentStandardOneYearNoUpfrontReservedPrice', 'CurrentStandardThreeYearNoUpfrontReservedPrice', 'CurrentStorage', 'CurrentVCpus', 'EffectiveRecommendationPreferencesCpuVendorArchitectures', 'EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics', 'EffectiveRecommendationPreferencesExternalMetricsSource', 'EffectiveRecommendationPreferencesInferredWorkloadTypes', 'EffectiveRecommendationPreferencesLookBackPeriod', 'EffectiveRecommendationPreferencesPreferredResources', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'EffectiveRecommendationPreferencesUtilizationPreferences', 'ExternalMetricStatusCode', 'ExternalMetricStatusReason', 'Finding', 'FindingReasonCodes', 'Idle', 'InferredWorkloadTypes', 'InstanceArn', 'InstanceName', 'InstanceState', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsInstanceGpuInfo', 'RecommendationOptionsInstanceType', 'RecommendationOptionsMemory', 'RecommendationOptionsMigrationEffort', 'RecommendationOptionsNetwork', 'RecommendationOptionsOnDemandPrice', 'RecommendationOptionsPerformanceRisk', 'RecommendationOptionsPlatformDifferences', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'RecommendationOptionsStandardOneYearNoUpfrontReservedPrice', 'RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice', 'RecommendationOptionsStorage', 'RecommendationOptionsVcpus', 'RecommendationsSourcesRecommendationSourceArn', 'RecommendationsSourcesRecommendationSourceType', 'Tags', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDiskReadBytesPerSecondMaximum', 'UtilizationMetricsDiskReadOpsPerSecondMaximum', 'UtilizationMetricsDiskWriteBytesPerSecondMaximum', 'UtilizationMetricsDiskWriteOpsPerSecondMaximum', 'UtilizationMetricsEbsReadBytesPerSecondMaximum', 'UtilizationMetricsEbsReadOpsPerSecondMaximum', 'UtilizationMetricsEbsWriteBytesPerSecondMaximum', 'UtilizationMetricsEbsWriteOpsPerSecondMaximum', 'UtilizationMetricsGpuMemoryPercentageMaximum', 'UtilizationMetricsGpuPercentageMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkInBytesPerSecondMaximum', 'UtilizationMetricsNetworkOutBytesPerSecondMaximum', 'UtilizationMetricsNetworkPacketsInPerSecondMaximum', 'UtilizationMetricsNetworkPacketsOutPerSecondMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# ExportEC2InstanceRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportECSServiceRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceRecommendationFilter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'CurrentPerformanceRisk', 'CurrentServiceConfigurationAutoScalingConfiguration', 'CurrentServiceConfigurationCpu', 'CurrentServiceConfigurationMemory', 'CurrentServiceConfigurationTaskDefinitionArn', 'CurrentServiceContainerConfigurations', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'FindingReasonCodes', 'LastRefreshTimestamp', 'LaunchType', 'LookbackPeriodInDays', 'RecommendationOptionsContainerRecommendations', 'RecommendationOptionsCpu', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsMemory', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'ServiceArn', 'Tags', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsMemoryMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportECSServiceRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportIdleRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleRecommendationFilter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'Finding', 'FindingDescription', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'ResourceArn', 'ResourceId', 'ResourceType', 'SavingsOpportunity', 'SavingsOpportunityAfterDiscount', 'Tags', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDatabaseConnectionsMaximum', 'UtilizationMetricsEBSVolumeReadIOPSMaximum', 'UtilizationMetricsEBSVolumeWriteIOPSMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkInBytesPerSecondMaximum', 'UtilizationMetricsNetworkOutBytesPerSecondMaximum', 'UtilizationMetricsVolumeReadOpsPerSecondMaximum', 'UtilizationMetricsVolumeWriteOpsPerSecondMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportIdleRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportLambdaFunctionRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionRecommendationFilter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'CurrentConfigurationMemorySize', 'CurrentConfigurationTimeout', 'CurrentCostAverage', 'CurrentCostTotal', 'CurrentPerformanceRisk', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'FindingReasonCodes', 'FunctionArn', 'FunctionVersion', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'NumberOfInvocations', 'RecommendationOptionsConfigurationMemorySize', 'RecommendationOptionsCostHigh', 'RecommendationOptionsCostLow', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsProjectedUtilizationMetricsDurationExpected', 'RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound', 'RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'Tags', 'UtilizationMetricsDurationAverage', 'UtilizationMetricsDurationMaximum', 'UtilizationMetricsMemoryAverage', 'UtilizationMetricsMemoryMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportLambdaFunctionRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportLicenseRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LicenseRecommendationFilter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'CurrentLicenseConfigurationInstanceType', 'CurrentLicenseConfigurationLicenseEdition', 'CurrentLicenseConfigurationLicenseModel', 'CurrentLicenseConfigurationLicenseName', 'CurrentLicenseConfigurationLicenseVersion', 'CurrentLicenseConfigurationMetricsSource', 'CurrentLicenseConfigurationNumberOfCores', 'CurrentLicenseConfigurationOperatingSystem', 'Finding', 'FindingReasonCodes', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsLicenseEdition', 'RecommendationOptionsLicenseModel', 'RecommendationOptionsOperatingSystem', 'RecommendationOptionsSavingsOpportunityPercentage', 'ResourceArn', 'Tags']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportLicenseRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExportRDSDatabaseRecommendationsRequest

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3DestinationConfig'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBRecommendationFilter]]

### fieldsToExport
- **Type**: typing.Optional[typing.List[typing.Literal['AccountId', 'CurrentDBInstanceClass', 'CurrentInstanceOnDemandHourlyPrice', 'CurrentInstancePerformanceRisk', 'CurrentStorageConfigurationAllocatedStorage', 'CurrentStorageConfigurationIOPS', 'CurrentStorageConfigurationMaxAllocatedStorage', 'CurrentStorageConfigurationStorageThroughput', 'CurrentStorageConfigurationStorageType', 'CurrentStorageOnDemandMonthlyPrice', 'DBClusterIdentifier', 'EffectiveRecommendationPreferencesCpuVendorArchitectures', 'EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics', 'EffectiveRecommendationPreferencesLookBackPeriod', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Engine', 'EngineVersion', 'Idle', 'InstanceFinding', 'InstanceFindingReasonCodes', 'InstanceRecommendationOptionsDBInstanceClass', 'InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency', 'InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'InstanceRecommendationOptionsEstimatedMonthlySavingsValue', 'InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'InstanceRecommendationOptionsInstanceOnDemandHourlyPrice', 'InstanceRecommendationOptionsPerformanceRisk', 'InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'InstanceRecommendationOptionsRank', 'InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'InstanceRecommendationOptionsSavingsOpportunityPercentage', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'MultiAZDBInstance', 'PromotionTier', 'ResourceArn', 'StorageFinding', 'StorageFindingReasonCodes', 'StorageRecommendationOptionsAllocatedStorage', 'StorageRecommendationOptionsEstimatedMonthlySavingsCurrency', 'StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'StorageRecommendationOptionsEstimatedMonthlySavingsValue', 'StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'StorageRecommendationOptionsIOPS', 'StorageRecommendationOptionsMaxAllocatedStorage', 'StorageRecommendationOptionsOnDemandMonthlyPrice', 'StorageRecommendationOptionsRank', 'StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'StorageRecommendationOptionsSavingsOpportunityPercentage', 'StorageRecommendationOptionsStorageThroughput', 'StorageRecommendationOptionsStorageType', 'Tags', 'UtilizationMetricsAuroraMemoryHealthStateMaximum', 'UtilizationMetricsAuroraMemoryNumDeclinedSqlTotalMaximum', 'UtilizationMetricsAuroraMemoryNumKillConnTotalMaximum', 'UtilizationMetricsAuroraMemoryNumKillQueryTotalMaximum', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDatabaseConnectionsMaximum', 'UtilizationMetricsEBSVolumeReadIOPSMaximum', 'UtilizationMetricsEBSVolumeReadThroughputMaximum', 'UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum', 'UtilizationMetricsEBSVolumeWriteIOPSMaximum', 'UtilizationMetricsEBSVolumeWriteThroughputMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkReceiveThroughputMaximum', 'UtilizationMetricsNetworkTransmitThroughputMaximum', 'UtilizationMetricsReadIOPSEphemeralStorageMaximum', 'UtilizationMetricsStorageNetworkReceiveThroughputMaximum', 'UtilizationMetricsStorageNetworkTransmitThroughputMaximum', 'UtilizationMetricsWriteIOPSEphemeralStorageMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# ExportRDSDatabaseRecommendationsResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.S3Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# ExternalMetricStatus

### statusCode
- **Type**: typing.Optional[typing.Literal['DATADOG_INTEGRATION_ERROR', 'DYNATRACE_INTEGRATION_ERROR', 'INSTANA_INTEGRATION_ERROR', 'INSUFFICIENT_DATADOG_METRICS', 'INSUFFICIENT_DYNATRACE_METRICS', 'INSUFFICIENT_INSTANA_METRICS', 'INSUFFICIENT_NEWRELIC_METRICS', 'INTEGRATION_SUCCESS', 'NEWRELIC_INTEGRATION_ERROR', 'NO_EXTERNAL_METRIC_SET']]

### statusReason
- **Type**: typing.Optional[str]


# ExternalMetricsPreference

### source
- **Type**: typing.Optional[typing.Literal['Datadog', 'Dynatrace', 'Instana', 'NewRelic']]


# Filter

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCodes', 'InferredWorkloadTypes', 'RecommendationSourceType']]

### values
- **Type**: typing.Optional[typing.List[str]]


# GetAutoScalingGroupRecommendationsRequest

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### autoScalingGroupArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Filter]]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# GetAutoScalingGroupRecommendationsResponse

### autoScalingGroupRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AutoScalingGroupRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GetRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEBSVolumeRecommendationsRequest

### volumeArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSFilter]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# GetEBSVolumeRecommendationsResponse

### volumeRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.VolumeRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GetRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEC2InstanceRecommendationsRequest

### instanceArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Filter]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# GetEC2InstanceRecommendationsResponse

### instanceRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.InstanceRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GetRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEC2RecommendationProjectedMetricsRequest

### instanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### stat
- **Type**: typing.Literal['Average', 'Maximum']
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# GetEC2RecommendationProjectedMetricsResponse

### recommendedOptionProjectedMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendedOptionProjectedMetric]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# GetECSServiceRecommendationProjectedMetricsRequest

### serviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### stat
- **Type**: typing.Literal['Average', 'Maximum']
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetECSServiceRecommendationProjectedMetricsResponse

### recommendedOptionProjectedMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceRecommendedOptionProjectedMetric]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# GetECSServiceRecommendationsRequest

### serviceArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceRecommendationFilter]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# GetECSServiceRecommendationsResponse

### ecsServiceRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ECSServiceRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GetRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEffectiveRecommendationPreferencesRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEffectiveRecommendationPreferencesResponse

### enhancedInfrastructureMetrics
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### externalMetricsPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ExternalMetricsPreference'>
- **Required**: Yes

### lookBackPeriod
- **Type**: typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']
- **Required**: Yes

### utilizationPreferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationPreference]
- **Required**: Yes

### preferredResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EffectivePreferredResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnrollmentStatusResponse

### status
- **Type**: typing.Literal['Active', 'Failed', 'Inactive', 'Pending']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### memberAccountsEnrolled
- **Type**: <class 'bool'>
- **Required**: Yes

### lastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### numberOfMemberAccountsOptedIn
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnrollmentStatusesForOrganizationRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EnrollmentFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEnrollmentStatusesForOrganizationRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EnrollmentFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.PaginatorConfig]


# GetEnrollmentStatusesForOrganizationResponse

### accountEnrollmentStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.AccountEnrollmentStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetIdleRecommendationsRequest

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleRecommendationFilter]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### orderBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.OrderBy]


# GetIdleRecommendationsResponse

### idleRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetLambdaFunctionRecommendationsRequest

### functionArns
- **Type**: typing.Optional[typing.List[str]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionRecommendationFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetLambdaFunctionRecommendationsRequestPaginate

### functionArns
- **Type**: typing.Optional[typing.List[str]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionRecommendationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.PaginatorConfig]


# GetLambdaFunctionRecommendationsResponse

### lambdaFunctionRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionRecommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetLicenseRecommendationsRequest

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LicenseRecommendationFilter]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]


# GetLicenseRecommendationsResponse

### licenseRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LicenseRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GetRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRDSDatabaseRecommendationProjectedMetricsRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### stat
- **Type**: typing.Literal['Average', 'Maximum']
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# GetRDSDatabaseRecommendationProjectedMetricsResponse

### recommendedOptionProjectedMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDatabaseRecommendedOptionProjectedMetric]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# GetRDSDatabaseRecommendationsRequest

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBRecommendationFilter]]

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferences]


# GetRDSDatabaseRecommendationsResponse

### rdsDBRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBRecommendation]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GetRecommendationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRecommendationError

### identifier
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# GetRecommendationPreferencesRequest

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Scope]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetRecommendationPreferencesRequestPaginate

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Scope]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.PaginatorConfig]


# GetRecommendationPreferencesResponse

### recommendationPreferencesDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationPreferencesDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRecommendationSummariesRequest

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetRecommendationSummariesRequestPaginate

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.PaginatorConfig]


# GetRecommendationSummariesResponse

### recommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Gpu

### gpuCount
- **Type**: typing.Optional[int]

### gpuMemorySizeInMiB
- **Type**: typing.Optional[int]


# GpuInfo

### gpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Gpu]]


# IdleEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# IdleRecommendation

### resourceArn
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EBSVolume', 'EC2Instance', 'ECSService', 'RDSDBInstance']]

### accountId
- **Type**: typing.Optional[str]

### finding
- **Type**: typing.Optional[typing.Literal['Idle', 'Unattached']]

### findingDescription
- **Type**: typing.Optional[str]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleSavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleSavingsOpportunityAfterDiscounts]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleUtilizationMetric]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]


# IdleRecommendationError

### identifier
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EBSVolume', 'EC2Instance', 'ECSService', 'RDSDBInstance']]


# IdleRecommendationFilter

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'ResourceType']]

### values
- **Type**: typing.Optional[typing.List[str]]


# IdleSavingsOpportunity

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleEstimatedMonthlySavings]


# IdleSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleEstimatedMonthlySavings]


# IdleSummary

### name
- **Type**: typing.Optional[typing.Literal['Idle', 'Unattached']]

### value
- **Type**: typing.Optional[float]


# IdleUtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['CPU', 'DatabaseConnections', 'EBSVolumeReadIOPS', 'EBSVolumeWriteIOPS', 'Memory', 'NetworkInBytesPerSecond', 'NetworkOutBytesPerSecond', 'VolumeReadOpsPerSecond', 'VolumeWriteOpsPerSecond']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# InferredWorkloadSaving

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AmazonEmr', 'ApacheCassandra', 'ApacheHadoop', 'Kafka', 'Memcached', 'Nginx', 'PostgreSql', 'Redis', 'SQLServer']]]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EstimatedMonthlySavings]


# InstanceEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# InstanceRecommendation

### instanceArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### instanceName
- **Type**: typing.Optional[str]

### currentInstanceType
- **Type**: typing.Optional[str]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Overprovisioned', 'Underprovisioned']]

### findingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CPUOverprovisioned', 'CPUUnderprovisioned', 'DiskIOPSOverprovisioned', 'DiskIOPSUnderprovisioned', 'DiskThroughputOverprovisioned', 'DiskThroughputUnderprovisioned', 'EBSIOPSOverprovisioned', 'EBSIOPSUnderprovisioned', 'EBSThroughputOverprovisioned', 'EBSThroughputUnderprovisioned', 'GPUMemoryOverprovisioned', 'GPUMemoryUnderprovisioned', 'GPUOverprovisioned', 'GPUUnderprovisioned', 'MemoryOverprovisioned', 'MemoryUnderprovisioned', 'NetworkBandwidthOverprovisioned', 'NetworkBandwidthUnderprovisioned', 'NetworkPPSOverprovisioned', 'NetworkPPSUnderprovisioned']]]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationMetric]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### recommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.InstanceRecommendationOption]]

### recommendationSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RecommendationSource]]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EffectiveRecommendationPreferences]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AmazonEmr', 'ApacheCassandra', 'ApacheHadoop', 'Kafka', 'Memcached', 'Nginx', 'PostgreSql', 'Redis', 'SQLServer']]]

### instanceState
- **Type**: typing.Optional[typing.Literal['pending', 'running', 'shutting-down', 'stopped', 'stopping', 'terminated']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]

### externalMetricStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ExternalMetricStatus]

### currentInstanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GpuInfo]

### idle
- **Type**: typing.Optional[typing.Literal['False', 'True']]


# InstanceRecommendationOption

### instanceType
- **Type**: typing.Optional[str]

### instanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.GpuInfo]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationMetric]]

### platformDifferences
- **Type**: typing.Optional[typing.List[typing.Literal['Architecture', 'Hypervisor', 'InstanceStoreAvailability', 'NetworkInterface', 'StorageInterface', 'VirtualizationType']]]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.InstanceSavingsOpportunityAfterDiscounts]

### migrationEffort
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]


# InstanceSavingsEstimationMode

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# InstanceSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.InstanceEstimatedMonthlySavings]


# JobFilter

### name
- **Type**: typing.Optional[typing.Literal['JobStatus', 'ResourceType']]

### values
- **Type**: typing.Optional[typing.List[str]]


# LambdaEffectiveRecommendationPreferences

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaSavingsEstimationMode]


# LambdaEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# LambdaFunctionMemoryProjectedMetric

### name
- **Type**: typing.Optional[typing.Literal['Duration']]

### statistic
- **Type**: typing.Optional[typing.Literal['Expected', 'LowerBound', 'UpperBound']]

### value
- **Type**: typing.Optional[float]


# LambdaFunctionMemoryRecommendationOption

### rank
- **Type**: typing.Optional[int]

### memorySize
- **Type**: typing.Optional[int]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionMemoryProjectedMetric]]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaSavingsOpportunityAfterDiscounts]


# LambdaFunctionRecommendation

### functionArn
- **Type**: typing.Optional[str]

### functionVersion
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentMemorySize
- **Type**: typing.Optional[int]

### numberOfInvocations
- **Type**: typing.Optional[int]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionUtilizationMetric]]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Unavailable']]

### findingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['Inconclusive', 'InsufficientData', 'MemoryOverprovisioned', 'MemoryUnderprovisioned']]]

### memorySizeRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaFunctionMemoryRecommendationOption]]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaEffectiveRecommendationPreferences]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]


# LambdaFunctionRecommendationFilter

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCode']]

### values
- **Type**: typing.Optional[typing.List[str]]


# LambdaFunctionUtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['Duration', 'Memory']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# LambdaSavingsEstimationMode

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# LambdaSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LambdaEstimatedMonthlySavings]


# LicenseConfiguration

### numberOfCores
- **Type**: typing.Optional[int]

### instanceType
- **Type**: typing.Optional[str]

### operatingSystem
- **Type**: typing.Optional[str]

### licenseEdition
- **Type**: typing.Optional[typing.Literal['Enterprise', 'Free', 'NoLicenseEditionFound', 'Standard']]

### licenseName
- **Type**: typing.Optional[typing.Literal['SQLServer']]

### licenseModel
- **Type**: typing.Optional[typing.Literal['BringYourOwnLicense', 'LicenseIncluded']]

### licenseVersion
- **Type**: typing.Optional[str]

### metricsSource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.MetricSource]]


# LicenseRecommendation

### resourceArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentLicenseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LicenseConfiguration]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### finding
- **Type**: typing.Optional[typing.Literal['InsufficientMetrics', 'NotOptimized', 'Optimized']]

### findingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CloudWatchApplicationInsightsError', 'InvalidCloudWatchApplicationInsightsSetup', 'LicenseOverprovisioned', 'Optimized']]]

### licenseRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.LicenseRecommendationOption]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]


# LicenseRecommendationFilter

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCode', 'LicenseName']]

### values
- **Type**: typing.Optional[typing.List[str]]


# LicenseRecommendationOption

### rank
- **Type**: typing.Optional[int]

### operatingSystem
- **Type**: typing.Optional[str]

### licenseEdition
- **Type**: typing.Optional[typing.Literal['Enterprise', 'Free', 'NoLicenseEditionFound', 'Standard']]

### licenseModel
- **Type**: typing.Optional[typing.Literal['BringYourOwnLicense', 'LicenseIncluded']]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]


# MemorySizeConfiguration

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]


# MetricSource

### provider
- **Type**: typing.Optional[typing.Literal['CloudWatchApplicationInsights']]

### providerArn
- **Type**: typing.Optional[str]


# OrderBy

### dimension
- **Type**: typing.Optional[typing.Literal['SavingsValue', 'SavingsValueAfterDiscount']]

### order
- **Type**: typing.Optional[typing.Literal['Asc', 'Desc']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PreferredResource

### name
- **Type**: typing.Optional[typing.Literal['Ec2InstanceTypes']]

### includeList
- **Type**: typing.Optional[typing.List[str]]

### excludeList
- **Type**: typing.Optional[typing.List[str]]


# ProjectedMetric

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'DISK_READ_BYTES_PER_SECOND', 'DISK_READ_OPS_PER_SECOND', 'DISK_WRITE_BYTES_PER_SECOND', 'DISK_WRITE_OPS_PER_SECOND', 'EBS_READ_BYTES_PER_SECOND', 'EBS_READ_OPS_PER_SECOND', 'EBS_WRITE_BYTES_PER_SECOND', 'EBS_WRITE_OPS_PER_SECOND', 'GPU_MEMORY_PERCENTAGE', 'GPU_PERCENTAGE', 'Memory', 'NETWORK_IN_BYTES_PER_SECOND', 'NETWORK_OUT_BYTES_PER_SECOND', 'NETWORK_PACKETS_IN_PER_SECOND', 'NETWORK_PACKETS_OUT_PER_SECOND']]

### timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### values
- **Type**: typing.Optional[typing.List[float]]


# PutRecommendationPreferencesRequest

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Scope]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### externalMetricsPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ExternalMetricsPreference]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### utilizationPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationPreference]]

### preferredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.PreferredResource]]

### savingsEstimationMode
- **Type**: typing.Optional[typing.Literal['AfterDiscounts', 'BeforeDiscounts']]


# RDSDBInstanceRecommendationOption

### dbInstanceClass
- **Type**: typing.Optional[str]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBUtilizationMetric]]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSInstanceSavingsOpportunityAfterDiscounts]


# RDSDBRecommendation

### resourceArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### engine
- **Type**: typing.Optional[str]

### engineVersion
- **Type**: typing.Optional[str]

### promotionTier
- **Type**: typing.Optional[int]

### currentDBInstanceClass
- **Type**: typing.Optional[str]

### currentStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.DBStorageConfiguration]

### dbClusterIdentifier
- **Type**: typing.Optional[str]

### idle
- **Type**: typing.Optional[typing.Literal['False', 'True']]

### instanceFinding
- **Type**: typing.Optional[typing.Literal['Optimized', 'Overprovisioned', 'Underprovisioned']]

### storageFinding
- **Type**: typing.Optional[typing.Literal['Optimized', 'Overprovisioned', 'Underprovisioned']]

### instanceFindingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CPUOverprovisioned', 'CPUUnderprovisioned', 'DBClusterWriterUnderprovisioned', 'EBSIOPSOverprovisioned', 'EBSIOPSUnderprovisioned', 'EBSThroughputOverprovisioned', 'EBSThroughputUnderprovisioned', 'InstanceStorageReadIOPSUnderprovisioned', 'InstanceStorageWriteIOPSUnderprovisioned', 'MemoryUnderprovisioned', 'NetworkBandwidthOverprovisioned', 'NetworkBandwidthUnderprovisioned', 'NewEngineVersionAvailable', 'NewGenerationDBInstanceClassAvailable']]]

### currentInstancePerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### storageFindingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['EBSVolumeAllocatedStorageUnderprovisioned', 'EBSVolumeIOPSOverprovisioned', 'EBSVolumeThroughputOverprovisioned', 'EBSVolumeThroughputUnderprovisioned', 'NewGenerationStorageTypeAvailable']]]

### instanceRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBInstanceRecommendationOption]]

### storageRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBStorageRecommendationOption]]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDBUtilizationMetric]]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSEffectiveRecommendationPreferences]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]


# RDSDBRecommendationFilter

### name
- **Type**: typing.Optional[typing.Literal['Idle', 'InstanceFinding', 'InstanceFindingReasonCode', 'StorageFinding', 'StorageFindingReasonCode']]

### values
- **Type**: typing.Optional[typing.List[str]]


# RDSDBStorageRecommendationOption

### storageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.DBStorageConfiguration]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSStorageSavingsOpportunityAfterDiscounts]


# RDSDBUtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['AuroraMemoryHealthState', 'AuroraMemoryNumDeclinedSql', 'AuroraMemoryNumKillConnTotal', 'AuroraMemoryNumKillQueryTotal', 'CPU', 'DatabaseConnections', 'EBSVolumeReadIOPS', 'EBSVolumeReadThroughput', 'EBSVolumeStorageSpaceUtilization', 'EBSVolumeWriteIOPS', 'EBSVolumeWriteThroughput', 'Memory', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'ReadIOPSEphemeralStorage', 'StorageNetworkReceiveThroughput', 'StorageNetworkTransmitThroughput', 'WriteIOPSEphemeralStorage']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]

### value
- **Type**: typing.Optional[float]


# RDSDatabaseProjectedMetric

### name
- **Type**: typing.Optional[typing.Literal['AuroraMemoryHealthState', 'AuroraMemoryNumDeclinedSql', 'AuroraMemoryNumKillConnTotal', 'AuroraMemoryNumKillQueryTotal', 'CPU', 'DatabaseConnections', 'EBSVolumeReadIOPS', 'EBSVolumeReadThroughput', 'EBSVolumeStorageSpaceUtilization', 'EBSVolumeWriteIOPS', 'EBSVolumeWriteThroughput', 'Memory', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'ReadIOPSEphemeralStorage', 'StorageNetworkReceiveThroughput', 'StorageNetworkTransmitThroughput', 'WriteIOPSEphemeralStorage']]

### timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### values
- **Type**: typing.Optional[typing.List[float]]


# RDSDatabaseRecommendedOptionProjectedMetric

### recommendedDBInstanceClass
- **Type**: typing.Optional[str]

### rank
- **Type**: typing.Optional[int]

### projectedMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSDatabaseProjectedMetric]]


# RDSEffectiveRecommendationPreferences

### cpuVendorArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['AWS_ARM64', 'CURRENT']]]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSSavingsEstimationMode]


# RDSInstanceEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# RDSInstanceSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSInstanceEstimatedMonthlySavings]


# RDSSavingsEstimationMode

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# RDSStorageEstimatedMonthlySavings

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# RDSStorageSavingsOpportunityAfterDiscounts

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.RDSStorageEstimatedMonthlySavings]


# ReasonCodeSummary

### name
- **Type**: typing.Optional[typing.Literal['MemoryOverprovisioned', 'MemoryUnderprovisioned']]

### value
- **Type**: typing.Optional[float]


# RecommendationExportJob

### jobId
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ExportDestination]

### resourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']]

### status
- **Type**: typing.Optional[typing.Literal['Complete', 'Failed', 'InProgress', 'Queued']]

### creationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# RecommendationPreferences

### cpuVendorArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['AWS_ARM64', 'CURRENT']]]


# RecommendationPreferencesDetail

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Scope]

### resourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### externalMetricsPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ExternalMetricsPreference]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### utilizationPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.UtilizationPreference]]

### preferredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EffectivePreferredResource]]

### savingsEstimationMode
- **Type**: typing.Optional[typing.Literal['AfterDiscounts', 'BeforeDiscounts']]


# RecommendationSource

### recommendationSourceArn
- **Type**: typing.Optional[str]

### recommendationSourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'LambdaFunction', 'License', 'RdsDBInstance', 'RdsDBInstanceStorage']]


# RecommendationSummary

### summaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Summary]]

### idleSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.IdleSummary]]

### recommendationResourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'LambdaFunction', 'License', 'RdsDBInstance', 'RdsDBInstanceStorage']]

### accountId
- **Type**: typing.Optional[str]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### idleSavingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### aggregatedSavingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### currentPerformanceRiskRatings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.CurrentPerformanceRiskRatings]

### inferredWorkloadSavings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.InferredWorkloadSaving]]


# RecommendedOptionProjectedMetric

### recommendedInstanceType
- **Type**: typing.Optional[str]

### rank
- **Type**: typing.Optional[int]

### projectedMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ProjectedMetric]]


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


# S3Destination

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### metadataKey
- **Type**: typing.Optional[str]


# S3DestinationConfig

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]


# SavingsOpportunity

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EstimatedMonthlySavings]


# Scope

### name
- **Type**: typing.Optional[typing.Literal['AccountId', 'Organization', 'ResourceArn']]

### value
- **Type**: typing.Optional[str]


# ServiceConfiguration

### memory
- **Type**: typing.Optional[int]

### cpu
- **Type**: typing.Optional[int]

### containerConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ContainerConfiguration]]

### autoScalingConfiguration
- **Type**: typing.Optional[typing.Literal['TargetTrackingScalingCpu', 'TargetTrackingScalingMemory']]

### taskDefinitionArn
- **Type**: typing.Optional[str]


# Summary

### name
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Overprovisioned', 'Underprovisioned']]

### value
- **Type**: typing.Optional[float]

### reasonCodeSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ReasonCodeSummary]]


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# UpdateEnrollmentStatusRequest

### status
- **Type**: typing.Literal['Active', 'Failed', 'Inactive', 'Pending']
- **Required**: Yes

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# UpdateEnrollmentStatusResponse

### status
- **Type**: typing.Literal['Active', 'Failed', 'Inactive', 'Pending']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.ResponseMetadata'>
- **Required**: Yes


# UtilizationMetric

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'DISK_READ_BYTES_PER_SECOND', 'DISK_READ_OPS_PER_SECOND', 'DISK_WRITE_BYTES_PER_SECOND', 'DISK_WRITE_OPS_PER_SECOND', 'EBS_READ_BYTES_PER_SECOND', 'EBS_READ_OPS_PER_SECOND', 'EBS_WRITE_BYTES_PER_SECOND', 'EBS_WRITE_OPS_PER_SECOND', 'GPU_MEMORY_PERCENTAGE', 'GPU_PERCENTAGE', 'Memory', 'NETWORK_IN_BYTES_PER_SECOND', 'NETWORK_OUT_BYTES_PER_SECOND', 'NETWORK_PACKETS_IN_PER_SECOND', 'NETWORK_PACKETS_OUT_PER_SECOND']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# UtilizationPreference

### metricName
- **Type**: typing.Optional[typing.Literal['CpuUtilization', 'MemoryUtilization']]

### metricParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.CustomizableMetricParameters]


# VolumeConfiguration

### volumeType
- **Type**: typing.Optional[str]

### volumeSize
- **Type**: typing.Optional[int]

### volumeBaselineIOPS
- **Type**: typing.Optional[int]

### volumeBurstIOPS
- **Type**: typing.Optional[int]

### volumeBaselineThroughput
- **Type**: typing.Optional[int]

### volumeBurstThroughput
- **Type**: typing.Optional[int]

### rootVolume
- **Type**: typing.Optional[bool]


# VolumeRecommendation

### volumeArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.VolumeConfiguration]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized']]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSUtilizationMetric]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### volumeRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.VolumeRecommendationOption]]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSEffectiveRecommendationPreferences]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.Tag]]


# VolumeRecommendationOption

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.VolumeConfiguration]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.SavingsOpportunity]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer.compute_optimizer_classes.EBSSavingsOpportunityAfterDiscounts]


