# Compute Optimizer Classes

# AccountEnrollmentStatusTypeDef

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Failed', 'Inactive', 'Pending']]

### statusReason
- **Type**: typing.Optional[str]

### lastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AutoScalingGroupConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoScalingGroupEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# AutoScalingGroupRecommendationOptionTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.AutoScalingGroupConfigurationTypeDef]

### instanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.GpuInfoTypeDef]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationMetricTypeDef]]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef]

### migrationEffort
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]


# AutoScalingGroupRecommendationTypeDef

### accountId
- **Type**: typing.Optional[str]

### autoScalingGroupArn
- **Type**: typing.Optional[str]

### autoScalingGroupName
- **Type**: typing.Optional[str]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Overprovisioned', 'Underprovisioned']]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationMetricTypeDef]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### currentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.AutoScalingGroupConfigurationTypeDef]

### currentInstanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.GpuInfoTypeDef]

### recommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.AutoScalingGroupRecommendationOptionTypeDef]]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EffectiveRecommendationPreferencesTypeDef]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AmazonEmr', 'ApacheCassandra', 'ApacheHadoop', 'Kafka', 'Memcached', 'Nginx', 'PostgreSql', 'Redis', 'SQLServer']]]


# AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.AutoScalingGroupEstimatedMonthlySavingsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerConfigurationTypeDef

### containerName
- **Type**: typing.Optional[str]

### memorySizeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.MemorySizeConfigurationTypeDef]

### cpu
- **Type**: typing.Optional[int]


# ContainerRecommendationTypeDef

### containerName
- **Type**: typing.Optional[str]

### memorySizeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.MemorySizeConfigurationTypeDef]

### cpu
- **Type**: typing.Optional[int]


# CurrentPerformanceRiskRatingsTypeDef

### high
- **Type**: typing.Optional[int]

### medium
- **Type**: typing.Optional[int]

### low
- **Type**: typing.Optional[int]

### veryLow
- **Type**: typing.Optional[int]


# CustomizableMetricParametersTypeDef

### threshold
- **Type**: typing.Optional[typing.Literal['P90', 'P95', 'P99_5']]

### headroom
- **Type**: typing.Optional[typing.Literal['PERCENT_0', 'PERCENT_10', 'PERCENT_20', 'PERCENT_30']]


# DBStorageConfigurationTypeDef

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


# DeleteRecommendationPreferencesRequestTypeDef

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### recommendationPreferenceNames
- **Type**: typing.Sequence[typing.Literal['EnhancedInfrastructureMetrics', 'ExternalMetricsPreference', 'InferredWorkloadTypes', 'LookBackPeriodPreference', 'PreferredResources', 'UtilizationPreferences']]
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ScopeTypeDef]


# DescribeRecommendationExportJobsRequestPaginateTypeDef

### jobIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.JobFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.PaginatorConfigTypeDef]


# DescribeRecommendationExportJobsRequestTypeDef

### jobIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.JobFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRecommendationExportJobsResponseTypeDef

### recommendationExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationExportJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# EBSEffectiveRecommendationPreferencesTypeDef

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSSavingsEstimationModeTypeDef]


# EBSEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# EBSFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Finding']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# EBSSavingsEstimationModeTypeDef

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# EBSSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSEstimatedMonthlySavingsTypeDef]


# EBSUtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['VolumeReadBytesPerSecond', 'VolumeReadOpsPerSecond', 'VolumeWriteBytesPerSecond', 'VolumeWriteOpsPerSecond']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# ECSEffectiveRecommendationPreferencesTypeDef

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSSavingsEstimationModeTypeDef]


# ECSEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# ECSSavingsEstimationModeTypeDef

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# ECSSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSEstimatedMonthlySavingsTypeDef]


# ECSServiceProjectedMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'Memory']]

### timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### upperBoundValues
- **Type**: typing.Optional[typing.List[float]]

### lowerBoundValues
- **Type**: typing.Optional[typing.List[float]]


# ECSServiceProjectedUtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'Memory']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### lowerBoundValue
- **Type**: typing.Optional[float]

### upperBoundValue
- **Type**: typing.Optional[float]


# ECSServiceRecommendationFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCode']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ECSServiceRecommendationOptionTypeDef

### memory
- **Type**: typing.Optional[int]

### cpu
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSSavingsOpportunityAfterDiscountsTypeDef]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceProjectedUtilizationMetricTypeDef]]

### containerRecommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ContainerRecommendationTypeDef]]


# ECSServiceRecommendationTypeDef

### serviceArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ServiceConfigurationTypeDef]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceUtilizationMetricTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceRecommendationOptionTypeDef]]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSEffectiveRecommendationPreferencesTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]


# ECSServiceRecommendedOptionProjectedMetricTypeDef

### recommendedCpuUnits
- **Type**: typing.Optional[int]

### recommendedMemorySize
- **Type**: typing.Optional[int]

### projectedMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceProjectedMetricTypeDef]]


# ECSServiceUtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'Memory']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# EffectivePreferredResourceTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Ec2InstanceTypes']]

### includeList
- **Type**: typing.Optional[typing.List[str]]

### effectiveIncludeList
- **Type**: typing.Optional[typing.List[str]]

### excludeList
- **Type**: typing.Optional[typing.List[str]]


# EffectiveRecommendationPreferencesTypeDef

### cpuVendorArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['AWS_ARM64', 'CURRENT']]]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### externalMetricsPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ExternalMetricsPreferenceTypeDef]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### utilizationPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationPreferenceTypeDef]]

### preferredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.EffectivePreferredResourceTypeDef]]

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.InstanceSavingsEstimationModeTypeDef]


# EnrollmentFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Status']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# EstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# ExportAutoScalingGroupRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.FilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'AutoScalingGroupArn', 'AutoScalingGroupName', 'CurrentConfigurationAllocationStrategy', 'CurrentConfigurationDesiredCapacity', 'CurrentConfigurationInstanceType', 'CurrentConfigurationMaxSize', 'CurrentConfigurationMinSize', 'CurrentConfigurationMixedInstanceTypes', 'CurrentConfigurationType', 'CurrentInstanceGpuInfo', 'CurrentMemory', 'CurrentNetwork', 'CurrentOnDemandPrice', 'CurrentPerformanceRisk', 'CurrentStandardOneYearNoUpfrontReservedPrice', 'CurrentStandardThreeYearNoUpfrontReservedPrice', 'CurrentStorage', 'CurrentVCpus', 'EffectiveRecommendationPreferencesCpuVendorArchitectures', 'EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics', 'EffectiveRecommendationPreferencesInferredWorkloadTypes', 'EffectiveRecommendationPreferencesLookBackPeriod', 'EffectiveRecommendationPreferencesPreferredResources', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'InferredWorkloadTypes', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsConfigurationAllocationStrategy', 'RecommendationOptionsConfigurationDesiredCapacity', 'RecommendationOptionsConfigurationEstimatedInstanceHourReductionPercentage', 'RecommendationOptionsConfigurationInstanceType', 'RecommendationOptionsConfigurationMaxSize', 'RecommendationOptionsConfigurationMinSize', 'RecommendationOptionsConfigurationMixedInstanceTypes', 'RecommendationOptionsConfigurationType', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsInstanceGpuInfo', 'RecommendationOptionsMemory', 'RecommendationOptionsMigrationEffort', 'RecommendationOptionsNetwork', 'RecommendationOptionsOnDemandPrice', 'RecommendationOptionsPerformanceRisk', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'RecommendationOptionsStandardOneYearNoUpfrontReservedPrice', 'RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice', 'RecommendationOptionsStorage', 'RecommendationOptionsVcpus', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDiskReadBytesPerSecondMaximum', 'UtilizationMetricsDiskReadOpsPerSecondMaximum', 'UtilizationMetricsDiskWriteBytesPerSecondMaximum', 'UtilizationMetricsDiskWriteOpsPerSecondMaximum', 'UtilizationMetricsEbsReadBytesPerSecondMaximum', 'UtilizationMetricsEbsReadOpsPerSecondMaximum', 'UtilizationMetricsEbsWriteBytesPerSecondMaximum', 'UtilizationMetricsEbsWriteOpsPerSecondMaximum', 'UtilizationMetricsGpuMemoryPercentageMaximum', 'UtilizationMetricsGpuPercentageMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkInBytesPerSecondMaximum', 'UtilizationMetricsNetworkOutBytesPerSecondMaximum', 'UtilizationMetricsNetworkPacketsInPerSecondMaximum', 'UtilizationMetricsNetworkPacketsOutPerSecondMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# ExportAutoScalingGroupRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportDestinationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef]


# ExportEBSVolumeRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSFilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'CurrentConfigurationRootVolume', 'CurrentConfigurationVolumeBaselineIOPS', 'CurrentConfigurationVolumeBaselineThroughput', 'CurrentConfigurationVolumeBurstIOPS', 'CurrentConfigurationVolumeBurstThroughput', 'CurrentConfigurationVolumeSize', 'CurrentConfigurationVolumeType', 'CurrentMonthlyPrice', 'CurrentPerformanceRisk', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsConfigurationVolumeBaselineIOPS', 'RecommendationOptionsConfigurationVolumeBaselineThroughput', 'RecommendationOptionsConfigurationVolumeBurstIOPS', 'RecommendationOptionsConfigurationVolumeBurstThroughput', 'RecommendationOptionsConfigurationVolumeSize', 'RecommendationOptionsConfigurationVolumeType', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsMonthlyPrice', 'RecommendationOptionsPerformanceRisk', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'RootVolume', 'Tags', 'UtilizationMetricsVolumeReadBytesPerSecondMaximum', 'UtilizationMetricsVolumeReadOpsPerSecondMaximum', 'UtilizationMetricsVolumeWriteBytesPerSecondMaximum', 'UtilizationMetricsVolumeWriteOpsPerSecondMaximum', 'VolumeArn']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportEBSVolumeRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportEC2InstanceRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.FilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'CurrentInstanceGpuInfo', 'CurrentInstanceType', 'CurrentMemory', 'CurrentNetwork', 'CurrentOnDemandPrice', 'CurrentPerformanceRisk', 'CurrentStandardOneYearNoUpfrontReservedPrice', 'CurrentStandardThreeYearNoUpfrontReservedPrice', 'CurrentStorage', 'CurrentVCpus', 'EffectiveRecommendationPreferencesCpuVendorArchitectures', 'EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics', 'EffectiveRecommendationPreferencesExternalMetricsSource', 'EffectiveRecommendationPreferencesInferredWorkloadTypes', 'EffectiveRecommendationPreferencesLookBackPeriod', 'EffectiveRecommendationPreferencesPreferredResources', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'EffectiveRecommendationPreferencesUtilizationPreferences', 'ExternalMetricStatusCode', 'ExternalMetricStatusReason', 'Finding', 'FindingReasonCodes', 'Idle', 'InferredWorkloadTypes', 'InstanceArn', 'InstanceName', 'InstanceState', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsInstanceGpuInfo', 'RecommendationOptionsInstanceType', 'RecommendationOptionsMemory', 'RecommendationOptionsMigrationEffort', 'RecommendationOptionsNetwork', 'RecommendationOptionsOnDemandPrice', 'RecommendationOptionsPerformanceRisk', 'RecommendationOptionsPlatformDifferences', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'RecommendationOptionsStandardOneYearNoUpfrontReservedPrice', 'RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice', 'RecommendationOptionsStorage', 'RecommendationOptionsVcpus', 'RecommendationsSourcesRecommendationSourceArn', 'RecommendationsSourcesRecommendationSourceType', 'Tags', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDiskReadBytesPerSecondMaximum', 'UtilizationMetricsDiskReadOpsPerSecondMaximum', 'UtilizationMetricsDiskWriteBytesPerSecondMaximum', 'UtilizationMetricsDiskWriteOpsPerSecondMaximum', 'UtilizationMetricsEbsReadBytesPerSecondMaximum', 'UtilizationMetricsEbsReadOpsPerSecondMaximum', 'UtilizationMetricsEbsWriteBytesPerSecondMaximum', 'UtilizationMetricsEbsWriteOpsPerSecondMaximum', 'UtilizationMetricsGpuMemoryPercentageMaximum', 'UtilizationMetricsGpuPercentageMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkInBytesPerSecondMaximum', 'UtilizationMetricsNetworkOutBytesPerSecondMaximum', 'UtilizationMetricsNetworkPacketsInPerSecondMaximum', 'UtilizationMetricsNetworkPacketsOutPerSecondMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# ExportEC2InstanceRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportECSServiceRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceRecommendationFilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'CurrentPerformanceRisk', 'CurrentServiceConfigurationAutoScalingConfiguration', 'CurrentServiceConfigurationCpu', 'CurrentServiceConfigurationMemory', 'CurrentServiceConfigurationTaskDefinitionArn', 'CurrentServiceContainerConfigurations', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'FindingReasonCodes', 'LastRefreshTimestamp', 'LaunchType', 'LookbackPeriodInDays', 'RecommendationOptionsContainerRecommendations', 'RecommendationOptionsCpu', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsMemory', 'RecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'ServiceArn', 'Tags', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsMemoryMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportECSServiceRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportIdleRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleRecommendationFilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'Finding', 'FindingDescription', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'ResourceArn', 'ResourceId', 'ResourceType', 'SavingsOpportunity', 'SavingsOpportunityAfterDiscount', 'Tags', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDatabaseConnectionsMaximum', 'UtilizationMetricsEBSVolumeReadIOPSMaximum', 'UtilizationMetricsEBSVolumeWriteIOPSMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkInBytesPerSecondMaximum', 'UtilizationMetricsNetworkOutBytesPerSecondMaximum', 'UtilizationMetricsVolumeReadOpsPerSecondMaximum', 'UtilizationMetricsVolumeWriteOpsPerSecondMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportIdleRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportLambdaFunctionRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionRecommendationFilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'CurrentConfigurationMemorySize', 'CurrentConfigurationTimeout', 'CurrentCostAverage', 'CurrentCostTotal', 'CurrentPerformanceRisk', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Finding', 'FindingReasonCodes', 'FunctionArn', 'FunctionVersion', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'NumberOfInvocations', 'RecommendationOptionsConfigurationMemorySize', 'RecommendationOptionsCostHigh', 'RecommendationOptionsCostLow', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'RecommendationOptionsProjectedUtilizationMetricsDurationExpected', 'RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound', 'RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound', 'RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'RecommendationOptionsSavingsOpportunityPercentage', 'Tags', 'UtilizationMetricsDurationAverage', 'UtilizationMetricsDurationMaximum', 'UtilizationMetricsMemoryAverage', 'UtilizationMetricsMemoryMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportLambdaFunctionRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportLicenseRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.LicenseRecommendationFilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'CurrentLicenseConfigurationInstanceType', 'CurrentLicenseConfigurationLicenseEdition', 'CurrentLicenseConfigurationLicenseModel', 'CurrentLicenseConfigurationLicenseName', 'CurrentLicenseConfigurationLicenseVersion', 'CurrentLicenseConfigurationMetricsSource', 'CurrentLicenseConfigurationNumberOfCores', 'CurrentLicenseConfigurationOperatingSystem', 'Finding', 'FindingReasonCodes', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'RecommendationOptionsEstimatedMonthlySavingsCurrency', 'RecommendationOptionsEstimatedMonthlySavingsValue', 'RecommendationOptionsLicenseEdition', 'RecommendationOptionsLicenseModel', 'RecommendationOptionsOperatingSystem', 'RecommendationOptionsSavingsOpportunityPercentage', 'ResourceArn', 'Tags']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# ExportLicenseRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportRDSDatabaseRecommendationsRequestTypeDef

### s3DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBRecommendationFilterTypeDef]]

### fieldsToExport
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccountId', 'CurrentDBInstanceClass', 'CurrentInstanceOnDemandHourlyPrice', 'CurrentInstancePerformanceRisk', 'CurrentStorageConfigurationAllocatedStorage', 'CurrentStorageConfigurationIOPS', 'CurrentStorageConfigurationMaxAllocatedStorage', 'CurrentStorageConfigurationStorageThroughput', 'CurrentStorageConfigurationStorageType', 'CurrentStorageOnDemandMonthlyPrice', 'DBClusterIdentifier', 'EffectiveRecommendationPreferencesCpuVendorArchitectures', 'EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics', 'EffectiveRecommendationPreferencesLookBackPeriod', 'EffectiveRecommendationPreferencesSavingsEstimationMode', 'Engine', 'EngineVersion', 'Idle', 'InstanceFinding', 'InstanceFindingReasonCodes', 'InstanceRecommendationOptionsDBInstanceClass', 'InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency', 'InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'InstanceRecommendationOptionsEstimatedMonthlySavingsValue', 'InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'InstanceRecommendationOptionsInstanceOnDemandHourlyPrice', 'InstanceRecommendationOptionsPerformanceRisk', 'InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum', 'InstanceRecommendationOptionsRank', 'InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'InstanceRecommendationOptionsSavingsOpportunityPercentage', 'LastRefreshTimestamp', 'LookbackPeriodInDays', 'MultiAZDBInstance', 'PromotionTier', 'ResourceArn', 'StorageFinding', 'StorageFindingReasonCodes', 'StorageRecommendationOptionsAllocatedStorage', 'StorageRecommendationOptionsEstimatedMonthlySavingsCurrency', 'StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts', 'StorageRecommendationOptionsEstimatedMonthlySavingsValue', 'StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts', 'StorageRecommendationOptionsIOPS', 'StorageRecommendationOptionsMaxAllocatedStorage', 'StorageRecommendationOptionsOnDemandMonthlyPrice', 'StorageRecommendationOptionsRank', 'StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage', 'StorageRecommendationOptionsSavingsOpportunityPercentage', 'StorageRecommendationOptionsStorageThroughput', 'StorageRecommendationOptionsStorageType', 'Tags', 'UtilizationMetricsAuroraMemoryHealthStateMaximum', 'UtilizationMetricsAuroraMemoryNumDeclinedSqlTotalMaximum', 'UtilizationMetricsAuroraMemoryNumKillConnTotalMaximum', 'UtilizationMetricsAuroraMemoryNumKillQueryTotalMaximum', 'UtilizationMetricsCpuMaximum', 'UtilizationMetricsDatabaseConnectionsMaximum', 'UtilizationMetricsEBSVolumeReadIOPSMaximum', 'UtilizationMetricsEBSVolumeReadThroughputMaximum', 'UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum', 'UtilizationMetricsEBSVolumeWriteIOPSMaximum', 'UtilizationMetricsEBSVolumeWriteThroughputMaximum', 'UtilizationMetricsMemoryMaximum', 'UtilizationMetricsNetworkReceiveThroughputMaximum', 'UtilizationMetricsNetworkTransmitThroughputMaximum', 'UtilizationMetricsReadIOPSEphemeralStorageMaximum', 'UtilizationMetricsStorageNetworkReceiveThroughputMaximum', 'UtilizationMetricsStorageNetworkTransmitThroughputMaximum', 'UtilizationMetricsWriteIOPSEphemeralStorageMaximum']]]

### fileFormat
- **Type**: typing.Optional[typing.Literal['Csv']]

### includeMemberAccounts
- **Type**: typing.Optional[bool]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# ExportRDSDatabaseRecommendationsResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.S3DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExternalMetricStatusTypeDef

### statusCode
- **Type**: typing.Optional[typing.Literal['DATADOG_INTEGRATION_ERROR', 'DYNATRACE_INTEGRATION_ERROR', 'INSTANA_INTEGRATION_ERROR', 'INSUFFICIENT_DATADOG_METRICS', 'INSUFFICIENT_DYNATRACE_METRICS', 'INSUFFICIENT_INSTANA_METRICS', 'INSUFFICIENT_NEWRELIC_METRICS', 'INTEGRATION_SUCCESS', 'NEWRELIC_INTEGRATION_ERROR', 'NO_EXTERNAL_METRIC_SET']]

### statusReason
- **Type**: typing.Optional[str]


# ExternalMetricsPreferenceTypeDef

### source
- **Type**: typing.Optional[typing.Literal['Datadog', 'Dynatrace', 'Instana', 'NewRelic']]


# FilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCodes', 'InferredWorkloadTypes', 'RecommendationSourceType']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetAutoScalingGroupRecommendationsRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### autoScalingGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.FilterTypeDef]]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# GetAutoScalingGroupRecommendationsResponseTypeDef

### autoScalingGroupRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.AutoScalingGroupRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GetRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEBSVolumeRecommendationsRequestTypeDef

### volumeArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSFilterTypeDef]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# GetEBSVolumeRecommendationsResponseTypeDef

### volumeRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.VolumeRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GetRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEC2InstanceRecommendationsRequestTypeDef

### instanceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.FilterTypeDef]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# GetEC2InstanceRecommendationsResponseTypeDef

### instanceRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.InstanceRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GetRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEC2RecommendationProjectedMetricsRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.TimestampTypeDef'>
- **Required**: Yes

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# GetEC2RecommendationProjectedMetricsResponseTypeDef

### recommendedOptionProjectedMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendedOptionProjectedMetricTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetECSServiceRecommendationProjectedMetricsRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.TimestampTypeDef'>
- **Required**: Yes


# GetECSServiceRecommendationProjectedMetricsResponseTypeDef

### recommendedOptionProjectedMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceRecommendedOptionProjectedMetricTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetECSServiceRecommendationsRequestTypeDef

### serviceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceRecommendationFilterTypeDef]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# GetECSServiceRecommendationsResponseTypeDef

### ecsServiceRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ECSServiceRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GetRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEffectiveRecommendationPreferencesRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEffectiveRecommendationPreferencesResponseTypeDef

### enhancedInfrastructureMetrics
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### externalMetricsPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ExternalMetricsPreferenceTypeDef'>
- **Required**: Yes

### lookBackPeriod
- **Type**: typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']
- **Required**: Yes

### utilizationPreferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationPreferenceTypeDef]
- **Required**: Yes

### preferredResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.EffectivePreferredResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnrollmentStatusResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.EnrollmentFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.PaginatorConfigTypeDef]


# GetEnrollmentStatusesForOrganizationRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.EnrollmentFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEnrollmentStatusesForOrganizationResponseTypeDef

### accountEnrollmentStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.AccountEnrollmentStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetIdleRecommendationsRequestTypeDef

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleRecommendationFilterTypeDef]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### orderBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.OrderByTypeDef]


# GetIdleRecommendationsResponseTypeDef

### idleRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetLambdaFunctionRecommendationsRequestPaginateTypeDef

### functionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionRecommendationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.PaginatorConfigTypeDef]


# GetLambdaFunctionRecommendationsRequestTypeDef

### functionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionRecommendationFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetLambdaFunctionRecommendationsResponseTypeDef

### lambdaFunctionRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionRecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetLicenseRecommendationsRequestTypeDef

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.LicenseRecommendationFilterTypeDef]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# GetLicenseRecommendationsResponseTypeDef

### licenseRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.LicenseRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GetRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.TimestampTypeDef'>
- **Required**: Yes

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef

### recommendedOptionProjectedMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDatabaseRecommendedOptionProjectedMetricTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRDSDatabaseRecommendationsRequestTypeDef

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBRecommendationFilterTypeDef]]

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### recommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesTypeDef]


# GetRDSDatabaseRecommendationsResponseTypeDef

### rdsDBRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBRecommendationTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GetRecommendationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRecommendationErrorTypeDef

### identifier
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# GetRecommendationPreferencesRequestPaginateTypeDef

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ScopeTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.PaginatorConfigTypeDef]


# GetRecommendationPreferencesRequestTypeDef

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ScopeTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetRecommendationPreferencesResponseTypeDef

### recommendationPreferencesDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationPreferencesDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRecommendationSummariesRequestPaginateTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.PaginatorConfigTypeDef]


# GetRecommendationSummariesRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetRecommendationSummariesResponseTypeDef

### recommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GpuInfoTypeDef

### gpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.GpuTypeDef]]


# GpuTypeDef

### gpuCount
- **Type**: typing.Optional[int]

### gpuMemorySizeInMiB
- **Type**: typing.Optional[int]


# IdleEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# IdleRecommendationErrorTypeDef

### identifier
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EBSVolume', 'EC2Instance', 'ECSService', 'RDSDBInstance']]


# IdleRecommendationFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'ResourceType']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# IdleRecommendationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleSavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleSavingsOpportunityAfterDiscountsTypeDef]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleUtilizationMetricTypeDef]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]


# IdleSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleEstimatedMonthlySavingsTypeDef]


# IdleSavingsOpportunityTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleEstimatedMonthlySavingsTypeDef]


# IdleSummaryTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Idle', 'Unattached']]

### value
- **Type**: typing.Optional[float]


# IdleUtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['CPU', 'DatabaseConnections', 'EBSVolumeReadIOPS', 'EBSVolumeWriteIOPS', 'Memory', 'NetworkInBytesPerSecond', 'NetworkOutBytesPerSecond', 'VolumeReadOpsPerSecond', 'VolumeWriteOpsPerSecond']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# InferredWorkloadSavingTypeDef

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AmazonEmr', 'ApacheCassandra', 'ApacheHadoop', 'Kafka', 'Memcached', 'Nginx', 'PostgreSql', 'Redis', 'SQLServer']]]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EstimatedMonthlySavingsTypeDef]


# InstanceEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# InstanceRecommendationOptionTypeDef

### instanceType
- **Type**: typing.Optional[str]

### instanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.GpuInfoTypeDef]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationMetricTypeDef]]

### platformDifferences
- **Type**: typing.Optional[typing.List[typing.Literal['Architecture', 'Hypervisor', 'InstanceStoreAvailability', 'NetworkInterface', 'StorageInterface', 'VirtualizationType']]]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.InstanceSavingsOpportunityAfterDiscountsTypeDef]

### migrationEffort
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]


# InstanceRecommendationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationMetricTypeDef]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### recommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.InstanceRecommendationOptionTypeDef]]

### recommendationSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RecommendationSourceTypeDef]]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EffectiveRecommendationPreferencesTypeDef]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AmazonEmr', 'ApacheCassandra', 'ApacheHadoop', 'Kafka', 'Memcached', 'Nginx', 'PostgreSql', 'Redis', 'SQLServer']]]

### instanceState
- **Type**: typing.Optional[typing.Literal['pending', 'running', 'shutting-down', 'stopped', 'stopping', 'terminated']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]

### externalMetricStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ExternalMetricStatusTypeDef]

### currentInstanceGpuInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.GpuInfoTypeDef]

### idle
- **Type**: typing.Optional[typing.Literal['False', 'True']]


# InstanceSavingsEstimationModeTypeDef

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# InstanceSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.InstanceEstimatedMonthlySavingsTypeDef]


# JobFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['JobStatus', 'ResourceType']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# LambdaEffectiveRecommendationPreferencesTypeDef

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaSavingsEstimationModeTypeDef]


# LambdaEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# LambdaFunctionMemoryProjectedMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Duration']]

### statistic
- **Type**: typing.Optional[typing.Literal['Expected', 'LowerBound', 'UpperBound']]

### value
- **Type**: typing.Optional[float]


# LambdaFunctionMemoryRecommendationOptionTypeDef

### rank
- **Type**: typing.Optional[int]

### memorySize
- **Type**: typing.Optional[int]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionMemoryProjectedMetricTypeDef]]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaSavingsOpportunityAfterDiscountsTypeDef]


# LambdaFunctionRecommendationFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCode']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# LambdaFunctionRecommendationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionUtilizationMetricTypeDef]]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Unavailable']]

### findingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['Inconclusive', 'InsufficientData', 'MemoryOverprovisioned', 'MemoryUnderprovisioned']]]

### memorySizeRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaFunctionMemoryRecommendationOptionTypeDef]]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaEffectiveRecommendationPreferencesTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]


# LambdaFunctionUtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Duration', 'Memory']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# LambdaSavingsEstimationModeTypeDef

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# LambdaSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.LambdaEstimatedMonthlySavingsTypeDef]


# LicenseConfigurationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.MetricSourceTypeDef]]


# LicenseRecommendationFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Finding', 'FindingReasonCode', 'LicenseName']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# LicenseRecommendationOptionTypeDef

### rank
- **Type**: typing.Optional[int]

### operatingSystem
- **Type**: typing.Optional[str]

### licenseEdition
- **Type**: typing.Optional[typing.Literal['Enterprise', 'Free', 'NoLicenseEditionFound', 'Standard']]

### licenseModel
- **Type**: typing.Optional[typing.Literal['BringYourOwnLicense', 'LicenseIncluded']]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]


# LicenseRecommendationTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentLicenseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.LicenseConfigurationTypeDef]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### finding
- **Type**: typing.Optional[typing.Literal['InsufficientMetrics', 'NotOptimized', 'Optimized']]

### findingReasonCodes
- **Type**: typing.Optional[typing.List[typing.Literal['CloudWatchApplicationInsightsError', 'InvalidCloudWatchApplicationInsightsSetup', 'LicenseOverprovisioned', 'Optimized']]]

### licenseRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.LicenseRecommendationOptionTypeDef]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]


# MemorySizeConfigurationTypeDef

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]


# MetricSourceTypeDef

### provider
- **Type**: typing.Optional[typing.Literal['CloudWatchApplicationInsights']]

### providerArn
- **Type**: typing.Optional[str]


# OrderByTypeDef

### dimension
- **Type**: typing.Optional[typing.Literal['SavingsValue', 'SavingsValueAfterDiscount']]

### order
- **Type**: typing.Optional[typing.Literal['Asc', 'Desc']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PreferredResourceTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Ec2InstanceTypes']]

### includeList
- **Type**: typing.Optional[typing.Sequence[str]]

### excludeList
- **Type**: typing.Optional[typing.Sequence[str]]


# ProjectedMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'DISK_READ_BYTES_PER_SECOND', 'DISK_READ_OPS_PER_SECOND', 'DISK_WRITE_BYTES_PER_SECOND', 'DISK_WRITE_OPS_PER_SECOND', 'EBS_READ_BYTES_PER_SECOND', 'EBS_READ_OPS_PER_SECOND', 'EBS_WRITE_BYTES_PER_SECOND', 'EBS_WRITE_OPS_PER_SECOND', 'GPU_MEMORY_PERCENTAGE', 'GPU_PERCENTAGE', 'Memory', 'NETWORK_IN_BYTES_PER_SECOND', 'NETWORK_OUT_BYTES_PER_SECOND', 'NETWORK_PACKETS_IN_PER_SECOND', 'NETWORK_PACKETS_OUT_PER_SECOND']]

### timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### values
- **Type**: typing.Optional[typing.List[float]]


# PutRecommendationPreferencesRequestTypeDef

### resourceType
- **Type**: typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']
- **Required**: Yes

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ScopeTypeDef]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### externalMetricsPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ExternalMetricsPreferenceTypeDef]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### utilizationPreferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationPreferenceTypeDef]]

### preferredResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.compute_optimizer_classes.PreferredResourceTypeDef]]

### savingsEstimationMode
- **Type**: typing.Optional[typing.Literal['AfterDiscounts', 'BeforeDiscounts']]


# RDSDBInstanceRecommendationOptionTypeDef

### dbInstanceClass
- **Type**: typing.Optional[str]

### projectedUtilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBUtilizationMetricTypeDef]]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSInstanceSavingsOpportunityAfterDiscountsTypeDef]


# RDSDBRecommendationFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Idle', 'InstanceFinding', 'InstanceFindingReasonCode', 'StorageFinding', 'StorageFindingReasonCode']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# RDSDBRecommendationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.DBStorageConfigurationTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBInstanceRecommendationOptionTypeDef]]

### storageRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBStorageRecommendationOptionTypeDef]]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDBUtilizationMetricTypeDef]]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSEffectiveRecommendationPreferencesTypeDef]

### lookbackPeriodInDays
- **Type**: typing.Optional[float]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]


# RDSDBStorageRecommendationOptionTypeDef

### storageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.DBStorageConfigurationTypeDef]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSStorageSavingsOpportunityAfterDiscountsTypeDef]


# RDSDBUtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['AuroraMemoryHealthState', 'AuroraMemoryNumDeclinedSql', 'AuroraMemoryNumKillConnTotal', 'AuroraMemoryNumKillQueryTotal', 'CPU', 'DatabaseConnections', 'EBSVolumeReadIOPS', 'EBSVolumeReadThroughput', 'EBSVolumeStorageSpaceUtilization', 'EBSVolumeWriteIOPS', 'EBSVolumeWriteThroughput', 'Memory', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'ReadIOPSEphemeralStorage', 'StorageNetworkReceiveThroughput', 'StorageNetworkTransmitThroughput', 'WriteIOPSEphemeralStorage']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum']]

### value
- **Type**: typing.Optional[float]


# RDSDatabaseProjectedMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['AuroraMemoryHealthState', 'AuroraMemoryNumDeclinedSql', 'AuroraMemoryNumKillConnTotal', 'AuroraMemoryNumKillQueryTotal', 'CPU', 'DatabaseConnections', 'EBSVolumeReadIOPS', 'EBSVolumeReadThroughput', 'EBSVolumeStorageSpaceUtilization', 'EBSVolumeWriteIOPS', 'EBSVolumeWriteThroughput', 'Memory', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'ReadIOPSEphemeralStorage', 'StorageNetworkReceiveThroughput', 'StorageNetworkTransmitThroughput', 'WriteIOPSEphemeralStorage']]

### timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### values
- **Type**: typing.Optional[typing.List[float]]


# RDSDatabaseRecommendedOptionProjectedMetricTypeDef

### recommendedDBInstanceClass
- **Type**: typing.Optional[str]

### rank
- **Type**: typing.Optional[int]

### projectedMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSDatabaseProjectedMetricTypeDef]]


# RDSEffectiveRecommendationPreferencesTypeDef

### cpuVendorArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['AWS_ARM64', 'CURRENT']]]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### savingsEstimationMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSSavingsEstimationModeTypeDef]


# RDSInstanceEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# RDSInstanceSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSInstanceEstimatedMonthlySavingsTypeDef]


# RDSSavingsEstimationModeTypeDef

### source
- **Type**: typing.Optional[typing.Literal['CostExplorerRightsizing', 'CostOptimizationHub', 'PublicPricing']]


# RDSStorageEstimatedMonthlySavingsTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### value
- **Type**: typing.Optional[float]


# RDSStorageSavingsOpportunityAfterDiscountsTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.RDSStorageEstimatedMonthlySavingsTypeDef]


# ReasonCodeSummaryTypeDef

### name
- **Type**: typing.Optional[typing.Literal['MemoryOverprovisioned', 'MemoryUnderprovisioned']]

### value
- **Type**: typing.Optional[float]


# RecommendationExportJobTypeDef

### jobId
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ExportDestinationTypeDef]

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


# RecommendationPreferencesDetailTypeDef

### scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ScopeTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'Idle', 'LambdaFunction', 'License', 'NotApplicable', 'RdsDBInstance']]

### enhancedInfrastructureMetrics
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### inferredWorkloadTypes
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### externalMetricsPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.ExternalMetricsPreferenceTypeDef]

### lookBackPeriod
- **Type**: typing.Optional[typing.Literal['DAYS_14', 'DAYS_32', 'DAYS_93']]

### utilizationPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.UtilizationPreferenceTypeDef]]

### preferredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.EffectivePreferredResourceTypeDef]]

### savingsEstimationMode
- **Type**: typing.Optional[typing.Literal['AfterDiscounts', 'BeforeDiscounts']]


# RecommendationPreferencesTypeDef

### cpuVendorArchitectures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS_ARM64', 'CURRENT']]]


# RecommendationSourceTypeDef

### recommendationSourceArn
- **Type**: typing.Optional[str]

### recommendationSourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'LambdaFunction', 'License', 'RdsDBInstance', 'RdsDBInstanceStorage']]


# RecommendationSummaryTypeDef

### summaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.SummaryTypeDef]]

### idleSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.IdleSummaryTypeDef]]

### recommendationResourceType
- **Type**: typing.Optional[typing.Literal['AutoScalingGroup', 'EbsVolume', 'Ec2Instance', 'EcsService', 'LambdaFunction', 'License', 'RdsDBInstance', 'RdsDBInstanceStorage']]

### accountId
- **Type**: typing.Optional[str]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### idleSavingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### aggregatedSavingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### currentPerformanceRiskRatings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.CurrentPerformanceRiskRatingsTypeDef]

### inferredWorkloadSavings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.InferredWorkloadSavingTypeDef]]


# RecommendedOptionProjectedMetricTypeDef

### recommendedInstanceType
- **Type**: typing.Optional[str]

### rank
- **Type**: typing.Optional[int]

### projectedMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ProjectedMetricTypeDef]]


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


# S3DestinationConfigTypeDef

### bucket
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]


# S3DestinationTypeDef

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### metadataKey
- **Type**: typing.Optional[str]


# SavingsOpportunityTypeDef

### savingsOpportunityPercentage
- **Type**: typing.Optional[float]

### estimatedMonthlySavings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EstimatedMonthlySavingsTypeDef]


# ScopeTypeDef

### name
- **Type**: typing.Optional[typing.Literal['AccountId', 'Organization', 'ResourceArn']]

### value
- **Type**: typing.Optional[str]


# ServiceConfigurationTypeDef

### memory
- **Type**: typing.Optional[int]

### cpu
- **Type**: typing.Optional[int]

### containerConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ContainerConfigurationTypeDef]]

### autoScalingConfiguration
- **Type**: typing.Optional[typing.Literal['TargetTrackingScalingCpu', 'TargetTrackingScalingMemory']]

### taskDefinitionArn
- **Type**: typing.Optional[str]


# SummaryTypeDef

### name
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized', 'Overprovisioned', 'Underprovisioned']]

### value
- **Type**: typing.Optional[float]

### reasonCodeSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.ReasonCodeSummaryTypeDef]]


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateEnrollmentStatusRequestTypeDef

### status
- **Type**: typing.Literal['Active', 'Failed', 'Inactive', 'Pending']
- **Required**: Yes

### includeMemberAccounts
- **Type**: typing.Optional[bool]


# UpdateEnrollmentStatusResponseTypeDef

### status
- **Type**: typing.Literal['Active', 'Failed', 'Inactive', 'Pending']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.compute_optimizer_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UtilizationMetricTypeDef

### name
- **Type**: typing.Optional[typing.Literal['Cpu', 'DISK_READ_BYTES_PER_SECOND', 'DISK_READ_OPS_PER_SECOND', 'DISK_WRITE_BYTES_PER_SECOND', 'DISK_WRITE_OPS_PER_SECOND', 'EBS_READ_BYTES_PER_SECOND', 'EBS_READ_OPS_PER_SECOND', 'EBS_WRITE_BYTES_PER_SECOND', 'EBS_WRITE_OPS_PER_SECOND', 'GPU_MEMORY_PERCENTAGE', 'GPU_PERCENTAGE', 'Memory', 'NETWORK_IN_BYTES_PER_SECOND', 'NETWORK_OUT_BYTES_PER_SECOND', 'NETWORK_PACKETS_IN_PER_SECOND', 'NETWORK_PACKETS_OUT_PER_SECOND']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum']]

### value
- **Type**: typing.Optional[float]


# UtilizationPreferenceTypeDef

### metricName
- **Type**: typing.Optional[typing.Literal['CpuUtilization', 'MemoryUtilization']]

### metricParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.CustomizableMetricParametersTypeDef]


# VolumeConfigurationTypeDef

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


# VolumeRecommendationOptionTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.VolumeConfigurationTypeDef]

### performanceRisk
- **Type**: typing.Optional[float]

### rank
- **Type**: typing.Optional[int]

### savingsOpportunity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.SavingsOpportunityTypeDef]

### savingsOpportunityAfterDiscounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSSavingsOpportunityAfterDiscountsTypeDef]


# VolumeRecommendationTypeDef

### volumeArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### currentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.VolumeConfigurationTypeDef]

### finding
- **Type**: typing.Optional[typing.Literal['NotOptimized', 'Optimized']]

### utilizationMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSUtilizationMetricTypeDef]]

### lookBackPeriodInDays
- **Type**: typing.Optional[float]

### volumeRecommendationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.VolumeRecommendationOptionTypeDef]]

### lastRefreshTimestamp
- **Type**: typing.Optional[datetime.datetime]

### currentPerformanceRisk
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium', 'VeryLow']]

### effectiveRecommendationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.compute_optimizer_classes.EBSEffectiveRecommendationPreferencesTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.compute_optimizer_classes.TagTypeDef]]


